# 知识编辑核心方法 — 2026-W22 (05/25-05/31)

本周新增 **30** 篇论文，**7** 篇附带代码。优先级：high 28 / medium 2 / low 0。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 评测信号 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|-----------|:----:|
| 1 | high | - | [Distributed Multi-Layer Editing for Rule-Level Knowledge in Larg...](http://arxiv.org/abs/2604.08284) | locate-then-edit | 在四款主流大模型上评测实例迁移性与规则理解能力，验证规则级编辑的性能提升。 | 可探索分层定位编辑思路在不同类型知识编辑中的通用性，拓展知识编辑适用场景。 | ✅ |
| 2 | high | - | [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editin...](http://arxiv.org/abs/2604.12559v1) | framework/tooling | 构建了带细粒度问答对与事实级指标的UnFine诊断基准，评测细粒度问答与整体编辑性能 | 可将该细粒度事实锚定的解耦思路，扩展到大语言模型的多轮顺序知识编辑场景中 | ✅ |
| 3 | high | - | [From Fact Overwriting to Knowledge Evolution: Causal Editing via...](http://arxiv.org/abs/2605.28303v1) | distillation-based edito... | 在LLaMA-3.1和Qwen-2.5上评测编辑自我否定率与多跳推理准确率，开放了方... | 可探索将因果编辑范式拓展到多轮顺序知识更新场景，验证其在持续知识演化中的鲁棒性 | ✅ |
| 4 | high | - | [HoReN: Normalized Hopfield Retrieval for Large-Scale Sequential ...](http://arxiv.org/abs/2605.08143v2) | memory-based editor | 评测了编辑性能、复述泛化能力、多顺序编辑累积下的稳定性，验证了方法的大规模扩展能力 | 可探索将该归一化霍普菲尔德检索编辑思路，拓展到更大规模的多领域知识编辑场景中 | ✅ |
| 5 | high | - | [Modality-Decoupled Online Recursive Editing](http://arxiv.org/abs/2605.20273v1) | online editor | 在多个多模态大语言模型骨干和在线编辑基准上，评测了方法的可靠性、泛化性、局部性与效率... | 可将模态解耦思路推广到多模态大模型的知识遗忘任务，验证解耦策略对遗忘性能的提升效果。 | ✅ |
| 6 | high | - | [ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Mod...](http://arxiv.org/abs/2605.18879v2) | unlearning | 评测了方法的遗忘效果，验证该方法在遗忘敏感知识的同时可较好保留模型通用效用，效果优于... | 可尝试将这种带闭式解的正交更新思路扩展至大规模多样本隐私遗忘场景，进一步提升遗忘效率。 | ✅ |
| 7 | high | - | [Automatically Finding and Validating Unexpected Side-Effects of ...](http://arxiv.org/abs/2605.05090v1) | evaluation/benchmark | 评测工具识别干预的预期与意外行为副作用，验证其可区分不同幅度干预，无效应时无假阳性差... | 可基于该方法构建知识编辑与遗忘的标准化副作用评测基准，提升领域方法评估的可靠性 | — |
| 8 | high | - | [Benchmarking Safety Risks of Knowledge-Intensive Reasoning under...](http://arxiv.org/abs/2605.10146v1) | evaluation/benchmark | 聚焦注入恶意知识对下游推理行为与可靠性的影响，从攻击有效性、推理正确性、副作用多维度... | 可基于EditRisk-Bench研究如何提升大语言模型对恶意知识编辑攻击的鲁棒性，缓解推理... | — |
| 9 | high | - | [BetaEdit: Null-Space Constrained Sequential Model Editing](http://arxiv.org/abs/2605.09285v1) | framework/tooling | 在三个大语言模型的两个标准基准上评测，验证大规模顺序编辑场景下的编辑性能和模型通用能... | 可将零空间约束结合历史感知的思路拓展到大规模知识遗忘任务，验证该范式的实际效果 | — |
| 10 | high | - | [Beyond Binary Edits Robust Multimodal Knowledge Editing with Adv...](http://arxiv.org/abs/2605.23780v1) | other | 重点评测多模态知识编辑的泛化能力与鲁棒性，验证方法跨语义变体的编辑一致性效果 | 可探索将该对抗子空间对齐思路扩展到大规模多模态大模型的增量知识编辑任务中 | — |
| 11 | high | - | [Closed-Form Concept Erasure via Double Projections](http://arxiv.org/abs/2604.10032v1) | unlearning | 在多个主流生成模型上评测对象、风格擦除任务，验证方法的擦除性能与非目标概念保留效果。 | 可将该闭式双投影框架扩展到多概念顺序擦除场景，验证该方法应对多轮编辑的鲁棒性。 | — |
| 12 | high | - | [DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editin...](http://arxiv.org/abs/2604.07965) | locate-then-edit | 评测顺序编辑后的编辑成功率、幻觉程度、后向迁移得分，验证方法的知识保留稳定性。 | 可将子空间结构隔离思路推广到大语言模型终身编辑，探索缓解顺序编辑遗忘的方案。 | — |

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

## 可延展 Idea Hook

- 可进一步探究该框架在顺序多轮知识编辑场景下的性能，拓展多模态知识编辑应用边界。
- 可探索将SAE听诊器思路拓展到各类知识编辑场景，验证其在更多任务下的通用性
- 可探索将因果编辑范式拓展到多轮顺序知识更新场景，验证其在持续知识演化中的鲁棒性
- 可探索将该对抗子空间对齐思路扩展到大规模多模态大模型的增量知识编辑任务中
- 可将模态解耦思路推广到多模态大模型的知识遗忘任务，验证解耦策略对遗忘性能的提升效果。
- 可将该分布对齐的监督构建思路拓展到顺序知识编辑场景，验证其在多轮编辑下的效果。
- 可尝试将这种带闭式解的正交更新思路扩展至大规模多样本隐私遗忘场景，进一步提升遗忘效率。
- 可进一步探究该方法在多轮顺序编辑下的性能保持，拓展到更大规模稀疏MoE大模型
- 可探索将该定位编辑思路扩展到多模态大模型安全对齐，优化神经元定位精度与编辑效率。
- 可基于本文结论，探索更有效缓解多语言编辑干扰的新型高性能向量融合方法
- 可将本文的自强化稳定循环机制推广到各类知识编辑方法，提升长期顺序编辑的稳定性。
- 可基于EditRisk-Bench研究如何提升大语言模型对恶意知识编辑攻击的鲁棒性，缓解推理安全风险

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
*自动生成于 2026-05-31 | Knowledge Editing Direction Radar*