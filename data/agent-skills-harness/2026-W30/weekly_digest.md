# Agent Skills 与 Harness — 2026-W30 (07/20-07/26)

本周新增 **87** 篇论文，**7** 篇附带代码。优先级：high 69 / medium 14 / low 4。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Agentic coding without the cloud: evaluating open-weight large l...](http://arxiv.org/abs/2607.21482v1) | evaluation/benchmark | 消费级硬件上运行的31-35B参数开放权重大模型，在该基准平均任务完成率最高达87.9%，接... | 构建标准化评测基准框架，对开放大模型驱动的智能体完成任务的效果进行量化评估 | 仅在特定纵向数据准备任务上验证，未测试更多通用场景，模型泛化能力... | ✅ |
| 2 | high | - | [ArbiGraph: Arbitrarily Scalable Verifiable Task Graphs for Evalu...](http://arxiv.org/abs/2607.20764v1) | evaluation/benchmark | Qwen3.5-27B工具辅助智能体在孤立任务准确率高，分支链式依赖数学任务准确率最高降33... | 通过生成参数可控、可自动验证的任务图，为智能体上下文管理评测提供可复现的反馈基准... | 仅评测单个模型，覆盖范围有限，仅为评测基准，未提出改进智能体能力... | ✅ |
| 3 | high | - | [Knowledge-Centric Self-Improvement](http://arxiv.org/abs/2607.19592v1) | agent harness | 该方案在三类基准上相比基线提升解决率同时降低成本，蒸馏得到的知识可跨不同LLM家族迁移。 | 将改进限定在持久化共享知识库层面，收集智能体任务洞见后蒸馏知识，实现可迁移的行为... | 未在大规模真实工业任务上验证，共享知识库的错误累积风险未做相关分... | ✅ |
| 4 | high | - | [PEARL: Auditable Repair for Scientific Reasoning Graph Extractio...](http://arxiv.org/abs/2607.17917v1) | agent harness | PEARL将大语言模型科学推理图的严格通过率从0/350提升至300/350，平均REA从0... | 通过无训练修复层，基于证据的法官反馈校验修复LLM生成的推理图，输出符合语义规范... | 仅在科学推理图提取任务验证，尚未验证其在通用Agent任务中的通... | ✅ |
| 5 | high | - | [SciForge: An AI-Native, Multimodal Workbench for Scientific Disc...](http://arxiv.org/abs/2607.16038v1) | agent harness | 模块化人机分工的agent工作流可支撑多类科学发现任务，已完成多日agent驱动的基因发现等... | 通过模块化服务设计、目标决策治理、证据追溯机制约束agent行为，实现人机协作科... | 未在标准公开基准上做对比验证，当前团队协作能力不足，缺乏大规模落... | ✅ |
| 6 | high | - | [pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architect...](http://arxiv.org/abs/2607.21268v1) | agent harness | 引入门控架构后，平均故障严重程度从1.58降至1.16，整体可用性从2.60升至3.10，5... | 通过门控机制诊断故障并触发回滚，保留人类对高成本不可逆决策的控制权，协调多智能体... | 依赖人工参与决策与评估，可扩展性不足，难以支撑大规模的落地应用 | ✅ |
| 7 | high | - | [(Over)Reliance on Test Agents in AI-Assisted Software Testing](http://arxiv.org/abs/2607.17927v1) | evaluation/benchmark | AI辅助软件测试中对测试Agent的过度依赖同时属于认知控制流失的代理问题与测试保障失效的保... | 提出过度依赖分析框架，收集测试Agent工作流中的依赖数据，识别过度依赖模式，支... | 缺少对测试Agent过度依赖的管控机制，易导致测试失效，给工业软... | — |
| 8 | high | - | [AREX: Towards a Recursively Self-Improving Agent for Deep Resear...](http://arxiv.org/abs/2607.21461v1) | agent harness | 带自主上下文压缩的递归自改进框架，可让同规模智能体在多个深度研究基准取得远超基线的性能 | 通过双层循环交替答案生成与逐约束验证，用自主上下文压缩维护长程状态，稠密奖励引导... | 训练依赖高质量轨迹与长程强化学习，大参数量版本对硬件算力有一定要... | — |
| 9 | high | - | [AgentDebugX: An Open-Source Toolkit for Failure Observability, A...](http://arxiv.org/abs/2607.18754v1) | agent harness | DeepDebug在Qwen3.5-9B上精确归因准确率达28.8%，比最强单遍基线高7.1... | 构建闭环调试harness框架，通过结构化多轮根因分析定位故障，实现故障恢复，支... | 仅在公开学术基准完成验证，未提及大规模工业场景下的落地稳定性表现... | — |
| 10 | high | - | [AgentLTL: A Trace-Verification Framework for Measuring, Enforcin...](http://arxiv.org/abs/2607.02599) | agent harness | 该框架微调在含 unseen工具别名的未见过模式上，准确率和合规性分别提升38、17.5个百... | 基于一阶线性时序逻辑定义程序规则，可在线门控工具调用、离线给轨迹打分，也可将分数... | 依赖人工编写一阶线性时序逻辑形式的程序规则，复杂场景下规则编写成... | — |
| 11 | high | - | [AgentTrails: Towards Trust and Reuse for Agentic Tasks](http://arxiv.org/abs/2607.18816v1) | agent harness | 基于起源图的轨迹表示可有效揭示隐藏依赖，对齐不同执行，发掘时序日志中隐藏的重复工具使用模式。 | 通过构建结构化起源图建模工具调用与数据依赖，支撑智能体执行的可理解、调试与复用。 | 仅做定性演示，无定量评测，方法通用性未在标准基准上验证。 | — |
| 12 | high | - | [Agentic Real2Sim: Physics-based World Modeling with Vision-Langu...](http://arxiv.org/abs/2607.19190v1) | agent harness | 采用开放权重VLM作为智能体后端，成本仅为前沿模型的很小一部分，却能达到与之相当的实转仿转换... | 通过开放权重VLM驱动智能体自动化实转仿全流程，替代人工调整与流程粘合，降低转换... | 仅在三类实验场景完成验证，未开展大规模工业场景测试，落地能力有待... | — |

## 方法族分布

- **agent harness**：40 篇
- **evaluation/benchmark**：22 篇
- **skill generation**：5 篇
- **survey**：3 篇
- **unlearning/safety**：3 篇
- **multi-agent coordination**：2 篇
- **tool-use control**：2 篇
- **other**：2 篇
- **policy optimization**：2 篇
- **factuality benchmark**：2 篇
- **未分类**：1 篇
- **online distillation**：1 篇

## 失败模式与风险信号

- 现有LLM代码助手解释忽略用户个体差异，工作流割裂，干扰开发者正常开发
- 自主数据科学智能体试错工作流计算成本高昂
- 模仿学习记忆静态线索，对未知机器人操纵任务泛化能力不足
- 现有LLM生成工作流结构脆弱、缺乏经验知识，执行成功率低
- 现有FAIR评估工具评分分歧大，无法处理JS渲染页面与仓库特定标识符，一致性差
- 智能体贡献生成速度远超维护者风险评估能力，开源项目AI治理规则碎片化
- 模型与Harness交互产生的隐性响应型缺陷，难以检测与复现
- 大规模动态环境中长周期工具使用鲁棒性差、有效性不足
- 开源智能体技能碎片化、冗余、质量不均，现有开放生态难以直接服务真实任务
- 预构建Harness持续更新成本高昂、劳动密集，难以兼顾性能与训练轨迹质量。

## 评测信号

- 评测前沿大模型在商业分析性知识工作上的表现，观测同一模型家族两年间的能力提升幅度。
- 通过八个真实场景案例验证了系统可支撑多类科学研究任务的完整运行，具备实际应用价值。
- 对照实验结果显示，使用TARS完成代码理解任务速度提升26%，用户认知负荷更低，对解释适配性评价更好。
- 训练加速约14倍，搜索推理加速3~6倍，转移预测精度比最强LLM基线高35.6%，同时保持 competitive 任务性能。
- 在可见任务直接推理和未知任务少样本微调场景下，模型性能均优于当前最优基线方法。
- 实验显示所提方法生成的工作流节点多样性更高、结构更连贯，执行成功率优于现有同类方法
- 加入批评代理后子原则评估一致性从71%提升至89%，与专家共识对齐度达82%，单数据集评估成本仅0.054美元。
- AGM大幅提升风险标签恢复率与评审感知支持度，贡献方提交的治理包结构合格率超九成。
- 不同于仅关注最终任务结果，该研究重点关注智能体过程层面的行为，包括工具执行、故障恢复、运行时等
- 多数AR缺陷为无明确测试预言的静默错误，大模型随机性导致可复现性差，用户与开发者对缺陷归因存在错位。

## 控制机制 / Harness 信号

- 本文梳理了5G/6G网络中控制、管理与AI原生平面，将大模型智能体能力映射到网络控制面。
- 本文为基准评测研究，未针对模型或智能体行为设计特定的控制与改进机制。
- 通过模块化服务设计、目标决策治理、证据追溯机制约束agent行为，实现人机协作科研工作流。
- 通过轻量级心智理论建模开发者特征，调整生成解释的深度与语气，实现适配开发者需求的智能体行为控制。
- 通过成本感知路由分配操作，结合轻量实际执行与LLM模拟，用误差感知强化学习优化世界模型，降低计算开销。
- 构建融入动力学信息的共享技能空间，通过多模块调制任务特征，引导智能体学习任务底层逻辑。
- 通过知识蒸馏提取分层知识，监督微调注入知识，推理阶段用自优化改进生成结构，提升可执行性
- 增设批评代理作为校验器，检查评估证据与结果一致性，可发起针对性重评估，提升评估一致性。
- 提出仓库托管的双向治理契约AGM，连接贡献方证据准备与维护方验证，明确权责以管控智能体贡献风险。
- 基于过程层行为评测得到的失败模式反馈，优化工具配置与动态工具选择，改进智能体设计

## 可靠性 / 落地风险

- 仅为综述梳理，未给出可复现、可落地的工业级智能体控制实现方案。
- 评测基于商学院教学案例，未验证与真实工业场景商业工作的匹配度，缺乏落地验证。
- 未在标准公开基准上做对比验证，当前团队协作能力不足，缺乏大规模落地测试。
- 仅开展18人小规模用户实验，缺乏大规模工业场景下的有效性验证。
- 仅在自建数据集验证，未在真实大规模工业数据科学场景测试，泛化性待验证。
- 未明确披露方法算力需求与可复现信息，工业落地适配的成本尚不清晰。
- 未公开具体数据集与实验细节，可复现性未验证，工业落地效果有待测试
- 仅在单模型族验证，基准规模较小，消融实验不完整，方法泛化性结论支撑不足。
- 依赖人工评审，大规模场景下的可扩展性未验证，自动化治理能力尚未明确。
- 仅在单一信息抽取任务验证，未测试更多通用场景，结论的通用性有待进一步验证

## 代码资源

- [pAI-Econ-claude: A Gated Human-in-the-Loop Multi-Agent Architecture for AI-Assis...](https://github.com/maxwell2732/pAI-Econ-claude.) · 134 stars
- [Metacognition in LLMs: Foundations, Progress, and Opportunities](https://github.com/yale-nlp/LLM-Metacognition.) · 44 stars
- [SciForge: An AI-Native, Multimodal Workbench for Scientific Discovery](https://github.com/AGI4Sci/SciForge) · 31 stars
- [Knowledge-Centric Self-Improvement](https://github.com/recursive-knowledge/KSI.) · 14 stars
- [PEARL: Auditable Repair for Scientific Reasoning Graph Extraction](https://github.com/BohanSu/auditable-repair-reasoning-graphs) · 1 stars
- [Agentic coding without the cloud: evaluating open-weight large language models o...](https://github.com/UCL-ARC/RRBench.) · 1 stars
- [ArbiGraph: Arbitrarily Scalable Verifiable Task Graphs for Evaluating Context Ma...](https://github.com/pavelgolikov/ArbiGraph.git)

## 常见基线方法

- **Claude Code**：2 篇
- **最强大语言模型基线**：1 篇
- **现有SOTA基线方法**：1 篇
- **现有大语言模型工作流生成方法**：1 篇
- **现有公开FAIR合规性评估工具**：1 篇
- **现有提升智能体可读性可追溯性的方案**：1 篇
- **无项目统筹的原生治理方案**：1 篇
- **固定LLM工作流基线**：1 篇
- **最大推理量设置基线**：1 篇
- **原始低推理量智能体基线**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **QwenClawBench**：2 篇
- **ARC-AGI-3**：2 篇
- **BusinessCaseBench**：1 篇
- **Visual Studio Code**：1 篇
- **非平凡Java代码片段**：1 篇
- **8K规模数据科学操作转移轨迹数据集**：1 篇
- **仿真环境**：1 篇
- **真实世界机器人操作场景**：1 篇
- **ComfyUI领域真实工作流集合**：1 篇

---
*自动生成于 2026-07-26 | ArXiv_Daily_Digest*