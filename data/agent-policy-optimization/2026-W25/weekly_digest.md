# Agent 策略优化与在线蒸馏 — 2026-W25 (06/15-06/21)

本周新增 **64** 篇论文，**9** 篇附带代码。优先级：high 32 / medium 26 / low 6。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Connect the Dots: Training LLMs for Long-Lifecycle Agents with C...](http://arxiv.org/abs/2606.20002v1) | policy optimization | 端到端强化学习在该设置下训练有效，所得元能力可泛化至训练域外、跨领域以及闭环Agent设置。 | 通过端到端强化学习框架训练，搭配定制化任务环境激励，让Agent自主学习更新环境... | 仅完成概念验证，评测基于自建定制环境，方法在真实长生命周期场景的... | ✅ |
| 2 | high | - | [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic re...](http://arxiv.org/abs/2606.16771v1) | policy optimization | 屏蔽存在严重奖励分歧的采样可保留有效强化学习优势信号，在多场景下性能显著优于现有对比方法 | 通过冲突感知过滤机制屏蔽存在严重奖励分歧的训练样本，结合查询级动态重加权调整更新... | 仅在有限的多奖励场景验证，未测试大规模复杂Agent任务下方法的... | ✅ |
| 3 | high | - | [REVES: REvision and VErification--Augmented Training for Test-Ti...](http://arxiv.org/abs/2606.18910v1) | policy optimization | 利用成功轨迹中的近错答案做修正验证训练，在LiveCodeBench比RL基线提6.5个点，... | 将成功轨迹中的中间近错样本转换为修正与验证提示，交替在线增强和策略优化改进模型推... | 依赖显式验证反馈（测试用例、真值、约束），无显式反馈的场景效果可... | ✅ |
| 4 | high | - | [Reward Hacking in Language Model Agents: Revisiting AI Safety Gr...](http://arxiv.org/abs/2606.15385v1) | evaluation/benchmark | 1.5B到14B不同规模的语言模型智能体零样本就会出现奖励黑客，直接奖励优化反而扩大观测奖励... | 构建可控评测套件研究语言智能体奖励黑客现象，未提出新的模型行为控制改进方法。 | 基于代理奖励优化的语言智能体天然存在奖励黑客风险，标准方法无法缓... | ✅ |
| 5 | high | - | [STARE: Surprisal-Guided Token-Level Advantage Reweighting for Po...](http://arxiv.org/abs/2606.19236v1) | policy optimization | GRPO中token级熵变化可分解为轨迹级优势和熵敏感函数的乘积，存在优势-意外度四象限结构... | 通过意外度引导的token级优势重加权，结合目标熵闭环调控，稳定RL后训练的策略... | 目前仅在闭卷推理和多轮工具任务验证，未在开放域复杂agent任务... | ✅ |
| 6 | high | - | [VeriGraph: Towards Verifiable Data-Analytic Agents](http://arxiv.org/abs/2606.16603v1) | policy optimization | 显式构建异质证据DAG可有效提升智能体输出可验证性，VeriGraph-8B取得87.61%... | 通过构建显式异质证据DAG，采用监督多目标的复合奖励进行图策略优化，规范智能体推... | 仅在有限基准测试验证，未验证大规模真实场景适用性，方法的工程可扩... | ✅ |
| 7 | high | - | [A First-Principles Derivation of LLM Policy Optimization: From E...](http://arxiv.org/abs/2606.16733v1) | survey | 仅修改轨迹侧或仅修改奖励侧的方法无法解决复合失效，需要对轨迹侧和奖励侧进行联合设计。 | 通过构建以轨迹侧、奖励侧为双轴的统一分析框架，梳理现有策略优化方法，定位现有方法... | 本文为纯分析综述，提出的框架与结论未经过实证验证，有待进一步实验... | — |
| 8 | high | - | [Beyond Entropy: Learning from Token-Level Distributional Deviati...](http://arxiv.org/abs/2606.19771v1) | policy optimization | 仅更新模型Top 10%的独特Token，就能在七个基准上相比基线平均提升pass@4 4.... | 通过JS散度筛选关键Token做选择性更新，同时调节香农熵和二阶Rényi熵，稳... | 仅在7B及以下开源模型验证，未测试更大规模模型，泛化性待验证 | — |
| 9 | high | - | [Beyond Reward Engineering: A Data Recipe for Long-Context Reinfo...](http://arxiv.org/abs/2606.18831v1) | policy optimization | 该数据方案搭配GRPO，可让微调后的Agent在GAIA提升4.8个点、BrowseComp... | 通过构建适配长上下文的训练数据，搭配GRPO强化学习优化Agent的长上下文推理... | 仅在有限模型和封闭基准验证，未验证开放场景下的泛化可靠性。 | — |
| 10 | high | - | [CORA: Analyzing and bridging thinking-answer gap in Multimodal R...](http://arxiv.org/abs/2606.14691v1) | reward learning | 在大视觉语言模型的多模态RLVR中，思考-答案语义不一致问题在整个训练流程和推理阶段都始终存... | 通过引入额外的思考-答案一致性奖励，结合混合奖励优势拆分，对齐推理与答案的语义一... | 摘要未披露具体实验数值与更多细节，未验证不同规模模型上的通用性，... | — |
| 11 | high | - | [CacheRL:Multi-Turn Tool-Calling Agents via Cached Rollouts and H...](http://arxiv.org/abs/2606.14179v1) | reward learning | 移除大模型知识迁移性能降41%，缓存感知奖励提17%，强SFT基础上强化学习额外增益十分有限 | 通过缓存轨迹降低训练成本，设计缓存感知动态奖励，结合监督微调与GRPO优化智能体... | 缓存轨迹保真度依赖大模型生成，存在偏差，实际在线部署效果未在摘要... | — |
| 12 | high | - | [Closing the Feedback Loop: From Experience Extraction to Insight...](http://arxiv.org/abs/2606.17591v1) | policy optimization | 相同积累经验下，无洞见治理回路会让性能低于零样本基线，有回路则大幅提升预测准确率和风险调整收... | 构建规则-证据-技能三层架构，通过反馈驱动的精选回路治理洞见，无需参数更新即可调... | 仅在金融预测单一场景验证，方法在通用智能体任务中的泛化性尚未得到... | — |

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
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*