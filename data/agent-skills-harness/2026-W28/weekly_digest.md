# Agent Skills 与 Harness — 2026-W28 (07/06-07/12)

本周新增 **86** 篇论文，**6** 篇附带代码。优先级：high 68 / medium 15 / low 3。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AgentLens: Production-Assessed Trajectory Reviews for Coding Age...](http://arxiv.org/abs/2607.06624v1) | evaluation/benchmark | 仅做任务通过与否的二元评估无法支撑生产诊断，全轨迹评估可有效识别代码智能体的产品回归问题。 | 通过提出带全轨迹评审的评估基准，为代码智能体行为优化提供反馈，支撑生产侧回归检查... | 轨迹评审依赖大语言模型，存在评审结果不一致，影响评估稳定性的潜在... | ✅ |
| 2 | high | - | [Auto: The AGI Compiler](http://arxiv.org/abs/2607.04542v1) | skill generation | 87.1%的前沿Agent行为片段是可观测确定性的，可将单任务边际成本从59微美元降至2微美... | 将Agent确定性行为提取编译为带沙箱验证的可执行技能，防护不匹配时回退原Age... | 防护校准难度大，存在静默错误风险，回退失败后无法重编译修复问题。 | ✅ |
| 3 | high | - | [Cognitive-structured Multimodal Agent for Multimodal Understandi...](http://arxiv.org/abs/2607.08497v1) | agent harness | 8B参数模型在20轮会话上检索准确率达91.4%，超过32B基线8.2个百分点，单轮推理时间... | 通过模块化认知结构、外部化情景记忆实现可扩展控制，推出工具增强的CMA-Harn... | 仅在自制基准验证，未在大规模真实工业场景进行充分测试。 | ✅ |
| 4 | high | - | [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Ag...](http://arxiv.org/abs/2607.04528v1) | agent harness | 受限行动、压缩修复等harness操作可保留终端任务成功，却会改变驱动智能体后续决策的信念。 | 提出无训练BIWM协议，通过规范观测、记录分支、影子执行风险分支，对齐不同har... | 忽略harness对信念的影响会导致评估结果不可靠，不同部署ha... | ✅ |
| 5 | high | - | [UniClawBench: A Universal Benchmark for Proactive Agents on Real...](http://arxiv.org/abs/2607.08768v1) | evaluation/benchmark | 基础模型本身的能力与智能体框架的设计，会共同影响主动智能体在真实世界任务上的表现。 | 通过能力维度拆解的评测基准结合闭环多智能体评测机制，实现对主动智能体真实表现的精... | 未明确披露评测过程的算力开销，面向工业场景的适配成本尚不清晰。 | ✅ |
| 6 | high | - | [ACE: Agentic Control for Embodied Manipulation via Zero-shot Wor...](http://arxiv.org/abs/2607.04162v1) | agent harness | 显式工作流推理加掩码控制的ACE，方程构造成功率50%、约束检索成功率70%，大幅优于表现不... | 通过显式工作流推理、掩码介导接口桥接推理与执行，依托闭环子目标验证实现控制，支持... | 仅在桌面简单操纵任务验证，未在复杂真实工业场景测试，泛化能力待验... | — |
| 7 | high | - | [AgentTether: Graph-Guided Diagnosis and Runtime Intervention for...](http://arxiv.org/abs/2607.06273v1) | agent harness | 在最难的Banking领域，AgentTether可修复59.04%Qwen3.7-max、... | 作为无需修改原有智能体的包装层，通过图诊断错因，结合修复记忆生成行为约束指导，实... | 仅在有限规模基准上测试，跨不同任务和智能体架构的泛化性未充分验证 | — |
| 8 | high | - | [Agentic AI and Retrieval-Augmented Models in Straight-Through Un...](http://arxiv.org/abs/2607.07858v1) | agent harness | 结合定向检索、第三方校验和多步规则评估的Agentic RAG，在多步骤、信息缺失场景提升最... | 通过结构化检索、显式多步规则评估、第三方数据校验约束智能体决策，保障决策透明可审... | 仅在合成实验环境验证，未使用真实工业业务数据测试，落地有效性待验... | — |
| 9 | high | - | [AgenticPD: A Stage-Aware Agentic Framework for Physical Design Q...](http://arxiv.org/abs/2607.04758v1) | agent harness | 基于阶段划分的智能体框架可复用中间检查点避免全流程重跑，获得更优布线后时序，功耗面积仍保持竞... | 通过阶段感知的智能体harness管理观测、执行历史与上下文，划分不同智能体职责... | 仅针对EDA物理设计特定场景，未提及方法通用性，也未说明开源可复... | — |
| 10 | high | - | [Akashic: A Low-Overhead LLM Inference Service with MemAttention](http://arxiv.org/abs/2607.05708v1) | agent harness | 上下文分块加协同内存放置，最高提升任务准确率10.2个点，吞吐量提升1.21倍，可持续请求率... | 通过低开销上下文分块内存管理与软硬件协同优化，降低推理开销，提升智能体服务效率与... | 未披露具体公开基准与实现细节，复现性不明确，缺乏真实工业场景验证... | — |
| 11 | high | - | [Articulating Assumptions in AI-Generated Scientific Analyses thr...](http://arxiv.org/abs/2607.05762v1) | multi-agent coordination | 模块化任务分解相比传统单提示方法，提升了分析的透明度与可靠性，还支持小尺寸模型完成完整工作流... | 通过模块化任务拆分，将不同功能分配给独立智能体，加入初始指令歧义校验，提升输出透... | 仅在对撞机物理领域完成验证，方法在其他领域的通用性尚未得到充分验... | — |
| 12 | high | - | [ArtisanCAD: An Industrial-Level CAD Agent with Expert-Grounded K...](http://arxiv.org/abs/2607.05750v1) | skill generation | 引入CAD-IR蒸馏专家知识后，在Text2CAD基准上将中间提示生成的平均倒角距离从14.... | 通过CAD-IR编码参数、操作依赖与验证规则，蒸馏专家知识得到可复用参数化技能，... | 依赖专家过程标注数据，绑定CATIA特定后端，对其他CAD工具通... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **agent harness**：32 篇
- **evaluation/benchmark**：18 篇
- **skill generation**：8 篇
- **unlearning/safety**：6 篇
- **tool-use control**：6 篇
- **multi-agent coordination**：5 篇
- **survey**：4 篇
- **online distillation**：2 篇
- **policy optimization**：2 篇
- **reward learning**：1 篇
- **未分类**：1 篇
- **other**：1 篇

## 失败模式与风险信号

- 无筛选工具检索引入噪声，生成器对未知开放内容产生幻觉
- 单VLA模型难以处理长周期任务，分层方法存在规划与执行的语义鸿沟
- 变分自动化工业任务中，无模型策略存在可靠性缺口，无法满足持续执行要求
- 现有评测忽略用户主权约束，易引发隐私泄露、同意侵犯、智能体被操纵等问题
- 现有自改进非递归，仅优化任务技能，改进流程固定，无法适配多样任务
- 网页可信与不可信内容结构纠缠，破坏安全防御的信任边界，导致可证明的提示注入防御失效。
- 持久化Agent的长期记忆易被不可信内容隐形注入污染，引发长期安全威胁。
- 早期错误传播、缺陷掩盖
- 原多轮OPD的高训练成本、前缀陷阱引发的双边分布偏移
- 忽略物理设计流程阶段特性，优化需全流程重跑，导致优化评估成本过高

## 评测信号

- 前沿开放生成器在该基准得分仅21-28分，较正常水平下降40分，无筛选搜索会引入噪声降低生成效果。
- 在Libero-long和RoboTwin上性能分别超出整体基线3.1%和4.1%，可零样本完成真实世界未知长周期任务。
- 在8个新增开放变分自动化任务基准上，GaP的任务成功率相比基线方法获得了显著提升。
- 除任务完成情况外，重点评测隐私泄露、同意违规、过度让步、被操纵捕获等损害用户主权的问题。
- 在三个基准上对比多种基线，评测智能体处理长程开放任务的留存准确率，得到明确的准确率提升数值。
- 摘要未提及具体评测结果与性能指标，仅公开了所提方法的实现代码。
- MemGhost攻击成功率高，可跨不同Agent架构和记忆后端迁移，对现有多层面防御仍保持有效。
- 生成错误代码后再生成测试的故障检测率仅14%，远低于独立生成的25%，错误传播普遍存在，大幅降低测试可靠性。
- 在基准ODE与PDE任务验证，PDEFlow可完成全流程工作，输出有效无求解器预测，适配低人工干预场景
- 任务完成率91.8%，安全关键子集合规率96.0%，单次预约成本0.0324美元，相比人工成本显著降低。

## 控制机制 / Harness 信号

- 通过教后搜索协同训练框架自动识别生成器的动态知识边界，构建了可复现的工具增强生成测试harness。
- 通过双向对齐接口传递可执行子任务，标准化技能基元，推理阶段设计适配任务上下文与技能约束的harness工程。
- 基于模块化开放机器人技能库生成图结构策略，通过并行仿真推演迭代优化，提升任务执行可靠性。
- 通过构建标准化评测基准，从用户主权维度评估智能体行为，推动满足约束要求的个人智能体优化。
- 通过双时标双循环演化机制，分别演化任务技能与元改进技能，共享单个冻结主干优化智能体行为。
- 通过在输入到智能体前掩码不可信内容，结合沙箱接口严格权限分离，重建信任边界，隔离agent与对抗内容。
- 本文构建完整评测基准评估隐形记忆注入攻击的有效性，验证主流持久化Agent架构存在该安全风险。
- 本文为实证研究，通过控制不同提示策略、多步工作流场景分析错误传播对测试可靠性的影响。
- 通过模块化全流程设计与注册表接口管控，将自然语言输入转化为验证后的规约，保障流水线可复现可扩展
- 通过分层确定性安全护栏严格限定任务范围，禁止违规医疗行为，对安全关键场景采用确定性短路机制管控风险。

## 可靠性 / 落地风险

- 知识边界与特定生成器绑定，更换模型需重新训练发现边界，适配成本相对较高。
- 仅在操纵领域验证效果，未在更多类型任务测试泛化能力，依赖预训练大模型。
- 仅在自建基准测试验证，未经过大规模真实工业场景的充分落地测试。
- 操纵行为判断存在主观性，人工评测一致性低，可能影响基准评测结果的稳定性。
- 递归演化过程缺少显式约束，技能结果可解释性不足，工业场景下回滚调试难度较高。
- 未提供实际场景评测结果，方法的实际防护效果与性能开销未验证，存在落地不确定性。
- 持久化个人Agent的长期记忆存在隐形注入漏洞，可被长期利用控制Agent，威胁用户数据安全。
- LLM驱动的编码Agent工作流存在错误相互掩盖问题，易漏检缺陷，会影响交付软件的质量。
- 仅在公开基准任务验证效果，未测试大规模实际工程问题，框架通用性与鲁棒性待验证
- 仅在自建基准测试，未经过真实医疗生产环境验证，存在实际落地的合规安全风险。

## 代码资源

- [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://github.com/HKU-MMLab/UniClawBench.) · 6 stars
- [Cognitive-structured Multimodal Agent for Multimodal Understanding, Generation, ...](https://github.com/caseclose/cma-harness) · 5 stars
- [Auto: The AGI Compiler](https://github.com/RightNow-AI/auto) · 4 stars
- [Multi-agent Autoformalization of Tensor Network Theory](https://github.com/LionSR/TNLean) · 3 stars
- [AgentLens: Production-Assessed Trajectory Reviews for Coding Agent Evaluation](https://github.com/agent-lens/agent-lens-bench.) · 1 stars
- [Measuring Harness-Induced Belief Divergence in Multi-Step LLM Agents](https://github.com/Hik289/Harness-induce-bias.git.)

## 常见基线方法

- **无技能基线**：2 篇
- **朴素搜索**：1 篇
- **前沿开放视觉生成器**：1 篇
- **整体式单模块基线**：1 篇
- **直接法**：1 篇
- **仅记忆基线**：1 篇
- **仅同意约束基线**：1 篇
- **仅证据基线**：1 篇
- **ReAct工具使用基线**：1 篇
- **安全提示基线**：1 篇

## 常用数据集

- **ALFWorld**：2 篇
- **BFCL**：2 篇
- **SearchGen-20K**：1 篇
- **SearchGen-Bench**：1 篇
- **SearchGen-Corpus-1M**：1 篇
- **Libero-long**：1 篇
- **RoboTwin**：1 篇
- **仿真变分自动化任务基准**：1 篇
- **真实世界变分自动化任务基准**：1 篇
- **SovereignPA-Bench**：1 篇

---
*自动生成于 2026-07-12 | ArXiv_Daily_Digest*