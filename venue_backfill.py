"""
Backfill venue metadata for existing local JSONL data.

This script is intentionally separate from main.py. It only reads existing
papers.jsonl files, resolves missing venue labels, and optionally writes the
updated JSONL back. By default it is a dry run.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

import yaml

from venue_resolver import annotate_venues


ROOT = Path(__file__).resolve().parent
DATA_DIR = ROOT / "data"
CONFIG_PATH = ROOT / "config" / "directions.yaml"


def load_directions() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}
    return config.get("directions", {})


def latest_week(directions: dict) -> str:
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


def load_jsonl(path: Path) -> list[dict]:
    rows = []
    if not path.exists():
        return rows
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def write_jsonl(path: Path, rows: list[dict]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def backfill_file(
    path: Path,
    write: bool,
    openreview: bool,
    semantic_scholar: bool,
    delay: float,
    limit: int | None,
) -> tuple[int, int, int, int]:
    rows = load_jsonl(path)
    if not rows:
        return 0, 0, 0, 0

    missing = [row for row in rows if not row.get("venue")]
    selected = missing[:limit] if limit else missing
    before = sum(1 for row in rows if row.get("venue"))
    if selected and write:
        annotate_venues(
            selected,
            use_openreview=openreview,
            use_semantic_scholar=semantic_scholar,
            delay=delay,
        )
        write_jsonl(path, rows)
    after = sum(1 for row in rows if row.get("venue"))
    return len(rows), before, after, len(selected)


def parse_args():
    parser = argparse.ArgumentParser(description="Backfill venue metadata without running main.py.")
    parser.add_argument("--week", help="ISO week such as 2026-W23. Defaults to latest active week.")
    parser.add_argument("--direction", action="append", help="Direction ID. Can be passed multiple times.")
    parser.add_argument("--write", action="store_true", help="Write updated JSONL files. Default is dry run.")
    parser.add_argument("--manual-only", action="store_true", help="Use only venue_overrides.yaml, no external venue calls.")
    parser.add_argument("--no-openreview", action="store_true", help="Disable OpenReview accepted-paper lookup.")
    parser.add_argument("--delay", type=float, default=0.0, help="Extra delay between venue lookups. S2 helper already rate-limits.")
    parser.add_argument("--limit", type=int, help="Only process this many missing-venue papers per direction.")
    return parser.parse_args()


def main():
    args = parse_args()
    directions = load_directions()
    selected = args.direction or list(directions)
    week = args.week or latest_week(directions)

    print(f"[VenueBackfill] week={week} mode={'write' if args.write else 'dry-run'}")
    openreview = not args.manual_only and not args.no_openreview
    semantic_scholar = not args.manual_only
    print(f"[VenueBackfill] OpenReview lookup={'on' if openreview else 'off'}")
    print(f"[VenueBackfill] Semantic Scholar lookup={'on' if semantic_scholar else 'off'}")

    for direction_id in selected:
        path = DATA_DIR / direction_id / week / "papers.jsonl"
        total, before, after, selected = backfill_file(
            path,
            write=args.write,
            openreview=openreview,
            semantic_scholar=semantic_scholar,
            delay=args.delay,
            limit=args.limit,
        )
        if total == 0:
            print(f"- {direction_id}: no data at {path}")
            continue
        if args.write:
            print(f"- {direction_id}: {before} -> {after} venue labels / {total} papers; processed {selected} missing")
        else:
            print(f"- {direction_id}: {before} venue labels / {total} papers; would process {selected} missing; pass --write to update")


if __name__ == "__main__":
    main()
