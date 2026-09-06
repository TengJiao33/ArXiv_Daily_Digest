# Agent Skills 与 Harness — 2026-W36 (08/31-09/06)

本周新增 **154** 篇论文，**14** 篇附带代码。优先级：high 130 / medium 23 / low 1。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AlgoWorlds: Benchmarking Tool Use for Global Optimization in Alg...](http://arxiv.org/abs/2608.29397) | evaluation/benchmark | 当前最优大模型多数情况可产出可行决策，但仅在38.61%案例中达到精确全局最优，多数失败为可... | 构建带可验证全局最优的评测基准，暴露大模型工具使用场景下的全局决策缺陷，提供评测... | 当前大模型在带约束的工业决策场景中难以得到全局最优解，实际落地可... | ✅ |
| 2 | high | - | [Analog-DB: An Agent-First Analog Integrated Circuit Database, Fr...](http://arxiv.org/abs/2609.01286v1) | agent harness | 23个电路工艺绑定全部符合自身记录规范，17个导入尺寸未过测试，经gm/ID循环1-3次迭代... | 通过分层验证框架与模式契约管控设计资源，支持带约束的参数化设计，方便智能体发现与... | 仅完成原理图级验证未涉及布局，距离实际工业流片应用还有一定差距。 | ✅ |
| 3 | high | - | [ChatDev 2.0: A No-Code Multi-Agent Platform for Developing Every...](http://arxiv.org/abs/2609.00714v1) | agent harness | DevAll无需编写任务特定编排代码，就能在三个代表性任务上复现现有SOTA多智能体的有竞争... | 通过声明式可执行图抽象和周期感知执行引擎，实现异构多智能体动态交互的无代码编排控... | 未披露具体评测细节，未验证大规模复杂场景下的平台运行稳定性 | ✅ |
| 4 | high | - | [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in C...](http://arxiv.org/abs/2609.02459v1) | evaluation/benchmark | 即使拥有工具访问权限与明确指引，智能体规划承诺执行率仅为48.2%到65.8%，关键状态监测... | 构建标准化评测基准，通过接口级指标量化智能体工具使用的行为缺陷，为改进提供反馈依... | 属于试点研究样本量小，评测结果统计可靠性不足，尚未适配实际工业任... | ✅ |
| 5 | high | - | [CogEvol: Towards Efficient and Reliable Learning Environment Gen...](http://arxiv.org/abs/2608.30968v1) | skill generation | CogEvol-27B参数仅为旗舰编码模型的1/26.9，仍取得幻灯片质量83.7分、交互式... | 基于生产故障构建验证SFT数据，结合规则与VLM混合奖励驱动GRPO强化学习，提... | 目前仅在AI原生教育场景验证落地，其他场景的通用性与可靠性尚未得... | ✅ |
| 6 | high | - | [Compile, Don't Memorize: A Context Compilation Architecture (CCA...](http://arxiv.org/abs/2609.00759v1) | agent harness | CCA可将Kimi K2.5在CL-bench的任务通过率从15.4%提升至21.4%，性能... | 通过将上下文显式编译为结构化中间表示，搭配可执行验证器与违规门控修正循环，约束输... | 仅在特定基准CL-bench验证，未在更多样的真实工业任务中测试... | ✅ |
| 7 | high | - | [FigMirror: Ground It, Code It, Plot It](http://arxiv.org/abs/2608.28814) | skill generation | 基于坐标的接地测量能够释放大模型的定位编码能力，可有效迁移参考风格到新数据，效果优于像素优化... | 通过接地测量步骤约束智能体行为，定位视觉元素并测量属性，释放大模型已有的定位与编... | 未验证在复杂专业科学图表上的泛化能力，摘要未说明方法的具体算力需... | ✅ |
| 8 | high | - | [Harness-of-Harness: Multi-Day Autonomous Software Development wi...](http://arxiv.org/abs/2609.01481v1) | agent harness | HoH三次迭代后相对对应独立harness平均提升52.25%，最高提升82.86%，可完成... | 在现有编码Agent harness基础上，将开发拆分为可验证小增量，约束输出而... | 依赖多个闭源大模型，未验证低算力小模型效果，工业落地算力成本尚不... | ✅ |
| 9 | high | - | [Learning to Evaluate Before Improving: Automatic Rubric Inductio...](http://arxiv.org/abs/2608.31076v1) | agent harness | 在多个基准中，AutoSciRub跨不同骨干大模型与agent harness均稳定提升，在... | 预先归纳任务专属可执行评分规则，以规则引导智能体科研执行，通过验证识别问题，引导... | 仅在有限科研基准测试验证，未在真实大规模开放式任务中验证泛化与落... | ✅ |
| 10 | high | - | [Learning to Zoom Efficiently with a Contrastive Curriculum](http://arxiv.org/abs/2609.03206v1) | tool-use control | 借助M&C数据集的ROI标签发现，召回率是与放大区域最终任务性能相关性最强的指标，本方法无需... | 通过设计基于对比课程的内在奖励信号，引导多模态大模型学习放大工具使用，无需监督微... | 仅针对视觉领域放大工具场景，方法通用性有待验证，优势是代码公开可... | ✅ |
| 11 | high | - | [MASkills: Continual Skills Optimization for Multi-Agent LLM Syst...](http://arxiv.org/abs/2609.02094v1) | skill optimization | 整合技能持续优化机制的MASkills框架，在HotpotQA、LoCoMo、GAIA三类多... | 通过构建可进化的智能体技能库，结合技能条件信用分配、分层信用聚合与动量平滑优化，... | 未披露具体性能提升幅度，仅验证有效性，缺乏大规模工业场景的落地测... | ✅ |
| 12 | high | - | [SimSkill: A Lifelong Learning AI Agent for Autonomous Mastery of...](http://arxiv.org/abs/2609.03753v1) | skill generation | SimSkill使交通仿真任务验证完成率最高提升25个百分点，过程与语义记忆有互补贡献，效果... | 通过识别能力缺口、动作-评论家循环验证经验，将经验固化为多类记忆构建可复用技能库... | 性能依赖基座模型与计算预算，对不同模型的泛化性不稳定，无法普遍降... | ✅ |

## 方法族分布

- **agent harness**：66 篇
- **evaluation/benchmark**：39 篇
- **skill generation**：10 篇
- **policy optimization**：8 篇
- **multi-agent coordination**：8 篇
- **tool-use control**：7 篇
- **unlearning/safety**：4 篇
- **online distillation**：3 篇
- **survey**：1 篇
- **未分类**：1 篇
- **other**：1 篇
- **skill compression**：1 篇

## 失败模式与风险信号

- 单进程Agent架构下一处故障会中断所有同驻会话，故障影响范围不可控。
- 智能体权限无边界约束、行为不可审计
- 工作上下文持续膨胀，上下文管理工具集不足、探索低效信用分配粗糙
- 工具被静默禁用未调用，模型编造源文本，产生现有指标无法发现的静默故障
- 训练评测脱离真实多轮用户交互场景
- Agent自演化变异不可回滚，原有方法无法成功恢复失败变异。
- 医疗AI Agent研究报告不完备，运行时、治理、可复现性信息严重缺失
- 仅任务语义匹配的技能路由，易选出语义合理但不符合用户约束的不适配技能
- 检索图像上下文丢失、长交互各类调用故障，浪费计算资源干扰策略更新
- 过早披露信息引发动作错误，全量工具信息导致大量无效token消耗

## 评测信号

- 80个会话在故障注入恢复后无重复效应，单故障仅影响对应节点，相比单进程架构故障影响大幅缩小。
- 统计得到插件增长速度、提交类型分布、组件共演化概率，明确了与传统开源软件开发的差异
- 当前领域不同研究的评估方案不具备可比性，现有智能体存在权限无约束、行为不可审计问题
- 在多个不同基模型和多个基准上，ContextPilot均取得更优性能，同时拥有更紧凑的工作上下文
- 原有保真度无法识别静默故障，该方法对207个干净样本零误报，可召回全部50个预设注入故障。
- 摘要未提及具体的量化评测信号与结果，仅介绍了平台的设计思路与协作目标。
- 经PersonaForge训练的智能体综合得分提升4.1%，任务完成和响应质量提升显著，同时交互效率更高。
- 验证了恢复语言扩展与状态寻址均可显著提升恢复率，发现部分效果存在模型依赖性。
- 现有医疗AI Agent研究在运行时架构、治理、可复现性维度的报告不完备率远高于评估维度
- SkillFeed在SkillFeed-Bench上top-1检索精度达75.1%，较基线提升23.1个百分点，轮廓变化场景提升35.1个百分点。

## 控制机制 / Harness 信号

- 通过跨进程架构的Agent线束实现故障隔离，每个插件作为独立进程，仅共享追加式会话记录，限制故障影响范围。
- 本文为实证研究，未提出针对Agent行为的新型控制改进机制，仅分析现有插件生态特征
- 本文为综述研究，梳理现有安全LLM智能体的架构、规划、编排等技术与评估体系
- 通过扩充上下文管理工具集，设计细粒度强化学习信用分配机制，优化智能体主动上下文管理行为
- 通过对工具调用进行调度级日志记录与规则检查，识别工具未调用的静默故障，提升结果可靠性。
- 通过设计专用协作harness与协作机制，支撑多Agent分工协作，支持成果复用，依托证明助手保障证明可被机器校验正确性。
- 通过生成符合真实用户统计的多轮交互模拟数据训练智能体，依托构建的评测基准优化智能体多轮交互表现。
- 通过EvoUndo框架的可恢复性验证、精确状态寻址与扩展恢复语言，约束自演化保障变异可回滚。
- 通过语义本体定义标准化Agent卡，统一规范表示AI Agent，支持报告完整性评估与治理管控
- 通过引入用户轮廓条件约束，构建检索重排序框架，筛选同时满足任务和用户要求的适配技能。

## 可靠性 / 落地风险

- 暂未验证大规模多任务场景的表现，跨进程通信存在额外性能开销，大规模可用性待验证。
- 仅覆盖Claude Code单平台插件生态，结论可推广性缺乏跨平台验证
- 领域评估标准不统一，智能体行为不可审计、权限不明确，落地安全风险不可控
- 仅在公开任务评测，未验证超大规模长周期真实工业任务的效果，未披露算力消耗
- 仅能检测工具未调用类故障，无法检测工具调用后仍出错的情况，仅少量断言可验证。
- 未提供平台实际运行效果的评测验证，实际协作效率与可扩展性尚未得到实证检验。
- 模拟数据对真实用户行为的还原度在域外场景未验证，替代真实数据的可靠性待检验。
- 可恢复效果存在模型依赖性，不同大模型表现不同，增加工业落地适配成本。
- 仅能评估报告完整性，无法评估Agent本身质量与部署就绪度，对工业落地支撑不足
- 依赖清晰完整的用户轮廓输入，评测仅在自建基准开展，泛化能力尚未验证。

## 代码资源

- [ChatDev 2.0: A No-Code Multi-Agent Platform for Developing Everything](https://github.com/OpenBMB/ChatDev.) · 34180 stars
- [FigMirror: Ground It, Code It, Plot It](https://github.com/VILA-Lab/FigMirror.) · 509 stars
- [WANDR: A Benchmark for Wide and Deep Research](https://github.com/perplexityai/wandr.) · 275 stars
- [mimeo: Compiling Public Expert Corpora into Agent Skills and Testing What Transf...](https://github.com/K-Dense-AI/mimeo) · 261 stars
- [CivBench: A Long-Horizon Benchmark for Tool-Mediated Agents in Civilization VI](https://github.com/lmwilki/civ6-mcp) · 157 stars
- [CogEvol: Towards Efficient and Reliable Learning Environment Generation](https://github.com/CogEvol/CogEvol-4B) · 24 stars
- [Learning to Evaluate Before Improving: Automatic Rubric Induction for Automatic ...](https://github.com/zjunlp/AutoSciRub) · 15 stars
- [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Imp...](https://github.com/Flesymeb/HarnessOfHarness) · 6 stars
- [Analog-DB: An Agent-First Analog Integrated Circuit Database, From Blocks to Sys...](https://github.com/MacAnalog/spicexplorer-release.) · 2 stars
- [SimSkill: A Lifelong Learning AI Agent for Autonomous Mastery of Traffic Simulat...](https://github.com/qiliuchn/SimSkill-V1.) · 1 stars

## 常见基线方法

- **未提及具体基线名称**：2 篇
- **单进程参考配置**：1 篇
- **传统开源软件(OSS)开发特征**：1 篇
- **基于专用工具的上下文管理方法**：1 篇
- **传统RL上下文管理方法**：1 篇
- **基于保真度的提取结果评价方法**：1 篇
- **常规修复策略**：1 篇
- **原恢复语言下确定性神谕分析**：1 篇
- **预训练技能路由基线**：1 篇
- **同参数规模开源模型**：1 篇

## 常用数据集

- **OSWorld**：3 篇
- **AgentDojo**：3 篇
- **GAIA**：3 篇
- **ALFWorld**：3 篇
- **SWE-bench Verified**：2 篇
- **Terminal-Bench 2.1**：2 篇
- **摘要未提及**：2 篇
- **LoCoMo**：2 篇
- **Claude Code**：2 篇
- **AppWorld**：2 篇

---
*自动生成于 2026-09-06 | ArXiv_Daily_Digest*