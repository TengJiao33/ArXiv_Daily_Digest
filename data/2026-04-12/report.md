# 🧪 ArXiv AI 日报

📅 **2026-04-12 周日** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **49,686** (¥0.0162)

## 🔥 今日必读

---

### 1. Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

🏷️ `cs.CV (计算机视觉)` | 📄 [arXiv](http://arxiv.org/abs/2604.08545v1)

👤 Shilin Yan, Jintao Tong, Hongwei Xue 等


**中文标题**: 明智行动：在智能体多模态模型中培养元认知工具使用

**背景与痛点**: 当前工具增强的多模态智能体普遍存在元认知缺陷，存在盲目调用工具的问题：哪怕问题可通过已有信息直接解决，也会触发工具调用，不仅带来严重延迟，还会引入额外噪声干扰推理。现有强化学习方案将精度与效率耦合为单奖励，惩罚过严抑制必要调用，惩罚过轻则被精度方差淹没，陷入两难无解。

**核心创新**: 本文提出分层解耦策略优化框架HDPO，从根本上重构了优化目标，将精度与效率从竞争的标量目标转为分层条件目标，拆分为两个正交优化通道，只在正确推理轨迹中优化工具调用效率，自然催生出先学正确性、再学高效性的隐式认知课程。

**技术细节**: HDPO保留两个独立优化通道：精度通道对所有采样轨迹用标准GRPO计算优势，全程优化任务正确性；效率通道仅统计回答正确的轨迹，工具奖励与调用次数成反比，仅当同prompt的正确轨迹不少于2条时才计算优势更新，最终总损失为两个通道损失的加权和。训练前还配套多阶段数据清洗，过滤掉 legacy 标注中不必要的工具调用示例和错误执行轨迹。

**实验结果**: 在十余种主流多模态推理基准（涵盖视觉感知、文档理解、数学推理）测试，相比基线标准GRPO，Metis将不必要工具调用率从98%降至2%，多个基准精度提升2-3个百分点，取得开源多模态智能体中的SOTA，验证了减少冗余调用可提升推理精度。

---

### 2. SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Natural Instructions

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.08477v1)

👤 Ashima Suvarna, Kendrick Phan, Mehrab Beikzadeh 等


**中文标题**: SUPERNOVA：基于自然指令强化学习激发大语言模型通用推理能力
**背景与痛点**: 当前带可验证奖励的强化学习（RLVR）仅在数学、代码等形式化领域提升大模型推理效果，面向因果推断、时序理解等能力的通用推理领域，缺乏高质量可验证RL训练数据，现有网络爬取数据噪声大，人工标注成本高，且STEM领域推理训练的能力无法迁移到通用推理。
**核心创新**: 提出面向通用推理RLVR的数据整理框架SUPERNOVA，核心思路是挖掘已有大规模人类标注指令调优数据的推理价值，将其改造适配RLVR训练要求，通过上百次控制实验总结出通用推理RL数据整理的可落地经验，不需要从零构建标注数据集。
**技术细节**: 整体分三阶段流程：首先从SuperNI的1600个任务中筛选83个候选，把开放型任务改造成可验证的选择题/固定答案格式，过滤过难、过易样本，按单任务训练后下游验证集的增益计算任务效用并排序；对比两种混合策略：宏观混合选总体表现Top任务，微观混合为每个下游子任务选各自Top任务再合并；测试发现多种合成难度增强干预均不优于原始高质量数据，训练采用GRPO算法。
**实验结果**: 在BBEH、Zebralogic、MMLU-Pro等通用推理基准测试，Qwen3全尺寸模型均获得稳定提升，BBEH测试集上不同规模相对提升最高达52.8%，4B规模的SUPERNOVA模型性能超过两倍参数量的Qwen3-8B，增益可跨模型家族迁移。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Audi...](http://arxiv.org/abs/2604.08401v1) `cs.AI (人工智能)` | 解决LLM智能体中推理轨迹连贯但隐含逻辑错误、误导后续动作的痛点，提出行动前自审计机制，有效提升智能体推理忠实性，实用性强。 |
| 5 | [PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in ...](http://arxiv.org/abs/2604.08529v1) `cs.HC` | 解决个人AIAgent中自然语言生成的工具相互隔离、无法协同工作的痛点，提出PSI共享状态架构，让生成的自定义工具保持连贯一致性。 |
| 6 | [What Drives Representation Steering? A Mechanistic Case Study on Steering Refusa...](http://arxiv.org/abs/2604.08524v1) `cs.LG (机器学习)` | steering向量是当前高效的LLM对齐方法，但学界缺乏对其内部工作机制的可解释性研究，该工作做了 mechanistic 案例研究，基础价值高。 |
| 7 | [Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models ...](http://arxiv.org/abs/2604.08476v1) `cs.CV (计算机视觉)` | 多模态大模型用GRPO训练提升视觉空间推理准确率后，普遍存在输出不忠实的问题，该工作提出约束策略优化改进GRPO，提升推理可靠性。 |
| 8 | [KV Cache Offloading for Context-Intensive Tasks](http://arxiv.org/abs/2604.08426v1) `cs.LG (机器学习)` | 长上下文LLM落地中，KV缓存是内存占用和推理延迟的核心瓶颈，该工作针对密集上下文任务研究KV缓存卸载，解决实际部署痛点，工业价值高。 |
| 9 | [PIArena: A Platform for Prompt Injection Evaluation](http://arxiv.org/abs/2604.08499v1) 💻 `cs.CR (加密与安全)` | 提示注入是大模型应用的核心安全风险，但当前领域缺少统一标准化的评估平台，该工作提出PIArena填补空白，推动大模型安全技术发展。 |
| 10 | [KnowU-Bench: Towards Interactive, Proactive, and Personalized Mobile Agent Evalu...](http://arxiv.org/abs/2604.08455v1) `cs.AI (人工智能)` | 交互式个性化移动Agent是前沿方向，但现有基准无法覆盖其交互性、主动性、个性化的评估需求，该工作提出新基准填补领域空白。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-12
