# 🧪 ArXiv AI 日报

📅 **2026-03-05 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **48,223** (¥0.0160)

## 🔥 今日必读

---

### 1. AgentIR: Reasoning-Aware Retrival for Deep Research Agents

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.04384v1)

👤 Zijian Chen, Xueguang Ma, Shengyao Zhuang 等


**中文标题**: AgentIR：面向深度研究智能体的推理感知检索

**背景与痛点**: 深度研究智能体已成为检索系统的一类核心新用户，这类智能体每次检索前都会生成显式自然语言推理轨迹，蕴含丰富搜索意图与多轮上下文，但现有检索系统完全忽略了这个免费可用的信号，同时也缺少适配深度研究多轮子查询的检索训练数据。

**核心创新**: 提出推理感知检索新范式，直接利用智能体本身生成的推理轨迹作为检索增强信号，联合编码推理轨迹与查询获得更精准的搜索嵌入；同时提出DR-Synth数据合成方法，从现有标准QA数据集自动生成训练数据，无需人工标注，也不会带来额外推理开销。

**技术细节**: 采用固定模板拼接当前轮智能体生成的推理轨迹和查询，输入预训练嵌入模型得到联合表征；训练使用对比损失，拉近正例文档与输入的余弦相似度，拉远负例。DR-Synth让智能体在标准QA上生成多轮搜索轨迹，提取每轮推理-查询对后，基于全局问题和标准答案做oracle重排序，标注正例和难负例，仅保留成功求解的轨迹用于训练，最终基于Qwen3-Embedding-4B微调得到目标模型。

**实验结果**: 在深度研究权威基准BrowseComp-Plus测试，搭配通义DeepResearch智能体，4B参数的AgentIR-4B取得68%端到端准确率，较两倍规模的传统嵌入模型提升18个绝对百分点，较BM25提升31个百分点，可零样本泛化到不同推理风格的其他智能体，还能减少搜索轮次提升效率。

---

### 2. Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.04257v1)

👤 Zhenting Wang, Huancheng Chen, Jiayun Wang 等


**中文标题**: Memex(RL)：通过索引化经验记忆扩展长周期大语言模型智能体
**背景与痛点**: 长周期LLM智能体完成数十上百步工具调用任务时，历史交互会快速耗尽有限上下文窗口。现有方案靠截断或有损压缩生成摘要，会永久丢弃后续可能需要的关键历史证据；基于语义相似度的外部检索又容易模糊出错，大多依赖手工启发式规则，无法适配复杂长任务需求。
**核心创新**: 提出「压缩上下文但不丢弃证据」的设计思路，核心是索引化经验记忆机制，将紧凑的带索引摘要放在工作上下文，全量原始交互归档在外部键值存储，智能体可按需精确取回所需内容，再用强化学习联合学习记忆的读写行为，相比纯摘要方法信息损失小得多。
**技术细节**: 维护两层存储：上下文内仅保留紧凑结构化的索引摘要（包含任务进度、索引-描述映射对），全量原始交互、工具输出存在外部键值经验库。核心操作包括压缩归档（将长历史替换为索引摘要，写入全量内容到外部库）和按需检索（按索引取回精确内容注入上下文）。MemexRL基于GRPO框架优化，奖励融合任务成功率，减去上下文溢出、冗余工具调用、格式错误三个惩罚，分段轨迹处理保证长轨迹信用分配，压缩时机由智能体自主学习。
**实验结果**: 在修改后的高难度ALFWorld长周期任务上测试，经过MemexRL训练后，任务成功率从24.2%提升到85.6%，同时峰值工作上下文长度降低43%，验证了该方法能在紧凑上下文预算下大幅提升长周期任务性能。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [$V_1$: Unifying Generation and Self-Verification for Parallel Reasoners](http://arxiv.org/abs/2603.04304v1) `cs.CL (计算语言学)` | 针对复杂推理任务测试时缩放的需求，统一生成与自验证框架，提升多方案并行推理的效果，推动LLM复杂推理能力的升级。 |
| 5 | [Dissecting Quantization Error: A Concentration-Alignment Perspective](http://arxiv.org/abs/2603.04359v1) `cs.LG (机器学习)` | 从浓度-对齐的新视角拆解大模型量化误差，为解决量化后精度下降问题提供新分析思路，对大模型端侧落地有重要价值。 |
| 6 | [RoboCasa365: A Large-Scale Simulation Framework for Training and Benchmarking Ge...](http://arxiv.org/abs/2603.04356v1) `cs.RO (机器人)` | 针对通用机器人研究缺少大规模训练评测基准的痛点，发布RoboCasa365大规模仿真框架，助力通用机器人技术的研发。 |
| 7 | [Retrieval or Representation? Reassessing Benchmark Gaps in Multilingual and Visu...](http://arxiv.org/abs/2603.04238v1) `cs.CL (计算语言学)` | 厘清了多语言、富视觉RAG任务中检索能力和表示能力的作用，重新梳理领域基准缺口，对RAG技术迭代和基准建设有指导意义。 |
| 8 | [Efficient Refusal Ablation in LLM through Optimal Transport](http://arxiv.org/abs/2603.04355v1) `cs.LG (机器学习)` | 针对大模型安全对齐中的拒绝行为优化需求，提出基于最优传输的高效拒绝消融方案，效果优于现有方法，对齐效率显著提升。 |
| 9 | [ZipMap: Linear-Time Stateful 3D Reconstruction with Test-Time Training](http://arxiv.org/abs/2603.04385v1) `cs.CV (计算机视觉)` | 解决了现有Transformer 3D重建方法计算复杂度随输入二次增长的痛点，提出线性时间有状态重建方案，效率提升显著，实用性强。 |
| 10 | [Agentics 2.0: Logical Transduction Algebra for Agentic Data Workflows](http://arxiv.org/abs/2603.04241v1) `cs.AI (人工智能)` | 针对企业部署Agentic AI对可靠性、可观测性的需求，提出逻辑转导代数框架，推动Agent技术从研究原型落地到企业生产场景。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-05
