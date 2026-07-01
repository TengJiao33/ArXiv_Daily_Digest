# 多 Agent 交互与一致性 — 2026-W24 (06/08-06/14)

本周新增 **157** 篇论文，**10** 篇附带代码。优先级：high 79 / medium 64 / low 14。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [CCKS: Consensus-based Communication and Knowledge Sharing](http://arxiv.org/abs/2606.12281v1) | multi-agent coordination | 结合共识约束的动作选择可平衡探索与向教师学习，集成后在两个基准上显著提升合作效率、学习速度与... | 通过对比学习构建共识模型约束智能体动作选择，让智能体合理参考教师建议，平衡探索与... | 仅在游戏类多智能体基准验证效果，未测试实际场景，方法的泛化性尚不... | ✅ |
| 2 | high | - | [Courtroom-Style Multi-Agent Debate with Progressive RAG and Role...](http://arxiv.org/abs/2603.28488) | multi-agent coordination | 渐进RAG带来了7.5个百分点的主要性能提升，结构化审议与模型异质性可有效缓解大语言模型系统... | 通过结构化法庭式多智能体辩论、渐进RAG动态扩充证据、多法官聚合校准输出，提升主... | 该方法采用多轮辩论和渐进检索，流程更长步骤更多，实际落地的推理成... | ✅ |
| 3 | high | - | [SLMJury: Can Small Language Models Judge as Well as Large Ones?](http://arxiv.org/abs/2606.07810) | evaluation/benchmark | RCR辩论协议下多Agent辩论会降低所有测试配置的评判准确率，10-token快速判决在数... | 构建SLMJury评测框架，对小语言模型作为裁判的能力开展多维度测试，验证多Ag... | 小模型裁判领域泛化能力差异大，不存在全能裁判，不同场景适用性差距... | ✅ |
| 4 | high | - | [When Disagreements Elicit Robustness: Investigating Self-Repair ...](http://arxiv.org/abs/2502.15153) | multi-agent coordination | 一般性分歧可提升多智能体任务成功率，任务关键分歧大幅降低单路径推理成功率，对多路径编程影响很... | 引入两类不同的分歧，通过踪迹分析探究多智能体系统在分歧下的自修复行为，挖掘鲁棒性... | 结论仅在有限基准上验证，未在大规模复杂真实任务中检验通用性。 | ✅ |
| 5 | high | - | [(Human) Attention Is (Still) All You Need: Human oversight makes...](http://arxiv.org/abs/2606.12848v1) | agent harness | 模型、智能体分解、提示均相同的情况下，HLER将多智能体基线72%的关键失败率降至16%，两... | 设计人在环架构，将LLM推理与数据工作分离，数据处理采用确定性流程，加入多个人类... | 依赖多步人类监督介入，自动化程度低，大规模应用时人力成本较高，可... | — |
| 6 | high | - | [AI Debaters are More Persuasive when Arguing in Alignment with T...](http://arxiv.org/abs/2510.13912) | evaluation/benchmark | 大模型偏向迎合裁判立场而非自身信念，顺序辩论偏向后发言者，符合先验的立场更有说服力但不合先验... | 预测量大语言模型的先验信念，设置与先验冲突的裁判角色，对比两种辩论协议分析策略与... | 结论仅基于小规模主观问题实验，未验证开放场景通用性，缺乏统一评测... | — |
| 7 | high | - | [ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate...](http://arxiv.org/abs/2606.13197v1) | multi-agent coordination | 真实模型异构加基于一致性的自适应控制，可提升多智能体辩论性能，四个基准准确率分别达65.5%... | 通过预辩论一致路由判断是否启动辩论，收敛后提前停止辩论，聚合时对异常答案降权，实... | 性能依赖模型池的异构性，语义离群检测可能误降正确离群答案的权重，... | — |
| 8 | high | ICLR 2026 | [Adaptive Collaboration with Humans: Metacognitive Policy Optimiz...](http://arxiv.org/abs/2603.07972) | policy optimization | 引入带 defer决策的元认知策略与双环持续学习的人在回路框架，性能稳定优于现有纯自主先进多... | 训练智能体学习元认知决策策略，采用双环优化架构，内环优化 defer决策，外环通... | 依赖人类专家提供高质量反馈，大规模落地时获取持续反馈的成本较高，... | — |
| 9 | high | - | [Agent System Operations: Categorization, Challenges, and Future ...](http://arxiv.org/abs/2606.01581) | survey | 基于大语言模型的智能体系统和传统系统一样会频繁遭遇异常，当前针对智能体系统运维的系统性研究十... | 提出名为AgentOps的智能体系统运维框架，涵盖监测、异常检测、根因定位与异常... | 当前该领域缺乏成熟系统的运维方案，无法有效处理智能体异常，工业落... | — |
| 10 | high | - | [Agentic Systems as Boosting Weak Reasoning Models](http://arxiv.org/abs/2605.14163) | multi-agent coordination | 8个弱模型提案经筛选后达到76.4%的任务求解率，匹配顶级强模型性能，剩余失败多来自弱模型共... | 采用验证器支撑的委员会搜索框架，通过评论家与比较器筛选多个弱推理agent的候选... | 需要生成多个候选提案，算力成本随提案数量k上升，且依赖额外的局部... | — |
| 11 | high | - | [An alignment safety case sketch based on debate](http://arxiv.org/abs/2505.03989) | unlearning/safety | 基于辩论训练可约束AI研发代理的不诚实行为，其安全论证的有效性严格依赖四个可验证的核心主张。 | 借助多Agent辩论训练AI代理使其保持诚实，部署阶段通过在线持续训练维持诚实性... | 安全论证依赖多个未验证的核心假设，缺乏实际评测验证，方案不完备，... | — |
| 12 | high | - | [Arbor: Tree Search as a Cognition Layer for Autonomous Agents](http://arxiv.org/abs/2606.12563v1) | multi-agent coordination | 无harness的单智能体仅实现33%吞吐提升，数小时内崩溃，Arbor最高获193%Par... | 通过共享搜索树形式的认知层工作内存，将失败作为诊断信号，采用编排+批评智能体的制... | 仅在LLM推理优化任务验证，在通用多智能体任务上的通用性尚未得到... | — |

## A 会 / Venue 标签

- **AAAI 2025**：2 篇
- **ICLR 2026**：1 篇

## 方法族分布

- **multi-agent coordination**：80 篇
- **evaluation/benchmark**：33 篇
- **agent harness**：11 篇
- **unlearning/safety**：7 篇
- **policy optimization**：5 篇
- **survey**：5 篇
- **consistency detection**：4 篇
- **other**：3 篇
- **online distillation**：2 篇
- **tool-use control**：2 篇
- **未分类**：2 篇
- **skill generation**：1 篇

## 失败模式与风险信号

- 大型社交网络中高顺从性引发集体准确性下降、虚假信息滋生
- 传统拜占庭容错不适配LLM语义提案，现有方法无法合理判定多智能体协作终态
- 长时域规划失效、任务分解瓶颈、合成幻觉、过程不可审计
- 现有多智能体通信方法为提升性能过度增加通信开销，通信效率低下
- 现有方法无法关联远距离动作的证据，难以检测多良性动作串联的隐藏恶意行为
- 静态规则无法适配事件驱动的动态宏观舆论演化过程
- 输入轨迹碎片化冗余、缺失安全关键行为，构造的技能行为重放一致性低
- 传统大语言模型裁判评分存在偏差、评分结果不稳定
- 端到端多智能体强化学习缺乏协同探索结构，信息摩擦损失更高
- 单遍生成模型的结构不稳定性

## 评测信号

- 以模型匹配真实人类数据的程度、群体集体准确性为核心信号，验证不同顺从度对共识的影响
- H-CSC可100%正确终止超出BFT范围的轮次，错误率低于0.04，相比严格消融提升36%/44%的语义提交覆盖率
- 该方法在两个基准上均取得最优整体得分，分别为58.03%和61.95%，信息召回和分析项排名第一
- 对比基线方法评测任务性能与通信信息熵效率，验证所提方法可在不损失性能的前提下提升通信效率。
- 在SHADE-Arena测试中TRACE总体F1达0.713、召回率达0.844，在需要长程证据关联的任务上性能提升最显著。
- 实验验证ES-MAS在CURE数据集上复现真实美国对华舆论历史趋势的性能显著优于现有多智能体模拟器
- 核心评测技能的行为重放一致性，所提方法相比两类基线将一致性提升了10.5%
- 框架性能显著优于prompt基线，接近有监督系统评分性能，消融实验验证了两个模块分别带来不同增益。
- 对比独立PPO与CA-ETC基线，得到两类方法在三个核心性能指标上的明确差异结果。
- 相比多个基线方法，ULPS实现了超9%的执行准确率提升，需要更少环境交互，最终获得更高的奖励AUC

## 控制机制 / Harness 信号

- 基于深度多智能体强化学习优化智能体交互行为，扩展other-play消除不真实交互约定，支持大规模群体建模
- 提出BFT启发的分层认证协议，基于嵌入生成终态信号，分类输出不同类型的提交或终止结果，保障拜占庭抗性
- 通过核心调度与工具生态解耦实现过程可追溯，结合动态规划、递归执行、评分标准优化规范智能体行为
- 通过在训练损失中加入信息熵效率指标IEI，约束并引导智能体学习兼顾性能与紧凑性的高效通信协议。
- 通过TIJ（分诊-检查-判断）循环跨推理步累积证据，实现长跨度LLM智能体轨迹的恶意行为检测。
- 通过事件与新闻驱动，设计动态分组交互机制，引导多智能体自下而上形成共识，缓解信息茧房，对齐历史时间线演化
- 通过设计RWSA技能分解中间表示，构建W2S自动技能构造框架，提升生成技能的行为重放一致性
- 通过多智能体分工辩论生成不同维度的评分论证，引入检索增强的裁判汇总校准结果，提升评分可靠性。
- 构建带时序扩展反馈的双边匹配部分可观察马尔可夫博弈框架，推出Learn2Match基准用于评测匹配算法性能。
- 将校准大语言模型融入训练循环提供行为引导，基于不确定性设计熵混合机制，自适应平衡大模型先验与学习策略

## 可靠性 / 落地风险

- 仅在少量真实样本和模拟场景验证，缺乏大规模真实场景验证，泛化性待确认
- 仅在小规模基准验证，大规模多智能体场景下的协议性能和效率尚未得到验证
- 框架基于特定平台搭建，未验证通用适配性，复杂深度研究任务运行算力消耗较高
- 未在大规模真实落地场景测试，所提指标的通用性和实际价值未得到充分验证。
- 仅在封闭基准测试验证，未验证开放真实场景下新型恶意行为的检测有效性。
- 研究仅针对美国对华舆论单一特定场景，框架泛化能力未验证，存在泛化不足风险
- 仅在自定义的70个技能上验证，未在公开大规模基准测试，泛化能力未得到验证
- 未在大规模公开数据集验证泛化能力，框架在不同评分场景的可扩展性未得到验证。
- 仅在自建基准上验证，未在真实双边匹配场景测试，研究落地性待验证。
- 仅在单个小型基准上验证效果，尚未验证扩展到目标场景的实际性能与可靠性

## 代码资源

- [When Disagreements Elicit Robustness: Investigating Self-Repair Capabilities und...](https://github.com/wbw625/MultiAgentRobustness.) · 5 stars
- [Beyond Static Evaluation: Co-Evolutionary Mechanisms for LLM-Driven Strategy Evo...](https://github.com/1xiangliu1/FAMOU-CoEvo) · 2 stars
- [Courtroom-Style Multi-Agent Debate with Progressive RAG and Role-Switching for C...](https://github.com/mnc13/PROClaim.) · 2 stars
- [SLMJury: Can Small Language Models Judge as Well as Large Ones?](https://github.com/anishh15/SLMJury) · 1 stars
- [Artificial Intelligence for Mathematical Reasoning: An Integrated Survey of Lang...](https://github.com/Starscream-11813/awesome-AI4Math.)
- [SAGE: An LLM-driven Self Reflective Agentic Framework for Fraud Detection](https://github.com/yichenC1c/SAGE.)
- [CCKS: Consensus-based Communication and Knowledge Sharing](https://github.com/yuanxpy/CCKS.)
- [MODF-SIR: A Multi-agent Omni-modal Distilled Framework for Social Intelligence R...](https://github.com/eeee-sys/MODF-SIR)
- [PRISM: Prosody-Integrated Multi-Agent Reasoning Framework for Empathetic Spoken ...](https://github.com/Bxzfrm/PRISM.)
- [Zero-source LLM Hallucination Detection with Human-like Criteria Probing](https://github.com/TRISKEL10N/HCPD.)

## 常见基线方法

- **自一致性**：2 篇
- **多智能体辩论**：2 篇
- **仅输出判决的强证书基线**：1 篇
- **严格语义消融基线**：1 篇
- **多种现有MARL通信方法**：1 篇
- **现有SOTA轨迹监控方法**：1 篇
- **现有LLM基多智能体模拟器**：1 篇
- **基于摘要的基线方法**：1 篇
- **基于提示的基线方法**：1 篇
- **标准LLM裁判方法**：1 篇

## 常用数据集

- **摘要未提及**：6 篇
- **HumanEval**：5 篇
- **MMLU-Pro**：4 篇
- **GSM8K**：3 篇
- **SWE-bench Verified**：3 篇
- **数学推理任务**：3 篇
- **MMLU**：2 篇
- **TruthfulQA**：2 篇
- **GAIA**：2 篇
- **Bluesky社交网络**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*