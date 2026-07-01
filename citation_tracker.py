"""
ArXiv_Daily_Digest — Semantic Scholar 引用追踪模块
通过种子论文的被引列表发现新论文，弥补关键词搜索的盲区。
支持可选 SEMANTIC_SCHOLAR_API_KEY / S2_API_KEY，并在 429 时自动退避。
"""

import time
import json
import os
from datetime import datetime, timedelta, timezone
from pathlib import Path

from semantic_scholar_client import (
    SemanticScholarRateLimitError,
    make_s2_session,
    semantic_scholar_get,
)

API_BASE = "https://api.semanticscholar.org/graph/v1"
ROOT = Path(__file__).resolve().parent
CACHE_PATH = ROOT / "data" / "_cache" / "semantic_scholar_citation_cache.json"


def citation_cache_ttl() -> timedelta:
    raw = os.getenv("SEMANTIC_SCHOLAR_CITATION_CACHE_TTL_DAYS", "14").strip()
    try:
        days = max(0.0, float(raw))
    except ValueError:
        days = 14.0
    return timedelta(days=days)


def load_citation_cache(path=CACHE_PATH):
    if not path.exists():
        return {}
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def save_citation_cache(cache, path=CACHE_PATH):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2, sort_keys=True)


def _cache_entry_is_fresh(entry):
    if not isinstance(entry, dict) or "data" not in entry:
        return False
    ttl = citation_cache_ttl()
    if ttl.total_seconds() <= 0:
        return False
    try:
        cached_at = datetime.fromisoformat(str(entry.get("cached_at", "")))
    except ValueError:
        return False
    if cached_at.tzinfo is None:
        cached_at = cached_at.replace(tzinfo=timezone.utc)
    return datetime.now(timezone.utc) - cached_at <= ttl


def _cached_citations(arxiv_id, cache):
    entry = cache.get(str(arxiv_id))
    if not _cache_entry_is_fresh(entry):
        return None
    return entry.get("data", [])


def get_citing_papers(arxiv_id, limit=50, session=None, cache=None):
    """
    查询引用了某篇种子论文的所有后续论文。
    :param arxiv_id: ArXiv ID（如 "2310.06824"）
    :param limit: 最大返回数量
    :return: 论文列表，每篇包含 title/authors/url/abstract 等
    """
    cached = _cached_citations(arxiv_id, cache or {})
    if cached is not None:
        print(f"[CitTracker] ♻️ ArXiv:{arxiv_id} 使用缓存引用 {len(cached)} 篇")
        return cached

    url = f"{API_BASE}/paper/ArXiv:{arxiv_id}/citations"
    params = {
        "fields": "title,authors,abstract,externalIds,year,citationCount,url",
        "limit": limit,
    }

    try:
        session = session or make_s2_session()
        resp = semantic_scholar_get(
            session,
            url,
            params=params,
            timeout=15,
            context=f"citations ArXiv:{arxiv_id}",
        )
        if resp.status_code == 404:
            print(f"[CitTracker] ⚠️ 论文 {arxiv_id} 在 Semantic Scholar 中未找到")
            if cache is not None:
                cache[str(arxiv_id)] = {
                    "cached_at": datetime.now(timezone.utc).isoformat(),
                    "data": [],
                    "status": 404,
                }
            return []
        resp.raise_for_status()
        data = resp.json()

        papers = []
        for item in data.get("data", []):
            citing = item.get("citingPaper", {})
            if not citing.get("title"):
                continue

            # 提取 ArXiv ID（如果有）
            ext_ids = citing.get("externalIds", {})
            paper_arxiv_id = ext_ids.get("ArXiv", "")

            papers.append({
                "title": citing.get("title", ""),
                "authors": [a.get("name", "") for a in citing.get("authors", [])],
                "summary": citing.get("abstract", "") or "",
                "url": f"http://arxiv.org/abs/{paper_arxiv_id}" if paper_arxiv_id else citing.get("url", ""),
                "pdf_url": f"http://arxiv.org/pdf/{paper_arxiv_id}" if paper_arxiv_id else "",
                "category": "via-citation",  # 标记来源是引用追踪
                "arxiv_id": paper_arxiv_id,
                "year": citing.get("year"),
                "citation_count": citing.get("citationCount", 0),
            })

        print(f"[CitTracker] ✅ ArXiv:{arxiv_id} 被 {len(papers)} 篇论文引用")
        if cache is not None:
            cache[str(arxiv_id)] = {
                "cached_at": datetime.now(timezone.utc).isoformat(),
                "data": papers,
                "status": resp.status_code,
            }
        return papers

    except SemanticScholarRateLimitError:
        raise
    except Exception as e:
        print(f"[CitTracker] ❌ 查询 {arxiv_id} 失败: {e}")
        return []


def track_all_seeds(seed_papers, delay=1.0):
    """
    批量追踪所有种子论文的被引列表。
    :param seed_papers: ArXiv ID 列表，如 ["2310.06824", "2306.03341"]
    :param delay: API 调用间隔（秒），防限流
    :return: 去重后的引用论文列表
    """
    if not seed_papers:
        return []

    all_papers = []
    seen_ids = set()
    session = make_s2_session()
    cache = load_citation_cache()
    s2_rate_limited = False

    for i, seed_id in enumerate(seed_papers):
        print(f"[CitTracker] ({i+1}/{len(seed_papers)}) 追踪种子论文: ArXiv:{seed_id}")
        cached = _cached_citations(seed_id, cache)
        if s2_rate_limited and cached is None:
            print(f"[CitTracker] ⏭️ S2 已限流，本轮跳过未缓存种子 ArXiv:{seed_id}")
            citing = []
        else:
            try:
                citing = get_citing_papers(seed_id, session=session, cache=cache)
                save_citation_cache(cache)
            except SemanticScholarRateLimitError as exc:
                print(f"[CitTracker] ⛔ Semantic Scholar 限流，后续仅使用缓存: {exc}")
                s2_rate_limited = True
                citing = cached or []

        for p in citing:
            pid = p.get("arxiv_id", "") or p.get("title", "")
            if pid and pid not in seen_ids:
                seen_ids.add(pid)
                all_papers.append(p)

        if not s2_rate_limited and i < len(seed_papers) - 1:
            time.sleep(delay)

    save_citation_cache(cache)
    print(f"[CitTracker] 📊 共发现 {len(all_papers)} 篇引用论文（已去重）")
    return all_papers

