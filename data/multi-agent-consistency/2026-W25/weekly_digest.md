# 多 Agent 交互与一致性 — 2026-W25 (06/15-06/21)

本周新增 **67** 篇论文，**3** 篇附带代码。优先级：high 29 / medium 31 / low 7。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Consensus-based Agentic Large Language Model Framework for Harmo...](http://arxiv.org/abs/2606.16987v1) | multi-agent coordination | 即使是先进大语言模型，HTS分类性能也从粗粒度章节级到细粒度编码后缀不断下降，10位精确分类... | 通过共识验证、分层级元素投票、置信度估计结合人工介入，优化规范多智能体分类推理行... | 实验基于私有数据集，无公开基准对比，方法在不同关税区域的泛化可靠... | ✅ |
| 2 | high | - | [A Neuro-Symbolic Approach to Strategy Synthesis for Strategic Lo...](http://arxiv.org/abs/2606.17962v1) | multi-agent coordination | 该生成-验证框架保留形式化可靠性，基于Qwen3-32B的验证流水线在策略合成任务上达到了9... | 采用生成-认证架构，以大语言模型作为策略生成器，结合形式化验证器验证生成策略，保... | 对于大规模多智能体场景，形式化验证的计算开销仍然较高，落地的扩展... | — |
| 3 | high | - | [AdaSTORM: Scaling LLM Reasoning on Dynamic Graphs via Adaptive S...](http://arxiv.org/abs/2606.16328v1) | multi-agent coordination | 该自适应多智能体框架可将LLM动态图推理扩展到千节点图，多场景下准确率超90%，显著优于七个... | 通过自适应分区匹配模型推理容量，结合时空解耦多智能体架构实现协作推理，突破规模瓶... | 未披露具体推理开销与延迟，未列出基线具体细节，可复现性存在一定不... | — |
| 4 | high | - | [AgentFinVQA: A Deployable Multi-Agent Pipeline for Auditable Fin...](http://arxiv.org/abs/2606.19782v1) | multi-agent coordination | 验证器置信信号有效，确认答案比修正答案准确率高12.6个百分点，近三分之二失败未被其有效检测 | 将问答任务分解为多智能体分工步骤，引入验证器生成置信判决，记录全流程轨迹实现可追... | 仅在单一基准评测，未验证真实金融场景下的合规性与方案鲁棒性 | — |
| 5 | high | - | [CAPRA: Scaling Feedback on Software Architecture Deliverables wi...](http://arxiv.org/abs/2606.18976v1) | multi-agent coordination | CAPRA在严格双评估者规则下满足88.8%的评估标准，与人类评估的kappa一致性为0.5... | 采用基于归一化莱文斯坦距离模糊匹配的确定性证据锚定，搭配一致性管理智能体交叉验证... | 仅在10份小规模样本上验证，结论泛化性不足，主观评估维度仍无法自... | — |
| 6 | high | - | [Contagion Networks: Evaluator Bias Propagation in Multi-Agent LL...](http://arxiv.org/abs/2606.20493v1) | evaluation/benchmark | 同模型智能体的偏差传染系数比跨模型弱3-5倍，评估委员会规模从1增至3可降低72.4%的有效... | 构建传染网络框架度量评估偏差传播，提出增大评估委员会规模抑制偏差传染，提升多智能... | 仅验证了小规模3智能体设置，更大规模复杂多智能体系统中的传播规律... | — |
| 7 | high | - | [Distributed General-Purpose Agent Networks: Architecture, Key Me...](http://arxiv.org/abs/2606.17368v1) | multi-agent coordination | 测试验证BAID风格分层验证的原型开销可控，MG-EigenTrust可适配跨主题伪装合谋攻... | 通过协议适配层为核心的分层架构，结合可验证身份信誉与语义传播机制，保障开放智能体... | 完全开放分布式网络的通信开销、节点动态性会影响可用性，实际落地部... | — |
| 8 | high | - | [EARS: Explanatory Abstention for Reliable Sub-Agent Modeling in ...](http://arxiv.org/abs/2606.18668v1) | multi-agent coordination | 引入子智能端侧带解释的弃权机制后，大规模多智能体电商助理的响应通过率从68.5%提升至78.... | 通过校准LLM法官集成生成子智能体失败模式标注，微调子智能体使其输出带理由的弃权... | 依赖LLM-as-Judge生成标注，跨领域泛化未验证，大规模场... | — |
| 9 | high | - | [Formal Verification of Learned Multi-Agent Communication Policie...](http://arxiv.org/abs/2606.19632v1) | unlearning/safety | 离散VQ-VIB消息比连续方法保真度高11.6-13.6个百分点，验证快3-4倍，安全性质迁... | 通过决策树蒸馏抽象原神经多智能体策略，使用概率模型检测器完成组合形式验证，保障策... | 依赖领域特定特征提取，蒸馏保真度未达100%，框架通用性未在更多... | — |
| 10 | high | - | [From Argument Components to Graphs: A Multi-Agent Debate with Co...](http://arxiv.org/abs/2606.16047v1) | multi-agent coordination | 仅对不确定样本辩论的选择性方案取得无训练方法最高Macro F1，全样本辩论的性能反而低于基... | 通过置信门控筛选不确定预测样本，依托多智能体辩论改进大模型推理结果，兼顾性能与效... | 仅在单论域数据集验证效果，泛化能力未测试，全场景应用时会出现性能... | — |
| 11 | high | - | [GeoDisaster: Benchmarking Orchestrated Agents for Operational Di...](http://arxiv.org/abs/2606.17246v1) | evaluation/benchmark | 现有RS-VLMs与通用智能体系统难以满足业务化灾害地理推理需求，RCEA可有效提升多智能体... | 通过显式执行契约规范多智能体协作，结合失败感知监督微调与契约强化学习对齐智能体行... | 基准与方法针对特定灾害领域，通用性有限，落地还需要适配更多不同的... | — |
| 12 | high | - | [Hidden Anchors in Multi-Agent LLM Deliberation](http://arxiv.org/abs/2606.19494v1) | multi-agent coordination | 仅当隐藏锚点远离初始观点时商议才能跳出初始信念凸包，锚点效应在开源模型中是连续谱而非全有全无... | 通过引入智能体自身的隐藏锚点信念，构建闭环动力系统建模多智能体商议过程，解释共识... | 仅做机制层面的建模验证，未在实际落地任务中测试模型的实用性与泛化... | — |

## 方法族分布

- **multi-agent coordination**：43 篇
- **evaluation/benchmark**：10 篇
- **agent harness**：4 篇
- **policy optimization**：2 篇
- **skill generation**：2 篇
- **tool-use control**：2 篇
- **model steering**：1 篇
- **consistency detection**：1 篇
- **online distillation**：1 篇
- **unlearning/safety**：1 篇

## 失败模式与风险信号

- 异构Agent跨环境协作失败，通信故障后消息丢失不可访问
- LLM智能体获得环境反馈后仍无法正确自我评估的反思失效
- 大模型原生配置易输出符合训练模式但违规危险的医疗内容
- 现有分散式安全屏蔽误排除仅靠协调才能实现的团队最优安全行为
- 多智能体跨机构通信隐私泄露
- 盲目扩展智能体规模或通信带宽仍无法提升多智能体任务成功率
- 单大语言模型单步自主分类难以处理模糊输入，细粒度分类精度不足
- 单一技能导致的搜索空间局限、同质次优解
- 错误信息在多智能体交互中传播扩散
- 翻译指称不一致、交互翻译错误导致下游协调失败

## 评测信号

- 实验结果显示，PCMA方法在多目标多智能体协作任务中，整体性能和权衡协调性均得到有效提升。
- 实验测得异构模型对的缺陷审查占比为69.8%，显著高于同构模型对的53.1%，验证方案有效性。
- 无需额外奖励模型、裁判或标注，同时降低智能体过度不自信率，提升文本转SQL任务的准确率。
- 原生大模型普遍存在高幻觉错误率，提出方法跨模型降低约53%幻觉错误率，提升临床输出安全性。
- 验证该方法能在保证端到端安全的前提下，有效提升团队奖励，恢复被现有方法排除的最优安全行为
- MedLatentDx相比原始潜在通信基线，提升跨医院罕见病诊断性能，同时降低了临床隐私内容泄露风险。
- 所有40份测试样本全部成功处理，处理准确率达到96.7%，单份成绩单处理耗时仅为45秒。
- 算法可在满足不同QoS约束的前提下提升硬件休眠时间，性能优于所有对比基线，支持快速适配变化的网络目标。
- 在合成实验和SWE-bench真实提交数据中，验证了多智能体成功概率随最小割代价上升指数衰减的结论。
- 在3300条专家标注数据集验证，先进LLM的HTS分类性能随分类粒度变细持续下降，10位精确分类难度大

## 控制机制 / Harness 信号

- 通过学习各智能体专属的协调偏好，引入合理偏好多样性优化团队决策，提升多目标场景下的协作效果。
- 通过基于文件的持久化消息存储结合两级通信路径，隔离不同Agent工作，提升异构协作可靠性。
- 基于环境反馈计算免费校准奖励，改进强化学习策略优化，提升智能体反思校准能力，实现智能体自验证。
- 通过事后对抗审计拦截危险输出，结合多智能体反馈循环验证大模型输出，降低幻觉提升医疗安全性。
- 基于线性时序逻辑安全片段构建契约组合屏蔽，结合非平稳多臂老虎机选择局部义务，约束动作保证全局安全
- 通过潜在KV蒸馏与跨族对齐，约束智能体仅传输不泄露隐私的压缩潜在表示，实现隐私保护下协作。
- 通过编排智能体管理各专用智能体的通信与结果调和，以GPA提取作为协调信号实现智能体协作质量控制。
- 通过全局奖励训练图神经网络，基于学习到的全局网络状态编码，为各基站分配协调的本地动作。
- 基于信息论分析提出多智能体系统设计准则，建议高最小割代价任务优先重构任务而非扩展规模。
- 通过构建智能体社交沙箱，采用平台无关交互单元，整合自动生成与用户自定义内容，实现多智能体空间协作

## 可靠性 / 落地风险

- 摘要未验证方法在大规模多智能体场景的泛化性，也未分析偏好协调的长期稳定性。
- 目前仅在自身开发项目验证，缺乏在更多不同规模第三方项目中的通用性验证。
- 仅在文本转SQL任务验证，方法通用性未得到验证，未测试在复杂通用任务上的效果。
- 仅在小规模自制数据集测试，未在真实大规模临床场景验证落地有效性。
- 未公开具体环境与基线细节，方法对大规模多智能体场景的扩展性未验证
- 异骨干LLM潜在对齐效果可能不稳定，隐私保护仅靠可重构内容验证，验证强度不足。
- 测试数据集仅含40份样本，规模较小，系统在更多差异化格式成绩单上的可靠性未经验证。
- 仅在仿真环境完成验证，未在真实工业网络场景测试，实际落地的有效性有待验证。
- 结论依赖任务可抽象为约束图的假设，真实开放场景的复杂任务未必满足该前提。
- 未给出实证评测结果，方案的实际可用性与稳定性未经验证，存在较大的落地不确定性

## 代码资源

- [Consensus-based Agentic Large Language Model Framework for Harmonized Tariff Sch...](https://github.com/Analytics-Everywhere-Lab/hts.) · 1 stars
- [Who Flips? Self- and Cross-Model Counterarguments Reveal Answer Instability in L...](https://github.com/nafisenik/WhoFlips) · 1 stars
- [Agentic Discovery of Non-Canonical Antimicrobial Peptides with AMPGAN v3](https://github.com/marszzibros/AMPGANv3)

## 常见基线方法

- **同构LLM Agent协作方案**：1 篇
- **基于共享运行时的多Agent协作方案**：1 篇
- **标准强化学习**：1 篇
- **原生 vanilla 大语言模型**：1 篇
- **原始潜在通信基线**：1 篇
- **先进基于图的基线方法**：1 篇
- **竞争性规则控制器**：1 篇
- **单智能体提示**：1 篇
- **投票决策**：1 篇
- **全量工具模式注入**：1 篇

## 常用数据集

- **ALFWorld**：2 篇
- **多个协作多目标多智能体环境**：1 篇
- **实际交通控制场景**：1 篇
- **自应用开发实验数据集**：1 篇
- **实际生产代码仓库环境**：1 篇
- **五个文本转SQL基准**：1 篇
- **自制103道临床多选题对抗禁药数据集**：1 篇
- **6种多智能体安全协调测试环境**：1 篇
- **CrossRare-Bench**：1 篇
- **美国13个州的40份真实高中成绩单**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*