"""
Research Radar — 方向相关性过滤
在 ArXiv 搜索与引用追踪合并后，按方向配置做轻量二次过滤。
"""


def _normalize_terms(terms):
    return [str(term).strip().lower() for term in terms or [] if str(term).strip()]


def _paper_text(paper):
    parts = [
        paper.get("title", ""),
        paper.get("summary", ""),
        paper.get("abstract", ""),
    ]
    return " ".join(str(part) for part in parts if part).lower()


def is_relevant(paper, direction_conf):
    """
    判断论文是否符合方向相关性约束。

    配置语义：
      - relevance.must_any: 至少命中一个领域锚点
      - relevance.topic_any: 至少命中一个主题词

    如果没有配置 relevance，则默认保留，避免影响已有方向。
    """
    relevance = direction_conf.get("relevance", {})
    must_any = _normalize_terms(relevance.get("must_any"))
    topic_any = _normalize_terms(relevance.get("topic_any"))

    if not must_any and not topic_any:
        return True

    text = _paper_text(paper)
    if must_any and not any(term in text for term in must_any):
        return False
    if topic_any and not any(term in text for term in topic_any):
        return False
    return True


def filter_relevant_papers(papers, direction_conf):
    """返回保留论文与被过滤论文。"""
    kept = []
    dropped = []

    for paper in papers:
        if is_relevant(paper, direction_conf):
            kept.append(paper)
        else:
            dropped.append(paper)

    return kept, dropped
