"""
ArXiv Daily Digest — AI 论文精选日报
主流程：抓取 50 篇 → AI 批量筛选 9 篇 → 代码检查 → Top2 深度摘要 → 分层报告 → 存储 → 推送
"""

import os
import json
import concurrent.futures
import io
import requests
import PyPDF2
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

from scraper_arxiv import ArxivScraper
from code_hunter import CodeHunter
from doubao_client import DoubaoClient
from notifier import HubNotifier
from storage import save_run_data


# ─── 领域分类映射 ──────────────────────────────────────────
CATEGORY_MAP = {
    "cs.CL": "计算语言学",
    "cs.AI": "人工智能",
    "cs.LG": "机器学习",
    "cs.CV": "计算机视觉",
    "cs.RO": "机器人",
    "cs.SE": "软件工程",
    "cs.CR": "加密与安全",
    "cs.NE": "神经与进化计算",
    "stat.ML": "统计学习",
}

def get_category_name(cat_code):
    """获取分类中文名"""
    primary = cat_code.split(".")[0] + "." + cat_code.split(".")[1] if "." in cat_code else cat_code
    cn = CATEGORY_MAP.get(primary, "")
    if cn:
        return f"{cat_code} ({cn})"
    return cat_code


# ─── AI 批量筛选提示词 ───────────────────────────────────────

SELECTION_SYSTEM = """你是一位资深 AI 研究顾问，每天帮助开发者从海量 ArXiv 论文中挑选最值得关注的研究。
你的判断标准：创新性、实用性、对工业界的影响力、研究方向的前沿程度。
你对 LLM、Agent、RAG、多模态、推理、对齐等热门方向有深入理解。"""

SELECTION_PROMPT = """以下是今天 ArXiv 上的 {count} 篇 AI 相关新论文。
请从中精选出 **最值得关注的 9 篇**，按推荐程度排序（最推荐的排第一）。

论文列表：
{papers_text}

请严格按以下 JSON 格式返回（不要返回任何其他内容）：
```json
[
  {{"index": 0, "reason": "推荐理由（中文，50-80字，详细说明解决了什么问题，核心创新点）"}},
  {{"index": 1, "reason": "推荐理由..."}},
  ...
]
```

注意：
- index 是论文在上面列表中的编号（从 0 开始）
- 返回恰好 9 个
- reason 用中文，详细概括推荐理由，50-80字
- 优先选择：有突破性创新的、解决实际痛点的、可能引领新方向的"""


# ─── AI 深度摘要提示词 ────────────────────────────────────

DEEP_SUMMARY_SYSTEM = """你是一位专业的 AI 研究员，擅长将学术论文转化为通俗易懂的中文技术解读。
你的读者是有技术背景的开发者，想快速了解论文的核心贡献。
输出风格：信息密度高、有洞察力、不说废话。"""



DEEP_SUMMARY_PROMPT = """请为以下 ArXiv 论文撰写一段深度技术解读。

---
标题: {title}
作者: {authors}
分类: {category}
{code_info}

论文全文内容 (已提取文本):
{full_text}
---

请按以下格式输出（严格遵守格式）：

**中文标题**: （翻译题目）

**背景与痛点**: （该研究针对什么问题？现有方法有何缺陷？100字左右）

**核心创新**: （核心思想是什么？相比现有技术有何独特之处？100字左右）

**技术细节**: （具体是如何实现的？模型架构、算法流程、关键技术点。150字左右，越详细越好）

**实验结果**: （在什么数据集上测试？性能提升多少？有无关键结论？50-100字）

注意：
- 深度解读，不要泛泛而谈，总字数 400-600 字
- 用中文输出
- 禁止使用 LaTeX 公式（手机端无法渲染），所有数学公式请用纯文本描述（如：平方根、求和、y=f(x) 等）
- 保持专业性，结构清晰，不要使用 Markdown 标题（# ## 等），使用加粗标注小标题"""


# ─── 阶段一：AI 批量筛选 ──────────────────────────────────

def ai_select_papers(papers, client):
    """
    将所有论文标题+摘要打包发给 AI，让它挑选最值得关注的 13 篇。
    只需 1 次 API 调用。
    返回: (selected_papers, usage)
    """
    # 构建论文列表文本
    paper_lines = []
    for i, p in enumerate(papers):
        # 只取摘要前 200 字节省 token
        abstract_short = p["summary"][:200]
        paper_lines.append(f"[{i}] 【{p['category']}】{p['title']}\n    摘要: {abstract_short}...")

    papers_text = "\n\n".join(paper_lines)

    prompt = SELECTION_PROMPT.format(count=len(papers), papers_text=papers_text)

    print(f"[AI 筛选] 正在从 {len(papers)} 篇中挑选 9 篇...")
    response, usage = client.chat_completion(
        messages=[{"role": "user", "content": prompt}],
        system_prompt=SELECTION_SYSTEM,
        max_tokens=1024,
    )

    if not response:
        print("[AI 筛选] ❌ AI 调用失败，随机取前 9 篇作为兜底")
        return papers[:9], usage

    # 解析 JSON 响应
    try:
        # 清理可能的 markdown 代码块包裹
        clean = response.strip()
        if clean.startswith("```"):
            clean = clean.split("\n", 1)[1]  # 去掉第一行 ```json
            clean = clean.rsplit("```", 1)[0]  # 去掉最后的 ```

        selections = json.loads(clean)
        selected = []
        seen_indices = set()

        for item in selections:
            idx = item.get("index", -1)
            if 0 <= idx < len(papers) and idx not in seen_indices:
                seen_indices.add(idx)
                paper = dict(papers[idx])
                paper["one_liner"] = item.get("reason", "")
                selected.append(paper)

        if len(selected) < 9:
            print(f"[AI 筛选] ⚠️ 只解析到 {len(selected)} 篇，补充到 9 篇")
            for i, p in enumerate(papers):
                if i not in seen_indices and len(selected) < 9:
                    paper = dict(p)
                    paper["one_liner"] = "AI 未提供推荐理由"
                    selected.append(paper)

        print(f"[AI 筛选] ✅ 精选 {len(selected)} 篇论文")
        return selected, usage

    except (json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"[AI 筛选] ⚠️ JSON 解析失败: {e}，使用前 9 篇")
        fallback = []
        for p in papers[:9]:
            paper = dict(p)
            paper["one_liner"] = "AI 解析异常"
            fallback.append(paper)
        return fallback, usage


# ─── 阶段二：代码检查 + 深度摘要 ─────────────────────────

def check_all_code(papers, hunter):
    """并行检查所有论文是否有 GitHub 代码"""
    print(f"[代码检查] 检查 {len(papers)} 篇论文的代码仓库...")

    def _check(paper):
        has_code, info = hunter.check_paper(paper)
        paper["has_code"] = has_code
        paper["repo_url"] = info.get("url", "") if has_code else ""
        paper["repo_stars"] = info.get("stars", 0) if has_code else 0
        return paper

    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        futures = [executor.submit(_check, p) for p in papers]
        results = [f.result() for f in futures]

    code_count = sum(1 for p in results if p["has_code"])
    print(f"[代码检查] ✅ {code_count}/{len(results)} 篇论文附带代码仓库")
    return results


def extract_full_text(pdf_url):
    """下载 PDF 并提取全文"""
    print(f"[PDF 下载] 正在获取: {pdf_url}")
    try:
        # 伪装 User-Agent 防止被拦截
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        # 将 arxiv.org 替换为 export.arxiv.org 可能更稳定，或者使用国内镜像
        # 这里先尝试直接下载，超时设置稍长
        response = requests.get(pdf_url, headers=headers, timeout=30)
        response.raise_for_status()

        with io.BytesIO(response.content) as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
            
            # 简单清洗
            text = text.strip()
            if len(text) < 500:
                print(f"[PDF 解析] ⚠️ 提取文本过短 ({len(text)} 字符)，可能解析失败")
                return None
            
            print(f"[PDF 解析] ✅ 成功提取 {len(text)} 字符")
            return text

    except Exception as e:
        print(f"[PDF 下下载/解析] ❌ 失败: {e}")
        return None


def generate_deep_summaries(top_papers, client):
    """对 Top 2 论文生成深度 AI 摘要"""
    total_usage = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0, "api_calls": 0}

    for p in top_papers:
        # 构建代码信息
        if p.get("has_code"):
            code_info = f"GitHub 代码: {p['repo_url']} (⭐ {p['repo_stars']})"
        else:
            code_info = "GitHub 代码: 暂无公开代码"


        # 尝试提取全文
        full_text = None
        if p.get("pdf_url"):
            full_text = extract_full_text(p["pdf_url"])
        
        # 如果提取失败，回退到摘要
        if not full_text:
            content_input = f"摘要 (英文):\n{p['summary']}"
            print(f"[深度摘要] ⚠️ 使用摘要回退模式")
        else:
            # 限制最大长度防止超长 (Doubao 32k/128k, 设置 10w 字符一般安全)
            if len(full_text) > 100000:
                full_text = full_text[:100000] + "\n...(后文截断)"
            content_input = full_text

        prompt = DEEP_SUMMARY_PROMPT.format(
            title=p["title"],
            authors=", ".join(p.get("authors", [])[:5]),
            category=get_category_name(p.get("category", "")),
            code_info=code_info,
            full_text=content_input,
        )

        try:
            response, usage = client.chat_completion(
                messages=[{"role": "user", "content": prompt}],
                system_prompt=DEEP_SUMMARY_SYSTEM,
                max_tokens=600,
            )
            if response:
                p["deep_summary"] = response
                print(f"[深度摘要] ✅ {p['title'][:40]}...")
                if usage:
                    total_usage["prompt_tokens"] += usage.get("prompt_tokens", 0)
                    total_usage["completion_tokens"] += usage.get("completion_tokens", 0)
                    total_usage["total_tokens"] += usage.get("total_tokens", 0)
                    total_usage["api_calls"] += 1
            else:
                p["deep_summary"] = f"_AI 偷懒了，请点击原链接查看 👉 [论文]({p['url']})_"
        except Exception as e:
            print(f"[深度摘要] ❌ {p['title'][:30]}... 失败: {e}")
            p["deep_summary"] = f"_AI 偷懒了，请点击原链接查看 👉 [论文]({p['url']})_"

    return total_usage


# ─── 报告组装 ──────────────────────────────────────────────

def _code_badge(paper):
    """生成代码徽章"""
    if paper.get("has_code"):
        stars = paper.get("repo_stars", 0)
        url = paper.get("repo_url", "")
        return f"✅ [代码]({url}) ⭐{stars}"
    return "⚠️ 暂无代码"


def build_report(selected_papers, usage_select, usage_deep, total_scanned):
    """组装分层 Markdown 报告：Top 2 深度解读 + 7 篇速览表格"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    weekday_map = {0: "周一", 1: "周二", 2: "周三", 3: "周四", 4: "周五", 5: "周六", 6: "周日"}
    weekday = weekday_map[datetime.now().weekday()]

    # 合并用量
    total_tokens = (usage_select.get("total_tokens", 0) + usage_deep.get("total_tokens", 0))
    total_calls = (usage_select.get("api_calls", 0) + usage_deep.get("api_calls", 0))

    lines = []
    lines.append(f"# 🧪 ArXiv AI 日报\n")
    lines.append(f"📅 **{date_str} {weekday}** | 🤖 扫描/精选: **{total_scanned}/{len(selected_papers)}**\n")

    if total_tokens:
        prompt_t = usage_select.get("prompt_tokens", 0) + usage_deep.get("prompt_tokens", 0)
        comp_t = usage_select.get("completion_tokens", 0) + usage_deep.get("completion_tokens", 0)
        cost = prompt_t / 1_000_000 * 0.3 + comp_t / 1_000_000 * 0.6
        lines.append(f"> 📊 Tokens: **{total_tokens:,}** (¥{cost:.4f})\n")

    # ─── 今日必读 (Top 2) ─────────────────────────
    top_papers = selected_papers[:2]
    rest_papers = selected_papers[2:]

    lines.append(f"## 🔥 今日必读\n")

    for i, p in enumerate(top_papers, 1):
        lines.append(f"---\n")
        lines.append(f"### {i}. {p['title']}\n")
        
        # 顶部角标行
        meta_parts = []
        cat_display = get_category_name(p.get('category', ''))
        meta_parts.append(f"🏷️ `{cat_display}`")
        meta_parts.append(f"📄 [arXiv]({p['url']})")
        
        if p.get("has_code"):
             meta_parts.append(f"💻 [GitHub]({p.get('repo_url', '')}) ⭐{p.get('repo_stars', 0)}")
        
        lines.append(f"{' | '.join(meta_parts)}\n")

        authors = p.get("authors", [])
        if authors:
            author_str = ", ".join(authors[:3])
            if len(authors) > 3:
                author_str += f" 等"
            lines.append(f"👤 {author_str}\n")

        if p.get("deep_summary"):
            lines.append(f"\n{p['deep_summary']}\n")
        elif p.get("one_liner"):
             # AI 生成深度摘要失败时的兜底
            lines.append(f"\n> 💬 {p['one_liner']}\n")

    # ─── 同样值得关注 (表格速览) ──────────────────
    # ─── 同样值得关注 (表格速览) ──────────────────
    if rest_papers:
        lines.append(f"\n---\n")
        lines.append(f"## 📋 同样值得关注\n")
        lines.append(f"| # | 论文 | 推荐理由 |")
        lines.append(f"|:-:|---|---|")

        for i, p in enumerate(rest_papers, 4):
            title_short = p["title"][:80] # 稍微长一点
            if len(p["title"]) > 80:
                title_short += "..."
            
            title_link = f"[{title_short}]({p['url']})"
            
            # 如果有代码，在标题后加标识
            if p.get("has_code"):
                title_link += f" 💻"

            reason = p.get("one_liner", "")
            cat_display = get_category_name(p.get('category', ''))
            lines.append(f"| {i} | {title_link} `{cat_display}` | {reason} |")

    # ─── 页脚 ─────────────────────────────────────
    lines.append(f"\n---\n")
    lines.append(f"🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | {date_str}\n")

    return "\n".join(lines)


# ─── 主流程 ────────────────────────────────────────────────

def run():
    """主流程"""
    print("=" * 55)
    print("🧪 ArXiv Daily Digest — AI 论文精选日报")
    print("=" * 55)

    # 1. 抓取论文
    print("\n[1/5] 抓取 ArXiv 最新论文...")
    scraper = ArxivScraper(max_results=50)
    papers = scraper.fetch_papers()
    if not papers:
        print("❌ 未获取到任何论文，流程终止")
        return
    total_scanned = len(papers)

    # 2. AI 批量筛选
    print(f"\n[2/5] AI 从 {total_scanned} 篇中精选 9 篇...")
    try:
        client = DoubaoClient()
    except ValueError as e:
        print(f"❌ AI 客户端初始化失败: {e}")
        return

    selected, usage_select = ai_select_papers(papers, client)
    usage_select["api_calls"] = 1

    # 3. 并行检查代码仓库
    print(f"\n[3/5] 检查代码仓库...")
    hunter = CodeHunter(github_token=os.getenv("GITHUB_TOKEN"))
    selected = check_all_code(selected, hunter)

    # 4. Top 2 深度摘要
    print(f"\n[4/5] 为 Top 2 生成深度摘要...")
    usage_deep = generate_deep_summaries(selected[:2], client)

    # 打印用量统计
    total_tokens = usage_select.get("total_tokens", 0) + usage_deep.get("total_tokens", 0)
    total_calls = 1 + usage_deep.get("api_calls", 0)
    if total_tokens:
        print(f"\n[API 用量] 调用 {total_calls} 次 | 合计 {total_tokens:,} tokens")

    # 5. 组装报告 + 存储 + 推送
    print(f"\n[5/5] 组装报告 → 存储 → 推送...")
    report = build_report(selected, usage_select, usage_deep, total_scanned)

    # 打印报告预览
    print("\n" + "=" * 55)
    print("📋 报告预览:")
    print("=" * 55)
    print(report)
    print("=" * 55)

    save_run_data(selected, report, total_scanned)

    title = f"🧪 {datetime.now().strftime('%m-%d')} ArXiv AI 日报"
    notifier = HubNotifier()
    success = notifier.send_all(report, title)

    if success:
        print("\n✅ 推送成功！")
    else:
        print("\n⚠️ 推送失败或无可用渠道，请检查 .env 配置")

    print("\n🏁 ArXiv Daily Digest 流程完成")


if __name__ == "__main__":
    run()
