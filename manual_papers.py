"""Load one-off manual paper injections for the main pipeline."""

from __future__ import annotations

import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config" / "manual_papers.yaml"


def extract_arxiv_id(value) -> str:
    match = re.search(r"\d{4}\.\d{4,5}", str(value or ""))
    return match.group(0) if match else ""


def _enabled(item: dict) -> bool:
    value = item.get("enabled", True)
    if isinstance(value, str):
        return value.strip().lower() not in {"0", "false", "no", "off"}
    return bool(value)


def _normalize_entry(item, direction_id: str | None = None) -> dict | None:
    if isinstance(item, str):
        arxiv_id = extract_arxiv_id(item)
        if not arxiv_id or not direction_id:
            return None
        return {
            "direction_id": direction_id,
            "arxiv_id": arxiv_id,
            "reason": "",
            "tags": [],
        }

    if not isinstance(item, dict) or not _enabled(item):
        return None

    item_direction = str(item.get("direction_id") or direction_id or "").strip()
    arxiv_id = extract_arxiv_id(
        item.get("arxiv_id")
        or item.get("id")
        or item.get("url")
        or item.get("pdf_url")
        or item.get("paper")
    )
    if not item_direction or not arxiv_id:
        return None

    tags = item.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]

    return {
        "direction_id": item_direction,
        "arxiv_id": arxiv_id,
        "reason": str(item.get("reason") or item.get("note") or "").strip(),
        "tags": [str(tag).strip() for tag in tags if str(tag).strip()],
    }


def load_manual_papers(path: Path = CONFIG_PATH, directions: dict | None = None) -> dict[str, list[dict]]:
    if not path.exists():
        return {}

    with path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    raw = config.get("manual_papers", [])
    by_direction: dict[str, list[dict]] = {}

    if isinstance(raw, dict):
        for direction_id, items in raw.items():
            if not isinstance(items, list):
                items = [items]
            for item in items:
                entry = _normalize_entry(item, direction_id=str(direction_id))
                if entry:
                    by_direction.setdefault(entry["direction_id"], []).append(entry)
    elif isinstance(raw, list):
        for item in raw:
            entry = _normalize_entry(item)
            if entry:
                by_direction.setdefault(entry["direction_id"], []).append(entry)

    if directions:
        known = set(directions)
        by_direction = {
            direction_id: entries
            for direction_id, entries in by_direction.items()
            if direction_id in known
        }

    deduped: dict[str, list[dict]] = {}
    for direction_id, entries in by_direction.items():
        seen = set()
        for entry in entries:
            if entry["arxiv_id"] in seen:
                continue
            deduped.setdefault(direction_id, []).append(entry)
            seen.add(entry["arxiv_id"])

    return deduped
