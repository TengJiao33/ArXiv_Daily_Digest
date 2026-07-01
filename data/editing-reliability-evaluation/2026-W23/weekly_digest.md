# 编辑可靠性与行为控制 — 2026-W23 (06/01-06/07)

本周新增 **161** 篇论文，**18** 篇附带代码。优先级：high 98 / medium 47 / low 16。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [CLaRE-ty Amid Chaos: Quantifying Representational Entanglement t...](http://arxiv.org/abs/2603.19297) | evaluation/benchmark | CLaRE相较基线与涟漪效应的斯皮尔曼相关平均提升62.2%，速度快2.74倍，峰值显存降低... | 评测方法对模型编辑涟漪效应的预测准确性，同时对比不同方法的计算速度、显存与存储占... | 知识编辑产生不可预测的涟漪效应（编辑串扰） | ✅ |
| 2 | high | ACL 2025 | [COMPKE: Complex Question Answering under Knowledge Editing](http://arxiv.org/abs/2506.00829) | evaluation/benchmark | MeLLo在GPT-4O-MINI上准确率达39.47，在Qwen2.5-3B上骤降至3.8... | 通过构建贴合真实复杂推理场景的评测基准，为知识编辑方法的有效性评测提供反馈支撑。 | 现有知识编辑方法效果高度依赖基座模型，泛化性差，原有评测无法反映... | ✅ |
| 3 | high | ICLR 2024 | [Composable Interventions for Language Models](http://arxiv.org/abs/2407.06483) | evaluation/benchmark | 通过310种不同组合实验发现，压缩会阻碍知识编辑与机器遗忘，干预组合效果依赖应用顺序，现有通... | 构建统一可组合干预研究框架，配套指标和代码，通过标准化实验分析多类干预的交互规律... | 现有干预未考虑多干预组合的实际落地需求，可组合性差，缺乏标准化评... | ✅ |
| 4 | high | - | [Does Localization Inform Editing? Surprising Differences in Caus...](http://arxiv.org/abs/2301.04213v2) | evaluation/benchmark | 绝大多数知识编辑场景中，因果追踪的定位结果无法指导最优编辑层选择，编辑层数本身对性能预测性远... | 通过对比不同定位结果与编辑位置下的编辑性能，验证定位对知识编辑的指导有效性 | 结论仅针对因果追踪方法，未验证其他定位方法，结论泛化性待验证 | ✅ |
| 5 | high | EMNLP 2025 | [Dynamic Retriever for In-Context Knowledge Editing via Policy Op...](http://arxiv.org/abs/2510.21059) | policy optimization | 动态选择演示可让上下文内知识编辑成功率最高提升17.1%，延迟降低41.6%，同时不损失无关... | 通过策略优化训练动态检索器，筛选适配当前编辑任务的上下文演示，剪枝低价值示例，不... | 仅在单一基准验证，未充分评测该方法在多场景下的知识编辑副作用 | ✅ |
| 6 | high | EMNLP 2024 | [Editing the Mind of Giants: An In-Depth Exploration of Pitfalls ...](http://arxiv.org/abs/2406.01436) | survey | 现有知识编辑方法编辑后普遍存在知识扭曲、通用能力下降的副作用，且相关缺陷评估缺乏统一的指标与... | 梳理现有知识编辑的各类副作用，构建统一的评估框架，为后续改进知识编辑可靠性提供基... | 知识编辑副作用缺乏统一评估标准，无法可靠衡量编辑效果，阻碍知识编... | ✅ |
| 7 | high | - | [From Risk Classification to Action Plan Remediation: A Guardrail...](http://arxiv.org/abs/2606.05805v1) | agent harness | TRIAD框架可将平均攻击成功率降至10.42%，在所有对比的护栏集成基线中取得最优的安全-... | 将护栏生成的结构化自然语言反馈注入智能体上下文，形成反馈与规划闭环，引导智能体修... | 仅在两个公开基准测试验证，未在真实复杂开放场景测试，闭环反馈的长... | ✅ |
| 8 | high | - | [Fundamental Problems With Model Editing: How Should Rational Bel...](http://arxiv.org/abs/2406.19354) | evaluation/benchmark | 现有模型编辑的标准表述存在基础性缺陷，研究隐含的「大语言模型具备可编辑信念」的假设本身就存疑... | 通过梳理现有模型编辑的核心开放问题，构建带金标准的评测基准，为改进模型编辑研究提... | 当前模型编辑研究缺乏清晰的问题定义和可靠的评测基准，研究结论的可... | ✅ |
| 9 | high | ICLR 2026 | [KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model...](http://arxiv.org/abs/2510.02392) | framework/tooling | 大语言模型对不同层级知识的更新过程与人类不同，更新过程中存在一致性-容量权衡 | 从知识传播、可塑性缩放、一致性、鲁棒性多个维度评测大模型知识更新的特性 | 现有知识更新研究评估不充分、孤立、规模偏小 | ✅ |
| 10 | high | - | [MedREK: Retrieval-Based Editing for Medical LLMs with Key-Aware ...](http://arxiv.org/abs/2510.13500) | memory-based editor | 集成共享查询-关键模块可提升医学知识检索精度，MedREK是首个经验证可支持医学大模型批量编... | 构建覆盖更广医学学科的MedVersa基准，在严格局部性约束下评估单样本与批量编... | 医学知识表征重叠导致检索不准，现有编辑仅支持单样本，参数编辑破坏... | ✅ |
| 11 | high | - | [Model Editing for New Document Integration in Generative Informa...](http://arxiv.org/abs/2603.02773) | locate-then-edit | DOME仅需增量训练约60%的训练时间，提升新文档检索性能同时维持原集合检索效果 | 评测新文档与原文档集合的检索性能，对比增量训练的训练时间，验证方法有效性与效率 | 跨查询编辑向量不可区分，新增文档泛化差，增量训练易发生灾难性遗忘 | ✅ |
| 12 | high | ICML 2026 | [Reverse-Engineering Model Editing on Language Models](http://arxiv.org/abs/2602.10134v2) | unlearning/safety | 模型编辑产生的参数更新矩阵的行空间编码了编辑主体的指纹，攻击者可借此高成功率恢复出原始编辑数... | 提出子空间伪装防御方法，通过语义诱饵混淆参数更新的指纹，在不损失编辑效用的前提下... | 模型编辑会因参数更新泄露编辑的敏感数据，给模型编辑的落地应用带来... | ✅ |

## A 会 / Venue 标签

- **ICLR 2026**：8 篇
- **ACL 2025**：6 篇
- **ACL 2024**：6 篇
- **EMNLP 2024**：5 篇
- **EMNLP 2025**：4 篇
- **ICLR 2024**：4 篇
- **AAAI 2026**：3 篇
- **ICML 2026**：3 篇
- **ACL 2026**：1 篇
- **ICML 2025**：1 篇

## 方法族分布

- **evaluation/benchmark**：48 篇
- **model steering**：26 篇
- **other**：15 篇
- **locate-then-edit**：14 篇
- **unlearning/safety**：11 篇
- **framework/tooling**：9 篇
- **policy optimization**：7 篇
- **survey**：5 篇
- **memory-based editor**：3 篇
- **知识编辑**：3 篇
- **agent harness**：3 篇
- **steering**：2 篇

## 失败模式与风险信号

- 持续顺序编辑引发的语义漂移、灾难性遗忘，无法精准回滚特定编辑
- 基于NTP的知识编辑存在上下文依赖，缺失上下文时会发生知识召回失败
- 固定编辑层无法适配知识所处的模型不同深度，导致样本间编辑性能参差不齐。
- 编辑修改目标行为后大模型通用能力退化
- 大语言模型易产生不合意输出，行为不可控，模型对齐性与可靠性不足
- 知识编辑泛化差、多轮更新不稳定、新老知识冲突、多轮更新灾难性遗忘
- 现有评估无法捕捉编辑引发的大范围知识漂移
- 顺序编辑崩溃
- 冲突知识传播引发多步推理失效
- 监督微调更新知识后无法提升新信息运用能力，强化学习适配计算成本过高

## 评测信号

- 实验验证方法在终身编辑中的知识学习保留能力、编辑准确性、效率与可逆编辑的有效性
- 评测框架缓解上下文依赖的效果与知识编辑成功率，验证缓解上下文依赖对鲁棒编辑的重要性
- 在多个基准数据集测试，验证所提方法在不同大模型、不同知识编辑方法下的有效性与鲁棒性。
- 评测编辑成功率与通用能力保留效果，重点关注编辑后大模型通用能力的退化幅度
- 本文未开展具体实验，未给出具体评测结果，研究目标为获得可信鲁棒可解释的可控大语言模型
- 评测知识编辑的泛化性能、多轮更新稳定性、灾难性遗忘程度、代码领域更新效能
- 量化知识编辑引发的知识漂移，可捕捉传统样本评估无法发现的编辑隐性副作用，提供更全面的编辑效果评估。
- 在多个大语言模型主干、多个L&E编辑器上，评测编辑有效范围与长期编辑性能的提升效果
- 评测知识更新后大语言模型多步推理中的冲突知识传播效果，推出标准化测试基准TRACK。
- 在知识融入问答、智能体工具使用基准评测，验证方法的跨域迁移性与可扩展性

## 控制机制 / Harness 信号

- 构造带思维链的指令编辑数据，结合监督微调与策略优化训练，推理阶段引入RAG实现知识编辑。
- 将知识控制建模为表示空间干预，学习编辑局部化的低维模块，推理通过查询自适应路由引导生成
- 本文未针对模型/Agent行为实施控制，仅构建可靠评测基准为后续相关研究提供评测支撑。
- 通过策略优化训练动态检索器，筛选适配当前编辑任务的上下文演示，剪枝低价值示例，不修改模型参数实现编辑
- 通过新增局部性测试的评测基准暴露现有方法不足，优化微调训练配置提升非结构化知识编辑性能。
- 通过梗图转文本流水线解耦任务，采用带人工指南的零样本思维链提示引导单模态LLM的推理行为。
- 提出更贴近真实应用场景的知识编辑评测基准，通过更全面的评测反馈提升知识编辑评测的可靠性。
- 提出文档级模型编辑任务并构建对应基准评测数据集，通过基准评测暴露现有方法不足，推动领域方法改进。
- 仅用隐状态与梯度一步计算参数偏移，搭配终身归一化策略，实现高效可扩展的大语言模型终身知识编辑
- 通过系统机制分析定位知识编辑后原始知识残留的关键模型结构因素，为提升编辑可靠性提供机制依据。

## 可靠性 / 落地风险

- 未讨论知识编辑对模型原有能力的影响，未评测编辑副作用，评测维度不够全面
- 长期多轮编辑下交叉干扰的累积效应未验证，大规模真实场景的可用性不明确
- 基准依赖时间筛选知识实体，仍可能存在预训练数据漏筛污染，会影响最终评测结果的可靠性。
- 仅在单一基准验证，未充分评测该方法在多场景下的知识编辑副作用
- 原有UKE缺少局部性评测，无法有效评估编辑副作用，容易导致方法选型出现偏差。
- 依赖梗图转文本流水线的信息完整性，转文本丢失关键视觉信息会直接导致检测出错。
- 现有知识编辑领域评测任务过于简单，虚高的评测得分无法反映方法在真实场景的真实可靠性。
- 现有模型编辑评测未覆盖真实场景文档级需求，无法准确衡量方法落地的实际可靠性。
- 未验证长期编辑对模型原有能力的影响，未提及编辑副作用，可靠性未充分验证
- 现有知识编辑依赖的常规评测无法识别知识残留问题，导致编辑后模型输出不可靠，影响落地应用。

## 代码资源

- [Does Localization Inform Editing? Surprising Differences in Causality-Based Loca...](https://github.com/google/belief-localization) · 62 stars
- [Language Modeling with Editable External Knowledge](https://github.com/belindal/ERASE) · 36 stars
- [Composable Interventions for Language Models](https://github.com/hartvigsen-group/composable-interventions.) · 28 stars
- [RuleArena: A Benchmark for Rule-Guided Reasoning with LLMs in Real-World Scenari...](https://github.com/skyriver-2000/RuleArena.) · 26 stars
- [KnowledgeSmith: Uncovering Knowledge Updating in LLMs with Model Editing and Unl...](https://github.com/AIFrontierLab/KnowledgeSmith.git) · 9 stars
- [Model Editing for New Document Integration in Generative Information Retrieval](https://github.com/zhangzhen-research/DOME) · 8 stars
- [Fundamental Problems With Model Editing: How Should Rational Belief Revision Wor...](https://github.com/peterbhase/LLM-belief-revision) · 6 stars
- [MARS: Benchmarking the Metaphysical Reasoning Abilities of Language Models with ...](https://github.com/HKUST-KnowComp/MARS.) · 6 stars
- [MedREK: Retrieval-Based Editing for Medical LLMs with Key-Aware Prompts](https://github.com/mylittleriver/MedREK.) · 5 stars
- [Editing the Mind of Giants: An In-Depth Exploration of Pitfalls of Knowledge Edi...](https://github.com/MiuLab/EditLLM-Survey.) · 4 stars

## 常见基线方法

- **微调**：3 篇
- **MEMIT**：3 篇
- **现有知识编辑方法**：2 篇
- **现有SOTA非结构化知识编辑方法**：2 篇
- **ROME**：2 篇
- **现有编辑方法**：1 篇
- **LoRA**：1 篇
- **已有模型编辑方法**：1 篇
- **原生顺序定位-编辑方法**：1 篇
- **增量级正则方法**：1 篇

## 常用数据集

- **摘要未提及**：10 篇
- **数学推理任务**：5 篇
- **CounterFact**：4 篇
- **摘要未提及具体数据集**：3 篇
- **MQuAKE**：2 篇
- **ZsRE**：2 篇
- **UnKEBench**：2 篇
- **AKEW**：2 篇
- **HumanEval**：2 篇
- **MBPP**：2 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*