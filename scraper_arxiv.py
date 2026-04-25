"""
ArXiv 论文抓取模块（Research Radar 版）
支持从 directions.yaml 读取多个研究方向，逐方向定向搜索。
"""

import arxiv


class ArxivScraper:
    """ArXiv 定向论文采集器"""

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
                categories = list(result.categories) if result.categories else []
                primary_cat = categories[0] if categories else "unknown"

                paper = {
                    "title": result.title,
                    "authors": [a.name for a in result.authors],
                    "summary": result.summary.replace("\n", " "),
                    "published": result.published,
                    "url": result.entry_id,
                    "pdf_url": result.pdf_url,
                    "category": primary_cat,
                }
                papers.append(paper)
        except Exception as e:
            print(f"[Scraper] ❌ ArXiv 查询失败: {e}")

        print(f"[Scraper] 获取到 {len(papers)} 篇论文")
        return papers


if __name__ == "__main__":
    scraper = ArxivScraper()
    results = scraper.fetch_papers(
        "(abs:truthfulness OR abs:hallucination) AND (cat:cs.CL OR cat:cs.AI)",
        max_results=5,
    )
    for p in results:
        print(f"  [{p['category']}] {p['title'][:60]}...")
