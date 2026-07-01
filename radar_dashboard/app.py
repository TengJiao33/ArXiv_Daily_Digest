"""
ArXiv_Daily_Digest local dashboard.

Run:
    python radar_dashboard/app.py
"""

from __future__ import annotations

import json
import os
import re
import sys
from collections import Counter, defaultdict
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from authority_anchors import is_authority_venue, load_authority_anchors

DATA_DIR = ROOT / "data"
CONFIG_PATH = ROOT / "config" / "directions.yaml"
STATIC_DIR = Path(__file__).resolve().parent / "static"


def load_directions():
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    return config.get("directions", {})


def iter_week_dirs():
    directions = load_directions()
    for direction_id in directions:
        direction_dir = DATA_DIR / direction_id
        if not direction_dir.exists():
            continue
        for week_dir in sorted(direction_dir.iterdir()):
            if week_dir.is_dir() and re.match(r"^\d{4}-W\d{2}$", week_dir.name):
                yield direction_id, week_dir.name, week_dir


def load_papers():
    papers = []
    directions = load_directions()
    for direction_id, week, week_dir in iter_week_dirs():
        path = week_dir / "papers.jsonl"
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    paper = json.loads(line)
                except json.JSONDecodeError:
                    continue
                extracted = paper.get("extracted") or {}
                method_family = extracted.get("method_family") or extracted.get("theme", "未分类") or "未分类"
                read_priority = str(extracted.get("read_priority", "low") or "low").lower()
                if read_priority not in {"high", "medium", "low"}:
                    read_priority = "low"
                papers.append(
                    {
                        "id": paper.get("id", ""),
                        "direction_id": direction_id,
                        "direction_name": directions.get(direction_id, {}).get("name", direction_id),
                        "week": week,
                        "title": paper.get("title", ""),
                        "title_zh": extracted.get("title_zh", ""),
                        "authors": paper.get("authors", []),
                        "url": paper.get("url", ""),
                        "pdf_url": paper.get("pdf_url", ""),
                        "category": paper.get("category", ""),
                        "published": paper.get("published", ""),
                        "collected": paper.get("collected", ""),
                        "abstract": paper.get("abstract") or paper.get("summary", ""),
                        "abstract_zh": extracted.get("abstract_zh", ""),
                        "has_code": bool(paper.get("has_code")),
                        "repo_url": paper.get("repo_url", ""),
                        "repo_stars": paper.get("repo_stars", 0),
                        "hf_upvotes": paper.get("hf_upvotes", 0),
                        "citation_count": paper.get("citation_count", 0),
                        "venue": paper.get("venue", ""),
                        "venue_year": paper.get("venue_year", ""),
                        "venue_type": paper.get("venue_type", ""),
                        "venue_url": paper.get("venue_url", ""),
                        "venue_confidence": paper.get("venue_confidence", ""),
                        "venue_source": paper.get("venue_source", ""),
                        "is_authority_venue": is_authority_venue(paper.get("venue", "")),
                        "ingest_source": paper.get("ingest_source", ""),
                        "manual_reason": paper.get("manual_reason", ""),
                        "manual_tags": paper.get("manual_tags", []),
                        "problem": extracted.get("problem", ""),
                        "method": extracted.get("method", ""),
                        "contribution": extracted.get("contribution", ""),
                        "limitations": extracted.get("limitations", ""),
                        "key_finding": extracted.get("key_finding", ""),
                        "theme": extracted.get("theme", "未分类") or "未分类",
                        "method_family": method_family,
                        "agent_setting": extracted.get("agent_setting", ""),
                        "control_mechanism": extracted.get("control_mechanism", ""),
                        "evaluation_environment": extracted.get("evaluation_environment", ""),
                        "evaluation_signal": extracted.get("evaluation_signal", ""),
                        "failure_mode": extracted.get("failure_mode", ""),
                        "reliability_risk": extracted.get("reliability_risk", ""),
                        "industrial_relevance": extracted.get("industrial_relevance", ""),
                        "read_priority": read_priority,
                        "baselines": extracted.get("baselines", []),
                        "datasets": extracted.get("datasets", []),
                    }
                )
    return papers


def latest_week(papers):
    weeks = sorted({p["week"] for p in papers})
    return weeks[-1] if weeks else ""


EVALUATION_GROUPS = [
    ("任务成功率", ["成功", "success", "质量", "准确", "recall", "accuracy", "effective", "pass rate"]),
    ("Agent / 工具执行", ["agent", "工具", "tool", "harness", "skill", "workflow", "执行", "environment"]),
    ("一致性 / 共识", ["一致", "consistency", "consensus", "disagreement", "stability", "稳定", "judge"]),
    ("局部性 / 副作用", ["局部", "locality", "specificity", "副作用", "side effect", "非目标", "无关"]),
    ("泛化 / 鲁棒性", ["泛化", "general", "robust", "鲁棒", "跨", "多语言", "变体"]),
    ("顺序 / 长期稳定", ["顺序", "sequential", "lifelong", "持续", "长期", "稳定", "退化"]),
    ("遗忘-保留权衡", ["遗忘", "保留", "forget", "retain", "unlearning", "utility"]),
    ("事实性 / 规则遵循", ["事实", "factual", "hallucination", "rule", "规则", "污染", "contamination"]),
    ("效率 / 规模", ["效率", "规模", "成本", "速度", "large-scale", "scal"]),
    ("基准 / 代码资源", ["基准", "benchmark", "代码", "开源", "数据集"]),
]


FAILURE_GROUPS = [
    ("工具误用 / 执行失败", ["工具", "tool", "执行", "action", "workflow", "API", "操作", "grounding"]),
    ("不一致与错误共识", ["不一致", "一致", "consistency", "disagreement", "consensus", "majority", "共识"]),
    ("冲突与串扰", ["冲突", "串扰", "干扰", "interference", "conflict", "无关知识"]),
    ("遗忘不彻底 / 可恢复", ["不彻底", "恢复", "relearn", "attack", "绕过", "擦除"]),
    ("幻觉 / 事实性失败", ["幻觉", "hallucination", "事实", "factual", "污染", "contamination", "过时"]),
    ("奖励 / 策略退化", ["奖励", "reward", "policy", "entropy", "collapse", "策略", "塌缩"]),
    ("通用能力下降", ["能力下降", "效用", "utility", "通用", "退化", "损害"]),
    ("顺序编辑退化", ["顺序", "sequential", "持续", "长期", "累积", "稳定"]),
    ("局部性不足 / 副作用", ["局部", "副作用", "side effect", "非目标", "扩散"]),
    ("效率与规模瓶颈", ["成本", "效率", "规模", "大规模", "计算"]),
    ("多模态 / 跨语言迁移失败", ["多模态", "跨语言", "VLM", "视觉", "语言"]),
]


def _group_text_signals(papers, field, rules, limit=6):
    grouped = {label: {"label": label, "count": 0, "example": ""} for label, _ in rules}
    other_examples = []

    for paper in papers:
        text = str(paper.get(field, "") or "").strip()
        if not text or text in {"摘要未提及", "未提及", "提取失败"}:
            continue

        lowered = text.lower()
        matched = False
        for label, keywords in rules:
            if any(keyword.lower() in lowered for keyword in keywords):
                grouped[label]["count"] += 1
                if not grouped[label]["example"]:
                    grouped[label]["example"] = text
                matched = True
        if not matched and len(other_examples) < 3:
            other_examples.append(text)

    rows = [row for row in grouped.values() if row["count"]]
    rows.sort(key=lambda row: row["count"], reverse=True)
    if other_examples:
        rows.append({"label": "其他具体信号", "count": len(other_examples), "example": other_examples[0]})
    return rows[:limit]


def summarize(papers):
    directions = load_directions()
    weeks = sorted({p["week"] for p in papers})
    current_week = latest_week(papers)
    current = [p for p in papers if p["week"] == current_week] if current_week else papers
    unique_current = {
        (p.get("id") or p.get("url") or p.get("title", "").lower())
        for p in current
    }
    current_authority = [
        p for p in current if p.get("is_authority_venue") or is_authority_venue(p.get("venue", ""))
    ]
    unique_current_authority = {
        (p.get("id") or p.get("url") or p.get("title", "").lower())
        for p in current_authority
    }
    authority_anchors = load_authority_anchors(directions=directions)
    anchor_counts = Counter(anchor["direction_id"] for anchor in authority_anchors)

    by_direction = []
    for direction_id, conf in directions.items():
        subset = [p for p in current if p["direction_id"] == direction_id]
        by_direction.append(
            {
                "id": direction_id,
                "name": conf.get("name", direction_id),
                "description": conf.get("description", ""),
                "count": len(subset),
                "code_count": sum(1 for p in subset if p["has_code"]),
                "authority_count": sum(1 for p in subset if p.get("is_authority_venue")),
                "anchor_count": anchor_counts.get(direction_id, 0),
                "themes": Counter(p["theme"] for p in subset).most_common(8),
                "method_families": Counter(p["method_family"] for p in subset).most_common(8),
                "priorities": Counter(p["read_priority"] for p in subset).most_common(),
            }
        )

    trend = []
    for week in weeks:
        row = {"week": week, "total": 0, "directions": {}}
        for direction_id in directions:
            count = sum(1 for p in papers if p["week"] == week and p["direction_id"] == direction_id)
            row["directions"][direction_id] = count
            row["total"] += count
        trend.append(row)

    theme_counts = Counter(p["theme"] for p in current if p["theme"] and p["theme"] != "未分类")
    method_family_counts = Counter(
        p["method_family"] for p in current if p["method_family"] and p["method_family"] != "未分类"
    )
    priority_counts = Counter(p["read_priority"] for p in current)
    venue_counts = Counter(p["venue"] for p in current if p.get("venue"))
    authority_venue_counts = Counter(p["venue"] for p in current_authority if p.get("venue"))
    category_counts = Counter(p["category"] or "unknown" for p in current)
    limitation_counts = Counter()
    failure_mode_counts = Counter()
    evaluation_signal_counts = Counter()
    for paper in current:
        limitation = paper.get("limitations", "").strip()
        if limitation and limitation not in {"摘要未提及", "未提及", "提取失败"}:
            limitation_counts[limitation] += 1
        failure = paper.get("failure_mode", "").strip()
        if failure and failure not in {"摘要未提及", "未提及", "提取失败"}:
            failure_mode_counts[failure] += 1
        signal = paper.get("evaluation_signal", "").strip()
        if signal and signal not in {"摘要未提及", "未提及", "提取失败"}:
            evaluation_signal_counts[signal] += 1
    code_papers = [
        {
            "title": p.get("title", ""),
            "url": p.get("url", ""),
            "repo_url": p.get("repo_url", ""),
            "repo_stars": p.get("repo_stars", 0),
            "direction_name": p.get("direction_name", ""),
        }
        for p in current
        if p.get("has_code")
    ]

    return {
        "current_week": current_week,
        "weeks": weeks,
        "total_papers": len(current),
        "unique_papers": len(unique_current),
        "total_code": sum(1 for p in current if p["has_code"]),
        "total_authority": len(unique_current_authority),
        "authority_anchor_count": len(authority_anchors),
        "authority_anchors": authority_anchors,
        "directions": by_direction,
        "trend": trend,
        "themes": theme_counts.most_common(16),
        "method_families": method_family_counts.most_common(16),
        "priorities": priority_counts.most_common(),
        "venues": venue_counts.most_common(12),
        "authority_venues": authority_venue_counts.most_common(12),
        "categories": category_counts.most_common(10),
        "limitations": limitation_counts.most_common(10),
        "failure_modes": failure_mode_counts.most_common(10),
        "evaluation_signals": evaluation_signal_counts.most_common(10),
        "code_papers": code_papers,
    }


def search_papers(papers, params):
    week = (params.get("week") or [""])[0]
    direction = (params.get("direction") or [""])[0]
    query = ((params.get("q") or [""])[0] or "").strip().lower()
    theme = ((params.get("theme") or [""])[0] or "").strip()

    result = papers
    if week and week != "all":
        result = [p for p in result if p["week"] == week]
    if direction and direction != "all":
        result = [p for p in result if p["direction_id"] == direction]
    if theme and theme != "all":
        result = [p for p in result if p["theme"] == theme or p["method_family"] == theme]
    if query:
        def matches(paper):
            haystack = " ".join(
                str(paper.get(key, ""))
                for key in [
                    "title",
                    "title_zh",
                    "abstract",
                    "abstract_zh",
                    "venue",
                    "manual_reason",
                    "problem",
                    "method",
                    "contribution",
                    "limitations",
                    "key_finding",
                    "theme",
                    "method_family",
                    "agent_setting",
                    "control_mechanism",
                    "evaluation_environment",
                    "evaluation_signal",
                    "failure_mode",
                    "reliability_risk",
                    "industrial_relevance",
                    "category",
                ]
            ).lower()
            return all(term in haystack for term in query.split())

        result = [p for p in result if matches(p)]

    result.sort(key=lambda p: (p["week"], p.get("collected", ""), p["title"]), reverse=True)
    limit = int((params.get("limit") or ["120"])[0])
    return result[:limit]


class RadarHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(STATIC_DIR), **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def send_json(self, payload, status=200):
        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/summary":
            papers = load_papers()
            self.send_json(summarize(papers))
            return
        if parsed.path == "/api/papers":
            papers = load_papers()
            self.send_json({"papers": search_papers(papers, parse_qs(parsed.query))})
            return
        if parsed.path == "/api/themes":
            papers = load_papers()
            params = parse_qs(parsed.query)
            week = (params.get("week") or [latest_week(papers)])[0]
            direction = (params.get("direction") or ["all"])[0]
            subset = papers
            if week != "all":
                subset = [p for p in subset if p["week"] == week]
            if direction != "all":
                subset = [p for p in subset if p["direction_id"] == direction]
            self.send_json({"themes": Counter(p["method_family"] for p in subset).most_common(40)})
            return
        super().do_GET()


def main():
    host = "127.0.0.1"
    port = int(os.environ.get("RADAR_DASHBOARD_PORT", "7860"))
    server = ThreadingHTTPServer((host, port), RadarHandler)
    print(f"ArXiv_Daily_Digest dashboard running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
