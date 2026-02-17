"""
ArXiv 论文抓取模块
从 ArXiv API 获取 AI 相关领域的最新论文。
搜索范围：cs.CL (计算语言学) / cs.AI (人工智能) / cs.LG (机器学习)
"""

import arxiv


class ArxivScraper:
    def __init__(self, max_results=50):
        self.max_results = max_results

    def fetch_papers(self, query="cat:cs.CL OR cat:cs.AI OR cat:cs.LG"):
        """
        从 ArXiv 获取最新论文。
        默认搜索 cs.CL / cs.AI / cs.LG 三个分类，按提交日期排序。
        """
        client = arxiv.Client()

        search = arxiv.Search(
            query=query,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.SubmittedDate,
        )

        papers = []
        for result in client.results(search):
            # 提取分类标签（取主分类）
            categories = [c for c in result.categories] if result.categories else []
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

        print(f"[Scraper] 从 ArXiv 获取到 {len(papers)} 篇论文")
        return papers


if __name__ == "__main__":
    scraper = ArxivScraper(max_results=5)
    results = scraper.fetch_papers()
    print(f"获取 {len(results)} 篇论文")
    for p in results:
        print(f"  [{p['category']}] {p['title'][:60]}...")
