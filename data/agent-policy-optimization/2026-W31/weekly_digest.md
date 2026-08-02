# Agent 策略优化与在线蒸馏 — 2026-W31 (07/27-08/02)

本周新增 **56** 篇论文，**8** 篇附带代码。优先级：high 30 / medium 18 / low 8。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [CAST: Game Solvers as Turn-Level Teachers for LLM Agents](http://arxiv.org/abs/2607.25308v1) | online distillation | 游戏求解器的状态值变化可转化为廉价准确的步级信用信号，仅用标量值即可实现有效策略蒸馏，性能全... | 通过引入游戏求解器生成的步级优势信号作为奖励，以蒸馏方式优化大语言模型智能体的决... | 方法依赖现成的游戏求解器，仅适用于有成熟求解器的任务，通用性受限 | ✅ |
| 2 | high | - | [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable ...](http://arxiv.org/abs/2607.23802v1) | reward learning | 基于任务变换的RLSVR在非可验证开放式任务上优于现有自提升方法，在可验证推理任务上也能获得... | 通过任务变换构造可自动生成完全自可验证奖励的代理环境，以奖励信号引导大语言模型自... | 方法依赖定制化任务变换设计，通用性有待验证，多智能体自博弈训练的... | ✅ |
| 3 | high | - | [LEEPS: Latent-Guided Explore-Exploit Prompt Sampling for Efficie...](http://arxiv.org/abs/2607.28077v1) | policy optimization | LEEPS在1.5B和7B规模Qwen2.5-Math上相对最强基线分别提升2.6%和3.7... | 通过自适应平衡探索与利用的提示采样，减少无效生成预算浪费，提升大语言模型RLVR... | 目前仅在静态推理任务验证，未在复杂交互式场景测试，跨场景泛化性有... | ✅ |
| 4 | high | - | [Offline-Online Curriculum RL for Multimodal Reasoning](http://arxiv.org/abs/2607.23700v1) | policy optimization | 结合离线步骤重要性估计与在线渐进强化学习，可有效区分关键推理步骤，兼顾性能与运行效率。 | 通过离线蒸馏筛选关键推理步骤，在线采用渐进式步骤级强化学习，引导模型聚焦关键步骤... | 摘要未披露方法在异构复杂推理任务的泛化效果，也未公开具体的性能提... | ✅ |
| 5 | high | - | [ReDiPPO: Reference-Guided Value Calibration and Discrepancy-Awar...](http://arxiv.org/abs/2607.27631v1) | policy optimization | 引入参考答案作为训练特权信号结合差异重加权，可有效提升PPO值估计精度，推理性能稳定优于多个... | 通过参考引导的值校准、差异感知的Token级优势重加权，改进PPO策略更新，提升... | 依赖训练阶段的参考答案作为特权信号，方法泛化性未在更多类型任务中... | ✅ |
| 6 | high | - | [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-...](http://arxiv.org/abs/2607.22529v1) | policy optimization | 协同进化技能的自博弈框架可兼顾验证可靠性与任务多样性，既能提升骨干模型性能，也能改善初始错配... | 通过强化学习自博弈循环，收集执行反馈动态更新扩展技能库，以分模块协同进化平衡验证... | 持续自进化扩展技能库会带来较高训练成本，技能动态路由的稳定性未得... | ✅ |
| 7 | high | - | [Weak-to-Strong On-Policy Distillation](http://arxiv.org/abs/2607.26246v1) | online distillation | 不同对比产生不同增强信号，所有监督源都弱于学生时，该方法仍可持续提升强学生性能 | 通过多个弱模型的正负对比提取能力方向构造代理教师，基于同策略蒸馏改进强学生模型性... | 仅在数学和代码任务验证，通用性未在更多通用场景测试，落地有待进一... | ✅ |
| 8 | high | - | [A Control System, a Dataset, and a Recipe for Making Frozen LLM ...](http://arxiv.org/abs/2607.25415v1) | agent harness | 约束harness为固定动作空间的在线强化学习优化，可在黑盒设置下实现可审计的领域适配，效果... | 将harness限定为固定小规模人类可读动作空间，以多目标奖励引导强化学习，在线... | 仅在三类中小型任务上验证，未测试大规模复杂工业场景，实际落地效果... | — |
| 9 | high | - | [AgentOmnia: Scaling Agentic Models for Full-Scenario Application...](http://arxiv.org/abs/2607.23124v1) | policy optimization | 基于Qwen3-30B优化后，AgentOmnia将OmniaBench难子集通过率从9.1... | 通过程序、求解器与验证器提供正确性信号，结合多方法后训练，基于PRD反馈引导智能... | 框架整体复杂度较高，PRD引导自进化仅小规模验证，大规模工业落地... | — |
| 10 | high | - | [Beyond Direct Answering: Aligning Educational LLMs as Socratic G...](http://arxiv.org/abs/2607.22996v1) | policy optimization | 显式关键词泄漏惩罚会与梯度行为对齐冲突，去掉惩罚后SE从30%升至63.3%，纯模型规模无法... | 设计涵盖认知深度、参与度、直接性的多维度启发式奖励，通过GRPO强化学习对齐优化... | 测试样本量仅30个，样本规模小，所得结论的泛化性有待进一步验证 | — |
| 11 | high | - | [Contrastive Reinforced Policy Optimization via Privileged Self-D...](http://arxiv.org/abs/2607.28026v1) | policy optimization, onl... | 引入分组对比可有效缓解OPSD的曝光偏差，在13个基准上稳定优于现有基线，提升长交互性能。 | 通过对比学习结合特权自蒸馏，利用预测熵区分正负优化位置，保留细粒度可靠优化信号改... | 仅在封闭标准基准测试，未在开放真实场景验证，预测熵分区的可靠性未... | — |
| 12 | high | - | [DHRCL:Training Code LLMs with Dense Hierarchical Rewards and Cur...](http://arxiv.org/abs/2607.26457v1) | reward learning | 在KodCode基准上，DHRCL在不同容量Qwen3模型上性能均优于各类基线，优势随模型容... | 通过设计分层递进的密集奖励结构与自动课程，结合阶段感知token信用分配，改进代... | 仅在Qwen系列模型和KodCode单基准上验证，方法的跨场景通... | — |

## A 会 / Venue 标签

- **ICLR 2026**：1 篇
- **ICML 2026**：1 篇

## 方法族分布

- **policy optimization**：32 篇
- **reward learning**：7 篇
- **online distillation**：6 篇
- **evaluation/benchmark**：2 篇
- **policy optimization, agent harness**：1 篇
- **other**：1 篇
- **knowledge distillation**：1 篇
- **multi-agent coordination**：1 篇
- **agent harness**：1 篇
- **policy optimization, online distillation**：1 篇
- **model steering**：1 篇
- **skill generation**：1 篇

## 失败模式与风险信号

- 原生基于KL的同策略蒸馏存在时间监督不匹配问题
- 现有LLM政策响应模拟未考虑行为摩擦，模拟准确度不足
- 大模型预测关系三元组违反关系约束，输出不一致、结果矛盾
- 学生策略蒸馏后易出现风格漂移与冗余退化，难以从专有教师迁移核心推理能力
- 长期记忆任务中检索记忆冗余冲突，上下文开销过大
- 训练-推理差异导致强化学习训练不稳定
- 训练部署不匹配，单控制器训练无法适配实际部署中多样的推理工作流
- 大语言模型社会认知能力不足，难以满足人类环境长期服务的交互需求
- 多模态推理依赖虚假捷径，中间步骤出错，降低推理可解释性与可靠性
- 固定采样参数无法适配不同提示与不同生成阶段的生成需求，导致生成质量偏低。

## 评测信号

- FlowCTS-OPD在所有目标指标上优于基线，核心指标提升明显：GenEval 0.90→0.93，OCR 0.90→0.92，PickScore 22.75→23.06
- 对比不同大语言模型在不同设置下的模拟性能，验证PTC人格设计对性能的稳定提升作用。
- 两条路径性能均优于基线，7-8B开源模型以远低于闭源模型的推理成本大幅缩小性能差距。
- 在七个QA基准上性能优于对比方法，Qwen3-1.7B成功率39.4%，Qwen3-4B成功率达44.4%
- 在两个测试基准上，MemChain对闭源、开源模型均能提升性能，同时大幅压缩输入记忆上下文规模
- 验证了FP8推理下ACRL稳定训练的效果，其准确率匹配BF16基线，性能优于重要性采样修正方案。
- SpyRL在非可验证开放式任务上性能优于现有自提升方法，在可验证推理任务上可获得一致的性能增益。
- 评测模型对未见控制器组合和控制器迁移的泛化能力，验证所提方法优于传统单控制器优化方法
- 现有大模型社会智能仍有较大提升空间，所提全harness架构可提升绝大多数模型基准对的表现，最优性能接近顶级闭源模型。
- 所提方法在多模态推理基准上取得当前最优性能，同时训练与推理的效率均优于现有方法。

## 控制机制 / Harness 信号

- 基于同策略蒸馏框架，匹配学生与参考轨迹推导时间加权速度匹配目标，优化流模型生成性能
- 通过引入感知交易成本的人格设计规范Agent行为，使用GRPO策略优化优化开源模型的模拟效果。
- 对黑盒大模型采用约束感知提示与验证自反思优化，对小模型通过知识蒸馏加复合奖励对齐注入一致性知识。
- 以多智能体生成的结构化协议为蒸馏中间表示，结合稠密蒸馏信号与稀疏RL目标优化学生智能体
- 通过强化学习优化记忆组织策略，将检索记忆整理为结构化紧凑证据上下文，降低回答模型处理负担
- 通过自适应控制将大语言模型强化学习的训练-推理差异维持在合理区间，稳定训练过程，同时提升策略探索能力。
- 通过任务变换构造可自动生成完全自可验证奖励的代理环境，以奖励信号引导大语言模型自提升优化。
- 将推理控制器显式纳入后训练循环，通过多任务强化学习与回合级GRPO实现模块化训练，适配多样控制器
- 结合在线策略蒸馏、基于规则的强化学习优化模型参数，通过harness架构在推理时路由多类支持调控行为。
- 通过离线蒸馏筛选关键推理步骤，在线采用渐进式步骤级强化学习，引导模型聚焦关键步骤提升推理质量。

## 可靠性 / 落地风险

- 仅在少量生成任务验证，扩展到大模型或Agent场景的效果未验证，增加监督步骤提升优化难度
- 研究样本仅来自荷兰，未在其他地区、其他政策场景验证，泛化性不明确。
- 仅在单一DocRE数据集验证，方法在其他任务上的泛化能力尚未得到验证。
- 依赖离线多智能体生成协议，流程复杂度较高，未验证更大规模模型的泛化效果
- 新增额外的记忆处理模块与训练流程，整体训练复杂度和成本高于原始范式
- 未在大规模下游任务验证通用性，方法的适用范围缺乏充分的实验验证。
- 方法依赖定制化任务变换设计，通用性有待验证，多智能体自博弈训练的整体成本较高。
- 未在具体下游任务和真实部署场景验证，实际落地的效果和稳定性尚不明确
- 社会智能评测依赖专家标注，方法落地的通用性和鲁棒性尚未经过大规模场景验证
- 摘要未披露方法在异构复杂推理任务的泛化效果，也未公开具体的性能提升量化数值。

## 代码资源

- [Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills](https://github.com/Qwen-Applications/skill-self-play.) · 49 stars
- [CAST: Game Solvers as Turn-Level Teachers for LLM Agents](https://github.com/Wloner0809/CAST.) · 6 stars
- [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open...](https://github.com/wangqinsi1/SpyRL.) · 2 stars
- [Weak-to-Strong On-Policy Distillation](https://github.com/Yu-Fangxu/W2S-OPD.) · 2 stars
- [Offline-Online Curriculum RL for Multimodal Reasoning](https://github.com/kk0013/CritiCuRL.)
- [LEEPS: Latent-Guided Explore-Exploit Prompt Sampling for Efficient RLVR in Large...](https://github.com/ShuangLiangX/LEEPS.)
- [RefineSVG: Visual Feedback-Driven Reinforcement Learning for Image-to-SVG Genera...](https://github.com/liuxiaobo66/RefineSVG.)
- [ReDiPPO: Reference-Guided Value Calibration and Discrepancy-Aware Token Reweight...](https://github.com/cii030/ReDiPPO.)

## 常见基线方法

- **GRPO**：5 篇
- **监督微调(SFT)**：2 篇
- **监督微调（SFT）**：2 篇
- **现有SOTA安全重对齐防御基线**：2 篇
- **PPO**：2 篇
- **DAPO**：2 篇
- **原生基于KL的同策略蒸馏**：1 篇
- **混合奖励强化学习基线**：1 篇
- **原生监督微调SFT**：1 篇
- **仅提示词方案**：1 篇

## 常用数据集

- **数学推理基准**：3 篇
- **ALFWorld**：3 篇
- **WebShop**：3 篇
- **摘要未提及**：2 篇
- **数学推理任务**：2 篇
- **推理基准**：2 篇
- **GenEval**：1 篇
- **OCR**：1 篇
- **荷兰公民节能改造调研问答数据集**：1 篇
- **DocRED**：1 篇

---
*自动生成于 2026-08-02 | ArXiv_Daily_Digest*