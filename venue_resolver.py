"""
Venue labeling for ArXiv_Daily_Digest.

The crawler still starts from arXiv/Semantic Scholar, but accepted papers often
need venue context to become useful in a research radar. This module first uses
manual overrides for known anchors, then checks OpenReview accepted-paper
metadata, and finally falls back to Semantic Scholar metadata when the title
match is very close.
"""

from __future__ import annotations

import difflib
import json
import os
import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
import yaml

from semantic_scholar_client import (
    SemanticScholarRateLimitError,
    make_s2_session,
    semantic_scholar_get,
)


ROOT = Path(__file__).resolve().parent
OVERRIDE_PATH = ROOT / "config" / "venue_overrides.yaml"
CACHE_PATH = ROOT / "data" / "_cache" / "semantic_scholar_venue_cache.json"
OPENREVIEW_CACHE_PATH = ROOT / "data" / "_cache" / "openreview_venue_cache.json"
S2_SEARCH_URL = "https://api.semanticscholar.org/graph/v1/paper/search"
OPENREVIEW_SEARCH_URL = "https://api2.openreview.net/notes/search"

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

OPENREVIEW_VENUE_PATTERNS = [
    (re.compile(r"^ICLR\.cc/(?P<year>\d{4})/Conference$"), "ICLR"),
    (re.compile(r"^ICML\.cc/(?P<year>\d{4})/Conference$"), "ICML"),
    (re.compile(r"^NeurIPS\.cc/(?P<year>\d{4})/Conference$"), "NeurIPS"),
    (re.compile(r"^COLMweb\.org/(?P<year>\d{4})/Conference$"), "COLM"),
]

OPENREVIEW_NON_ACCEPTED_TERMS = {
    "withdraw",
    "rejected",
    "desk rejected",
    "submitted",
    "not accepted",
}

_LAST_OPENREVIEW_REQUEST_AT = 0.0


class OpenReviewRateLimitError(RuntimeError):
    """Raised when OpenReview remains rate-limited after retries."""


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


def load_s2_cache(path: Path = CACHE_PATH) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_s2_cache(cache: dict[str, Any], path: Path = CACHE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2, sort_keys=True)


def load_openreview_cache(path: Path = OPENREVIEW_CACHE_PATH) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_openreview_cache(cache: dict[str, Any], path: Path = OPENREVIEW_CACHE_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2, sort_keys=True)


def _cache_key(title: str) -> str:
    return normalize_title(title)


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


def _openreview_min_interval() -> float:
    configured = os.getenv("OPENREVIEW_MIN_INTERVAL", "").strip()
    if configured:
        try:
            return max(0.0, float(configured))
        except ValueError:
            pass
    return 1.0


def _retry_after_seconds(response: requests.Response) -> float | None:
    raw = response.headers.get("Retry-After", "").strip()
    if not raw:
        return None
    try:
        return max(0.0, float(raw))
    except ValueError:
        return None


def _openreview_get(
    session: requests.Session,
    url: str,
    *,
    params: dict[str, Any] | None = None,
    timeout: int = 20,
    context: str = "OpenReview",
    max_retries: int | None = None,
) -> requests.Response:
    global _LAST_OPENREVIEW_REQUEST_AT

    if max_retries is None:
        max_retries = int(os.getenv("OPENREVIEW_MAX_RETRIES", "3"))

    response = None
    for attempt in range(max_retries + 1):
        elapsed = time.monotonic() - _LAST_OPENREVIEW_REQUEST_AT
        min_interval = _openreview_min_interval()
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        response = session.get(url, params=params, timeout=timeout)
        _LAST_OPENREVIEW_REQUEST_AT = time.monotonic()
        if response.status_code != 429:
            return response

        retry_after = _retry_after_seconds(response)
        fallback = min(45.0, (2**attempt) * 3.0)
        wait_seconds = retry_after if retry_after is not None else fallback
        print(
            f"[OpenReview] 429 rate limit for {context}; "
            f"sleeping {wait_seconds:.1f}s before retry {attempt + 1}/{max_retries}"
        )
        time.sleep(wait_seconds)

    assert response is not None
    if response.status_code == 429:
        raise OpenReviewRateLimitError(f"429 after {max_retries + 1} attempts for {context}")
    return response


def _content_value(content: dict[str, Any], key: str) -> Any:
    value = content.get(key)
    if isinstance(value, dict) and "value" in value:
        return value.get("value")
    return value


def _compact_openreview_note(note: dict[str, Any]) -> dict[str, Any]:
    content = note.get("content") or {}
    return {
        "id": note.get("id", ""),
        "forum": note.get("forum", ""),
        "title": _content_value(content, "title") or "",
        "venue": _content_value(content, "venue") or "",
        "venueid": _content_value(content, "venueid") or "",
    }


def _openreview_venue_from_id(venue_id: str) -> tuple[str, int | str]:
    for pattern, venue in OPENREVIEW_VENUE_PATTERNS:
        match = pattern.match(venue_id or "")
        if match:
            return venue, int(match.group("year"))
    return "", ""


def _openreview_type(venue_text: str) -> str:
    text = (venue_text or "").lower()
    if "oral" in text:
        return "oral"
    if "spotlight" in text:
        return "spotlight"
    if "poster" in text:
        return "poster"
    if "conference" in text:
        return "conference"
    return "conference"


def _format_openreview_label(note: dict[str, Any]) -> dict[str, Any]:
    venue_id = str(note.get("venueid", "") or "")
    venue_text = str(note.get("venue", "") or "")
    venue, year = _openreview_venue_from_id(venue_id)
    if not venue or venue not in A_VENUES:
        return {}

    lowered_venue = venue_text.lower()
    if not lowered_venue:
        return {}
    if any(term in lowered_venue for term in OPENREVIEW_NON_ACCEPTED_TERMS):
        return {}
    if venue.lower() not in lowered_venue and str(year) not in lowered_venue:
        return {}

    forum_id = note.get("forum") or note.get("id") or ""
    return {
        "venue": venue,
        "venue_year": year,
        "venue_type": _openreview_type(venue_text),
        "venue_url": f"https://openreview.net/forum?id={forum_id}" if forum_id else "",
        "venue_confidence": "openreview",
        "venue_source": "openreview",
    }


def _lookup_openreview(
    paper: dict[str, Any],
    session: requests.Session,
    cache: dict[str, Any] | None = None,
    title_threshold: float = 0.96,
) -> dict[str, Any]:
    title = paper.get("title", "")
    if not title:
        return {}

    key = _cache_key(title)
    cached = cache.get(key) if cache is not None else None
    if cached is not None:
        candidates = cached.get("data", [])
    else:
        params = {"term": title, "limit": 20}
        try:
            response = _openreview_get(
                session,
                OPENREVIEW_SEARCH_URL,
                params=params,
                timeout=20,
                context=f"venue search: {title[:48]}",
            )
            response.raise_for_status()
            candidates = [
                _compact_openreview_note(note)
                for note in response.json().get("notes", [])
            ]
            if cache is not None:
                cache[key] = {
                    "cached_at": datetime.now(timezone.utc).isoformat(),
                    "query": title,
                    "data": candidates,
                }
        except OpenReviewRateLimitError:
            raise
        except Exception as exc:
            print(f"[OpenReview] lookup failed: {title[:60]}... {exc}")
            return {}

    wanted = normalize_title(title)
    for candidate in candidates:
        candidate_title = normalize_title(candidate.get("title", ""))
        if not candidate_title:
            continue
        ratio = difflib.SequenceMatcher(None, wanted, candidate_title).ratio()
        if ratio < title_threshold:
            continue

        label = _format_openreview_label(candidate)
        if label:
            return label

    return {}


def _lookup_semantic_scholar(
    paper: dict[str, Any],
    session,
    cache: dict[str, Any] | None = None,
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
    key = _cache_key(title)
    cached = cache.get(key) if cache is not None else None
    if cached is not None:
        candidates = cached.get("data", [])
    else:
        try:
            response = semantic_scholar_get(
                session,
                S2_SEARCH_URL,
                params=params,
                timeout=15,
                context=f"venue search: {title[:48]}",
            )
            response.raise_for_status()
            candidates = response.json().get("data", [])
            if cache is not None:
                cache[key] = {
                    "cached_at": datetime.now(timezone.utc).isoformat(),
                    "query": title,
                    "data": candidates,
                }
        except SemanticScholarRateLimitError:
            raise
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
    session=None,
    cache: dict[str, Any] | None = None,
    openreview_session: requests.Session | None = None,
    openreview_cache: dict[str, Any] | None = None,
    use_openreview: bool = True,
    use_semantic_scholar: bool = True,
) -> dict[str, Any]:
    overrides = overrides or load_overrides()
    label = _lookup_override(paper, overrides)
    if label:
        return label

    if use_openreview:
        openreview_session = openreview_session or requests.Session()
        label = _lookup_openreview(paper, openreview_session, cache=openreview_cache)
        if label:
            return label

    if not use_semantic_scholar:
        return {}

    session = session or make_s2_session()
    return _lookup_semantic_scholar(paper, session, cache=cache)


def annotate_venues(
    papers: list[dict[str, Any]],
    use_openreview: bool = True,
    use_semantic_scholar: bool = True,
    delay: float = 0.2,
) -> list[dict[str, Any]]:
    if not papers:
        return papers

    overrides = load_overrides()
    openreview_session = requests.Session() if use_openreview else None
    s2_session = make_s2_session() if use_semantic_scholar else None
    openreview_cache = load_openreview_cache() if use_openreview else {}
    cache = load_s2_cache() if use_semantic_scholar else {}
    labeled = 0
    openreview_rate_limited = False
    s2_rate_limited = False

    for index, paper in enumerate(papers):
        try:
            label = resolve_venue(
                paper,
                overrides=overrides,
                session=s2_session,
                cache=cache,
                openreview_session=openreview_session,
                openreview_cache=openreview_cache,
                use_openreview=use_openreview and not openreview_rate_limited,
                use_semantic_scholar=use_semantic_scholar and not s2_rate_limited,
            )
        except OpenReviewRateLimitError as exc:
            print(f"[Venue] Stopping OpenReview venue lookup for this batch: {exc}")
            openreview_rate_limited = True
            try:
                label = resolve_venue(
                    paper,
                    overrides=overrides,
                    session=s2_session,
                    cache=cache,
                    use_openreview=False,
                    use_semantic_scholar=use_semantic_scholar and not s2_rate_limited,
                )
            except SemanticScholarRateLimitError as s2_exc:
                print(f"[Venue] Stopping Semantic Scholar venue lookup for this batch: {s2_exc}")
                s2_rate_limited = True
                label = {}
        except SemanticScholarRateLimitError as exc:
            print(f"[Venue] Stopping Semantic Scholar venue lookup for this batch: {exc}")
            s2_rate_limited = True
            label = {}

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

        external_lookup_active = (
            (use_openreview and not openreview_rate_limited)
            or (use_semantic_scholar and not s2_rate_limited)
        )
        if external_lookup_active and delay > 0 and index < len(papers) - 1:
            time.sleep(delay)

    if use_openreview:
        save_openreview_cache(openreview_cache)
    if use_semantic_scholar:
        save_s2_cache(cache)

    suffix_parts = []
    if openreview_rate_limited:
        suffix_parts.append("OpenReview rate-limited")
    if s2_rate_limited:
        suffix_parts.append("S2 rate-limited")
    suffix = f" ({', '.join(suffix_parts)})" if suffix_parts else ""
    print(f"[Venue] Labeled {labeled}/{len(papers)} papers with venue metadata{suffix}")
    return papers

