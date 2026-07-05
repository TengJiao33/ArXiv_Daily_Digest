# 多 Agent 交互与一致性 — 2026-W27 (06/29-07/05)

本周新增 **92** 篇论文，**7** 篇附带代码。优先级：high 41 / medium 40 / low 11。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Mixture of Debaters: Learn to Debate at Architectural Level in M...](http://arxiv.org/abs/2606.29425v1) | multi-agent coordination | 该方法在多模态基准上准确率优于对比方法，同时实现延迟降低3.7倍，token消耗减少87%。 | 基于混合专家范式构建动态自辩论架构，通过双路由、动量切换等机制优化多智能体辩论的... | 仅在通用多模态基准验证，未在特定下游任务测试，方法泛化能力未得到... | ✅ |
| 2 | high | - | [PEAR: Permutation-Equivariant Adaptive Routing Multi-Agent Debat...](http://arxiv.org/abs/2606.20621) | multi-agent coordination | 基于动态角色分配的排列等变自适应路由，在多个推理基准上相较最强辩论基线平均准确率获得显著提升 | 在推理阶段通过排列等变自适应路由，动态调整多智能体辩论的通信角色与稀疏拓扑，均衡... | 仅在封闭推理基准验证，未测试开放复杂任务，动态路由会增加推理阶段... | ✅ |
| 3 | high | - | [PaperJury: Due-Process Review for Bounded LaTeX Revision](http://arxiv.org/abs/2606.16322) | agent harness | 将安全性和任务完成逻辑放在确定性编排而非模型自主判断，可获得更稳定安全的多轮审查修订效果。 | 通过确定性编排管理分解、路由、停止与补丁应用，约束语义代理仅做受限审查修复，引入... | 仅在学术LaTeX修订场景验证，通用性待验证，依赖专家主观评估，... | ✅ |
| 4 | high | - | [Attractor States Emerge in Multi-Turn LLM Conversations](http://arxiv.org/abs/2606.30571) | multi-agent coordination | 自对弈会形成模型特有吸引子，混合对弈中模型不对称影响对方，Claude Haiku是强吸引子... | 本文未提出特定控制机制，所得的吸引子规律可用于辅助自主智能体系统的预测与监控设计... | 仅覆盖有限数量的模型与话题，结论泛化性待验证，尚未形成落地可用的... | — |
| 5 | high | - | [BOUNDARY_SYNC: Measuring Communication-Induced Representational ...](http://arxiv.org/abs/2607.01600v1) | evaluation/benchmark | 文本通信会使多智能体表征显著同质化（CAF=0.803），耦合方向受群体大小调节，且为提示驱... | 本文提出表征耦合的量化测量方法，验证了表征耦合可在提示层级控制，为多智能体系统设... | 跨不同大模型结果稳定性差，实验需要大量API调用，整体实验成本较... | — |
| 6 | high | ICLR 2026 | [Benefits and Limitations of Communication in Multi-Agent Reasoni...](http://arxiv.org/abs/2510.13903v1) | multi-agent coordination | 任一资源（智能体数量/通信带宽）受约束时，多智能体推理存在固有局限，实证验证了理论预测的参量... | 构建理论框架分析多智能体系统表达能力并推导相关边界，结合实证验证结论，为系统设计... | 仅在合成基准上验证，缺乏真实复杂任务下的验证，结论对实际场景的适... | — |
| 7 | high | - | [Budgeted Act-or-Defer Multi-Agent LLM Deliberation with Local Re...](http://arxiv.org/abs/2606.29654) | multi-agent coordination | 该方法在激活测试集仅用9%~12%预声明错误行动预算，可达到最高84%自动化率与96%已执行... | 通过计算状态条件正确率的下置信界判断输出可靠性，在给定错误预算下决策执行或推迟，... | 可靠性保证为条件性，依赖预设假设，若假设不成立则无法保证错误行动... | — |
| 8 | high | - | [COHORT: Collaborative Orchestration for Hardening via Offensive ...](http://arxiv.org/abs/2606.30479) | multi-agent coordination | 该框架生成的缓解方案中46.7%可同时阻断攻击并保留连通性，成功率是同条件单智能体基线的4.... | 通过角色分解分工生成候选缓解方案，结合攻击性重放、连通性检查筛选合格输出，约束多... | 所有验证均在仿真环境完成，未在真实生产网络验证，实际落地效果存在... | — |
| 9 | high | - | [Calibrating the Evaluator: Does Probability Calibration Mitigate...](http://arxiv.org/abs/2606.31371v1) | evaluation/benchmark | 概率校准可将偏好耦合系数γ降低20-49%，JS散度降低45-67%，该效果并非源于更新不对... | 通过对评估器的成对偏好判断施加概率校准，减少虚假偏好传播，缓解反馈循环中的偏好耦... | 实验样本量仅N=5，样本量较小，所得结论的泛化性有待进一步验证。 | — |
| 10 | high | - | [Can LLMs Be CEOs? Benchmarking Strategic Resource Reallocation w...](http://arxiv.org/abs/2606.17459) | evaluation/benchmark | 所有模型均有较高结构有效性，但战略校准能力差异大，存在三类系统性失效，还存在整合与决断性的权... | 通过构建多角色多智能体模拟评测基准，从四个维度评估大语言模型整合冲突建议的战略决... | 仅在模拟场景测试，和真实组织决策环境差距较大，结论的实际应用外推... | — |
| 11 | high | - | [ClawArena-Team: Benchmarking Subagent Orchestration and Dynamic ...](http://arxiv.org/abs/2606.31174v1) | evaluation/benchmark | LLM子智能体管理的瓶颈是权限授予而非感知，没有模型工作区权限精度超过50%，成本与管理质量... | 通过约束主智能体的感知与工作区访问范围，固定子智能体池，分离出主智能体的管理能力... | 现有LLM子智能体管理权限精度不足，难以满足工业场景多子智能体编... | — |
| 12 | high | ICLR 2026 | [Context Learning for Multi-Agent Discussion](http://arxiv.org/abs/2602.02350v3) | multi-agent coordination | 自适应控制上下文一致性可避免多智能体讨论过早收敛到多数噪声，任务性能较现有方法提升20%-5... | 为每个智能体训练可动态生成上下文指令的生成器，采用自适应机制控制上下文一致性，避... | 未披露具体实现细节与标准基准，可复现性未验证，存在一定的可复现风... | — |

## A 会 / Venue 标签

- **ICLR 2026**：7 篇
- **ICML 2026**：1 篇

## 方法族分布

- **multi-agent coordination**：54 篇
- **evaluation/benchmark**：18 篇
- **agent harness**：9 篇
- **unlearning/safety**：4 篇
- **未分类**：2 篇
- **online distillation**：1 篇
- **other**：1 篇
- **factuality benchmark**：1 篇
- **policy optimization**：1 篇
- **model steering**：1 篇

## 失败模式与风险信号

- 智能体运行时被内存投毒、工具链操纵、多智能体协议攻击劫持，现有防御机制失效。
- 策略内蒸馏性能饱和、强化学习早期训练效率低下
- 固定通信拓扑性能不足，自演化易将随机好运或错误经验纳入学习策略
- 不当人格组合会大幅降低开放协作与议价类多智能体任务的性能
- 延迟验证导致错误断言传播，引发多智能体共识振荡，破坏一致性
- 直接伪标注生成掩码存在几何退化、边界泄漏，未考虑可靠性导致分割性能下降
- 多智能体辩论固定拓扑引发位置偏差，放大不可靠智能体，对角色分配敏感度高
- 利益相关者坍塌、不确定性抑制、多Agent辩论难达成共识
- 现有安全防御漏检意图在prompt、危害在输出分离的对抗不安全交互
- 多智能体文档评估计算开销高，多文档上下文混淆导致性能下降

## 评测信号

- 仅提出自身免疫率（假阳性干预率）这一潜在评估指标，未给出实际实验评测结果。
- 以平均成功率为核心指标，验证得ATOD在不同尺寸学生模型上均稳定优于对比基线，性能超越教师模型。
- 东广岛实例中，生成的196608名合成居民人口统计特征符合普查数据，支撑三类可复现仿真案例。
- 在CF全测试集将RMSE从12.53降至7.87，同时降低通信、模型调用与令牌成本，Silo任务也获得一致提升。
- 评测不同人格组合的多智能体团队在不同任务中的任务完成性能，对比不同场景下的性能差异。
- 在五个开源大语言模型上验证了校正剂量与延迟引发共识振荡的理论预测，证实了接地验证的稳定作用
- 在涂鸦标注、点标注、有限标签三种实验设置下，该方法均达到了当前最优的分割性能。
- 在四个推理基准、六种LLM上，PEAR相较现有最强辩论基线的平均准确率获得了显著提升
- NoT可在所有测试模型上大幅降低两种推理失效比例，扩展为五轮辩论后可实现95%以上的完全共识。
- 相比最强基线平均F1从0.90提升至0.95，攻击成功率降至4.1%， benign敏感请求误报率从0.12降至0.06

## 控制机制 / Harness 信号

- 设计嵌入智能体认知循环的内源性分层免疫架构，通过元认知自监控三元组实现持续免疫学习，动态抵御运行时威胁。
- 通过退火调度结合策略内蒸馏与强化学习，搭配轮级分歧不确定性重加权，改进多轮智能体训练。
- 通过将LLM生成的决策信号离线预编译为查找策略，降低大规模多智能体仿真的计算开销。
- 通过外层大语言模型学习生成时序通信DAG，结合多种约束机制保障自演化过程，优化多智能体通信结构。
- 通过不同人格提示操纵智能体的人格特质，调控智能体的交互沟通风格，探究对团队性能的影响。
- 通过对延迟共识过程建模推导不稳定性阈值，优化校正验证节点放置，抑制振荡维持多智能体共识稳定
- 通过带有辩论裁决机制的视觉语言智能体筛选可靠时间锚点，结合可靠性感知鲁棒学习优化输出。
- 在推理阶段通过排列等变自适应路由，动态调整多智能体辩论的通信角色与稀疏拓扑，均衡各智能体影响力提升可靠性
- 通过设计分五段的结构化推理提示脚手架，扩展为五轮多利益相关方辩论，引导推理并达成共识。
- 在模型响应交付用户前，由专门分析器分别验证prompt意图与响应危害，搭配仲裁法官消解冲突，过滤不安全输出。

## 可靠性 / 落地风险

- 仅提出理论架构，未经过实验验证，防御效果和自身假阳性风险尚未明确。
- 仅在单智能体任务验证效果，未验证多智能体场景下的方法稳定性，可靠性风险未知。
- 离线预编译决策无法适配动态新场景，大规模智能体群体的行为真实性未充分验证。
- 仅在两类特定任务上验证，方法通用性未验证，外层规划额外增加了大模型调用环节。
- 仅在三类小规模任务中验证，结论未在实际工业场景验证，泛化性存在不确定性。
- 仅在开源模型验证，未在真实复杂多智能体任务测试，结论泛化性有待验证
- 仅在医学分割数据集验证，方法在通用多Agent场景下的通用性有待进一步验证。
- 仅在封闭推理基准验证，未测试开放复杂任务，动态路由会增加推理阶段的额外计算开销
- 仅在百个样本的小规模场景验证，未测试大规模复杂场景下的效果稳定性。
- 仅在标准基准测试，未验证大规模真实交互场景下的鲁棒性与推理效率，存在落地风险

## 代码资源

- [PaperJury: Due-Process Review for Bounded LaTeX Revision](https://github.com/u7079256/paperjury.) · 485 stars
- [Cache-to-Cache: Direct Semantic Communication Between Large Language Models](https://github.com/thu-nics/C2C.) · 413 stars
- [ARTEMIS: Agent-guided Reliability-aware Temporal Mask Evolution for Imperfectly ...](https://github.com/wangtong627/ARTEMIS.) · 2 stars
- [PEAR: Permutation-Equivariant Adaptive Routing Multi-Agent Debate](https://github.com/EVIEHub/PEAR.) · 1 stars
- [MMBench-Live: A Continuously Evolving Benchmark for Multimodal Models](https://github.com/PRIS-CV/MMBench-Live.) · 1 stars
- [Mixture of Debaters: Learn to Debate at Architectural Level in Multi-Agent Reaso...](https://github.com/YongLD/MoD.)
- [Safety Testing LLM Agents at Scale: From Risk Discovery to Evidence-Grounded Ver...](https://github.com/Yunhao-Feng/Vera.)

## 常见基线方法

- **单个大语言模型**：2 篇
- **带代码片段的结构化提示基线**：2 篇
- **OPD**：1 篇
- **GRPO**：1 篇
- **固定拓扑方法**：1 篇
- **冷生成拓扑方法**：1 篇
- **SAM2直接伪标注方法**：1 篇
- **现有多智能体辩论基线**：1 篇
- **最强辩论基线方法**：1 篇
- **标准思维链(CoT)**：1 篇

## 常用数据集

- **摘要未提及**：5 篇
- **LiveCodeBench**：3 篇
- **ALFWorld**：1 篇
- **WebShop**：1 篇
- **Search-QA**：1 篇
- **日本东广岛市人口普查数据**：1 篇
- **地理空间数据**：1 篇
- **YJMob100K移动手机数据**：1 篇
- **Count-Frequency聚合任务**：1 篇
- **Silo-Bench风格分布式协调任务**：1 篇

---
*自动生成于 2026-07-05 | ArXiv_Daily_Digest*