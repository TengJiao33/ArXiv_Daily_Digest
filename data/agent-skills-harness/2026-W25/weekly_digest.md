# Agent Skills 与 Harness — 2026-W25 (06/15-06/21)

本周新增 **147** 篇论文，**8** 篇附带代码。优先级：high 118 / medium 23 / low 6。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 控制/评测 | 风险 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|------|-----------|:----:|
| 1 | high | - | [Benign in Isolation, Harmful in Composition: Security Risks in A...](http://arxiv.org/abs/2606.15242) | evaluation/benchmark | 构建可控沙箱评测基准SCR-Bench，从激活路径层面评估智能体多技能组合的安全... | 工业级agent技能生态大量复用第三方技能，现有审核漏检风险，会... | 如何基于路径感知风险评估思路，设计面向工业级agent技能生态的可落地安全审核机制？ | ✅ |
| 2 | high | - | [Consensus-based Agentic Large Language Model Framework for Harmo...](http://arxiv.org/abs/2606.16987v1) | multi-agent coordination | 通过共识验证、分层投票、置信度估计结合人机闭环，约束智能体行为，提升分类可靠性与... | 采用私有标注数据集，无公开基准对比，结果的可比较性存在不足。 | 可基于该多智能体共识框架，探索垂直领域工业任务中多智能体harness的可靠性优化方案。 | ✅ |
| 3 | high | - | [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic re...](http://arxiv.org/abs/2606.16771) | policy optimization | 通过冲突感知过滤存在严重奖励分歧的rollout，结合查询级重加权调整更新强度，... | 仅在通用研究场景验证，未在大规模真实工业场景测试，实际落地效果尚... | 能否将该多奖励冲突缓解机制引入工具调用agent的harness框架，提升多约束下agent... | ✅ |
| 4 | high | - | [VeriGraph: Towards Verifiable Data-Analytic Agents](http://arxiv.org/abs/2606.16603) | agent harness | 通过构建显式异质证据DAG，结合图基策略优化联合监督多维度，提升智能体推理的可验... | 仅在学术基准测试，未验证真实工业数据分析场景的可用性与稳定性 | 可将VeriGraph的证据图推理框架推广到通用工具调用场景，提升工具调用结果的可验证性与可... | ✅ |
| 5 | high | - | [A Framework for Evaluating Agentic Skills at Scale](http://arxiv.org/abs/2606.17819v1) | evaluation/benchmark | 构建可复用评估框架，支持开发者自定义任务评估技能效用，通过标准化评分规则评测技能... | 未验证该评估框架得到的技能效用结果，与工业场景实际落地效果的一致... | 能否基于该公开数据集，构建适配工业需求的轻量智能体技能验证基准，测试小模型的技能适配能力？ | — |
| 6 | high | - | [Agent trajectories as programs: fingerprinting and programming c...](http://arxiv.org/abs/2606.16988) | evaluation/benchmark | 通过将智能体轨迹转化为压缩的程序化表征，提取行为指纹，实现对智能体行为过程的审计... | 仅聚焦行为特性分析，未落地到实际任务性能改进，缺乏真实场景部署验... | 基于行为指纹能否实现编码智能体的任务自适应路由，降低工业场景的整体调用成本？ | — |
| 7 | high | - | [AgentFairBench: Do LLM Agents Discriminate When They Act?](http://arxiv.org/abs/2606.16723v1) | evaluation/benchmark | 构建标准化评测基准和轻量化NumPy实现的评测harness，通过统计校正度量A... | 基于合成数据的评测和真实业务场景存在差距，仅用名字编码人口属性的... | 如何基于这个低成本可复现的基准，构建面向工业落地Agent的公平性合规校验 harness？ | — |
| 8 | high | - | [Agentic Electronic Design Automation: A Handoff Perspective](http://arxiv.org/abs/2606.19795v1) | survey | 通过定义交接有效性概念、分类现有系统，提出标准化五层通信协议规范智能体跨边界交接... | 仅提出框架协议，未做实际落地验证，缺乏实测的可靠性数据支撑 | 可将交接有效性框架迁移到通用多Agent工作流，设计通用跨Agent交接契约的可靠性控制方案 | — |
| 9 | high | - | [Analyzing Defensive Misdirection Against Model-Guided Automated ...](http://arxiv.org/abs/2606.20470v1) | unlearning/safety | 采用检测-误导的控制机制，对检测出的恶意交互返回安全且带策略误导性的响应，干扰攻... | 未验证误导策略对正常合法交互的负面影响，缺乏大规模业务场景的落地... | 能否将检测-误导防御思路整合到工具调用Agent的安全harness中，低成本提升工业Age... | — |
| 10 | high | - | [Are Online Skill and Memory Modules Always Worth Their Tokens? A...](http://arxiv.org/abs/2606.15017) | evaluation/benchmark | 通过设定固定总推理token预算，对比增强模块方案与同预算朴素基线，评估在线模块... | 现有技能记忆模块徒增推理部署成本，实际落地收益不足，不符合低算力... | 可探索成本感知的Agent harness框架，裁剪冗余技能模块，在低推理预算下保持Agen... | — |
| 11 | high | - | [Auditing Reward Hackability in Code RL Training Environments](http://arxiv.org/abs/2606.16062) | evaluation/benchmark | 通过审计识别缺陷测试任务，采用带Docker黄金校验门的LLM裁判强化测试环境，... | 现有代码Agent评测基准存在大量可破解任务，会高估模型能力，误... | 可借鉴该奖励可破解性审计思路，构建鲁棒性更强的代码Agent评测基准，满足工业落地的评测需求... | — |
| 12 | high | - | [Autonomous Event-Driven Multi-Agent Orchestration for Enterprise...](http://arxiv.org/abs/2606.20058v1) | multi-agent coordination | 通过引入带有优先级推理、关联事件合并、抢占功能的任务管理器，优化大规模多智能体编... | DAG架构在企业规模下开销较高，未针对低算力工业路线做针对性优化 | 面向大规模企业事件驱动场景，设计低开销任务管理器优化多智能体编排的可靠性与运行效率 | — |

## 方法族分布

- **agent harness**：49 篇
- **evaluation/benchmark**：47 篇
- **tool-use control**：13 篇
- **multi-agent coordination**：10 篇
- **skill generation**：8 篇
- **unlearning/safety**：4 篇
- **policy optimization**：4 篇
- **survey**：3 篇
- **other**：2 篇
- **factuality benchmark**：2 篇
- **online distillation**：2 篇
- **未分类**：1 篇

## 失败模式与风险信号

- 并行分支文本合成计算冗余、效率低，会丢失原生并行结构信息
- 现有Agent护栏未限制推理资源，可被利用陷入长推理循环，引发整个服务系统瘫痪。
- 临时零散工具调用，缺乏状态与技能复用，无法支撑长期持续工作
- 陌生复杂场景泛化能力不足
- 现有评测脱离真实入侵工作流，难以提前发现AI带来的攻击风险
- 手工静态Harness适应性差，新任务需定制，无法利用执行轨迹迭代改进
- 部署后Agent技能无法适配新场景，技能演化缺乏可用的真值反馈
- 本地执行故障无法恢复，无差别调用远程推理导致成本高、延迟大
- 智能体获得环境反馈后仍错误评估自身输出的反思缺口
- 全局信任无法适配能力的技能异质性，跨技能信息借用易被攻击劫持任务路由

## 评测信号

- 该方法在7个数据集上性能匹配或超过基线，剩余两个性能接近，首token生成时间降低2.5倍到11倍
- 攻击可实现13-63倍token放大，真实部署中最高148倍延迟放大，单份投毒即可饱和共享护栏基础设施。
- 提出评测应从静态基准转向沙箱化、可审计、支持自演进的AI生态系统评测范式
- 最优智能体任务成功率仅19.1%，远低于非专家人类的80%以上，凸显复杂真实场景下的显著能力缺口。
- 不同前沿大模型在网页利用、后利用两个阶段的任务解决率，还发现未知漏洞和可绕过防御的变异payload。
- 在25个真实C/C++漏洞样本中，该架构达到44%的漏洞检测准确率，性能与GPT 5.5相当，修复准确率为19%。
- 平均性能提升14.5%，最高达44%，基线性能越低收益越大，性能提升可不依赖模型缩放
- SkillAudit平均任务奖励达73.9%，远高于无技能Agent的40.9%和静态专家技能的56.7%
- 在400次测试中，困难模糊场景成功率从5.0%提升到95.0%，相对手动基线降低16.7%调用量和29.2%token消耗
- 在五个Text-to-SQL基准上，欠置信率从44.4%降至7.7%，任务准确率从75.1%提升至76.5%，双指标均提升

## 控制机制 / Harness 信号

- 通过即插即用的框架，结合缓存校准、微调适配器与知识蒸馏，优化并行智能体分支的合成效率。
- 本文未提出新的Agent行为控制方法，通过构造恶意payload暴露现有Agent护栏的可用性缺陷。
- 通过构建带持久工作区、可复用技能、验证循环与治理的工作站架构，规范agent持续工作行为
- 本文未设计针对智能体行为的控制改进方案，仅通过构建标准化基准评测来暴露当前智能体的能力缺陷。
- 通过构建标准化开放靶场与配套工具链，实现可复现的AI自主网络攻击能力标准化评测。
- 通过划分规划、分析、修复、验证四类角色，构建贴合工业工作流的框架，规范智能体的任务执行流程。
- 构建可组合Harness原语，基于执行轨迹反馈迭代演化更新Harness，提供模型训练信号，闭合迭代循环
- 通过成对轨迹审计分离技能对行为的影响，用PACE生成编辑指引，搭配结构验证器回滚有害更新
- 设计PMR框架将安全关键任务执行保留在本地，通过学习得到的CVI准入门选择性调用外部推理并做安全验证过滤
- 通过对比智能体自身反思与环境实际结果生成免费校准奖励，增强标准强化学习，动态调整系数提升反思校准能力

## 可靠性 / 落地风险

- 仅在公开基准测试验证，未验证对不同底层大模型的适配性，缺少实际工业场景测试
- 工业界常用的共享Agent护栏架构存在可用性漏洞，容易被恶意投毒瘫痪整体服务。
- 仅提出范式框架，缺乏具体实现与实证验证，落地有效性尚未得到确认
- 现有评测无法发现智能体落地真实复杂场景的能力缺陷，容易高估智能体的实际可用能力。
- 当前缺乏标准化可复现的AI网络攻击评测机制，难以提前防控AI带来的新型网络安全风险。
- 仅用25个漏洞样本做实验，样本量较小，所用均为百亿级参数大模型，整体算力成本较高。
- 完整代码暂未开源，实际工程落地的稳定性尚未经公开复现验证
- 未在大规模真实工业场景验证，方法的泛化能力尚不明确
- 仅针对无人机场景验证，方法在通用agent任务的泛化性未验证，工业落地需进一步适配
- 仅在Text-to-SQL任务验证效果，未在更通用的多工具智能体场景验证泛化性

## 可延展 Idea Hook

- 如何将这种缓存级并行合成方法推广到并行工具调用场景，搭建低延迟工业级Agent harness框架？
- 我们可以尝试设计推理资源受限、成本可控的鲁棒Agent护栏，防御这类针对共享护栏的拒绝服务攻击。
- 基于"工作区+技能"范式搭建轻量持久自主Agent，验证其长期任务执行的可靠性
- 可基于GauntletBench测试不同agent harness方案对智能体复杂场景泛化能力的实际提升效果。
- 可基于该开放基准评测开源Agent的网络安全技能，探索安全场景下的Agent行为约束方案。
- 能否构建低算力、符合工业流程的角色分工智能体harness，实现可落地的软件漏洞处理工具？
- 如何基于执行轨迹反馈自动演化适配不同任务的低算力Agent Harness，满足工业场景动态需求？
- 基于SkillAudit的无真值审计思路，探索面向工业部署Agent的在线自动技能演化方案
- 可将本文选择性调用智能体推理的CVI机制推广到通用LLM Agent工具调用场景，降低调用成本提升可靠性
- 能否将这种无额外成本的反思校准方法推广到通用工具使用智能体，提升智能体落地的可靠性
- 如何设计鲁棒的技能条件化信任防御机制，抵御跨技能污染攻击，满足工业异构多智能体任务调度需求。
- 面向工业落地低算力需求，探索基于缓存展开的小参数工具调用智能体训练方案的实际可用性

## 下次可问导师的问题

- 这种基于KV缓存的并行合成方案，能不能适配我们正在研发的低延迟Agent框架？
- 我们是否需要在现有的Agent harness框架中加入推理资源限制，来防范这类拒绝服务攻击？
- 我们是否可以沿着该范式做一个轻量可复现的持久Agent demo来探索方向？
- 我们要不要基于这个新基准测试我们设计的agent harness框架在复杂场景下的能力表现？
- 我们是否可以基于该基准开展开源大模型Agent的网络安全能力评测相关工作？
- 我们是否可以基于该分工思路，裁剪模型得到低成本可演示的漏洞处理智能体？
- 这个基于轨迹自动演化Agent Harness的思路，能不能适配我们要做的低算力工业友好型Agent路线？
- 这种无真值的Agent技能自动演化方案，是否适合我们落地工具调用Agent的需求？
- 这种选择性准入调用机制，是否可以复用在通用Agent工具调用的成本优化场景中？
- 我们是否可以基于该思路，改进工具调用智能体的自我校验能力，做一个低成本可演示方案？
- 我们要不要跟进设计可防御跨技能信任污染攻击的鲁棒多智能体任务路由框架？
- 我们能否基于这个思路复现一个低算力、可演示的本地多轮工具调用智能体Demo？

## 代码资源

- [From Generation to Judgment: Opportunities and Challenges of LLM-as-a-judge](https://github.com/llm-as-a-judge/Awesome-LLM-as-a-judge.) · 556 stars
- [DACO: Towards Application-Driven and Comprehensive Data Analysis via Code Genera...](https://github.com/shirley-wu/daco) · 13 stars
- [GD$^2$PO: Mitigating Multi-Reward Conflicts via Group-Dynamic reward-Decoupled P...](https://github.com/Qwen-Applications/GD2PO.) · 7 stars
- [Benign in Isolation, Harmful in Composition: Security Risks in Agent Skill Ecosy...](https://github.com/saint-viperx/SCR_Bench.) · 6 stars
- [VeriGraph: Towards Verifiable Data-Analytic Agents](https://github.com/ignorejjj/VeriGraph.) · 2 stars
- [Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Sch...](https://github.com/Analytics-Everywhere-Lab/hts.) · 1 stars
- [InvDesMobility: a reliability-gated first-principles feedback framework for clos...](https://github.com/DreamLufei/invDesMobility)
- [Evaluating Second-Order Bias of LLMs Through Epistemic Entitlement](https://github.com/uofthcdslab/second-order-bias.)

## 常见基线方法

- **无技能基线**：2 篇
- **零样本基线**：2 篇
- **基于文本拼接的标准合成方法**：1 篇
- **传统聊天机器人**：1 篇
- **临时工具调用Agent**：1 篇
- **前沿SOTA智能体**：1 篇
- **非专家人类**：1 篇
- **GPT-5.5 with Codex**：1 篇
- **其余五个前沿AI系统**：1 篇
- **GPT 5.5**：1 篇

## 常用数据集

- **SWE-bench Verified**：5 篇
- **GAIA**：3 篇
- **WebArena**：3 篇
- **摘要未提及**：2 篇
- **BFCL**：2 篇
- **数学推理数据集**：1 篇
- **科学问答数据集**：1 篇
- **代码生成数据集**：1 篇
- **多智能体数据库诊断数据集**：1 篇
- **多类Agent基准**：1 篇

---
*自动生成于 2026-06-21 | ArXiv_Daily_Digest*