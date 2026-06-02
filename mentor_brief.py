"""
Generate a mentor-alignment brief from local radar data.

This script does not call external APIs. It reads config/directions.yaml and
data/{direction}/{week}/papers.jsonl, then writes a compact Markdown brief for
the next discussion with a mentor.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from datetime import date
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
CONFIG_PATH = ROOT / "config" / "directions.yaml"
DEFAULT_OUTPUT_DIR = ROOT / "output" / "mentor_briefs"

PRIORITY_SCORE = {"high": 30, "medium": 15, "low": 0}
RELEVANCE_SCORE = {"high": 12, "medium": 6, "low": 0}
FEASIBILITY_SCORE = {"high": 10, "medium": 5, "low": 0}
COST_PENALTY = {"high": -8, "medium": -3, "low": 3}


def load_directions() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    return config.get("directions", {})


def latest_week_for_active_dirs(directions: dict) -> str:
    weeks = set()
    for direction_id in directions:
        direction_dir = DATA_DIR / direction_id
        if not direction_dir.exists():
            continue
        for child in direction_dir.iterdir():
            if child.is_dir() and child.name[:4].isdigit() and "-W" in child.name:
                weeks.add(child.name)
    if weeks:
        return sorted(weeks)[-1]
    year, week, _ = date.today().isocalendar()
    return f"{year}-W{week:02d}"


def load_week_papers(direction_id: str, week: str) -> list[dict]:
    path = DATA_DIR / direction_id / week / "papers.jsonl"
    papers = []
    if not path.exists():
        return papers
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                papers.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return papers


def clean(value, default=""):
    text = str(value or "").strip()
    if text in {"提取失败", "摘要未提及", "未提及", "暂不明显", "无明显假设"}:
        return default
    return text


def short(value, limit=96, default="—"):
    text = clean(value, default="")
    if not text:
        return default
    return text if len(text) <= limit else text[:limit] + "..."


def normalized_level(value, default="low"):
    level = str(value or default).strip().lower()
    return level if level in {"high", "medium", "low"} else default


def paper_score(paper: dict) -> int:
    ext = paper.get("extracted", {}) or {}
    score = PRIORITY_SCORE[normalized_level(ext.get("read_priority"))]
    score += RELEVANCE_SCORE[normalized_level(ext.get("industrial_relevance"))]
    score += FEASIBILITY_SCORE[normalized_level(ext.get("idea_feasibility"))]
    score += COST_PENALTY[normalized_level(ext.get("compute_cost"), default="medium")]
    if paper.get("has_code"):
        score += 5
    if paper.get("venue"):
        score += 3
    return score


def paper_link(paper: dict, limit=76) -> str:
    title = short(paper.get("title"), limit=limit)
    url = paper.get("url", "")
    return f"[{title}]({url})" if url else title


def summarize_direction(direction_id: str, direction: dict, papers: list[dict], top_n: int) -> list[str]:
    lines = []
    lines.append(f"## {direction.get('name', direction_id)}")
    lines.append("")
    lines.append(direction.get("description", ""))
    lines.append("")

    if not papers:
        lines.append("> 本周暂无本方向数据。GitHub Actions 采集后会自动补齐。")
        lines.append("")
        return lines

    high = sum(1 for p in papers if normalized_level((p.get("extracted") or {}).get("read_priority")) == "high")
    code = sum(1 for p in papers if p.get("has_code"))
    families = Counter(clean((p.get("extracted") or {}).get("method_family"), "未分类") for p in papers)
    lines.append(f"- 本周论文：{len(papers)} 篇；high priority：{high} 篇；带代码：{code} 篇。")
    lines.append(
        "- 主要方法族："
        + "、".join(f"{name}({count})" for name, count in families.most_common(4))
    )
    lines.append("")

    ranked = sorted(papers, key=paper_score, reverse=True)[:top_n]
    lines.append("### 优先阅读")
    lines.append("")
    for index, paper in enumerate(ranked, 1):
        ext = paper.get("extracted", {}) or {}
        tags = [
            f"priority={normalized_level(ext.get('read_priority'))}",
            f"industry={normalized_level(ext.get('industrial_relevance'))}",
            f"feasible={normalized_level(ext.get('idea_feasibility'))}",
            f"cost={normalized_level(ext.get('compute_cost'), default='medium')}",
        ]
        if paper.get("has_code"):
            tags.append("code")
        lines.append(f"{index}. {paper_link(paper)}")
        lines.append(f"   - 标签：{', '.join(tags)}")
        lines.append(f"   - 核心发现：{short(ext.get('key_finding'), 120)}")
        lines.append(f"   - 控制/评测：{short(ext.get('control_mechanism') or ext.get('evaluation_signal'), 120)}")
        lines.append(f"   - 风险：{short(ext.get('reliability_risk') or ext.get('failure_mode'), 120)}")
        lines.append(f"   - Idea：{short(ext.get('idea_hook'), 140)}")
        question = clean(ext.get("mentor_question"))
        if question:
            lines.append(f"   - 想问老师：{question}")
    lines.append("")

    idea_hooks = [
        clean((p.get("extracted") or {}).get("idea_hook"))
        for p in ranked
        if clean((p.get("extracted") or {}).get("idea_hook"))
    ]
    if idea_hooks:
        lines.append("### 可带去讨论的候选切入点")
        lines.append("")
        for hook in idea_hooks[:3]:
            lines.append(f"- {hook}")
        lines.append("")

    return lines


def build_brief(week: str, top_n: int) -> str:
    directions = load_directions()
    lines = []
    lines.append(f"# Mentor Alignment Brief — {week}")
    lines.append("")
    lines.append("目标：把雷达结果压缩成 2-3 个可和导师讨论的候选方向，优先看意义、差异性、可行性和工业相关性。")
    lines.append("")

    for direction_id, direction in directions.items():
        papers = load_week_papers(direction_id, week)
        lines.extend(summarize_direction(direction_id, direction, papers, top_n))

    lines.append("---")
    lines.append(f"*Generated from local ArXiv_Daily_Digest data on {date.today():%Y-%m-%d}. No external API was called.*")
    return "\n".join(lines) + "\n"


def parse_args():
    parser = argparse.ArgumentParser(description="Generate mentor-alignment Markdown from local radar data.")
    parser.add_argument("--week", help="ISO week such as 2026-W23. Defaults to latest active week.")
    parser.add_argument("--top", type=int, default=5, help="Top papers per direction.")
    parser.add_argument("--out", help="Output path. Defaults to output/mentor_briefs/{week}.md.")
    parser.add_argument("--stdout", action="store_true", help="Print the brief instead of writing a file.")
    return parser.parse_args()


def main():
    args = parse_args()
    directions = load_directions()
    week = args.week or latest_week_for_active_dirs(directions)
    brief = build_brief(week, top_n=max(1, args.top))

    if args.stdout:
        print(brief, end="")
        return None

    output_path = Path(args.out) if args.out else DEFAULT_OUTPUT_DIR / f"{week}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(brief, encoding="utf-8")
    print(f"wrote {output_path}")
    return output_path


if __name__ == "__main__":
    main()
