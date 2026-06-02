"""
ArXiv_Daily_Digest — 论文结构化信息提取模块

使用豆包 AI 从论文摘要中提取 problem/method/limitations 等结构化字段。
这是整个系统的"翻译层"：把英文摘要变成可分析、可排序、可用于导师对齐的结构化数据。
"""

import json
import time


EXTRACTION_SYSTEM = """你是一位 LLM/Agent reliability、agent harness、model control、unlearning 与 factuality 方向的学术论文信息提取助手。
你的任务是从论文标题、摘要和当前研究方向中提取结构化信息，服务研究方向跟踪、读论文排序、两周一次导师选题对齐。
你可以做轻量判断，但必须基于标题和摘要，不要编造。输出必须严格为 JSON 格式。"""

EXTRACTION_PROMPT = """从以下论文摘要中提取结构化信息。

当前研究方向: {direction_name}
方向说明: {direction_description}
标题: {title}
摘要: {abstract}

请严格按以下 JSON 格式输出（不要输出任何其他内容）：
```json
{{
  "title_zh": "论文标题的中文学术翻译（忠实、简洁）",
  "abstract_zh": "论文摘要的中文翻译（保留关键术语、方法名和指标，100-250字）",
  "problem": "该研究针对什么问题？（30-60字中文）",
  "method": "核心方法是什么？（30-60字中文）",
  "contribution": "主要贡献/结果是什么？（30-60字中文）",
  "limitations": "论文提到的局限性或未解决的问题（30-60字中文，如果摘要中没提到写'摘要未提及'）",
  "assumptions": "论文隐含的关键假设（30-60字中文，如果不明显写'无明显假设'）",
  "future_work": "论文提到的未来工作方向（30-60字中文，如果没提到写'未提及'）",
  "baselines": ["对比的基线方法1", "基线方法2"],
  "datasets": ["使用的数据集/环境/benchmark 1", "数据集/环境/benchmark 2"],
  "key_finding": "这篇论文最具体、最独特的发现是什么？写出机制、数值、现象或失败模式，不要空泛。（一句话，30-70字中文）",
  "theme": "这篇论文属于什么研究主题？用3-10个中文字概括，例如'可执行技能'、'多Agent一致性'、'奖励学习'、'事实性评测'",
  "method_family": "方法族/论文类型：从 agent harness、skill generation、tool-use control、multi-agent coordination、consistency detection、policy optimization、online distillation、reward learning、factuality benchmark、unlearning/safety、model steering、evaluation/benchmark、survey、other 中选一个或写更贴切短语",
  "edit_target": "被控制、编辑、遗忘或约束的对象：agent action / tool use / workflow / factual knowledge / safety knowledge / private data / reasoning behavior / reward policy / representation / parameter / unknown 等，中文短语",
  "agent_setting": "如果涉及 agent，说明环境和任务形态，如 web/OS/coding/search/KBQA/multi-agent/tool-use；若不涉及写'非Agent论文'",
  "control_mechanism": "论文如何控制或改进模型/agent 行为，如 harness、skill program、verifier、debate、reward、distillation、steering、unlearning、benchmark feedback；30-60字中文",
  "evaluation_environment": "主要评测环境、任务或指标，如 WebArena、OSWorld、SWE-bench、HotpotQA、RuleArena、AntiLeakBench、accuracy/success rate/consistency；若摘要未提及写'摘要未提及'",
  "evaluation_signal": "摘要中最值得关注的评测信号，如 success rate、consistency、side effect、retain-forget tradeoff、hallucination、代码或基准，30-70字中文",
  "failure_mode": "这篇论文暴露或试图解决的失败模式，如工具误用、不一致、早期错误传播、奖励塌缩、遗忘不彻底、副作用；如果摘要未提及写'摘要未提及'",
  "reliability_risk": "从可靠性/工业落地角度看最大风险是什么？如副作用、不可复现、成本高、评测弱、数据污染、回滚困难；30-60字中文",
  "industrial_relevance": "high / medium / low 三选一，判断是否贴近工业界 agent/harness/reliability/应用需求",
  "idea_feasibility": "high / medium / low 三选一，判断本科远程实习阶段能否低成本形成复现、benchmark、demo 或分析实验",
  "compute_cost": "low / medium / high 三选一，估计实验算力和工程成本",
  "idea_hook": "对 LLM/Agent reliability、harness、factuality 或 safety 方向可延展的一句话选题钩子，30-70字中文；若不相关写'暂不明显'",
  "mentor_question": "下次和导师讨论时最值得问的一个判断问题，20-60字中文",
  "read_priority": "high / medium / low 三选一，按方向相关性、方法新意、评测价值、工业相关性和可行性判断",
  "direction_fit": "为什么这篇论文适合或不适合当前研究方向，20-60字中文"
}}
```

注意：
- 全部用中文输出，枚举字段 industrial_relevance / idea_feasibility / compute_cost / read_priority 只输出英文 high、medium 或 low。
- title_zh 和 abstract_zh 要忠实翻译原文，不要添加摘要中没有的信息。
- key_finding 要具体到机制、数值、现象或失败模式层面，拒绝空泛描述。
- method_family 和 theme 要尽量稳定，便于后续聚合。
- mentor_question 要像真实导师讨论问题，不要写成泛泛的"是否有意义"。
- 如果摘要信息不足，如实写"摘要未提及"，不要编造。"""


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
        "agent_setting": "提取失败",
        "control_mechanism": "提取失败",
        "evaluation_environment": "提取失败",
        "evaluation_signal": "提取失败",
        "failure_mode": "提取失败",
        "reliability_risk": "提取失败",
        "industrial_relevance": "low",
        "idea_feasibility": "low",
        "compute_cost": "high",
        "idea_hook": "提取失败",
        "mentor_question": "提取失败",
        "read_priority": "low",
        "direction_fit": "提取失败",
    }


def extract_paper_info(paper, client):
    """
    对单篇论文进行结构化信息提取。
    返回提取结果字典，失败时返回默认空字典。
    """
    prompt = EXTRACTION_PROMPT.format(
        direction_name=paper.get("direction_name", "未指定方向"),
        direction_description=paper.get("direction_description", "未提供方向说明"),
        title=paper["title"],
        abstract=paper.get("summary", "") or paper.get("abstract", ""),
    )

    try:
        response, usage = client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            system_prompt=EXTRACTION_SYSTEM,
            max_tokens=1600,
        )

        if not response:
            return _empty_extracted()

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

        if i < total - 1:
            time.sleep(delay)

    success = sum(1 for p in results if p["extracted"]["problem"] != "提取失败")
    print(f"[Processor] ✅ 提取完成: {success}/{total} 篇成功")
    return results
