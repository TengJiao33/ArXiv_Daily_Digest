"""
GitHub 代码检查模块（辅助角色）
检查论文摘要中是否包含 GitHub 链接，验证仓库是否有效。
不作为论文筛选条件，只作为信息提示。
"""

import re
import requests
import os


class CodeHunter:
    """检查论文是否附带可用的 GitHub 代码仓库"""

    def __init__(self, github_token=None):
        self.github_token = github_token
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if self.github_token:
            self.headers["Authorization"] = f"token {self.github_token}"

    def extract_github_links(self, text):
        """从文本中提取 GitHub 仓库链接"""
        if not text:
            return []
        return re.findall(r'(https?://github\.com/[a-zA-Z0-9._-]+/[a-zA-Z0-9._-]+)', text)

    def check_repo(self, repo_url):
        """
        检查 GitHub 仓库是否有效且包含代码。
        返回: (has_code, repo_info)
          - has_code: bool
          - repo_info: {"stars": int, "desc": str, "url": str} 或 {}
        """
        match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
        if not match:
            return False, {}

        owner, repo = match.groups()
        repo = repo.rstrip('.git')
        api_url = f"https://api.github.com/repos/{owner}/{repo}"

        try:
            resp = requests.get(api_url, headers=self.headers, timeout=10)
            if resp.status_code != 200:
                return False, {}

            repo_data = resp.json()
            if repo_data.get("size", 0) == 0:
                return False, {}

            return True, {
                "stars": repo_data.get("stargazers_count", 0),
                "desc": repo_data.get("description", ""),
                "url": repo_url,
            }
        except Exception:
            return False, {}

    def check_paper(self, paper):
        """
        检查一篇论文是否有可用的 GitHub 代码。
        返回: (has_code, repo_info)
        """
        links = self.extract_github_links(paper.get("summary", ""))
        if not links:
            return False, {}

        # 检查第一个找到的链接
        return self.check_repo(links[0])
