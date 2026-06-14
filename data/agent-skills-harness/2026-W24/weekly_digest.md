# Agent Skills 与 Harness — 2026-W24 (06/08-06/14)

本周新增 **210** 篇论文，**20** 篇附带代码。优先级：high 153 / medium 44 / low 13。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 控制/评测 | 风险 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|------|-----------|:----:|
| 1 | high | - | [$τ$-Rec: A Verifiable Benchmark for Agentic Recommender Systems](http://arxiv.org/abs/2606.10156v1) | evaluation/benchmark | 通过可验证奖励和揭示标签询问机制控制对话过程中任务约束的呈现，依托基准评测智能体... | 现有评测无法准确衡量智能体推荐可靠性，实际部署中智能体推理一致性... | 基于该可验证基准，能否设计低算力、高可靠的工业级对话推荐智能体harness控制框架？ | ✅ |
| 2 | high | - | [Act As a Real Researcher: A Suite of Benchmarks Evaluating Front...](http://arxiv.org/abs/2606.07462) | evaluation/benchmark | 通过构建针对性评测基准暴露现有研究型智能体的缺陷，为后续改进智能体提供方向。 | 仅推出评测基准未给出改进方案，当前研究型智能体可靠性远不满足实用... | 能否设计轻量agent harness机制，弥补研究型智能体遗漏细粒度关键细节的缺陷，提升其... | ✅ |
| 3 | high | - | [Agent Skill Evaluation and Evolution: Frameworks and Benchmarks](http://arxiv.org/abs/2606.11435v1) | survey | 通过系统性梳理现有技能演化范式与基准，梳理领域缺口，为技能优化评估提供参考框架。 | 作为综述未开展实证验证，现有领域基准存在结构缺口，落地参考性存在... | 针对该综述指出的基准缺口，可构建面向低算力工业场景的可复现智能体技能评测基准。 | ✅ |
| 4 | high | - | [AutoMegaKernel: A Statically-Checked Agent Harness for Self-Reta...](http://arxiv.org/abs/2606.09682v1) | agent harness | 通过静态调度IR验证器在kernel启动前检查死锁与竞态，提前拒绝不安全的Age... | 仅支持Llama系列模型，仅在推理类GPU上性能占优，适用场景有... | 可将本文静态提前拒错的思路，迁移到通用Agent工具调用的安全harness设计中 | ✅ |
| 5 | high | - | [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent ...](http://arxiv.org/abs/2606.12344v1) | evaluation/benchmark | 通过设计统一适配协议与评测基准，规范异构agent harness的评测流程，实... | 新基准尚未经大规模第三方验证，成本差异可能增加工业落地选型的复杂... | 能否基于Claw-SWE-Bench，优化出低算力低成本、符合工业要求的高性能编码agent... | ✅ |
| 6 | high | - | [Demo2Tutorial: From Human Experience to Multimodal Software Tuto...](http://arxiv.org/abs/2606.03951) | skill generation | 通过从人类交互体验中蒸馏出结构化教程知识，改进GUI智能体的规划行为，提升其任务... | 未说明复杂软件交互场景下的泛化能力，新建基准的覆盖范围不明确，存... | 能否基于人类交互演示蒸馏得到可复用的GUI agent技能，构建低算力的可落地agent h... | ✅ |
| 7 | high | - | [FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Ver...](http://arxiv.org/abs/2606.00660) | agent harness | 通过细粒度自验证框架，将原问题分解为可检查子问题，逐一对候选验证打分，选出最优输... | 仅在智能搜索任务验证，未验证在其他类型Agent任务上的泛化性，... | 能否将这种轻量细粒度自验证框架推广到通用工具调用Agent，以低成本提升Agent输出可靠性... | ✅ |
| 8 | high | - | [From Model Scaling to System Scaling: Scaling the Harness in Age...](http://arxiv.org/abs/2605.26112) | agent harness | 设计可审计、模块化、可验证的智能体harness架构，编排约束上下文、记忆与技能... | 仅提出研究方向与参考框架，尚未建立完整的harness评测体系，... | 可基于该思路探索适配低算力场景的模块化可复现智能体harness，验证系统设计对长程任务的实... | ✅ |
| 9 | high | - | [Getting Better at Working With You: Compiling User Corrections i...](http://arxiv.org/abs/2606.13174v1) | agent harness | 在编码智能体运行时添加即插即用技能层，从用户修正提取原子规则，任务完成前执行规则... | 依赖用户修正的清晰度，模糊修正无法生成有效规则，复杂场景下规则冲... | 能否将该基于用户修正的运行时约束方案拓展到通用工具Agent，实现MCP工具调用的合规管控 | ✅ |
| 10 | high | - | [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajec...](http://arxiv.org/abs/2606.11520v1) | evaluation/benchmark | 提出三阶段数据合成范式，构建带真实故障恢复动态的多轮训练轨迹，通过微调提升OS智... | 仅在ClawEval单一基准评测，未验证复杂真实OS场景，方法泛... | 基于该开源ISETrace数据集，能否搭建出低算力、可复现的OS智能体工具执行演示方案？ | ✅ |
| 11 | high | - | [PaperMentor: A Human-Centered Multi-Agent Writing Tutor for AI R...](http://arxiv.org/abs/2606.08857v1) | agent harness | 通过整合资深研究者整理的专家写作技能库，部署12个专用Agent，仅生成建议不替... | 用户研究样本量仅14，缺乏大规模基准测试，结果的泛化性有待进一步... | 这种基于人工整理专家技能库的多Agent harness方案，能否推广到其他领域的专业辅助任... | ✅ |
| 12 | high | - | [Pushing the Limits of LLM Tool Calling via Experiential Knowledg...](http://arxiv.org/abs/2606.10875v1) | tool-use control | 通过整合经验知识，采用扩宽推理宽度的推理方法，结合知识感知训练，优化大语言模型工... | 仅在公开标准基准上验证，未在真实工业场景复杂工具任务中验证实际性... | 能否将该经验知识激活增强思路适配到MCP工具调用场景，降低工业级agent工具调用失败率？ | ✅ |

## 方法族分布

- **evaluation/benchmark**：79 篇
- **agent harness**：61 篇
- **skill generation**：14 篇
- **tool-use control**：13 篇
- **unlearning/safety**：8 篇
- **policy optimization**：8 篇
- **multi-agent coordination**：8 篇
- **survey**：8 篇
- **other**：4 篇
- **model steering**：2 篇
- **reward learning**：2 篇
- **未分类**：2 篇

## 失败模式与风险信号

- 合成任务分布不匹配智能体弱点与训练进度
- 长范围规划失效、单Agent任务分解瓶颈、长文本合成幻觉、过程不可审计
- Agent互操作协议通信元数据明文泄露，攻击者可提前推断工作流与后续动作
- 现有恶意检测只能覆盖代码或指令单一方面，无法处理兼具代码与prompt属性的混合恶意技能风险
- 工具调用次优、多步交互错误累积、强化学习引发的过度自信错误
- 命令式编排状态机脆性大，低质量检索下智能体性能严重下滑，技能无法挽回损失
- 轨迹碎片化冗余、遗漏安全关键行为，导致生成技能行为重放一致性差
- Agent非预期优化，优化方向偏离可读性提升目标
- 原有调度器无法适配动态变化的集群规模，新规模下注意力特征分布偏移导致性能下降。
- 长周期任务中智能体记忆无法处理失败场景，缺乏在线可扩展性。

## 评测信号

- 基于真实用户生产数据，对比自主智能体与传统搜索工具在知识工作中的效率、成本与用户满意度差异
- 相同算力预算下多个基准任务解决率优于基线，三次迭代后在SWE-bench Verified上取得50.40%的任务解决率。
- 在两个深度研究基准取得最优整体性能，分别获58.03%、61.95%的最优得分，信息召回与分析排名第一。
- 验证了仅靠工作流开头的无负载元数据即可有效推断任务类别，防护方案可显著降低攻击者优势。
- 现有检测器对不同类型恶意技能效果差异极大，纯野生样本评测会带来最高66个召回点的排名偏差，现有方法无法完整覆盖风险。
- 评测方法的决策质量、整体智能体性能，以及优化过程中智能体不确定性估计的可靠性。
- 高质量检索下声明式技能提升准确率降低编排错误，低质量检索时所有智能体性能都会大幅下滑
- W2S相比摘要、提示类基线，将生成技能的行为重放一致性提升10.5%，验证了结构化分解的有效性。
- 验证QRS引导的LLM Agent可在不损失反编译代码正确性的前提下，实现针对性的可读性提升。
- 16节点训练直接测试48节点，SCALE相对无SRR的同架构将平均响应时间降低了8.9%。

## 控制机制 / Harness 信号

- 本文为基于现有工业产品的实证研究，未提出新的智能体行为控制或改进机制，仅开展效果分析
- 从智能体历史求解轨迹提炼结构化技能，生成针对性训练任务，经执行验证和奖励筛选后迭代优化智能体。
- 通过解耦Agent核心与工具生态实现全流程可追溯，结合动态规划、递归执行、评分推理优化约束agent行为。
- 在传输层与引导层定义元数据隐私保护属性，通过隐私传输方案抑制攻击者的工作流推断。
- 构建经Docker沙箱运行时验证的恶意智能体技能基准，为恶意技能检测提供真值评测，支撑检测方法改进。
- 通过将不确定性量化融入奖励设计维持决策不确定性分隔，结合轻量关键节点标注做后训练，改进工具调用决策。
- 在系统提示中附加自然语言形式的领域技能文件，让智能体推理时自主决定控制流，实现工具使用任务编排
- 通过RWSA中间表示结构化分解技能，基于W2S框架从交互轨迹提炼对齐可执行技能，保障行为一致性。
- 通过QRS量化框架引导，以结构相似性做门控，结合三个可读性子指标约束Agent优化方向，兼顾正确性与可读性。
- 通过结构化表示正则化稳定不同集群规模下的注意力特征统计，提升调度器的规模泛化能力。

## 可靠性 / 落地风险

- 所用数据为Perplexity内部非公开数据，难以复现，结论仅来自单平台，泛化性不足
- 闭环自演化过程可能累积历史轨迹中的错误，导致生成训练任务偏差，性能提升不可持续。
- 未公开代码与复现细节，未明确说明实际运行算力消耗，可复现性待验证。
- 现有主流Agent互操作协议默认存在该漏洞，修改底层传输的兼容性改造成本较高。
- 第三方智能体技能供应链风险缺乏有效评测，现有检测工具效果偏差大，工业落地实际效果不可控。
- 未披露具体实验细节与真实场景表现，方法的泛化能力未经过实际落地场景验证。
- 性能高度依赖检索质量，工业场景检索质量往往难以保证，低质量下方案完全失效
- 仅在小规模自定义技能集合测试，未验证大规模真实工业场景下的通用性。
- 仅验证单阶段优化，未在完整逆向工程全流程测试，工业落地需扩展适配。
- 仅在模拟节点环境验证，未在真实工业大规模集群测试，实际可用性待进一步验证。

## 可延展 Idea Hook

- 如何结合真实知识工作场景的需求，设计兼顾自主性与可控性的工业级agent harness框架
- 探索如何从智能体交互轨迹提炼可执行技能，构建低算力闭环自演化的单智能体控制框架。
- 如何将该可审计递归规划机制适配，打造低算力可复现的深度研究Agent Harness？
- 如何兼容现有A2A/MCP互操作协议，设计轻量元数据防护方案保障生产环境工作流完整性？
- 基于MalSkillBench基准，研发联合推理代码与指令的恶意智能体第三方技能检测框架，满足工业供应链安全需求。
- 能否将这种不确定性对齐的奖励设计思路适配到MCP工具调用场景，提升工业级agent的工具调用可靠性？
- 能否通过轻量检索优化提升低检索质量下声明式技能智能体的鲁棒性，适配工业工具使用场景？
- 针对Agent技能手工编写成本高的痛点，可基于该思路做工具调用技能自动提取的轻量可演示原型。
- 可探索将这种多指标门控的Agent引导方法，推广到通用Agent输出对齐的各类场景中。
- 可将这种规模泛化的正则化思路迁移到开放环境多工具调用的工作流调度agent harness中。
- 可参考该自适应记忆框架，设计面向工业场景的低算力长周期任务智能体harness方案做验证。
- 如何借鉴拆分技能、限制变更规模的思路，构建低成本工业友好的代码改进agent harness？

## 下次可问导师的问题

- 我们研究agent harness是否需要结合真实工业场景的实证发现，调整框架设计方向？
- 我们是否可以基于开源大模型复现该方法，验证低算力下自演化编码智能体的实际效果？
- 这种多Agent深度研究框架，改造成轻量工业可用Agent Harness的成本高吗？
- 我们当前的Agent harness框架是否需要补充通信元数据防护来适配生产多Agent场景？
- 我们是否需要跟进这个方向，开发适配第三方智能体技能的安全控制检测框架？
- 我们能否基于这篇的不确定性对齐思路，改造现有agent框架的工具调用决策模块？
- 我们是否可以将声明式技能范式移植到现有工具智能体项目中做落地验证？
- 我们是否可以基于该方法思路，落地一个工具调用技能自动提取的轻量可演示原型？
- 这种量化指标门控引导Agent的思路，能否推广到通用工具调用对齐场景？
- 这种规模泛化的正则化方法能不能迁移到我们研究的开放智能体工作流调度场景？
- 我们要不要适配这个框架，开发轻量长周期智能体记忆方案做可用的工业演示demo？
- 我们能不能基于该思路做一个面向开源项目的可复现轻量级代码改进agent demo？

## 代码资源

- [From Model Scaling to System Scaling: Scaling the Harness in Agentic AI](https://github.com/SafeRL-Lab/cheetahclaws) · 721 stars
- [MiniMax Sparse Attention](https://github.com/MiniMax-AI/MSA.) · 155 stars
- [ExCyTIn-Bench: Evaluating LLM agents on Cyber Threat Investigation](https://github.com/microsoft/SecRL) · 127 stars
- [Demo2Tutorial: From Human Experience to Multimodal Software Tutorials](https://github.com/showlab/Demo2Tutorial.) · 13 stars
- [AutoMegaKernel: A Statically-Checked Agent Harness for Self-Retargeting Megakern...](https://github.com/RightNow-AI/AutoMegaKernel) · 12 stars
- [ISE: An Execution-Grounded Recipe for Multi-Turn OS-Agent Trajectories](https://github.com/Valiere01/ISE-Trace.) · 7 stars
- [PaperMentor: A Human-Centered Multi-Agent Writing Tutor for AI Research Papers o...](https://github.com/jiarui-liu/overleaf) · 5 stars
- [Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Cod...](https://github.com/opensquilla/claw-swe-bench) · 5 stars
- [Recovering Policy-Induced Errors: Benchmarking and Trajectory Synthesis for Robu...](https://github.com/AlibabaResearch/RoTS.) · 4 stars
- [FineVerify: Scaling Test-Time Compute with Fine-Grained Self-Verification for Ag...](https://github.com/XuZhao0/fineverify) · 3 stars

## 常见基线方法

- **Claude Code**：2 篇
- **人类专家**：2 篇
- **Codex**：2 篇
- **基础模型**：2 篇
- **GPT-5**：2 篇
- **BrowseComp**：2 篇
- **Perplexity Search**：1 篇
- **仅配备搜索工具的人类**：1 篇
- **自演化基线**：1 篇
- **HTTP(S)原生地址传输**：1 篇

## 常用数据集

- **摘要未提及**：5 篇
- **SWE-bench Verified**：3 篇
- **Terminal-Bench 2.0**：3 篇
- **SkillsBench**：3 篇
- **BrowseComp**：3 篇
- **BFCL**：3 篇
- **GAIA**：3 篇
- **SWE-bench Pro**：2 篇
- **OSWorld**：2 篇
- **数学推理基准**：2 篇

---
*自动生成于 2026-06-14 | ArXiv_Daily_Digest*