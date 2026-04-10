# 🧪 ArXiv AI 日报

📅 **2026-04-10 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **50,085** (¥0.0164)

## 🔥 今日必读

---

### 1. Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

🏷️ `cs.CV (计算机视觉)` | 📄 [arXiv](http://arxiv.org/abs/2604.08545v1)

👤 Shilin Yan, Jintao Tong, Hongwei Xue 等


**中文标题**: 明智行动：在智能体多模态模型中培养元认知工具使用能力

**背景与痛点**: 当前工具增强的多模态智能体普遍存在元认知缺陷，无法正确判断何时依赖内部知识、何时调用外部工具，存在“盲目调用工具”的问题，既增加推理延迟，还会引入冗余噪声干扰推理。现有强化学习方法将准确率和工具效率耦合为单一标量奖励，惩罚过严会抑制必要工具调用，惩罚过轻则信号被准确率方差淹没，无法解决过度用工具的问题。

**核心创新**: 打破了现有方法将任务准确率和工具效率耦合优化的范式，提出将工具效率从竞争标量目标转为条件目标，通过解耦优化消除两个目标的梯度干扰，自然诱导出“先掌握任务正确性、再优化工具调用效率”的隐性认知课程，从根本上解决了盲目调用工具的问题，打破了准确率和效率必须此消彼长的误区。

**技术细节**: 算法每次迭代对每个问题采样多条推理轨迹，分两个独立通道优化：1.准确率通道：对所有轨迹计算包含正确性、格式合规性的奖励，用标准GRPO计算优势，优化任务整体正确性；2.效率通道：仅筛选答对的轨迹参与计算，奖励值与工具调用次数成反比，仅在正确轨迹集合内计算优势，错误轨迹不提供效率梯度，避免模型为省工具故意答错。最终总损失为两个通道损失的加权和，配套多阶段数据清洗过滤低质量、不需要工具的样本。

**实验结果**: 在高分辨率视觉感知、文档理解、多模态数学推理等十余个主流基准测试，训练得到的Metis模型将工具调用率从原有方法的98%降至2%，同时全面超越现有开源多模态智能体的准确率，在WeMath基准上相对基线提升26.4个百分点，验证了方法的有效性。

---

### 2. SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.08477v1)

👤 Ashima Suvarna, Kendrick Phan, Mehrab Beikzadeh 等


**中文标题**: SUPERNOVA：基于自然指令强化学习激发大语言模型通用推理能力

**背景与痛点**: 当前可验证奖励强化学习（RLVR）仅在数学、代码等形式领域提升大模型推理效果，在因果推理、时序理解等通用推理任务上表现不佳。现有扩展方法多依赖噪声大的网络爬取数据，且数学推理能力无法有效迁移到通用场景，缺少适配RLVR的高质量通用推理训练数据方案。

**核心创新**: 核心发现现有大量人工标注的指令调优数据集已经蕴含丰富的通用推理模式，无需从零构建新数据，仅需适配改造即可用于RLVR训练。提出SUPERNOVA多阶段数据整理框架，通过百组控制实验总结出面向通用推理的RLVR数据整理实用原则。

**技术细节**: 框架分三阶段实现：1.任务选择：从Super Natural Instructions筛选候选任务，将原开放指令改造成可验证的问答/多选格式，过滤过难（胜率0）过易（胜率1）样本，按单任务训练后的下游推理增益计算任务效用并排序；2.任务混合：对比宏观混合（按整体平均选top任务）和微观混合（按每个目标子任务分别选top，再取并集）；3.测试多种合成难度增强干预，最终采用控制实验得到的最优组合，用GRPO算法做强化学习训练。

**实验结果**: 在BBEH、Zebralogic、MMLU-Pro等多个通用推理基准测试，0.6B到4B不同规模Qwen模型经SUPERNOVA训练后，在BBEH上相对基线最高提升52.8%，4B模型性能超过两倍参数量的Qwen3-8B，提升效果可跨模型家族泛化。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Audi...](http://arxiv.org/abs/2604.08401v1) `cs.AI (人工智能)` | 针对LLM智能体中存在连贯推理却违反逻辑或事实的痛点，提出动作执行前自我审计的机制，有效提升智能体推理的忠实性与可靠性。 |
| 5 | [Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models ...](http://arxiv.org/abs/2604.08476v1) `cs.CV (计算机视觉)` | 解决多模态大模型用GRPO训练时，精度提升但推理不忠实的问题，提出约束策略优化方法，有效提升了视觉空间推理的可靠度。 |
| 6 | [PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in ...](http://arxiv.org/abs/2604.08529v1) `cs.HC` | 针对个人AI生成的自定义工具普遍孤立无法协同的痛点，提出PSI共享状态架构，让独立生成的工具能状态一致协同工作，实用性很强。 |
| 7 | [What Drives Representation Steering? A Mechanistic Case Study on Steering Refusa...](http://arxiv.org/abs/2604.08524v1) `cs.LG (机器学习)` | 方向向量 steering是高效的LLM对齐调优方法，但此前缺乏可解释性研究，该工作分析其内在机制，解释了拒绝行为的原理，推进对齐可解释性研究。 |
| 8 | [KV Cache Offloading for Context-Intensive Tasks](http://arxiv.org/abs/2604.08426v1) `cs.LG (机器学习)` | 长上下文LLM落地中，KV缓存是内存和延迟的核心瓶颈，该工作优化KV缓存卸载方案，适配上下文密集型任务，缓解落地瓶颈，工业价值高。 |
| 9 | [ClawBench: Can AI Agents Complete Everyday Online Tasks?](http://arxiv.org/abs/2604.08523v1) `cs.CL (计算语言学)` | 现有AI Agent评测缺乏真实日常在线任务的统一测试基准，该工作提出ClawBench，填补了日常真实任务Agent评测的领域空白。 |
| 10 | [Phantasia: Context-Adaptive Backdoors in Vision Language Models](http://arxiv.org/abs/2604.08395v1) `cs.CV (计算机视觉)` | 揭示了视觉语言模型中新型上下文自适应后门攻击，发现了多模态模型之前未被关注的安全风险，对VLM安全研究有重要参考价值。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-10
