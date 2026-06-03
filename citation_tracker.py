"""
ArXiv_Daily_Digest — Semantic Scholar 引用追踪模块
通过种子论文的被引列表发现新论文，弥补关键词搜索的盲区。
支持可选 SEMANTIC_SCHOLAR_API_KEY / S2_API_KEY，并在 429 时自动退避。
"""

import time

from semantic_scholar_client import make_s2_session, semantic_scholar_get

API_BASE = "https://api.semanticscholar.org/graph/v1"


def get_citing_papers(arxiv_id, limit=50, session=None):
    """
    查询引用了某篇种子论文的所有后续论文。
    :param arxiv_id: ArXiv ID（如 "2310.06824"）
    :param limit: 最大返回数量
    :return: 论文列表，每篇包含 title/authors/url/abstract 等
    """
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
        return papers

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

    for i, seed_id in enumerate(seed_papers):
        print(f"[CitTracker] ({i+1}/{len(seed_papers)}) 追踪种子论文: ArXiv:{seed_id}")
        citing = get_citing_papers(seed_id, session=session)

        for p in citing:
            pid = p.get("arxiv_id", "") or p.get("title", "")
            if pid and pid not in seen_ids:
                seen_ids.add(pid)
                all_papers.append(p)

        if i < len(seed_papers) - 1:
            time.sleep(delay)

    print(f"[CitTracker] 📊 共发现 {len(all_papers)} 篇引用论文（已去重）")
    return all_papers

