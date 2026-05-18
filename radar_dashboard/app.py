"""
Research Radar local dashboard.

Run:
    python radar_dashboard/app.py
"""

from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
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
                papers.append(
                    {
                        "id": paper.get("id", ""),
                        "direction_id": direction_id,
                        "direction_name": directions.get(direction_id, {}).get("name", direction_id),
                        "week": week,
                        "title": paper.get("title", ""),
                        "authors": paper.get("authors", []),
                        "url": paper.get("url", ""),
                        "pdf_url": paper.get("pdf_url", ""),
                        "category": paper.get("category", ""),
                        "published": paper.get("published", ""),
                        "collected": paper.get("collected", ""),
                        "abstract": paper.get("abstract") or paper.get("summary", ""),
                        "has_code": bool(paper.get("has_code")),
                        "repo_url": paper.get("repo_url", ""),
                        "repo_stars": paper.get("repo_stars", 0),
                        "problem": extracted.get("problem", ""),
                        "method": extracted.get("method", ""),
                        "contribution": extracted.get("contribution", ""),
                        "limitations": extracted.get("limitations", ""),
                        "key_finding": extracted.get("key_finding", ""),
                        "theme": extracted.get("theme", "未分类") or "未分类",
                        "baselines": extracted.get("baselines", []),
                        "datasets": extracted.get("datasets", []),
                    }
                )
    return papers


def latest_week(papers):
    weeks = sorted({p["week"] for p in papers})
    return weeks[-1] if weeks else ""


def summarize(papers):
    directions = load_directions()
    weeks = sorted({p["week"] for p in papers})
    current_week = latest_week(papers)
    current = [p for p in papers if p["week"] == current_week] if current_week else papers

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
                "themes": Counter(p["theme"] for p in subset).most_common(8),
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
    category_counts = Counter(p["category"] or "unknown" for p in current)
    limitation_counts = Counter()
    for paper in current:
        limitation = paper.get("limitations", "").strip()
        if limitation and limitation not in {"摘要未提及", "未提及", "提取失败"}:
            limitation_counts[limitation] += 1

    code_papers = [
        {
            "title": p["title"],
            "url": p["url"],
            "repo_url": p["repo_url"],
            "repo_stars": p["repo_stars"],
            "direction_name": p["direction_name"],
        }
        for p in current
        if p["has_code"]
    ]

    return {
        "current_week": current_week,
        "weeks": weeks,
        "total_papers": len(current),
        "total_code": sum(1 for p in current if p["has_code"]),
        "directions": by_direction,
        "trend": trend,
        "themes": theme_counts.most_common(16),
        "categories": category_counts.most_common(10),
        "limitations": limitation_counts.most_common(10),
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
        result = [p for p in result if p["theme"] == theme]
    if query:
        def matches(paper):
            haystack = " ".join(
                str(paper.get(key, ""))
                for key in [
                    "title",
                    "abstract",
                    "problem",
                    "method",
                    "contribution",
                    "limitations",
                    "key_finding",
                    "theme",
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
            self.send_json({"themes": Counter(p["theme"] for p in subset).most_common(40)})
            return
        super().do_GET()


def main():
    host = "127.0.0.1"
    port = int(os.environ.get("RADAR_DASHBOARD_PORT", "7860"))
    server = ThreadingHTTPServer((host, port), RadarHandler)
    print(f"Research Radar Dashboard running at http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
