# 🧪 ArXiv AI 日报

📅 **2026-02-19 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **59,269** (¥0.0193)

## 🔥 今日必读

---

### 1. Towards a Science of AI Agent Reliability

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2602.16666v1)

👤 Stephan Rabanser, Sayash Kapoor, Peter Kirgis 等


**中文标题**: 迈向AI智能体可靠性的科学体系

**背景与痛点**: 当前AI智能体逐步落地高影响力实际任务，但现有评估范式仅依赖平均任务成功率这一单指标，掩盖了智能体行为的关键缺陷：无法区分失败的可预测性、对扰动的敏感度、以及失败后果的严重程度，导致基准性能和实际部署可靠性严重脱节，多次发生真实世界高成本故障。

**核心创新**: 该研究借鉴航空、核电等安全关键工程领域的成熟可靠性实践，首次将AI智能体可靠性拆解为一致性、鲁棒性、可预测性、安全性四个正交维度，设计了12个可量化计算、且独立于原始任务准确率的评估指标，实现了可靠性与能力的解耦评估。

**技术细节**: 一致性衡量相同任务多次运行的结果一致性、执行轨迹相似性、资源消耗稳定性；鲁棒性分别衡量对基础设施故障、环境结构变化、语义等价指令重述的性能保持率；可预测性通过校准误差、对错区分度、Brier得分衡量智能体置信度和实际性能的匹配程度；安全性分别统计约束违规频率和违规后果的平均严重程度，单独报告避免平均掩盖尾部风险，所有指标归一化到0-1区间。

**实验结果**: 在GAIA通用智能体基准和τ-bench客服交互基准上评估了三家头部厂商的14款主流模型，发现近18个月模型任务准确率稳定提升，但整体可靠性年增速仅为准确率的七分之一，一致性和可预测性是当前最突出短板，能力提升不会自动转化为可靠性提升。

---

### 2. Policy Compiler for Secure Agentic Systems

🏷️ `cs.CR (加密与安全)` | 📄 [arXiv](http://arxiv.org/abs/2602.16708v1)

👤 Nils Palumbo, Sarthak Choudhary, Jihye Choi 等


**中文标题**: 面向安全智能体系统的策略编译器

**背景与痛点**: 目前大语言模型驱动的智能体广泛部署在需要合规授权的生产场景，现有方案大多将安全策略嵌入prompt，依赖大模型自身遵守规则，既无法避免prompt注入、模型误判导致的违规，也无法通过线性消息历史追踪跨智能体的因果信息流与数据溯源，难以满足复杂组织级策略的执行要求。

**核心创新**: 提出PCAS框架，核心思路是将智能体系统状态建模为记录所有事件因果依赖的有向无环图，用基于Datalog扩展的声明式语言表达策略，能够描述跨智能体的传递性信息流、审批流规则，通过独立于大模型推理的参考监视器实现确定性策略 enforcement，原有智能体无需安全相关重构就能获得构造性合规保证。

**技术细节**: PCAS通过插桩层拦截所有智能体动作（工具调用、API请求、跨智能体消息），可观测服务动态维护事件依赖图，边代表事件间的因果依赖。待执行动作触发授权时，系统提取动作的完整反向依赖切片（所有传递影响该动作的历史事件），策略引擎基于差分Datalog对策略规则做增量求值，参考监视器根据结果放行或拦截，拦截时返回结构化反馈供智能体重试，默认拒绝规则优先，支持自定义谓词与反馈标注。

**实验结果**: 在提示注入防御、τ2-bench客户服务、多智能体药物警戒三个真实场景测试，PCAS将前沿大模型的策略合规率从基线的48%提升至93%，实现零已执行策略违规，提示注入场景攻击成功率降为0，运行延迟与成本开销可控，平均单任务成本增加不超过0.02美元。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [FlowPrefill: Decoupling Preemption from Prefill Scheduling Granularity to Mitiga...](http://arxiv.org/abs/2602.16603v1) `cs.DC` | 大模型并发服务中普遍存在队头阻塞问题，拖累吞吐量与延迟表现，本文解耦抢占与预填充调度粒度，缓解该问题，提升LLM Serving性能，实用性极强。 |
| 5 | [Align Once, Benefit Multilingually: Enforcing Multilingual Consistency for LLM S...](http://arxiv.org/abs/2602.16660v1) `cs.CL (计算语言学)` | 多语言LLM安全对齐传统方案需要逐语言优化，成本极高，本文提出多语言一致性对齐方案，实现一次对齐多语言受益，大幅降低对齐成本。 |
| 6 | [Agent Skill Framework: Perspectives on the Potential of Small Language Models in...](http://arxiv.org/abs/2602.16653v1) `cs.AI (人工智能)` | 当前Agent方案多依赖大尺寸大模型，工业场景需要低成本部署方案，本文探索小语言模型在工业Agent中的潜力，贴合产业落地需求。 |
| 7 | [Causality is Key for Interpretability Claims to Generalise](http://arxiv.org/abs/2602.16698v1) `cs.LG (机器学习)` | 当前LLM可解释性研究普遍存在结论无法泛化的痛点，本文指出因果性是可解释性结论泛化的核心，对领域研究方向有重要指导意义。 |
| 8 | [Scaling Open Discrete Audio Foundation Models with Interleaved Semantic, Acousti...](http://arxiv.org/abs/2602.16687v1) `cs.SD` | 现有音频基础模型多为文本优先架构，限制了通用音频建模能力，本文提出交错多类Token的开放离散音频基座，推动音频大模型技术发展。 |
| 9 | [Error Propagation and Model Collapse in Diffusion Models: A Theoretical Study](http://arxiv.org/abs/2602.16601v1) `stat.ML (统计学习)` | 基于合成数据递归训练扩散模型容易发生模型坍塌，但缺乏系统的理论分析，本文从理论层面研究错误传播和坍塌机制，对领域研究有指导价值。 |
| 10 | [RIDER: 3D RNA Inverse Design with Reinforcement Learning-Guided Diffusion](http://arxiv.org/abs/2602.16548v1) `cs.LG (机器学习)` | 3D RNA逆设计是RNA药物研发和合成生物学的核心问题，本文提出强化学习引导扩散的RIDER方案，提升了逆设计效率，对生物AI应用价值高。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-19
