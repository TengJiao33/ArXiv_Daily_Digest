# Agent 策略优化与在线蒸馏 — 2026-W23 (06/01-06/07)

本周新增 **129** 篇论文，**17** 篇附带代码。优先级：high 61 / medium 55 / low 13。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 控制/评测 | 风险 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|------|-----------|:----:|
| 1 | high | - | [Agentic Monte Carlo: Simulating Reinforcement Learning for Black...](http://arxiv.org/abs/2606.05296v1) | policy optimization | 通过学习价值函数引导序贯蒙特卡洛对最优策略后验采样，无需修改黑箱模型参数即可完成... | 依赖测试时多轮采样，计算成本随性能提升同步升高，对黑箱模型输出稳... | 可结合AMC框架优化黑箱教师智能体的策略，提升面向黑箱老师的在线蒸馏任务的最终效果。 | ✅ |
| 2 | high | - | [Breaking Contextual Inertia: Reinforcement Learning with Single-...](http://arxiv.org/abs/2603.04783) | policy optimization | 利用模型自身单轮能力作为锚点构建奖励信号，通过强化学习校准多轮推理行为，打破上下... | 依赖模型自身单轮能力，若单轮能力不足则方法效果下降，未明确在标准... | 如何将这种基于模型自身能力锚定的思路，推广到多轮Agent交互场景的可靠性优化中？ | ✅ |
| 3 | high | - | [Milestone-Guided Policy Learning for Long-Horizon Language Agent...](http://arxiv.org/abs/2605.06078) | policy optimization | 通过按里程碑分割轨迹，结合分段奖励塑形与双尺度优势估计，优化信用分配，提升长周期... | 该方法依赖任务存在可划分的里程碑结构，对无明确里程碑的任务通用性... | 可否将本文的里程碑信用分配范式引入在线策略蒸馏，提升长周期agent训练的样本效率？ | ✅ |
| 4 | high | - | [PRPO: Aligning Process Reward with Outcome Reward in Policy Opti...](http://arxiv.org/abs/2601.07182) | policy optimization | 在无价值网络的无批评家框架下，通过对齐过程奖励与结果奖励的优势分布，为多步推理提... | 仅在小模型数学推理任务验证，未在复杂开放任务测试，方法的通用性有... | 可拓展研究将PRPO的过程-结果奖励对齐思路应用到多步交互agent，提升长周期任务策略优化... | ✅ |
| 5 | high | - | [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assign...](http://arxiv.org/abs/2605.20061) | policy optimization | 通过信念一致性构建自监督稠密信号，结合信念感知分组优化优势估计，改进智能体长周期... | 仅在两个公开基准验证，未在更大规模复杂长周期任务测试，泛化性待验... | 基于信念一致性的信用分配思路，能否结合在线蒸馏提升大语言模型智能体的长周期决策性能？ | ✅ |
| 6 | high | - | [SOD: Step-wise On-policy Distillation for Small Language Model A...](http://arxiv.org/abs/2605.07725) | online distillation | 基于师生蒸馏框架，按每一步师生分歧自适应重加权蒸馏强度，过滤误导性教师信号，优化... | 仅在公开标准基准上验证，未测试真实复杂工具交互场景下的鲁棒性。 | 如何利用分步自适应蒸馏抑制小语言模型智能体的错误级联，提升工具推理的可靠性？ | ✅ |
| 7 | high | - | [Safe and Scalable Web Agent Learning via Recreated Websites](http://arxiv.org/abs/2603.10505) | reward learning | 构建大模型生成的可验证合成网站环境，提供可编程验证的确定性奖励，替代不可靠的启发... | 合成环境与真实网站存在差异可能带来泛化偏差，自动克隆网站对大模型... | 能否将VeriEnv提供的可验证确定性奖励与在线策略蒸馏结合，进一步提升网络智能体自进化训练... | ✅ |
| 8 | high | - | [Sailing by the Stars: A Survey on Reward Models and Learning Str...](http://arxiv.org/abs/2505.02686v2) | survey | 本文系统梳理了基于奖励信号引导大语言模型行为的各类学习策略与奖励模型设计相关研究... | 作为综述类研究未开展实证验证，对领域问题的分析缺乏实际落地的实证... | 基于该综述梳理的奖励学习研究成果，能否总结出适配Agent在线策略蒸馏的奖励设计方案？ | ✅ |
| 9 | high | - | [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi...](http://arxiv.org/abs/2605.02178) | policy optimization | 通过不确定性感知机制，在token级监测不确定性触发思考干预，轮级重采样低效探索... | 不确定性阈值需要针对不同任务调参，在大规模复杂任务上的泛化性尚未... | 可结合该细粒度不确定性探索控制方法，改进多轮智能体在线策略蒸馏过程的训练稳定性。 | ✅ |
| 10 | high | - | [A Subgoal-driven Framework for Improving Long-Horizon LLM Agents](http://arxiv.org/abs/2603.19685) | policy optimization | 通过子目标分解实现显式实时在线规划，设计基于里程碑的密集奖励信号做强化学习微调优... | 依赖专有大模型生成子目标，落地成本较高，未验证跨不同长任务的泛化... | 探索将本文的里程碑奖励机制与在线策略蒸馏结合，进一步降低开放大模型agent的推理成本并提升... | — |
| 11 | high | - | [ATLAS: Agentic Test-time Learning-to-Allocate Scaling](http://arxiv.org/abs/2606.01667v1) | agent harness | 以LLM作为端到端编排器，通过探索动作动态分配计算资源，自主决定停止时机，集成证... | 依赖LLM做端到端编排，扩展多求解器后系统复杂度上升，落地部署的... | 能否将在线策略蒸馏引入ATLAS框架，学习编排器的动态分配策略，进一步降低测试时计算开销并提... | — |
| 12 | high | - | [AgentMath: Empowering Mathematical Reasoning for Large Language ...](http://arxiv.org/abs/2512.20745) | policy optimization | 通过自动生成高质量SFT数据、交错执行的智能体强化学习，结合训练调度优化，提升A... | 仅在数学推理基准验证，未测试通用场景，工程优化复杂度较高，大模型... | 将本文交错工具执行的RL策略优化方法迁移到通用工具Agent，能否提升其工具使用的可靠性？ | — |

## A 会 / Venue 标签

- **EMNLP 2025**：2 篇
- **ICLR 2025**：1 篇
- **NeurIPS 2024**：1 篇
- **ACL 2025**：1 篇

## 方法族分布

- **policy optimization**：74 篇
- **reward learning**：17 篇
- **survey**：9 篇
- **online distillation**：8 篇
- **unlearning/safety**：4 篇
- **evaluation/benchmark**：3 篇
- **agent harness**：2 篇
- **other**：2 篇
- **model steering**：2 篇
- **multi-agent coordination**：2 篇
- **未分类**：2 篇
- **policy optimization, online distillation**：1 篇

## 失败模式与风险信号

- 安全对齐后大模型通用能力退化（对齐税）
- 多域RL后训练中，新域训练会导致已训练旧域发生性能退化（跨域干扰）
- 强化训练缺乏动作对环境影响的监督，现有世界建模方法依赖额外资源。
- 现有技能方法依赖外部技能，导致工程复杂度高、上下文更长、部署延迟高
- 权力攫取风险，微小错误或幻觉被放大为灾难性安全故障
- 长推理推理开销高，现有CoT压缩存在灵活性差、成本高、扩展性不足问题
- 难题下正奖励成功轨迹稀缺，仅结果RLVR训练缺乏足够学习信号，效果不佳
- 不同社会群体间的事实回答不一致
- 依赖粗糙反馈的自动奖励设计导致策略与任务指令对齐不良
- 人工固定编排计算分配，无法根据问题灵活调度，造成不必要的算力浪费

## 评测信号

- 仅用100个有害样本（不足现有基线1%数据量），实现更优的安全性能与通用能力的平衡
- 短域刷新将数学性能从57.66恢复至66.04，基本保留其他域性能，最终获得最优平均得分66.39。
- 跨不同模型与强化学习算法，在三个智能体任务基准上相对强RL基线都取得了一致的性能提升。
- 对比多个基线方法，在两个基准验证SIRI相较基础方法GiGPO有明显性能提升，报告了具体任务成功率。
- 验证方案可达成安全与效用的平衡，在有效缓解权力攫取风险的同时保留Agent原有任务完成能力。
- 在9B至122B不同架构模型上实现19%-46%token压缩，精度下降可忽略，训练成本大幅低于现有多阶段方法。
- 性能相近的不同RL算法表征不变性存在稳定差异，该差异对迁移学习有下游影响，且可在LLM中观测到。
- 在七个开放域QA基准上，CAPF相比仅结果RLVR，将Qwen3-4B的平均精确匹配得分提升3.8个百分点。
- TriAlign相比强基线能更好平衡事实准确性、跨群体一致性与个性化三个目标，有效减少不同群体间的事实差异。
- RDA生成策略的指令对齐性显著优于对比基线，同时可以保持与基线相当的任务成功率。

## 控制机制 / Harness 信号

- 通过激活引导构建安全教师模型，筛选安全相关token，仅在安全token施加反向KL蒸馏惩罚实现局部对齐
- 通过局部扰动模型定位损伤所在的低维冲突子空间，利用短域刷新收缩有害分量，实现受损性能选择性恢复。
- 在强化学习训练过程中添加辅助世界建模监督，通过三个专用模块优化监督质量，联合训练提升智能体性能。
- 从自身成功轨迹自挖掘并验证技能，仅将有益技能引导动作蒸馏到原策略，推理无需额外技能库。
- 以服务端插件形式，通过世界模型前瞻推理实现主动工具过滤与紧急干预，结合双可验证奖励强化学习优化策略。
- 通过含自适应中位数长度预算、余弦衰减token奖励、乘法奖励的强化学习框架优化，压缩思维链长度，降低推理开销。
- 基于MDP约简理论分析不同深度RL算法的表征特性，揭示学习目标对表征不变性的影响规律。
- 训练阶段引入验证器侧特权反馈引导智能体修正轨迹，通过信用衰减适配无反馈部署，将零奖励尝试转为正奖励轨迹。
- 采用离线多智能体强化学习框架，通过公平感知目标与显式不一致惩罚，联合优化事实准确性、一致性与个性化效果。
- 借助视觉语言模型引入语义理解，通过任务分解、轨迹评估、失败总结迭代优化奖励代码，提升对齐性。

## 可靠性 / 落地风险

- 仅在小样本设置下验证，未验证大规模实际场景下的泛化性与稳定性
- 随多域任务数量增加，逐个域刷新的成本会上升，扩展到更多域时性能保持的难度会增加。
- 未披露具体基准与实验细节，未在真实复杂任务验证，方法实际泛化能力尚不明确。
- 仅在两个中等规模基准测试，未验证更大模型与更长视界任务的泛化能力。
- 额外的前瞻推理会增加Agent运行计算开销，服务端插件需要适配现有MCP架构。
- 仅在静态推理任务验证效果，未在交互类Agent场景验证方法的通用性与稳定性。
- 属于基础理论研究，缺乏大规模量化评测验证结论普适性，结论通用性待进一步验证。
- 仅在4B小参数模型和开放域QA验证，未验证大模型及其他任务场景的泛化效果。
- 未披露具体基准细节和训练设置，可复现性不明确，离线多智能体训练成本未公开说明。
- 仅在小规模封闭机器人操作任务验证，未测试开放复杂场景，泛化能力未得到验证。

## 可延展 Idea Hook

- 将这种局部化蒸馏思路引入agent在线策略蒸馏，能否减少对齐对agent通用能力的损耗？
- 可基于该低维冲突子空间机制，设计多任务Agent后训练中跨域性能干扰的低成本抑制方案。
- 可以探索将该策略与世界建模联合训练思路引入在线蒸馏，提升学生智能体的训练效率与最终性能。
- 能否将这种自内化技能蒸馏思路拓展到测试时缩放，提升长视界agent的任务执行可靠性？
- 可结合当前Agent在线蒸馏方向，研究如何压缩SafeMCP的推理开销，同时保持原有的安全防御效果。
- 能否将HMPO的自适应长度压缩思路引入Agent在线蒸馏，压缩Agent长推理轨迹以降低在线推理开销。
- 能否利用不同RL算法表征不变性的差异，设计更适合在线蒸馏的teacher模型表征，提升蒸馏效果？
- 可将CAPF的特权反馈思路扩展到通用Agent在线策略蒸馏中，解决稀疏奖励下的训练低效问题。
- 能否将TriAlign的一致性惩罚奖励设计思路，引入个性化agent策略优化，提升多群体场景下agent输出事实一致性？
- 能否将这种引入语义反馈的奖励设计思路，推广到通用大模型智能体的在线奖励学习对齐中？
- 能否将在线策略蒸馏引入ATLAS框架，学习编排器的动态分配策略，进一步降低测试时计算开销并提升性能？
- 能否将ReSkill的技能策略协同进化机制，结合在线蒸馏实现agent测试阶段扩展，提升泛化性能？

## 下次可问导师的问题

- 这种局部化同策略蒸馏思路，是否适合迁移到agent策略优化场景中？
- 这种局部低维干扰机制，能否推广到多任务LLM Agent后训练中，稳定抑制性能退化？
- 我们研究在线策略蒸馏，是否可以结合该联合训练思路设计新的蒸馏训练框架？
- 我们能不能将这种自技能蒸馏的思路整合进当前的在线agent蒸馏研究中？
- 我们是否需要结合当前的策略优化方向，探索Agent安全防御的轻量化改进方向？
- 我们是否可以尝试将HMPO的自适应压缩思路结合到当前Agent在线蒸馏的研究流程中？
- 这种表征不变性的差异是否可以用来优化agent在线蒸馏过程，提升蒸馏效率？
- 我们是否可以尝试将CAPF机制整合到当前搜索Agent的策略优化框架中做效果验证？
- 我们做agent策略优化时，是否需要加入这类事实一致性约束来提升agent输出的事实可靠性？
- 我们是否可以基于该语义奖励思路，开展通用任务智能体的奖励学习改进研究？
- 我们结合在线蒸馏改进该自适应测试时缩放框架，这个选题的挖掘空间和价值怎么样？
- 我们研究在线策略蒸馏，是否可以引入本文的协同机制来提升学生智能体策略的泛化性？

## 代码资源

- [SOD: Step-wise On-policy Distillation for Small Language Model Agents](https://github.com/YoungZ365/SOD.) · 130 stars
- [Sailing by the Stars: A Survey on Reward Models and Learning Strategies for Lear...](https://github.com/bobxwu/learning-from-rewards-llm-papers.) · 71 stars
- [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Re...](https://github.com/WillDreamer/T2PO.) · 33 stars
- [Milestone-Guided Policy Learning for Long-Horizon Language Agents](https://github.com/ZJU-REAL/BEACON.) · 17 stars
- [Text-to-Decision Agent: Offline Meta-Reinforcement Learning from Natural Languag...](https://github.com/NJU-RL/T2DA) · 17 stars
- [ReRec: Reasoning-Augmented LLM-based Recommendation Assistant via Reinforcement ...](https://github.com/jiani-huang/ReRec.) · 6 stars
- [Enhancing LLM Metacognition via Cognitive Pairwise Training](https://github.com/Tsinghua-dhy/CPT.) · 5 stars
- [Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforceme...](https://github.com/THUAIS-Lab/CHERRL.) · 4 stars
- [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assignment for Long-Ho...](https://github.com/Fateyetian/Rebel.git.) · 3 stars
- [Generalization in Online Reinforcement Learning for Mobile Agents](https://github.com/zihuanjiang/AndroidWorld-Generalization) · 3 stars

## 常见基线方法

- **GRPO**：10 篇
- **GPT-4o**：5 篇
- **GiGPO**：3 篇
- **强化学习基线**：3 篇
- **监督微调**：3 篇
- **PPO**：2 篇
- **GPT-5.2**：2 篇
- **GPT-4-Turbo**：2 篇
- **监督微调(SFT)**：2 篇
- **基础大语言模型**：2 篇

## 常用数据集

- **ALFWorld**：7 篇
- **WebShop**：7 篇
- **摘要未提及**：7 篇
- **数学推理任务**：3 篇
- **WebArena-Lite**：3 篇
- **WebArena**：3 篇
- **AndroidWorld**：3 篇
- **LiveCodeBench**：2 篇
- **数学推理基准**：2 篇
- **网页导航基准**：2 篇

---
*自动生成于 2026-06-07 | ArXiv_Daily_Digest*