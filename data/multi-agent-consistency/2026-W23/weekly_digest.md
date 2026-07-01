# 多 Agent 交互与一致性 — 2026-W23 (06/01-06/07)

本周新增 **150** 篇论文，**20** 篇附带代码。优先级：high 96 / medium 43 / low 11。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AgentDropoutV2: Optimizing Information Flow in Multi-Agent Syste...](http://arxiv.org/abs/2602.23258) | agent harness | 测试时校正拒绝剪枝可有效抑制多智能体错误传播，在数学、代码基准分别提升准确率6.39、2.2... | 离线从多智能体历史失败轨迹蒸馏错误模式构建指标池，测试时拦截输出，校正后剪枝不可... | 依赖离线历史错误模式蒸馏，对未见过的新错误模式泛化性不足，存在适... | ✅ |
| 2 | high | - | [Beyond Alignment: Value Diversity as a Collective Property in Mu...](http://arxiv.org/abs/2606.05985v1) | evaluation/benchmark | 价值多样性与价值对齐不相关，当前LLM多文化多智能体价值多样性远低于人类，社会交互会进一步推... | 仅提出价值多样性这一新的系统级评估维度，未提出针对智能体行为的控制改进方法。 | 仅提出评估维度，未给出同质化问题的解决方案，结论泛化性有待进一步... | ✅ |
| 3 | high | ICLR 2024 | [ChatEval: Towards Better LLM-based Evaluators through Multi-Agen...](http://arxiv.org/abs/2308.07201v1) | evaluation/benchmark | 融入多智能体辩论的ChatEval可模拟人类评估过程，评估结果相比单智能体方法更贴近人类水平... | 通过多智能体辩论框架整合不同大语言模型的能力优势，构建多智能裁判团队，提升文本评... | 需要调用多个大语言模型完成辩论，评估的算力与时间成本高于单智能体... | ✅ |
| 4 | high | - | [CyberJurors: A Multi-Agent Simulation Task for E-Commerce Disput...](http://arxiv.org/abs/2605.28369) | multi-agent coordination | CyberJurors在电商纠纷裁决任务上性能优于现有SOTA大模型和法庭模拟器，与真实陪审... | 个体层面分解任务做精细推理，集体层面模拟多轮讨论投票，融入判例缓解认知偏差，规范... | 基于众包数据构建基准，可能存在标签噪声，模型在更多样真实场景的泛... | ✅ |
| 5 | high | EMNLP 2024 | [DebUnc: Improving Large Language Model Agent Communication With ...](http://arxiv.org/abs/2407.06426) | multi-agent coordination | 基于注意力传递不确定性的方法效果尤其突出，框架性能会随不确定性估计可靠性提升持续提升。 | 引入不确定性度量评估各智能体置信度，通过改进注意力机制或文本提示，调整多智能体辩... | 未披露具体评测基准细节，未验证跨模型泛化性，不确定性估计本身可能... | ✅ |
| 6 | high | - | [Debate or Vote: Which Yields Better Decisions in Multi-Agent Lar...](http://arxiv.org/abs/2508.17536) | multi-agent coordination | 原本归为多智能体辩论的大部分性能增益实际来自多数投票，单独辩论无法提升决策期望正确率。 | 通过拆解多智能体辩论的核心组件分析不同机制作用，提出偏向正确信念更新的定向干预改... | 盲目依赖多智能体辩论会增加计算成本，却无法获得对应性能提升。 | ✅ |
| 7 | high | ICML 2025 | [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reason...](http://arxiv.org/abs/2506.08292) | multi-agent coordination | ECON在六个推理规划基准上平均性能比现有多LLM方法高出11.2%，理论上拥有比非均衡方案... | 将多LLM协调建模为不完全信息博弈，基于贝叶斯纳什均衡设计分层强化学习框架，实现... | 未在更大规模多LLM集成场景验证实际效果，可扩展性的实际优势还需... | ✅ |
| 8 | high | - | [Hear Both Sides: Efficient Multi-Agent Debate via Diversity-Awar...](http://arxiv.org/abs/2603.20640) | multi-agent coordination | 选择性保留分歧性高的消息而非全量广播，可稳定提升辩论性能，智能体规模越大噪声越重提升越明显。 | 通过多样性感知的消息保留机制，每轮选择性广播分歧最大的响应子集，过滤冗余噪声，提... | 分歧度量的稳定性可能影响结果，未验证长周期复杂辩论场景下的泛化效... | ✅ |
| 9 | high | - | [Learning to break: Knowledge-enhanced reasoning in multi-agent d...](http://arxiv.org/abs/2312.04854) | multi-agent coordination | 引入共享检索知识可打破多智能体辩论认知孤岛，基于Qwen1.5-72B-Chat的MADKE... | 通过引入共享检索知识池与自适应知识选择，在多智能体辩论过程中对齐智能体认知，提升... | 未验证开放域真实场景下的泛化性，大模型推理成本较高，未提及长周期... | ✅ |
| 10 | high | - | [MOC: Multi-Order Communication in LLM-based Multi-Agent Systems](http://arxiv.org/abs/2606.02359v1) | multi-agent coordination | MOC在不同参数规模的大语言模型、六个不同数据集上，都能稳定提升任务性能同时降低通信成本。 | 重构智能体间通信，构建结构化多阶证据流，设计语义拓扑合并算法，兼顾通信效率与语义... | 未公开具体实验数据集，方法在更复杂大规模多智能体场景下的泛化性未... | ✅ |
| 11 | high | ICLR 2026 | [Multi-Agent Debate with Memory Masking](http://arxiv.org/abs/2603.20215) | multi-agent coordination | 多智能体辩论的性能高度依赖前期辩论生成的记忆质量，错误记忆会显著降低多智能体辩论的推理性能。 | 在每轮多智能体辩论开始前引入记忆掩码机制，让智能体过滤历史错误记忆、保留有效记忆... | 仅在数学与逻辑推理任务验证，未测试其他多智能体场景，方法泛化性尚... | ✅ |
| 12 | high | - | [What Should Agents Say? Action-state Communication for Efficient...](http://arxiv.org/abs/2606.05304v1) | multi-agent coordination | 不存在通用最优的固定跨智能体通信策略，PACT在SWE-agent减半输入token保解决率... | 通过设计协议化通信机制，将无约束自然语言通信压缩为结构化动作状态记录，保留有效信... | 仅在编码类多智能体任务验证效果，在其他类型多智能体任务中的通用性... | ✅ |

## A 会 / Venue 标签

- **ICLR 2026**：2 篇
- **ACL 2025**：2 篇
- **ICML 2025**：2 篇
- **ICLR 2024**：2 篇
- **EMNLP 2024**：2 篇
- **EMNLP 2025**：1 篇
- **ACL 2024**：1 篇
- **ICLR 2023**：1 篇
- **ICML 2023**：1 篇

## 方法族分布

- **multi-agent coordination**：92 篇
- **evaluation/benchmark**：30 篇
- **agent harness**：6 篇
- **survey**：5 篇
- **consistency detection**：4 篇
- **policy optimization**：3 篇
- **unlearning/safety**：3 篇
- **reward learning**：1 篇
- **multi-agent coordination, factuality benchmark**：1 篇
- **tool-use control**：1 篇
- **skill generation**：1 篇
- **model steering**：1 篇

## 失败模式与风险信号

- 多跳多智能体通信中关键信息稀释，证据感受野受限
- 大规模多智能体集群因信息传播稀疏，一致性收敛后稳态分散度随规模增大而升高
- 现有模型因缺乏领域知识、对硬件约束不敏感，导致信号生成性能大幅下降
- 现有资源分配方法忽略资源间协作模式，导致实际任务交接流程性能偏低。
- 全连接通信开销过高，固定稀疏拓扑适配性差，易丢失关键纠错信息
- 不同社会群体间的通用事实输出不一致，客观任务回答准确性存在系统性偏差
- 单轮防御无法捕捉多轮越狱的跨轮风险累积，重训练防御会损害模型原生效用。
- 现有理论框架无法刻画分类多智能体策略一致性失效问题
- 多智能体交互中大模型盲目从众，容易被误导产生有害修正，引入错误
- 单智能体处理长周期任务易卡住、执行效率低

## 评测信号

- MOC在不同参数规模大模型、六个不同数据集上，均能稳定提升任务性能，同时有效降低通信成本。
- 在最多10个智能体的协作导航任务中，该方法所得帕累托前沿优于基线，可扩展到更大规模团队
- 相比集中式MARL可得到更平滑的一致性轨迹，3智能体训练的策略零样本扩展到250智能体仍能收敛
- 在真实场景中评测配置可行性与信号保真度，结果表明RadioMaster性能显著优于现有SOTA基线方法。
- 该方法相比启发式基线，平均降低流程成本37%、等待时间58%，性能提升显著，稳定优于基线方法。
- 验证DySCo可在降低多智能体共识的token成本与通信延迟的同时，保留推理和问答任务的有效性能。
- 评测模型在通用真值准确率、跨群体事实一致性、个性化质量三个目标上的平衡表现
- 该方法将攻击成功率降至0.2%-4.0%，在MMLU和GSM8K上模型效用的降幅不超过1.5%，泛化性稳定。
- 通过资源约束下异构智能体攻防的免疫堡垒防御案例，验证了所提框架具备良好的表达能力。
- 测量不同社会线索下大模型从众行为中有益修正和有害修正的占比，验证通用推理干预的缓解效果。

## 控制机制 / Harness 信号

- 重构智能体间通信，构建结构化多阶证据流，设计语义拓扑合并算法，兼顾通信效率与语义保真度。
- 通过协调图分解联合任务，结合拉格朗日对偶控制目标与约束的权衡，使用消息传递协调多智能体动作
- 将集群通信图融入分层决策过程，训练分布式一致性规划器，引导多智能体达成控制一致性
- 通过领域知识检索、多智能体协作生成、闭环物理层验证三层协同架构，提升信号生成可用性。
- 结合多智能体流程仿真与多目标进化算法，引入协作感知优化，生成资源专属的帕累托最优交接策略。
- 通过动态估计通信边价值选择高价值交互，基于信任加权聚合答案，共识稳定时提前终止，优化多智能体共识过程。
- 将每个社会群体建模为独立智能体，通过公平感知目标和显式不一致惩罚优化，保障跨群体通用事实一致性
- 整合回合级风险、历史上下文、响应输出三类信号，通过时变得分机制实现多轮越狱防御。
- 通过构建基于层的统一范畴框架建模多智能体系统，基于范畴理论工具实现策略一致性的可验证分类。
- 通过操纵共识结构、同伴权威标签两种社会线索开展对照实验，提出多智能体系统应验证同伴答案而非直接聚合。

## 可靠性 / 落地风险

- 未公开具体实验数据集，方法在更复杂大规模多智能体场景下的泛化性未验证。
- 仅验证了最多10个智能体的场景，更大规模更复杂约束下的有效性未经验证
- 依赖固定的2邻居通信拓扑，动态拓扑下的有效性未验证，大规模场景下一致性精度会下降
- 依赖专用无线硬件，仅在自建基准测试，泛化性未验证，工业落地不确定性较高。
- 仅在中小规模数据集验证，未测试大规模复杂业务场景的通用性与稳定性。
- 仅给出任务类验证，未披露公开基准的具体量化结果，实际有效性验证不充分。
- 未公开具体基准与基线细节，离线多智能体强化学习算力开销较高，泛化性未经验证
- 仅在两个目标模型上验证，未覆盖更多真实场景，防御的通用泛化性有待进一步验证。
- 该工作为纯理论框架，未在大规模实际多智能体场景中验证，落地性尚不明确。
- 现有多智能体大语言模型系统仅聚合不验证同伴答案，容易因从众误导引入错误，降低输出可靠性。

## 代码资源

- [ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate](https://github.com/chanchimin/ChatEval.) · 335 stars
- [Debate or Vote: Which Yields Better Decisions in Multi-Agent Large Language Mode...](https://github.com/deeplearning-wisc/debate-or-vote.) · 77 stars
- [From Debate to Equilibrium: Belief-Driven Multi-Agent LLM Reasoning via Bayesian...](https://github.com/tmlr-group/ECON.) · 39 stars
- [AgentDropoutV2: Optimizing Information Flow in Multi-Agent Systems via Test-Time...](https://github.com/TonySY2/AgentDropoutV2.) · 27 stars
- [Hear Both Sides: Efficient Multi-Agent Debate via Diversity-Aware Message Retent...](https://github.com/DA2I2-SLM/DAR.) · 17 stars
- [Learning to break: Knowledge-enhanced reasoning in multi-agent debate system](https://github.com/FutureForMe/MADKE) · 14 stars
- [DebUnc: Improving Large Language Model Agent Communication With Uncertainty Metr...](https://github.com/lukeyoffe/debunc.) · 13 stars
- [Memory-Augmented LLM-based Multi-Agent System for Automated Feature Generation o...](https://github.com/fxdong24/MALMAS) · 13 stars
- [Beyond the Individual: Virtualizing Multi-Disciplinary Reasoning for Clinical In...](https://github.com/HovChen/Aegle.) · 8 stars
- [Benchmarking LLM-as-a-Judge for Long-Form Output Evaluation](https://github.com/cjj826/LongJudgeBench.) · 5 stars

## 常见基线方法

- **自一致性**：4 篇
- **多数投票**：4 篇
- **SOTA基线方法**：2 篇
- **思维链（Chain-of-Thought）**：2 篇
- **单大语言模型基线**：2 篇
- **现有多智能体辩论方法**：2 篇
- **固定奖励整形比训练的基线方法**：1 篇
- **集中式MARL控制器**：1 篇
- **启发式基线**：1 篇
- **全连接通信多智能体框架**：1 篇

## 常用数据集

- **摘要未提及**：8 篇
- **GSM8K**：4 篇
- **MMLU**：3 篇
- **GAIA**：3 篇
- **HotpotQA**：2 篇
- **SWE-bench**：2 篇
- **MMLU-Pro**：2 篇
- **GPQA**：2 篇
- **数学推理基准**：2 篇
- **六个不同类型数据集**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*