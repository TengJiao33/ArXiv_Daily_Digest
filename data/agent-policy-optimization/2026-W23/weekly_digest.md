# Agent 策略优化与在线蒸馏 — 2026-W23 (06/01-06/07)

本周新增 **129** 篇论文，**17** 篇附带代码。优先级：high 61 / medium 55 / low 13。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Agentic Monte Carlo: Simulating Reinforcement Learning for Black...](http://arxiv.org/abs/2606.05296v1) | policy optimization | 随着测试时计算量扩展，AMC性能持续提升，效果优于提示基线甚至GRPO，且无需修改黑箱智能体... | 通过学习价值函数引导序贯蒙特卡洛对最优策略后验采样，无需修改黑箱模型参数即可完成... | 依赖测试时多轮采样，计算成本随性能提升同步升高，对黑箱模型输出稳... | ✅ |
| 2 | high | - | [Breaking Contextual Inertia: Reinforcement Learning with Single-...](http://arxiv.org/abs/2603.04783) | policy optimization | 大模型多轮交互性能下降根源是上下文惯性，利用自身单轮能力做锚点强化可显著提效且无需外部验证器 | 利用模型自身单轮能力作为锚点构建奖励信号，通过强化学习校准多轮推理行为，打破上下... | 依赖模型自身单轮能力，若单轮能力不足则方法效果下降，未明确在标准... | ✅ |
| 3 | high | - | [Milestone-Guided Policy Learning for Long-Horizon Language Agent...](http://arxiv.org/abs/2605.06078) | policy optimization | 在长周期ALFWorld任务中，BEACON成功率达92.9%，接近翻倍GRPO的53.5%... | 通过按里程碑分割轨迹，结合分段奖励塑形与双尺度优势估计，优化信用分配，提升长周期... | 该方法依赖任务存在可划分的里程碑结构，对无明确里程碑的任务通用性... | ✅ |
| 4 | high | - | [PRPO: Aligning Process Reward with Outcome Reward in Policy Opti...](http://arxiv.org/abs/2601.07182) | policy optimization | 仅用8次采样、无需价值网络，PRPO在MATH500上将Qwen2.5-Math-1.5B推... | 在无价值网络的无批评家框架下，通过对齐过程奖励与结果奖励的优势分布，为多步推理提... | 仅在小模型数学推理任务验证，未在复杂开放任务测试，方法的通用性有... | ✅ |
| 5 | high | - | [Rewarding Beliefs, Not Actions: Consistency-Guided Credit Assign...](http://arxiv.org/abs/2605.20061) | policy optimization | 引入信念一致性自监督后，对比GRPO基线，任务成功率最高提升20.4个百分点，样本效率提升2... | 通过信念一致性构建自监督稠密信号，结合信念感知分组优化优势估计，改进智能体长周期... | 仅在两个公开基准验证，未在更大规模复杂长周期任务测试，泛化性待验... | ✅ |
| 6 | high | - | [SOD: Step-wise On-policy Distillation for Small Language Model A...](http://arxiv.org/abs/2605.07725) | online distillation | 现有同策略蒸馏应用于工具推理会引发错误级联放大分歧，本文方法最高提20.86%，0.6B模型... | 基于师生蒸馏框架，按每一步师生分歧自适应重加权蒸馏强度，过滤误导性教师信号，优化... | 仅在公开标准基准上验证，未测试真实复杂工具交互场景下的鲁棒性。 | ✅ |
| 7 | high | - | [Safe and Scalable Web Agent Learning via Recreated Websites](http://arxiv.org/abs/2603.10505) | reward learning | 经VeriEnv训练的智能体可泛化到未见网站，通过自进化获得站点特异性能力，扩展训练环境可获... | 构建大模型生成的可验证合成网站环境，提供可编程验证的确定性奖励，替代不可靠的启发... | 合成环境与真实网站存在差异可能带来泛化偏差，自动克隆网站对大模型... | ✅ |
| 8 | high | - | [Sailing by the Stars: A Survey on Reward Models and Learning Str...](http://arxiv.org/abs/2505.02686v2) | survey | 当前大语言模型发展已从预训练缩放转向后训练与测试时缩放，从奖励中学习是该阶段的核心统一范式。 | 本文系统梳理了基于奖励信号引导大语言模型行为的各类学习策略与奖励模型设计相关研究... | 作为综述类研究未开展实证验证，对领域问题的分析缺乏实际落地的实证... | ✅ |
| 9 | high | - | [T$^2$PO: Uncertainty-Guided Exploration Control for Stable Multi...](http://arxiv.org/abs/2605.02178) | policy optimization | 在token和轮两个层级做不确定性引导探索控制，可有效缓解多轮RL训练崩溃，显著提升任务性能... | 通过不确定性感知机制，在token级监测不确定性触发思考干预，轮级重采样低效探索... | 不确定性阈值需要针对不同任务调参，在大规模复杂任务上的泛化性尚未... | ✅ |
| 10 | high | - | [A Subgoal-driven Framework for Improving Long-Horizon LLM Agents](http://arxiv.org/abs/2603.19685) | policy optimization | 结合显式推理时规划与里程碑奖励，Gemma3-12B成功率从6.4%升至43%，超过GPT-... | 通过子目标分解实现显式实时在线规划，设计基于里程碑的密集奖励信号做强化学习微调优... | 依赖专有大模型生成子目标，落地成本较高，未验证跨不同长任务的泛化... | — |
| 11 | high | - | [ATLAS: Agentic Test-time Learning-to-Allocate Scaling](http://arxiv.org/abs/2606.01667v1) | agent harness | 基于Claude Sonnet 4.6的ATLAS在HLE-Verified达56%，多模型... | 以LLM作为端到端编排器，通过探索动作动态分配计算资源，自主决定停止时机，集成证... | 依赖LLM做端到端编排，扩展多求解器后系统复杂度上升，落地部署的... | — |
| 12 | high | ICLR 2026 | [AgentMath: Empowering Mathematical Reasoning for Large Language ...](http://arxiv.org/abs/2512.20745) | policy optimization | AgentMath-30B-A3B在三个基准分别达90.6%/86.4%/73.8%准确率，... | 通过自动生成高质量SFT数据、交错执行的智能体强化学习，结合训练调度优化，提升A... | 仅在数学推理基准验证，未测试通用场景，工程优化复杂度较高，大模型... | — |

## A 会 / Venue 标签

- **ICLR 2026**：3 篇
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
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*