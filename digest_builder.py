"""
Research Radar — 周报生成模块
每周日自动汇总本周各方向的论文数据，生成结构化 Markdown 周报。
周报是 Claude 深度分析时的"入口"——先看周报了解大局，再深入具体论文。
"""

import os
import json
from datetime import date
from collections import Counter


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def generate_weekly_digest(direction_id, direction_name, target_date=None):
    """
    生成某方向的周报 Markdown。
    读取该周的 papers.jsonl，统计趋势，输出 weekly_digest.md。
    """
    if target_date is None:
        target_date = date.today()

    year, week, _ = target_date.isocalendar()
    week_str = f"{year}-W{week:02d}"
    week_dir = os.path.join(DATA_DIR, direction_id, week_str)
    jsonl_path = os.path.join(week_dir, "papers.jsonl")

    # 读取论文
    papers = []
    if os.path.exists(jsonl_path):
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        papers.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue

    if not papers:
        print(f"[Digest] ℹ️ {direction_id} {week_str}: 无论文数据，跳过")
        return None

    # 计算周一和周日日期
    week_start = date.fromisocalendar(year, week, 1)
    week_end = date.fromisocalendar(year, week, 7)

    # ─── 统计 ──────────────────────────────────
    categories = Counter(p.get("category", "unknown") for p in papers)
    code_count = sum(1 for p in papers if p.get("has_code", False))

    # 聚合提取字段
    all_baselines = []
    all_datasets = []
    all_limitations = []

    for p in papers:
        ext = p.get("extracted", {})
        for b in ext.get("baselines", []):
            all_baselines.append(b)
        for d in ext.get("datasets", []):
            all_datasets.append(d)
        lim = ext.get("limitations", "")
        if lim and lim not in ("提取失败", "摘要未提及"):
            all_limitations.append(lim)

    baseline_counts = Counter(all_baselines).most_common(10)
    dataset_counts = Counter(all_datasets).most_common(10)

    # ─── 构建 Markdown ────────────────────────
    lines = []
    lines.append(f"# {direction_name} — {week_str} ({week_start:%m/%d}-{week_end:%m/%d})\n")
    lines.append(f"本周新增 **{len(papers)}** 篇论文。{code_count} 篇附带代码仓库。\n")

    # 数量预警
    if len(papers) < 5:
        lines.append(f"> ⚠️ 本周论文数较少，搜索关键词可能过窄，考虑扩展 arxiv_query\n")
    elif len(papers) > 40:
        lines.append(f"> ⚠️ 本周论文数较多，搜索关键词可能过宽，考虑收紧 arxiv_query\n")

    # 分类分布
    lines.append(f"## 分类分布\n")
    for cat, count in categories.most_common():
        lines.append(f"- `{cat}`: {count} 篇")
    lines.append("")

    # 论文列表
    lines.append(f"## 论文列表\n")
    lines.append(f"| # | 论文 | 核心方法 | 主要贡献 | 代码 |")
    lines.append(f"|:-:|------|---------|---------|:----:|")

    for i, p in enumerate(papers, 1):
        ext = p.get("extracted", {})
        title_short = p["title"][:60]
        if len(p["title"]) > 60:
            title_short += "..."
        title_link = f"[{title_short}]({p.get('url', '')})"
        method = ext.get("method", "—")
        if len(method) > 40:
            method = method[:40] + "..."
        contribution = ext.get("contribution", "—")
        if len(contribution) > 40:
            contribution = contribution[:40] + "..."
        code = "✅" if p.get("has_code") else "—"
        lines.append(f"| {i} | {title_link} | {method} | {contribution} | {code} |")
    lines.append("")

    # 高频 Baselines
    if baseline_counts:
        lines.append(f"## 常见基线方法\n")
        for name, count in baseline_counts:
            lines.append(f"- **{name}** ({count} 篇引用)")
        lines.append("")

    # Limitations（核心价值字段）
    if all_limitations:
        lines.append(f"## 本周提到的 Limitations\n")
        for lim in all_limitations:
            lines.append(f"- {lim}")
        lines.append("")

    # 常用数据集
    if dataset_counts:
        lines.append(f"## 常用数据集\n")
        for name, count in dataset_counts:
            lines.append(f"- **{name}** ({count} 篇使用)")
        lines.append("")

    lines.append(f"\n---\n")
    lines.append(f"*自动生成于 {date.today():%Y-%m-%d} | Research Radar*")

    digest_text = "\n".join(lines)

    # 写入
    os.makedirs(week_dir, exist_ok=True)
    digest_path = os.path.join(week_dir, "weekly_digest.md")
    with open(digest_path, "w", encoding="utf-8") as f:
        f.write(digest_text)

    print(f"[Digest] ✅ {direction_id} {week_str}: 周报已生成 ({len(papers)} 篇)")
    return digest_path
