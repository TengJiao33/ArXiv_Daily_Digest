# Agent Skills 与 Harness — 2026-W26 (06/22-06/28)

本周新增 **93** 篇论文，**5** 篇附带代码。优先级：high 61 / medium 27 / low 5。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 控制/评测 | 风险 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|------|-----------|:----:|
| 1 | high | - | [EnterpriseClawBench: Benchmarking Agents from Real Workplace Ses...](http://arxiv.org/abs/2606.23654v1) | evaluation/benchmark | 通过构建带多维度标注的标准化评测基准，提出多维度评测协议，规范企业智能体的能力评... | 基准原始数据未公开，第三方无法直接复现原实验，难以验证论文得到的... | 能否基于该论文的评测协议，构建小规模开源中文企业场景agent评测基准，验证不同harnes... | ✅ |
| 2 | high | - | [MacAgentBench: Benchmarking AI Agents on Real-World macOS Deskto...](http://arxiv.org/abs/2606.22557v1) | evaluation/benchmark | 通过构建带细粒度多检查点评分的评测基准，为桌面智能体能力评估提供反馈支撑。 | 仅覆盖macOS平台，对其他桌面系统通用性不足，评测范围存在一定... | 基于MacAgentBench研究技能库对桌面Agent性能的影响，探索轻量工业友好的桌面A... | ✅ |
| 3 | high | - | [MedGuards: Multi-Agent System for Reliable Medical Error Detecti...](http://arxiv.org/abs/2606.25651v1) | agent harness | 将医疗错误检测纠正任务拆分给多个专用智能体，通过置信度引导仲裁解决分歧，无需额外... | 仅在公开医疗文本数据集验证，未在真实临床落地场景测试，实际效果待... | 能否将这种无需微调的多智能体置信度仲裁护栏方案，推广到通用领域Agent的输出可靠性保障？ | ✅ |
| 4 | high | - | [OPID: On-Policy Skill Distillation for Agentic Reinforcement Lea...](http://arxiv.org/abs/2606.26790v1) | online distillation | 从同策略轨迹提取分层技能生成稠密令牌级监督，结合结果优势优化策略，改进智能体决策... | 仅在中小规模任务基准测试，未验证大规模真实场景下的稳定性与适配性 | 可将该同策略分层技能蒸馏思路推广到工具调用场景，优化多轮工具交互的决策效率 | ✅ |
| 5 | high | - | [Why Multi-Step Tool-Use Reinforcement Learning Collapses and How...](http://arxiv.org/abs/2606.26027v1) | tool-use control | 引入多种监督信号，采用监督微调与强化学习交错训练，修正控制token概率异常，提... | 分布外泛化性能较差，未在真实任务验证，落地应用存在一定不确定性。 | 如何基于该方法设计低算力的稳定多步工具调用agent训练方案，适配工业demo落地需求？ | ✅ |
| 6 | high | - | [A Deterministic Control Plane for LLM Coding Agents](http://arxiv.org/abs/2606.26924v1) | agent harness | 在现有harness之上新增确定性控制平面，通过内容寻址、层级权限、可追溯、漂移... | 仅在人工注入违规的测试中验证机制，缺乏真实开发者场景的落地效果验... | 可基于该思路构建开源通用的确定性Agent控制平面，适配多场景，打造工业友好的可控Agent... | — |
| 7 | high | - | [A Process Harness for Uplifting Legacy Workflows to Agentic BPM:...](http://arxiv.org/abs/2606.27188v1) | agent harness | 通过在原有确定性工作流引擎外部增设策略管控的智能体线束层，拦截指定控制点实现管控... | 仅在单一场景验证，未经过多类大规模业务场景测试，落地通用性有待验... | 能否基于该流程线束思路，构建面向国内企业遗留业务系统的低成本智能体升级改造管控框架 | — |
| 8 | high | - | [A Stackelberg Framework for Resource-Aware LLM Agents: Learning,...](http://arxiv.org/abs/2606.23026v1) | agent harness | 通过斯塔克尔伯格博弈建模资源治理问题，优化策略后结合真实API校准完成策略修复与... | 仅开展300轮小规模实验，理论结果为条件性，未得到经认证的真实系... | 如何将该博弈资源管控框架适配到多工具调用场景，实现低算力工业级Agent？ | — |
| 9 | high | - | [A Survey on Multi-Agent LLM Frameworks with Semantic Memory Inte...](https://www.semanticscholar.org/paper/21c04ba4ed923d1984fb6dd10f4e2681dbaf854a) | survey | 通过梳理现有多智能体的DAG编排、语义记忆集成等架构，归纳核心问题，明确领域评估... | 领域缺乏统一系统设计标准与标准化评估方法，可落地性缺乏验证，工业... | 能否设计低协调开销、具备故障检测能力的标准化动态DAG多智能体harness框架，适配工业落... | — |
| 10 | high | - | [ATRIA: Adaptive Traceable ECG Reporting with Iterative Agents](http://arxiv.org/abs/2606.24392v1) | multi-agent coordination | 通过将每个报告断言绑定对应证据，支持迭代修正单个结果，复用已有临床可信模型保障输... | 无大规模量化评测验证效果，仅靠案例演示，临床实际落地还需要更多有... | 能否将这种迭代可追溯的多智能体harness框架推广到更多专业领域文档生成任务，提升输出可修... | — |
| 11 | high | - | [Adaptive Evaluation of Out-of-Band Defenses Against Prompt Injec...](http://arxiv.org/abs/2606.26479v1) | evaluation/benchmark | 提出自适应攻击评测协议，验证带外确定性中介机制对提示注入防御的鲁棒性。 | 多数现有带外防御未经过自适应攻击验证，实际部署存在潜在安全漏洞。 | 可扩展开展各类主流带外防御的自适应攻击测评，为工业界agent防御选型提供参考。 | — |
| 12 | high | - | [AgentLens: Interpretable Safety Steering via Mechanistic Subspac...](http://arxiv.org/abs/2606.22673v1) | model steering | 基于机制可解释性定位安全相关的隐藏表示子空间，运行时检测风险并干预子空间，调控不... | 仅在小规模自建基准上验证，尚未验证更大模型与真实复杂编码场景的效... | 能否将这种低开销的机制子空间调控方法推广到通用工具智能体的安全控制中？ | — |

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

## 可延展 Idea Hook

- 可探索将文本层结构化变异的智能体控制思路，迁移到agent工具调用的可控多样性设计中
- 可基于该评测基准，探索面向工业级多智能体系统的低成本提示优化可控框架，可做可复现demo。
- 能否基于该论文的评测协议，构建小规模开源中文企业场景agent评测基准，验证不同harness方案的性能？
- 可以将这种限定智能体角色、结论锚定可靠源的harness思路，推广到通用智能体任务抑制幻觉影响。
- 探索将该无需训练的自适应压缩方案集成到长周期任务智能体，降低工业落地的推理成本
- 可扩展该方法到MCP生态的第三方工具恶意检测，探索低算力下规模化检测工业场景恶意工具的可行性。
- 将几何信息流控制集成到Agent工具调用框架中，验证轻量安全防护方案的落地效果。
- 能否基于上下文完整性规则设计agent控制harness，降低计算机使用智能体的隐私泄露风险？
- 能否设计面向AI Agent编码的安全约束harness，减少氛围编码生成应用的常见安全漏洞？
- 基于AFTER基准，能否设计面向工业场景的低算力可复现LLM Agent程序记忆管理控制框架？
- 探索将分歧点偏好学习推广到工业级多工具调用场景，实现agent工具能力的低成本自进化。
- 可基于本文双环境互补训练思路，探索低算力可复现的移动端智能体harness方案，适配工业落地需求

## 下次可问导师的问题

- 这种文本层引入结构约束的智能体工作流思路，能否迁移到agent可控性优化场景中？
- 我们是否可以基于该基准，开发适配工业需求的低成本多智能体提示优化控制方案？
- 我们要不要基于这篇论文的协议，构建小规模开源中文企业场景agent评测基准做后续研究？
- 这种分离智能体辅助任务与核心结论的角色约束思路，能否推广到通用智能体可靠性提升？
- 我们能不能基于这个思路做一个面向长对话智能体的低成本自适应压缩演示Demo？
- 我们是否需要跟进这个方向，开发适配第三方Agent技能平台的低成本恶意检测工具？
- 我们是否可以基于该思路，开发一个面向Agent工具调用的轻量安全控制可运行demo？
- 我们是否可以基于该基准开发轻量上下文隐私控制harness，验证约束的实际效果？
- 我们方向是否需要跟进AI Agent代码生成场景，开发对应的安全约束harness框架？
- 我们是否可以基于AFTER基准，开发适配工业需求的轻量可复现Agent程序记忆管理方案？
- 这种基于分歧点偏好学习的方法，能否适配我们当前的多工具调用agent开发框架？
- 我们是否可以基于该思路做一个低算力可演示的安卓端手机操作智能体demo？

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
*自动生成于 2026-06-28 | ArXiv_Daily_Digest*