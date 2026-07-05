# Agent Skills 与 Harness — 2026-W27 (06/29-07/05)

本周新增 **238** 篇论文，**16** 篇附带代码。优先级：high 177 / medium 42 / low 19。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Agent-as-a-Router: Agentic Model Routing for Coding Tasks](http://arxiv.org/abs/2606.22902) | agent harness | 仅给普通LLM路由增加任务维度性能统计，即可获得15.3%的相对性能提升，超过同先验的启发式... | 通过构建上下文-动作-反馈循环，搭配编排器、验证器与记忆模块，积累执行经验补全信... | 依赖多个第三方大模型服务，部署的一致性和可用性受外部服务制约，存... | ✅ |
| 2 | high | ICML 2026 | [AutoRAS: Learning Robust Agentic Systems with Primitive Represen...](http://arxiv.org/abs/2606.21445) | agent harness | 基于符号基元的自动化设计方案，在对抗攻击下性能下降幅度最小，同时具备更优的成本权衡。 | 通过将智能体系统设计转化为符号基元序列优化，引入执行得到的安全信号提升系统鲁棒性... | 未披露具体评测基准与详细定量结果，实际落地的效果有待进一步验证。 | ✅ |
| 3 | high | - | [Beyond Parallel Sampling: Diverse Query Initialization for Agent...](http://arxiv.org/abs/2606.17209) | agent harness | 标准并行采样收益递减根源是首轮查询冗余；DivInit在匹配算力下，多跳问答平均提升5至7个... | 采用无训练的首轮查询多样化干预，减少并行轨迹检索冗余，提升同等算力下的搜索性能。 | 仅针对首轮查询优化，未验证在更复杂开放领域搜索任务的通用性。 | ✅ |
| 4 | high | - | [Bridging VideoQA and Video-Guided Agentic Tasks via Generalized ...](http://arxiv.org/abs/2606.29445v1) | evaluation/benchmark | 兼顾任务相关性和场景动态的广义关键帧提取，在EgoSchema全集涨2.0%、NExT-QA... | 通过任务驱动、感知场景的关键帧提取筛选有效输入帧，提升MLLM基GUI智能体的任... | 仅在有限学术基准验证，未测试真实场景长周期复杂任务的泛化稳定性。 | ✅ |
| 5 | high | - | [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](http://arxiv.org/abs/2606.29920) | evaluation/benchmark | 即使最先进大模型验证性能较强仍存在大量噪声，弱模型对提示变化更敏感，批处理存在精度-效率权衡... | 通过构建专用评测基准评测LaaJ在智能体场景的验证可靠性，为后续相关方案优化提供... | 现有LaaJ验证仍存在不可忽视的噪声，直接用于工业级智能体评测可... | ✅ |
| 6 | high | - | [DMV-Bench: Diagnosing Long-Horizon Multimodal Agents'Visual Memo...](http://arxiv.org/abs/2606.27499) | evaluation/benchmark | 在5、10、15、50四种长度的任务链上，DualMem在两个测试模型上均优于对比方法，视觉... | 构建标准化评测基准诊断智能体视觉记忆缺陷，通过双编码并行记忆架构提升智能体长程视... | 评测场景较为特定，仅针对视觉记忆任务，方法在通用长程任务中的泛化... | ✅ |
| 7 | high | - | [FeatX: Editing Software by Editing Features for Repository-Level...](http://arxiv.org/abs/2606.31206v1) | agent harness | FeatX相比强LLM基线函数级修改定位F1相对提升42.6%，总调用成本仅0.07美元，可... | 通过提取仓库分层特征结构与特征-代码映射，将特征编辑转换为代码补丁，以特征导向工... | 仅在小规模特征编辑场景验证，未在大规模复杂仓库任务中做充分测试。 | ✅ |
| 8 | high | - | [ICBCBench: An Industry Consortium Benchmark for Financial Deep R...](http://arxiv.org/abs/2606.17458) | evaluation/benchmark | 当前最优深度研究智能体与大语言模型在金融深度研究中，复杂推理、事实锚定与报告质量仍存在显著缺... | 通过构建双轨评测基准，为金融深度研究智能体提供全面评估反馈，助力改进智能体产业级... | 现有模型均达不到该基准体现的产业级要求，金融深度研究智能体落地仍... | ✅ |
| 9 | high | - | [ProMSA:Progressive Multimodal Search Agents for Knowledge-Based ...](http://arxiv.org/abs/2606.27974v1) | tool-use control | 带工具调用预算约束的渐进自适应检索，相比固定检索流水线，可稳定提升KB-VQA的检索与端到端... | 通过显式工具调用预算约束行为，先SFT学习规范工具调用格式，再经序列强化学习优化... | 仅在两个特定KB-VQA数据集验证，泛化能力未测试，存在跨场景落... | ✅ |
| 10 | high | - | [Safety Testing LLM Agents at Scale: From Risk Discovery to Evide...](http://arxiv.org/abs/2607.01793) | evaluation/benchmark | 对四个生产级智能体框架测试显示，多通道攻击下平均攻击成功率达93.9%，现有框架存在大量安全... | 将待测智能体放在隔离沙箱运行，由控制智能体基于运行时观测引导交互，基于环境和工具... | 大规模测试的算力消耗未披露，适配新型智能体的实际落地扩展成本未明... | ✅ |
| 11 | high | ICML 2026 | [Think Twice Before You Act: Protecting LLM Agents Against Tool D...](http://arxiv.org/abs/2606.20922) | tool-use control | 现有提示注入防御难以防御跨工具描述投毒，投毒描述会留在规划上下文持续影响后续工具选择。 | 通过隔离规划机制，将检测出的可疑不对齐工具放入隔离名单，切断投毒描述的后续影响，... | 依赖可疑工具检测的准确性，摘要未评测误检误隔离对正常任务性能的影... | ✅ |
| 12 | high | - | [Tmax: A simple recipe for terminal agents](http://arxiv.org/abs/2606.23321) | agent harness | 仅9B参数的终端智能体经Tmax训练后，在Terminal-Bench 2.0上取得27%精... | 通过多样化数据生成结合纯结果型强化学习，构建简单可复现的终端智能体训练方案。 | 仅在单个公开基准上验证效果，模型在真实终端环境下的泛化能力尚未得... | ✅ |

## A 会 / Venue 标签

- **ICLR 2026**：9 篇
- **ICML 2026**：5 篇

## 方法族分布

- **evaluation/benchmark**：86 篇
- **agent harness**：80 篇
- **skill generation**：12 篇
- **multi-agent coordination**：12 篇
- **tool-use control**：10 篇
- **unlearning/safety**：9 篇
- **policy optimization**：9 篇
- **other**：4 篇
- **survey**：4 篇
- **reward learning**：3 篇
- **model steering**：2 篇
- **factuality detection**：1 篇

## 失败模式与风险信号

- 已对齐Agent易遭遇运行时劫持，原有外部防御机制无法有效防护
- 推理漂移、强模型能力无法被弱Agent/人类利用
- 多工具调用任务完成但发生隐私过度披露，中间调用泄露不必要私密信息
- 故障检测后生成的恢复动作不满足安全约束、实时性不足，导致容错控制失效
- 静态检索不自适应，工具调用冗余
- 长时序展开过程中局部预测误差沿图扩散，引发长时域规划发散失效
- 对抗输入规避安全防护，工具使用与多步推理场景安全失效
- 长交互中无法正确丢弃过时事实，记忆更新失败
- 早期侦察失败引发错误级联，掩盖Agent真实的漏洞利用能力
- 自主评估提供的奖励存在噪声，导致计算机使用智能体强化学习性能下降

## 评测信号

- 在所有参与测试的硬件设计基准上达到100%的完全文手动完成率，同时明确所用基准仅为真实工程问题的受控近似。
- 未给出实际评测结果，仅提出可采用自身免疫率（假阳性干预率）作为新型安全评测指标。
- 评测单Agent推理能力、强弱Agent交接鲁棒性、相对于弱模型的分布漂移程度、思维链可读性。
- 评测任务私有信息流向合规性，同时评估Agent的任务完成效果与多工具轨迹中的隐私过度披露风险。
- 验证得到轻量LLM（GPT-4o-mini/GPT-4.1-mini）生成的故障恢复决策可满足对应过程的动态延迟预算，对两类任务均有效
- 在两个基准数据集上，ProMSA相较RAG和agent强基线，一致提升了检索准确率与端到端问答准确率。
- 智能体无需人工即可完成重识别，单目标成本仅分钟级美元级，整体重识别成功率41.9%，目标子集达72%。
- 验证得出感知误差GWM可阻止长时域展开误差发散，同时保持精度，明确GWM适用于动态图展开任务
- 评测模型对抗场景下的安全鲁棒性与整体能力，发现8B参数Yuvion在安全任务上优于更大尺寸的主流SOTA模型。
- 前沿模型用自维护受限记忆后准确率从92%降至77%，小模型微调后 unseen 对话准确率从9%提升至16.7%。

## 控制机制 / Harness 信号

- 通过编译Markdown harness生成带领域知识、评估规则和策略的项目包，依托git操作管理状态，实现免手动迭代演化。
- 提出嵌入Agent认知循环的原生内生免疫架构，通过分层隔离与元认知自监控实现动态运行时安全防御。
- 采用强弱Agent协作生成推理，以团队联合奖励约束强Agent推理模式，通过GRPO损失优化强Agent，适配弱Agent需求。
- 构建专用隐私评测基准，对Agent多工具调用轨迹开展目的绑定隐私审计，识别隐私过度披露问题。
- 通过多智能体分工、预执行仿真验证、安全约束校验结合图RAG知识检索，约束智能体生成合规的故障恢复动作
- 通过显式工具调用预算约束行为，先SFT学习规范工具调用格式，再经序列强化学习优化决策，去重避免冗余检索。
- 本文未提出针对agent行为的改进控制机制，仅验证大语言模型自主完成重识别任务的能力。
- 通过分析两种误差放大机制，引入谱正则化、展开一致性与关键节点加权，抑制误差放大提升稳定性
- 通过对抗感知数据构造、多阶段安全训练、安全感知智能体强化学习提升模型工具使用的安全鲁棒性。
- 构建针对过时记忆惩罚、新鲜事实奖励的强化学习环境，通过GRPO微调优化智能体的记忆更新策略。

## 可靠性 / 落地风险

- 方法仅在受控基准验证，尚未适配真实工业芯片设计的复杂场景，泛化能力未得到验证。
- 仅提出架构设计方案，未给出实证验证结果，实际防御效果与落地性待验证。
- 仅在竞赛数学推理场景验证，未在通用多Agent场景验证，方法泛化性有待进一步验证。
- 仅完成评测基准构建，未提出解决隐私过度披露的落地方案，需额外开发对应的防护控制方法。
- 仅在仿真场景完成验证，缺乏真实工业复杂场景的实测，落地存在较高不确定性
- 仅在两个特定KB-VQA数据集验证，泛化能力未测试，存在跨场景落地适配风险。
- 智能体可低成本规模化实现隐私重识别，现有隐私保护机制未充分应对该新型可扩展威胁。
- 仅在标准图基准测试，未在实际大规模工业agent任务验证，泛化性待确认
- 自构建评测集可能与真实落地场景存在偏差，未提及实际部署的长期鲁棒性验证。
- 目前仅获得小幅准确率提升，未在大规模实际工业任务中验证落地效果。

## 代码资源

- [Qwen-AgentWorld: Language World Models for General Agents](https://github.com/QwenLM/Qwen-AgentWorld) · 766 stars
- [Tmax: A simple recipe for terminal agents](https://github.com/hamishivi/tmax.) · 164 stars
- [Agent-as-a-Router: Agentic Model Routing for Coding Tasks](https://github.com/LanceZPF/agent-as-a-router.) · 161 stars
- [TraceLab: Characterizing Coding Agent Workloads for LLM Serving](https://github.com/uw-syfi/TraceLab.git) · 12 stars
- [ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question ...](https://github.com/DingWu1021/Promsa.) · 8 stars
- [Bridging VideoQA and Video-Guided Agentic Tasks via Generalized Keyframe Extract...](https://github.com/VG-GUI-TASKER/VG-GUI-TASKER.) · 7 stars
- [HOLMES: Evaluating Higher-Order Logical Reasoning in LLMs](https://github.com/wuyucheng2002/HOLMES.) · 3 stars
- [Beyond Parallel Sampling: Diverse Query Initialization for Agentic Search](https://github.com/cxcscmu/diverse-query-initialization) · 2 stars
- [Can LLM-as-a-Judge Reliably Verify Rubrics in Agentic Scenarios?](https://github.com/THU-KEG/RuVerBench.) · 1 stars
- [ICBCBench: An Industry Consortium Benchmark for Financial Deep Research](https://github.com/DeepFin-Intelligence/ICBCBench.) · 1 stars

## 常见基线方法

- **GPT-5.5**：4 篇
- **Claude Code**：4 篇
- **GRPO**：3 篇
- **ReAct**：3 篇
- **GEPA**：3 篇
- **GPT-5.4**：2 篇
- **零样本基线**：2 篇
- **OpenCode**：2 篇
- **基于置信度的基线方法**：2 篇
- **Claude Opus 4.8**：2 篇

## 常用数据集

- **摘要未提及**：6 篇
- **WebShop**：5 篇
- **OSWorld**：4 篇
- **ALFWorld**：4 篇
- **GAIA**：4 篇
- **Terminal-Bench 2.0**：2 篇
- **编码任务基准**：2 篇
- **HotpotQA**：2 篇
- **ToolBench**：2 篇
- **AndroidWorld**：2 篇

---
*自动生成于 2026-07-05 | ArXiv_Daily_Digest*