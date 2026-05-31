# LLM 真值性与事实性 — 2026-W22 (05/25-05/31)

本周新增 **29** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.CL`: 20 篇
- `via-citation`: 4 篇
- `cs.LG`: 2 篇
- `cs.CV`: 2 篇
- `cs.AI`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Mitigating Provenance-Role Collapse in Long-Term Agents via ...](http://arxiv.org/abs/2605.25869v1) | 提出类型化记忆中间表示MemIR，拆分记忆结构添加源监控约束，经多路由投影生成归... | 所提MemIR在实验中持续优于现有记忆基线，在需要源跟踪等的任务上性能提升显著 | — |
| 2 | [TIAR: Trajectory-Informed Advantage Reweighting for LLM Abst...](http://arxiv.org/abs/2605.25850v1) | 提出轨迹信息感知的优势重加权方法TIAR，在GRPO训练中动态调整弃权奖励 | 提出创新的弃权学习方法TIAR，在多个测试集上取得最优效果，完整保留原有基线准确... | — |
| 3 | [Double Triangle Annotation: A Scalable Human-in-the-Loop Fra...](http://arxiv.org/abs/2605.25781v1) | 提出双层人在回路双三角标注框架，利用跨模型共识自动标注，分歧交由人工和专家处理 | 取得高精度标注结果，自动接受超八成五标注，发布首个相关结构化提取真值基准 | — |
| 4 | [AutoSG: LLM-Driven Solver Generation Solely from Task Prompt...](http://arxiv.org/abs/2605.25658v1) | 提出全自动工作流AutoSG，包含检索增强生成、一步自精修、无实例评判三个核心模... | AutoSG生成的定制化求解器在多类昂贵优化任务上显著优于现有SOTA和已有LL... | — |
| 5 | [From Automation to Collaboration: Human-in-the-Loop Methods ...](http://arxiv.org/abs/2605.25226v1) | 本文调研梳理面向安全可信NLP的近期人在回路方法，分析人类专业知识在各环节的支撑... | 系统梳理相关研究进展，指出现有研究多处缺口，提出了可供参考的实用研究方向。 | — |
| 6 | [By Their Fruits You Will Know Them: Comparing Formalizations...](http://arxiv.org/abs/2605.25186v1) | 对同一法律条文的不同形式化做节点匹配构建共享接口，用SAT求解器枚举分歧边例转为... | 提出系统比较同一法律条文不同形式化的方法，并将其应用于大模型生成形式化的实践 | — |
| 7 | [LLM Agent Based Renewable Energy Forecasting Using Edge and ...](http://arxiv.org/abs/2605.25141v1) | 调研各类现有预测方法，探究大语言模型智能体整合多源数据构建统一决策支持流程。 | 提出覆盖预测全流程的六层分类体系，梳理出该领域目前存在的十二项开放研究挑战。 | — |
| 8 | [Faithfulness Metrics Don't Measure Faithfulness: A Meta-Eval...](http://arxiv.org/abs/2605.25052v1) | 构造输出可反映真实中间计算的任务，开发自动标注流水线得到真实保真度标签，构建基准... | 构建含3066条标注思维链的BonaFide基准，首次系统评估现有主流保真度指标 | — |
| 9 | [Language Bias in LVLMs: From In-Depth Analysis to Simple and...](http://arxiv.org/abs/2605.25036v1) | 提出语言偏差正则化LBR和语言偏差惩罚LBP，分别在调优与DPO训练中缓解语言偏... | 所提方法无需额外数据或辅助模型，有效缓解偏差，提升模型整体对齐与基准性能 | ✅ |
| 10 | [MimirRAG: A Multi-Agent RAG Framework for Financial Data Ret...](http://arxiv.org/abs/2605.25030v1) | 提出融合元数据集成的多智能体RAG框架MimirRAG，具备模块化完整处理流水线 | 该框架在FinanceBench取得89.3%准确率，优于基准，可提升金融领域的... | — |
| 11 | [Universal Boosts, Specific Suppressors: Sparse Autoencoder S...](http://arxiv.org/abs/2605.24977v1) | 无需更新模型权重，推理时基于逐令牌稀疏自编码器做解码残差引导，结合抑制增强干预 | 所提方法有效提升多个放射学VLM的报告质量，可零样本迁移，已发布相关工具资源 | — |
| 12 | [Mitigating Object Hallucinations in Vision-Language Models t...](http://arxiv.org/abs/2605.24957v1) | 提出无需训练的区域感知自适应加权推理策略，动态抑制诱发幻觉的注意力路径。 | 在多个标准多模态基准取得SOTA，有效减少幻觉，同时保留生成流畅性与语言先验。 | — |
| 13 | [MultiHaluDet: Multilingual Hallucination Detection via LLM H...](http://arxiv.org/abs/2605.24919v1) | 提出三阶段堆叠框架MultiHaluDet，探测冻结大模型全隐藏状态轨迹，无需语... | 实现最优多语言幻觉检测性能，在不同资源层级语言上泛化检测能力优于基线 | — |
| 14 | [Hallucination as Commitment Failure: Larger LLMs Misfire Des...](http://arxiv.org/abs/2605.22007) | 引入语义层面的答案可用性概念，聚合同一答案概念的token变体开展实验测试 | 明确了大语言模型幻觉产生的新机制，指出指令调优规模提升会催生更自信的幻觉 | — |
| 15 | [The Point of No Return: Counterfactual Localization of Decep...](http://arxiv.org/abs/2605.17113) | 提出反事实定位方法，对推理轨迹各句前缀重采样，估计欺骗结果的发生概率 | 构建五个自然涌现欺骗的测试环境，发布百万级句子规模的欺骗推理研究语料 | — |
| 16 | [Graph Alignment Topology as an Inductive Bias for Grounding ...](http://arxiv.org/abs/2605.22963) | 在参考信息与大模型输出间构建对齐二分图，训练图神经网络建模对齐结构 | 所提方法在四个不同幻觉与问答数据集上取得最优，性能超过包括GPT-4o在内的对比... | — |
| 17 | [Hallucination Behavior in Multimodal LLMs Across Agricultura...](http://arxiv.org/abs/2605.27595) | 围绕图像转文本、文本转图像两类任务，依据农业领域标准评估模型幻觉情况 | 系统评估多模态大模型农业影像任务的幻觉，识别出两类任务中反复出现的幻觉模式 | — |
| 18 | [CommunityFact: A Dynamic, Multilingual, Multi-domain Benchma...](http://arxiv.org/abs/2605.30241v1) | 引入面向真实场景错误信息检测的可更新基准CommunityFact，评估不同推理... | 构建了覆盖五语言两领域共15992条独立声明的基准，支撑错误信息检测研究 | — |
| 19 | [UniSteer: Text-Guided Flow Matching in Activation Space for ...](http://arxiv.org/abs/2605.30076v1) | 提出UniSteer文本引导激活流匹配模型，学习激活空间的通用条件速度场实现LL... | 在三个目标LLM上验证，可为多类LLM调控与激活空间分类任务提供统一接口 | — |
| 20 | [Towards Verifiable Multimodal Deep Research: A Multi-Agent H...](http://arxiv.org/abs/2605.29861v1) | 提出Ptah多智能体框架分阶段生成交错报告，配套PtahEval评估协议与验证机... | 提出新的多智能体框架与评估方案，实验证明生成的多模态报告优于现有强基线 | — |
| 21 | [Towards Localized and Disentangled Knowledge Editing for Mul...](http://arxiv.org/abs/2605.29826v1) | 提出LDKE框架，通过定位事实特定模型层，解耦目标相关与无关输入实现精准泛化编辑 | 在多个基准和多模态大模型实验验证，该方法泛化编辑能力优异同时保持高局部性 | — |
| 22 | [Teaching Language Models to Check Grounded Claim Factuality ...](http://arxiv.org/abs/2605.29712v1) | 将问题建模为正误阅读理解任务，用测试策略提示大模型，微调带自修正机制的小语言模型 | 方法比无引导推理减少超80%token用量，在一个基准取得SOTA，小模型性能媲... | — |
| 23 | [Verifiable Rewards Beyond Math and Code: Lightweight Corpus-...](http://arxiv.org/abs/2605.29648v1) | 提出CorVer，基于维基百科共现统计的轻量级语料接地句级过程奖励，仅需小模型和... | 多项实验验证其效果优于多个基线，训练速度大幅提升，显著提升事实问答准确率 | — |
| 24 | [DiffSpot: Can VLMs Spot Fine-Grained Visual Differences in W...](http://arxiv.org/abs/2605.29615v1) | 推出代码驱动的DiffSpot基准，通过修改单个CSS属性构造受控网页图像对，筛... | 构建了包含4400对图像的找差异基准，完成对13种前沿模型的零样本能力评估 | — |
| 25 | [K-FinHallu: A Hallucination Detection Benchmark for Multi-Tu...](http://arxiv.org/abs/2605.29523v1) | 基于语境可回答性分层分类法，构建韩语金融多轮对话，注入幻觉后评测大模型检测能力 | 推出首个面向韩语金融领域多轮RAG的幻觉检测基准K-FinHallu，填补了该领... | — |
| 26 | [Source-Grounded Semantic Reinforcement Learning for Low-Reso...](http://arxiv.org/abs/2605.29502v1) | 提出源接地语义强化学习SG-SRL框架，利用跨语言语义奖励做无参考强化学习，辅以... | 验证该方法提升语义接地与事实覆盖率，证明其在低资源语言场景具备良好泛化能力 | — |
| 27 | [Hallucination Detection-Guided Preference Optimization for C...](http://arxiv.org/abs/2605.28910v1) | 提出幻觉检测器引导的迭代修正，将修正轨迹转化为偏好对用于模型微调 | 所提方法可大幅降低临床摘要幻觉，同时保留摘要质量，提升了事实忠实度 | — |
| 28 | [Functional Entropy: Predicting Functional Correctness in LLM...](http://arxiv.org/abs/2605.28500v1) | 提出一系列代码专属功能等价方法，用LLM功能等价评估替换NLI语义等价，包含功能... | 系统评估多种UQ方法在代码生成任务的迁移效果，提出的方法在多数设置中性能优于对比... | — |
| 29 | [Skill0.5: Joint Skill Internalization and Utilization for Ou...](http://arxiv.org/abs/2605.28424v1) | 提出Skill0.5强化学习框架，通过动态难度感知路由，实现通用技能内化与特定技... | 解决了现有方法的两难困境，在分布内和分布外场景下性能均优于对比基线方法 | — |

## 常见基线方法

- **现有记忆基线** (1 篇引用)
- **静态三元基线** (1 篇引用)
- **多种对比基线** (1 篇引用)
- **传统手工标注** (1 篇引用)
- **大模型全自动标注流水线** (1 篇引用)
- **人类设计SOTA框架** (1 篇引用)
- **现有LLM生成求解器** (1 篇引用)
- **经典预测方法** (1 篇引用)
- **统计时间序列模型** (1 篇引用)
- **深度学习架构** (1 篇引用)

## 本周提到的 Limitations

- 现有研究在可扩展探测、可持续鲁棒基准、低资源场景、私有系统治理方面存在缺口。
- 领域仍存在十二项开放挑战，涉及实时部署、模型漂移、大语言模型幻觉控制等多方面。
- 现有保真度指标性能差、偏见强、长链表现差，计算成本高，当前保真度评价存在根本性缺口
- 所有接受评测的模型在合理拒答这一检测维度上的性能表现均为最差

## 常用数据集

- **TriviaQA** (2 篇使用)
- **LoCoMo** (1 篇使用)
- **BEAM-100K** (1 篇使用)
- **AbstentionBench全部测试数据集** (1 篇使用)
- **Guides Rosenwald** (1 篇使用)
- **摘要未提及** (1 篇使用)
- **九个前沿LLM生成的十个欧盟法律条款形式化** (1 篇使用)
- **BonaFide** (1 篇使用)
- **FinanceBench** (1 篇使用)
- **MIMIC-CXR** (1 篇使用)


---

*自动生成于 2026-05-31 | Research Radar*