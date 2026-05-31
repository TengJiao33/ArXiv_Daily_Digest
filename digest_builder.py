"""
Knowledge Editing Direction Radar — 周报生成模块
每周日自动汇总本周各方向的论文数据，生成面向读论文排序和选题判断的 Markdown 周报。
"""

import os
import json
from datetime import date
from collections import Counter


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PRIORITY_ORDER = {"high": 0, "medium": 1, "low": 2}


def _short(text, limit=72, default="—"):
    text = str(text or "").strip()
    if not text:
        return default
    return text if len(text) <= limit else text[:limit] + "..."


def _priority(ext):
    value = str(ext.get("read_priority", "low") or "low").strip().lower()
    return value if value in PRIORITY_ORDER else "low"


def _method_family(ext):
    return str(ext.get("method_family") or ext.get("theme") or "未分类").strip() or "未分类"


def _venue_label(paper):
    venue = str(paper.get("venue") or "").strip()
    if not venue:
        return "-"
    year = str(paper.get("venue_year") or "").strip()
    return f"{venue} {year}".strip()


def _load_week_jsonl(jsonl_path):
    papers = []
    if os.path.exists(jsonl_path):
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    papers.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return papers


def generate_weekly_digest(direction_id, direction_name, target_date=None):
    """
    生成某方向的周报 Markdown。
    读取该周的 papers.jsonl，输出 weekly_digest.md。
    """
    if target_date is None:
        target_date = date.today()

    year, week, _ = target_date.isocalendar()
    week_str = f"{year}-W{week:02d}"
    week_dir = os.path.join(DATA_DIR, direction_id, week_str)
    jsonl_path = os.path.join(week_dir, "papers.jsonl")

    papers = _load_week_jsonl(jsonl_path)
    if not papers:
        print(f"[Digest] ℹ️ {direction_id} {week_str}: 无论文数据，跳过")
        return None

    week_start = date.fromisocalendar(year, week, 1)
    week_end = date.fromisocalendar(year, week, 7)

    code_count = sum(1 for p in papers if p.get("has_code", False))
    method_families = Counter()
    priorities = Counter()
    venues = Counter()
    failure_modes = []
    evaluation_signals = []
    idea_hooks = []
    baselines = []
    datasets = []

    for p in papers:
        ext = p.get("extracted", {}) or {}
        method_families[_method_family(ext)] += 1
        priorities[_priority(ext)] += 1
        if p.get("venue"):
            venues[_venue_label(p)] += 1

        failure = str(ext.get("failure_mode", "") or "").strip()
        if failure and failure not in {"提取失败", "摘要未提及"}:
            failure_modes.append(failure)

        signal = str(ext.get("evaluation_signal", "") or "").strip()
        if signal and signal not in {"提取失败", "摘要未提及"}:
            evaluation_signals.append(signal)

        hook = str(ext.get("idea_hook", "") or "").strip()
        if hook and hook not in {"提取失败", "暂不明显"}:
            idea_hooks.append(hook)

        baselines.extend(ext.get("baselines", []) or [])
        datasets.extend(ext.get("datasets", []) or [])

    priority_ranked = sorted(
        papers,
        key=lambda p: (
            PRIORITY_ORDER.get(_priority(p.get("extracted", {}) or {}), 2),
            not bool(p.get("has_code", False)),
            p.get("title", ""),
        ),
    )

    lines = []
    lines.append(f"# {direction_name} — {week_str} ({week_start:%m/%d}-{week_end:%m/%d})\n")
    lines.append(
        f"本周新增 **{len(papers)}** 篇论文，**{code_count}** 篇附带代码。"
        f"优先级：high {priorities.get('high', 0)} / medium {priorities.get('medium', 0)} / low {priorities.get('low', 0)}。\n"
    )

    if len(papers) < 5:
        lines.append("> ⚠️ 本周论文数较少，搜索关键词可能过窄，可考虑扩展 arxiv_query。\n")
    elif len(papers) > 40:
        lines.append("> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。\n")

    lines.append("## 优先阅读\n")
    lines.append("| # | 优先级 | Venue | 论文 | 方法族 | 评测信号 | Idea Hook | 代码 |")
    lines.append("|:-:|:------:|:-----:|------|--------|----------|-----------|:----:|")
    for i, p in enumerate(priority_ranked[:12], 1):
        ext = p.get("extracted", {}) or {}
        title = _short(p.get("title", ""), 64)
        title_link = f"[{title}]({p.get('url', '')})" if p.get("url") else title
        code = "✅" if p.get("has_code") else "—"
        lines.append(
            f"| {i} | {_priority(ext)} | {_venue_label(p)} | {title_link} | {_short(_method_family(ext), 24)} | "
            f"{_short(ext.get('evaluation_signal'), 42)} | {_short(ext.get('idea_hook'), 46)} | {code} |"
        )
    lines.append("")

    if venues:
        lines.append("## A 会 / Venue 标签\n")
        for venue, count in venues.most_common(10):
            lines.append(f"- **{venue}**：{count} 篇")
        lines.append("")

    if method_families:
        lines.append("## 方法族分布\n")
        for family, count in method_families.most_common(12):
            lines.append(f"- **{family}**：{count} 篇")
        lines.append("")

    if failure_modes:
        lines.append("## 失败模式与风险信号\n")
        for failure, count in Counter(failure_modes).most_common(10):
            suffix = f"（{count}）" if count > 1 else ""
            lines.append(f"- {failure}{suffix}")
        lines.append("")

    if evaluation_signals:
        lines.append("## 评测信号\n")
        for signal, count in Counter(evaluation_signals).most_common(10):
            suffix = f"（{count}）" if count > 1 else ""
            lines.append(f"- {signal}{suffix}")
        lines.append("")

    if idea_hooks:
        lines.append("## 可延展 Idea Hook\n")
        for hook in idea_hooks[:12]:
            lines.append(f"- {hook}")
        lines.append("")

    code_papers = [p for p in papers if p.get("has_code")]
    if code_papers:
        lines.append("## 代码资源\n")
        for p in sorted(code_papers, key=lambda item: item.get("repo_stars", 0), reverse=True)[:10]:
            repo = p.get("repo_url") or p.get("url", "")
            stars = p.get("repo_stars", 0)
            stars_text = f" · {stars} stars" if stars else ""
            lines.append(f"- [{_short(p.get('title'), 80)}]({repo}){stars_text}")
        lines.append("")

    baseline_counts = Counter(baselines).most_common(10)
    dataset_counts = Counter(datasets).most_common(10)
    if baseline_counts:
        lines.append("## 常见基线方法\n")
        for name, count in baseline_counts:
            lines.append(f"- **{name}**：{count} 篇")
        lines.append("")
    if dataset_counts:
        lines.append("## 常用数据集\n")
        for name, count in dataset_counts:
            lines.append(f"- **{name}**：{count} 篇")
        lines.append("")

    lines.append("---")
    lines.append(f"*自动生成于 {date.today():%Y-%m-%d} | Knowledge Editing Direction Radar*")

    os.makedirs(week_dir, exist_ok=True)
    digest_path = os.path.join(week_dir, "weekly_digest.md")
    with open(digest_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print(f"[Digest] ✅ {direction_id} {week_str}: 周报已生成 ({len(papers)} 篇)")
    return digest_path
