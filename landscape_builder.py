"""
ArXiv_Daily_Digest — 研究版图生成模块
从每周 JSONL 数据中读取论文的 key_finding、method_family 和 theme 字段，
优先按 method_family 分组，生成一份结构化的"研究版图" landscape.md。

设计原则：
  - 豆包的智能用在单篇提取时（key_finding / method_family / theme），一次写定不改
  - 版图的组织和格式由代码完成，不涉及 AI 重写
  - 每周一份，独立存档，不引用上周——像文件袋一样一周一周的
"""

import os
import json
from datetime import date
from collections import defaultdict


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def generate_landscape(direction_id, direction_name, target_date=None):
    """
    生成某方向某周的研究版图。
    从该周的 papers.jsonl 读取数据，按 theme 分组，输出 landscape.md。
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
        print(f"[Landscape] ℹ️ {direction_id} {week_str}: 无论文数据，跳过")
        return None

    # 计算周一和周日日期
    week_start = date.fromisocalendar(year, week, 1)
    week_end = date.fromisocalendar(year, week, 7)

    # ─── 按 method_family 分组，旧数据 fallback 到 theme ─────────────────
    family_groups = defaultdict(list)

    for p in papers:
        ext = p.get("extracted", {})
        theme = ext.get("theme", "未分类")
        method_family = ext.get("method_family") or theme or "未分类"
        key_finding = ext.get("key_finding", "")

        # 兼容旧数据：如果没有 key_finding，从 contribution 回填
        if not key_finding or key_finding == "提取失败":
            key_finding = ext.get("contribution", "暂无")

        # 兼容旧数据：如果没有 method_family，用 theme；都没有则未分类
        if not method_family or method_family in ("未分类", "提取失败"):
            method_family = theme if theme and theme not in ("提取失败",) else "未分类"

        entry = {
            "title": p.get("title", ""),
            "url": p.get("url", ""),
            "arxiv_id": p.get("id", ""),
            "key_finding": key_finding,
            "method": ext.get("method", ""),
            "theme": theme,
            "evaluation_signal": ext.get("evaluation_signal", ""),
            "failure_mode": ext.get("failure_mode", ""),
            "idea_hook": ext.get("idea_hook", ""),
            "read_priority": ext.get("read_priority", "low"),
            "venue": p.get("venue", ""),
            "venue_year": p.get("venue_year", ""),
            "has_code": p.get("has_code", False),
            "repo_url": p.get("repo_url", ""),
        }
        family_groups[method_family].append(entry)

    # ─── 方法族排序：按论文数量降序，"未分类"放最后 ──────
    sorted_families = sorted(
        family_groups.keys(),
        key=lambda t: (t == "未分类", -len(family_groups[t]))
    )

    # ─── 构建 Markdown ────────────────────────────
    lines = []
    lines.append(f"# 📡 {direction_name} — 方法版图")
    lines.append(f"> {week_str} ({week_start:%m/%d}-{week_end:%m/%d}) | "
                 f"本周 {len(papers)} 篇 | 自动生成\n")

    # 全局统计
    code_count = sum(1 for p in papers if p.get("has_code", False))
    high_count = sum(1 for p in papers if (p.get("extracted", {}) or {}).get("read_priority") == "high")
    lines.append(f"📊 **{len(family_groups)}** 个方法族 | "
                 f"**{high_count}** 篇 high priority | "
                 f"**{code_count}** 篇附带代码\n")
    lines.append("---\n")

    # 按方法族输出
    for family in sorted_families:
        entries = family_groups[family]
        lines.append(f"### 🔬 {family}（{len(entries)} 篇）\n")

        for e in entries:
            title_short = e["title"][:65]
            if len(e["title"]) > 65:
                title_short += "..."

            # 构建论文链接
            if e["url"]:
                paper_ref = f"[{title_short}]({e['url']})"
            else:
                paper_ref = title_short

            # 代码标记
            code_mark = ""
            if e["has_code"] and e["repo_url"]:
                code_mark = f" 💻"

            priority_mark = ""
            if str(e.get("read_priority", "")).lower() == "high":
                priority_mark = " ⭐"

            venue_mark = ""
            if e.get("venue"):
                venue_mark = f" `{e['venue']} {e.get('venue_year', '')}`".strip()

            # 核心发现
            finding = e["key_finding"]
            if len(finding) > 80:
                finding = finding[:80] + "..."

            lines.append(f"- **{finding}**{priority_mark}{code_mark} {venue_mark}".rstrip())
            lines.append(f"  _{paper_ref}_\n")

            signal = e.get("evaluation_signal", "")
            if signal and signal not in ("提取失败", "摘要未提及"):
                lines.append(f"  - 评测信号：{signal}")
            failure = e.get("failure_mode", "")
            if failure and failure not in ("提取失败", "摘要未提及"):
                lines.append(f"  - 失败模式：{failure}")
            hook = e.get("idea_hook", "")
            if hook and hook not in ("提取失败", "暂不明显"):
                lines.append(f"  - Idea hook：{hook}")
            if signal or failure or hook:
                lines.append("")

        lines.append("")

    # 底部
    lines.append("---")
    lines.append(f"*ArXiv_Daily_Digest 自动生成 | {date.today():%Y-%m-%d}*")

    landscape_text = "\n".join(lines)

    # 写入文件
    os.makedirs(week_dir, exist_ok=True)
    landscape_path = os.path.join(week_dir, "landscape.md")
    with open(landscape_path, "w", encoding="utf-8") as f:
        f.write(landscape_text)

    print(f"[Landscape] ✅ {direction_id} {week_str}: "
          f"版图已生成 ({len(papers)} 篇, {len(family_groups)} 个方法族)")
    return landscape_path

