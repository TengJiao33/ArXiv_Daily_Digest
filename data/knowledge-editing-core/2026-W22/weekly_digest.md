# knowledge-editing-core — 2026-W22 (05/25-05/31)

本周新增 **30** 篇论文，**7** 篇附带代码。优先级：high 28 / medium 2 / low 0。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Distributed Multi-Layer Editing for Rule-Level Knowledge in Larg...](http://arxiv.org/abs/2604.08284) | locate-then-edit | 公式与描述集中在Transformer较早层，实例关联中间层；DMLE比最优基线分别提升13... | 在四款主流大模型上评测实例迁移性与规则理解能力，验证规则级编辑的性能提升。 | 现有单一层/连续块局部干预无法可靠编辑需跨多形式一致的规则级知识... | ✅ |
| 2 | high | - | [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editin...](http://arxiv.org/abs/2604.12559v1) | framework/tooling | 将离散事实锚定在浅层、深层仅做最小更新，可在保持整体编辑SOTA的同时大幅提升细粒度问答性能 | 构建了带细粒度问答对与事实级指标的UnFine诊断基准，评测细粒度问答与整体编辑... | 现有方法整体记忆文本，缺乏可靠的细粒度事实访问能力 | ✅ |
| 3 | high | - | [From Fact Overwriting to Knowledge Evolution: Causal Editing via...](http://arxiv.org/abs/2605.28303v1) | distillation-based edito... | 原有静态事实覆盖编辑的自我反驳率达95.6%，本文CODE方法可将其压制到1.8%，多跳准确... | 在LLaMA-3.1和Qwen-2.5上评测编辑自我否定率与多跳推理准确率，开放... | 静态事实覆盖编辑破坏预训练逻辑拓扑，引发认知失调，产生高比例自我... | ✅ |
| 4 | high | - | [HoReN: Normalized Hopfield Retrieval for Large-Scale Sequential ...](http://arxiv.org/abs/2605.08143v2) | memory-based editor | HoReN可在ZsRE上支撑5万次顺序编辑，性能仍稳定在0.93以上，现有方法1万次编辑前就... | 评测了编辑性能、复述泛化能力、多顺序编辑累积下的稳定性，验证了方法的大规模扩展能... | 顺序编辑累积导致性能崩溃 | ✅ |
| 5 | high | - | [Modality-Decoupled Online Recursive Editing](http://arxiv.org/abs/2605.20273v1) | online editor | 分模态维护局部统计加固定正交低秩编辑子空间，可同时缓解跨模态冲突与长周期编辑干扰，性能优于强... | 在多个多模态大语言模型骨干和在线编辑基准上，评测了方法的可靠性、泛化性、局部性与... | 跨模态冲突、顺序编辑的长周期干扰与编辑间串扰 | ✅ |
| 6 | high | - | [ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Mod...](http://arxiv.org/abs/2605.18879v2) | unlearning | 通过带闭式解的乘法参数更新实现表征正交性，少样本设置下性能优于现有基线，同时可保留模型通用效... | 评测了方法的遗忘效果，验证该方法在遗忘敏感知识的同时可较好保留模型通用效用，效果... | 现有遗忘方法计算成本高，遗忘后易损害模型相关知识与整体效用 | ✅ |
| 7 | high | - | [Automatically Finding and Validating Unexpected Side-Effects of ...](http://arxiv.org/abs/2605.05090v1) | evaluation/benchmark | 该流水线可可靠恢复合成注入的已知变化，能区分大干预与细微干预，无效应时不产生幻觉差异 | 评测工具识别干预的预期与意外行为副作用，验证其可区分不同幅度干预，无效应时无假阳... | 干预后意外副作用难以自动发现，容易产生虚假差异结论 | — |
| 8 | high | - | [Benchmarking Safety Risks of Knowledge-Intensive Reasoning under...](http://arxiv.org/abs/2605.10146v1) | evaluation/benchmark | 恶意知识编辑可稳定诱导错误不安全推理且基本保留通用能力，风险难检测，识别出三类影响风险的关键... | 聚焦注入恶意知识对下游推理行为与可靠性的影响，从攻击有效性、推理正确性、副作用多... | 现有基准缺乏对恶意知识编辑安全风险的系统评估，恶意编辑风险隐蔽难... | — |
| 9 | high | - | [BetaEdit: Null-Space Constrained Sequential Model Editing](http://arxiv.org/abs/2605.09285v1) | framework/tooling | 近似零空间的现有零空间编辑方法存在固有知识泄露，历史感知更新可有效保留长程顺序编辑的性能和通... | 在三个大语言模型的两个标准基准上评测，验证大规模顺序编辑场景下的编辑性能和模型通... | 知识泄露，大规模顺序编辑性能退化 | — |
| 10 | high | - | [Beyond Binary Edits Robust Multimodal Knowledge Editing with Adv...](http://arxiv.org/abs/2605.23780v1) | other | 结合对抗语义变体生成与低秩对齐的机制，可有效提升多模态知识编辑跨语义变体的泛化鲁棒性 | 重点评测多模态知识编辑的泛化能力与鲁棒性，验证方法跨语义变体的编辑一致性效果 | 现有多模态知识编辑无法在语义等价的多模态变体间有效传播编辑效果 | — |
| 11 | high | - | [Closed-Form Concept Erasure via Double Projections](http://arxiv.org/abs/2604.10032v1) | unlearning | 双投影闭式概念擦除无需训练仅需数秒，在多种生成模型上性能不输SOTA，且更好保留非目标概念。 | 在多个主流生成模型上评测对象、风格擦除任务，验证方法的擦除性能与非目标概念保留效... | 概念擦除过程中误扭曲无关非目标概念的编辑串扰问题 | — |
| 12 | high | - | [DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editin...](http://arxiv.org/abs/2604.07965) | locate-then-edit | 1000次顺序编辑后编辑成功率仍超95%，相较现有方法幻觉降低3%-5%，后向迁移得分最优。 | 评测顺序编辑后的编辑成功率、幻觉程度、后向迁移得分，验证方法的知识保留稳定性。 | 顺序编辑中概念纠缠引发编辑串扰、灾难性遗忘与性能退化 | — |

## A 会 / Venue 标签

- **ICML 2026**：2 篇

## 方法族分布

- **locate-then-edit**：8 篇
- **evaluation/benchmark**：5 篇
- **framework/tooling**：5 篇
- **other**：4 篇
- **unlearning**：3 篇
- **memory-based editor**：2 篇
- **distillation-based editor**：1 篇
- **online editor**：1 篇
- **知识编辑方法**：1 篇

## 失败模式与风险信号

- 因果错位导致编辑局限于单样本，特征纠缠引发无关知识意外改动
- SAE特征子空间投影造成信息瓶颈，丢弃大量修改能量，编辑无显著性能提升
- 静态事实覆盖编辑破坏预训练逻辑拓扑，引发认知失调，产生高比例自我反驳
- 现有多模态知识编辑无法在语义等价的多模态变体间有效传播编辑效果
- 跨模态冲突、顺序编辑的长周期干扰与编辑间串扰
- 知识注入后模型原有能力大幅下降，发生灾难性遗忘
- 现有遗忘方法计算成本高，遗忘后易损害模型相关知识与整体效用
- 现有知识编辑方法多适配密集层，无法高效适配混合专家架构大模型
- 安全-效用权衡，良性任务保留能力下降
- 多语言编辑相互串扰

## 评测信号

- 在多个基准和多款多模态大语言模型上评测，验证方法兼顾编辑局部性与向相关上下文的泛化能力。
- 在Minerva Math基准的7个数学科目评测，该方法显著提升5个科目准确率，无显著性能退化
- 在LLaMA-3.1和Qwen-2.5上评测编辑自我否定率与多跳推理准确率，开放了方法实现代码
- 重点评测多模态知识编辑的泛化能力与鲁棒性，验证方法跨语义变体的编辑一致性效果
- 在多个多模态大语言模型骨干和在线编辑基准上，评测了方法的可靠性、泛化性、局部性与效率。
- 评测知识注入准确率与原有能力保留程度，重点考察知识记忆与能力保留的权衡效果。
- 评测了方法的遗忘效果，验证该方法在遗忘敏感知识的同时可较好保留模型通用效用，效果优于现有基线。
- 在主流知识编辑指标上验证编辑质量，同时对比测试了不同方法的编辑加速效果
- 评测方法在LLM和VLM上的越狱缓解效果，同时验证编辑对模型通用推理能力的影响。
- 在大规模批量多语言编辑场景下，评测融合方法可靠性、多语言干扰缓解效果及参数敏感性

## 代码资源

- [Distributed Multi-Layer Editing for Rule-Level Knowledge in Large Language Model...](https://github.com/Pepper66/DMLE.) · 4 stars
- [ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models](https://github.com/XMUDeepLIT/ZeroUnlearn.) · 2 stars
- [Modality-Decoupled Online Recursive Editing](https://github.com/lab-klc/M-ORE.) · 1 stars
- [HoReN: Normalized Hopfield Retrieval for Large-Scale Sequential Model Editing](https://github.com/ha11ucin8/HoReN.) · 1 stars
- [From Fact Overwriting to Knowledge Evolution: Causal Editing via On-Policy Self-...](https://github.com/CrashBugger/CODE.)
- [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](https://github.com/caskcsg/FABLE.)
- [Darkness Visible: Reading the Exception Handler of a Language Model](https://github.com/pbalogh/transparent-gpt2)

## 常见基线方法

- **SAE特征子空间投影引导的模型编辑方法**：1 篇
- **监督微调(SFT)**：1 篇
- **在线策略自蒸馏**：1 篇
- **摘要未提及具体基线**：1 篇
- **无共享协方差简单求和**：1 篇
- **单语定位后编辑方法**：1 篇
- **现有零空间编辑方法**：1 篇
- **现有历史感知编辑方法**：1 篇
- **参数修改类编辑器**：1 篇
- **参数保留类编辑器**：1 篇

## 常用数据集

- **Minerva Math**：1 篇
- **自建合成评测语料**：1 篇
- **开放域事实问答基准**：1 篇
- **知识编辑基准**：1 篇
- **摘要未提及具体数据集**：1 篇
- **MzsRE**：1 篇
- **标准顺序编辑基准一**：1 篇
- **标准顺序编辑基准二**：1 篇
- **EC-Bench**：1 篇
- **ZsRE**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*