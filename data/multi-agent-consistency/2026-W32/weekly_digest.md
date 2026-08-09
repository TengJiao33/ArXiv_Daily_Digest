# 多 Agent 交互与一致性 — 2026-W32 (08/03-08/09)

本周新增 **69** 篇论文，**3** 篇附带代码。优先级：high 37 / medium 22 / low 10。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Aug...](http://arxiv.org/abs/2608.05573v1) | evaluation/benchmark | 精炼后的JudgeSkill使Agent评判准确率提升14.8个百分点，十次rollout选... | 将验证知识外部化为可复用JudgeSkill，引导评判器做针对性检查，输出基于证... | 仅在自建基准上验证效果，尚未在大规模真实业务任务中验证方法的泛化... | ✅ |
| 2 | high | - | [Adaptive Arena-based Contestable Argumentative Network-of-Expert...](http://arxiv.org/abs/2608.05391v1) | multi-agent coordination | 结合医学微调基座模型的CANOE框架，在护理计划协同任务上同时兼具优异的临床正确性、安全性与... | 通过基于竞技场的定量双极论证框架解决多智能体论点冲突，支持人类介入争议后重计算输... | 仅在特定医疗任务验证，未验证该框架在其他多智能体场景下的通用性与... | — |
| 3 | high | - | [Adjudicated Captioning: Multi-Agent Alignment Scoring and Consen...](http://arxiv.org/abs/2607.28986v1) | multi-agent coordination | 该框架中，非学习架构改动贡献了+7.8的CIDEr提升，学习得到的重排序器仅额外带来+1.8... | 引入验证器重排序检索结果，输出端采用基于共识蒸馏的重排序器做波束仲裁优化对齐。 | 依赖多个预训练冻结组件的性能，新增模块增加了推理阶段的计算开销。 | — |
| 4 | high | - | [Adversarial Stress Testing of Role-Playing Language Agents using...](http://arxiv.org/abs/2608.03166v1) | evaluation/benchmark | 多策略对抗能发现单策略测试不可见的失效，鲁棒性得分平均降0.17-0.20，权威挑战与情感操... | 构建多智能体对抗评测框架，通过自动裁判多维度打分，系统性发现智能体失效，支撑智能... | 对抗测试本身存在潜在伦理风险，未验证大规模真实场景下的方法通用性... | — |
| 5 | high | - | [Agents Catching Agents: Shortcut Cascades and Benchmark Gaming i...](http://arxiv.org/abs/2608.03744v1) | consistency detection | 两名同伴坚持相同错误答案时，38%的被测智能体会采纳错误，门控监督误报率达100%，仅独立裁... | 设计三类监督智能体，提出独立裁判机制，通过私下重查询被测智能体，识别多智能体委员... | 非独立监督完全无法识别错误操纵，错误传播易引发临床决策失误，威胁... | — |
| 6 | high | - | [An Actionable Diagnosis of Multilingual, Multi-Agent Planning Fa...](http://arxiv.org/abs/2608.03735v1) | agent harness | 规划失败占总失败的比例随语言资源可用性降低而升高，低资源语言影响最显著，TART平均提升准确... | 通过归纳规划接地失败的分类体系，将分类关键信息显式提供给规划器与下游子智能体，降... | 仅针对规划阶段失败展开研究，未覆盖多智能体交互其他环节，泛化性有... | — |
| 7 | high | - | [Autonomous Repair for Multi-Agent Systems via Monte-Carlo Tree S...](http://arxiv.org/abs/2607.29055v1) | multi-agent coordination | MARS的诊断引导扩展、分类增强评估两个核心模块有效，在StateMAS上相对SOTA绝对提... | 通过基于蒙特卡洛树搜索的MARS框架自动修复多智能体错误输出，结合诊断引导与部分... | 仅在自建基准上验证效果，未在真实工业场景测试，方法泛化能力尚不明... | — |
| 8 | high | - | [Benchmarking and Enhancing LLMs for Rule-Intensive Review of Nat...](http://arxiv.org/abs/2608.06312v1) | evaluation/benchmark, mu... | 最强主流大模型任务CMCS仅0.3280远低于专家的0.6640，所提框架可将指标提升至0.... | 将审查知识转化为专属技能，通过多智能体分工协调各审查环节，加入结果验证提升输出质... | 仅针对中国国家标准领域，基准领域特定性强，方法在其他领域的泛化性... | — |
| 9 | high | - | [Certifying Collective Reasoning in Multi-Agent Systems via Koopm...](http://arxiv.org/abs/2608.05956v1) | consistency detection | 次主导特征值得到的收敛截止与实际观测收敛的双对数相关性达0.93，24种配置中96%的情况可... | 通过库普曼谱分析生成收敛截止、派系划分、可审计基三类认证，为可信集体推理提供保证... | 仅在特定模型上验证，未在真实复杂多智能体任务中验证方法的泛化有效... | — |
| 10 | high | - | [CockpitHAT: Dependency-Graph-Driven Hierarchical Attribution for...](http://arxiv.org/abs/2608.01805v1) | evaluation/benchmark | 依赖感知多通道风险校准归因，在Who&When基准上比SOTA ECHO最高提升17.6/1... | 通过依赖图驱动的分层归因，结合多通道证据与安全加权，实现多智能体进程级故障的准确... | 目前仅验证座舱场景效果，方法通用性有待验证，构建标注基准依赖专家... | — |
| 11 | high | ICML 2026 | [Emergence of Biased Consensus in Multi-Agent LLM Debates](http://arxiv.org/abs/2608.02827v1) | multi-agent coordination | 噪声是多智能体辩论中偏误共识涌现的关键驱动，从众性超临界阈值会发生集体偏误相变，异质性可抑制... | 通过理论建模揭示偏误共识的涌现机制，发现智能体异质性可抑制多智能体辩论中集体偏误... | 涌现的偏误集体共识会带来公平性与安全性问题，给多智能体决策系统落... | — |
| 12 | high | - | [Enhancing Social Intelligence in LLMs with Hierarchical Reasonin...](http://arxiv.org/abs/2608.05832v1) | multi-agent coordination | 所提方法微调的Qwen2.5-7B智能体，在多智能体社交谈判任务的目标完成成功率比GPT-4... | 通过分层分解社交对话任务，设计方差门控动态奖励机制优化智能体策略，提升目标协调能... | 仅在单一社交谈判基准验证，方法的泛化能力与稳定性未得到充分验证。 | — |

## A 会 / Venue 标签

- **ICML 2026**：2 篇

## 方法族分布

- **multi-agent coordination**：34 篇
- **evaluation/benchmark**：13 篇
- **agent harness**：6 篇
- **skill generation**：2 篇
- **unlearning/safety**：2 篇
- **survey**：2 篇
- **tool-use control**：2 篇
- **consistency detection**：2 篇
- **skill optimization**：1 篇
- **online distillation**：1 篇
- **agent memory**：1 篇
- **other**：1 篇

## 失败模式与风险信号

- 现有智能体漏洞修复因缺少必要的多维度程序上下文，修复效果不佳
- 原有内存操作额外成本高，易丢失信息掩盖原始证据
- 多智能体产生错误输出后缺乏自动修复机制，依赖人工完成故障归因与修复
- 单次图文对齐后解码无额外视觉反馈，性能提升长期停滞
- 有界覆盖空性、规范歧义、时序逻辑错误、多属性压力
- 智能体故障起源难以定位，现有故障分类多基准特定，缺乏通用共享结构，无法指导修复。
- 现有技能优化依赖真值反馈，无标注场景下无法有效优化智能体技能
- 运行中故障累积、工具错误级联、目标偏移、结果编造
- 现有自适应MAR方法信用分配粒度粗，算子效用估计不准确，推理精度成本平衡不佳
- 自蒸馏教师输出不可靠，现有方法对噪声敏感、容易忽略位置差异

## 评测信号

- 在SEC-Bench的300个真实实例中，经消毒器补丁验证，AgenticRepair成功率达73%，较最强基线提升29%。
- 保持问答性能竞争力的同时，消除内存操作的额外大模型调用，相对最快基线降低57.6%的时间成本。
- 在StateMAS基准上，MARS相对现有SOTA修复性能绝对提升3.0%-12.1%，token消耗与基线方法相当
- 不重训练原模型前提下，COCO Karpathy的CIDEr较IFCap提升9.6，较NES提升7.7，跨数据集迁移有效。
- 可成功检测修复一个真实ALU功能bug，仅一个基准设计可稳定修复，明确总结了四类失效模式。
- 在NeuroBench测试中，CyberNeuro将域外领域准确率从40%提升至69%，本地WandaMind方案token消耗量仅为Neuroclaw的约10.6%。
- 用独立推理智能体作为裁判评测分类可复现性，最强裁判对人类标注的Cohen's κ达到0.76。
- 对比现有无真值提示优化器和基于真值的技能优化器，评测SSO在两类任务上的性能表现。
- 5%误报预算下故障检出率达0.71，修复后任务成功率从52%提升至73%，单步开销仅约200微秒
- 该方法在六个推理基准上适度提升推理准确率，同时大幅降低推理成本，相比现有代表性MAR方法取得更优的准确率-成本平衡。

## 控制机制 / Harness 信号

- 通过编排多个专用子智能体分别构建三类程序上下文，将上下文注入修复子智能体内存引导补丁合成。
- 通过确定性零Token内存操作组织原始交互轨迹，仅最终问答调用大模型，校准冲突，约束答案锚定原始信息。
- 通过基于蒙特卡洛树搜索的MARS框架自动修复多智能体错误输出，结合诊断引导与部分回滚平衡性能与token成本
- 引入验证器重排序检索结果，输出端采用基于共识蒸馏的重排序器做波束仲裁优化对齐。
- 通过开源形式验证后端生成正确性证明与反例，将反例反馈给LLM迭代修正输出，保障修复的正确性。
- 设置专用Validator验证智能体，集成人在回路验证面板，在保障数据隐私的同时，提升生物医学分析质量。
- 通过以交互为中心的故障分类定位故障起源，明确不同组件的修复方向，为智能体系统改进提供支撑。
- 通过LLM评判对比行为差异，排序筛选优质行为迭代更新技能，基于无标注验证集判断是否接受更新。
- 通过低成本遥测检测器提前检测故障，搭配确定性验证层过滤误报，对检出故障执行回滚重跑修复
- 通过设计基于共享前缀的新型信用分配机制，训练轻量状态路由器动态选算子，优化多步协作效用估计，提升推理精度成本比。

## 可靠性 / 落地风险

- 需要调用多个LLM子智能体，整体推理成本较高，修复效果依赖基础模型本身能力。
- 仅在封闭问答基准测试，未验证开放复杂长交互场景的效果，泛化能力尚不明确。
- 仅在自建基准上验证效果，未在真实工业场景测试，方法泛化能力尚不明确
- 依赖多个预训练冻结组件的性能，新增模块增加了推理阶段的计算开销。
- 仅单基准可稳定修复，存在多种常见失效模式，方案受限于开源形式验证工具本身缺陷。
- 仅在公开基准测试集完成验证，未测试真实临床复杂场景，实际落地的可靠性有待验证。
- 分类准确性依赖裁判模型能力，未在大规模落地任务中验证分类体系的实用性。
- 完全依赖大语言模型评判的准确性，无真值监督，容易引入评判偏差影响最终优化效果。
- 基础检测器跨部署冷迁移性能差，需重新校准，不利于跨场景的快速落地部署
- 仅在通用推理基准完成验证，未在复杂真实业务场景测试，方法实际泛化能力未知。

## 代码资源

- [SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic E...](https://github.com/HanZhi306/SkillTV-Bench) · 3 stars
- [Verifiable Memory: Learning Unified Memory Management with Local and Global Veri...](https://github.com/Sun-SYSU-24/VerMem.) · 1 stars
- [Attacking and Defending Multi-Agent Collaborative Filtering Systems Through Conn...](https://github.com/anjunhu/ConnACF)

## 常见基线方法

- **未提及具体基线名称**：2 篇
- **未提及具体基线方法名称**：1 篇
- **现有最优SOTA方法**：1 篇
- **IFCap**：1 篇
- **NES**：1 篇
- **基于仿真的RTL修复验证**：1 篇
- **依赖商业工具的RTL修复方案**：1 篇
- **基线模型**：1 篇
- **Neuroclaw**：1 篇
- **现有无真值提示优化器**：1 篇

## 常用数据集

- **摘要未提及**：4 篇
- **ALFWorld**：2 篇
- **SEC-Bench**：1 篇
- **长内存问答基准**：1 篇
- **长上下文问答基准**：1 篇
- **StateMAS**：1 篇
- **COCO Karpathy**：1 篇
- **Flickr30k Karpathy**：1 篇
- **NoCaps**：1 篇
- **ALU功能案例**：1 篇

---
*自动生成于 2026-08-09 | ArXiv_Daily_Digest*