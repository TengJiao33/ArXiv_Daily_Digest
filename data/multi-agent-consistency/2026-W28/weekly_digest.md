# 多 Agent 交互与一致性 — 2026-W28 (07/06-07/12)

本周新增 **45** 篇论文，**4** 篇附带代码。优先级：high 15 / medium 22 / low 8。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [A hierarchical memory architecture overcomes context limits in l...](http://arxiv.org/abs/2607.07666v1) | multi-agent coordination | 104次运行中项目中期上下文中位数仅301token，跨不同大模型、不同提示均能保持稳定的模... | 通过分层记忆架构管控上下文规模，由领域专家PI智能体监督约束，保障长周期运行稳定... | 仅在药代动力学建模领域验证，跨领域通用性未得到充分验证 | — |
| 2 | high | - | [Agent Delivery Engineering Predictive Reliability Framework](http://arxiv.org/abs/2607.07689v1) | agent harness | 检测到被正常表层指标掩盖的退化“虚假繁荣”，指数法预测MAE=1.228，方向准确率76.8... | 聚合多层面异质信号生成信任裕度指标，提前预测系统健康轨迹，预警可靠性风险，管控多... | 16/20输入因子依赖ADE收集的数据，对非ADE部署场景的泛化... | — |
| 3 | high | - | [Beyond the Leaderboard: A Synthesis of Tool-Use, Planning, and R...](http://arxiv.org/abs/2607.05775v1) | survey | 失效随任务长度非线性叠加，单个子任务强性能无法保证端到端成功，额外支撑不能持续提升可靠性。 | 构建统一的大语言模型智能体失效分类体系，为后续改进智能体可靠性提供方向参考。 | 大语言模型智能体端到端可靠性不足，任务长度增加失效非线性上升，难... | — |
| 4 | high | - | [Decision Protocols in Multi-Agent Large Language Model Conversat...](http://arxiv.org/abs/2607.05477v1) | multi-agent coordination | 共识协议在知识密集型域表现更优，投票与裁判协议更适配逻辑任务，增加响应多样性可提升决策质量。 | 通过设计投票、共识、裁判三类决策协议，规范多智能体协作决策过程，优化输出结果质量... | 多智能体讨论决策过程会增加测试时间开销，提升了实际落地部署的时间... | — |
| 5 | high | - | [Formal Mechanisms for Market Stability in Self-Interested Agent ...](http://arxiv.org/abs/2607.08652v1) | multi-agent coordination | 最优对抗攻击仅使调解机制下诚实智能体效用降低13.3%，无法摧毁市场，调解可在持续对抗压力下... | 引入形式化调解机制约束自利智能体行为，抵御对抗攻击，维持多智能体市场的合作稳定。 | 仅在固定规模的模拟场景验证，未测试更大规模复杂场景下的通用性 | — |
| 6 | high | - | [LLM Agents for Deliberative Collaboration: A Study on Joint Deci...](http://arxiv.org/abs/2607.06157v1) | evaluation/benchmark | 即使借助外部数学工具，当前最优LLM仍可能在信息对齐或决策推理环节失败，但商议可带来纠错机会... | 通过形式化问题定义，构建基准与评测协议，依托商议过程帮助智能体对齐信息、实现错误... | 当前LLM在复杂商议协作任务中可靠性不足，易在核心环节出错，无法... | — |
| 7 | high | - | [MUTE: Return-Preserving Communication Unlearning for Efficient M...](http://arxiv.org/abs/2607.03473v1) | multi-agent coordination | 通过价值引导的消息遗忘，可在多智能体环境实现80%-90%带宽缩减同时保持和SOTA相当的性... | 通过基于注意力的反事实消息价值估计，选择性遗忘低价值消息传输，兼顾通信稀疏性与原... | 未给出具体公开基准，方法依赖预训练无约束策略，泛化能力未得到充分... | — |
| 8 | high | - | [Rethinking Scientific Discovery in an Agentic Era](http://arxiv.org/abs/2607.03863v1) | agent harness, multi-age... | SCION在科学研究任务的分解、验证、细化和记忆复用环节，表现显著优于现有自主研究智能体基线... | 通过元Harness整合各类研究要素，依靠带验证检查点的REP分解任务，结合管控... | 未披露大规模真实科学研究的落地成本与长期稳定性，方法泛化性有待进... | — |
| 9 | high | - | [Social Networks of LLM Agents](http://arxiv.org/abs/2607.03695v1) | multi-agent coordination | 狭窄注意力会引发羊群效应，有效样本量不随群体规模增长；仅无向正则度图中宽注意力可实现群体智慧... | 通过提出SNLA框架建模LLM智能体间的实际影响力，揭示注意力对群体共识形成的影... | 核心结论仅针对特定结构的曝光图得出，实际网络结构复杂，结论泛化性... | — |
| 10 | high | - | [Swarm-Driven Multi-Agent Reasoning for Smart City Security](http://arxiv.org/abs/2607.03628v1) | multi-agent coordination | TPSC-Sec共识接受率达0.97±0.02，自适应选择可减少50%活跃智能体，同时提升系... | 通过群体共识机制强化合理假设抑制矛盾，加入验证校准和分歧自适应控制，降低推理不一... | 未公开具体数据集与基线对比，在真实智慧城市场景的落地有效性有待验... | — |
| 11 | high | - | [TACTIC-KG: Toward Small Agent Teams for Cyber Threat Intelligenc...](http://arxiv.org/abs/2607.05001v1) | multi-agent coordination | 采用3B-8B轻量模型的专业化分工多智能体，在多项核心指标上均优于更大规模的整体式ICL基线... | 通过任务分解得到模块化专业智能体，引入验证模块，使用轻量大模型提升稳定性与一致性... | 仅在人工标注CTI数据集上评测，未验证大规模真实场景下的泛化性，... | — |
| 12 | high | - | [Think Big, Search Small: Where Capacity Matters in Hierarchical ...](http://arxiv.org/abs/2607.07548v1) | multi-agent coordination | 扩容委托角色可提升精确匹配约11个百分点，扩容执行子智能体仅提升约2.6个百分点，容量敏感度... | 拆分角色固定混杂变量，对执行子智能体采用质量过滤轨迹蒸馏，通过优化容量分配提升性... | 仅在多跳QA任务验证，未在其他多智能体搜索场景验证，泛化性有待确... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **multi-agent coordination**：19 篇
- **evaluation/benchmark**：10 篇
- **agent harness**：5 篇
- **unlearning/safety**：3 篇
- **policy optimization**：2 篇
- **survey**：2 篇
- **model steering**：1 篇
- **tool-use control**：1 篇
- **agent harness, multi-agent coordination**：1 篇
- **multi-agent simulation**：1 篇

## 失败模式与风险信号

- 传统多智能体强化学习忽略策略交互的底层市场拓扑，导致算法性能较差
- 现有智能体记忆防御可被针对推理历史的投毒攻击轻易绕过
- 整体式大语言模型构建知识图谱存在成本高、可控性差、性能不稳定、一致性差的问题
- 长时域任务中智能体轨迹忽略，中间步骤偏离目标遗忘交互历史
- 工具误用，包括跳过必要工具、忽略工具结果、编造输出、不必要调用工具
- 对工具使用智能体的知识库访问行为预判错误
- 步级优势估计对分组方式敏感，分组方案难以兼顾公平性与对比信号完整性
- 幻觉级联、无限循环、提示注入攻击
- 现有AIoT系统缺乏全系统级的实时推理与自主协作能力
- 结构化工具调用错误率高，易引发重试协调开销，降低代理系统整体可靠性

## 评测信号

- 在两个复杂度递增的高铁定价场景中，所提框架的收益和稳定性均优于关系型和非关系型对比基线方法。
- FARMA基线条件下攻击成功率最高达100%，可击败现有防御；SENTINEL可将成功率降至0%且无假阳性。
- 在人工标注CTI报告上，TACTIC-KG在抽取F1、分类准确率、结构图相似度三项指标上均优于更大规模的整体式ICL基线。
- 在三个公开智能体任务基准上评测，STAPO取得当前最优性能，同时大幅缓解了轨迹忽略问题。
- 最优模型干净工具使用率仅为86.33%，忠实工具使用仍未饱和，整体得分相近的模型失败模式差异显著
- 对照金标准盲评，渐进式披露回答质量非劣于基线，访问成本可降低三分之一到一半以上。
- 在相当计算开销下验证ProGPO相比基线的性能提升，同时测试方法在不同参数规模大模型上的可扩展性。
- 提出的四条多智能体缩放定理的定性预测结果，与已发表多智能体基准结果保持一致。
- NLT相较结构化工具调用在准确率、错误率、token开销上优势显著，优势幅度随模型能力提升而减小
- 在多个科学研究任务中，SCION整体性能优于现有基线，在任务分解、验证等环节优势尤为突出。

## 控制机制 / Harness 信号

- 通过实体图建模编码实体间竞争、协作与连接关系，改进多智能体强化学习的特征提取过程，提升学习效果。
- 提出分层防御流程SENTINEL，核心推理卫士通过五个加权信号分析推理条目，检测伪造以抵御投毒攻击。
- 通过任务分解得到模块化专业智能体，引入验证模块，使用轻量大模型提升稳定性与一致性，降低部署成本。
- 通过归一化熵定位轨迹忽略相关异常步骤，结合轨迹感知奖励与独立惩罚优化策略，提升智能体轨迹感知能力与训练稳定性。
- 提出诊断工具使用失败的标准化基准，通过评测定位不同模型工具使用的具体问题，为行为改进提供反馈
- 通过将知识库改造为渐进式披露访问结构，控制仅访问结构差异开展消融，优化LLM访问成本。
- 通过改进步级分组策略优化的优势估计，设计上下文一致的动作对比方案，融合状态势信号提升智能体学习性能与可靠性。
- 借鉴系统生物基序设计可组合智能体架构，加入认知拓扑层实现误差抑制，提升智能体可靠性。
- 梳理智能体物联网的整体架构框架，为构建具备自主协调能力的分布式多智能体生态提供参考。
- 采用自然语言工具（NLT）替代传统结构化工具调用，从源头减少工具调用错误，降低系统协调开销

## 可靠性 / 落地风险

- 仅在特定高铁定价实验环境验证，方法通用性不足，落地适用性有待进一步验证。
- 带持久记忆的智能体推理历史易被投毒操控，现有常见防御均失效，威胁运行可靠性。
- 仅在人工标注CTI数据集上评测，未验证大规模真实场景下的泛化性，存在落地不确定性。
- 仅在三个中等规模任务基准验证，未在更大规模更长时域的复杂真实任务验证有效性。
- 现有评估无法定位具体工具使用失败，容易高估模型可靠性，会影响基于工具调用的智能体落地效果
- 仅基于单个特定知识库开展实验，结论的普适性有待更多场景验证。
- 仅在两个中小基准任务验证，未验证方法在大规模复杂交互场景下的有效性与稳定性。
- 仅验证定性结论符合已有基准，缺乏实际任务下的性能与可靠性实证测试。
- 仅为范式梳理与综述研究，未经过实际落地验证，技术可行性缺乏实证支撑。
- 在深度优化的高能力前沿大模型上，NLT优势不明显甚至反转，适用场景存在局限

## 代码资源

- [UniClawBench: A Universal Benchmark for Proactive Agents on Real-World Tasks](https://github.com/HKU-MMLab/UniClawBench.) · 6 stars
- [Multi-agent Autoformalization of Tensor Network Theory](https://github.com/LionSR/TNLean) · 3 stars
- [Relational Multi-Agent Reinforcement Learning for Dynamic Pricing in High-Speed ...](https://github.com/Kinrre/RelationalRailPricing-RL)
- [FirstResearch: Auditable Question Formation for LLM Scientific Discovery Agents](https://github.com/louiswang524/FirstResearch.)

## 常见基线方法

- **单智能体基线**：2 篇
- **关系型基线方法**：1 篇
- **非关系型基线方法**：1 篇
- **关键词过滤**：1 篇
- **A-MemGuard**：1 篇
- **更大规模整体式上下文学习(ICL)基线**：1 篇
- **近期现有最先进系统**：1 篇
- **Llama-3.1-70B**：1 篇
- **Qwen2.5-72B**：1 篇
- **大型整体索引基线**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **ALFWorld**：2 篇
- **WebShop**：2 篇
- **高铁定价强化学习环境**：1 篇
- **人工标注网络威胁情报(CTI)报告**：1 篇
- **Search-Augmented QA**：1 篇
- **ToolFailBench**：1 篇
- **709页LLM维护的真实markdown维基知识库**：1 篇
- **材料分析**：1 篇
- **分子设计**：1 篇

---
*自动生成于 2026-07-12 | ArXiv_Daily_Digest*