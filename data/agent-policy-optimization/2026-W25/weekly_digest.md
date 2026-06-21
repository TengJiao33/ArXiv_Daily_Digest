# Agent 策略优化与在线蒸馏 — 2026-W25 (06/15-06/21)

本周新增 **64** 篇论文，**9** 篇附带代码。优先级：high 32 / medium 26 / low 6。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 控制/评测 | 风险 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|------|-----------|:----:|
| 1 | high | - | [Connect the Dots: Training LLMs for Long-Lifecycle Agents with C...](http://arxiv.org/abs/2606.20002v1) | policy optimization | 通过端到端强化学习框架训练，搭配定制化任务环境激励，让Agent自主学习更新环境... | 仅完成概念验证，评测基于自建定制环境，方法在真实长生命周期场景的... | 能否将本文长生命周期Agent持续更新范式与在线蒸馏结合，提升长生命周期Agent的迭代优化... | ✅ |
| 2 | high | - | [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic re...](http://arxiv.org/abs/2606.16771v1) | policy optimization | 通过冲突感知过滤机制屏蔽存在严重奖励分歧的训练样本，结合查询级动态重加权调整更新... | 仅在有限的多奖励场景验证，未测试大规模复杂Agent任务下方法的... | 多奖励冲突广泛存在于Agent后训练对齐中，可尝试将该冲突感知过滤机制扩展到在线策略蒸馏场景 | ✅ |
| 3 | high | - | [REVES: REvision and VErification--Augmented Training for Test-Ti...](http://arxiv.org/abs/2606.18910v1) | policy optimization | 将成功轨迹中的中间近错样本转换为修正与验证提示，交替在线增强和策略优化改进模型推... | 依赖显式验证反馈（测试用例、真值、约束），无显式反馈的场景效果可... | 可将该修正验证训练框架结合在线策略蒸馏，优化agent多步推理的测试时缩放效果，提升推理可靠... | ✅ |
| 4 | high | - | [Reward Hacking in Language Model Agents: Revisiting AI Safety Gr...](http://arxiv.org/abs/2606.15385v1) | evaluation/benchmark | 构建可控评测套件研究语言智能体奖励黑客现象，未提出新的模型行为控制改进方法。 | 基于代理奖励优化的语言智能体天然存在奖励黑客风险，标准方法无法缓... | 我们研究Agent策略优化与在线蒸馏，能否用在线奖励蒸馏校正缓解语言智能体的奖励黑客问题？ | ✅ |
| 5 | high | - | [STARE: Surprisal-Guided Token-Level Advantage Reweighting for Po...](http://arxiv.org/abs/2606.19236v1) | policy optimization | 通过意外度引导的token级优势重加权，结合目标熵闭环调控，稳定RL后训练的策略... | 目前仅在闭卷推理和多轮工具任务验证，未在开放域复杂agent任务... | 可将该熵稳定调控思路引入agent在线策略蒸馏，解决在线蒸馏过程中的策略熵塌缩问题，提升训练... | ✅ |
| 6 | high | - | [VeriGraph: Towards Verifiable Data-Analytic Agents](http://arxiv.org/abs/2606.16603v1) | policy optimization | 通过构建显式异质证据DAG，采用监督多目标的复合奖励进行图策略优化，规范智能体推... | 仅在有限基准测试验证，未验证大规模真实场景适用性，方法的工程可扩... | 能否将VeriGraph的显式证据约束与复合奖励思路，结合在线蒸馏提升通用推理智能体的可验证... | ✅ |
| 7 | high | - | [A First-Principles Derivation of LLM Policy Optimization: From E...](http://arxiv.org/abs/2606.16733v1) | survey | 通过构建以轨迹侧、奖励侧为双轴的统一分析框架，梳理现有策略优化方法，定位现有方法... | 本文为纯分析综述，提出的框架与结论未经过实证验证，有待进一步实验... | 可基于该框架梳理出的问题，设计联合优化轨迹侧与奖励侧的新型Agent策略优化方法。 | — |
| 8 | high | - | [Beyond Entropy: Learning from Token-Level Distributional Deviati...](http://arxiv.org/abs/2606.19771v1) | policy optimization | 通过JS散度筛选关键Token做选择性更新，同时调节香农熵和二阶Rényi熵，稳... | 仅在7B及以下开源模型验证，未测试更大规模模型，泛化性待验证 | 可将该选择性Token更新的优化思路，拓展到Agent在线策略蒸馏中解决优化不稳定问题 | — |
| 9 | high | - | [Beyond Reward Engineering: A Data Recipe for Long-Context Reinfo...](http://arxiv.org/abs/2606.18831v1) | policy optimization | 通过构建适配长上下文的训练数据，搭配GRPO强化学习优化Agent的长上下文推理... | 仅在有限模型和封闭基准验证，未验证开放场景下的泛化可靠性。 | 能否将这种以数据为中心的长上下文RL思路，结合在线蒸馏优化长上下文Agent的策略？ | — |
| 10 | high | - | [CORA: Analyzing and bridging thinking-answer gap in Multimodal R...](http://arxiv.org/abs/2606.14691v1) | reward learning | 通过引入额外的思考-答案一致性奖励，结合混合奖励优势拆分，对齐推理与答案的语义一... | 摘要未披露具体实验数值与更多细节，未验证不同规模模型上的通用性，... | 可将该一致性对齐思路拓展到多模态Agent推理中，设计兼顾性能和推理一致性的Agent奖励函... | — |
| 11 | high | - | [CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and H...](http://arxiv.org/abs/2606.14179v1) | reward learning | 通过缓存轨迹降低训练成本，设计缓存感知动态奖励，结合监督微调与GRPO优化智能体... | 缓存轨迹保真度依赖大模型生成，存在偏差，实际在线部署效果未在摘要... | 可探索基于缓存大模型轨迹的低成本agent策略优化，验证缓存感知奖励设计在在线蒸馏中的效果 | — |
| 12 | high | - | [Closing the Feedback Loop: From Experience Extraction to Insight...](http://arxiv.org/abs/2606.17591v1) | policy optimization | 构建规则-证据-技能三层架构，通过反馈驱动的精选回路治理洞见，无需参数更新即可调... | 仅在金融预测单一场景验证，方法在通用智能体任务中的泛化性尚未得到... | 基于反馈的洞见治理思路能否解决通用场景非平稳环境下在线智能体的留存-遗忘两难问题？ | — |

## 方法族分布

- **policy optimization**：37 篇
- **reward learning**：7 篇
- **online distillation**：6 篇
- **skill generation**：3 篇
- **unlearning/safety**：3 篇
- **survey**：2 篇
- **tool-use control**：2 篇
- **evaluation/benchmark**：1 篇
- **other**：1 篇
- **model steering**：1 篇
- **multi-agent coordination**：1 篇

## 失败模式与风险信号

- 推理过程与最终答案语义不一致
- 原有RL训练的智能体缺乏进度元认知，阻碍长范围任务性能扩展
- 在线工具执行成本过高，噪声缓存环境会降低智能体训练的鲁棒性
- 仅提示评测低估大模型ICD编码能力，漏码问题降低整体编码性能
- 长上下文关键证据定位失效
- 评分标准不完整，导致深度研究Agent强化学习训练效率低下
- 稀疏奖励无法有效强化有用的中间推理行为
- 错误回答过度思考、token效率低，部分模型无法通过该方法获得性能提升。
- 通用查询策略无法适配不同检索器特性，导致RAG性能无法达到最优。
- 单一技能局限导致解空间探索不足，智能体易陷入同质次优解

## 评测信号

- 实验验证CORA可提升多模态推理任务性能，有效缓解思考-答案不一致，生成更可靠的推理轨迹。
- 提出评测应从原有静态基准转向沙箱环境下可审计、自进化的AI生态系统评测。
- 在三个基准任务上，相比基线模型可获得最高12%的绝对任务成功率提升，性能增益十分明显。
- 小型模型达到92%的多步工具调用过程准确率，接近GPT-5的94%，算力需求仅为GPT-5的百分之一
- 对比不同训练设置下大语言模型ICD编码的表现，验证各后训练阶段对编码性能与宏观指标的提升效果。
- ContextRL较标准GRPO长周期基准平均提升+2.2%、VQA基准提升+1.8%，排除了新增对比数据的增益影响
- 和现有开放SOTA深度研究模型性能相当，强化学习训练GPU耗时降低约13倍，训练效率提升显著。
- 实验验证ExpRL的RL预启动效果优于多个对比基线，能够为后续稀疏奖励RL提供更优初始化
- 测试数学、排序、优化等推理任务性能，分析方法对过度思考、token效率的影响，未公开具体基准数值。
- 摘要仅提及性能可通过引入检索器专属人类指导和扩大模型规模提升，未给出具体量化评测结果。

## 控制机制 / Harness 信号

- 通过引入额外的思考-答案一致性奖励，结合混合奖励优势拆分，对齐推理与答案的语义一致性。
- 提出通过推理时扩展计算、反思、过程监督、强化学习优化认知，搭配持久工作区、可复用技能与验证循环改进执行。
- 通过先执行后回溯反思的范式，让智能体自生成进度信号，借助复合奖励训练优化智能体策略。
- 通过缓存轨迹降低训练成本，设计缓存感知动态奖励，结合监督微调与GRPO优化智能体工具调用能力
- 通过监督微调和强化学习后训练适配ICD编码任务，提出扩展GRPO的PHI课程优化漏码，提升模型编码性能。
- 通过设计上下文选择的辅助奖励目标，利用强化学习引导模型学习细粒度上下文 grounding，改进推理性能
- 通过证据树构建完整可靠的评分标准监督，使用基于评分的GRPO奖励优化Agent策略，提升训练效率。
- 将参考解答作为奖励支架，由LLM评判生成密集奖励，通过强化学习优化大模型中期推理策略
- 挖掘推理的外在关键token与内在认知特性，通过推理提示引导、训练数据增强改进代码推理性能。
- 通过强化学习引导大模型学习适配不同检索器特性的查询生成策略，借助分支rollout技术提升训练稳定性。

## 可靠性 / 落地风险

- 摘要未披露具体实验数值与更多细节，未验证不同规模模型上的通用性，可复现信息不足。
- 仅为概念范式梳理，未提供实证验证，提出的新评测框架也未落地实现。
- 仅在三个中小规模基准验证，尚未在更大规模的复杂长范围任务上验证效果。
- 缓存轨迹保真度依赖大模型生成，存在偏差，实际在线部署效果未在摘要中验证
- 未在真实临床生产场景验证，未披露数据集合规性，结论推广性有待验证。
- 仅在公开基准验证，性能提升幅度较小，未验证真实复杂场景下的泛化能力
- 未披露三个基准的具体信息，数据构建过程的可复现性未得到验证。
- 依赖额外大语言模型做奖励评判，会显著提升训练阶段的算力开销，整体训练成本较高
- 未在公开标准基准上充分验证结论，结论在更多模型和任务上的普适性有待验证。
- 未公开具体评测数据集与量化结果，结论普适性缺乏充分验证，可复现性存在一定风险。

## 可延展 Idea Hook

- 可将该一致性对齐思路拓展到多模态Agent推理中，设计兼顾性能和推理一致性的Agent奖励函数。
- 如何基于持久工作区与可复用技能的设计，提升长周期自主Agent任务执行的可靠性？
- 可探索将该回溯式进度感知机制结合在线蒸馏，进一步优化长范围任务的LLM智能体策略性能。
- 可探索基于缓存大模型轨迹的低成本agent策略优化，验证缓存感知奖励设计在在线蒸馏中的效果
- 可借鉴本文分阶段后训练+课程强化学习的思路，优化agent任务场景下的动作召回与性能。
- 能否将这种上下文感知辅助奖励目标结合在线蒸馏，提升长周期agent策略的泛化性能？
- 可借鉴该证据树评分监督思路，探索其结合在线策略蒸馏优化Agent训练效率的可行性。
- 能不能将ExpRL的奖励支架思路应用到agent在线策略蒸馏中，改进agent中间行为的奖励设计？
- 能否将本文发现的代码推理认知行为融入agent策略优化，提升复杂推理任务的agent token效率？
- 可将本文针对不同检索工具的差异化策略优化思路，迁移到agent工具调用的策略优化研究中。
- 能否将集体技能树搜索与在线策略蒸馏结合，用教师集体技能提升学生agent的工具泛化能力？
- 多奖励冲突广泛存在于Agent后训练对齐中，可尝试将该冲突感知过滤机制扩展到在线策略蒸馏场景

## 下次可问导师的问题

- 我们是否可以将这种思考-答案一致性奖励引入到当前正在做的Agent在线蒸馏奖励设计中？
- 我们要不要沿着数字同事的「工作区+技能」范式，开展长周期Agent可靠性方向的研究？
- 我们是否可以借鉴该进度感知思路，改进现有在线蒸馏的智能体训练方案？
- 这种基于缓存轨迹训练小型工具调用智能体的思路，能不能迁移到我们的在线策略蒸馏研究中？
- 我们是否可以将本文扩展GRPO的课程后训练思路，迁移到当前的agent策略优化任务中？
- 这种上下文辅助奖励目标能否适配在线蒸馏，进一步提升编码智能体的策略性能？
- 我们是否可以借鉴该评分构建思路改进当前Agent奖励学习方案，提升训练效率？
- 将ExpRL的密集奖励支架思路引入agent在线策略蒸馏是否可行，能否带来明显性能提升？
- 将本文发现的验证回溯行为引入agent在线蒸馏，是否能有效提升coding agent的推理性能？
- 我们做agent工具调用策略优化，是否可以借鉴这篇工作的RL适配思路做改进？
- 我们当前的在线蒸馏方向，结合这种多模型集体技能构建思路会不会有明显增益？
- 我们正在做在线多奖励策略蒸馏，是否适合引入该冲突感知过滤机制来提升训练效率？

## 代码资源

- [Connect the Dots: Training LLMs for Long-Lifecycle Agents with Cross-Domain Gene...](https://github.com/agentscope-ai/Trinity-RFT) · 654 stars
- [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled P...](https://github.com/Qwen-Applications/GD2PO.) · 6 stars
- [Learning from the Self-future: On-policy Self-distillation for dLLMs](https://github.com/xingzhejun/d-OPSD.) · 3 stars
- [STARE: Surprisal-Guided Token-Level Advantage Reweighting for Policy Entropy Sta...](https://github.com/hp-luo/STARE.) · 2 stars
- [VeriGraph: Towards Verifiable Data-Analytic Agents](https://github.com/ignorejjj/VeriGraph.) · 1 stars
- [Can Post-Training Turn LLMs into Good Medical Coders? An Empirical Study of Gene...](https://github.com/AlexandreWANG915/LLM4ICD.)
- [Understanding the Behaviors of Environment-aware Information Retrieval](https://github.com/LCO-Embedding/Envs-aware-Information-Retrieval.)
- [Reward Hacking in Language Model Agents: Revisiting AI Safety Gridworlds](https://github.com/asparius/verl-agent-safety)
- [REVES: REvision and VErification--Augmented Training for Test-Time Scaling](https://github.com/yxliu02/REVES.git.)

## 常见基线方法

- **GRPO**：7 篇
- **DAPO**：3 篇
- **标准GRPO**：2 篇
- **SFT**：2 篇
- **传统聊天机器人范式**：1 篇
- **临时工具调用Agent**：1 篇
- **原Qwen系列模型**：1 篇
- **在线进度提示方法**：1 篇
- **原生Qwen3-4B-Thinking**：1 篇
- **GPT-5**：1 篇

## 常用数据集

- **ALFWorld**：3 篇
- **摘要未提及**：3 篇
- **WebShop**：2 篇
- **AIME 2024**：2 篇
- **AIME 2025**：2 篇
- **代表性多模态推理基准**：1 篇
- **Sokoban**：1 篇
- **公开智能体工具调用基准**：1 篇
- **摘要未提及具体数据集**：1 篇
- **长周期推理基准集合**：1 篇

---
*自动生成于 2026-06-21 | ArXiv_Daily_Digest*