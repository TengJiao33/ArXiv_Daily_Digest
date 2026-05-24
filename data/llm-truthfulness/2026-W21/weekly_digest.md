# LLM 真值性与事实性 — 2026-W21 (05/18-05/24)

本周新增 **25** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.CL`: 13 篇
- `via-citation`: 7 篇
- `cs.AI`: 3 篇
- `cs.LG`: 1 篇
- `cs.CR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [When Reasoning Traces Become Performative: Step-Level Eviden...](http://arxiv.org/abs/2605.11746) | 构建基于答案承诺代理的步骤级检测-分类-比较框架，结合多技术交叉验证，在多模型多... | 揭示思维链轨迹步骤对齐度低，明确错配核心模式，证实CoT有用但对答案形成的报告不... | — |
| 2 | [Architecture, Not Scale: Circuit Localization in Large Langu...](http://arxiv.org/abs/2605.08853) | 选取Pythia与Qwen2.5模型，对三类不同大语言模型电路的特性开展对比研究 | 挑战了可解释性难度是模型规模固有结果的观点，证明架构选择比参数规模更影响研究难度 | — |
| 3 | [The Geometry of Forgetting: Temporal Knowledge Drift as an I...](http://arxiv.org/abs/2605.09195) | 探究知识时间漂移在大语言模型残差流中的几何编码，用带漂移标签训练线性探针检测漂移 | 证明知识时间漂移编码方向正交于正确性与不确定性，验证线性探针可有效检测该漂移 | — |
| 4 | [Hallucination Detection via Activations of Open-Weight Proxy...](http://arxiv.org/abs/2605.07209) | 提出代理分析器框架，基于小开源模型的内部激活提取18种特征，训练堆叠集成模型检测... | 所提方法适配各类生成模型，在多规模模型上性能优于现有基线，检测效果稳定优异 | — |
| 5 | [Dual-Pathway Circuits of Object Hallucination in Vision-Lang...](http://arxiv.org/abs/2605.13156) | 提出双通路回路分析框架，结合激活补丁与条件通路分析识别表征幻觉相关回路 | 识别出两类功能通路，抑制幻觉通路可大幅降低幻觉且精度损失小，结果跨架构一致 | — |
| 6 | [APCD: Adaptive Path-Contrastive Decoding for Reliable Large ...](http://arxiv.org/abs/2605.09492) | 提出自适应路径对比解码APCD框架，包含熵驱动扩展与散度感知路径对比两个组件 | 在八个基准上实验验证，该方法提升了生成的事实准确性，同时保持解码效率 | ✅ |
| 7 | [How LLMs Are Persuaded: A Few Attention Heads, Rerouted](http://arxiv.org/abs/2605.09314) | 通过多步干预验证，定位追踪大语言模型被劝说诱导出错的因果路径与相关特征 | 揭示大语言模型被劝说出错的紧凑因果机制，证实该机制可监控，修改特征可阻断劝说 | — |
| 8 | [Predictable Confabulations: Factual Recall by LLMs Scales wi...](http://arxiv.org/abs/2605.18732v1) | 借助自动参考验证系统，对38个模型的八千九百余条学术引用的回忆能力进行评估。 | 揭示了大语言模型事实回忆质量的变化规律，可解释不同模型间的大部分性能方差。 | — |
| 9 | [TRACE: Trajectory Correction from Cross-layer Evidence for H...](http://arxiv.org/abs/2605.18163v1) | 提出无训练的TRACE算法，推理时依据输入的跨层候选轨迹动态选择校正方式纠正幻觉 | 在15个模型3个基准上全单元提升，平均MC1提12.26点，无需标注检索或微调 | — |
| 10 | [FedSDR: Federated Self-Distillation with Rectification](http://arxiv.org/abs/2605.18028v1) | 先提出联邦自蒸馏FedSD策略，后提出带校正的FedSDR，采用双LoRA分支选... | 建立联邦自蒸馏基础策略，提出增强框架FedSDR，大量实验验证其具有更优异的性能 | — |
| 11 | [Predictive Prefetching for Retrieval-Augmented Generation](http://arxiv.org/abs/2605.17989v1) | 提出适配动态信息需求的预测预取异步检索框架，通过三个组件预测检索时机与内容 | 可最高降低43.5%端到端延迟，提升62.4%首token时间，维持与同步RAG... | — |
| 12 | [Systematic Evaluation of the Quality of Synthetic Clinical N...](http://arxiv.org/abs/2605.17775v1) | 对百万级MIMIC来源的改写合成临床笔记，开展多维度系统评估 | 系统分析合成临床笔记的信息特性，验证其可增强罕见ICD编码任务训练 | — |
| 13 | [QQJ: Quantifying Qualitative Judgment for Scalable and Human...](http://arxiv.org/abs/2605.17382v1) | 提出QQJ评估框架，基于专家设计的多维评分规则，用小高质量标注校准大模型对齐专家... | 实现可解释可扩展的生成式AI评估，比现有方法更对齐人类判断，稳定性和诊断能力更优 | — |
| 14 | [AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowled...](http://arxiv.org/abs/2605.17352v1) | 提出自适应多智能体轨迹对齐框架AMATA，包含轨迹内偏好学习与智能体间依赖学习两... | 在五个知识密集型QA基准上性能优于各类对比方法，可有效减少模型的token消耗量 | — |
| 15 | [ConflictRAG: Detecting and Resolving Knowledge Conflicts in ...](http://arxiv.org/abs/2605.17301v1) | 提出冲突感知的ConflictRAG框架，在答案生成前完成知识冲突的检测、分类与... | 提出两阶段冲突检测、熵-TOPSIS可信度评估与CARS指标，实验性能优于多个对... | — |
| 16 | [The Range Shrinks, the Threat Remains: Re-evaluating LLM Pac...](http://arxiv.org/abs/2605.17062v1) | 沿用Spracklen等人的研究方法，对五款新发布的前沿代码大模型开展测试验证 | 复现验证了前沿新模型的包幻觉率，发现多模型共有的幻觉包名，得到多个新的量化现象结... | — |
| 17 | [PARALLAX: Separating Genuine Hallucination Detection from Be...](http://arxiv.org/abs/2605.17028v1) | 控制基准构建缺陷后开展多方法多模型多数据集大规模评估，提出监督探针DRIFT用于... | 揭示现有幻觉检测进展大多由基准构建缺陷导致，多数方法控制缺陷后性能接近随机 | — |
| 18 | [HalluScore: Large Language Model Hallucination Question Answ...](http://arxiv.org/abs/2605.17007v1) | 构建结构化阿拉伯语问答基准HalluScore，经多流程筛选得到827道带多标签... | 推出HalluScore评测基准，对17个大模型做实证分析，提供高质量人工标注幻... | — |
| 19 | [How do Humans Process AI-generated Hallucination Contents: a...](http://arxiv.org/abs/2605.16953v1) | 招募27名参与者完成内容验证任务，记录脑电信号，采用平均事件相关电位法开展研究 | 揭示人类处理幻觉与非幻觉内容时多个认知过程模式不同，误判与正确判断的幻觉神经响应... | — |
| 20 | [Understanding Data Temporality Impact on Large Language Mode...](http://arxiv.org/abs/2605.22769v1) | 构建包含七千余道时序问题的基准与评估方案，预训练后与打乱预训练模型对比 | 引入时序问题基准与评估方案，验证了时序预训练可提升大语言模型事实知识的时效性 | — |
| 21 | [Assisted Counterspeech Writing at the Crossroads of Hate Spe...](http://arxiv.org/abs/2605.22435v1) | 测试三种知识驱动的大语言模型对抗话语生成策略，经专家修订后用人工自动指标评估 | 证实结合多源指南文档的混合策略效果最优，发布了含专家验证对抗话语的数据集 | — |
| 22 | [Do Factual Recall Mechanisms Carry over from Text to Speech ...](http://arxiv.org/abs/2605.22170v1) | 采用先前应用于文本模型的因果中介分析，基于SpiritLM多模态模型开展实验研究 | 增进了对语音语言模型编码事实关联内部机制的理解，为改进语音AI系统提供了见解 | — |
| 23 | [A Comparative Study of Language Models for Khmer Retrieval-A...](http://arxiv.org/abs/2605.22099v1) | 构建面向高棉语电信领域文档的RAG问答系统，分两阶段对比评估检索与生成模型。 | 评测了多个常用嵌入和生成模型，明确了当前高棉语RAG应用存在的主要瓶颈。 | — |
| 24 | [ACL-Verbatim: hallucination-free question answering for rese...](http://arxiv.org/abs/2605.21102v1) | 将抽取式问答系统VerbatimRAG应用于ACL论文集，将用户查询映射至检索文... | 构建了用户查询到研究论文相关文本段映射的新基准数据集，训练评估了多种抽取模型 | — |
| 25 | [Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v2) | 构建支持英法双语、覆盖两类用户的ClaimRAG-LAW数据集，采用细粒度框架评... | 提出面向法律RAG的ClaimRAG-LAW基准数据集，支持双语，覆盖专家与非专... | — |

## 常见基线方法

- **SAPLMA** (2 篇引用)
- **Qwen2.5** (1 篇引用)
- **DeepSeek-R1-Distill** (1 篇引用)
- **标准多头注意力** (1 篇引用)
- **token熵** (1 篇引用)
- **语义熵** (1 篇引用)
- **CCS** (1 篇引用)
- **ReDeEP** (1 篇引用)
- **传统算法** (1 篇引用)
- **同步RAG** (1 篇引用)

## 本周提到的 Limitations

- 整文改写会丢失细粒度细节，分块改写在不完全上下文下会降低事实精确度
- 当前法律领域RAG系统在检索、生成以及主张级分析方面均存在明显局限性

## 常用数据集

- **七个推理基准** (1 篇使用)
- **RAGTruth** (1 篇使用)
- **LLM-AggreFact** (1 篇使用)
- **POPE-adversarial** (1 篇使用)
- **AMBER** (1 篇使用)
- **八个评测基准** (1 篇使用)
- **多个基准数据集** (1 篇使用)
- **MIMIC** (1 篇使用)
- **五个已建立知识密集型QA基准** (1 篇使用)
- **三个基准数据集，未提及具体名称** (1 篇使用)


---

*自动生成于 2026-05-24 | Research Radar*