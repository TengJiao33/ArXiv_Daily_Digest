# LLM 真值性与事实性 — 2026-W20 (05/11-05/17)

本周新增 **25** 篇论文。2 篇附带代码仓库。

## 分类分布

- `cs.CL`: 12 篇
- `cs.LG`: 5 篇
- `cs.AI`: 4 篇
- `cs.CV`: 2 篇
- `via-citation`: 1 篇
- `cs.CR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Beyond Reasoning: Reinforcement Learning Unlocks Parametric ...](http://arxiv.org/abs/2605.07153) | 在可控零样本单跳闭卷问答设置下，仅以二元正确性奖励训练，做事实级训练测试去重 | 证实强化学习可提升大模型参数知识召回，平均获约27%相对增益，拓展了强化学习应用... | — |
| 2 | [Geometric Factual Recall in Transformers](http://arxiv.org/abs/2605.12426v1) | 结合理论推导与实证分析，在单层和多跳场景下分析Transformer的几何记忆机... | 证明对数级嵌入维度即可满足记忆需求，给出多跳场景容量深度权衡与信息论下界 | — |
| 3 | [Scalable Token-Level Hallucination Detection in Large Langua...](http://arxiv.org/abs/2605.12384v1) | 提出TokenHD词级幻觉检测器训练管道，含可扩展标注合成引擎，采用重要性加权训... | 实现无需预定义步骤分割的检测，训练出的小模型性能超更大推理模型，跨场景泛化良好 | — |
| 4 | [GKnow: Measuring the Entanglement of Gender Bias and Factual...](http://arxiv.org/abs/2605.12299v1) | 构建GKnow基准评测数据集，通过神经元消融实验分析神经元与电路层面的性别特性 | 整理出GKnow基准数据集，发现消融去偏不可靠，现有偏见评测会掩盖事实性别知识下... | — |
| 5 | [Instruction Lens Score: Your Instruction Contributes a Power...](http://arxiv.org/abs/2605.12258v1) | 基于指令token嵌入特性的洞察，提出即插即用的InsLen物体幻觉检测方法 | InsLen无需辅助模型与额外训练，多基准多架构下优于现有方法，验证了其有效性鲁... | ✅ |
| 6 | [Mitigating Context-Memory Conflicts in LLMs through Dynamic ...](http://arxiv.org/abs/2605.12185v1) | 提出两阶段动态认知协调解码（DCRD），先评估上下文保真度预测冲突，再分路径处理... | 构建知识冲突QA基准ConflictKG，实验证明DCRD性能优于所有基线，达到... | — |
| 7 | [PrivacySIM: Evaluating LLM Simulation of User Privacy Behavi...](http://arxiv.org/abs/2605.12147v1) | 提出评测套件PrivacySIM，基于千名用户真实隐私响应基准，测试不同pers... | 提出隐私行为模拟评测套件PrivacySIM，得到多项关键发现，开放套件供后续研... | — |
| 8 | [Towards Order Fairness: Mitigating LLMs Order Sensitivity th...](http://arxiv.org/abs/2605.11974v1) | 提出双组优势优化DGAO，利用强化学习平衡组内准确率优势与组间稳定性优势 | 首次将强化学习用于缓解大语言模型顺序敏感度，提出两个新评估指标，多任务验证效果优... | ✅ |
| 9 | [Allegory of the Cave: Measurement-Grounded Vision-Language L...](http://arxiv.org/abs/2605.11727v1) | 提出测量接地的视觉语言学习方法，构建PRISM-VL，结合原始测量输入与曝光包围... | 验证保留测量域信息可提升VLM多模态推理性能，模型在测试基准上取得优于基线的结果... | — |
| 10 | [Three Regimes of Context-Parametric Conflict: A Predictive F...](http://arxiv.org/abs/2605.11574v1) | 提出三制度分析框架，区分参数强度与参数唯一性，通过多模型多阶段实验验证 | 提出情境-参数冲突的三制度框架，明确各制度主导预测因素，完成实证验证 | — |
| 11 | [StoicLLM: Preference Optimization for Philosophical Alignmen...](http://arxiv.org/abs/2605.11483v1) | 基于斯多葛基础文本微数据集，采用ORPO、AlphaPO偏好优化训练小型语言模型 | 验证仅300个高保真样本即可实现小模型斯多葛向内美德强对齐，效果接近少样本提示且... | — |
| 12 | [VERDI: Single-Call Confidence Estimation for Verification-Ba...](http://arxiv.org/abs/2605.11334v1) | 提出VERDI方法，将验证式评估分解为子检查提取三类结构信号，结合逻辑回归得到置... | 所提方法在多个公开基准和生产系统中表现优异，支持跨模型迁移，可实现可扩展提取 | — |
| 13 | [Grounded or Guessing? LVLM Confidence Estimation via Blind-I...](http://arxiv.org/abs/2605.10893v1) | 提出模型无关的BICR置信度估计框架，基于真实与黑屏图像的对比排名训练轻量探针 | 在多个LVLM和多任务测试中，BICR同时取得最优校准与判别性能，参数量远少于最... | — |
| 14 | [Do We Really Need External Tools to Mitigate Hallucinations?...](http://arxiv.org/abs/2605.14621v1) | 提出无需训练的SIRA内部对比解码框架，在模型内构建反事实参考做token级对比... | 无需训练与外部工具，稳定降低大视觉语言模型幻觉，保留描述能力且计算开销更低 | — |
| 15 | [When Answers Stray from Questions: Hallucination Detection v...](http://arxiv.org/abs/2605.14449v1) | 提出问答正交分解框架QAOD，对答案表示做正交分解，设计两种互补探测策略检测幻觉 | 两种探测策略分别在域内检测和跨域泛化取得最优性能，生成成本更低效果更优 | — |
| 16 | [Hypergraph Enterprise Agentic Reasoner over Heterogeneous Bu...](http://arxiv.org/abs/2605.14259v1) | 提出基于分层超图本体的企业推理器HEAR，以证据驱动推理循环完成结构化多跳分析 | 在供应链任务中最高准确率达94.7%，兼顾效率与正确性，为企业智能建立可扩展可审... | — |
| 17 | [ProtoMedAgent: Multimodal Clinical Interpretability via Priv...](http://arxiv.org/abs/2605.14113v1) | 提出ProtoMedAgent框架，在神经符号瓶颈上做测试时优化，加入基于k-匿... | 经临床队列验证，报告忠实度远高于标准RAG，可有效降低成员隐私推理风险 | — |
| 18 | [Know When To Fold 'Em: Token-Efficient LLM Synthetic Data Ge...](http://arxiv.org/abs/2605.14062v1) | 提出轻量无训练的多阶段生成中拒绝框架MSIFR，分阶段在生成中途检测终止低质量生... | 从理论证明早拒不会偏差样本效用，实验证实在保证精度的同时可大幅降低token消耗... | — |
| 19 | [Derivation Prompting: A Logic-Based Method for Improving Ret...](http://arxiv.org/abs/2605.14053v1) | 为检索增强生成框架的生成步骤提出基于逻辑推导的新提示方法，可构建可解释推导树 | 提升生成过程可控性与可解释性，案例研究显示相比基线显著减少不可接受回答 | — |
| 20 | [Bridging Legal Interpretation and Formal Logic: Faithfulness...](http://arxiv.org/abs/2605.14049v1) | 提出结合大语言模型表达能力与形式验证严谨性的神经符号方法构建法律AI | 可让AI辅助法律推理兼具能力与可靠性，减轻人工验证负担同时满足法律问责要求 | — |
| 21 | [Collider-Bench: Benchmarking AI Agents with Particle Physics...](http://arxiv.org/abs/2605.13950v1) | 提出Collider-Bench基准，基于公开资料评测大语言模型智能体重现LHC... | 发布源自LHC搜索的初始任务集、容器化沙盒与模拟工具，评测了多类通用编码智能体 | — |
| 22 | [Negation Neglect: When models fail to learn negations in tra...](http://arxiv.org/abs/2605.13829v1) | 在多个主流大语言模型上，使用人工构造的否定主张开展实验，对比不同否定表述的效果。 | 提出「否定忽视」现象，验证其普遍存在于主流大模型，证实该效应可延伸至AI安全场景... | — |
| 23 | [Where Does Reasoning Break? Step-Level Hallucination Detecti...](http://arxiv.org/abs/2605.13772v1) | 将幻觉建模为单前向隐藏态轨迹属性，提出带对比PCA的教师模型与蒸馏BiLSTM学... | 证明对比PCA是传输分离目标的最优投影，所提模型性能优于现有多个基线方法 | — |
| 24 | [PersonalAI 2.0: Enhancing knowledge graph traversal/retrieva...](http://arxiv.org/abs/2605.13481v1) | 提出PersonalAI 2.0框架，融入规划机制，采用多阶段动态查询实现自适应... | 所提框架在多个基准上优于现有方法，降低幻觉提升准确率，在MINE-1取得SOTA... | — |
| 25 | [GeoBuildBench: A Benchmark for Interactive and Executable Ge...](http://arxiv.org/abs/2605.13167v1) | 构建含489个经筛选验证的中文教材问题的基准，要求模型生成DSL程序完成几何构造 | 推出GeoBuildBench评估基准，开源相关代码，为接地可执行推理提供严谨测... | — |

## 常见基线方法

- **训练时基线** (1 篇引用)
- **推理时基线** (1 篇引用)
- **步骤级检测方法** (1 篇引用)
- **QwQ-32B** (1 篇引用)
- **现有物体幻觉检测方法** (1 篇引用)
- **对比解码方法** (1 篇引用)
- **动态解码方法** (1 篇引用)
- **无persona条件下的隐私行为模拟** (1 篇引用)
- **RGB Qwen3-VL-8B** (1 篇引用)
- **少样本提示** (1 篇引用)

## 本周提到的 Limitations

- 当前表现最优的模型准确率仅40.4%，远无法忠实模拟个体用户的隐私决策
- 所有模型都在斯多葛向外世界主义义务上持续失败，小模型表征局限无法仅靠微数据适配解决
- 学生模型在分布偏移下性能崩溃，部署核心障碍是分布偏移下保留对比传输裕度
- 现有SOTA多模态模型常出现结构幻觉、漏对象，利用反馈自我修正的能力十分有限

## 常用数据集

- **事实类问答基准** (1 篇使用)
- **DiFair** (1 篇使用)
- **GKnow** (1 篇使用)
- **StereoSet** (1 篇使用)
- **多个基准数据集** (1 篇使用)
- **ConflictKG** (1 篇使用)
- **六个QA数据集** (1 篇使用)
- **五项公开隐私领域用户研究数据** (1 篇使用)
- **一千名用户真实隐私响应数据集** (1 篇使用)
- **150K质量控制指令调优集** (1 篇使用)


---

*自动生成于 2026-05-17 | Research Radar*