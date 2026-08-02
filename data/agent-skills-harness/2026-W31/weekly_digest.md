# Agent Skills 与 Harness — 2026-W31 (07/27-08/02)

本周新增 **183** 篇论文，**13** 篇附带代码。优先级：high 149 / medium 27 / low 7。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Colla...](http://arxiv.org/abs/2607.28430) | agent harness | 四智能体方案任务解决率达62.1%，较单智能体提升29.8个百分点，性能增益随任务难度提升而... | 通过为智能体harness新增异步消息传递层，提供三个通信原语，支持智能体不中断... | 需要多个LLM智能体同时运行，调用量增加会提升落地成本，未验证非... | ✅ |
| 2 | high | - | [An Empirical Study of Coordination Mode as the First-Class Citiz...](http://arxiv.org/abs/2607.27877) | evaluation/benchmark | 相同任务与模型下，改变协调拓扑可让评分变动超30分、耗时翻倍，拓扑对性能的影响堪比模型能力。 | 通过构建标准化评测基准，设计确定性评分规则，量化不同协调模式下多智能体编码的实际... | 测试仅覆盖10个真实项目，样本量有限，结论在更大规模场景下的泛化... | ✅ |
| 3 | high | - | [ClawRec: A Claw-Native Recommender System](http://arxiv.org/abs/2607.23779) | evaluation/benchmark | ClawRec在ClawRec-SimBench上NDCG@20达0.6134（提升0.11... | 通过维护带关联证据的时序结构化跨平台用户状态，基于边际效用筛选候选，生成贴合用户... | 依赖用户授权的跨平台上下文数据，实际落地存在数据获取门槛与隐私合... | ✅ |
| 4 | high | - | [ContractHIL-HLS: Contract-Aligned Multi-Agent Workflow with Hard...](http://arxiv.org/abs/2607.25283v1) | agent harness | 引入结构化契约将单样本测试通过率从64.0%提升至70.2%，板级设计将平均时延从207.3... | 通过结构化契约定义显式约束、验证规则与回滚机制，结合硬件在环测量反馈修正智能体设... | 仅在HLS设计场景验证，板级测试案例少，通用性有待更多硬件场景验... | ✅ |
| 5 | high | - | [DataClawEval: A Benchmark for Data Engineering Agents in Real In...](http://arxiv.org/abs/2607.28033v1) | evaluation/benchmark | 评测16个前沿智能体显示，最强模型整体得分仅74.9，无模型全面领先，各模型仅擅长特定执行引... | 构建标准化工业数据工程场景评测框架，通过隔离沙箱和确定性规则实现对智能体能力的客... | 当前前沿智能体在端到端工业数据工程任务上性能不足，距离实际工业落... | ✅ |
| 6 | high | - | [FinanceHarness: Autonomous Financial Deep Research Framework](http://arxiv.org/abs/2607.27853v1) | agent harness | 现有主流大模型和智能体在FinanceGym上得分低于40%，同开源主干下FinanceHa... | 通过分层harness驱动研究智能体，遵循从业者引导工作流调用金融工具，结合奖励... | 仅适配金融深度研究场景，未验证跨领域通用性，任务整体难度较高落地... | ✅ |
| 7 | high | - | [Focus Is All You Need: Adaptive Goal-aware Attention Orchestrati...](http://arxiv.org/abs/2607.23678v1) | multi-agent coordination | 结合目标、拓扑与资源感知的动态注意力分配，可在提升任务效果的同时降低冗余计算、延迟与toke... | 通过注意力编排机制，动态根据目标、拓扑与计算约束调整智能体优先级与资源分配，聚焦... | 未在公开标准基准上验证，方法通用性和工业场景下的稳定性未得到充分... | ✅ |
| 8 | high | - | [LabEvolver: Training-Free Experience Evolution for Safe and Grou...](http://arxiv.org/abs/2607.27690v1) | skill generation | 无训练经验演化可同时提效增安全，pH调节完成时间降48.2%，ALFWorld成功率从76.... | 通过双循环结构管控智能体行为，内循环做在线感知规划与安全验证，外循环从轨迹蒸馏可... | 仅在两个场景验证，更大范围通用场景下的落地有效性尚未得到充分验证 | ✅ |
| 9 | high | - | [SecRespond: Benchmarking AI Agents for Real-World Post-Compromis...](http://arxiv.org/abs/2607.26791v1) | evaluation/benchmark | 当前LLM智能体能可靠发现告警暴露的问题，但难以主动排查静默入侵、生成合格修复方案，无模型能... | 构建公开可复现的评测基准，用于发现LLM智能体在入侵响应任务上的能力缺陷。 | 当前LLM智能体能力不足，无法满足真实入侵响应的工业落地需求。 | ✅ |
| 10 | high | - | [WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surfa...](http://arxiv.org/abs/2607.25765v1) | evaluation/benchmark | 金约束工具访问下智能体路由F1达98.7-99.8%，但答案准确率仅56.1-75.3%，正... | 构建标准化智能体评测harness，通过控制工具访问、添加表层提示，探究其对智能... | 仅提供了评测基准与框架，未给出解决选对知识源后回答不佳问题的落地... | ✅ |
| 11 | high | - | [(Im)Paired Programming: Coding Agents Improve Productivity but H...](http://arxiv.org/abs/2607.26375v1) | evaluation/benchmark | 编码智能体助力初始任务完成但会损害用户代码理解，低努力交互对应理解更差，用户明知理解差仍偏好... | 本文未提出具体的agent行为控制机制，仅指明未来需引导开发者主动参与，减少低努... | 长期大规模使用会降低开发者对代码的掌控能力，不利于代码长期维护与... | — |
| 12 | high | - | [A Control System, a Dataset, and a Recipe for Making Frozen LLM ...](http://arxiv.org/abs/2607.25415v1) | agent harness | 限定harness为固定小规模可阅读动作空间后，样本高效强化学习可在黑盒模型上实现可审计的有... | 将harness限定为固定小规模人类可读动作空间，通过多目标奖励引导的强化学习优... | 固定的harness动作空间灵活性不足，可能难以适配复杂程度更高... | — |

## 方法族分布

- **evaluation/benchmark**：65 篇
- **agent harness**：65 篇
- **skill generation**：11 篇
- **tool-use control**：10 篇
- **multi-agent coordination**：8 篇
- **unlearning/safety**：6 篇
- **online distillation**：5 篇
- **survey**：3 篇
- **policy optimization**：3 篇
- **other**：2 篇
- **factuality benchmark**：2 篇
- **agent harness, evaluation/benchmark**：1 篇

## 失败模式与风险信号

- 误导性奖励污染训练循环
- 添加流程化技能引发的LLM智能体性能退化（回归问题）
- 逐调用路由反馈归因错误，不匹配长周期智能体任务的评价逻辑
- 静态授权过度授权，工具权限滥用，LLM代理失配误用
- 智能体自主开发会引入功能规范未要求的额外实现决策，产生未测试的决策点
- 开放式环境真值缺失，智能体随运行时间累积产生运行漂移，可靠性下降
- 现有VLM智能体无法在跨任务3D场景动作中保持持续稳定的良好表现
- 现有方案存在幻觉、准确率不足，企业大场景下计算成本过高
- 冻结权重Agent部署后无法积累经验，重复任务性能无法提升
- 长范围训练不稳定、推理精度效率失衡、智能体任务失败率高

## 评测信号

- 该框架可持续提升合格骨干大模型的性能上限，还能显著扭转初始不对齐模型的性能表现。
- 关注添加技能带来的性能回归副作用，区分两类失败，更准确衡量技能对智能体的实际影响。
- 在多个智能体基准上获得非支配的精度-延迟帕累托前沿，两个测试基准均取得显著的精度提升与延迟降低。
- 合成数据生成结合策略迭代可降低93%的权限越限，构建的数据集标注一致性高，Cohen's κ最高可达0.967
- 对比不同协作模式开发的代码功能正确性、测试套件质量，分析各模式的适用场景。
- 相比各基线方法，该框架在预测准确率和速度上均获得大幅提升，自研ARIMA算法提速同时精度保持不变。
- 评测十一种不同配置的闭源VLM智能体，总体得分范围为38.6-50.2，不存在能在所有任务稳定表现优异的模型
- 摘要未给出本文方案的具体评测结果，仅指出现有方案存在幻觉多、准确率低、成本高的问题。
- 对比不同基线的单试任务成功率，验证不同反馈类型的效果，同时测试累积记忆的跨模型迁移效果
- 3B紧致模型在智能体基准上性能优于更大参数量的两个基线模型，在推理与对齐任务上也保持竞争力。

## 控制机制 / Harness 信号

- 通过动态技能控制器收集执行反馈更新扩展技能库，在强化学习自博弈循环中协调组件，避免误导奖励污染训练。
- 通过分解技能净效应的评估框架，指出技能设计需强化接地与验证，减少性能退化以提升可靠性。
- 通过任务级路由框架，基于任务终端奖励更新路由策略，对齐监督单元，平衡大模型调用的精度与部署延迟。
- 基于动态最小权限原则设计三源权限分层防御架构，同时支持强制管控和仅行为观测两种部署模式。
- 通过划分不同交互协作模式，基于测试驱动开发流程结合结构化提示约束开发行为。
- 通过引入结合ARIMA预测器的自校准机制，动态逼近真值缓解运行漂移，无需持续人工监督保障可靠性。
- 通过构建统一循环的标准化评测基准，为3D场景智能体的动作性能提供评估反馈，支撑后续优化。
- 通过基于检索知识的证据化推理，结合多智能体自适应规划，提升集成可信度，降低企业场景计算成本。
- 为原冻结权重智能体添加外部记忆模块，将部署反馈蒸馏为可检索自然语言规则，增量更新能力不修改原模型
- 通过混合RLHF、长度控制推理强化学习、带奖惩的智能体RL优化行为，减少失败，平衡推理精度与效率。

## 可靠性 / 落地风险

- 仅在通用基准完成评测，未在真实工业场景验证，开放技能进化存在一定不可控风险。
- 现有技能设计过度侧重流程指导，忽略接地与验证，易引入大量不可预见的性能回退。
- 该方法仅在公开基准验证，未提及大规模工业场景测试，实际落地泛化性待验证。
- 仅在合成数据集上验证效果，缺乏真实企业场景的落地测试，实际可靠性待验证
- 属于预探索性研究，样本量有限，结论的普适性有待进一步验证。
- 仅在单一特定边缘资源场景验证，方法的通用性和泛化能力未经过多场景测试。
- 评测全部基于闭源私有VLM，未公开配置细节，结果的可复现性存在一定风险
- 本文为综述性研究，未提供具体落地实现与实测验证，落地有效性有待验证。
- 错误反馈可能存入外部记忆持续累积影响性能，摘要未提及错误处理与回滚机制
- 未在真实复杂落地场景验证泛化能力，小参数量处理超长任务能力可能受限。

## 代码资源

- [SecRespond: Benchmarking AI Agents for Real-World Post-Compromise Incident Respo...](https://github.com/Alibaba-NLP/qqr) · 269 stars
- [WorldCupArena: Fine-Grained Evaluation of Language Models and Deep-Research Agen...](https://github.com/wzk1015/WorldCupArena.) · 20 stars
- [EvoGUI: An Evolution-Aware Benchmark for GUI State-Transition Understanding](https://github.com/Yyhhh6/EvoGUI.) · 4 stars
- [DataClawEval: A Benchmark for Data Engineering Agents in Real Industrial Harness](https://github.com/Dicemy/DataClawEval) · 3 stars
- [WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge Rou...](https://github.com/haolpku/WorkSurface-Bench.) · 2 stars
- [FinanceHarness: Autonomous Financial Deep Research Framework](https://github.com/Yijia-Xiao/FinanceHarness.) · 2 stars
- [LabEvolver: Training-Free Experience Evolution for Safe and Grounded Wet-Lab Age...](https://github.com/AndyGao6186/LabEvolver.) · 1 stars
- [AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration](https://github.com/Coral-Protocol/AgentRadio.) · 1 stars
- [Would You Walk to the Car Wash? Revealing the Salience Bias of Large Language Mo...](https://github.com/Wuzheng02/SaliTrap.) · 1 stars
- [Focus Is All You Need: Adaptive Goal-aware Attention Orchestration for Multi-Age...](https://github.com/MingzhouFan97/AGAO.)

## 常见基线方法

- **GRPO**：2 篇
- **ReAct**：2 篇
- **未提及具体基线名称**：2 篇
- **GPT-5.6 Sol**：2 篇
- **人类基线**：2 篇
- **现有自蒸馏基线**：2 篇
- **现有SOTA方法**：2 篇
- **无技能的LLM智能体**：1 篇
- **现有逐调用路由器**：1 篇
- **单个模型基线**：1 篇

## 常用数据集

- **摘要未提及**：5 篇
- **ALFWorld**：5 篇
- **WebShop**：4 篇
- **工具使用基准**：2 篇
- **WebArena**：2 篇
- **HotpotQA**：2 篇
- **HumanEval**：2 篇
- **MTDTool**：2 篇
- **SWE-bench Verified**：2 篇
- **ProgramBench**：2 篇

---
*自动生成于 2026-08-02 | ArXiv_Daily_Digest*