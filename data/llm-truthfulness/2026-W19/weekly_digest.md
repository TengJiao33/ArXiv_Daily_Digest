# LLM 真值性与事实性 — 2026-W19 (05/04-05/10)

本周新增 **39** 篇论文。2 篇附带代码仓库。

## 分类分布

- `cs.CL`: 26 篇
- `cs.LG`: 6 篇
- `cs.CV`: 3 篇
- `via-citation`: 2 篇
- `cs.IR`: 1 篇
- `cs.CR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [When LLMs Stop Following Steps: A Diagnostic Study of Proced...](http://arxiv.org/abs/2605.00817v1) | 构建可控的流程执行诊断基准，给模型输入逐步算法与数值，测试其流程执行能力 | 分析大模型流程执行失败类型，发现表象推理能力下，忠实执行指令存在显著缺陷 | — |
| 2 | [LLM-Oriented Information Retrieval: A Denoising-First Perspe...](http://arxiv.org/abs/2605.00505v1) | 提出四阶段信息检索挑战框架，梳理按流水线组织的信噪比优化技术分类体系 | 梳理多个依赖检索领域的去噪研究，阐明面向大语言模型IR的范式转变方向 | — |
| 3 | [ReLay: Personalized LLM-Generated Plain-Language Summaries f...](http://arxiv.org/abs/2605.00468v1) | 构建ReLay数据集，基于该数据集使用两种个性化方法对五种大语言模型进行评估 | 构建了包含300组参与者-简明摘要对的ReLay数据集，揭示个性化与安全间存在权... | — |
| 4 | [Online Self-Calibration Against Hallucination in Vision-Lang...](http://arxiv.org/abs/2605.00323v1) | 提出OSCAR在线自校准框架，结合蒙特卡洛树搜索与双粒度奖励机制，经直接偏好优化... | 实验表明该方法在幻觉基准上取得最优性能，同时提升了模型的通用多模态能力 | — |
| 5 | [HalluScan: A Systematic Benchmark for Detecting and Mitigati...](http://arxiv.org/abs/2605.02443v1) | 构建HalluScan基准框架，通过72种不同配置系统评测幻觉检测与缓解效果 | 提出HalluScore指标、ADR路由算法，完成幻觉错误分解，测得不同检测方法... | — |
| 6 | [Compositional Multi-hop Factual Error Correction via Decompo...](http://arxiv.org/abs/2605.02277v1) | 提出推理感知框架CECoR，采用分解注入范式，结合监督微调与强化学习两阶段学习 | 所提方法在多跳基准上性能优于对比方法，可泛化到单跳，抗噪稳定通用性强 | — |
| 7 | [EditPropBench: Measuring Factual Edit Propagation in Scienti...](http://arxiv.org/abs/2605.02083v1) | 构建带句子级标注的EditPropBench基准，以ERA为核心指标评测LLM编... | 推出带句子级依赖监督的可控评估基准，发现当前LLM编辑仍存在较多必要更新遗漏 | — |
| 8 | [The Compliance Gap: Why AI Systems Promise to Follow Process...](http://arxiv.org/abs/2605.01771v1) | 通过两个定理推导得出结论，在六个前沿模型开展13组共2031次实验验证推导结果 | 定义了合规缺口新概念，验证其存在性与不可检测性，发布首个流程合规开放基准BS-B... | — |
| 9 | [Mitigating Multimodal LLMs Hallucinations via Relevance Prop...](http://arxiv.org/abs/2605.01766v1) | 提出无训练的LIME框架，利用分层相关性传播量化标记贡献，推理时更新KV增强对感... | 在多个音视觉多模态基准验证，可减少幻觉、增强多模态对齐，同时保留生成质量 | — |
| 10 | [MIRL: Mutual Information-Guided Reinforcement Learning for V...](http://arxiv.org/abs/2605.01520v1) | 提出互信息引导的MIRL解耦框架，以互信息为预筛选信号分配预算，解耦训练优化视觉... | 解决了现有可验证奖励强化学习的两个核心缺陷，在六个基准上取得更高准确率，减少了采... | — |
| 11 | [FT-RAG: A Fine-grained Retrieval-Augmented Generation Framew...](http://arxiv.org/abs/2605.01495v1) | 提出FT-RAG细粒度框架，分解表格为条目级语义单元构图，结合图检索与多模态融合... | 提出FT-RAG框架与Multi-Table-RAG-Lib基准数据集，性能达到... | — |
| 12 | [Hallucinations Undermine Trust; Metacognition is a Way Forwa...](http://arxiv.org/abs/2605.01428v1) | 提出基于元认知的忠实不确定性思路，对齐模型语言不确定性与内在不确定性以应对幻觉。 | 指出消除幻觉与保留效用存在固有权衡，提出表达不确定性的新路径，点明元认知对可信大... | — |
| 13 | [MemORAI: Memory Organization and Retrieval via Adaptive Grap...](http://arxiv.org/abs/2605.01386v1) | 提出MemORAI框架，整合选择性过滤压缩、溯源多关系图、查询自适应检索三项创新 | 在两个基准测试取得SOTA性能，证明三类设计对个性化对话代理必不可少 | — |
| 14 | [A Multi-View Media Profiling Suite: Resources, Evaluation, a...](http://arxiv.org/abs/2605.01336v1) | 构建多视图表示，对嵌入视图与含强化学习变体的融合策略做系统评估，开展大量实验 | 推出MBFC-2025大规模标签集，在ACL-2020取得SOTA结果，在MBF... | — |
| 15 | [LLM Ghostbusters: Surgical Hallucination Suppression via Ada...](http://arxiv.org/abs/2605.01047v1) | 提出后部署自适应遗忘框架，结合混合token级目标与无监督自适应发现环抑制幻觉 | 无需人工标注，可泛化到未见幻觉，降低81%包幻觉率，同时保留模型通用编码性能 | — |
| 16 | [Logical Consistency as a Bridge: Improving LLM Hallucination...](http://arxiv.org/abs/2605.03971v1) | 提出LaaB框架，以逻辑一致性为桥梁，通过元判断与互学习对齐整合双视角检测信号 | 在4个公开数据集、4种大模型上对比8个基线，实验验证LaaB检测性能更优 | — |
| 17 | [TriBench-Ko: Evaluating LLM Risks in Judicial Workflows](http://arxiv.org/abs/2605.03792v1) | 构建韩国司法场景的TriBench-Ko评估基准，覆盖四项核心任务，多维度联合评... | 公开TriBench-Ko评估基准，评估多款当代大模型，诊断出司法场景下大模型输... | ✅ |
| 18 | [SERE: Structural Example Retrieval for Enhancing LLMs in Eve...](http://arxiv.org/abs/2605.03701v1) | 提出基于三个结构概念的SERE结构示例检索框架，选取相关示例引导大语言模型因果推... | 缓解大语言模型的因果推理偏差，提升了事件因果识别准确率，多个数据集验证方法有效 | ✅ |
| 19 | [CuraView: A Multi-Agent Framework for Medical Hallucination ...](http://arxiv.org/abs/2605.03476v1) | 提出多智能体框架CuraView，基于GraphRAG构建知识图谱，实现闭环分级... | 提升临床文档事实可靠性，性能优于主流基线，可产出可复用标注数据集供下游使用 | — |
| 20 | [Geometric Deviation as an Unsupervised Pre-Generation Reliab...](http://arxiv.org/abs/2605.03196v1) | 通过测量隐藏状态相对于可回答参考集的几何偏差，无需标记数据也无需访问模型输出 | 验证几何偏差可作为轻量预生成可回答性信号，明确了该方法的适用边界 | — |
| 21 | [Evaluating Reasoning Models for Queries with Presuppositions](http://arxiv.org/abs/2605.03050v1) | 构建覆盖健康、科学、通用知识领域不同预设程度的查询，评估多个广泛部署的模型 | 重新考察了大型推理模型对含预设用户查询的处理能力，得到了明确的量化评估结果 | — |
| 22 | [Low-Cost Black-Box Detection of LLM Hallucinations via Dynam...](http://arxiv.org/abs/2605.05134v1) | 将LLM视为黑盒动力系统，基于Koopman算子理论构造差分残差得分，引入偏好感... | 实现单样本低开销幻觉检测，无需二次采样或外部知识，在三个基准上取得SOTA性能 | — |
| 23 | [When Relations Break: Analyzing Relation Hallucination in Vi...](http://arxiv.org/abs/2605.05045v1) | 研究旋转和噪声对关系推理的影响，评估了提示增强与多种预处理改进策略的效果 | 揭示了视觉语言模型感知鲁棒性与关系理解之间存在差距，指出需研发更鲁棒的几何感知模... | — |
| 24 | [Detecting Hallucinations in Large Language Models via Intern...](http://arxiv.org/abs/2605.05025v1) | 测量每个注意力头分布与均匀参考分布的KL散度，用该特征训练逻辑回归探针检测幻觉。 | 提出轻量单遍不确定性量化检测方法，性能可与现有不确定性估计方法相媲美。 | — |
| 25 | [Uncertainty-Aware Exploratory Direct Preference Optimization...](http://arxiv.org/abs/2605.04874v1) | 提出不确定性感知探索的UE-DPO方法，基于令牌级认知不确定性引导模型主动自我校... | 为所提方法提供了理论依据，大量实验验证了该方法的有效性与鲁棒性 | — |
| 26 | [NoisyCausal: A Benchmark for Evaluating Causal Reasoning Und...](http://arxiv.org/abs/2605.04313v1) | 构建注入可控形式噪声的NoisyCausal基准，提出结合大语言模型与显式因果结... | 推出结构化噪声下因果推理新基准NoisyCausal，所提方法性能优异泛化性好，... | — |
| 27 | [MedFabric and EtHER: A Data-Centric Framework for Word-Level...](http://arxiv.org/abs/2605.04180v1) | 提出以数据为中心的流水线生成MedFabric数据集，构建模块化词级编造检测器E... | 提出MedFabric数据集与EtHER检测器，检测器在词级编造基准上性能超SO... | — |
| 28 | [Not All That Is Fluent Is Factual: Investigating Hallucinati...](http://arxiv.org/abs/2605.04171v1) | 选取四类共80个提示测试四个主流大模型，采用多维度评分结合新提出的幻觉指数HI进... | 提出了新的加权评估指标幻觉指数HI，发现大模型幻觉不止受模型架构单一因素影响 | — |
| 29 | [Steer Like the LLM: Activation Steering that Mimics Promptin...](http://arxiv.org/abs/2605.03907) | 将提示引导建模为激活引导，提出PSR模型，训练其模仿提示干预估计token专属引... | 实验证明PSR优于现有激活引导方法，在多个任务上表现可与基于提示的方法相媲美 | — |
| 30 | [Cited but Not Verified: Parsing and Evaluating Source Attrib...](http://arxiv.org/abs/2605.06635v1) | 提出首个来源归因评估框架，用可复现AST解析器批量提取评估LLM生成报告的行内引... | 搭建了来源归因评估基础设施，对14种闭开源大模型完成基准测试，揭示引用质量与事实... | — |
| 31 | [How Many Iterations to Jailbreak? Dynamic Budget Allocation ...](http://arxiv.org/abs/2605.06605v1) | 提出理论有效的DAPRO动态预算分配框架，用于界定多轮LLM交互中目标事件的触发... | 提供满足预算的无分布有限样本覆盖率保证，所得界比先前工作更紧，实验效果优于基线 | — |
| 32 | [Automated Clinical Report Generation for Remote Cognitive Re...](http://arxiv.org/abs/2605.06594v1) | 对比知识工程规则模板法与零样本GPT-4方法，由八位专业人员做多维度人工评估。 | 提出八项远程康复临床报告系统设计建议，给出可复制的低资源临床NLG研究方法。 | — |
| 33 | [Towards Generation-Efficient Uncertainty Estimation in Large...](http://arxiv.org/abs/2605.06053v1) | 构建不确定性估计统一框架，提出对数幅值法和蒸馏得到的纯输入元不确定性估计器。 | 理清不同估计方法的性能-成本权衡，验证仅需更少生成即可实现有效的不确定性估计。 | — |
| 34 | [Knowing but Not Correcting: Routine Task Requests Suppress F...](http://arxiv.org/abs/2605.05957v1) | 构建含300个错误前提的基准评估，提出两种无需训练的纠正抑制干预方法CDS和DP... | 证实纠正抑制是普遍严重现象，提出的方法提升纠错效果，引入事实严格性作为模型可靠性... | — |
| 35 | [Hallucination as an Anomaly: Dynamic Intervention via Probab...](http://arxiv.org/abs/2605.05953v1) | 提出PCNET概率电路检测幻觉，仅在偏离事实区域触发PC-LDCD对比解码修正内... | 在多个大模型和基准测试中性能领先，幻觉检测AUROC最高达99%，有效降低正确内... | — |
| 36 | [Estimating the Black-box LLM Uncertainty with Distribution-A...](http://arxiv.org/abs/2605.05777v1) | 提出分布对齐对抗蒸馏DisAAD，引导轻量代理学习黑盒LLM输出分布，基于证据学... | 实验验证方法有效，仅为目标黑盒LLM大小1%的轻量代理即可实现可靠的不确定性量化 | — |
| 37 | [The Cost of Context: Mitigating Textual Bias in Multimodal R...](http://arxiv.org/abs/2605.05594v1) | 提出无参数推理时框架BAIR，恢复视觉显著性，对文本干扰项施加位置感知惩罚 | 在医疗事实性等多个基准上，无需重训练微调即可恢复多模态接地，提升诊断可靠性 | — |
| 38 | [A Few Good Clauses: Comparing LLMs vs Domain-Trained Small L...](http://arxiv.org/abs/2605.05532v1) | 将自研法律领域混合专家模型Olava Extract与五种前沿大模型对比性能与推... | 证实高性能法律AI无需依赖超大型模型，挑战了企业AI需大模型大投入的固有认知 | — |
| 39 | [CAST: Mitigating Object Hallucination in Large Vision-Langua...](http://arxiv.org/abs/2605.04641) | 提出无训练、即插即用的CAST方法，利用描述查询对应注意力模式增强模型视觉感知能... | 在五个模型五个基准上平均降低6.03%对象幻觉，性能达SOTA，几乎不增加推理成... | — |

## 常见基线方法

- **专家撰写的静态简明摘要** (1 篇引用)
- **NLI验证** (1 篇引用)
- **RAV方法** (1 篇引用)
- **远监督方法** (1 篇引用)
- **少样本大语言模型基线** (1 篇引用)
- **确定性替换基线** (1 篇引用)
- **IFEval** (1 篇引用)
- **SWE-bench** (1 篇引用)
- **BFCL** (1 篇引用)
- **COMPASS** (1 篇引用)

## 本周提到的 Limitations

- 现有个性化PLS方法未能平衡效果提升与偏见强化、幻觉引入等安全风险
- 当前最强LLM编辑器仍遗漏约30%所需级联更新，无法实现可靠的自动科学修订
- 现有大模型缺乏区分自身已知与未知的能力，消除幻觉和保留效用存在不可避免的固有权衡。
- 该几何信号不具有普适性，仅在结构化领域可靠，事实类提示中无可靠信号
- 推理模型仍无法挑战26-42%的错误预设，且性能易受预设表述强度的影响
- 现有提示增强与预处理策略仅能部分改善关系幻觉，无法完全解决该问题
- 专家临床评估规模受限，两种方法对比经校正后未达到统计学显著性。

## 常用数据集

- **摘要未提及** (2 篇使用)
- **ReLay** (1 篇使用)
- **HalluScan基准** (1 篇使用)
- **多跳事实纠错基准** (1 篇使用)
- **EditPropBench** (1 篇使用)
- **arXiv cs.CL基准数据集论文** (1 篇使用)
- **BS-Bench** (1 篇使用)
- **Multi-Table-RAG-Lib** (1 篇使用)
- **LOCOMO** (1 篇使用)
- **LongMemEval** (1 篇使用)


---

*自动生成于 2026-05-10 | Research Radar*