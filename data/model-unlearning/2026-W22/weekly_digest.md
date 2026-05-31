# 模型遗忘与反知识编辑 — 2026-W22 (05/25-05/31)

本周新增 **25** 篇论文，**6** 篇附带代码。优先级：high 25 / medium 0 / low 0。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 评测信号 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|-----------|:----:|
| 1 | high | - | [DualOptim+: Bridging Shared and Decoupled Optimizer States for B...](http://arxiv.org/abs/2605.21539v1) | unlearning | 在虚构遗忘、真实遗忘、安全对齐、多任务学习多类任务上，验证不同目标间的性能权衡与内存... | 可探索该框架在更大参数规模大模型上的适配性，以及更低量化精度下的遗忘性能表现 | ✅ |
| 2 | high | - | [Machine Unlearning for Masked Diffusion Language Models](http://arxiv.org/abs/2605.18253v1) | unlearning | 在标准基准与多种MDLM主干模型上开展实验，验证了所提方法的遗忘性能与隐私效用权衡 | 可进一步探索该框架在隐私数据遗忘、安全内容清除等实际场景下的适配与性能优化 | ✅ |
| 3 | high | - | [Measuring the Depth of LLM Unlearning via Activation Patching](http://arxiv.org/abs/2605.24614v1) | evaluation/benchmark | 在横跨8种遗忘方法的150个模型上验证，UDS的忠实度与鲁棒性优于20种对比指标，开... | 可将UDS扩展到不同架构LLM的遗忘审计，探索不同遗忘方法的擦除深度分布规律 | ✅ |
| 4 | high | - | [Object Hallucination-Free Reinforcement Unlearning for Vision-La...](http://arxiv.org/abs/2605.08031) | unlearning | 评测遗忘性能、知识保留性能与物体幻觉副作用，验证所提方法性能优于现有方法。 | 可拓展到多模态大模型遗忘任务，进一步探索不同奖励设计对幻觉抑制的作用。 | ✅ |
| 5 | high | - | [On the Robustness of Machine Unlearning for Vision-Language Mode...](http://arxiv.org/abs/2605.26992) | survey | 在多类提示设置下统一评估现有方法，通过三种攻击范式检验VLM机器遗忘的实际鲁棒性 | 可基于本文提出的攻击范式，设计能抵抗知识重激活的鲁棒多模态机器遗忘方法 | ✅ |
| 6 | high | - | [ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Mod...](http://arxiv.org/abs/2605.18879v2) | unlearning | 评测方法的遗忘效果与模型通用效用的保留能力，验证所提方法性能优于现有各类基线方法。 | 可探索将这种带闭式解的表征正交编辑思路，扩展到大规模多样本场景的大模型知识遗忘中。 | ✅ |
| 7 | high | - | [ASRU: Activation Steering Meets Reinforcement Unlearning for Mul...](http://arxiv.org/abs/2605.15687v1) | unlearning | 同时评测遗忘效果、遗忘后生成质量与模型原有效用，关注三者之间的平衡表现。 | 可尝试将该激活引导结合强化优化的遗忘框架推广到不同架构的多模态大模型中验证通用性。 | — |
| 8 | high | - | [CATA: Continual Machine Unlearning via Conflict-Averse Task Arit...](http://arxiv.org/abs/2605.18610v1) | unlearning | 在单次遗忘和持续遗忘两种设置下，评测遗忘有效性、模型保真度与遗忘持续性三项核心指标 | 可探索该冲突规避任务算术框架，如何适配更大规模多模态大模型的持续机器遗忘场景 | — |
| 9 | high | - | [Calibration vs Decision Making: Revisiting the Reliability Parad...](http://arxiv.org/abs/2605.20915v1) | evaluation/benchmark | 同时从概率校准误差和决策规则的虚假关联依赖两个层面，评估遗忘后语言模型的可靠性 | 能否设计同时覆盖概率校准与决策规则可靠性的机器遗忘评估指标，提升可靠性判断准确性 | — |
| 10 | high | - | [Causal Unlearning in Collaborative Optimization: Exact and Appro...](http://arxiv.org/abs/2605.20341v1) | unlearning | 评测了方法加速比、模型测试精度、遗忘集成员推理成功率，验证了效率、精度和隐私恢复效果 | 可拓展研究异质联邦场景下大规模大模型的高效因果遗忘，适配生产环境异步删除需求 | — |
| 11 | high | - | [Distinguishable Deletion: Unifying Knowledge Erasure and Refusal...](http://arxiv.org/abs/2605.16776v1) | unlearning | 通过大量实验对比现有两类方法，验证所提EUA方法在大模型知识遗忘任务上性能优于已有方... | 可探索该能量边界统一框架在顺序遗忘、大规模多类敏感知识遗忘场景下的泛化能力。 | — |
| 12 | high | - | [DurableUn: Quantization-Induced Recovery Attacks in Machine Unle...](http://arxiv.org/abs/2605.02196) | unlearning | 评测多种遗忘方法在不同精度下的遗忘效果、模型效用与量化鲁棒性，验证所提方法的多指标均... | 可进一步研究破解FA-RA-Q-INT4三难困境，实现兼顾遗忘、效用与量化鲁棒性的鲁棒遗忘。 | — |

## 方法族分布

- **unlearning**：18 篇
- **evaluation/benchmark**：6 篇
- **survey**：1 篇

## 失败模式与风险信号

- 跨请求干扰、顺序请求下模型效用损失累积
- 反事实训练存在知识冲突干扰优化，以及幻觉溢出推高无关领域幻觉率
- 现有针对已遗忘模型的恢复攻击实用性差，生成的对抗提示易被安全过滤检测。
- 遗忘不彻底，残留知识隐藏于内部表征，现有评估指标缺乏通用性无法有效检测
- 仅用校准误差衡量遗忘后模型可靠性，无法识别依赖虚假关联的不可靠决策
- 遗忘与保留目标梯度方向冲突，导致二者性能权衡效果不佳
- 数据删除后重训开销过高，遗忘更新易串扰影响无关客户端
- 顺序更新中冲突更新削弱过往遗忘效果，导致已移除知识重新出现
- 掩码扩散语言模型领域缺乏专用的机器遗忘方案
- 知识删除易产生偏置删除，拒绝范式遗忘不彻底，存在有害知识复现问题

## 评测信号

- 验证了方法的遗忘效果、原模型效用保留、顺序请求可扩展性，以及对转述跨语言查询的鲁棒性。
- 提出带新型权衡指标和梯度诊断工具的扩展基准RWKU+，聚焦大语言模型遗忘的隐藏成本与副作用。
- 评测攻击成功率、对抗提示隐蔽性与生成图像质量，验证了BEAP相较现有方法的性能提升。
- 在横跨8种遗忘方法的150个模型上验证，UDS的忠实度与鲁棒性优于20种对比指标，开放了代码
- 同时从概率校准误差和决策规则的虚假关联依赖两个层面，评估遗忘后语言模型的可靠性
- 在虚构遗忘、真实遗忘、安全对齐、多任务学习多类任务上，验证不同目标间的性能权衡与内存开销
- 评测了方法加速比、模型测试精度、遗忘集成员推理成功率，验证了效率、精度和隐私恢复效果
- 在单次遗忘和持续遗忘两种设置下，评测遗忘有效性、模型保真度与遗忘持续性三项核心指标
- 在标准基准与多种MDLM主干模型上开展实验，验证了所提方法的遗忘性能与隐私效用权衡
- 通过大量实验对比现有两类方法，验证所提EUA方法在大模型知识遗忘任务上性能优于已有方法。

## 可延展 Idea Hook

- 可探索结合大模型上下文理解能力优化拒绝规则诱导，提升大规模顺序遗忘场景的性能。
- 针对反事实知识训练的两大缺陷，可探索缓解知识冲突与幻觉溢出的改进型大语言模型遗忘方案。
- 可基于该攻击思路设计更鲁棒的文生图概念遗忘方法，提升遗忘后模型的安全防御能力。
- 可将UDS扩展到不同架构LLM的遗忘审计，探索不同遗忘方法的擦除深度分布规律
- 能否设计同时覆盖概率校准与决策规则可靠性的机器遗忘评估指标，提升可靠性判断准确性
- 可探索该框架在更大参数规模大模型上的适配性，以及更低量化精度下的遗忘性能表现
- 可拓展研究异质联邦场景下大规模大模型的高效因果遗忘，适配生产环境异步删除需求
- 可探索该冲突规避任务算术框架，如何适配更大规模多模态大模型的持续机器遗忘场景
- 可进一步探索该框架在隐私数据遗忘、安全内容清除等实际场景下的适配与性能优化
- 可探索该能量边界统一框架在顺序遗忘、大规模多类敏感知识遗忘场景下的泛化能力。
- 可探索将这种带闭式解的表征正交编辑思路，扩展到大规模多样本场景的大模型知识遗忘中。
- 可尝试将该激活引导结合强化优化的遗忘框架推广到不同架构的多模态大模型中验证通用性。

## 代码资源

- [Measuring the Depth of LLM Unlearning via Activation Patching](https://github.com/gnueaj/unlearning-depth-score) · 5 stars
- [Machine Unlearning for Masked Diffusion Language Models](https://github.com/leegeoru/MDU.) · 2 stars
- [ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Models](https://github.com/XMUDeepLIT/ZeroUnlearn.) · 2 stars
- [DualOptim+: Bridging Shared and Decoupled Optimizer States for Better Machine Un...](https://github.com/CityU-MLO/DualOptimPlus.) · 1 stars
- [On the Robustness of Machine Unlearning for Vision-Language Models](https://github.com/XMUDeepLIT/VLM-UnL-Attack.)
- [Object Hallucination-Free Reinforcement Unlearning for Vision-Language Models](https://github.com/XMUDeepLIT/HFRU.)

## 常见基线方法

- **现有输出级遗忘评估指标**：1 篇
- **现有白盒遗忘评估指标**：1 篇
- **预训练语言模型**：1 篇
- **微调语言模型**：1 篇
- **从头重训**：1 篇
- **合理基线**：1 篇
- **现有大语言模型机器遗忘方法**：1 篇
- **知识删除类方法**：1 篇
- **可区分拒绝类方法**：1 篇
- **梯度类机器遗忘方法**：1 篇

## 常用数据集

- **TOFU**：4 篇
- **RWKU+**：1 篇
- **摘要未提及**：1 篇
- **CIFAR-10**：1 篇
- **MNIST**：1 篇
- **Fashion-MNIST**：1 篇
- **标准基准数据集**：1 篇
- **多模型安全风险评测基准**：1 篇
- **六个未提及具体名称的数据集**：1 篇
- **未提及具体名称数据集1**：1 篇

---
*自动生成于 2026-05-31 | Knowledge Editing Direction Radar*