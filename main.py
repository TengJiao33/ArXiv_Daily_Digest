"""
ArXiv_Daily_Digest.

Daily pipeline for the Agent Reliability Radar dashboard: load direction config,
collect papers, enrich metadata, extract research signals, persist JSONL records,
and generate weekly artifacts.
"""

import copy
import os
import sys
import yaml
import concurrent.futures
from datetime import date
from dotenv import load_dotenv

# 确保 .env 从项目根目录加载（而非当前工作目录）
_project_root = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_project_root, ".env"))

from scraper_arxiv import ArxivScraper
from code_hunter import CodeHunter
from processor import extract_batch
from doubao_client import DoubaoClient
from storage import append_papers, load_existing_ids, normalize_paper_id
from digest_builder import generate_weekly_digest
from landscape_builder import generate_landscape
from citation_tracker import track_all_seeds
from notifier import HubNotifier
from relevance_filter import filter_relevant_papers
from hf_daily import get_trending_top_n, match_hf_upvotes
from venue_resolver import annotate_venues
from manual_papers import load_manual_papers


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")


def load_config():
    """加载研究方向配置"""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "directions.yaml")
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_all_code(papers, hunter):
    """并行检查所有论文是否有 GitHub 代码"""
    def _check(paper):
        has_code, info = hunter.check_paper(paper)
        paper["has_code"] = has_code
        paper["repo_url"] = info.get("url", "") if has_code else ""
        paper["repo_stars"] = info.get("stars", 0) if has_code else 0
        return paper

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(_check, p) for p in papers]
        results = [f.result() for f in futures]

    return results


ENRICHMENT_CACHE_FIELDS = [
    "has_code",
    "repo_url",
    "repo_stars",
    "hf_upvotes",
    "venue",
    "venue_year",
    "venue_type",
    "venue_url",
    "venue_confidence",
    "venue_source",
    "extracted",
    "extraction_depth",
]


def paper_identity(paper):
    """Return a stable key for reusing expensive enrichment within one run."""
    return normalize_paper_id(paper).lower()


def enrichment_cache_key(paper):
    """Cache expensive extraction per paper and direction because prompts are direction-aware."""
    direction_id = str(paper.get("direction_id", "") or "").strip().lower()
    identity = paper_identity(paper)
    return f"{direction_id}:{identity}" if direction_id else identity


def annotate_direction_context(papers, direction_id, direction_conf):
    """Attach direction metadata used by the structure extraction prompt."""
    for paper in papers:
        paper["direction_id"] = direction_id
        paper["direction_name"] = direction_conf.get("name", direction_id)
        paper["direction_description"] = direction_conf.get("description", "")


def merge_unique_papers(*paper_groups):
    """Merge paper groups in order, keeping the first copy of each paper."""
    merged = []
    seen = set()
    for papers in paper_groups:
        for paper in papers or []:
            key = paper_identity(paper)
            if not key or key in seen:
                continue
            merged.append(paper)
            seen.add(key)
    return merged


def mark_manual_papers(papers, manual_entries):
    """Attach manual injection metadata to fetched arXiv seed papers."""
    entry_by_id = {entry["arxiv_id"].lower(): entry for entry in manual_entries}
    for paper in papers:
        entry = entry_by_id.get(paper_identity(paper))
        if not entry:
            continue
        paper["ingest_source"] = "manual"
        paper["manual_inject"] = True
        paper["manual_reason"] = entry.get("reason", "")
        paper["manual_tags"] = entry.get("tags", [])
    return papers


def apply_cached_enrichment(paper, cached_paper):
    """Copy model/API-derived metadata while preserving this direction's source record."""
    for field in ENRICHMENT_CACHE_FIELDS:
        if field in cached_paper:
            paper[field] = copy.deepcopy(cached_paper[field])

    if not paper.get("citation_count") and cached_paper.get("citation_count"):
        paper["citation_count"] = cached_paper["citation_count"]


def split_cached_papers(papers, enrichment_cache):
    """Apply cached enrichment and return papers that still need external calls."""
    uncached = []
    cached_count = 0
    for paper in papers:
        key = enrichment_cache_key(paper)
        cached_paper = enrichment_cache.get(key)
        if cached_paper:
            apply_cached_enrichment(paper, cached_paper)
            cached_count += 1
        else:
            uncached.append(paper)
    return uncached, cached_count


def remember_enriched_papers(papers, enrichment_cache):
    for paper in papers:
        key = enrichment_cache_key(paper)
        if key and paper.get("extracted"):
            enrichment_cache[key] = copy.deepcopy(paper)


def run():
    """主流程"""
    print("=" * 55)
    print("🛰️  ArXiv_Daily_Digest")
    print("=" * 55)

    # 1. 加载配置
    config = load_config()
    directions = config.get("directions", {})
    manual_papers_by_direction = load_manual_papers(directions=directions)
    print(f"\n📡 已配置 {len(directions)} 个研究方向:")
    for did, dconf in directions.items():
        print(f"   • {dconf['name']} ({did})")
    total_manual = sum(len(entries) for entries in manual_papers_by_direction.values())
    if total_manual:
        print(f"   • 手动注入论文 {total_manual} 篇（不触发引用扩展）")

    # 2. 初始化组件
    scraper = ArxivScraper()
    hunter = CodeHunter(github_token=os.getenv("GITHUB_TOKEN"))

    try:
        client = DoubaoClient()
    except ValueError as e:
        print(f"\n❌ 豆包客户端初始化失败: {e}")
        print("提示：请在 .env 中配置 DOUBAO_API_KEY 和 DOUBAO_ENDPOINT_ID")
        return

    # 3. 逐方向采集 + 提取 + 存储
    daily_stats = {}
    enrichment_cache = {}

    for direction_id, direction_conf in directions.items():
        name = direction_conf["name"]
        query = direction_conf["arxiv_query"]
        max_papers = direction_conf.get("max_papers", 30)

        print(f"\n{'─' * 55}")
        print(f"📡 [{name}]")
        print(f"{'─' * 55}")

        # 3a. ArXiv 定向搜索
        print(f"\n[1/4] ArXiv 定向搜索...")
        papers = scraper.fetch_papers(query, max_results=max_papers)

        # 1b. 手动论文注入：只拉取论文本体，不触发 citation expansion
        manual_entries = manual_papers_by_direction.get(direction_id, [])
        if manual_entries:
            manual_ids = [entry["arxiv_id"] for entry in manual_entries]
            print(f"\n[1b/4] 手动论文注入 ({len(manual_ids)} 篇)...")
            manual_source_papers = scraper.fetch_papers_by_ids(manual_ids)
            manual_source_papers = mark_manual_papers(manual_source_papers, manual_entries)
            if manual_source_papers:
                papers = merge_unique_papers(manual_source_papers, papers)
                print(f"  → 手动论文优先合并后共 {len(papers)} 篇")

        # 3b. 种子论文本体回填 + Semantic Scholar 引用追踪
        seed_papers = direction_conf.get("seed_papers", [])
        if seed_papers:
            print(f"\n[2a/4] ArXiv 种子论文本体回填 ({len(seed_papers)} 篇种子)...")
            seed_source_papers = scraper.fetch_papers_by_ids(seed_papers)
            if seed_source_papers:
                papers = merge_unique_papers(seed_source_papers, papers)
                print(f"  → 种子优先合并后共 {len(papers)} 篇")

            print(f"\n[2b/4] Semantic Scholar 引用追踪 ({len(seed_papers)} 篇种子)...")
            cited_papers = track_all_seeds(seed_papers, delay=1.0)
            # 合并：用 ArXiv ID 去重
            papers = merge_unique_papers(papers, [cp for cp in cited_papers if cp.get("summary")])
            print(f"  → 合并后共 {len(papers)} 篇")
        else:
            print(f"\n[2/4] 无种子论文，跳过引用追踪")

        if not papers:
            print(f"[{direction_id}] ⚠️ 未获取到论文，跳过")
            daily_stats[direction_id] = 0
            continue

        # 按方向做二次过滤，拦截 ArXiv 查询和引用追踪带来的泛领域噪音。
        # 手动注入论文来自人工判断，保留并绕过关键词过滤。
        manual_candidates = [p for p in papers if p.get("manual_inject")]
        auto_candidates = [p for p in papers if not p.get("manual_inject")]
        before_filter = len(auto_candidates)
        filtered_auto, dropped_papers = filter_relevant_papers(auto_candidates, direction_conf)
        papers = merge_unique_papers(manual_candidates, filtered_auto)
        if manual_candidates:
            print(f"  → 手动注入论文保留 {len(manual_candidates)} 篇（跳过相关性过滤）")
        if dropped_papers:
            print(f"  → 方向相关性过滤：保留 {len(papers)} 篇，过滤 {len(dropped_papers)} 篇")
            for p in dropped_papers[:5]:
                print(f"    - 过滤: {p.get('title', '')[:80]}")
            if len(dropped_papers) > 5:
                print(f"    - ... 另有 {len(dropped_papers) - 5} 篇")
        else:
            print(f"  → 方向相关性过滤：{before_filter} 篇全部保留")

        if not papers:
            print(f"[{direction_id}] ⚠️ 过滤后无相关论文，跳过")
            daily_stats[direction_id] = 0
            continue

        # 先过滤掉已经存储过的论文，避免重复调豆包 API
        existing_ids = {str(pid).lower() for pid in load_existing_ids(direction_id)}
        new_papers = [p for p in papers if paper_identity(p) not in existing_ids]
        print(f"  → 去重后 {len(new_papers)} 篇需要处理（已存在 {len(papers) - len(new_papers)} 篇）")

        if len(new_papers) > max_papers:
            manual_new_papers = [p for p in new_papers if p.get("manual_inject")]
            auto_new_papers = [p for p in new_papers if not p.get("manual_inject")]
            auto_limit = max(0, max_papers - len(manual_new_papers))
            print(f"  → 本次自动论文处理上限 {max_papers} 篇，手动注入论文优先且不被截断")
            new_papers = manual_new_papers + auto_new_papers[:auto_limit]

        if not new_papers:
            print(f"[{direction_id}] ℹ️ 全部已存在，跳过")
            daily_stats[direction_id] = 0
            continue

        annotate_direction_context(new_papers, direction_id, direction_conf)
        uncached_papers, cached_count = split_cached_papers(new_papers, enrichment_cache)
        if cached_count:
            print(f"  → 复用本次运行已处理论文 {cached_count} 篇，避免重复调外部 API")

        if uncached_papers:
            # 3c. 代码检查（只对新论文）
            print(f"\n[3/4] 检查代码仓库...")
            uncached_papers = check_all_code(uncached_papers, hunter)
            code_count = sum(1 for p in uncached_papers if p.get("has_code"))
            print(f"  → {code_count}/{len(uncached_papers)} 篇附带代码")

            # 3d. 豆包结构化提取（只对新论文）
            print(f"\n[4/4] 豆包结构化提取...")
            uncached_papers = extract_batch(uncached_papers, client, delay=1.0)

            # 3e. HF Daily Papers upvote 匹配
            match_hf_upvotes(uncached_papers)

            # 3f. Venue 标注：手工锚点优先，Semantic Scholar 补全
            annotate_venues(uncached_papers, use_semantic_scholar=True, delay=0.2)
            remember_enriched_papers(uncached_papers, enrichment_cache)
        else:
            print(f"\n[3/4] 代码检查：全部使用缓存")
            print(f"[4/4] 豆包结构化提取：全部使用缓存")

        # 3g. 存储到 JSONL
        new_count = append_papers(direction_id, new_papers)
        daily_stats[direction_id] = new_count

    # 4. 打印每日统计
    print(f"\n{'=' * 55}")
    print(f"📊 今日采集统计 ({date.today():%Y-%m-%d})")
    print(f"{'=' * 55}")
    for did, count in daily_stats.items():
        name = directions[did]["name"]
        status = f"{count} 篇新增" if count > 0 else "无新增"
        print(f"  {name}: {status}")

    # 5. 每日推送（每天都推，不只周日）
    try:
        notifier = HubNotifier()
        daily_lines = build_daily_push_lines(directions, daily_stats)
        notifier.send_all("\n".join(daily_lines), f"📡 Agent Radar {date.today():%m/%d}")
    except Exception as e:
        print(f"[Push] 每日推送失败（不影响主流程）: {e}")

    # 6. 如果是周日，额外生成周报 + 研究版图
    if date.today().weekday() == 6:  # 周日
        print(f"\n📝 今天是周日，生成本周周报 + 研究版图...")
        for direction_id, direction_conf in directions.items():
            generate_weekly_digest(direction_id, direction_conf["name"])
            generate_landscape(direction_id, direction_conf["name"])
    else:
        print(f"\n💡 提示：周报将在每周日自动生成。")

    print(f"\n🏁 ArXiv_Daily_Digest 采集完成")


def build_daily_push_lines(directions, daily_stats, target_date=None):
    """构建每日推送内容：各方向新增 + HF trending top-5。"""
    if target_date is None:
        target_date = date.today()

    lines = [f"📡 ArXiv_Daily_Digest 每日速报 | {target_date:%m/%d}"]
    lines.append("")

    # 各方向新增统计
    total_new = sum(daily_stats.values())
    lines.append(f"**今日新增 {total_new} 篇**")
    for did, direction_conf in directions.items():
        name = direction_conf["name"]
        count = daily_stats.get(did, 0)
        if count > 0:
            lines.append(f"  • {name}: +{count}")
        else:
            lines.append(f"  • {name}: 无新增")
    lines.append("")

    # HF Daily Papers trending top-5
    lines.append("**🔥 HF 社区今日热门 Top-5**")
    try:
        trending = get_trending_top_n(target_date, n=5, min_upvotes=3)
        if trending:
            for i, p in enumerate(trending, 1):
                title_short = p["title"][:50]
                if len(p["title"]) > 50:
                    title_short += "..."
                lines.append(f"  {i}. [{p['hf_upvotes']}⬆] {title_short}")
        else:
            lines.append("  （今日暂无数据）")
    except Exception:
        lines.append("  （获取失败）")

    return lines

if __name__ == "__main__":
    run()
