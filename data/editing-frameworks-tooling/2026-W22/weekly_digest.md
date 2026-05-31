# 编辑框架、工具与基准 — 2026-W22 (05/25-05/31)

本周新增 **20** 篇论文，**2** 篇附带代码。优先级：high 8 / medium 12 / low 0。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 评测信号 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|-----------|:----:|
| 1 | high | - | [Evi-Steer: Learning to Steer Biomedical Vision-Language Models t...](http://arxiv.org/abs/2605.26292v1) | steering | 在15个覆盖8器官8模态的生物医学数据集的少样本、域泛化设置下评测，性能优于SOTA... | 可将证据不确定性适配思路拓展到大模型知识编辑，提升编辑后模型的域泛化鲁棒性。 | ✅ |
| 2 | high | - | [Benchmarking Safety Risks of Knowledge-Intensive Reasoning under...](http://arxiv.org/abs/2605.10146v1) | evaluation/benchmark | 从攻击有效性、推理正确性、副作用三个维度，评估注入恶意知识对下游推理行为和可靠性的影... | 可基于EditRisk-Bench开发抵御恶意知识注入的安全编辑方法，降低知识编辑引入的推理... | — |
| 3 | high | - | [FineSteer: A Unified Framework for Fine-Grained Inference-Time S...](http://arxiv.org/abs/2604.15488v1) | steering | 在安全和真实性两类基准上开展实验，对比现有最优方法，验证引导效果与效用保留能力 | 可将该细粒度推理引导思路适配到知识编辑场景，缓解编辑后模型通用能力下降的问题 | — |
| 4 | high | - | [Harnessing Agentic Evolution](http://arxiv.org/abs/2605.13821v1) | meta-learning editor | 在智能体推理基准与三个开放端优化任务上，对比多个基线评测长周期进化搜索的性能 | 可将元智能体编辑进化机制的思路引入知识编辑，解决长周期知识编辑的漂移问题 | — |
| 5 | high | - | [Mitigating Hallucination in Vision-Language Models through Barri...](http://arxiv.org/abs/2605.29881v1) | steering | 在LLaVA-1.5-7B和Qwen-VL-Chat两个模型上测试，幻觉基准性能更优... | 这种按需自适应干预的引导思路，可迁移到通用大语言模型的事实幻觉缓解研究中。 | — |
| 6 | high | - | [Robust and Generalizable Safety Steering for Text-to-Image Diffu...](http://arxiv.org/abs/2605.30049v1) | steering | 评测目标域与整体不安全生成率，同时验证源域安全保留效果与生成图像质量，检验方法鲁棒泛... | 可将该位置感知稀疏特征迁移思路扩展到大模型安全对齐，探索跨风险域安全适配新方案 | — |
| 7 | high | - | [SAVeS: Steering Safety Judgments in Vision-Language Models via S...](http://arxiv.org/abs/2603.19092v1) | steering | 提出SAVeS基准与评测协议，可区分行为拒绝、接地安全推理和错误拒绝三类情形 | 可研究如何修正多模态安全模型的偏置，使其依赖接地视觉理解而非浅层语义提升鲁棒性 | — |
| 8 | high | - | [SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Kn...](http://arxiv.org/abs/2603.15226v1) | locate-then-edit | 评测多类大语言模型多次顺序编辑后的通用能力保留效果，验证编辑后模型的完整性 | 可扩展探索稀疏电路锚定机制在大模型海量编辑场景下的稳定性与泛化能力 | — |
| 9 | medium | - | [DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Plann...](http://arxiv.org/abs/2604.04875v1) | framework/tooling | 构建了带视觉连续性、听觉对齐定制指标的Mashup-Bench基准，通过客观指标和人... | 可借鉴该分层多智能体分工协调思路，解决复杂多模态场景下的知识编辑任务 | ✅ |
| 10 | medium | - | [AST: Adaptive, Seamless, and Training-Free Precise Speech Editin...](http://arxiv.org/abs/2604.16056v1) | framework/tooling | 提出WDTW指标评估未编辑区域时间一致性，构建公开基准数据集LibriSpeech-... | 可借鉴该无训练编辑、边界自适应约束思路，解决知识编辑中保留原知识一致性的问题。 | — |
| 11 | medium | - | [ATHENA: Adaptive Test-Time Steering for Improving Count Fidelity...](http://arxiv.org/abs/2603.19676v1) | steering | 在多个标准基准与新增复杂数据集、多个扩散骨干上验证，证明方法可提升计数保真度且保持良... | 可将测试时间自适应引导思路引入知识编辑领域，优化生成约束满足度，提升知识编辑输出可靠性。 | — |
| 12 | medium | - | [Beyond Static Personas: Situational Personality Steering for Lar...](http://arxiv.org/abs/2604.13846v3) | steering | 在公开基准PersonalityBench和自建SPBench上评测，验证方法对未知... | 可将这种神经元级情境引导思路迁移到知识编辑，提升编辑结果的情境适配能力 | — |

## 方法族分布

- **steering**：12 篇
- **framework/tooling**：5 篇
- **meta-learning editor**：1 篇
- **evaluation/benchmark**：1 篇
- **locate-then-edit**：1 篇

## 失败模式与风险信号

- 固定层安全引导不稳定，已知风险学习的引导机制无法可靠迁移到新风险域
- 解码过程中视觉grounding退化，模型生成不存在物体的幻觉，现有方法干预不合理。
- 现有确定性参数适配方法在领域偏移、图文对齐模糊场景下性能不佳
- 现有免微调视频编辑未充分利用噪声隐空间信息，编辑效果差、内容一致性不足
- 长周期进化易漂移，无法有效利用积累的进化证据
- 同策略自蒸馏中教师响应偏移导致师生不匹配、令牌级监督校准错误
- 编辑串扰，修改会蔓延至不应改变的非目标区域
- 现有基准缺失相关评估，恶意知识编辑的安全风险隐蔽难以检测
- 单轮编辑错误解析指令导致错误编辑、顺序编辑误差累积降低结果保真度
- 编辑后未编辑区域时间保真度低，编辑边界存在伪影，编辑质量与一致性难以兼顾

## 评测信号

- 评测目标域与整体不安全生成率，同时验证源域安全保留效果与生成图像质量，检验方法鲁棒泛化性
- 在LLaVA-1.5-7B和Qwen-VL-Chat两个模型上测试，幻觉基准性能更优，不损失通用任务性能。
- 在数学推理基准上验证，该方法可在不增加token级负对数似然的前提下稳定提升推理准确率
- 在15个覆盖8器官8模态的生物医学数据集的少样本、域泛化设置下评测，性能优于SOTA，已公开代码。
- 仅提及方法取得更好视觉质量与当前最优性能，未给出具体评测指标与数值细节
- 在智能体推理基准与三个开放端优化任务上，对比多个基线评测长周期进化搜索的性能
- 在多个不同推理基准上开展实验，验证所提方法相比现有同策略自蒸馏的推理性能提升
- 在多个图像编辑基准上取得最优图像相似性，相比扩散方法编辑速度提升6倍，模型仅960M参数
- 从攻击有效性、推理正确性、副作用三个维度，评估注入恶意知识对下游推理行为和可靠性的影响
- 重点评测复杂指令编辑的鲁棒性，以及合成数据学习得到的分解能力在真实场景的泛化迁移能力

## 可延展 Idea Hook

- 可将该位置感知稀疏特征迁移思路扩展到大模型安全对齐，探索跨风险域安全适配新方案
- 这种按需自适应干预的引导思路，可迁移到通用大语言模型的事实幻觉缓解研究中。
- 可将该推理模式引导思路用于优化知识编辑后小模型，提升其推理性能与可靠性
- 可将证据不确定性适配思路拓展到大模型知识编辑，提升编辑后模型的域泛化鲁棒性。
- 可将分区域差异化噪声引导的思路引入知识编辑，优化编辑后原有正确知识的保留效果
- 可将元智能体编辑进化机制的思路引入知识编辑，解决长周期知识编辑的漂移问题
- 可将该结果引导校准思路引入知识编辑后输出校准，缓解编辑偏差，提升编辑可靠性
- 可借鉴该工作约束编辑范围的思路，解决知识编辑中修改串扰非目标知识的问题
- 可基于EditRisk-Bench开发抵御恶意知识注入的安全编辑方法，降低知识编辑引入的推理安全风险
- 可借鉴本文顺序分解加合成数据训练的思路，解决多步复杂知识编辑的误差累积问题
- 可借鉴该无训练编辑、边界自适应约束思路，解决知识编辑中保留原知识一致性的问题。
- 可将该细粒度推理引导思路适配到知识编辑场景，缓解编辑后模型通用能力下降的问题

## 代码资源

- [DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Planning and Intent-G...](https://github.com/AK-DREAM/DIRECT) · 14 stars
- [Evi-Steer: Learning to Steer Biomedical Vision-Language Models through Efficient...](https://github.com/HealthX-Lab/Evi-Steer.)

## 常见基线方法

- **现有推理阶段幻觉缓解方法**：1 篇
- **现有SOTA参数高效适配方法**：1 篇
- **五种进化基线方法**：1 篇
- **四种进化基线方法**：1 篇
- **标准同策略自蒸馏(OPSD)**：1 篇
- **同策略自蒸馏其他变体**：1 篇
- **基于扩散的图像编辑方法**：1 篇
- **单轮图像编辑**：1 篇
- **传统顺序图像编辑**：1 篇
- **先前时间一致性最优基线**：1 篇

## 常用数据集

- **幻觉评测基准**：1 篇
- **通用多模态评测基准**：1 篇
- **15个覆盖8器官8模态的生物医学成像数据集**：1 篇
- **智能体与推理基准**：1 篇
- **开放端优化任务**：1 篇
- **多类推理基准**：1 篇
- **CrispEdit-2M**：1 篇
- **合成大规模图像编辑数据集**：1 篇
- **真实世界图像编辑数据集**：1 篇
- **LibriSpeech-Edit**：1 篇

---
*自动生成于 2026-05-31 | Knowledge Editing Direction Radar*