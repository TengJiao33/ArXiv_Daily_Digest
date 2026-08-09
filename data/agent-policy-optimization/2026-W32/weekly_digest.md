# Agent 策略优化与在线蒸馏 — 2026-W32 (08/03-08/09)

本周新增 **65** 篇论文，**9** 篇附带代码。优先级：high 37 / medium 20 / low 8。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Agentic Reinforcement Learning with Observation-Calibrated Self-...](http://arxiv.org/abs/2608.04788v1) | online distillation | 三种不同规模Qwen3模型上，OCSD在三个基准均稳定优于强基线，校准残差更贴合局部环境反馈 | 通过观测校准自蒸馏获得校准后的稠密token级监督，调制GRPO更新，消除分数偏... | 需要构造两组匹配的回放视图，相比原有方法训练的计算开销有所提升 | ✅ |
| 2 | high | - | [Cooperative Coevolution for Resource-Constrained Agentic LLM Pos...](http://arxiv.org/abs/2608.02391v1) | policy optimization | 相同GPU小时预算下，CoPES恢复全参数GRPO92%的验证准确率增益，标准ES仅67%，... | 通过协同进化将全参数空间分解为低维子空间搜索，实现资源受限下内存高效的Agent... | 仅在4B参数规模的工具Agent上验证，未测试更大规模模型，方法... | ✅ |
| 3 | high | - | [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Sel...](http://arxiv.org/abs/2608.06243v1) | online distillation | DASH无需额外增加师生模型前向计算，在三个数学推理基准所有模型尺度上性能均优于原生OPSD... | 通过散度自适应传播门动态调整token级监督权重，改进同策略自蒸馏对大模型推理能... | 仅在数学推理任务验证效果，方法的通用性尚未在其他任务场景得到验证... | ✅ |
| 4 | high | - | [EnvACE: Internalizing Environment Dynamics via World Rehearsal f...](http://arxiv.org/abs/2608.06197v1) | policy optimization | 跨不同模型规模世界排练均能持续提升策略学习，中等排练预算下测试阶段私有排练无需额外交互即可提... | 通过世界排练让策略内化环境动态，基于任务成功奖励端到端优化，测试阶段用私有排练改... | 依赖大模型自身模拟环境响应，可能存在环境动态模拟偏差，性能受限于... | ✅ |
| 5 | high | - | [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap i...](http://arxiv.org/abs/2608.02508v1) | policy optimization | 采用降阶效用状态可将Cold-Q率降低80.0%，反馈密度提升约6倍，内存大小降低84.4%... | 通过设计降阶固定维度的效用状态表征，集中反馈，避免无关经验获错误更新，解决记忆-... | 未验证在更长交互周期、更复杂大规模任务下的方法稳定性与泛化能力 | ✅ |
| 6 | high | - | [SearchMaster: Grounded and Regulated Self-Play for Search Agents](http://arxiv.org/abs/2608.01822v1) | policy optimization | 接地规整自对弈可将Qwen3.5-9B搜索平均准确率从38.19%提升至51.52%，Bro... | 通过证据链生成器、搜索深度奖励、过度打开惩罚规范任务生成与工具使用，结合GRPO... | 仅在单个骨干模型上验证效果，方法对不同规模大模型的泛化性未得到充... | ✅ |
| 7 | high | - | [Self-Improving Large Language Models via Progressive Experience ...](http://arxiv.org/abs/2608.02139v1) | policy optimization | 在三种不同模型规模下，SPEE在五个数学推理基准上的性能始终优于两类现有自演化基线。 | 通过显式经验演化整合成败轨迹、筛选低效用经验，经特权引导自蒸馏内化，再用奖励强化... | 仅在封闭数学推理任务验证，未测试开放域场景，方法泛化性有待进一步... | ✅ |
| 8 | high | - | [Toward Plasticity-Preserving KL Regularization for Capability Re...](http://arxiv.org/abs/2608.01743v1) | policy optimization | 当参考策略不完善时，全策略KL会存在严格最优正确性间隔，CoKL可避免该缺陷，且更好平衡新旧... | 通过设计正确性条件KL正则化约束策略漂移，在保留基座原有能力的同时，降低对新任务... | 仅在可控测试环境验证效果，未在复杂真实任务场景验证方法的泛化能力... | ✅ |
| 9 | high | - | [Beyond On-Policy Exploration: Integrating External Policy Rollou...](http://arxiv.org/abs/2608.01717v1) | policy optimization | ERILS将数独best-of-4准确率从基线的40.3%提升到98.4%，联合奖励处理会引... | 通过整合外部高奖励策略展开轨迹补充正样本，经长度控制和信源分离奖励处理稳定训练，... | 依赖更强外部策略提供高奖励轨迹，效果受外部策略质量限制，仅在三类... | — |
| 10 | high | - | [Beyond the Mean: Multi-Moment Policy Optimization for LLM Reason...](http://arxiv.org/abs/2608.02149v1) | policy optimization | 联合优化失败概率分布的多个矩相比仅优化单一矩，可稳定提升大语言模型数学推理性能，优于现有强基... | 通过基于矩的优化目标设计，联合最小化失败概率分布的多个矩，优化大语言模型推理策略... | 仅在封闭数学推理基准验证，未测试开放场景泛化性，性能提升的通用性... | — |
| 11 | high | - | [CRISP: Critical Step Perception for Training Efficient Deep Sear...](http://arxiv.org/abs/2608.01867v1) | policy optimization | 区分关键与冗余工具交互而非统一惩罚，可在保持准确率的前提下，分别减少15.1%和33.2%的... | 通过反向归纳标注关键步骤，蒸馏得到识别器，设计效率感知奖励优化策略，剪枝冗余工具... | 关键步骤标签依赖强模型反向归纳，标签质量直接影响最终训练得到的智... | — |
| 12 | high | - | [CausalOPD: First-Wrong-Step Supervision for Distilling Causal Ch...](http://arxiv.org/abs/2608.03673v1) | online distillation | CausalOPD相比序列级在线过程蒸馏平均路径正确率提升23.4个百分点，对错推理率从15... | 通过在线蒸馏结合教师首错定位、局部强化学习修复，配合分阶段课程，提升学生模型推理... | 仅在三个自定义领域验证，未公开具体实现细节，方法通用性与可复现性... | — |

## 方法族分布

- **policy optimization**：37 篇
- **online distillation**：10 篇
- **model steering**：4 篇
- **reward learning**：3 篇
- **evaluation/benchmark**：3 篇
- **other**：2 篇
- **tool-use control**：2 篇
- **unlearning/safety**：1 篇
- **agent harness**：1 篇
- **survey**：1 篇
- **skill distillation**：1 篇

## 失败模式与风险信号

- 多专家整合时可执行动作被破坏，传统蒸馏忽略动作token的核心作用
- 多奖励混合优化时目标相互冲突，对齐税高，导致后训练不稳定且效率低下。
- 传统标量奖励泛化差，生成式奖励缺灵活性，混合方法存在推理与奖励对齐错配
- 闭源API下直接监督微调无法达到人形操纵任务的部署级性能要求
- 现有不可学习文本防护方法无法适配LLM开放生成场景，防护效果受类别特定提示限制
- 奖励驱动RL优化与教师引导防御策略之间存在策略对齐缺陷
- 测试时潜在推理信用分配间接，推理结果鲁棒性不足
- 记忆-奖励陷阱、反馈随状态空间扩张过度分散
- 大模型幻觉导致规划不可靠，规划范围受限
- 资源受限场景下Agent后训练内存开销高、训练耗时过长

## 评测信号

- 核心评测指标为平均成功率，8B参数模型相较最强基线提升2.0%，整合后性能接近多领域教师平均水平。
- PRISM在多个测试任务上性能优于现有多奖励强化学习基线，同时额外具备推理阶段偏好可控性。
- 在偏好建模与策略对齐任务上，LatentRM性能优于现有三类奖励模型，对分布外任务泛化性更好
- 任务成功率，CLIFT两轮迭代后达到接近完美的成功率，性能优于两个对比基线方法。
- 评测核心为未授权微调后LLM的性能下降幅度、合法场景文本的效用保留程度，同时验证迁移性与抗攻击鲁棒性
- 评测不同网络配置下的防御能力，验证模型体量缩减数个量级后防御能力的保持效果，对比各类基线性能。
- 调研验证领域对电力AI实践教学存在迫切需求，活动数据显示该框架获得领域广泛关注。
- 平均准确率达64.5%，较思维链提升6.6个百分点，较最优对比方法提升2.4个百分点，鲁棒性显著提升。
- 在两个基准实现性能提升，Cold-Q率降80.0%，反馈密度提约6倍，内存降84.4%，LLM调用减21.1%
- 在三个攻击场景测试中，相较前沿大语言模型基线，该方案平均恢复时间降15.1%，恢复率提升33.6%。

## 控制机制 / Harness 信号

- 通过结构化动作蒸馏，按动作正确性分配训练信号，抑制无效监督，优化学生智能体的训练过程。
- 将多奖励目标转化为独立正策略加全局负策略的分解优化，推理时通过灵活组合策略实现可控偏好。
- 通过学习离散潜变量形式的潜在推理轨迹优化奖励模型，为大语言模型对齐提供更精准鲁棒的奖励信号
- 将部署获得的奖励反馈转化为闭源API可接受的监督数据，实现无需访问模型内部的闭环策略迭代改进。
- 通过强化学习优化生成策略，生成带扰动的不可学习文本，降低未授权微调后LLM效用，实现数据防护
- 通过在线策略蒸馏，将大语言模型教师的防御策略迁移到轻量RL智能体，提升小智能体决策稳定性与可部署性。
- 本文为电力系统AI教育资源框架，不涉及对模型或智能体行为的控制与改进。
- 通过在Transformer指定层插入可优化潜在状态，利用奖励加权梯度优化内部推理，提升鲁棒性与可解释性。
- 通过设计降阶固定维度的效用状态表征，集中反馈，避免无关经验获错误更新，解决记忆-奖励陷阱
- 采用分层多尺度规划，依托数字孪生开展仿真验证，减少大模型重复调用，缓解幻觉提升可靠性。

## 可靠性 / 落地风险

- 未披露具体评测基准细节，未说明方法带来的额外训练与推理开销。
- 未明确说明方法的计算开销，也未在大规模工业级任务验证，落地成本不明确。
- 未在具体下游agent任务验证效果，未披露训练开销，泛化性需更多真实场景验证
- 完全依赖第三方闭源API，无法自主控制训练过程，自定义修改的复现难度较高
- 基于强化学习训练生成器，计算开销较大，大规模真实场景落地的成本未被讨论
- 仅在学术基准网络环境验证，未在真实企业生产网络测试，真实场景落地有效性待验证。
- 仅面向入门教学场景，未涉及工业级复杂电力AI应用，缺乏落地性能相关验证。
- 未公开所用基准具体细节，未在复杂任务验证泛化性，结论适用范围不明确
- 未验证在更长交互周期、更复杂大规模任务下的方法稳定性与泛化能力
- 依赖数字孪生支撑规划与执行，特定场景下数字孪生构建成本较高，落地门槛较高。

## 代码资源

- [EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinf...](https://github.com/Within-yao/EnvACE.) · 13 stars
- [RoMeRL: Balancing Feedback Coverage and the Memory-Reward Trap in Self-Evolving ...](https://github.com/YOUNG-fnxm/RoMeRL) · 7 stars
- [CoEvoKG: Co-Evolving Knowledge Graphs with Self-Evolving Search Agents](https://github.com/lazzy1225/CoEvoKG.) · 2 stars
- [Toward Plasticity-Preserving KL Regularization for Capability Retention in LLM R...](https://github.com/Lumina04/CoKL.) · 2 stars
- [DASH: Divergence-Adaptive Supervision Horizons for On-Policy Self-Distillation o...](https://github.com/DBtxy/DASH-OPSD) · 2 stars
- [Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training](https://github.com/MetaronWang/CoPES)
- [Self-Improving Large Language Models via Progressive Experience Evolution](https://github.com/rrrsj/SPEE.)
- [SearchMaster: Grounded and Regulated Self-Play for Search Agents](https://github.com/WentaoTan/SearchMaster.)
- [Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation](https://github.com/yiy1x/OCSD.)

## 常见基线方法

- **DAPO**：2 篇
- **权重合并**：1 篇
- **传统同策略蒸馏**：1 篇
- **现有多奖励强化学习基线**：1 篇
- **标量奖励模型**：1 篇
- **生成式奖励模型**：1 篇
- **混合奖励模型**：1 篇
- **直接API监督微调**：1 篇
- **同演示训练的领先开源权重VLA**：1 篇
- **现有不可学习文本防护方法**：1 篇

## 常用数据集

- **ALFWorld**：5 篇
- **推理基准**：3 篇
- **WebShop**：3 篇
- **数学推理任务**：3 篇
- **摘要未提及**：3 篇
- **MATH500**：2 篇
- **数学推理基准**：2 篇
- **多平台GUI环境**：1 篇
- **科学推理任务**：1 篇
- **工具使用推理任务**：1 篇

---
*自动生成于 2026-08-09 | ArXiv_Daily_Digest*