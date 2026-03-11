# 🧪 ArXiv AI 日报

📅 **2026-03-11 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **46,721** (¥0.0156)

## 🔥 今日必读

---

### 1. Model Merging in the Era of Large Language Models: Methods, Applications, and Future Directions

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.09938v1)

👤 Mingyang Song, Mao Zheng


**中文标题**: 大语言模型时代的模型合并：方法、应用与未来方向

**背景与痛点**: 当前开源微调大语言模型爆发式增长，从业者需要组合不同模型的专业化能力，传统集成方案推理开销高，全量重训成本极高，已有研究零散，现有综述仅覆盖部分技术分支，缺乏从理论到工程落地的统一系统化梳理框架。

**核心创新**: 这是一篇针对大语言模型模型合并领域的系统性综述，首次提出FUSE四维度分类框架，从「为什么合并可行」「如何执行合并」「适用场景」「落地支撑资源」四个维度结构化整整个领域，系统分析不同方法的实践 tradeoff，明确核心开放挑战，为社区提供清晰的研究与应用基础。

**技术细节**: FUSE框架将领域划分为四个模块：基础层梳理了损失景观几何、线性模式连通性、权重排列对称性三大核心理论，明确了共享初始化、架构兼容等合并成功的前提条件；合并策略层按技术演进路径，分类梳理了权重平均、任务向量算术、稀疏增强合并、MoE结构路由、进化搜索五大类方法，逐个分析核心逻辑、代表工作和实用优劣；最后覆盖应用场景与开源工具生态。

**实验结果**: 本文整合了领域现有实证结论，验证了共享初始化可为合并提供强线性模式连通性，稀疏增强方法可有效缓解参数冲突，合理合并得到的模型性能可超越单个源模型，同时指出领域仍存在理论缺口、大模型扩展性、标准化不足等核心开放问题。

---

### 2. Thinking to Recall: How Reasoning Unlocks Parametric Knowledge in LLMs

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.09906v1)

👤 Zorik Gekhman, Roee Aharoni, Eran Ofek 等


**中文标题**: 思考以回忆：推理如何解锁大语言模型中的参数知识

**背景与痛点**: 现有研究普遍认为推理只对多跳问答、数学计算这类复杂任务有用，默认简单单跳事实问答不需要分步推理，既不清楚推理对大模型参数知识召回的实际作用，也未拆解背后的核心驱动机制，仅观测到表层的准确率提升。

**核心创新**: 本文打破直觉，证实哪怕对不需要逻辑分解的简单单跳事实问题，开启推理也能大幅扩展大模型参数知识的召回边界，解锁模型已存储但原本无法生成的正确答案；进一步通过控制实验拆解出两大核心作用机制，揭示了中间幻觉的风险并给出可落地的优化方案。

**技术细节**: 本文采用可开关推理模式的混合大模型控制变量，用pass@k指标衡量模型知识召回的能力边界。通过对照实验拆解两大机制：第一计算缓冲效应，将推理替换为等长无意义占位符，性能仍优于关闭推理基线，证明额外token可提供独立于语义的隐式计算空间，该效应存在饱和点；第二事实预激活，提取推理中的相关事实作为额外输入，关闭推理仍能恢复大部分推理增益，证明生成相关事实可搭建语义桥促进答案召回。

**实验结果**: 在SimpleQA-Verified和EntityQuestions两个闭卷问答数据集，Gemini 2.5系列、Qwen3-32B三个模型上测试，开启推理后pass@k最高提升近一倍，能力越弱的模型获益越大；测试阶段优先选择无中间幻觉的推理轨迹，可带来最高12.2%的相对准确率提升。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Good Reasoning Makes Good Demonstrations: Implicit Reasoning Quality Supervision...](http://arxiv.org/abs/2603.09803v1) `cs.LG (机器学习)` | 现有强化推理方法仅以最终答案对错为奖励，忽略推理过程质量，本文提出上下文强化学习实现隐式推理质量监督，有效提升大模型推理表现。 |
| 5 | [MSSR: Memory-Aware Adaptive Replay for Continual LLM Fine-Tuning](http://arxiv.org/abs/2603.09892v1) `cs.LG (机器学习)` | 针对动态环境下大模型持续微调的灾难性遗忘痛点，提出记忆感知自适应重放方法，兼顾性能和遗忘抑制，对LLM落地动态场景很实用。 |
| 6 | [Think Before You Lie: How Reasoning Improves Honesty](http://arxiv.org/abs/2603.09957v1) `cs.AI (人工智能)` | 现有研究对LLM欺骗行为的产生机制缺乏深入理解，本文揭示推理过程能有效提升LLM诚实性，对大模型安全对齐研究有重要价值。 |
| 7 | [GAST: Gradient-aligned Sparse Tuning of Large Language Models with Data-layer Se...](http://arxiv.org/abs/2603.09865v1) `cs.LG (机器学习)` | 针对大模型参数高效微调的效率瓶颈，提出梯度对齐的稀疏调优框架，结合数据层选择，兼顾性能和调优效率，对大模型适配落地很有帮助。 |
| 8 | [World2Mind: Cognition Toolkit for Allocentric Spatial Reasoning in Foundation Mo...](http://arxiv.org/abs/2603.09774v1) `cs.AI (人工智能)` | 当前多模态大模型的空间推理能力普遍偏弱，本文提出认知对齐的推理工具包，提升异中心空间推理性能，推动空间相关AI任务发展。 |
| 9 | [MedMASLab: A Unified Orchestration Framework for Benchmarking Multimodal Medical...](http://arxiv.org/abs/2603.09909v1) 💻 `cs.AI (人工智能)` | 医疗多模态多智能体研究存在架构碎片化、缺乏标准化基准的问题，本文提出统一编排基准框架，推动临床决策AI的规范化研究。 |
| 10 | [From Data Statistics to Feature Geometry: How Correlations Shape Superposition](http://arxiv.org/abs/2603.09972v1) 💻 `cs.LG (机器学习)` | 针对大模型 mechanistic 可解释性中特征叠加的成因不清晰问题，本文从数据相关性到特征几何角度解释叠加形成，推进可解释性理论研究。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-11
