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
    title = str(item.get("title") or "").strip()
    url = str(item.get("url") or item.get("paper_url") or "").strip()
    pdf_url = str(item.get("pdf_url") or item.get("pdf") or "").strip()
    summary = str(item.get("summary") or item.get("abstract") or "").strip()

    if not item_direction:
        return None

    tags = item.get("tags") or []
    if isinstance(tags, str):
        tags = [tags]

    entry = {
        "direction_id": item_direction,
        "arxiv_id": arxiv_id,
        "title": title,
        "authors": item.get("authors") or [],
        "summary": summary,
        "url": url,
        "pdf_url": pdf_url,
        "category": str(item.get("category") or "").strip(),
        "published": str(item.get("published") or "").strip(),
        "reason": str(item.get("reason") or item.get("note") or "").strip(),
        "tags": [str(tag).strip() for tag in tags if str(tag).strip()],
    }
    if entry["arxiv_id"] or (entry["title"] and (entry["url"] or entry["pdf_url"])):
        return entry
    return None


def manual_entry_key(entry: dict) -> str:
    if entry.get("arxiv_id"):
        return str(entry["arxiv_id"]).lower()
    if entry.get("url"):
        return str(entry["url"]).strip().lower()
    if entry.get("pdf_url"):
        return str(entry["pdf_url"]).strip().lower()
    return str(entry.get("title") or "").strip().lower()


def manual_entry_to_paper(entry: dict) -> dict | None:
    if entry.get("arxiv_id"):
        return None
    title = str(entry.get("title") or "").strip()
    url = str(entry.get("url") or "").strip()
    pdf_url = str(entry.get("pdf_url") or "").strip()
    if not title or not (url or pdf_url):
        return None
    authors = entry.get("authors") or []
    if isinstance(authors, str):
        authors = [part.strip() for part in authors.split(";") if part.strip()]
    return {
        "title": title,
        "authors": authors,
        "summary": str(entry.get("summary") or "").strip(),
        "published": entry.get("published", ""),
        "url": url or pdf_url,
        "pdf_url": pdf_url,
        "category": entry.get("category", "") or "manual",
        "ingest_source": "manual",
        "manual_inject": True,
        "manual_reason": entry.get("reason", ""),
        "manual_tags": entry.get("tags", []),
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
            key = manual_entry_key(entry)
            if not key or key in seen:
                continue
            deduped.setdefault(direction_id, []).append(entry)
            seen.add(key)

    return deduped
