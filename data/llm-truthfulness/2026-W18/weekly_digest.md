# LLM 真值性与事实性 — 2026-W18 (04/27-05/03)

本周新增 **29** 篇论文。3 篇附带代码仓库。

## 分类分布

- `cs.CL`: 22 篇
- `cs.LG`: 2 篇
- `cs.SE`: 1 篇
- `eess.AS`: 1 篇
- `via-citation`: 1 篇
- `cs.DB`: 1 篇
- `cs.AI`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Context-Fidelity Boosting: Enhancing Faithful Generation thr...](http://arxiv.org/abs/2604.22335v1) | 受水印技术对数塑形原理启发，提出轻量解码框架CFB，基于上下文支持度调整对数，包... | 无需重训练与架构修改，可适配多种大模型，实验验证能提升忠实性且开销极小，代码已开... | — |
| 2 | [How Large Language Models Balance Internal Knowledge with Us...](http://arxiv.org/abs/2604.22193v1) | 提出三源交互框架，在两个数据集上系统评估三个模型家族共27个大语言模型 | 发现大模型知识源依赖的普遍规律，证明微调多源交互数据可提升模型信息分辨能力 | — |
| 3 | [Dissociating Decodability and Causal Use in Bracket-Sequence...](http://arxiv.org/abs/2604.22128v1) | 对Dyck语言训练的Transformer的残差流与注意力模式开展探针探测和干预... | 厘清了表征可解码性与因果作用的差异，证明可解码不代表会被因果使用 | — |
| 4 | [MEG-RAG: Quantifying Multi-modal Evidence Grounding for Evid...](http://arxiv.org/abs/2604.24564v1) | 提出语义感知的MEG指标量化检索证据贡献，基于此构建MEG-RAG框架训练多模态... | 提升生成结果准确性与多模态一致性，在基准上优于强基线，跨不同教师模型泛化性良好 | — |
| 5 | [A Multi-Dimensional Audit of Politically Aligned Large Langu...](http://arxiv.org/abs/2604.24429v1) | 借鉴哈贝马斯交往行动理论，提出四维审计框架，采用自动化定量指标审计政治对齐大语言... | 提出政治对齐大语言模型的多维度审计框架，揭示了不同对齐方案下模型表现的权衡关系 | — |
| 6 | [Differentiable Faithfulness Alignment for Cross-Model Circui...](http://arxiv.org/abs/2604.24302v1) | 提出可微分保真度对齐（DFA）框架，将小源模型电路信息经学习对齐迁移到目标大模型 | 验证DFA优于简单基线，部分场景下电路保真度不弱于直接归因，证明小模型可提供机制... | ✅ |
| 7 | [MEMCoder: Multi-dimensional Evolving Memory for Private-Libr...](http://arxiv.org/abs/2604.24222v1) | 提出MEMCoder框架，引入多维进化记忆，采用双源检索机制，通过执行反馈闭环动... | 增强现有RAG性能，平均pass@1提升16.31%，域适配能力优于现有同类记忆... | — |
| 8 | [Factual and Edit-Sensitive Graph-to-Sequence Generation via ...](http://arxiv.org/abs/2604.24104v1) | 提出DLM4G非自回归扩散框架，采用基于去噪误差的图感知自适应噪声生成策略 | 所提方法性能优于各类基线，可推广到分子字幕，具备科学G2S生成的通用性 | — |
| 9 | [JudgeSense: A Benchmark for Prompt Sensitivity in LLM-as-a-J...](http://arxiv.org/abs/2604.23478v1) | 提出JudgeSense框架与基准，通过法官灵敏度分数JSS量化提示灵敏度属性 | 提出JudgeSense基准，发布相关代码、日志和验证数据集，支撑标准化JSS报... | — |
| 10 | [AI Safety Training Can be Clinically Harmful](http://arxiv.org/abs/2604.23445v1) | 选取四个生成模型在不同严重程度的PE疗法、CBT练习场景测试，由三名法官的LLM... | 发现RLHF安全对齐会干扰治疗作用机制，提出符合监管要求的五轴AI心理健康评估框... | — |
| 11 | [Bridging Reasoning and Action: Hybrid LLM-RL Framework for E...](http://arxiv.org/abs/2604.23345v1) | 提出VLK-RL混合框架，LLM生成候选约束后交叉验证，转换为结构化约束状态供R... | 所提框架在多个基准上显著提升泛化性与鲁棒性，长程任务性能优于强单模型基线 | — |
| 12 | [Process Supervision of Confidence Margin for Calibrated LLM ...](http://arxiv.org/abs/2604.23333v1) | 提出校准感知的强化学习框架RLCM，通过裕度增强过程奖励联合优化正确性与置信可靠... | 在多类推理基准上大幅提升校准效果且维持准确率，支持更高效共形风险控制与置信聚合 | — |
| 13 | [Evaluating Temporal Consistency in Multi-Turn Language Model...](http://arxiv.org/abs/2604.23051v1) | 引入基于Wikidata生成、包含超百万问题链的大规模诊断基准ChronoSco... | 提出时间范围稳定性研究视角，构建公开基准，揭示现有最优模型存在时间推理缺陷 | ✅ |
| 14 | [LLM-ReSum: A Framework for LLM Reflective Summarization thro...](http://arxiv.org/abs/2604.25665v1) | 对14种自动摘要指标和LLM评估器做元评估，提出无需微调的闭环自反馈LLM-Re... | 提出LLM-ReSum摘要框架提升摘要质量，构建法律摘要新基准PatentSum... | — |
| 15 | [Walking Through Uncertainty: An Empirical Study of Uncertain...](http://arxiv.org/abs/2604.25591v1) | 对五种代表性不确定性估计方法，在多模型多任务设置下开展系统性实证研究 | 首次开展音频感知大语言模型不确定性估计系统实证研究，得出两个核心发现，探索了自适... | — |
| 16 | [From World-Gen to Quest-Line: A Dependency-Driven Prompt Pip...](http://arxiv.org/abs/2604.25482v1) | 提出依赖感知的多阶段提示流水线，借助结构化中间表示建模叙事依赖，分阶段生成RPG... | 该流水线可减少叙事漂移与幻觉，生成逻辑合理结构有效的RPG内容，复杂度提升时质量... | — |
| 17 | [LegalMidm: Use-Case-Driven Legal Domain Specialization for K...](http://arxiv.org/abs/2604.25297v1) | 提出面向韩国法律实际需求的系统训练框架，联合法律专家构建数据集并优化训练流程 | 推出韩国法律领域大语言模型LegalMidm，提出用例驱动的高质量法律数据集构建... | — |
| 18 | [Faithful Autoformalization via Roundtrip Verification and Re...](http://arxiv.org/abs/2604.25031v1) | 提出无需真实标注的往返验证方法，不一致时诊断定位错误后做针对性修复 | 验证该方法可有效提升形式化等价率，效果优于随机修复，证实等价性与语义漂移负相关 | — |
| 19 | [Incompressible Knowledge Probes: Estimating Black-Box LLM Pa...](http://arxiv.org/abs/2604.24827v1) | 提出不可压缩知识探针，基于事实知识存储与参数量关系校准对数线性映射估算参数量 | 构建了分七层难度的事实问题基准，可对各类闭源大模型有效估算参数规模 | — |
| 20 | [Position: Logical Soundness is not a Reliable Criterion for ...](http://arxiv.org/abs/2604.04177) | 结合认知科学与语用学相关研究，对逻辑合理结论引发不合理人类推断的场景进行类型划分 | 指出原有基于逻辑的方法存在结构性缺陷，提出利用大模型类人推理做互补验证的思路 | — |
| 21 | [MoRFI: Monotonic Sparse Autoencoder Feature Identification](http://arxiv.org/abs/2604.26866v1) | 开展控制变量微调实验，利用预训练稀疏自编码器分析激活，提出MoRFI捕捉因果相关... | 提出MoRFI特征识别方法，可跨模型可靠发现致幻潜方向，通过单潜干预恢复知识。 | — |
| 22 | [Tree-of-Text: A Tree-based Prompting Framework for Table-to-...](http://arxiv.org/abs/2604.26501v1) | 提出Tree-of-Text树结构提示框架，引导大语言模型分三阶段完成表格到文本... | 在多个数据集上性能优于现有方法，时间成本仅约为Chain-of-Table的40... | — |
| 23 | [StratMem-Bench: Evaluating Strategic Memory Use in Virtual C...](http://arxiv.org/abs/2604.26243v1) | 设计StratMem-Bench评估基准，提出包含多指标的评估框架，评估虚拟角色... | 填补了虚拟角色对话策略记忆评估的空白，提出了新基准与配套多指标评估框架。 | — |
| 24 | [CacheRAG: A Semantic Caching System for Retrieval-Augmented ...](http://arxiv.org/abs/2604.26176v1) | 提出面向大语言模型KGQA的缓存增强架构CacheRAG，含三个适配大模型场景的... | 多个基准实验证明CacheRAG显著优于现有SOTA基线，在CRAG数据集准确率... | — |
| 25 | [HIVE: Hidden-Evidence Verification for Hallucination Detecti...](http://arxiv.org/abs/2604.26139v1) | 提出HIVE隐藏证据验证框架，从去噪轨迹提取压缩隐藏证据，选择信息丰富的步层证据... | 在两个D-LLM三个QA基准上优于八个基线，取得0.9236 AUROC和0.9... | — |
| 26 | [BioGraphletQA: Knowledge-Anchored Generation of Complex QA D...](http://arxiv.org/abs/2604.26048v1) | 采用知识图谱小图元锚定的生成流程，用结构化提示控制大模型生成问题的复杂度与事实性... | 提出可扩展的系统化生成框架，构建新型生物医学问答数据集，验证了其实际应用价值。 | ✅ |
| 27 | [Geometry-Calibrated Conformal Abstention for Language Models](http://arxiv.org/abs/2604.27914v1) | 提出基于共形预测的事后弃权框架CA，引入利用模型表示几何的置信度校准策略 | 所提方法提供有限样本保证，可对齐置信度与模型无知，显著提升选择性回答性能 | — |
| 28 | [Perturbation Probing: A Two-Pass-per-Prompt Diagnostic for F...](http://arxiv.org/abs/2604.27401v1) | 提出扰动探测法，每个提示两次前向传播无需反向传播，再对识别神经元做一次性干预扫描... | 识别出对齐大模型两种FFN行为电路结构，给出干预预测指标，提供了精准编辑工具。 | — |
| 29 | [When Roles Fail: Epistemic Constraints on Advocate Role Fide...](http://arxiv.org/abs/2604.27228v1) | 基于TRUST流水线开展实证检验，开发认识立场分类器，用四项指标测量60份多语政... | 识别出两种角色失效模式，明确其统一作用机制，发现不同因素对角色保真度的影响差异 | — |

## 常见基线方法

- **未提及具体基线** (1 篇引用)
- **角色扮演对齐** (1 篇引用)
- **微调对齐** (1 篇引用)
- **直接节点归因** (1 篇引用)
- **简单基线** (1 篇引用)
- **现有检索增强生成RAG系统** (1 篇引用)
- **现有基于记忆的持续学习方法** (1 篇引用)
- **G2S扩散基线** (1 篇引用)
- **微调自回归基线** (1 篇引用)
- **零样本LLM迁移基线** (1 篇引用)

## 本周提到的 Limitations

- 现有政治对齐大语言模型的对齐策略不够均衡鲁棒，仍需进一步改进优化
- 源模型与目标模型的规模、架构差异越大，跨模型电路迁移的效果越差
- 经深度安全调优的模型估算结果仅为下界，拒答策略会隐藏模型已知的知识容量
- 定向引导干预适用范围有限，仅对满足条件的部分模型和特定电路有效。

## 常用数据集

- **未命名数据集1** (1 篇使用)
- **未命名数据集2** (1 篇使用)
- **Dyck语言** (1 篇使用)
- **模板化自然语言数据集** (1 篇使用)
- **M²RAG基准** (1 篇使用)
- **摘要未提及** (1 篇使用)
- **NdonnxEval** (1 篇使用)
- **NumbaEval** (1 篇使用)
- **三个文本图数据集** (1 篇使用)
- **分子字幕数据集** (1 篇使用)


---

*自动生成于 2026-05-03 | Research Radar*