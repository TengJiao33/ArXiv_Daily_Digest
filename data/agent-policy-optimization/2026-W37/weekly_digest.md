# Agent 策略优化与在线蒸馏 — 2026-W37 (09/07-09/13)

本周新增 **40** 篇论文，**3** 篇附带代码。优先级：high 13 / medium 9 / low 18。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skil...](http://arxiv.org/abs/2609.04865v1) | policy optimization | 联合训练推理与元技能智能体可显著提升性能，在ALFWorld成功率达98.4%(+3.5pp... | 将静态元技能工作流建模为可学习智能体，与推理智能体联合端到端训练，实现技能协同适... | 仅在两个特定基准验证，未在大规模复杂场景测试，多智能体联合训练计... | ✅ |
| 2 | high | - | [Revisiting Complete Reasoning Traces for Post-Training](http://arxiv.org/abs/2609.07103v1) | policy optimization | 推理轨迹中的中间token对最终推理质量贡献极小，完整轨迹仅带来有限收益，仅用端点训练就可获... | 剔除推理轨迹中冗余的中间token，仅利用轨迹端点训练，提升大语言模型后训练的推... | 未在下游任务开展充分量化验证，结论在不同场景下的泛化性有待验证。 | ✅ |
| 3 | high | - | [A Verifier-Guided Explainable Reasoning Framework with Gold-Anch...](http://arxiv.org/abs/2609.05221v1) | policy optimization | RLVR将推理可解释性指标P3从50.68%提升至72.20%，答案准确率基本稳定，符号验证... | 通过符号验证器生成多维度反馈，基于反馈构建奖励执行RLVR优化推理，推理阶段增加... | 仅在小规模438样本测试，未在大规模公开基准验证，方法泛化能力未... | — |
| 4 | high | - | [BRACE: Anchored Bellman-Residual Correction for Stale Critics in...](http://arxiv.org/abs/2609.09783v1) | policy optimization | BRACE在BrowseComp-Plus上mean@1较最强基线提升2.4%，单步速度比同... | 通过提出锚定贝尔曼残差校正处理过期评判器偏差，分离策略校正与奖励传播，提升训练效... | 仅在单个基准上验证效果，方法在多场景下的泛化性尚未得到验证。 | — |
| 5 | high | - | [ConsensusBench: Benchmark of Consensus Nodes for LLM Reasoning v...](http://arxiv.org/abs/2609.04648v1) | reward learning | 基于共识节点的过程奖励可有效缓解长推理轨迹奖励稀疏，在多个推理数据集上性能稳定优于GRPO类... | 基于共识节点构造稠密过程奖励，融入GRPO类强化学习算法，缓解奖励稀疏，引导大模... | 依赖规则提取共识节点与构造奖励，在开放域非规则任务上的泛化性存在... | — |
| 6 | high | - | [Environments as Scaffold: Enriching Feedback to Bootstrap Self-E...](http://arxiv.org/abs/2609.08404v1) | policy optimization | FEE训练可降低熵波动稳定训练，促进状态探索，环境引导会内化入策略权重，组内反馈一致性是稳定... | 通过改造环境侧提供丰富反馈，缓解奖励稀疏问题，稳定强化学习训练动态，优化智能体策... | 依赖环境侧改造适配，不同任务改造成本不一，方法的通用性还需进一步... | — |
| 7 | high | - | [Extremely Sparse Supervision Incentivizes Reasoning Ability](http://arxiv.org/abs/2609.04565v1) | online distillation | 每个推理轨迹仅需1-2个token（占总token的0.05%）的极稀疏监督，效果匹配甚至超... | 在同策略蒸馏设置中引入极稀疏关键token监督替代全token监督，提升大模型推... | 目前仅在推理类任务验证效果，未在通用agent场景验证，通用性有... | — |
| 8 | high | - | [One Step, One Lead: Mitigating Higher-Order Interference in Mult...](http://arxiv.org/abs/2609.06469v1) | policy optimization | 跨步输出回退比同点梯度诊断更关联后续任务损伤，前序checkpoint足迹比Hessian代... | 通过识别跨步输出回退风险，在GRPO更新中加入自适应缩放校正，抑制多域训练的高阶... | 未在公开标准多域任务基准上验证，方法泛化性未充分验证，存在推广不... | — |
| 9 | high | - | [Proof-Carrying Cognition: Closing the Verification Gap with Real...](http://arxiv.org/abs/2609.09776v1) | reward learning | 不可靠验证器随测试计算量增加正确性从0.94降至0.32，现实锚定奖励可将hacking g... | 通过现实锚定校准奖励，引入可靠验证机制校正奖励信号，缓解大模型推理奖励优化过程的... | 需要持续获取现实锚定标签来更新奖励，落地过程中的标签获取成本较高 | — |
| 10 | high | - | [SRPO: Setwise Relative Policy Optimization for Multi-Agent LLMs](http://arxiv.org/abs/2609.08452v1) | policy optimization | SRPO可适配固定、混合、动态路由多种工作流，在不同模型规模下性能最优且优化过程稳定。 | 通过将单次状态转移对应的多个输出整合为统一动作优化，改进多智能体大语言模型的强化... | 仅在两类任务上验证，未覆盖更复杂的真实多智能体场景，泛化能力有待... | — |
| 11 | high | - | [TV-Regulated OPD: Direction Matters in On-Policy Distillation](http://arxiv.org/abs/2609.08341v1) | online distillation | 仅保留token级优势的符号即可达到与标准OPD相当的性能，平滑有界优势可不损性能地稳定训练... | 通过总变分（TV）正则化调整在线策略蒸馏的优势信号，降低监督信号方差，稳定训练过... | 未在具体基准任务与实际场景中验证，缺乏详实评测结果支撑，方法落地... | — |
| 12 | high | ICML 2026 | [UniRRM: Unified Reasoning Reward Models Across Languages and Eva...](http://arxiv.org/abs/2609.05910v1) | reward learning | 采用阶段推理链生成动态适配标准的UniRRM，同尺寸模型性能接近SOTA，对未见评测范式依然... | 通过统一框架构建多语言奖励模型，生成输入适配的细粒度评判标准，提供更稳定可靠的奖... | 未披露具体评测基准细节，未验证该奖励模型在下游实际Agent任务... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **policy optimization**：16 篇
- **reward learning**：6 篇
- **online distillation**：4 篇
- **evaluation/benchmark**：4 篇
- **other**：4 篇
- **未分类**：3 篇
- **survey**：1 篇
- **multi-agent coordination**：1 篇
- **agent harness**：1 篇

## 失败模式与风险信号

- 大模型暖通应用缺乏实地验证，落地就绪度低，暂无法支撑自主控制落地。
- 大语言模型推理产生大量发散分支，部分推理结果荒谬不可靠
- 推理解释不一致、锚定不足、可验证性差
- 技能演化与策略优化解耦，元技能固定，限制技能灵活演化与协同适应
- 大模型生成反馈泛泛而谈、缺乏可操作性，无法识别故事最核心的写作问题
- 原模型存在负向输出行为，跨语言迁移后训练无法提升域外文本简化性能
- 长推理轨迹下最终奖励稀疏，缺乏中间步骤反馈导致推理性能不足
- 现有大模型后训练token密集程度高，训练效率低下、成本过高
- 大语言模型智能体缺乏道德提示时，产生伤害生灵的道德副作用概率极高
- 现有强化学习更新单元与多智能体系统实际执行的联合动作不匹配

## 评测信号

- 调研统计显示仅约6%的研究达到试点级，目前没有研究可满足暖通领域即刻产业应用要求。
- 实验验证了GUT方法量化和降低大语言模型推理不确定性的有效性，在多个模型和数据集上均取得效果。
- RLVR将推理可解释性P3提升21.52个百分点，答案正确率保持稳定，符号验证可额外提升答案准确率。
- 验证不同样本设置下学生模型性能，证明仅用少量选择出的难样本即可达到全量数据集基线的性能。
- 摘要未提及具体评测结果与相关评测信号
- 在ALFWorld和WebShop上成功率分别达98.4%和90.6%，较基线提升3.5和6.2个百分点，同时提升训练效率。
- 在三类故事语料的自动、人工评估中，该方法性能均优于包括Gemini在内的现有SOTA大语言模型。
- 英文ASSET后训练后，模型在两个加泰罗尼亚基准性能提升，抑制负向行为，跨语言迁移未提升域外性能。
- 在基于结构的分子先导优化任务上，该方法性能优于规模大得多的前沿模型，验证了方法的有效性。
- 在多个公开数学推理数据集与自建ConsensusBench上，所提方法的最终答案准确率稳定优于GRPO类基准方法。

## 控制机制 / Harness 信号

- 本文为综述研究，仅分类评估现有大模型在暖通领域的应用方案，未开展模型行为控制改进。
- 通过将推理潜在分支建模为有向无环图得到图复杂度衡量不确定性，以负不确定性作为强化学习奖励优化模型推理行为。
- 通过符号验证器生成多维度反馈，基于反馈构建奖励执行RLVR优化推理，推理阶段增加系统级校正提升可靠性。
- 通过选择难样本开展同策略蒸馏，让学生模型在长推理过程中与教师保持对齐，学习关键推理模式。
- 通过贝叶斯框架统一各类大模型训练推理范式，理清不同方法的等价性与差异，为训练流水线设计提供理论依据。
- 将静态元技能工作流建模为可学习智能体，与推理智能体联合端到端训练，实现技能协同适配演化。
- 通过设计面向反馈建设性的多成分奖励函数，结合GRPO强化学习优化，引导大模型生成合格反馈。
- 通过设计融合SARI指标与惩罚项的奖励函数，结合GRPO策略优化后训练，改进模型输出并抑制负向行为。
- 利用基于课程的合成任务逐步后训练，结合RLVR优化模型的分子生成能力，降低训练成本。
- 基于共识节点构造稠密过程奖励，融入GRPO类强化学习算法，缓解奖励稀疏，引导大模型生成正确推理过程。

## 可靠性 / 落地风险

- 绝大多数研究未经过实地验证，缺乏运营约束测试，方案的时延与安全特性未得到验证。
- 该方法需要对推理分支建图建模，会带来额外计算开销，方法泛化性未得到充分验证。
- 仅在小规模438样本测试，未在大规模公开基准验证，方法泛化能力未得到充分验证。
- 仅在1.5B-7B中小参数模型上验证，未测试更大规模模型，结论推广性存在不确定性。
- 属于纯理论分析工作，未提供实证验证，所得结论的实用性有待进一步检验。
- 仅在两个特定基准验证，未在大规模复杂场景测试，多智能体联合训练计算开销较高。
- 未公开具体使用的数据集细节，方法的可复现性存在一定潜在风险。
- 仅在单个7B大模型上验证，跨语言迁移方案效果不稳定，域外泛化能力不足
- 仅在任务测试中验证方法性能，未经过真实湿实验验证，实际泛化性不确定。
- 依赖规则提取共识节点与构造奖励，在开放域非规则任务上的泛化性存在不确定性。

## 代码资源

- [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hie...](https://github.com/jinyuan-cookie/CoSkill.) · 4 stars
- [Revisiting Complete Reasoning Traces for Post-Training](https://github.com/naver-ai/revisiting-trace.) · 2 stars
- [Where to Look and What to Use: Retrieve-Localize-Generate for Long-Term Conversa...](https://github.com/Nikol-coder/MemLoc.) · 1 stars

## 常见基线方法

- **传统机器学习**：1 篇
- **模型预测控制**：1 篇
- **强化学习**：1 篇
- **基于本体的工具**：1 篇
- **无RLVR与符号验证的微调基线模型**：1 篇
- **17K规模全量数据集基线**：1 篇
- **基于技能的基线方法**：1 篇
- **强化学习基线方法**：1 篇
- **Gemini**：1 篇
- **现有SOTA大语言模型**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **数学推理任务**：2 篇
- **438样本教育问答留出测试集**：1 篇
- **摘要未提及具体数据集名称**：1 篇
- **ALFWorld**：1 篇
- **WebShop**：1 篇
- **三类故事语料数据集**：1 篇
- **ASSET数据集**：1 篇
- **定制化加泰罗尼亚文本简化基准**：1 篇
- **翻译版加泰罗尼亚ASSET**：1 篇

---
*自动生成于 2026-09-13 | ArXiv_Daily_Digest*