"""
Knowledge Editing Direction Radar — 论文结构化信息提取模块
使用豆包 AI 从论文摘要中提取 problem/method/limitations 等结构化字段。
这是整个系统的"翻译层"——把英文摘要变成可分析的结构化数据。
"""

import json
import time


# ─── 提取 Prompt ──────────────────────────────────────────

EXTRACTION_SYSTEM = """你是一位 knowledge editing / unlearning / reliability 方向的学术论文信息提取助手。
你的任务是从论文摘要中提取结构化信息，服务研究方向跟踪、读论文排序和选题判断。
你可以做轻量判断，但必须基于标题和摘要，不要编造。输出必须严格为 JSON 格式。"""

EXTRACTION_PROMPT = """从以下论文摘要中提取结构化信息。

标题: {title}
摘要: {abstract}

请严格按以下 JSON 格式输出（不要输出任何其他内容）：
```json
{{
  "title_zh": "论文标题的中文学术翻译（忠实、简洁）",
  "abstract_zh": "论文摘要的中文翻译（保留关键术语、方法名和指标，100-250字）",
  "problem": "该研究针对什么问题？（30-50字中文）",
  "method": "核心方法是什么？（30-50字中文）",
  "contribution": "主要贡献/结果是什么？（30-50字中文）",
  "limitations": "论文提到的局限性或未解决的问题（30-50字中文，如果摘要中没提到写'摘要未提及'）",
  "assumptions": "论文隐含的关键假设（30-50字中文，如果不明显写'无明显假设'）",
  "future_work": "论文提到的未来工作方向（30-50字中文，如果没提到写'未提及'）",
  "baselines": ["对比的基线方法1", "基线方法2"],
  "datasets": ["使用的数据集1", "数据集2"],
  "key_finding": "这篇论文最具体、最独特的发现是什么？要求：写出具体的机制、数值或现象，而非笼统描述。例如'检测层(14)≠校正层(16)，最佳监控深度因任务而异'而非'发现了新现象'。（一句话，30-60字中文）",
  "theme": "这篇论文属于什么研究主题？用3-8个中文字概括，例如'层选择机制'、'安全引导'、'知识边界感知'、'探针分析'等",
  "method_family": "方法族/论文类型：从 locate-then-edit、meta-learning editor、memory-based editor、unlearning、evaluation/benchmark、framework/tooling、steering、survey、other 中选一个或用更贴切短语",
  "edit_target": "编辑或遗忘的对象：factual association / behavior / safety knowledge / private data / benchmark knowledge / representation / parameter / unknown 等，中文短语",
  "evaluation_signal": "摘要中最值得关注的评测信号，如 locality/generality/specificity/portability/robustness/retain-forget tradeoff/side effect/代码或基准，30-60字中文",
  "failure_mode": "这篇论文暴露或试图解决的失败模式，如编辑串扰、顺序编辑崩溃、遗忘不彻底、保留能力下降；如果摘要未提及写'摘要未提及'",
  "idea_hook": "对 knowledge editing / unlearning / reliability 方向可延展的一句话选题钩子，30-60字中文；若不相关写'暂不明显'",
  "read_priority": "high / medium / low 三选一，按方向相关性、方法新意、评测价值和代码/基准价值判断",
  "direction_fit": "为什么这篇论文适合或不适合当前研究方向，20-50字中文"
}}
```

注意：
- 全部用中文输出
- title_zh 和 abstract_zh 要忠实翻译原文，不要添加摘要中没有的信息
- key_finding 是最重要的字段——要具体到机制、数值、现象层面，拒绝空泛描述
- theme 要简短精准，同一研究主题的不同论文应使用相同的 theme 词
- method_family 要尽量稳定，便于后续按方法族聚合
- read_priority 只输出 high、medium 或 low，不要输出中文
- limitations 和 assumptions 请认真提取
- 如果摘要信息不足，如实写"摘要未提及"，不要编造"""


def _empty_extracted():
    """返回空的提取结果（提取失败时使用）"""
    return {
        "title_zh": "提取失败",
        "abstract_zh": "提取失败",
        "problem": "提取失败",
        "method": "提取失败",
        "contribution": "提取失败",
        "limitations": "提取失败",
        "assumptions": "提取失败",
        "future_work": "提取失败",
        "baselines": [],
        "datasets": [],
        "key_finding": "提取失败",
        "theme": "未分类",
        "method_family": "未分类",
        "edit_target": "未知",
        "evaluation_signal": "提取失败",
        "failure_mode": "提取失败",
        "idea_hook": "提取失败",
        "read_priority": "low",
        "direction_fit": "提取失败",
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
            max_tokens=1200,
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
