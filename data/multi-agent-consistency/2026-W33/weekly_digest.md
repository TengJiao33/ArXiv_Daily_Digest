# 多 Agent 交互与一致性 — 2026-W33 (08/10-08/16)

本周新增 **81** 篇论文，**4** 篇附带代码。优先级：high 37 / medium 37 / low 7。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [M3MAD-Bench: Multi-Dimensional Evaluation of Multi-Agent Debate ...](http://arxiv.org/abs/2601.02854) | evaluation/benchmark | 多智能体辩论并非普遍有效，协作方法比对抗方法更鲁棒，尤其在推理密集型和多模态任务，但效率成本... | 构建标准化统一评测基准，通过多维度指标评估多智能体辩论方法，为该领域提供可靠可复... | 效果更优的协作式多智能体辩论方法效率开销大，工业落地存在较高的成... | ✅ |
| 2 | high | - | [A multi-agent vision-language debate framework for zero-shot cro...](https://www.semanticscholar.org/paper/fdf80bf14084d7f2fd4f6ff638e2932b7e541cda) | multi-agent coordination | 协作多智能体审议可提升个体诊断性能，其中性能较弱的参与智能体获得的提升幅度最大。 | 通过结构化多轮辩论、反趋炎附势机制、性能加权共识投票，引导多智能体开展证据驱动的... | 需要调用多个不同来源的VLM，推理成本较高，大规模落地的资源门槛... | — |
| 3 | high | - | [Agent Behavioral Contracts II: Certifying Compositional Reliabil...](http://arxiv.org/abs/2608.12895v1) | agent harness | 同模型双智能体切换任务中，任一失效时90%为共同失效，正相关会高估多智能体冗余的可靠性 | 提出无需依赖独立性假设的组合可靠性认证方法，纠正原有假设带来的多智能体可靠性高估... | 工业界常用的独立性假设会高估多智能体可靠性，导致实际系统可靠性低... | — |
| 4 | high | - | [Blockchain Empowered Trustworthy Agent Networks: Foundations, Ta...](http://arxiv.org/abs/2608.04626) | survey | 开放智能体网络的网络级信任危机无法由单智能体安全或封闭多智能体协调解决，区块链仅适合做共享信... | 依托区块链作为开放智能体网络的共享信任层，从五个维度满足信任需求，提升多智能体跨... | 区块链作为共享基础设施性能开销较高，缺乏实际落地验证，整体落地成... | — |
| 5 | high | - | [BoardroomAI: Dependency-Aware Human-Steerable Multi-Agent Delibe...](http://arxiv.org/abs/2608.13046) | multi-agent coordination | 依赖感知传播仅检查14.59%的节点就达到穷举影响计算的效果，12例试点中6例生成有效决策，... | 通过依赖感知的演化决策图记录决策要素与依赖，支持人类动态干预，选择性重算相关决策... | 所有结果均为合成数据，仅为原型级别，缺乏真实场景验证，泛化性未得... | — |
| 6 | high | - | [Consensus-Gated Execution: A Multi-Agent LLM Architecture for Au...](https://www.semanticscholar.org/paper/87cf1f451a3c909117ec394b2bc35f684bbf6d6a) | multi-agent coordination | CGX夏普比达1.90，相较趋势跟踪提升3倍，2022熊市中阻挡了93%的高风险交易会话 | 通过多空智能体结构化辩论生成对立观点，元评估器基于共识强度设置执行门控，过滤交易... | 仅在加密货币场景验证，多轮辩论计算成本较高，跨场景泛化性未得到验... | — |
| 7 | high | - | [Cross-platform epistemic verification for improving factual reli...](http://arxiv.org/abs/2608.05302) | consistency detection | 异质证据与多验证模型的共识可有效识别AI生成摘要的事实不确定性，且能保留原语义提升事实一致性... | 引入多LLM陪审团验证机制，基于多源异质证据的共识评分识别错误断言，迭代修正提升... | 依赖多LLM陪审团与多源开放检索，推理成本较高，工业落地存在一定... | — |
| 8 | high | - | [Discovering Efficient and Explainable Communication Topologies f...](http://arxiv.org/abs/2608.12921v1) | multi-agent coordination | 剪枝后的精简关键通信子图可大幅降低通信成本，同时仍能保持与原拓扑相当的任务性能。 | 通过因果推理识别关键通信子图，剪枝冗余通信边，在保持任务性能的同时降低通信成本，... | 未披露具体基线对比细节，仅在公开基准测试，大规模真实场景下的效果... | — |
| 9 | high | - | [Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Pl...](http://arxiv.org/abs/2608.12547v1) | evaluation/benchmark | 两个前沿闭源大语言模型无通信协调可稳定超过纳什基线，多数开源模型仅获部分收益，四代理及以上团... | 本文未对模型或智能体行为进行控制改进，仅构建基准评测大语言模型的无通信多智能体协... | 仅在小规模简单博弈场景测试，大规模多智能体协调性能差，距离实际落... | — |
| 10 | high | - | [ExRole: From Team Trajectories to Executable Roles in Multi-Agen...](http://arxiv.org/abs/2608.11949v1) | multi-agent coordination | 在两个基准上，ExRole相比单智能体搜索EM/F1分别提升15.0/14.4和13.5/1... | 从团队轨迹学习可感知未来的可执行角色原型，引导智能体交互，通过对齐信用分配共享L... | 仅在闭域多跳问答基准验证，未测试开放域复杂多智能体交互场景的泛化... | — |
| 11 | high | - | [ForestBench: A Unified Graph Framework for Evaluating Multi-Agen...](http://arxiv.org/abs/2608.08605v1) | evaluation/benchmark | 基准森林构建完成后，ForestBench可在数毫秒内完成单条轨迹评分，无需额外LLM推理，... | 构建统一的多智能体协作轨迹图表示与参考基准，为不同多智能体协作方法提供统一可复用... | 依赖预构建的参考成功图集合，新任务适配成本未说明，泛化性未得到充... | — |
| 12 | high | - | [GUIDE: Governed Unified Intelligence for Document-to-Artifact Ge...](http://arxiv.org/abs/2608.12133v1) | multi-agent coordination | 该管控多智能体框架达到96%文档成功率，71.4%提取规则可自动批准，将单文档处理时长从2-... | 通过共享版本化规则库、模式验证的智能体间契约和端到端溯源，搭配分工专用智能体管控... | 未与现有主流方法对比，仅在自有企业数据集测试，跨场景泛化能力未得... | — |

## A 会 / Venue 标签

- **KDD 2026**：1 篇

## 方法族分布

- **multi-agent coordination**：40 篇
- **evaluation/benchmark**：20 篇
- **consistency detection**：6 篇
- **agent harness**：3 篇
- **tool-use control**：2 篇
- **survey**：2 篇
- **unlearning/safety**：2 篇
- **policy optimization**：2 篇
- **reward learning**：1 篇
- **other**：1 篇
- **skill generation**：1 篇
- **未分类**：1 篇

## 失败模式与风险信号

- 提示注入、不安全工具调用等智能体安全失效问题
- 单模型单视角难以捕捉细微伪造痕迹，对新兴伪造方法泛化能力不足
- 现有规划方法时域短视、规划开销高、适用场景局限于结构化地图
- 隐藏拜占庭攻击引发多智能体协作性能下降，隐秘动作覆盖破坏团队整体性能
- 现有神经元分割难以兼顾细节与拓扑，分割结果碎片化
- 多约束组合推理能力不足，无法满足组合购物任务的各类合规性要求
- 长周期整仓库迁移中，智能体难以保持迁移目标，无法生成可运行的迁移结果
- 技能执行偏离流程、单步执行错误，相似任务与重复运行表现不稳定、一致性差
- 现有多智能体缺乏子任务参数适配，异质性不足，专项能力有限，造成复杂任务性能瓶颈。
- 检索得到的合理技能包执行无价值，带来不必要的高额计算开销

## 评测信号

- 在Agent-SafetyBench上F1达88.5%，假阳性率1.1%，相对多个基线均有统计显著的性能提升
- 摘要未提及具体量化评测信号，仅说明该方法具备现有方案难以实现的能力
- 由全小型开源MLLM构成的多智能框架，性能超越闭源GPT与Gemini，在自建基准所有指标排名第一。
- 可在1秒内协调数千智能体，支持万级智能体负载，系统吞吐量显著高于所有对比基线方法。
- 仅给出理论推导的算法遗憾上界，未开展实际场景实验，没有实测性能数据
- 在三个公开数据集上性能优于现有最优分割方法，在挑战性ZBFWB数据集上F1得分相比现有最优提升3.02%。
- 摘要未提及实证评测信号，仅给出理论层面的遗憾界与均衡收敛性相关结论。
- 现有各类大语言模型智能体，哪怕是性能较强的模型，在带多约束的组合购物任务上仍表现不佳。
- 在A2H-RepoBench不同规模的代码仓库迁移任务中，ECAT整体迁移质量达到74.7%，性能优于现有所有基于智能体的方法。
- SkillSentry平均提升任务成功率24.1%，同时可有效降低不同配置下智能体重复运行的性能波动。

## 控制机制 / Harness 信号

- 通过密码学承诺锁定允许的工具与约束，引入隔离Judge模型验证，生成零知识证明，验证通过后才允许工具执行
- 以LLM Judge作为验证评估器、LLM Editor作为变异生成器，结合蒙特卡洛树搜索引导生成符合目标的复杂系统
- 通过法官智能仲裁整合四个领域专家的多视角分析结果，解决单视角缺陷，提升检测泛化能力。
- 通过交错规划窗口分批更新智能体路径，集成优先级继承与回溯机制，提升拥挤场景下的规划吞吐量。
- 通过建立适配攻击者信息的鲁棒MDP模型，设计在线鲁棒学习算法，提升多智能体抗拜占庭攻击的可靠性
- 设计三个分工明确的协作智能体，分别完成错误诊断、指令生成、质量验证，通过多轮推理优化分割结果。
- 通过引入正则化惩罚鼓励智能体探索，避免过度承诺次优选择，帮助学习过程收敛到均衡。
- 通过构建标准化多约束组合购物评测基准，结合语义评估与确定性验证，为改进智能体提供反馈。
- 通过判别器计算代码熵生成优化信号，引导生成器迭代更新，仅保留降熵更新，蒸馏得到自进化迁移知识记忆树。
- 通过运行时监控智能体技能执行，结合技能规范与历史轨迹迭代优化运行指导，约束执行流程提升可靠性。

## 可靠性 / 落地风险

- 证明生成额外延迟较高，平均每次约2.26秒，仅在单个基准测试，泛化性待验证
- 未经过公开基准验证有效性，LLM生成的复杂系统存在结果不稳定、难以复现的风险
- 数据集标注由多模型自动合成，未提及人工校验，可能存在标注噪声影响可靠性。
- 仅在两类MAPF场景验证，未在更多复杂真实工业场景测试，泛化能力有待验证。
- 纯理论研究，未经过实际多智能体系统验证，实际场景下的有效性尚未确认
- 仅在公开学术数据集验证，未测试实际临床场景泛化能力，工业落地性未验证
- 属于理论综述工作，未开展实证落地验证，距离实际工业应用有较大差距。
- 现有LLM智能体多约束感知推理能力不足，难以满足真实购物场景的落地要求。
- 仅在安卓转鸿蒙单一场景验证，方法通用性未得到验证，缺乏更多场景下的落地测试。
- 仅在自定义15项技能上测试，未在公开标准基准验证，大规模复杂场景通用性待验证

## 代码资源

- [SodaMem: Evidence-Grounded Temporal Graph Memory for LLM Agents](https://github.com/SodaMem/SodaMem) · 15 stars
- [M3MAD-Bench: Multi-Dimensional Evaluation of Multi-Agent Debate Across Domains a...](https://github.com/liaolea/M3MAD-Bench.) · 5 stars
- [MARC v1: An Open-Source Multi-Agent Framework for Clinical AI Reasoning and Coor...](https://github.com/Penn-RAIL/MARC-v1.) · 2 stars
- [MADE: Belief-Driven Dual-Agent Coordination for Autonomous Model Deployment](https://github.com/HITDiSC/MADE.)

## 常见基线方法

- **单智能体基线方法**：2 篇
- **NeMo Guardrails**：1 篇
- **Llama Prompt Guard 2**：1 篇
- **GPT-OSS-Safeguard**：1 篇
- **常规深度伪造检测器**：1 篇
- **多模态大语言模型**：1 篇
- **闭源GPT模型**：1 篇
- **Gemini模型**：1 篇
- **PIBT**：1 篇
- **EPIBT**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **Agent-SafetyBench**：1 篇
- **FaceVid-Forensics-100K**：1 篇
- **两类真实多智能体路径规划场景**：1 篇
- **BigNeuron**：1 篇
- **CWMBS**：1 篇
- **ZBFWB**：1 篇
- **ComboShoppingBench**：1 篇
- **模拟商业外卖购物环境**：1 篇
- **A2H-RepoBench**：1 篇

---
*自动生成于 2026-08-16 | ArXiv_Daily_Digest*