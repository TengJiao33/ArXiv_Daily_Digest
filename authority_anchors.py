"""Load manually curated A-conference anchor papers."""

from __future__ import annotations

from pathlib import Path

import yaml

from venue_catalog import is_authority_venue, normalize_venue


ROOT = Path(__file__).resolve().parent
CONFIG_PATH = ROOT / "config" / "authority_anchors.yaml"


def _as_list(value) -> list[str]:
    if isinstance(value, list):
        return [str(item).strip() for item in value if str(item).strip()]
    if value:
        return [str(value).strip()]
    return []


def load_authority_anchors(path: Path = CONFIG_PATH, directions: dict | None = None) -> list[dict]:
    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    anchors = []
    for item in config.get("authority_anchors", []) or []:
        if not isinstance(item, dict):
            continue

        direction_id = str(item.get("direction_id") or "").strip()
        title = str(item.get("title") or "").strip()
        venue = normalize_venue(item.get("venue"))
        if not direction_id or not title or not venue:
            continue

        direction_name = direction_id
        if directions and direction_id in directions:
            direction_name = directions[direction_id].get("name", direction_id)

        anchors.append(
            {
                "direction_id": direction_id,
                "direction_name": direction_name,
                "title": title,
                "venue": venue,
                "year": item.get("year", ""),
                "type": str(item.get("type") or "").strip(),
                "url": str(item.get("url") or "").strip(),
                "note": str(item.get("note") or "").strip(),
                "tags": _as_list(item.get("tags")),
                "is_authority_venue": is_authority_venue(venue),
            }
        )

    return sorted(
        anchors,
        key=lambda anchor: (
            anchor["direction_id"],
            -int(anchor["year"] or 0),
            anchor["venue"],
            anchor["title"].lower(),
        ),
    )
