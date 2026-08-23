# Agent 策略优化与在线蒸馏 — 2026-W34 (08/17-08/23)

本周新增 **38** 篇论文，**2** 篇附带代码。优先级：high 19 / medium 14 / low 5。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Mul...](http://arxiv.org/abs/2608.17253v1) | multi-agent coordination | 增加群体多样性可减少自反馈循环的相关错误，在7个文本基准提升3.0-8.6%，4个多模态基准... | 通过同伴生成奖励替代自生成奖励，依靠多智能体群体多样性降低错误相关性，缓解训练崩... | 需要同时优化多个独立模型，计算资源开销较大，工业落地部署的成本偏... | ✅ |
| 2 | high | - | [Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal ...](http://arxiv.org/abs/2608.17310v1) | policy optimization | 在WebArena-Lite上，Qwen-3.5-27B全参数优化较No Skill基线提升... | 基于进化策略采样参数扰动，利用奖励信号进行在线奖励加权更新，搭配余弦衰减扰动规模... | 仅在有限测试场景验证，方法在更多复杂长视野任务上的泛化性未得到充... | — |
| 3 | high | - | [Ask to Be Sure: Informative Interactions for Confident Multi-Tur...](http://arxiv.org/abs/2608.15949v1) | reward learning | 无需真实推荐标签，以交互带来的熵减为奖励微调，即可同时提升多轮推荐的质量与对话效率。 | 通过计算交互带来的推荐熵减构造奖励信号，引导大语言模型微调，生成更具信息性的交互... | 仅在两个公开数据集验证，未测试开放真实推荐场景，泛化能力有待进一... | — |
| 4 | high | - | [Debate Training Reduces Reward Hacking in RLAIF](http://arxiv.org/abs/2608.17776v1) | reward learning | 辩论训练可在训练全程维持裁判性能，恢复45%的验证准确率性能差距，增加辩论轮次可抵消弱裁判带... | 采用双人对抗辩论机制，通过设置评论者词数限制平衡博弈，抑制奖励黑客行为，提升RL... | 依赖多智能体对抗训练，平衡博弈难度大，训练成本较高，性能稳定性受... | — |
| 5 | high | - | [Efficient RLVR Scheduling via Graph-Structured Online Difficulty...](http://arxiv.org/abs/2608.17941v1) | policy optimization | 通过图共享相关样本的rollout反馈，可在无额外探测开销下缓解难度估计冷启动和反馈过时问题... | 通过在线估计样本难度实现自适应探索预算分配，优化RLVR训练过程，提升大模型推理... | 图构建和在线变分更新会引入额外计算开销，复杂度随样本量增加而上升... | — |
| 6 | high | - | [EnvHarness: Awakening Static Worlds for Agent Learning](http://arxiv.org/abs/2608.19880v1) | agent harness | EnvHarness在留存测试实例上最高取得9.0个点性能提升，同时减少9.8%的执行步骤，... | 通过EnvHarness可编程层改造静态环境，EnvRigger生成针对策略缺陷... | 未验证大规模场景下改造的稳定性，自动生成改造组件的泛化能力未得到... | — |
| 7 | high | - | [GUPO: Gradient Uncertainty-aware Policy Optimization for Post-Tr...](http://arxiv.org/abs/2608.17411v1) | policy optimization | 同一小批量内不同查询生成的组梯度常存在方向冲突，该冲突会显著降低策略更新的有效性。 | 通过引入梯度不确定性校准梯度聚合过程，改进大语言模型后训练阶段的策略更新效果。 | 未披露具体评测基准，方法有效性未在公开知名基准上得到充分验证。 | — |
| 8 | high | - | [LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents](http://arxiv.org/abs/2608.17393v1) | policy optimization | LEGO-RL可将Qwen3.5-35B-A3B的SWE-bench解决率提升5.4~9.4... | 依托原生智能体harness，通过进程内LLM代理、沙箱防御和可观测训练稳定训练... | 仅在编码智能体场景验证，跨任务通用性未验证，大规模沙箱编排存在一... | — |
| 9 | high | - | [LLM-Based Hierarchical Coordinated Control with Continuation-Awa...](http://arxiv.org/abs/2608.15041v1) | policy optimization | 加入对协调决策后系统长期演化的评估后，所提方法在两个任务上性能持续优于所有对比基线。 | 通过延续感知GRPO优化协调策略，不仅评估决策的即时结果，还兼顾决策后的系统长期... | 仅验证常规工况，未提及极端场景下的协调稳定性，工业落地存在潜在不... | — |
| 10 | high | - | [Le Critique: Privileged Value Functions for LLM Reinforcement Le...](http://arxiv.org/abs/2608.16739v1) | policy optimization | 结合特权价值函数与TETHER的方案，在多个推理任务上稳定优于标准价值基线，性能比肩甚至超过... | 通过提出特权价值函数注入token级任务信号，结合自适应插值基线改进强化学习训练... | 仅在推理任务验证，未涉及复杂真实agent任务，方法工程落地的可... | — |
| 11 | high | - | [MLREF: Efficient Module Reuse for Reward Design in Reinforcement...](http://arxiv.org/abs/2608.18827v1) | reward learning | 基于模块池复用的奖励设计，相较整体式生成方法在运动任务提效25.2%，操纵任务提效6.6%，... | 通过构建可演化的奖励模块池，结合反射优化、信用分配与回滚合并策略优化奖励设计，提... | 未验证模块池规模扩大后的运行效率，也未在开放复杂场景验证方法可靠... | — |
| 12 | high | - | [MidTool: Mid-training Data Synthesis for Agentic Tool Use](http://arxiv.org/abs/2608.20314v1) | tool-use control | 针对通用工具使用的专门训练中期，无论后续采用SFT还是RL后训练，都能在多个基准上稳定提升性... | 通过构建注入工具使用监督的合成训练中期数据，在预训练后后训练前塑造模型工具使用能... | 合成监督可能存在噪声，大规模训练语料的构建与模型训练需要较高的计... | — |

## 方法族分布

- **policy optimization**：15 篇
- **reward learning**：8 篇
- **agent harness**：3 篇
- **evaluation/benchmark**：2 篇
- **unlearning/safety**：2 篇
- **other**：2 篇
- **model steering**：2 篇
- **agent harness, online distillation**：1 篇
- **知识蒸馏**：1 篇
- **multi-agent coordination**：1 篇
- **tool-use control**：1 篇

## 失败模式与风险信号

- 无约束的单查询独立评分易遗漏关键要求、样本间波动大，难以诊断修复模型的持久能力缺陷。
- 运行时行为漂移，偏离原始任务对外部系统造成不可逆副作用
- 小众多对多代码翻译生成结果不可执行
- 单轮结果奖励与多轮反馈修复场景不匹配，丢失中间轮次的细粒度执行信号
- 训练阻塞导致吞吐量低、离策略性高，仅能提供粗糙的序列级信用分配
- 语义先验与奖励结构错配时，模型过度 exploitation导致决策性能严重退化。
- 现有模型可正确预测整体有害性，但普遍误识别攻击目标与对应支撑证据
- 强化学习早期成功轨迹稀缺，稀疏终端回报下细粒度信用分配失效
- 跨语言性能差异，微调引发的灾难性遗忘
- 现有多轮推荐交互未衡量信息获取量，难以有效挖掘用户真实偏好

## 评测信号

- 跨三个模型世代，该方法在两个任务上相对对应基模型均取得一致性能提升，最高提升分别达15.86与8.04点。
- 验证了小模型输出符合规定输出模式，语义内容恰当，可利用漂移相关信息给出正确的漂移恢复决策。
- 4B模型在HumanEval-X++全语言平均性能提升13%，中端语言提升达21%，稳定优于未训练基线。
- TaPR提升了多轮代码生成的三轮成功率，在7B/8B高潜力模型切片上提升达3.31个百分点，稠密奖励硬子集峰值更高
- 在多个推理任务上对比验证，结果显示所提方法优于标准价值函数基线，性能比肩或超过当前常用的GRPO方法。
- 观测语义标签与奖励结构对齐/错配时模型的探索倾向与性能变化，对比不同奖励下的探索触发差异。
- 所提方法在Qwen3-VL-8B主干上，将JRA从17.58%提升至52.51%，同时提升了有害性分类准确率
- 模型提升了未见细胞上下文的响应推断能力，保留通用语言能力，可零额外后训练迁移多任务，得到有竞争力的生物表示。
- TRCA在多个长视野任务基准上一致优于基线，在不同尺寸Qwen模型上均取得显著的任务得分提升
- 评测关注模型跨语言推理性能与微调引发的灾难性遗忘，给出了不同设置下明确的性能提升幅度。

## 控制机制 / Harness 信号

- 基于专家构建的评分标准获取细粒度诊断与优化信号，在强化学习过程中触发针对性监督微调，优化模型输出。
- 在主智能体外部添加即插即用的图结构恢复模块，通过结合混合奖励的强化学习训练小模型实现漂移诊断与行为恢复。
- 通过执行验证生成偏好信号，训练奖励模型提供优化信号，使用GRPO算法优化模型翻译行为。
- 通过设计逐轮稠密的测试通过率奖励，改进多轮代码智能体的奖励信号，优化策略提升自修复能力
- 通过提出特权价值函数注入token级任务信号，结合自适应插值基线改进强化学习训练，优化大语言模型策略。
- 通过构建语义老虎机测试框架，分析预训练语义先验对大语言模型智能体探索行为的偏差影响。
- 通过锚定校准解耦优化，结合实体监督微调与条件策略优化，约束优化范围提升模型细粒度有害目标识别能力
- 基于细胞扰动实验数据构建可计算奖励信号，通过强化学习调优预训练大模型，激发其生物推理能力。
- 基于动作转移设计三类评分规则生成细粒度步级奖励信号，改进长视野智能体的信用分配，辅助策略优化
- 通过探测模型多语言能力弱点，生成针对性硬度优化的合成训练数据，微调改进模型跨语言性能。

## 可靠性 / 落地风险

- 依赖领域专家构建标准框架，专家成本较高，仅在两个领域验证，通用性未得到充分验证。
- 仅在单个公开基准验证，未覆盖更多真实复杂场景，泛化能力有待进一步验证。
- 依赖执行验证获取标注，小众语言执行环境搭建成本高，大规模扩展存在难度。
- 仅在公开代码生成基准测试验证，未测试真实开发场景效果，通用性有待进一步验证
- 仅在推理任务验证，未涉及复杂真实agent任务，方法工程落地的可行性尚未得到验证。
- 大语言模型决策智能体存在预训练带来的固有语义偏差，错配场景下鲁棒性与可靠性不足。
- 仅在整合后的现有数据集上验证，对未见新型有害模因的泛化能力未验证
- 依赖实验测量的细胞扰动数据，数据获取成本较高，方法可扩展性受限于实验数据规模。
- 依赖手工设计的评分规则，泛化到新任务需要重新设计规则，存在额外适配成本
- 未公开具体评测基准细节，合成数据生成依赖预训练模型，落地成本存在不确定性。

## 代码资源

- [Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL](https://github.com/DrStranded/Co-RL.) · 1 stars
- [HarmTrace: Anchor-Calibrated Decoupled Optimization for Fine-Grained Target Iden...](https://github.com/llly1234/HarmTrace-for-Harmful-Memes.)

## 常见基线方法

- **GRPO**：3 篇
- **摘要未提及具体基线**：2 篇
- **对应基模型**：1 篇
- **现有后训练方法**：1 篇
- **单查询独立评分方法**：1 篇
- **未训练基线基座模型**：1 篇
- **outcome-only GRPO**：1 篇
- **标准价值函数基线**：1 篇
- **均值基线GRPO**：1 篇
- **原生多模态大语言模型主干**：1 篇

## 常用数据集

- **ALFWorld**：3 篇
- **WebShop**：3 篇
- **数学推理数据集**：1 篇
- **医学问答数据集**：1 篇
- **AppWorld**：1 篇
- **HumanEval-X++**：1 篇
- **HumanEval-X**：1 篇
- **LiveCodeBench**：1 篇
- **多个推理任务**：1 篇
- **Meme3W**：1 篇

---
*自动生成于 2026-08-23 | ArXiv_Daily_Digest*