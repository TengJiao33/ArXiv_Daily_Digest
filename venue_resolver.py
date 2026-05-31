"""
Venue labeling for Knowledge Editing Direction Radar.

The crawler still starts from arXiv/Semantic Scholar, but accepted papers often
need venue context to become useful in a research radar. This module first uses
manual overrides for known anchors, then falls back to Semantic Scholar metadata
when the title match is very close.
"""

from __future__ import annotations

import difflib
import re
import time
from pathlib import Path
from typing import Any

import requests
import yaml


ROOT = Path(__file__).resolve().parent
OVERRIDE_PATH = ROOT / "config" / "venue_overrides.yaml"
S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"

A_VENUES = {
    "ACL",
    "EMNLP",
    "NAACL",
    "EACL",
    "TACL",
    "ICLR",
    "ICML",
    "NeurIPS",
    "COLM",
    "AAAI",
}

VENUE_ALIASES = {
    "association for computational linguistics": "ACL",
    "annual meeting of the association for computational linguistics": "ACL",
    "findings of the association for computational linguistics": "ACL",
    "conference on empirical methods in natural language processing": "EMNLP",
    "empirical methods in natural language processing": "EMNLP",
    "north american chapter of the association for computational linguistics": "NAACL",
    "transactions of the association for computational linguistics": "TACL",
    "international conference on learning representations": "ICLR",
    "international conference on machine learning": "ICML",
    "advances in neural information processing systems": "NeurIPS",
    "conference on language modeling": "COLM",
    "aaai conference on artificial intelligence": "AAAI",
}


def normalize_title(title: str) -> str:
    text = (title or "").lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_venue(venue: str) -> str:
    raw = (venue or "").strip()
    if not raw:
        return ""

    upper = raw.upper()
    for name in A_VENUES:
        if upper == name or re.search(rf"\b{re.escape(name)}\b", upper):
            return name

    lower = raw.lower()
    for pattern, alias in VENUE_ALIASES.items():
        if pattern in lower:
            return alias
    return raw


def extract_arxiv_id(paper: dict[str, Any]) -> str:
    candidates = [
        paper.get("arxiv_id", ""),
        paper.get("id", ""),
        paper.get("url", ""),
        paper.get("pdf_url", ""),
    ]
    for value in candidates:
        match = re.search(r"(\d{4}\.\d{4,5})", str(value or ""))
        if match:
            return match.group(1)
    return ""


def load_overrides(path: Path = OVERRIDE_PATH) -> dict[str, Any]:
    if not path.exists():
        return {"by_arxiv": {}, "by_title": {}}
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return {
        "by_arxiv": data.get("by_arxiv") or {},
        "by_title": data.get("by_title") or {},
    }


def _format_label(source: dict[str, Any]) -> dict[str, Any]:
    venue = normalize_venue(str(source.get("venue", "")))
    if not venue:
        return {}
    return {
        "venue": venue,
        "venue_year": source.get("year") or "",
        "venue_type": source.get("type") or "conference",
        "venue_url": source.get("url") or "",
        "venue_confidence": source.get("confidence") or "manual",
        "venue_source": source.get("source") or "override",
    }


def _lookup_override(paper: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    arxiv_id = extract_arxiv_id(paper)
    if arxiv_id and arxiv_id in overrides["by_arxiv"]:
        return _format_label(overrides["by_arxiv"][arxiv_id])

    normalized = normalize_title(paper.get("title", ""))
    for title, label in overrides["by_title"].items():
        if normalize_title(title) == normalized:
            return _format_label(label)

    return {}


def _lookup_semantic_scholar(
    paper: dict[str, Any],
    session: requests.Session,
    title_threshold: float = 0.92,
) -> dict[str, Any]:
    title = paper.get("title", "")
    if not title:
        return {}

    params = {
        "query": title,
        "limit": 3,
        "fields": "title,venue,year,publicationVenue,url,externalIds",
    }
    try:
        response = session.get(S2_SEARCH_URL, params=params, timeout=15)
        response.raise_for_status()
        candidates = response.json().get("data", [])
    except Exception as exc:
        print(f"[Venue] Semantic Scholar lookup failed: {title[:60]}... {exc}")
        return {}

    wanted = normalize_title(title)
    for candidate in candidates:
        candidate_title = normalize_title(candidate.get("title", ""))
        ratio = difflib.SequenceMatcher(None, wanted, candidate_title).ratio()
        if ratio < title_threshold:
            continue

        venue = ""
        publication_venue = candidate.get("publicationVenue") or {}
        if isinstance(publication_venue, dict):
            venue = publication_venue.get("name") or ""
        venue = normalize_venue(venue or candidate.get("venue") or "")
        if venue not in A_VENUES:
            continue

        return {
            "venue": venue,
            "venue_year": candidate.get("year") or paper.get("year") or "",
            "venue_type": "conference",
            "venue_url": candidate.get("url") or paper.get("url", ""),
            "venue_confidence": "semantic-scholar",
            "venue_source": "semantic-scholar",
        }

    return {}


def resolve_venue(
    paper: dict[str, Any],
    overrides: dict[str, Any] | None = None,
    session: requests.Session | None = None,
    use_semantic_scholar: bool = True,
) -> dict[str, Any]:
    overrides = overrides or load_overrides()
    label = _lookup_override(paper, overrides)
    if label:
        return label

    if not use_semantic_scholar:
        return {}

    session = session or requests.Session()
    return _lookup_semantic_scholar(paper, session)


def annotate_venues(
    papers: list[dict[str, Any]],
    use_semantic_scholar: bool = True,
    delay: float = 0.2,
) -> list[dict[str, Any]]:
    if not papers:
        return papers

    overrides = load_overrides()
    session = requests.Session()
    labeled = 0

    for index, paper in enumerate(papers):
        label = resolve_venue(
            paper,
            overrides=overrides,
            session=session,
            use_semantic_scholar=use_semantic_scholar,
        )
        if label:
            paper.update(label)
            labeled += 1
        else:
            paper.setdefault("venue", "")
            paper.setdefault("venue_year", "")
            paper.setdefault("venue_type", "")
            paper.setdefault("venue_url", "")
            paper.setdefault("venue_confidence", "")
            paper.setdefault("venue_source", "")

        if use_semantic_scholar and index < len(papers) - 1:
            time.sleep(delay)

    print(f"[Venue] Labeled {labeled}/{len(papers)} papers with venue metadata")
    return papers

