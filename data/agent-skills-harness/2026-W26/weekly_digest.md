# Agent Skills 与 Harness — 2026-W26 (06/22-06/28)

本周新增 **93** 篇论文，**5** 篇附带代码。优先级：high 61 / medium 27 / low 5。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [EnterpriseClawBench: Benchmarking Agents from Real Workplace Ses...](http://arxiv.org/abs/2606.23654v1) | evaluation/benchmark | 当前最优配置Codex+GPT-5.5在该真实场景基准上仅取得0.663得分，企业智能体评测... | 通过构建带多维度标注的标准化评测基准，提出多维度评测协议，规范企业智能体的能力评... | 基准原始数据未公开，第三方无法直接复现原实验，难以验证论文得到的... | ✅ |
| 2 | high | - | [MacAgentBench: Benchmarking AI Agents on Real-World macOS Deskto...](http://arxiv.org/abs/2606.22557v1) | evaluation/benchmark | 最优配置Claude Opus在OpenClaw上可达73.7% Pass@1，性能优势来自... | 通过构建带细粒度多检查点评分的评测基准，为桌面智能体能力评估提供反馈支撑。 | 仅覆盖macOS平台，对其他桌面系统通用性不足，评测范围存在一定... | ✅ |
| 3 | high | - | [MedGuards: Multi-Agent System for Reliable Medical Error Detecti...](http://arxiv.org/abs/2606.25651v1) | agent harness | 无需微调基座大模型，多智能体分工加置信度仲裁方案，在四个多语言医疗数据集上各项指标取得显著提... | 将医疗错误检测纠正任务拆分给多个专用智能体，通过置信度引导仲裁解决分歧，无需额外... | 仅在公开医疗文本数据集验证，未在真实临床落地场景测试，实际效果待... | ✅ |
| 4 | high | - | [OPID: On-Policy Skill Distillation for Agentic Reinforcement Lea...](http://arxiv.org/abs/2606.26790v1) | online distillation | OPID在三个测试基准上全面优于仅结果RL和现有技能蒸馏基线，稳定提升了任务性能与样本效率 | 从同策略轨迹提取分层技能生成稠密令牌级监督，结合结果优势优化策略，改进智能体决策... | 仅在中小规模任务基准测试，未验证大规模真实场景下的稳定性与适配性 | ✅ |
| 5 | high | - | [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How...](http://arxiv.org/abs/2606.26027v1) | tool-use control | 多步工具使用强化学习的灾难性崩溃源于特定控制token概率异常突增，模型底层工具使用能力完好... | 引入多种监督信号，采用监督微调与强化学习交错训练，修正控制token概率异常，提... | 分布外泛化性能较差，未在真实任务验证，落地应用存在一定不确定性。 | ✅ |
| 6 | high | - | [A Deterministic Control Plane for LLM Coding Agents](http://arxiv.org/abs/2606.26924v1) | agent harness | 调研发现10.1%的配置路径跨仓库重复，75.5%克隆对跨组织，不到1%的Agent配置声明... | 在现有harness之上新增确定性控制平面，通过内容寻址、层级权限、可追溯、漂移... | 仅在人工注入违规的测试中验证机制，缺乏真实开发者场景的落地效果验... | — |
| 7 | high | - | [A Process Harness for Uplifting Legacy Workflows to Agentic BPM:...](http://arxiv.org/abs/2606.27188v1) | agent harness | 流程线束可在不替换原有工作流引擎的前提下，同时满足业务流程的结构合规要求和控制点的智能自主适... | 通过在原有确定性工作流引擎外部增设策略管控的智能体线束层，拦截指定控制点实现管控... | 仅在单一场景验证，未经过多类大规模业务场景测试，落地通用性有待验... | — |
| 8 | high | - | [A Stackelberg Framework for Resource-Aware LLM Agents: Learning,...](http://arxiv.org/abs/2606.23026v1) | agent harness | 修复后的控制器相比保守基线平均token成本降低17.4%，输出质量差异不存在统计显著性。 | 通过斯塔克尔伯格博弈建模资源治理问题，优化策略后结合真实API校准完成策略修复与... | 仅开展300轮小规模实验，理论结果为条件性，未得到经认证的真实系... | — |
| 9 | high | - | [A Survey on Multi-Agent LLM Frameworks with Semantic Memory Inte...](https://www.semanticscholar.org/paper/21c04ba4ed923d1984fb6dd10f4e2681dbaf854a) | survey | 当前集成语义记忆与动态DAG编排的LLM多智能体框架普遍存在协调需求高、故障检测能力弱、无统... | 通过梳理现有多智能体的DAG编排、语义记忆集成等架构，归纳核心问题，明确领域评估... | 领域缺乏统一系统设计标准与标准化评估方法，可落地性缺乏验证，工业... | — |
| 10 | high | - | [ATRIA: Adaptive Traceable ECG Reporting with Iterative Agents](http://arxiv.org/abs/2606.24392v1) | multi-agent coordination | 模拟临床迭代流程的多智能体架构，结合已有临床验证模型，可产出可追溯可修正的可信报告，支持直接... | 通过将每个报告断言绑定对应证据，支持迭代修正单个结果，复用已有临床可信模型保障输... | 无大规模量化评测验证效果，仅靠案例演示，临床实际落地还需要更多有... | — |
| 11 | high | - | [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injec...](http://arxiv.org/abs/2606.26479v1) | evaluation/benchmark | 单H200的Qwen2.5-7B设置中，Progent将攻击成功率从25.8%降至4.2%，... | 提出自适应攻击评测协议，验证带外确定性中介机制对提示注入防御的鲁棒性。 | 多数现有带外防御未经过自适应攻击验证，实际部署存在潜在安全漏洞。 | — |
| 12 | high | - | [AgentLens: Interpretable Safety Steering via Mechanistic Subspac...](http://arxiv.org/abs/2606.22673v1) | model steering | 干预大语言模型单个网络层中的10维子空间，即可有效减少多轮编码智能体的有害执行行为。 | 基于机制可解释性定位安全相关的隐藏表示子空间，运行时检测风险并干预子空间，调控不... | 仅在小规模自建基准上验证，尚未验证更大模型与真实复杂编码场景的效... | — |

## 方法族分布

- **agent harness**：34 篇
- **evaluation/benchmark**：27 篇
- **tool-use control**：7 篇
- **survey**：6 篇
- **multi-agent coordination**：5 篇
- **unlearning/safety**：4 篇
- **skill generation**：3 篇
- **model steering**：2 篇
- **未分类**：1 篇
- **other**：1 篇
- **policy optimization**：1 篇
- **online distillation**：1 篇

## 失败模式与风险信号

- 文生图生成多样性坍塌，现有提升多样性方法的变异无实际语义意义
- 提示优化扩展至多智能体时搜索空间指数增长，效果不稳定
- 现有企业智能体评测仅用单一分数汇总性能，无法全面反映智能体实际落地能力。
- 大模型幻觉污染因果结论
- 陈旧内容锚定后续生成、固定压缩错误丢弃推理过程的有用中间结果
- 现有提示注入防御无法检测嵌入合法指令的恶意Agent技能，引发供应链攻击风险
- 现有方法污点爆炸、提示注入操纵工具、隐私信息泄露
- 上下文隐私泄露，含视觉共置泄露、过度分享、接收方内容错配三类。
- AI Agent生成代码易出现多种异于传统开发的安全漏洞
- 训练部署提示不匹配，工具选择缺乏结构化

## 评测信号

- 仅定性说明方法可生成符合要求的可导航设计空间，未给出具体量化评测结果与指标
- 关注不同任务、工作流、团队规模等系统配置下，提示优化为多智能体系统带来的性能增益差异。
- 评测需覆盖harness-模型组合、产出质量、成本、运行时、技能迁移多个维度，当前最优模型得分仅0.663。
- 通过案例验证该方案可隔离大语言模型的不可靠性，避免幻觉错误被引入最终的因果发现结论中。
- 任务准确率较无压缩基线最高提升18.1个百分点，token成本降低30%-70%，效果匹配或超越固定间隔压缩
- 相比直接LLM扫描成本降低一个数量级，仅小幅损失召回，能检出多数现有检测器漏检的恶意技能。
- 在多个基准上达到近乎完美的召回，F1匹配或超过GPT基线，token成本最高降81倍，小模型结果可跨模型迁移。
- 15个前沿计算机使用智能体平均隐私泄露率达67.9%，11个在超半数场景发生信息泄露。
- 分析已部署氛围编码应用中漏洞的流行度、严重程度与根因，总结异于传统开发的漏洞特征模式。
- 验证程序记忆可为工业工作流带来稳定性能增益，多模型轨迹演化技能的跨模型泛化优于单模型轨迹源。

## 控制机制 / Harness 信号

- 在文本层引入多样性，利用带结构化变异约束的智能体工作流，引导生成符合要求的可控多样图像
- 通过对多智能体系统的系统提示优化开展基准评测，分析不同设置下提示优化对系统行为的改进效果。
- 通过构建带多维度标注的标准化评测基准，提出多维度评测协议，规范企业智能体的能力评估流程。
- 通过明确智能体的辅助定位，约束智能体仅负责工作流辅助任务，不输出核心因果结论，保证因果主张锚定数据与正式算法。
- 在推理阶段添加可调用压缩工具与轻量压缩时机判断规则，引导模型自主完成自适应上下文压缩，无需训练
- 采用两阶段检测机制，基于注意力筛选可疑片段后做精细判断，实现低成本规模化的恶意Agent技能审计管控。
- 提出几何信息流框架GIF跟踪输入输出信息流动，上界互信息检测非法流动，结合轻量分类器实现安全控制。
- 构建可执行、能确定性打分的评测harness，检测计算机使用智能体的上下文信息泄露问题。
- 本文未提出行为控制改进方法，仅设计结合Agent辅助审计与人工验证的漏洞分析框架开展安全研究。
- 通过构建标准化评估基准梳理技能泛化特性，指导生产平台中程序记忆系统的构建部署，提升任务性能。

## 可靠性 / 落地风险

- 未给出具体评测基准与量化结果，方法的复现性与落地效果未验证，存在评测不足风险
- 仅开展泛化性评测，未验证工业真实场景下的落地效果，评测维度不够贴近工业需求。
- 基准原始数据未公开，第三方无法直接复现原实验，难以验证论文得到的实验结论。
- 仅做了单个案例验证，缺乏多场景大规模评测，方案的泛化性未得到充分验证。
- 不同开源自模型对压缩工具的使用不均匀，仅在两类任务验证，未测试复杂长周期场景
- 依赖注意力得分筛选可疑片段，可能漏检注意力占比低的隐蔽恶意指令，存在漏检风险。
- 方法依赖局部正则性假设，跨不同场景模型的泛化性未充分验证，黑盒部署依赖迁移效果。
- 面向用户的计算机使用智能体普遍存在高概率隐私泄露，落地存在严重隐私安全风险。
- 工业界采用氛围编码开发会引入大量未被发现的应用安全隐患，增大落地后的安全风险。
- 仅提出评估基准未给出落地方案，结论在不同工业场景的泛化性未进一步验证。

## 代码资源

- [MacAgentBench: Benchmarking AI Agents on Real-World macOS Desktop](https://github.com/JetAstra/MacAgentBench.) · 43 stars
- [EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions](https://github.com/FrontisAI/EnterpriseClawBench) · 25 stars
- [OPID: On-Policy Skill Distillation for Agentic Reinforcement Learning](https://github.com/jinyangwu/OPID) · 21 stars
- [MedGuards: Multi-Agent System for Reliable Medical Error Detection and Correctio...](https://github.com/congboma/MedErrBench.) · 2 stars
- [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How Supervisory Sig...](https://github.com/hypasd-art/Tool-RL-Box.)

## 常见基线方法

- **摘要未提及**：2 篇
- **Codex with GPT-5.5**：1 篇
- **固定间隔上下文压缩**：1 篇
- **无上下文压缩基线**：1 篇
- **直接LLM扫描**：1 篇
- **关键词与正则匹配**：1 篇
- **SkillSpector**：1 篇
- **Cisco Skill Scanner**：1 篇
- **基于注意力的基线方法**：1 篇
- **直接LLM裁判基线（GPT-5.5 xhigh reasoning）**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **ALFWorld**：3 篇
- **EnterpriseClawBench**：1 篇
- **大五人格数据集**：1 篇
- **竞赛数学基准**：1 篇
- **智能体搜索基准**：1 篇
- **第三方Agent技能市场**：1 篇
- **本文发布的恶意Agent技能标注数据集**：1 篇
- **提示注入基准任务**：1 篇
- **隐私泄露基准任务**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*