# Agent 策略优化与在线蒸馏 — 2026-W26 (06/22-06/28)

本周新增 **49** 篇论文，**8** 篇附带代码。优先级：high 24 / medium 16 / low 9。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [ARCO: Adaptive Rubric with Co-Evolution for Multi-Step LLM-Based...](http://arxiv.org/abs/2606.21262v1) | reward learning | ARCO在两个开源骨干模型的所有测试设置下，均提升了最优精确匹配（EM）分数，生成的步级准则... | 通过设计自适应协同进化的步级评分奖励机制，解决步级信用分配问题，优化多步智能体的... | 仅在多跳问答任务验证，未在复杂通用多步智能体任务测试，泛化性待验... | ✅ |
| 2 | high | - | [ReNIO: Reweighting Negative Trajectory Importance for LLM On-Pol...](http://arxiv.org/abs/2606.23104v1) | online distillation | OPD和OPSD中仅训练错误学生生成输出效果优于仅训练正确输出，在数学推理上对7B模型最高取... | 通过对同策略蒸馏中的负推理轨迹进行重要性重加权，优化训练信号质量，提升大语言模型... | 仅在封闭型推理任务验证，未在开放交互类任务测试，方法依赖额外教师... | ✅ |
| 3 | high | - | [What are Key Factors for Updates in RL for LLM Reasoning?](http://arxiv.org/abs/2606.22570v1) | policy optimization | 每轮rollout的梯度步数决定的离策略程度，会改变重要性采样比分布与裁剪行为，影响更新中占... | 通过理论分析明确RLVR更新的核心影响因素，设计自适应裁剪策略优化改进RLVR的... | 仅在3B、7B模型上验证，未测试更大参数模型，方法的泛化性未得到... | ✅ |
| 4 | high | - | [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How...](http://arxiv.org/abs/2606.26027v1) | policy optimization | 多步工具使用RL的灾难性崩溃源于特定控制token概率异常突增，仅破坏输出格式，底层工具能力... | 引入多种监督信号，通过将监督微调与强化学习交错训练，抑制控制token概率异常，... | 未在公开标准工具使用基准上验证结论，所得结论的泛化性仍需进一步验... | ✅ |
| 5 | high | - | [A Formula-Driven Survey and Research Agenda for On-Policy Distil...](http://arxiv.org/abs/2606.22793v1) | survey | 采样同策略蒸馏的稳定性讨论混淆了时序信用分配和词汇概率路由两个独立作用机制。 | 通过公式驱动的分类框架梳理同策略蒸馏中反馈到更新的全流程，厘清混淆的核心机制，提... | 提出的新方法假设尚未经过实证验证，结论缺乏落地数据支撑，可靠性待... | — |
| 6 | high | - | [AsyncOPD: How Stale Can On-Policy Distillation Be?](http://arxiv.org/abs/2606.24143v1) | online distillation | 教师加权前向KL对过时rollout更鲁棒，学生加权反向KL更脆弱，AsyncOPD吞吐量提... | 通过异步解耦rollout生成与模型更新，基于KL鲁棒性设计改进估计器，提升同策... | 未在实际下游任务验证泛化性，仅报告吞吐量与准确率，实际落地效果尚... | — |
| 7 | high | - | [BiPACE: Bisimulation-Guided Policy Optimization with Action Coun...](http://arxiv.org/abs/2606.25556v1) | policy optimization | 在ALFWorld的Qwen2.5-7B上，将验证成功率从GiGPO的90.8提升至97.1... | 通过双模拟引导的隐藏态聚类结合动作条件反事实基线，改进策略优势估计，无需额外判别... | 仅在中小规模文本类智能体基准验证，未测试更大模型与开放域复杂任务... | — |
| 8 | high | - | [CalVerT: Augmenting Agents with Calibrated Verifier Telemetry Im...](http://arxiv.org/abs/2606.21777v1) | policy optimization | 添加校准验证器遥测后，可在智能体过度依赖参数知识时触发检索提升F1，同时减少充足上下文下的冗... | 通过在智能体原有状态中加入校准自置信度和接地验证器得分，增强状态感知，优化动作决... | 仅在问答任务验证，未在其他类型Agent任务测试，泛化能力未验证... | — |
| 9 | high | - | [Curriculum Reinforcement Learning Can Incentivize Reasoning Capa...](http://arxiv.org/abs/2606.22317v1) | policy optimization | 边界感知课程RL可同时提升pass@1与pass@256，pass@256较原生RLVR平均... | 采用边界感知课程强化学习，先定位模型当前推理边界，引入针对性教师引导，再通过RL... | 未公开具体实验使用的推理基准细节，推理边界依赖pass@256代... | — |
| 10 | high | - | [Designing Reward Signals for Portable Query Generation: A Case S...](http://arxiv.org/abs/2606.27291v1) | reward learning | GRPO对虚假奖励信号比RLOO、REINFORCE++更敏感，加规则奖励下界提质量0.14... | 通过鲁棒奖励塑造，引入确定性规则奖励下界，抑制策略优化对奖励缺陷的利用，提升生成... | 依赖人工/大模型设计奖励，跨任务泛化性未验证，工业落地需要针对不... | — |
| 11 | high | - | [EvoRubrics: Dynamic Rubrics as Rewards via Adversarial Co-Evolut...](http://arxiv.org/abs/2606.23038v1) | reward learning | 仅靠策略生成与评分评估的共进化就足以提供丰富学习信号，无外部监督的全自监督变体仍可获得有意义... | 通过策略模型与评分生成器的对抗共进化，动态生成适配的奖励信号，引导策略优化并自动... | 双模型共进化训练算力开销较高，未在具体下游落地任务验证泛化效果 | — |
| 12 | high | - | [GEOALIGN: Geometric Rollout Curation for Robust LLM Reinforcemen...](http://arxiv.org/abs/2606.26917v1) | policy optimization | 批次内少量高奖励轨迹的方向分歧会引发训练失稳，基于方向共识筛选轨迹可稳定训练且几乎无额外开销... | 基于批次方向共识检测修正不一致训练轨迹，以极低额外开销稳定在线大语言模型强化学习... | 仅在两个封闭任务验证，未测试开放复杂场景下方法的通用性和稳定性。 | — |

## 方法族分布

- **policy optimization**：27 篇
- **reward learning**：10 篇
- **online distillation**：3 篇
- **survey**：3 篇
- **knowledge distillation**：2 篇
- **evaluation/benchmark**：2 篇
- **未分类**：1 篇
- **model steering**：1 篇

## 失败模式与风险信号

- 现有方法依赖预定义启发式，仅关注视觉操作，无法处理数值计算问题
- 传统知识蒸馏无法有效传递共情所需的细粒度理解能力
- 标准同策略蒸馏同等对待所有生成样本，未能充分挖掘负样本的训练价值。
- 奖励饱和、奖励黑客
- 长周期任务奖励稀疏延迟，信用分配粗粒度短视，状态值估计方差高
- 后训练阶段知识蒸馏在训练数据充足时，性能优势会发生明显衰减
- 无负例训练的SFT无法学习推理高效回溯，导致推理计算量过高
- 同策略蒸馏稳定性讨论混淆核心机制，方法设计缺乏清晰的理论边界。
- 奖励塌缩、响应过度压缩引发的随机塌缩
- 现有RLVR方法依赖启发式设计，算法选择存在分歧甚至相互矛盾

## 评测信号

- 经分组约束奖励的强化学习训练后，模型平均性能提升6.1个百分点，交错推理准确率提升9.9个百分点，工具调用成功率超95%。
- 该方法取得有竞争力的性能，部分场景下小模型的准确率和语义相关性可匹配甚至超越大尺寸教师模型。
- 在数学推理任务上，Qwen3-1.7B相对提升最高8.90%，R1-Distill-Qwen-7B相对提升最高10.00%。
- 在多个基准上性能一致优于静态和动态评分基线，学习到的奖励模型具备可迁移性，全自监督变体仍有性能增益
- 在三个长周期智能体基准上，G2PO相比GRPO最高提升任务成功率22.2%，整体性能显著优于现有SOTA基线方法。
- 仅明确提出所提方法可稳定提升学生模型性能，未给出具体评测指标与详细量化结果。
- 仅从理论推导得出两种方法的推理计算量指数级差异，未给出实际任务的实证评测结果。
- 相比基础模型提升整体推理准确率，同时将token生成量降低超过60%，验证了方法的稳定性
- ACPO在3B、7B模型的多个推理基准上性能优于DAPO、CISPO两个强基线，验证了分析驱动方法更鲁棒有效。
- 相较SFT基线，树编辑距离最多降23.8%、token级莱文斯坦距最多降38.6%，零样本性能优于主流大模型少样本结果。

## 控制机制 / Harness 信号

- 通过设计分组约束的奖励函数，使用强化学习训练优化MLLM的交错推理与工具调用策略，提升任务表现。
- 通过引入仅训练阶段可用的特权信息，结合多源注意力与双对齐损失，实现大模型共情知识向小模型的迁移。
- 通过对同策略蒸馏中的负推理轨迹进行重要性重加权，优化训练信号质量，提升大语言模型推理能力。
- 通过策略模型与评分生成器的对抗共进化，动态生成适配的奖励信号，引导策略优化并自动构造学习课程
- 通过将线性交互轨迹转化为全局状态转移图，设计分组聚合状态值估计与边中心化优势估计，优化智能体策略。
- 通过知识蒸馏迁移大教师模型知识到小学生模型，提出两阶段蒸馏策略提升低资源场景小模型性能。
- 通过RLVR的结果奖励信号让模型学习推理过程的高效回溯，还可将该能力通过蒸馏迁移到基础大模型。
- 通过公式驱动的分类框架梳理同策略蒸馏中反馈到更新的全流程，厘清混淆的核心机制，提出两类改进假设。
- 通过设计仅针对正确回答的自适应效率奖励，结合动态归一化和控制环调整，稳定GRPO优化过程
- 通过理论分析明确RLVR更新的核心影响因素，设计自适应裁剪策略优化改进RLVR的更新过程。

## 可靠性 / 落地风险

- 未披露训练算力成本，未公开具体所用数据集，跨不同任务的泛化性未得到验证。
- 仅在共情对话单任务验证，方法泛化性未验证，未披露实际工业部署的具体成本。
- 仅在封闭型推理任务验证，未在开放交互类任务测试，方法依赖额外教师模型的概率输出。
- 双模型共进化训练算力开销较高，未在具体下游落地任务验证泛化效果
- 构建全局状态转移图对长轨迹的内存需求较高，长序列场景下的扩展性可能存在不足。
- 未给出详细的量化评测结果，也未验证结论在不同模型族上的泛化性，存在一定不确定性。
- 仅有理论推导无实证验证，结论未在实际真实推理任务中得到验证落地。
- 提出的新方法假设尚未经过实证验证，结论缺乏落地数据支撑，可靠性待验证。
- 仅在数学推理任务验证，未在通用Agent场景测试，方法通用性待验证
- 仅在3B、7B模型上验证，未测试更大参数模型，方法的泛化性未得到充分验证。

## 代码资源

- [ARCO: Adaptive Rubric with Co-Evolution for Multi-Step LLM-Based Agents](https://github.com/zihangtian/ARCO.) · 7 stars
- [Learning at the Right Pace: Adaptive Data Scheduling Improves LLM Reinforcement ...](https://github.com/Richard-zrx/ADS.) · 2 stars
- [CineCap: Structured Reasoning with Spatio-Temporal Anchors for Cinematographic V...](https://github.com/Hectormxy/CineCap.git.) · 2 stars
- [What are Key Factors for Updates in RL for LLM Reasoning?](https://github.com/Control-derek/ACPO) · 1 stars
- [AIR: Adaptive Interleaved Reasoning with Code in MLLMs](https://github.com/CongHan0808/AIR.git.)
- [ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation](https://github.com/BDML-lab/ReNIO.)
- [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Sig...](https://github.com/hypasd-art/Tool-RL-Box.)
- [OPERA: Aligning Open-Ended Reasoning via Objective Perplexity-based Reinforcemen...](https://github.com/pangpang-xuan/OPERA.)

## 常见基线方法

- **GRPO**：6 篇
- **监督微调（SFT）**：2 篇
- **原生RLVR**：2 篇
- **传统知识蒸馏**：1 篇
- **大尺寸教师语言模型**：1 篇
- **标准同策略蒸馏(OPD)**：1 篇
- **同策略自蒸馏(OPSD)**：1 篇
- **静态评分准则基线**：1 篇
- **现有动态评分准则基线**：1 篇
- **prompt-based基线**：1 篇

## 常用数据集

- **摘要未提及**：6 篇
- **WebShop**：3 篇
- **ALFWorld**：3 篇
- **LiveCodeBench**：2 篇
- **推理任务基准**：2 篇
- **摘要未提及具体数据集名称**：1 篇
- **多模态共情对话数据集**：1 篇
- **纯文本共情对话数据集**：1 篇
- **数学推理基准**：1 篇
- **代码生成基准**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*