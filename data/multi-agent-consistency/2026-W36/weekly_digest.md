# 多 Agent 交互与一致性 — 2026-W36 (08/31-09/06)

本周新增 **64** 篇论文，**2** 篇附带代码。优先级：high 30 / medium 24 / low 10。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [FaVOR: LLM-Based Agentic Framework for Factor Mining via Empiric...](http://arxiv.org/abs/2608.30192v1) | consistency detection | 基于假设层级证据、三阶段一致性构建的因子，相比仅优化收益的方法，跨市场区间更鲁棒、经济含义清... | 通过分解、验证、整合三阶段一致性循环，绑定因子数学形式与经济逻辑，保障结果一致性... | 仅在两个股指数据集验证，未验证更多市场场景的泛化能力，评测覆盖范... | ✅ |
| 2 | high | - | [Harness-RL: Black-Box Reinforcement Learning with Action-Args De...](http://arxiv.org/abs/2608.29641v1) | policy optimization | 七个基准上Qwen2.5-1.5B平均F1达42.93，Qwen2.5-3B达47.79，该... | 通过动作与参数解耦，将策略梯度分区路由到对应参数子空间，结合黑盒轨迹建模优化中心... | 仅在1.5B、3B小参数模型上验证，仅覆盖问答检索任务，泛化能力... | ✅ |
| 3 | high | - | [A Case Study on Emergent Cheating and Whistleblowing in Autonomo...](http://arxiv.org/abs/2609.04170v1) | multi-agent coordination | 在100个LLM智能体构成的透明共享研究群体中，作弊会因竞争压力自发传播，同时也会自发涌现反... | 提出采用分级制裁、集体选择规则等制度机制，支撑自主群体的去中心化自我治理，管控不... | 自主智能体群体行为不确定性高，提出的治理机制有效性未得到充分验证 | — |
| 4 | high | - | [AI agents reshape consensus formation in human groups](http://arxiv.org/abs/2609.02122v1) | multi-agent coordination | LLM智能体占比不同形成三种共识区间：低占比人主导共识、中占比破坏收敛、高占比恢复为智能体主... | 通过调整混合群体中LLM智能体的占比探究共识变化，指出占比和透明度是系统设计的核... | 结论基于特定人工实验场景，尚未验证在真实复杂场景下的泛化有效性，... | — |
| 5 | high | - | [Agents That Model Agents: Five Principles Toward a Theory of Min...](http://arxiv.org/abs/2609.01779v1) | multi-agent coordination | 仅深度为2的心理理论可恢复正确动作，认知信噪比可隔离获多数邻居认同的幻觉智能体，谱间隙决定一... | 通过心理理论建模邻居智能体信念，基于认知通道框架和五大原则阻止幻觉传播，提升系统... | 仅在电信特定场景的小规模模型上验证，通用性未得到验证，落地范围有... | — |
| 6 | high | - | [ArcticSwarm: Deferring Early Consensus in Long-Horizon Multi-Age...](http://arxiv.org/abs/2609.01870v1) | multi-agent coordination | 限制证据收集阶段的同伴信息读取、强化承诺边界可拓宽搜索，Qwen 3.5-27B在Brows... | 通过门控隔离限制智能体在证据收集阶段获取同伴信息，设置承诺边界做结构化评审，筛选... | 多子智能体架构会提升搜索成本，未验证该方法在更多类型任务上的通用... | — |
| 7 | high | - | [Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agen...](http://arxiv.org/abs/2608.30373v1) | evaluation/benchmark | 不对称角色提示引发严格立场主导，产生共识无法修正的系统性下行偏差，去除角色不对称可基本恢复人... | 通过消融实验定位多Agent主观评测性能下降的根源，提出去除角色不对称的对称MA... | 现有多Agent主观评测方法存在系统性偏差，评测结果不符合人类判... | — |
| 8 | high | - | [Bilevel Coordinated Reflection: A Game-Theoretic Approach to Mul...](http://arxiv.org/abs/2609.02750v1) | multi-agent coordination | 仅观测生成文本的验证门无法均匀提升性能，基于Kimi的系统在SWE-bench解决率达72.... | 通过博弈论建模多智能体交互，采用环境接地评估筛选候选记忆，通过随机反思优化改进协... | 仅在编码任务SWE-bench上验证，方法在其他多智能体任务的泛... | — |
| 9 | high | - | [CM2: Multimodal Cultural Reasoning via an Integrated Multi-Agent...](http://arxiv.org/abs/2608.30498v1) | multi-agent coordination | 集成多模块的CM2框架相比CoT等现有范式，在多模态文化推理任务上获得稳定提升，且能实现有效... | 通过集成多功能模块的多智能体架构，结合奖励驱动反馈，实现跨模态冲突仲裁，改进推理... | 仅在单一基准开展实验，未验证方法的跨场景泛化能力，落地相关测试不... | — |
| 10 | high | ICML 2026 | [CauseCollab: Causal Unified and Modality-Agnostic Network for He...](http://arxiv.org/abs/2609.03818v1) | multi-agent coordination | 在模态差异较大的异构协作感知场景中，本文方法相比现有方法性能增益更显著，在两个公开基准上达到... | 从因果视角建模协议空间表征学习，解耦语义因素与模态混杂因素，通过统一转换器保证跨... | 仅在两个公开数据集验证，未测试大规模真实复杂场景下的泛化性与落地... | — |
| 11 | high | - | [Control-Data Flow Separation: Stable Prompt Optimization in Mult...](http://arxiv.org/abs/2609.00621v1) | agent harness | 分离控制流与数据流后，优化提示不会破坏执行协议，在多类任务中实现100%协议有效性同时稳定提... | 通过分离执行控制流与任务内容数据流，将执行协议转为可验证程序对象，仅开放内容部分... | 需要为执行协议单独开发类型化可验证程序对象，增加了多智能体系统的... | — |
| 12 | high | - | [EDGE: Engine for Deterministic Graph Evaluation through Conversa...](http://arxiv.org/abs/2608.29971v1) | evaluation/benchmark | 采用AgentGraph、LangGraph这类带显式结构化节点转移配置的智能体，行为确定性... | 通过图结构DSL定义显式结构化节点转移约束智能体行为，构建评估框架量化行为的一致... | 穷尽枚举所有对话路径的评测成本高，难以适配大规模复杂多智能体编排... | — |

## A 会 / Venue 标签

- **ACL 2026**：1 篇
- **ICML 2026**：1 篇

## 方法族分布

- **multi-agent coordination**：32 篇
- **evaluation/benchmark**：12 篇
- **agent harness**：6 篇
- **unlearning/safety**：4 篇
- **policy optimization**：3 篇
- **consistency detection**：2 篇
- **agent harness, evaluation/benchmark**：1 篇
- **agent harness, multi-agent coordination**：1 篇
- **skill architecture**：1 篇
- **survey**：1 篇
- **other**：1 篇

## 失败模式与风险信号

- 全智能体反思模式下，正常智能体记忆会被错误见解污染，失败无法得到针对性修正。
- 稀疏终端奖励下细粒度信用分配不准确，浪费验证器内部任务结构信息。
- 传统人工与单算法文献分析效率低、可扩展性差、领域适配性不足
- 现有防御无法适配新型提示注入攻击变体，存在效率精度适应性三者难以兼顾的缺陷
- 现有方法结构知识不对齐，知识密集型任务存在冗余交互、验证不足
- 静态智能体harness能力扩展性差，无法根据任务运行新证据动态调整执行决策。
- 现有模型卡结构不统一、大量缺失，导致模型难以开展对比与解读
- 个体价值建模语义碎片化、价值体系缺乏内在一致性，静态评估无法适配动态交互场景
- 大语言模型临床应用易产生幻觉事实、无依据推荐和引用错误
- 语义漂移、确认偏误、信息过载遗漏关键紧急指征

## 评测信号

- 在三个基准数据集上，初始成功率相比基线分别提升22%、26%、27%，低资源设置下仍能保持良好性能。
- 在两个基准任务上对比基线验证性能提升，通过消融实验验证所提机制设计的必要性。
- 在包含32642篇中英双语气候-健康文献的测试集上，该框架核心信息提取任务F1分数达到0.92，性能良好。
- 在新型注入攻击基准上，CAITLYN的自主合成防御可大幅降低攻击成功率，性能对标SOTA且token开销更低。
- 在专家级GPQA数据集上，K-GAT相比LLM-Debate基线准确率提升15.7%，计算token消耗不到基线的一半。
- 在两个长周期编码基准上，任务性能分别达到82.6%和87.19%，相比官方榜单最优结果提升3.4和3.39个百分点。
- MCTidy信息保留充分、幻觉少、跨运行稳定性强；MCGenie生成语义相似度均值约0.9，超一半完全正确
- 该框架达到90.78%的价值还原保真度，价值泛化较基线提升5.3%，人格区分度与行为一致性优于基线方法。
- 未给出具体量化评测结果，仅验证了该框架具备可靠、可审计、隐私保护的实用特性。
- 在真实医疗病历上的实验显示，MASGR性能显著优于现有基线，复杂医疗转诊案例的性能提升尤为明显。

## 控制机制 / Harness 信号

- 通过自动故障归因定位出错智能体，仅要求出错智能体做针对性反思，避免错误污染正常智能体记忆。
- 借助验证器内部结构，沿依赖证明边追溯动作信用并重新分配优势，改进大语言模型智能体训练。
- 通过中心协调模块调度不同专用智能体，采用四层幻觉控制策略结合人工验证，保障分析结果的准确性与可靠性。
- 以与智能体无关的中间件形式，通过两级模块防御已知注入攻击，通过异常监控模块自主合成新防御应对新型攻击。
- 通过将外部证据整合进自回归图生成，知识条件化学习协作拓扑，缓解结构与知识不对齐问题，提升任务性能。
- 通过设计可组合的开源智能体harness，基于任务运行产生的新证据动态调整上下文、反馈与任务控制逻辑。
- 本文不涉及对模型或智能体行为的控制，聚焦模型卡的标准化整理与自动生成工作
- 通过多个社会学专家智能体对调查回答做深度语义重构，生成一致个体价值画像，引入多智能体辩论评估一致性。
- 引入结合规则检查与大语言模型文本蕴含的混合验证层，验证输出合规性，提升系统可靠性与可审计性。
- 通过结构化临床推理图强制智能体建立显式逻辑连接，采用知识引导的仲裁机制保障决策合规。

## 可靠性 / 落地风险

- 若故障归因错误定位错误智能体，会导致真实错误无法修正，遗留多智能体协作的潜在问题。
- 方法依赖终端验证器内置的任务相关结构，泛化到无对应结构的任务时效果会受限。
- 依赖人工验证环节增加人力成本，仅在单一领域验证，跨领域泛化能力未得到验证。
- 自主合成的新防御未经过充分验证，面对未知攻击的稳定性和正确性存在不确定性。
- 仅在有限的知识密集型基准验证，未测试该方法在更多类型多智能体任务中的通用性。
- 仅在公开编码基准完成验证，尚未在大规模工业级复杂代码任务中测试，通用性待验证。
- 生成质量高度依赖模型配套支撑资源尤其是关联论文，缺乏对应资源时生成质量无法保障
- 依赖14个专家智能体运行，推理成本较高，未提及专家智能体自身偏差对结果的影响。
- 未经过大规模临床场景验证，实际应用中的临床有效性和可靠性有待进一步检验。
- 未使用公开通用基准评测，方法在非医疗领域的泛化性还有待验证。

## 代码资源

- [Harness-RL: Black-Box Reinforcement Learning with Action-Args Decoupling for Cen...](https://github.com/jiangxinke/Harness-RL.) · 435 stars
- [FaVOR: LLM-Based Agentic Framework for Factor Mining via Empirical Validation](https://github.com/damilab/FaVOR.)

## 常见基线方法

- **Reflexion**：1 篇
- **Retroformer**：1 篇
- **COPPER**：1 篇
- **仅结果训练**：1 篇
- **现有细粒度信用分配方法**：1 篇
- **大语言模型裁判基线**：1 篇
- **静态基线**：1 篇
- **LLM-Debate**：1 篇
- **官方排行榜最优基准方法**：1 篇
- **机械拼接调查响应法**：1 篇

## 常用数据集

- **SWE-bench Verified**：2 篇
- **Terminal-Bench 2.1**：2 篇
- **摘要未提及**：2 篇
- **HotPotQA**：1 篇
- **ChartQAPro**：1 篇
- **Mind2Web**：1 篇
- **ALFWorld**：1 篇
- **WebShop**：1 篇
- **1993-2023年覆盖中国的32642篇中英双语气候-健康文献语料**：1 篇
- **标准基准**：1 篇

---
*自动生成于 2026-09-06 | ArXiv_Daily_Digest*