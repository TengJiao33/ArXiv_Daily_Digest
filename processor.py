"""
Research Radar — 论文结构化信息提取模块
使用豆包 AI 从论文摘要中提取 problem/method/limitations 等结构化字段。
这是整个系统的"翻译层"——把英文摘要变成可分析的结构化数据。
"""

import json
import time


# ─── 提取 Prompt ──────────────────────────────────────────

EXTRACTION_SYSTEM = """你是一位学术论文信息提取助手。你的任务是从论文摘要中提取结构化信息。
你只需要提取，不需要评价或推荐。输出必须严格为 JSON 格式。"""

EXTRACTION_PROMPT = """从以下论文摘要中提取结构化信息。

标题: {title}
摘要: {abstract}

请严格按以下 JSON 格式输出（不要输出任何其他内容）：
```json
{{
  "problem": "该研究针对什么问题？（30-50字中文）",
  "method": "核心方法是什么？（30-50字中文）",
  "contribution": "主要贡献/结果是什么？（30-50字中文）",
  "limitations": "论文提到的局限性或未解决的问题（30-50字中文，如果摘要中没提到写'摘要未提及'）",
  "assumptions": "论文隐含的关键假设（30-50字中文，如果不明显写'无明显假设'）",
  "future_work": "论文提到的未来工作方向（30-50字中文，如果没提到写'未提及'）",
  "baselines": ["对比的基线方法1", "基线方法2"],
  "datasets": ["使用的数据集1", "数据集2"]
}}
```

注意：
- 全部用中文输出
- limitations 和 assumptions 是最重要的字段，请认真提取
- 如果摘要信息不足，如实写"摘要未提及"，不要编造"""


def _empty_extracted():
    """返回空的提取结果（提取失败时使用）"""
    return {
        "problem": "提取失败",
        "method": "提取失败",
        "contribution": "提取失败",
        "limitations": "提取失败",
        "assumptions": "提取失败",
        "future_work": "提取失败",
        "baselines": [],
        "datasets": [],
    }


def extract_paper_info(paper, client):
    """
    对单篇论文进行结构化信息提取。
    返回提取结果字典，失败时返回默认空字典。
    """
    prompt = EXTRACTION_PROMPT.format(
        title=paper["title"],
        abstract=paper.get("summary", ""),
    )

    try:
        response, usage = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            system_prompt=EXTRACTION_SYSTEM,
            max_tokens=512,
        )

        if not response:
            return _empty_extracted()

        # 清理 markdown 代码块包裹
        clean = response.strip()
        if clean.startswith("```"):
            clean = clean.split("\n", 1)[1]
            clean = clean.rsplit("```", 1)[0]

        return json.loads(clean)

    except (json.JSONDecodeError, Exception) as e:
        print(f"[Processor] ⚠️ 提取失败: {paper['title'][:40]}... — {e}")
        return _empty_extracted()


def extract_batch(papers, client, delay=1.0):
    """
    批量提取论文信息。
    每次调用之间间隔 delay 秒，避免触发豆包限流。
    返回带有 extracted 字段的论文列表。
    """
    results = []
    total = len(papers)

    for i, paper in enumerate(papers):
        print(f"[Processor] ({i+1}/{total}) 提取: {paper['title'][:50]}...")
        extracted = extract_paper_info(paper, client)
        paper["extracted"] = extracted
        paper["extraction_depth"] = "abstract_only"
        results.append(paper)

        # 限流保护
        if i < total - 1:
            time.sleep(delay)

    success = sum(1 for p in results if p["extracted"]["problem"] != "提取失败")
    print(f"[Processor] ✅ 提取完成: {success}/{total} 篇成功")
    return results
