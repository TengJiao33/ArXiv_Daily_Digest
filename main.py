"""
Research Radar — 研究方向定向雷达
主流程：加载方向配置 → 逐方向 ArXiv 定向采集 → 豆包结构化提取 → JSONL 存储 → 周报生成

设计分工：
  - 豆包（自动、便宜）：每日定向采集 + 结构化提取
  - Claude（按需、强力）：你不定时带进来做深度分析
"""

import os
import yaml
import concurrent.futures
from datetime import datetime, date
from dotenv import load_dotenv

# 确保 .env 从项目根目录加载（而非当前工作目录）
_project_root = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(_project_root, ".env"))

from scraper_arxiv import ArxivScraper
from code_hunter import CodeHunter
from processor import extract_batch
from doubao_client import DoubaoClient
from storage import append_papers
from digest_builder import generate_weekly_digest
from notifier import HubNotifier


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


def run():
    """主流程"""
    print("=" * 55)
    print("🛰️  Research Radar — 研究方向定向雷达")
    print("=" * 55)

    # 1. 加载配置
    config = load_config()
    directions = config.get("directions", {})
    print(f"\n📡 已配置 {len(directions)} 个研究方向:")
    for did, dconf in directions.items():
        print(f"   • {dconf['name']} ({did})")

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

    for direction_id, direction_conf in directions.items():
        name = direction_conf["name"]
        query = direction_conf["arxiv_query"]
        max_papers = direction_conf.get("max_papers", 30)

        print(f"\n{'─' * 55}")
        print(f"📡 [{name}]")
        print(f"{'─' * 55}")

        # 3a. ArXiv 定向搜索
        print(f"\n[1/3] ArXiv 定向搜索...")
        papers = scraper.fetch_papers(query, max_results=max_papers)

        if not papers:
            print(f"[{direction_id}] ⚠️ 未获取到论文，跳过")
            daily_stats[direction_id] = 0
            continue

        # 3b. 代码检查
        print(f"\n[2/3] 检查代码仓库...")
        papers = check_all_code(papers, hunter)
        code_count = sum(1 for p in papers if p.get("has_code"))
        print(f"  → {code_count}/{len(papers)} 篇附带代码")

        # 3c. 豆包结构化提取
        print(f"\n[3/3] 豆包结构化提取...")
        papers = extract_batch(papers, client, delay=1.0)

        # 3d. 存储到 JSONL
        new_count = append_papers(direction_id, papers)
        daily_stats[direction_id] = new_count

    # 4. 打印每日统计
    print(f"\n{'=' * 55}")
    print(f"📊 今日采集统计 ({date.today():%Y-%m-%d})")
    print(f"{'=' * 55}")
    for did, count in daily_stats.items():
        name = directions[did]["name"]
        status = f"{count} 篇新增" if count > 0 else "无新增"
        print(f"  {name}: {status}")

    # 5. 如果是周日，生成周报
    if date.today().weekday() == 6:  # 周日
        print(f"\n📝 今天是周日，生成本周周报...")
        for direction_id, direction_conf in directions.items():
            generate_weekly_digest(direction_id, direction_conf["name"])

        # 可选：推送周报摘要到微信
        try:
            notifier = HubNotifier()
            summary_lines = [f"📡 Research Radar 周报 | {date.today():%m/%d}"]
            for did, count in daily_stats.items():
                name = directions[did]["name"]
                summary_lines.append(f"• {name}: 本周共 {count} 篇")
            notifier.send_all("\n".join(summary_lines), "📡 Research Radar 周报")
        except Exception:
            pass  # 推送失败不影响主流程
    else:
        print(f"\n💡 提示：周报将在每周日自动生成。手动生成请运行:")
        print(f"   python -c \"from digest_builder import *; from storage import *; ...\"")

    print(f"\n🏁 Research Radar 采集完成")


# ─── 工具函数：手动生成周报 ────────────────────────────

def generate_all_digests():
    """手动触发所有方向的周报生成（不需要等到周日）"""
    config = load_config()
    for direction_id, direction_conf in config.get("directions", {}).items():
        generate_weekly_digest(direction_id, direction_conf["name"])


if __name__ == "__main__":
    run()
