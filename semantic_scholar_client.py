"""
Small Semantic Scholar API helper with API-key support and 429 backoff.

The Academic Graph API accepts an optional x-api-key header. With a key, the
introductory limit is still modest, so this helper enforces a conservative
client-side interval and retries 429 responses using Retry-After when present.
"""

from __future__ import annotations

import os
import time
from typing import Any

import requests

try:
    from dotenv import load_dotenv

    load_dotenv()
except Exception:
    pass


_LAST_REQUEST_AT = 0.0


class SemanticScholarRateLimitError(RuntimeError):
    """Raised when a Semantic Scholar request is still rate-limited after retries."""


def get_s2_api_key() -> str:
    """Return a Semantic Scholar API key from either common env var name."""
    return (
        os.getenv("SEMANTIC_SCHOLAR_API_KEY", "").strip()
        or os.getenv("S2_API_KEY", "").strip()
    )


def make_s2_session() -> requests.Session:
    session = requests.Session()
    api_key = get_s2_api_key()
    if api_key:
        session.headers.update({"x-api-key": api_key})
    return session


def default_min_interval() -> float:
    configured = os.getenv("SEMANTIC_SCHOLAR_MIN_INTERVAL", "").strip()
    if configured:
        try:
            return max(0.0, float(configured))
        except ValueError:
            pass
    return 1.2 if get_s2_api_key() else 3.0


def _retry_after_seconds(response: requests.Response) -> float | None:
    raw = response.headers.get("Retry-After", "").strip()
    if not raw:
        return None
    try:
        return max(0.0, float(raw))
    except ValueError:
        return None


def semantic_scholar_get(
    session: requests.Session,
    url: str,
    *,
    params: dict[str, Any] | None = None,
    timeout: int = 15,
    context: str = "Semantic Scholar",
    max_retries: int | None = None,
    min_interval: float | None = None,
) -> requests.Response:
    global _LAST_REQUEST_AT

    if max_retries is None:
        try:
            max_retries = int(os.getenv("SEMANTIC_SCHOLAR_MAX_RETRIES", "4"))
        except ValueError:
            max_retries = 4
    max_retries = max(0, max_retries)
    if min_interval is None:
        min_interval = default_min_interval()

    retry_5xx = os.getenv("SEMANTIC_SCHOLAR_RETRY_5XX", "1").strip().lower() not in {
        "0",
        "false",
        "no",
    }
    max_attempts = max_retries + 1
    response = None
    for attempt in range(max_attempts):
        elapsed = time.monotonic() - _LAST_REQUEST_AT
        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        response = session.get(url, params=params, timeout=timeout)
        _LAST_REQUEST_AT = time.monotonic()

        if response.status_code == 429:
            if attempt >= max_retries:
                raise SemanticScholarRateLimitError(
                    f"429 after {max_attempts} attempts for {context}"
                )

            retry_after = _retry_after_seconds(response)
            fallback = min(60.0, (2**attempt) * (2.5 if get_s2_api_key() else 6.0))
            wait_seconds = retry_after if retry_after is not None else fallback
            print(
                f"[S2] 429 rate limit for {context}; "
                f"sleeping {wait_seconds:.1f}s before retry {attempt + 1}/{max_retries}"
            )
            time.sleep(wait_seconds)
            continue

        if retry_5xx and response.status_code in {500, 502, 503, 504} and attempt < max_retries:
            wait_seconds = min(30.0, (2**attempt) * 2.0)
            print(
                f"[S2] {response.status_code} server error for {context}; "
                f"sleeping {wait_seconds:.1f}s before retry {attempt + 1}/{max_retries}"
            )
            time.sleep(wait_seconds)
            continue

        return response

    assert response is not None
    return response
