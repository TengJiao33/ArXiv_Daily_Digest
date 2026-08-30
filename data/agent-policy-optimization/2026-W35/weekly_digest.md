# Agent 策略优化与在线蒸馏 — 2026-W35 (08/24-08/30)

本周新增 **64** 篇论文，**8** 篇附带代码。优先级：high 33 / medium 22 / low 9。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [EDGE: Experience-Distillation for Guided Exploration in Agentic ...](http://arxiv.org/abs/2608.21946v1) | online distillation | 7B规模模型上，EDGE相比GRPO在两个基准成功率分别提8.3、12.5个点，移除外部经验... | 将检索经验作为临时训练支架，通过经验蒸馏把探索收益内化到参数策略，配合共进化经验... | 仅在两个基准完成评测，未验证在更大规模模型与复杂任务上的泛化能力 | ✅ |
| 2 | high | - | [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for M...](http://arxiv.org/abs/2608.22479v1) | policy optimization | 在Qwen2.5-3B和7B骨干模型上，GTA-RAG均稳定优于RL类RAG基线，大幅提升证... | 基于轨迹级监督，结合GRPO与轨迹引导奖励优化检索策略，兼顾答案准确性与证据获取... | 仅在封闭问答基准评测，未验证开放域复杂场景的泛化能力。 | ✅ |
| 3 | high | - | [How to Train a Critic Stably and Efficiently](http://arxiv.org/abs/2608.23566v1) | policy optimization | 精心设计的单回复评价器训练方案，每个prompt仅采样一个回复，就能匹配甚至超过分组多回复采... | 通过优化评价器训练流程，引入多项适配设计，稳定评价器训练过程，提升强化学习的优势... | 仅在数学推理任务验证方法效果，缺乏跨不同类型任务的泛化性验证 | ✅ |
| 4 | high | - | [On-policy Distillation with Verifiable Reward](http://arxiv.org/abs/2608.24696v1) | online distillation | 无需新增任何超参数即可无缝结合OPD与RLVR，在六个推理基准上性能稳定优于标准同策略蒸馏。 | 结合同策略蒸馏的密集监督信号与RLVR的任务正确性，通过ReLU门控对齐蒸馏信号... | 未披露具体推理基准细节，方法仅在推理任务验证，跨任务通用性待验证... | ✅ |
| 5 | high | ICML 2026 | [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reaso...](http://arxiv.org/abs/2608.23493v1) | policy optimization | 基于Qwen3-8B的SRPO仅用缩放监督微调8%的训练FLOPs，就在AIME'24达到7... | 通过大模型自反思生成反思补丁，以自生成的教师分数作为稠密token级训练信号优化... | 自反思生成的反思补丁质量依赖模型自身能力，可能存在质量不稳定，导... | ✅ |
| 6 | high | - | [AHEAD: Adaptive Hindsight with Environment-Augmented Distillatio...](http://arxiv.org/abs/2608.24114v1) | online distillation | 7B规模模型上，AHEAD较GRPO在ALFWorld提升13.3个点任务成功率，在WebS... | 通过步感知自适应匹配监督源，结合环境增强蒸馏与LLM矫正提示，对GRPO做极小改... | 仅在三个学术基准验证，未测试大规模真实场景，额外LLM生成矫正提... | — |
| 7 | high | - | [Agent-G$^2$: Gaussian Guidance for Agentic Reinforcement Learnin...](http://arxiv.org/abs/2608.23318) | policy optimization | 有用引导深度的信息量近似服从围绕中心带的高斯分布，方法性能超基线2.3-7.4个点，成本仅为... | 通过在线估计引导深度的高斯分布，优化智能体探索起点，缓解奖励稀疏，降低额外采样成... | 仅在两个中小型文本智能体基准验证，未在更大规模复杂长视界任务验证... | — |
| 8 | high | - | [Agentic Game Development as a Verifiable Trajectory Data Engine ...](http://arxiv.org/abs/2608.25518v1) | reward learning | 游戏引擎可自动输出空间场景的碰撞、物理、可通行性等可验证密集奖励，适配空间世界模型的RL后训... | 通过游戏引擎自动生成可验证的密集奖励信号，结合开发者人工验证反馈，支撑空间世界模... | 未给出实际实验验证结果，方法的实际有效性未得到实证确认 | — |
| 9 | high | - | [Beyond Success and Failure: Length-Aware Contrastive Learning fo...](http://arxiv.org/abs/2608.21830v1) | policy optimization | 引入轨迹层长度感知的结构化偏好，可提供更有效学习信号，在稳定优化同时一致提升GUI智能体性能... | 通过在对比RLVR框架中引入轨迹层级长度感知结构化偏好，优化智能体策略，缓解奖励... | 未在大规模真实GUI场景验证，方法泛化性和落地能力有待进一步验证... | — |
| 10 | high | - | [Beyond the Stability-Exploration Dilemma: Environmental Regulari...](http://arxiv.org/abs/2608.23311v1) | policy optimization | 输入侧查询KL不会对响应分布施加直接梯度压力，可在保留探索空间的同时控制分布偏移，提升性能与... | 通过引入输入侧的查询KL正则项约束查询分布偏移，不直接影响响应分布梯度，兼顾优化... | 仅在数学推理任务验证，未在多类Agent任务验证，方法泛化性有待... | — |
| 11 | high | - | [BioMed-Agent-RL: A Meta Learning, All You Need for Biomedical Ap...](http://arxiv.org/abs/2608.21864v1) | policy optimization | 该智能体在多个医疗基准上达到约73%准确率，相较现有基线提升约5%，性能超过GPT-5等现有... | 通过结合动态熵调节的偏好优化与强化学习，引导智能体自适应整合临床信息，提升输出可... | 仅在公开基准完成评测，未在真实临床场景验证，临床落地的安全性未得... | — |
| 12 | high | - | [Boosting LLM Exploration via Weak-Model Guidance in RLVR](http://arxiv.org/abs/2608.27420v1) | policy optimization | 分布存在差异的弱模型前缀能有效缓解RLVR熵坍缩，评测的k值越大，该方法的性能提升越显著。 | 通过引入弱模型生成的陌生推理前缀扰动，打破模型过度自信，缓解熵坍缩，提升RLVR... | 仅在数学推理基准完成验证，方法在其他类型任务上的通用性未得到验证... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **policy optimization**：33 篇
- **reward learning**：9 篇
- **online distillation**：5 篇
- **other**：4 篇
- **evaluation/benchmark**：3 篇
- **unlearning/safety**：3 篇
- **agent harness**：2 篇
- **skill generation**：2 篇
- **reliability improvement**：1 篇
- **tool-use control**：1 篇
- **model steering**：1 篇

## 失败模式与风险信号

- 单维度对齐忽略跨维度副作用，离策略无校正蒸馏会引发鲁棒性灾难性崩溃
- 基于评价器的标准强化学习训练不稳定
- 稀疏终端监督导致信用分配不佳，训练数据效率低下
- 传统动作侧Policy-KL正则无法兼顾策略优化稳定性与探索，易出现分布漂移或探索不足
- 不符合工具顺序约束，无法应对权限限制与意外运行时错误
- 审议冗余、证据聚合不可靠、辩论调节能力弱
- 现有对齐大模型存在未被发现的多轮心理越狱安全漏洞，现有方法难以发现该类漏洞。
- 传统知识蒸馏应用于扩散语言模型提升有限，甚至劣化生成质量
- 大规模LLM推演中长尾长生成拖慢整体步骤完工时间，均匀路由加剧该性能问题
- 现有RAG无法区分语义相似性与地理有效性，地理相关问题错误置信率过高

## 评测信号

- 检测单维度评估无法发现的可信性跨维度权衡，量化安全对齐、蒸馏等操作对各维度性能的影响。
- 在1.5B到30B参数的模型上，BPCO持续提升基线性能，单回复采样即可匹配或超越分组多回复基线
- 数据效率远优于缩放监督微调，仅用其8%的训练FLOPs就取得更高的推理准确率和智能体任务成功率
- 替换标准Policy-KL后，在六个数学推理基准获得更高精度，高温解码与长周期训练下行为更稳定
- 发现当前前沿大语言模型在移动场景下可靠性不足，在严格运行约束与运行时异常下性能会大幅下滑。
- Meta-Moderator性能优于现有常用决策层，具备跨任务、跨系统配置迁移能力，可降低证据错误聚合概率。
- PsychJail取得87.3%的平均攻击成功率，性能优于所有对比的单轮和多轮攻击基线方法。
- 在指令跟随任务中，SelFusion性能优于所有对比的带外部教师的知识蒸馏方法，多配置下学生模型超过LLM教师性能。
- 验证了方案可在不引入额外长度偏差、保留在线策略生成特性的前提下，大幅提升LLM大规模推演速度，最高取得2.59倍相对加速。
- 该方法将位置相关问题的错误置信率降至0.009，远低于基线的约0.090，人类偏好对齐程度也显著优于基线。

## 控制机制 / Harness 信号

- 构建统一黑盒评测框架，输出分层风险画像与跨维度权衡分析，为大模型可信性对齐提供反馈。
- 通过优化评价器训练流程，引入多项适配设计，稳定评价器训练过程，提升强化学习的优势估计质量
- 通过大模型自反思生成反思补丁，以自生成的教师分数作为稠密token级训练信号优化策略，无需额外奖励模型或大教师
- 通过引入输入侧的查询KL正则项约束查询分布偏移，不直接影响响应分布梯度，兼顾优化稳定性和探索性
- 构建带实时应用数据库的可执行交互式沙箱，结合基于证据的验证，为移动智能体研发提供评测反馈。
- 通过结果驱动策略优化训练可学习元协调器，动态监测辩论效用，调节审议进程，控制输出答案时机。
- 基于社会心理学说服理论与说服知识模型设计攻击策略，用带PKM门控奖励的强化学习优化攻击agent策略。
- 通过双向自蒸馏改进扩散语言模型生成质量，基于token级正确性动态调整蒸馏方向，无需依赖外部教师模型。
- 通过部分推演识别长尾生成，分离长尾与普通生成的资源池，动态调整副本分配，优化推演总完工时间，提升推演速度。
- 在检索阶段引入基于DAG距离的地理适用性估计，通过选择性回答机制降低RAG生成错误回答的风险。

## 可靠性 / 落地风险

- 大规模跨维度评测需要数千次测试运行，评测成本较高，规模化落地存在一定门槛。
- 仅在数学推理任务验证方法效果，缺乏跨不同类型任务的泛化性验证
- 自反思生成的反思补丁质量依赖模型自身能力，可能存在质量不稳定，导致优化效果出现波动
- 仅在数学推理任务验证，未在多类Agent任务验证，方法泛化性有待进一步验证
- 现有大模型驱动的端侧移动智能体真实场景可靠性不足，距离实际工业落地还有较大差距。
- 未披露具体基准细节，缺乏细分场景测试，框架泛化可靠性未得到充分验证。
- 提出的多轮心理越狱方法可能被恶意滥用，对模型特征的解读未验证，结论不确定性较高。
- 仅在指令跟随任务验证，未涉及大规模落地测试，两次前向传播会增加训练阶段的计算成本。
- 依赖长尾提示在策略更新中保持长尾的假设，若假设不成立，方法性能会出现明显下降。
- 仅针对地理领域场景设计，通用性不足，泛化能力未在其他领域得到验证。

## 代码资源

- [On-policy Distillation with Verifiable Reward](https://github.com/LeapLabTHU/OPDVR.) · 6 stars
- [EDGE: Experience-Distillation for Guided Exploration in Agentic Reinforcement Le...](https://github.com/xvolcano02/EDGE.) · 3 stars
- [How to Train a Critic Stably and Efficiently](https://github.com/QPHutu/golden_critic) · 1 stars
- [SRPO: Self-Reflective Policy Optimization for Long-Horizon Reasoning](https://github.com/Galleons2029/SRPO) · 1 stars
- [SelFusion: Self-distillation for Diffusion Language Models](https://github.com/scai-research/SelFusion_official)
- [GTA-RAG: Graph-Trajectory-Augmented Reinforcement Learning for Multi-Turn Retrie...](https://github.com/cjcj46262/GTA-RAG.)
- [PhysMLLMs: Spatial Priors for Unified Referring Segmentation and Grounded Reason...](https://github.com/tusu-code/20260121-icml2026-2.git.)
- [Behavior2Trip: Towards Personalized Travel Planning via User Behavior Trajectory](https://github.com/BUAA-IRIP-LLM/Behavior2Trip)

## 常见基线方法

- **GRPO**：4 篇
- **单维度独立评估框架**：1 篇
- **基于评价器的基线方法**：1 篇
- **基于分组的强化学习基线方法**：1 篇
- **现有最优方法**：1 篇
- **缩放监督微调**：1 篇
- **标准Policy-KL正则化策略优化**：1 篇
- **传统动作侧正则化方法**：1 篇
- **固定预算协调方法**：1 篇
- **一致性停止方法**：1 篇

## 常用数据集

- **WebShop**：6 篇
- **ALFWorld**：6 篇
- **摘要未提及**：3 篇
- **aiXamine内置46项跨维度测试**：1 篇
- **数学推理任务基准**：1 篇
- **AIME'24**：1 篇
- **SWE-Bench-Lite**：1 篇
- **六个数学推理基准**：1 篇
- **MobilePA-Bench**：1 篇
- **五个推理基准**：1 篇

---
*自动生成于 2026-08-30 | ArXiv_Daily_Digest*