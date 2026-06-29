"""Shared venue catalog and normalization helpers."""

from __future__ import annotations

import re


AUTHORITY_VENUES = {
    "AAAI",
    "ACL",
    "COLM",
    "CVPR",
    "EACL",
    "EMNLP",
    "ICLR",
    "ICML",
    "IJCAI",
    "KDD",
    "NAACL",
    "NeurIPS",
    "SIGIR",
    "TACL",
    "WWW",
}


VENUE_ALIASES = {
    "aaai conference on artificial intelligence": "AAAI",
    "annual meeting of the association for computational linguistics": "ACL",
    "association for computational linguistics": "ACL",
    "conference and workshop on neural information processing systems": "NeurIPS",
    "conference on computer vision and pattern recognition": "CVPR",
    "conference on empirical methods in natural language processing": "EMNLP",
    "conference on language modeling": "COLM",
    "empirical methods in natural language processing": "EMNLP",
    "european chapter of the association for computational linguistics": "EACL",
    "findings of the association for computational linguistics": "ACL",
    "international conference on learning representations": "ICLR",
    "international conference on machine learning": "ICML",
    "international joint conference on artificial intelligence": "IJCAI",
    "knowledge discovery and data mining": "KDD",
    "north american chapter of the association for computational linguistics": "NAACL",
    "sigkdd conference on knowledge discovery and data mining": "KDD",
    "special interest group on information retrieval": "SIGIR",
    "the web conference": "WWW",
    "transactions of the association for computational linguistics": "TACL",
    "web conference": "WWW",
    "world wide web conference": "WWW",
}


_AUTHORITY_VENUE_KEYS = {venue.upper() for venue in AUTHORITY_VENUES}


def normalize_venue(venue: str | None) -> str:
    """Normalize common conference names to compact venue labels."""
    raw = str(venue or "").strip()
    if not raw:
        return ""

    upper = raw.upper()
    for name in AUTHORITY_VENUES:
        if upper == name or re.search(rf"\b{re.escape(name.upper())}\b", upper):
            return name

    lower = raw.lower()
    for pattern, alias in VENUE_ALIASES.items():
        if pattern in lower:
            return alias
    return raw


def is_authority_venue(venue: str | None) -> bool:
    return normalize_venue(venue).upper() in _AUTHORITY_VENUE_KEYS
