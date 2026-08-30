# 多 Agent 交互与一致性 — 2026-W35 (08/24-08/30)

本周新增 **83** 篇论文，**5** 篇附带代码。优先级：high 41 / medium 32 / low 10。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Gover...](http://arxiv.org/abs/2608.21867v1) | agent harness | 持久化保存验证器信号作为记忆元数据可有效提升性能，在WebArena上相比Reasoning... | 通过将验证器信号持久化为记忆的生命周期元数据，在记忆全流程管控质量，避免错误记忆... | 验证器本身的错误会被持久化存储，长期运行可能持续污染记忆库，累积... | ✅ |
| 2 | high | - | [A Safety-Driven Architectural Framework for Fail-Operational Dro...](http://arxiv.org/abs/2608.20906v1) | multi-agent coordination | 当安全监控器满足C_monitor>0.9991时，SAIL IV场景理论上可达成每飞行小时... | 通过硬件隔离的安全监控器作为运行时保证网关，强制执行形式化安全契约，依托健康向量... | 仅完成理论建模验证，缺乏实际工程场景实测，实际落地可靠性待验证 | — |
| 3 | high | - | [A Theory of Post-hoc Debate Judgement](http://arxiv.org/abs/2608.19002) | multi-agent coordination | 两种辩论裁决方法的准确率表现相近，但大语言模型裁判不具备计算论辩语义的形式性质保障 | 提出事后辩论裁决的形式性质要求，引入基于计算论辩语义的裁判机制提升裁决可靠性 | 仅在主张验证场景验证，未覆盖更多类型的实际多智能体辩论应用场景 | — |
| 4 | high | - | [Adaptive Influence Graphs for Failure Attribution in Multi-Agent...](http://arxiv.org/abs/2608.24361v1) | agent harness | 更丰富的故障追踪表示可稳定提升归因效果，自适应图构建加智能体导向遍历能取得最优结果。 | 通过构建自适应影响图结构化故障追踪，引导智能体遍历定位关键错误，提升多智能体故障... | 仅在单个公开基准验证，方法在真实复杂场景下的归因效果尚未得到验证... | — |
| 5 | high | - | [Adversarial Review: Structured Disagreement for Grounded Agentic...](http://arxiv.org/abs/2608.18167) | multi-agent coordination | 仅3个智能体的AR在LiveCodeBench通过率超过五智能体基线，原生AR存在无证据虚假... | 引入结构化分歧机制，由评论智能体审核评审结果，避免虚假共识，以最小化协作降低多智... | 该方法仅在代码相关基准验证，通用性未在其他多智能体任务测试，适用... | — |
| 6 | high | - | [AgentDropout: Dynamic Redundancy Elimination for Multi-Agent Col...](https://www.semanticscholar.org/paper/739e8b9eb096c7948c756009f1323b2e382b4073) | multi-agent coordination | AgentDropout可比固定5智能体辩论保持相当或更高精度，降低38.0–43.5%令牌... | 通过计算智能体输出相对于群体共识的语义新颖性，动态停用得分低于自适应阈值的低贡献... | 仅在中小规模公开推理任务验证，未测试更大规模多智能体场景的稳定性... | — |
| 7 | high | - | [AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared...](http://arxiv.org/abs/2608.23740v1) | multi-agent coordination | 性能提升核心来自协调而非并行或CRDT合并，双智能体比单智能体少放弃任务，运行间差异更小 | 基于CRDT构建共享工作空间，提供文件级声明、状态广播等协调原语，管控多智能体并... | 仅在CLI稳定的前沿编码模型上验证，未覆盖更多场景，通用性有待进... | — |
| 8 | high | - | [Aligned Alone, Misaligned Together: Forecasting Adversarial Capt...](http://arxiv.org/abs/2608.22444v1) | unlearning/safety | 单智对齐的大模型群体可被少数坚定对抗智能体带偏，可基于无对抗行为提前预测，去除对抗后群体可恢... | 通过基于无攻击状态下群体行为校准响应函数，提前预测群体被对抗捕获的结果，实现安全... | 现有多智能体部署多沿用单智能体评估，无法提前识别群体层面对抗风险... | — |
| 9 | high | - | [Apodex 1.1: Scaling Agentic Intelligence for Complex Work](http://arxiv.org/abs/2608.23283) | multi-agent coordination | 参数量仅35B的Apodex 1.1 Mini尺寸远小于多数前沿系统，仍在多类复杂任务上保持... | 依托共享执行框架与AgentOS维护任务状态与溯源，通过环境扩展与协调训练提升智... | 未披露具体评测细节与可复现性信息，大规模多智能体协调的稳定性未明... | — |
| 10 | high | - | [Belief Cascades Drive Persuasion in LLM Agent Networks](http://arxiv.org/abs/2608.25152v1) | evaluation/benchmark | 直接暴露可可靠预测下一轮立场改变，未指定说服的智能体也能传递可测量的说服力，仅分析文本会遗漏... | 构建可控测试床研究说服行为，提出使用信念探测、暴露溯源、动作日志改进多智能体说服... | 仅依赖文本内容评估会得到偏差结果，无法准确识别智能体真实立场与人... | — |
| 11 | high | - | [Candidate supply and answer selection shape the value of LLM jud...](http://arxiv.org/abs/2608.25937v1) | multi-agent coordination | 结合答案频率与LLM评判仅修改终选规则，就将准确率从63.82%提升至70.82%-70.9... | 通过引入LLM评判输出答案正确性信号，结合答案频率修改终选规则，挽救被错误压制的... | 结论基于固定候选池重放得到，在端到端动态多智能体系统中的泛化性尚... | — |
| 12 | high | - | [Congestion-Aware Scheduling for Heterogeneous LLM-Agent Teams](https://www.semanticscholar.org/paper/90339aea366d0e19556fd6fbc6a4959e1541935e) | multi-agent coordination | 候选收缩策略可在保持任务性能的同时，降低拥塞场景下异构多智能体系统的平均及95分位等待时间。 | 通过拥塞感知的候选集收缩调度策略，平衡智能体能力与负载，引入稳定破局减少分配波动... | 仅在标准学术基准测试验证，未覆盖大规模真实工业场景的复杂任务需求... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **multi-agent coordination**：43 篇
- **evaluation/benchmark**：19 篇
- **agent harness**：6 篇
- **tool-use control**：4 篇
- **unlearning/safety**：3 篇
- **skill generation**：2 篇
- **policy optimization**：1 篇
- **技能检索**：1 篇
- **survey**：1 篇
- **multi-agent coordination, model steering**：1 篇
- **model steering**：1 篇
- **other**：1 篇

## 失败模式与风险信号

- 现有大模型无法从发明人非正式披露生成完整合法的专利申请
- 长轨迹运行中早期错误累积传播，现有运行时干预的成本与显存开销过高。
- 多智能体协调的非确定性不满足安全关键场景适航的确定性可靠性要求
- 信息缺失导致输出内容不达标，提示明确禁止缺陷反而会使残留缺陷集中在禁止类别
- 隐式场景下通信动作不适配、过早达成错误共识、通信效率低下
- 动态边缘网络联邦学习的大量轮次能耗浪费
- 经典流量模型无法适配多智能体大语言模型系统生成的内部流量
- 多分布式信源未体现出优于单信源的共识协调优势
- 任务分解粒度不当导致性能下降，幻觉错误对碎片化多智能体配置冲击更大
- 面对严格工具顺序、权限限制与意外运行错误时性能骤降，能力不可靠

## 评测信号

- 在Dis2Pat基准上，所提Patent-MAF基线性能优于评测的开源大模型，效果可媲美大规模闭源大模型。
- COTA在三个测试环境搭配三个actor的全部九个评估设置中均实现性能提升，效果优于所有对比基线。
- 经马尔可夫可靠性建模验证，满足条件的安全监控器可实现每飞行小时10^-7次危险故障的预定目标
- 无示例时40/55部分输出不弱于人类，68%缺陷源于信息缺失，结构化指令使答案质量从74%降至48%
- 覆盖12种开放/闭源权重大语言模型的实验显示，Consilience相比基线提升决策准确率与通信效率。
- 在非独立同分布CIFAR-10基准上，FL-MAESTRO精度与最强能量感知基线持平，浪费能耗从超三分之一降至接近零
- 测量不同协调拓扑下大语言模型调用的到达间隔分布，验证泊松指数空模型不成立，拓扑会影响后端流量与系统指标。
- 观测到社交推送带来词汇相似度显著提升、对立观点留存率下降，但分布式信源相比单信源无显著立场改变优势
- 仅通过案例验证发现了传统方法无法得到的候选材料，未给出量化的评测指标与结果。
- 中间分解粒度准确率高于端点粒度，匹配prompt预算下单智能体准确率低6.5个百分点，幻觉注入会颠倒性能排序。

## 控制机制 / Harness 信号

- 构建多智能体框架Patent-MAF实现可本地部署的专利撰写，为该任务提供基准基线辅助模型性能评测。
- 通过经成对监督训练的微型比较器对比原方案与备选方案的优劣，按需给出非绑定建议，引导原智能体重规划改进性能。
- 通过硬件隔离的安全监控器作为运行时保证网关，强制执行形式化安全契约，依托健康向量触发任务重分配管控集群行为
- 采用不对称结构条件化方案控制模型行为，读取阶段使用结构化输入，写作阶段保留散文输入。
- 通过回合级共形校准实现多智能体通信自适应控制，基于讨论状态选动作和发言者，提供性能保证并过滤不合理提案。
- 采用分维度专用大语言模型智能体分工决策，协调器整合输出，新增非大语言模型可行性校验保证决策可行
- 构建多层测量框架，分析不同协调拓扑下的多智能体系统流量特性，明确拓扑对流量模式的影响。
- 通过构建标准化预注册测试床，控制多智能体的交互环境与信源设置，观测群体行为变化规律
- 串联计算材料发现的各异质阶段，采用逐步提高计算成本的筛选策略，控制智能体完成端到端任务。
- 采用控制变量法分离分解粒度的影响，提出在依赖层中点放置分解边界的启发式优化规则。

## 可靠性 / 落地风险

- 专利数据存在较强隐私要求，数据集公开性受限，评测的可复现性存在一定风险。
- 未验证跨任务泛化能力，多次采样对比会带来额外推理延迟，一定程度增加运行时开销。
- 仅完成理论建模验证，缺乏实际工程场景实测，实际落地可靠性待验证
- 性能高度依赖输入知识源，缺失私有知识就会产生内容缺失，输出质量受输入格式影响大
- 推理阶段每轮都需要做校准与动作选择，额外计算开销较大，长对话场景落地成本偏高。
- 部署多个专用大语言模型智能体增加了服务器计算开销，提升了实际部署的资源成本
- 仅验证了现有经典模型不适用，未提出适配的新流量模型，对工业落地支撑不足。
- 结论仅基于合成开源模型智能体群体，推广到真实工业场景存在较大不确定性
- 未提供量化评测结果，结果可靠性待验证，逐步提高计算成本的筛选策略整体运行成本较高。
- 属于特定任务的小规模试点研究，结论泛化性未验证，落地还需进一步拓展研究。

## 代码资源

- [FL-MAESTRO: Multi-Agent LLM Orchestration for Resource-Constrained Federated Lea...](https://github.com/denoslab/FL-MAESTRO.) · 1 stars
- [MemGuard: Persisting Verifier Signals for LLM-Agent Memory Governance](https://github.com/whyyyyy123/MemGuard.) · 1 stars
- [AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design](https://github.com/lmqfly/AgentFold.) · 1 stars
- [Towards Traffic Modelling of Multi-Agent Systems: The Role of Coordination Topol...](https://github.com/dlamagna/agentraffic.)
- [ATHENA: Knowledge-guided agentic neural architecture search for AutoFormer-based...](https://github.com/GatorAIM/ATHENA.)

## 常见基线方法

- **开源大语言模型**：1 篇
- **闭源大语言模型**：1 篇
- **基于专家求解器的干预方法**：1 篇
- **基于任务型评论家的干预方法**：1 篇
- **人类撰写的招标应答**：1 篇
- **全结构化输入条件化**：1 篇
- **固定讨论协议**：1 篇
- **非结构化讨论协议**：1 篇
- **全信息基线**：1 篇
- **能量感知基线**：1 篇

## 常用数据集

- **摘要未提及**：2 篇
- **MATH-500**：2 篇
- **GSM8K**：2 篇
- **LiveCodeBench**：2 篇
- **Dis2Pat**：1 篇
- **WebShop**：1 篇
- **ALFWorld**：1 篇
- **tau^3-Retail**：1 篇
- **SAIL IV 场景**：1 篇
- **企业实际招标应答数据集**：1 篇

---
*自动生成于 2026-08-30 | ArXiv_Daily_Digest*