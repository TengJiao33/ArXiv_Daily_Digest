"""
ArXiv_Daily_Digest — ArXiv 论文抓取模块
支持从 directions.yaml 读取多个研究方向，逐方向定向搜索。
"""

import re
import time

import arxiv


class ArxivScraper:
    """ArXiv 定向论文采集器"""

    def _paper_from_result(self, result):
        categories = list(result.categories) if result.categories else []
        primary_cat = categories[0] if categories else "unknown"

        return {
            "title": result.title,
            "authors": [a.name for a in result.authors],
            "summary": result.summary.replace("\n", " "),
            "published": result.published,
            "url": result.entry_id,
            "pdf_url": result.pdf_url,
            "category": primary_cat,
        }

    def fetch_papers(self, query, max_results=30):
        """
        执行单个方向的 ArXiv 搜索。
        :param query: ArXiv API 查询字符串（从 directions.yaml 读取）
        :param max_results: 最大返回数量
        :return: 论文字典列表
        """
        client = arxiv.Client()

        search = arxiv.Search(
            query=query,
            max_results=max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

        papers = []
        try:
            for result in client.results(search):
                papers.append(self._paper_from_result(result))
        except Exception as e:
            print(f"[Scraper] ❌ ArXiv 查询失败: {e}")

        print(f"[Scraper] 获取到 {len(papers)} 篇论文")
        return papers

    def fetch_papers_by_ids(self, arxiv_ids):
        """
        按 arXiv ID 拉取种子论文本体。
        directions.yaml 里的 seed_papers 既用于引用追踪，也用于把权威锚点本体送入后续结构化提取。
        """
        clean_ids = []
        seen = set()
        for raw_id in arxiv_ids or []:
            match = re.search(r"\d{4}\.\d{4,5}", str(raw_id))
            if not match:
                continue
            arxiv_id = match.group(0)
            if arxiv_id not in seen:
                clean_ids.append(arxiv_id)
                seen.add(arxiv_id)

        if not clean_ids:
            return []

        client = arxiv.Client(delay_seconds=3.1, num_retries=5)
        search = arxiv.Search(id_list=clean_ids, max_results=len(clean_ids))
        found = {}
        papers = []
        try:
            time.sleep(3.1)
            for result in client.results(search):
                arxiv_id = result.get_short_id().split("v")[0]
                found[arxiv_id] = self._paper_from_result(result)
        except Exception as e:
            print(f"[Scraper] ArXiv 种子论文拉取失败: {e}")
            return papers

        for arxiv_id in clean_ids:
            paper = found.get(arxiv_id)
            if paper:
                papers.append(paper)
            else:
                print(f"[Scraper] 未找到种子论文: {arxiv_id}")

        print(f"[Scraper] 获取到 {len(papers)}/{len(clean_ids)} 篇种子论文")
        return papers

