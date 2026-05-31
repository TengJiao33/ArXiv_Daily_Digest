"""
Knowledge Editing Direction Radar — 数据存储模块
按研究方向 + ISO 周组织数据，使用 JSONL 格式追加写入。
自动去重（基于 ArXiv ID）。
"""

import os
import json
import re
from datetime import datetime, date


DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")


def extract_arxiv_id(url):
    """从 ArXiv URL 中提取论文 ID（去除版本号）"""
    match = re.search(r'(\d{4}\.\d{4,5})', str(url))
    return match.group(1) if match else str(url)


def get_week_str(target_date=None):
    """获取 ISO 周字符串，如 '2026-W17'"""
    if target_date is None:
        target_date = date.today()
    year, week, _ = target_date.isocalendar()
    return f"{year}-W{week:02d}"


def get_week_dir(direction_id, target_date=None):
    """获取指定方向当前周的目录路径"""
    week_str = get_week_str(target_date)
    return os.path.join(DATA_DIR, direction_id, week_str)


def load_existing_ids(direction_id):
    """加载该方向所有历史周已有的论文 ID 集合（用于全局去重）"""
    direction_dir = os.path.join(DATA_DIR, direction_id)
    ids = set()
    
    if not os.path.exists(direction_dir):
        return ids
        
    for week_folder in os.listdir(direction_dir):
        jsonl_path = os.path.join(direction_dir, week_folder, "papers.jsonl")
        if os.path.exists(jsonl_path):
            with open(jsonl_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            paper = json.loads(line)
                            ids.add(paper.get("id", ""))
                        except json.JSONDecodeError:
                            continue
    return ids


def append_papers(direction_id, papers):
    """
    将论文追加到当前周的 JSONL 文件。
    自动去重（基于 arxiv_id），返回新增论文数量。
    """
    week_dir = get_week_dir(direction_id)
    os.makedirs(week_dir, exist_ok=True)
    jsonl_path = os.path.join(week_dir, "papers.jsonl")

    existing_ids = load_existing_ids(direction_id)
    new_count = 0

    with open(jsonl_path, "a", encoding="utf-8") as f:
        for paper in papers:
            arxiv_id = extract_arxiv_id(paper.get("url", ""))

            if arxiv_id in existing_ids:
                continue

            record = {
                "id": arxiv_id,
                "title": paper.get("title", ""),
                "authors": paper.get("authors", []),
                "url": paper.get("url", ""),
                "pdf_url": paper.get("pdf_url", ""),
                "category": paper.get("category", ""),
                "published": str(paper.get("published", "")),
                "collected": datetime.now().strftime("%Y-%m-%d"),
                "abstract": paper.get("summary", ""),  # 保存原始英文摘要
                "has_code": paper.get("has_code", False),
                "repo_url": paper.get("repo_url", ""),
                "repo_stars": paper.get("repo_stars", 0),
                "hf_upvotes": paper.get("hf_upvotes", 0),
                "citation_count": paper.get("citation_count", 0),
                "venue": paper.get("venue", ""),
                "venue_year": paper.get("venue_year", ""),
                "venue_type": paper.get("venue_type", ""),
                "venue_url": paper.get("venue_url", ""),
                "venue_confidence": paper.get("venue_confidence", ""),
                "venue_source": paper.get("venue_source", ""),
                "extracted": paper.get("extracted", {}),
                "extraction_depth": paper.get("extraction_depth", "none"),
            }

            f.write(json.dumps(record, ensure_ascii=False) + "\n")
            existing_ids.add(arxiv_id)
            new_count += 1

    if new_count > 0:
        print(f"[Storage] ✅ {direction_id}: {new_count} 篇新论文已追加")
    else:
        print(f"[Storage] ℹ️ {direction_id}: 无新论文（全部已存在）")

    return new_count


def load_week_papers(direction_id, target_date=None):
    """加载指定周的所有论文数据"""
    week_dir = get_week_dir(direction_id, target_date)
    jsonl_path = os.path.join(week_dir, "papers.jsonl")

    papers = []
    if os.path.exists(jsonl_path):
        with open(jsonl_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        papers.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    return papers
