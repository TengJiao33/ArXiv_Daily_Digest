# Agent 策略优化与在线蒸馏 — 2026-W30 (07/20-07/26)

本周新增 **46** 篇论文，**2** 篇附带代码。优先级：high 17 / medium 21 / low 8。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Distilled Reinforcement Learning for LLM Post-training](http://arxiv.org/abs/2607.17247v1) | online distillation | Distilled RL可有效从教师向学生迁移原本无法获得的知识，跨家族蒸馏下也能显著提升p... | 通过将教师监督整合到强化学习目标，结合三个核心组件实现选择性知识迁移，避免无条件... | 未披露具体评测数据集，可复现性仅依赖开源代码，存在一定可复现风险... | ✅ |
| 2 | high | - | [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing an...](http://arxiv.org/abs/2607.17038v1) | reward learning | 引入奖励驱动批评模块后，任务成功率相比标准ReAct框架获得24.5%的绝对提升，同时可有效... | 通过内置自校正奖励模型评估决策轨迹，结合POMDP路由与强化学习动态调整推理路径... | 仅在两个特定基准上验证效果，未测试更复杂通用场景，泛化能力尚不明... | ✅ |
| 3 | high | - | [Co-Evolving LLM Evaluators and Policies via DynamicRubric](http://arxiv.org/abs/2607.20083v1) | policy optimization | 策略优化中转移概率质量的方向增益正好等于两响应间的评测器分数差，评测器应随监督的策略共同进化... | 通过让评测器与待优化策略共进化，生成动态加权评分规则，为策略优化提供更强的监督信... | 针对每个候选响应集动态生成评分规则，相比静态方案会产生额外的计算... | — |
| 4 | high | - | [DSWorld: A Data Science World Model for Efficient Autonomous Age...](http://arxiv.org/abs/2607.15901v1) | policy optimization | DSWorld将RL智能体训练加速约14倍、搜索推理加速3-6倍，转移预测性能超出最强LLM... | 通过学习世界模型预判操作效果，结合成本感知路由，用误差感知强化学习优化预测，加速... | 仅在自建数据集验证，方法泛化性未在真实大规模数据科学任务中验证。 | — |
| 5 | high | - | [Enhancing Rubric-based RL via Self-Distillation](http://arxiv.org/abs/2607.18082v2) | policy optimization | 训练过程中超过57%的样本存在被抑制准则问题，平均每个样本有1.8个满足条件却丢失学习信号的... | 通过自蒸馏为未探索准则注入优化信号，翻转被抑制准则的token级优势，改进基于评... | 仅在两类小规模学术基准验证，未在大规模真实场景测试，泛化性未得到... | — |
| 6 | high | - | [Fishing Out Free Riders: Shapley-Based Reward Attribution for Pa...](http://arxiv.org/abs/2607.18979v1) | reward learning | 细粒度路径级Shapley奖励归因能有效识别“搭便车”的冗余有害路径，让训练更稳定，推理性能... | 通过基于Shapley值的细粒度路径级奖励分配，替代原有结果级统一奖励，优化大模... | 基于蒙特卡洛采样近似计算Shapley值，计算开销随路径数量增长... | — |
| 7 | high | - | [H$^2$SD: Hybrid Hindsight Self-Distillation](http://arxiv.org/abs/2607.18955v1) | online distillation | 按轨迹正确性差异化使用教师信号，可在保持优化稳定与生成效率的同时稳定优于现有主流基线 | 通过混合后见自蒸馏，根据轨迹正确性差异化使用教师信号，优化推理监督，提升大模型推... | 未披露具体评测基准细节，方法面向通用推理，落地特定agent场景... | — |
| 8 | high | - | [LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks](http://arxiv.org/abs/2607.18110v1) | online distillation | 基于细粒度经验知识的监督相比标量奖励，能更好提升开放式任务分布外泛化，同时有效缓解奖励破解。 | 利用LLM教练输出的细粒度经验知识做上下文蒸馏，为策略后训练提供稠密监督，缓解奖... | 依赖大模型教练提供反馈，教练评估偏差会传递给策略，未披露具体基准... | — |
| 9 | high | - | [Multi-turn RL with Structural and Performance Aware Rewards for ...](http://arxiv.org/abs/2607.20908v1) | reward learning | 该方法对比Qwen-3-32B和CUDA Agent，分别获得最高5倍、3.32倍加速提升，... | 通过融合可验证执行奖励与程序结构感知奖励的统一信号，引导强化学习优化CUDA代码... | 方法仅适配CUDA代码生成任务，跨场景泛化性未验证，落地场景范围... | — |
| 10 | high | - | [Off-Context GRPO: Learning to Reason on Hard Problems using Priv...](http://arxiv.org/abs/2607.19313v1) | policy optimization | 加入重要性修正的OC-GRPO在数学推理基准上，相较原生GRPO平均获得3.9%绝对提升、1... | 通过引入带特权信息的引导推演，结合重要性修正的优化目标，调整模型更新方向，提升大... | 仅在数学推理基准验证，方法通用性尚未在更多类型任务中得到验证。 | — |
| 11 | high | - | [PATS: Policy-Aware Training Scaffolding for Agentic Reinforcemen...](http://arxiv.org/abs/2607.21419v1) | policy optimization | PATS在ALFWorld和WebShop上比强基线最高提升18.6%，在七个搜索QA基准上... | 通过动态策略感知训练支架为弱策略提供任务引导，随策略提升缩减引导，结合RLVR与... | 仅在给定基准上验证，未测试更复杂长程任务的泛化性，未披露工业落地... | — |
| 12 | high | - | [Process Reward Informed Tree Rollout for Effective Multi-Turn RL](http://arxiv.org/abs/2607.15610v1) | policy optimization | 相同训练预算下，该方法在SWE-Bench性能提升最高+5.0个百分点，FrozenLake... | 通过过程奖励引导树状轨迹展开，选择性分配采样预算、裁剪无效退化路径，提升策略优化... | 方法效果依赖过程反馈评分器的质量，额外的树管理步骤会增加一定计算... | — |

## 方法族分布

- **policy optimization**：20 篇
- **reward learning**：12 篇
- **online distillation**：8 篇
- **other**：2 篇
- **evaluation/benchmark**：1 篇
- **multi-agent coordination**：1 篇
- **unlearning/safety**：1 篇
- **model steering**：1 篇

## 失败模式与风险信号

- 现有自主数据科学智能体依赖试错工作流，计算开销过大，训练推理速度慢
- 低精度NVFP4用于MoE强化学习引发训练崩溃、性能退化
- 现有方法无法平衡token预算与多事件捕捉，缺乏自校正机制，建模不可靠
- 现有文生图文化真实性评估存在文化偏差，基于VQA的评估推理速度慢、扩展性不足
- 原有均匀轨迹展开浪费计算预算于无效死端路径，优质中间状态探索不足。
- RLVR处理难题时产生零学习信号，特权引导训练存在目标失配问题
- 扩散drafter存在域级、词元级方差大，接受率波动大，推理验证成本高的问题
- 纯分数强化学习引发的反馈质量退化
- 生成分子难以对齐目标性质，离散序列优化方差高、训练过程不稳定
- 结果级统一奖励导致学习信号模糊、训练不稳定，冗余推理路径拉低模型推理性能

## 评测信号

- 观测到预训练损失可预测给定RL算力下的后训练性能，预训练token越多，后RL性能越高、提升速度越快。
- DSWorld实现训练加速约14倍、推理加速3-6倍，转移预测超出最强LLM基线35.6%，且保持任务竞争性能。
- QUADS达到BF16级精度，相较原生NVFP4 RL平均pass@1提升21.49分，rollout吞吐量较FP8高约16%。
- 在公开长视频基准和自研MEventBench上，该模型的性能均显著优于当前已有的最优基线方法
- 在CulturalFrames基准上取得80.54%成对准确率，推理速度相比传统VQA基评估器提升10倍，性能优于现有方法
- 对比现有主流方法，相同训练预算下该方法在SWE-Bench最高提5.0个百分点，FrozenLake最高提9.3个百分点。
- 在标准数学推理基准测试，OC-GRPO相较原生GRPO取得平均3.9%绝对准确率提升、13.8%相对增益，额外成本可忽略。
- 重点评测不同阶段加入推理对翻译质量的影响，分析翻译质量提升与计算成本增加之间的权衡关系。
- AdaFlash可稳定提升部署推理加速比，高并发场景增益显著，吞吐量较之前SOTA方法最高提升约66%
- RFE框架契合专家偏好，具备强区分能力，RLAES-AGFO在ASAP基准QWK达0.803，为大语言模型方法最优。

## 控制机制 / Harness 信号

- 通过受控测试床控制预训练与后训练的变量，采用基于可验证奖励的强化学习研究模型推理能力变化。
- 通过学习世界模型预判操作效果，结合成本感知路由，用误差感知强化学习优化预测，加速智能体训练推理。
- 通过双侧量化误差对齐、训练侧不对称量化感知、rollout侧残差激活补偿稳定低精度MoE强化学习训练。
- 通过模块化设计实现动态粒度编码调度，结合强化学习学习最优定位策略，提升长视频建模可靠性
- 通过构建集成隐式文化探针与跳跃连接交叉注意力的奖励模型，提供文化感知的评估奖励信号，缓解评估偏差。
- 通过过程奖励引导树状轨迹展开，选择性分配采样预算、裁剪无效退化路径，提升策略优化的探索效率，改进智能体性能。
- 通过引入带特权信息的引导推演，结合重要性修正的优化目标，调整模型更新方向，提升大模型推理能力。
- 采用可验证奖励强化学习（RLVR）开展模型后训练，通过控制阶段是否保留推理迹分析推理的影响。
- 通过定制逆KL散度的同策略蒸馏降低域级方差，搭配自适应长度头处理词元级方差，降低推理验证成本
- 通过设计基于评分标准的可评估奖励，用强化学习优化作文评分与反馈，按需激活奖励降低评估开销并提升质量。

## 可靠性 / 落地风险

- 研究基于中小规模模型与特定领域，结论能否推广到大规模通用大语言模型仍不明确。
- 仅在自建数据集验证，方法泛化性未在真实大规模数据科学任务中验证。
- 方法仅针对NVFP4格式，仅在MoE RL场景验证，跨场景通用性仍有待验证。
- 动态粒度调度机制增加了模型复杂度，推理开销不稳定，工业落地部署难度较高
- 仅在单一文化评估基准上验证，未验证其在实际生成偏好优化中的落地效果
- 方法效果依赖过程反馈评分器的质量，额外的树管理步骤会增加一定计算开销。
- 仅在数学推理基准验证，方法通用性尚未在更多类型任务中得到验证。
- 推理会增加输出token数量，推高计算资源需求，落地应用的算力成本较高。
- 未验证该方法在不同大模型、多任务域下的泛化能力，缺乏长序列场景的效果验证
- 奖励评估依赖LLM-as-judge，奖励质量受基座模型能力限制，仍存在一定的评估开销。

## 代码资源

- [Distilled Reinforcement Learning for LLM Post-training](https://github.com/597358816/Distilled-RL.) · 3 stars
- [Reward-Driven LLM Agent Workflows: Synthesizing POMDP Routing and Self-Correctio...](https://github.com/01Amez/RLAW_Implementation.)

## 常见基线方法

- **GRPO**：2 篇
- **监督微调（SFT）**：1 篇
- **最强LLM基线**：1 篇
- **原生NVFP4强化学习**：1 篇
- **FP8低精度推理**：1 篇
- **现有SOTA长视频理解方法**：1 篇
- **代表性视觉语言评估指标**：1 篇
- **MLLM基评估器**：1 篇
- **传统VQA基评估器**：1 篇
- **RLOO**：1 篇

## 常用数据集

- **数学推理基准**：4 篇
- **摘要未提及**：3 篇
- **人类国际象棋对局**：1 篇
- **国际象棋谜题**：1 篇
- **数学领域文本**：1 篇
- **8K规模数据科学操作转移轨迹数据集**：1 篇
- **多个MoE强化学习基准**：1 篇
- **公开长视频理解基准**：1 篇
- **MEventBench**：1 篇
- **CulturalFrames基准**：1 篇

---
*自动生成于 2026-07-26 | ArXiv_Daily_Digest*