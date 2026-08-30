# Agent Skills 与 Harness — 2026-W35 (08/24-08/30)

本周新增 **170** 篇论文，**8** 篇附带代码。优先级：high 146 / medium 20 / low 4。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [FM-Bench: A Benchmark for Long-Horizon Management with Competing...](http://arxiv.org/abs/2608.18423) | evaluation/benchmark | 模型规模、价格、Token消耗都无法预测长周期表现，现有模型无法学习隐藏价格，自管理内存存在... | 通过构建标准化长周期管理评测基准，以确定性自动计分机制量化智能体的长周期决策能力... | 长周期场景下智能体能力缺陷明显，表现不可预测，自管理内存机制不成... | ✅ |
| 2 | high | - | [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Gover...](http://arxiv.org/abs/2608.21867) | agent harness | 匹配运行时预算下，MemGuard在全部16组骨干-基准设置中最优，WebArena成功率最... | 通过在内存全生命周期持久化保存验证器信号，在各环节管控智能体记忆，提升决策可靠性... | 未提及超长时间任务流落地的存储开销与长期运行稳定性表现 | ✅ |
| 3 | high | - | [Recursive Experiential-Working Memory Evolution for Long-Horizon...](http://arxiv.org/abs/2608.24876v1) | agent harness | 随着交互视野变长该方法优势越大，最长任务上成功率提升达32.2个百分点，常见长视野故障最多降... | 通过经验-工作记忆耦合引导技能按需调用，基于执行证据定位故障，由元智能体完成带验... | 仅在封闭基准完成验证，未在开放真实场景测试，未明确披露方法的额外... | ✅ |
| 4 | high | - | [Risk-Aware Reranking for Agentic Tool Retrieval](http://arxiv.org/abs/2608.22751) | tool-use control | 检索阶段过滤可减少智能体暴露的候选动作空间，能提升相关性与安全性的权衡，可补充下游工具安全保... | 在工具检索阶段加入风险感知重排序，结合规则约束过滤高风险工具，缩小暴露给智能体的... | 风险分级依赖人工标注，当前标注规模有限，跨领域泛化性有待进一步验... | ✅ |
| 5 | high | ICML 2026 | [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reaso...](http://arxiv.org/abs/2608.23493) | policy optimization | 基于Qwen3-8B底座，SRPO仅用规模化监督微调8%的训练FLOPs，就在AIME'24... | 通过引导大模型自生成反思补丁，将稀疏终端监督转为稠密token训练信号，优化智能... | 仅在8B参数小模型上验证，未披露大模型效果，也未测试跨分布泛化性... | ✅ |
| 6 | high | - | [Verify Smarter, Evolve Further: Efficient Harness Evolution thro...](http://arxiv.org/abs/2608.27311v1) | agent harness | 带显式归因的行为感知验证可比基线大幅降低评估预算，同时提升测试集平均留出性能7.6%-13.... | 通过行为感知验证与归因证据门控实现agent harness的自动化进化，选择性... | 仅在有限测试集上验证，未提及大规模真实工业场景下的适配效果。 | ✅ |
| 7 | high | - | [$Z^2$-ACT: End-to-End Verifiable Agentic Intent Control for Open...](http://arxiv.org/abs/2608.21049v1) | agent harness | 该架构在近实时控制场景下，仅带来适度延迟与信令开销，就能有效提升行为过滤能力与对抗攻击韧性 | 通过意图合约编码、对抗意图检查、自管理门控、零知识证明提交实现可验证可审计的安全... | 仅在公开数据集完成评测，缺乏实际多厂商6G网络部署下的长期运行验... | — |
| 8 | high | - | [A Contract-Centered Architecture for Scalable and Manageable Age...](http://arxiv.org/abs/2608.27086v1) | agent harness | 本文尚未完成架构实现与对应实验，暂未获得经过实际测量得出的任何具体研究发现 | 通过组织契约划分各模块权责，依托预注册的能力容量边际约束，管控智能体运行并控制管... | 核心假设未经过验证，无实际实现与评测结果，架构实际落地可行性未知 | — |
| 9 | high | - | [A Policy Algebra for Trust-Preserving Agentic AI Execution](http://arxiv.org/abs/2608.16402) | agent harness | 该策略代数运行时可拦截94.8%的策略违规事件，同时保留86.9%任务完成率，审计完备性达9... | 通过策略代数组合身份、授权、预算等各类约束，运行时干预违规行为，将执行约束在可信... | 未在大规模复杂工业场景验证，未提及方法具体的算力开销与工程落地成... | — |
| 10 | high | - | [A Programming Paradigm for Spatiotemporal Composability](http://arxiv.org/abs/2608.25512v1) | agent harness | 通过统一上下文中介各组件的效应与共效应，可实现不同组件效应交错执行且互不干扰，满足全系统时空... | 通过上下文范式中介所有效应与共效应，用可回滚效应回滚组件副作用，用反应式共效应管... | 仅给出核心框架实现，未在实际大规模Agent场景验证，缺少性能与... | — |
| 11 | high | - | [A survey of reward hacking in agentic large language model syste...](https://www.semanticscholar.org/paper/ffcbc4c0827327a594672ea9e1307f3ca4f24db8) | survey | 智能体大语言模型的奖励黑客会从特征层逐级升级到环境层，需要全流程分层防御而非单点防护 | 提出构建纵深防御架构，从数据、奖励设计到运行监控、治理全流程分层应对奖励黑客问题 | 智能体系统的奖励黑客会引发生产环境不可预测的安全风险，现有单点防... | — |
| 12 | high | - | [ADeptS-Bench: Measuring the Trustworthiness of Computer Use Agen...](http://arxiv.org/abs/2608.26204) | evaluation/benchmark | 现有模型无法同时做到任务成功率超80%、攻击成功率低于30%，普遍存在误操作和过度拒绝偏差。 | 本文通过构建结构化评测基准识别现有计算机使用智能体的安全缺陷，为智能体安全优化提... | 现有计算机使用智能体安全缺陷突出，误操作风险高，安全性远达不到实... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **agent harness**：72 篇
- **evaluation/benchmark**：43 篇
- **tool-use control**：14 篇
- **survey**：12 篇
- **unlearning/safety**：8 篇
- **policy optimization**：7 篇
- **skill generation**：5 篇
- **multi-agent coordination**：4 篇
- **agent harness, evaluation/benchmark**：2 篇
- **other**：1 篇
- **model steering**：1 篇
- **reward learning**：1 篇

## 失败模式与风险信号

- 自然语言工作流依赖隐式，智能体执行一致性差、长分支指令遵循失败
- 训练碎片化，同轨迹动作权重统一，技能引导会对部分决策造成干扰，降低模型性能
- 现有大模型无法从发明人非正式披露生成完整合法一致的专利申请
- 异构Agent对规范的解释不一致，跨Agent规范转移存在严重性能退化
- 单智能体架构无法承载需要异构专长、多子任务协作的复杂任务需求。
- 功能与安全评估割裂，评测存在多种有效性威胁
- 恶意技能劫持Agent，变换形式绕过单阶段防护，跨工具多轮发起攻击
- LLM辅助Agent动作不精确、侵入式采集带来运行安全风险
- 现有评测方法与人类判断不对齐，无法准确衡量药物发现智能体输出质量
- 不可信模型输入导致控制不安全、验证审计不完备，无法满足多厂商场景需求

## 评测信号

- 相较于原始自然语言工作流，编译后任务解决率提升28个百分点，跨模型一致性升32个百分点，重复执行一致性升56个百分点。
- 统计得到不同作者-评审者产品配置下AI评审输出的差异，产出了多维度的AI对AI评审实证数据
- 在三个公开基准上，AUSO相比竞争基线，在智能体性能和分布外泛化能力上都获得了一致提升。
- 在Dis2Pat基准上对比不同模型生成性能，验证Patent-MAF优于开源模型，性能可媲美闭源大模型。
- 跨Agent规范转移存在显著Agent依赖的性能退化，检索增强摄入是唯一在多Agent帕累托前沿均存在的有效策略。
- 本文为综述研究，未开展实证评测，仅汇总整理了该领域的相关论文、数据与开源项目。
- 指出现有智能体评测存在弱测试预言、数据泄漏、harness不固定、未充分报告预算与人工干预等问题。
- ClawSentry可大幅降低恶意攻击成功率，对合法技能的正常任务成功率影响极小，可适配多主流Agent框架。
- 在真实Windows工作站测试得到两个CS2轨迹均无丢失ETW缓冲区与事件，证明生成的轨迹完整可审计。
- 核心关注评测裁判与人类专家判断的对齐度，优化后对齐度从0.80提升至0.86，验证了框架有效性。

## 控制机制 / Harness 信号

- 通过编译将隐式自然语言工作流转换为显式声明工件读写、约束和控制流的工作流，经约束优化细化复杂步骤提升可靠性。
- 本文为AI对AI代码评审的实证评测研究，通过构建大规模数据集统计分析不同代理配置的评审行为特征
- 采用分阶段渐进优化，在动作层面评估技能价值，按对决策的收益调整更新强度，引导技能从内化到利用转变。
- 构建多智能体框架实现可本地部署的专利撰写，提出基准数据集与基线方法评测模型的专利撰写能力。
- 通过实证分析明确跨Agent规范转移问题，指出检索增强摄入可获得更优的跨Agent开发性能。
- 通过构建显式动态演化图结构抽象任务、智能体与系统状态，组织协调异构多智能个体。
- 通过提出多维度保证框架与跨研究比较的最小报告协议，规范智能体评估流程。
- 分四个风险位点做渐进式多层检测，通过Agent束协议统一适配多框架，无需修改Agent内部实现。
- 采用证据门控事务机制，结合人在环审核，对每个动作做风险验证，设置证据不足时的停止条件。
- 构建人类对齐的大语言模型裁判，定义标准化评测维度，为药物发现智能体提供可靠评测依据。

## 可靠性 / 落地风险

- 仅在有限真实领域样本测试，未提及大规模落地的算力开销与跨领域适配成本
- 研究仅为现象统计，未构建可控AI评审框架，结论外部有效性有待进一步验证
- 摘要未明确说明方法的算力消耗与可复现细节，缺乏面向工业场景的适配验证。
- 新构建数据集覆盖场景有限，方法未经过真实工业专利撰写场景的落地验证。
- 异构多Agent开发中规范不具备通用可移植性，会降低多Agent软件工程流程的可靠性。
- 仅提出范式框架并做综述梳理，未提供落地实现与实测验证，实际效果尚不明确。
- 现有研究评测不规范，可复现性差，功能安全割裂，难以支撑工业级可靠落地。
- 未在大规模工业生产级Agent场景验证效果，未提及实际部署的额外运行开销。
- 仅在单工作站单应用测试，未验证实际诊断效果，泛化性有待验证。
- 依赖闭源大参数量大模型作为裁判，落地成本较高，泛化性有待进一步验证。

## 代码资源

- [EMRB: A Multi-Level Benchmark for Evaluating LLM Reasoning over Raw Electromagne...](https://github.com/mingxuZhang2/EMRB) · 110 stars
- [FM-Bench: A Benchmark for Long-Horizon Management with Competing Agents](https://github.com/Analogy-AI/fm-bench.) · 18 stars
- [Recursive Experiential-Working Memory Evolution for Long-Horizon Agent Harnesses](https://github.com/Gen-Verse/Recuris) · 5 stars
- [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance](https://github.com/whyyyyy123/MemGuard.) · 2 stars
- [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning](https://github.com/Galleons2029/SRPO) · 2 stars
- [Risk-Aware Reranking for Agentic Tool Retrieval](https://github.com/qli447/risk-aware-tool-retrieval-release.) · 2 stars
- [AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design](https://github.com/lmqfly/AgentFold.) · 1 stars
- [Verify Smarter, Evolve Further: Efficient Harness Evolution through Behavior-Awa...](https://github.com/jhxu5214/HarnessLens.)

## 常见基线方法

- **Claude Code**：3 篇
- **提示工程**：2 篇
- **原始自然语言工作流**：1 篇
- **开源大语言模型**：1 篇
- **闭源大语言模型**：1 篇
- **直接使用原生规范**：1 篇
- **压缩规范转移**：1 篇
- **重写规范转移**：1 篇
- **上下文工程**：1 篇
- **线束工程**：1 篇

## 常用数据集

- **摘要未提及**：8 篇
- **ALFWorld**：5 篇
- **WebShop**：4 篇
- **Terminal-Bench 2.0**：3 篇
- **AppWorld**：3 篇
- **AgentDojo**：3 篇
- **SWE-bench Verified**：3 篇
- **OpenClaw**：2 篇
- **MATH-500**：2 篇
- **BFCL**：2 篇

---
*自动生成于 2026-08-30 | ArXiv_Daily_Digest*