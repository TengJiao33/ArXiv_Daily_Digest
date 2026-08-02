# 多 Agent 交互与一致性 — 2026-W31 (07/27-08/02)

本周新增 **72** 篇论文，**3** 篇附带代码。优先级：high 38 / medium 22 / low 12。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Colla...](http://arxiv.org/abs/2607.28430v1) | multi-agent coordination | 四个经AgentRadio组织的智能体在SWE-Atlas QnA上达到62.1%任务解决率... | 通过新增异步消息传递harness层，让智能体保持对同伴的被动感知，实现执行过程... | 多智能体异步运行带来更高的计算资源成本，未验证更大规模协作下的稳... | ✅ |
| 2 | high | - | [Focus Is All You Need: Adaptive Goal-aware Attention Orchestrati...](http://arxiv.org/abs/2607.23678v1) | multi-agent coordination | 结合三类注意力的自适应编排AGAO，相比现有图执行策略，可提升任务效果，同时减少冗余计算、延... | 结合目标、拓扑、资源三类感知注意力做编排，动态调整智能体计算优先级与资源，聚焦目... | 仅在通用多智能体工作负载验证，未在大规模真实工业场景测试，方法泛... | ✅ |
| 3 | high | - | [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable ...](http://arxiv.org/abs/2607.23802v1) | reward learning | SpyRL在非可验证开放式任务上性能优于现有自提升方法，在可验证推理任务上也能获得一致性能增... | 通过任务变换构建多智能体自对弈环境，生成自可验证的奖励信号，引导大模型完成开放式... | 该方法依赖定制化任务变换构造代理环境，新场景适配性不确定，通用性... | ✅ |
| 4 | high | - | [$Σ$-Mem: An Online Reliability Memory for LLM-based Multi-Agent ...](http://arxiv.org/abs/2607.27958v1) | multi-agent coordination | 随着正确性反馈增加性能持续提升，分布外评测集上结果优于多数投票与最优固定peer。 | 通过在线维护记录智能体个体与关系的可靠性证据的记忆，引导多智能体协调，提升输出可... | 仅在Qwen家族模型验证，未在更多复杂任务验证，方法的通用性有待... | — |
| 5 | high | - | [A Comparative Study of MCP and A2A for Inter-Agent Coordination ...](http://arxiv.org/abs/2607.23884v1) | multi-agent coordination | MCP实现轻量、协调复杂度低，但状态和任务生命周期需应用层实现；A2A原生支持状态协调，但实... | 通过对比不同协调协议的设计，梳理协调责任的分布规律，为多智能体协调工程设计提供参... | 结论仅适用于本次评估的特定协调模式，推广性有限，不同场景结论可能... | — |
| 6 | high | - | [ARCHER: Agentic Rule and Compliance Harness for Executable Regul...](http://arxiv.org/abs/2607.25566v1) | agent harness | ARCHER确定性多智能体编排比基线平均联合准确率提升82%，自托管开源模型可达前沿API ... | 采用确定性编排的多智能体harness架构，生成可审计验证代码，兼顾验证准确率与... | 仅在建筑合规场景完成验证，方法在其他合规领域的通用性有待进一步验... | — |
| 7 | high | - | [An Empirical Study of Coordination Mode as the First-Class Citiz...](http://arxiv.org/abs/2607.27877v1) | evaluation/benchmark | 相同任务与模型下，改变协作拓扑可使评分变动超30分、时钟时间翻倍，结构化流水线性能最优，过多... | 构建标准化评测基准，测试多智能体不同协作拓扑结构，通过自动评分器度量多维度性能，... | 仅在10个全栈编码项目上验证结论，普适性有待更多不同任务场景的进... | — |
| 8 | high | - | [Are Diversity Metrics Measuring Diversity? A Capability-Controll...](http://arxiv.org/abs/2607.20768) | evaluation/benchmark | 所有子集都存在隐式互补性，但仅9.98%的规模3标准子集简单投票优于最强单模型，多数多样性指... | 通过显式控制大语言模型的平均能力，实证审计现有多样性指标对集成多数投票增益的预测... | 结论的效应大小依赖集成配置，多指标联合回归构造秩亏，结论的普遍适... | — |
| 9 | high | - | [Auditing Emergent LLM-Agent Collaboration through Cooperation-Ob...](http://arxiv.org/abs/2607.27429v1) | agent harness | iCORE-Audit相比被动全状态观测，真实LLM执行中终端性能绝对提升31.0%，可准确... | 基于iCORE统一编码，通过验证工作健全性与智能体分配稳定性，实现多智能体协作的... | 未在公开标准基准验证，方法在复杂实际任务中的普适性与效果待进一步... | — |
| 10 | high | - | [Before Agents Speak: Pre-hoc Failure Risk Inference in Multi-Age...](http://arxiv.org/abs/2607.26836) | agent harness | HalluProp在多智能体故障定位中平均AUROC达84.6%，诊断速度比事后方法快65倍... | 通过事前风险推断完成上游筛查定位故障智能体，支持早期干预，补充现有事后方法，提升... | 未在大规模实际多智能体任务中验证泛化能力，实际落地的适配性有待进... | — |
| 11 | high | - | [Belief Coevolution in a Social Network of Generalist and Special...](http://arxiv.org/abs/2607.27512v1) | multi-agent coordination | 引入微调后的专精大模型可使群体共识偏移翻倍，仅靠角色提示无法实现真实的多智能体信念扩散仿真。 | 本文构建CoevolveSim仿真框架，控制三类不同变量开展实验，研究多智能体信... | 研究结论全部来自仿真模拟，未在真实多智能体业务应用场景中完成验证... | — |
| 12 | high | - | [Cardiologent: Multi-Agent Clinical Decision Support for Patient-...](http://arxiv.org/abs/2607.25340v1) | multi-agent coordination | Cardiologent在所有患者级任务维度得分最高，大模型裁判与心脏病专家的ICC达0.7... | 引入审查智能体，对每一项推理结论对照所引用的临床指南验证，保障输出决策合规、可审... | 未披露具体数据集细节，未经过真实临床大规模验证，落地泛化性有待验... | — |

## 方法族分布

- **multi-agent coordination**：34 篇
- **evaluation/benchmark**：14 篇
- **agent harness**：7 篇
- **tool-use control**：3 篇
- **survey**：3 篇
- **policy optimization**：2 篇
- **other**：2 篇
- **知识蒸馏**：1 篇
- **factuality benchmark**：1 篇
- **reward learning**：1 篇
- **consistency detection**：1 篇
- **online distillation**：1 篇

## 失败模式与风险信号

- 中心化奖励强加单一外部正确知识定义，限制去中心化的能力涌现。
- 大语言模型智能体的挑衅升级、谄媚漂移、卡顿重复等反应式倾向失败
- 传统蒸馏无法传递核心推理能力，学生模型易发生风格漂移与冗余退化
- 检索记忆冗余、冲突、相关性弱，长期记忆任务上下文开销大，回答多次运行不稳定
- 静态排行榜忽略计算成本，导致排名反转，无法选出适合部署的优质模型
- 原有RLVR适用范围受限，开放式任务奖励获取存在评估偏差与额外成本。
- 现有图基多智能体执行均匀分配资源，在无关低影响任务上造成不必要计算资源浪费
- 语言模型生成科学领域主张错误，存在一致性问题
- 现有大语言模型智能体发展跨领域跨任务碎片化，性能提升局限于特定类别。
- 多客户端规模下多智能体隐私博弈均衡难以求解，现有方法无法支持个性化隐私保障

## 评测信号

- 验证SME轮换的鲁棒性、拓扑与尺度不变性，分析不同信念维度下的系统动力学，明确专家集中现象的驱动因素。
- 16组实验中13组p<0.05下调节后智能体更平静，效果跨不同谱系的独立模型族稳定可复现。
- 通过案例验证该架构可有效降低能耗与通信开销，产出满足研究者需求的结构化监测知识
- MAPD在七个QA基准上优于对比方法，Qwen3-1.7B平均成功率39.4%，Qwen3-4B平均成功率达到44.4%
- 在两个基准上，对闭源与开源冻结回答模型均达到SOTA，同时显著压缩输入记忆上下文的规模。
- 原始事实性得分相近的模型，计入计算成本后排名会反转，多智能体竞争可获得稳定小幅的资源效率提升。
- 从八项工业界提出的工程需求维度，对比两种协调协议的实现复杂度与功能支持能力差异。
- 该方法在非可验证开放式任务上优于现有自提升方法，在可验证推理任务上也能取得稳定的性能提升。
- 相较于现有基于图的多智能体执行策略，AGAO提升任务效果的同时，减少了不必要的计算、端到端延迟与token消耗。
- 验证器门控重试相比单次尝试修复成功率提升7.1-8.3个百分点，最优策略排序随模型不同反转

## 控制机制 / Harness 信号

- 通过同伴一致性验证推断能力、动态分配专家身份、加权社会共识更新，实现去中心化多智能体共识学习。
- 设计确定性元控制层，仅基于数值状态遥测调节底层智能体行为，构造层面不存在提示注入通道。
- 采用分层主从设计控制硬件激活时机，依托多智能体框架协调各类任务，管控系统整体能耗
- 通过多智能体生成结构化归一化搜索轨迹协议作为蒸馏监督，结合稀疏强化学习优化学生模型，缓解风格漂移
- 通过两阶段训练优化记忆组织策略，生成结构化有序记忆轨迹，压缩上下文同时提升回答稳定性。
- 通过设计资源感知的多智能体对抗评测协议，归一化计算成本，引入Q-Score引导更资源高效的模型策略。
- 通过对比不同协调协议的设计，梳理协调责任的分布规律，为多智能体协调工程设计提供参考。
- 通过任务变换构建多智能体自对弈环境，生成自可验证的奖励信号，引导大模型完成开放式任务自提升。
- 结合目标、拓扑、资源三类感知注意力做编排，动态调整智能体计算优先级与资源，聚焦目标关键推理路径。
- 通过符号验证器检验对偶主张的一致性，以验证结果作为门控信号引导语言模型修正错误主张

## 可靠性 / 落地风险

- 全部实验均为仿真模拟，未在真实业务场景验证，实际落地效果缺乏有效验证。
- 控制器未经过对抗测试，部分近饱和宿主模型上的调节效果不显著。
- 仅通过案例验证，无标准化基准与量化对比，大规模落地的性能缺乏足够验证
- 仅在QA任务验证，未明确跨任务泛化边界，通用可靠性未得到充分验证
- 需要额外训练记忆策略，增加了整体模型的训练复杂度与部署开销。
- 成本权重会影响评测排名，不同场景成本偏好不同，结果的通用性有待验证。
- 结论仅适用于本次评估的特定协调模式，推广性有限，不同场景结论可能存在偏差。
- 该方法依赖定制化任务变换构造代理环境，新场景适配性不确定，通用性有待验证。
- 仅在通用多智能体工作负载验证，未在大规模真实工业场景测试，方法泛化性有待验证。
- 最优验证策略依赖特定模型，结论跨模型通用性不足，可迁移性较差

## 代码资源

- [From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for Open...](https://github.com/wangqinsi1/SpyRL.) · 2 stars
- [Focus Is All You Need: Adaptive Goal-aware Attention Orchestration for Multi-Age...](https://github.com/MingzhouFan97/AGAO.)
- [AgentRadio: Passive Awareness for Long-Horizon Multi-Agent Collaboration](https://github.com/Coral-Protocol/AgentRadio.)

## 常见基线方法

- **单智能体基线**：2 篇
- **主流知识蒸馏方法**：1 篇
- **基于结果的强化学习方法**：1 篇
- **暴力Best-of-4智能体**：1 篇
- **模型上下文协议（MCP）**：1 篇
- **Agent2Agent（A2A）**：1 篇
- **现有自提升方法**：1 篇
- **现有基于图的多智能体执行策略**：1 篇
- **单次尝试修复**：1 篇
- **停止优先策略组合**：1 篇

## 常用数据集

- **摘要未提及**：4 篇
- **多智能体仿真实验环境**：1 篇
- **水下视觉与声学监测案例**：1 篇
- **七个QA问答基准**：1 篇
- **LoCoMo**：1 篇
- **LongMemEval-S**：1 篇
- **摘要任务**：1 篇
- **开放域问答任务**：1 篇
- **软件工程协调任务场景**：1 篇
- **SpyRL多智能体自对弈环境**：1 篇

---
*自动生成于 2026-08-02 | ArXiv_Daily_Digest*