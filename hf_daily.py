"""
Knowledge Editing Direction Radar — HuggingFace Daily Papers 补充源
从 HF Daily Papers API 拉取每日 trending 论文，提供 upvote 信号。
不替代 ArXiv 主流程，仅作为"社区热度"补充信号。

API: https://huggingface.co/api/daily_papers?date=YYYY-MM-DD
返回: [{paper: {id, title, summary, ...}, numUpvotes, ...}, ...]
"""

import requests
from datetime import date


HF_API_URL = "https://huggingface.co/api/daily_papers"


def fetch_hf_daily(target_date=None, min_upvotes=5):
    """
    获取 HuggingFace 某天的 trending 论文。
    :param target_date: 日期对象，默认今天
    :param min_upvotes: 最低 upvote 数过滤阈值
    :return: 按 upvotes 降序排列的论文列表
    """
    if target_date is None:
        target_date = date.today()

    date_str = target_date.strftime("%Y-%m-%d")

    try:
        resp = requests.get(
            HF_API_URL,
            params={"date": date_str},
            timeout=15,
        )
        resp.raise_for_status()
        data = resp.json()
    except Exception as e:
        print(f"[HF Daily] ❌ 获取失败 ({date_str}): {e}")
        return []

    papers = []
    for item in data:
        upvotes = item.get("numUpvotes", 0)
        if upvotes < min_upvotes:
            continue

        paper_info = item.get("paper", {})
        arxiv_id = paper_info.get("id", "")
        title = paper_info.get("title", "")
        summary = paper_info.get("summary", "")

        papers.append({
            "arxiv_id": arxiv_id,
            "title": title,
            "summary": summary,
            "hf_upvotes": upvotes,
            "hf_date": date_str,
            "url": f"http://arxiv.org/abs/{arxiv_id}" if arxiv_id else "",
        })

    # 按 upvotes 降序
    papers.sort(key=lambda p: p["hf_upvotes"], reverse=True)
    print(f"[HF Daily] ✅ {date_str}: {len(papers)} 篇 (≥{min_upvotes} upvotes)")
    return papers


def get_trending_top_n(target_date=None, n=5, min_upvotes=3):
    """
    获取当日 HF trending top-N 论文，用于每日推送摘要。
    :return: top-N 论文列表 [{title, arxiv_id, hf_upvotes, url}, ...]
    """
    papers = fetch_hf_daily(target_date, min_upvotes=min_upvotes)
    return papers[:n]


def match_hf_upvotes(papers, target_date=None):
    """
    给已有论文列表补充 HF upvote 信息。
    对 papers 中每篇论文，如果它出现在当日 HF trending 中，
    则写入 hf_upvotes 字段。
    :param papers: 论文列表（会被原地修改）
    :return: 匹配到的数量
    """
    hf_papers = fetch_hf_daily(target_date, min_upvotes=0)
    hf_map = {p["arxiv_id"]: p["hf_upvotes"] for p in hf_papers if p["arxiv_id"]}

    matched = 0
    for paper in papers:
        # 从 url 中提取 arxiv_id
        url = paper.get("url", "")
        import re
        m = re.search(r'(\d{4}\.\d{4,5})', url)
        if m:
            aid = m.group(1)
            if aid in hf_map:
                paper["hf_upvotes"] = hf_map[aid]
                matched += 1

    if matched:
        print(f"[HF Daily] 📊 匹配到 {matched} 篇论文的 HF upvotes")
    return matched

