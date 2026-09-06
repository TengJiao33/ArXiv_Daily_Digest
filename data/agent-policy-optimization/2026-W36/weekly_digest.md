# Agent 策略优化与在线蒸馏 — 2026-W36 (08/31-09/06)

本周新增 **73** 篇论文，**8** 篇附带代码。优先级：high 31 / medium 24 / low 18。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory ...](http://arxiv.org/abs/2608.29622v1) | policy optimization | 引入细粒度动作建模与信息感知优化的强化学习框架，在长程多步推理中性能稳定优于强基线，推理更鲁... | 通过设计细粒度动作空间、分层动作感知奖励与信息感知轨迹拒斥策略，改进智能体长程推... | 仅在标准基准测试，未验证复杂开放真实场景表现，实际落地泛化性存在... | ✅ |
| 2 | high | - | [Gradients Know What Outcomes Don't: Unlocking Reinforcement Lear...](http://arxiv.org/abs/2609.03342v1) | reward learning | GAR仅带来不到9%的额外时钟开销，在Qwen3模型上稳定优于GRPO，可无领域特定数据跨域... | 通过设计梯度对齐的密集推理奖励，改进RLVR训练，提升大语言模型推理任务的性能表... | 依赖专家锚点梯度质量，存在额外计算开销，大规模部署的成本控制有待... | ✅ |
| 3 | high | - | [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Disti...](http://arxiv.org/abs/2609.02548v1) | online distillation | 该方法将Qwen3-8B最弱领域性能提升14.79个点，领域差距缩小74.7%，效果优于按域... | 通过答案验证筛选合格教师，利用多教师蒸馏将多个固定教师的多领域能力整合到单个学生... | 依赖验证器的判断准确性，未在公开标准基准验证，实际泛化性不明确。 | ✅ |
| 4 | high | - | [One Policy, Any Budget: Internalizing Budget-Aware Search via Re...](http://arxiv.org/abs/2609.00813v1) | policy optimization | 单个训练后的策略即可适配所有规模的搜索预算，还能泛化到训练范围外的未见约束，工具效率更优无多... | 通过两阶段课程强化学习训练，设计自适应加权复合奖励，引导智能体学习适配任意预算的... | 仅在问答基准完成评测，未在真实复杂搜索场景验证，落地泛化性有待进... | ✅ |
| 5 | high | - | [WM-R1: Training GUI Agents to Reason and leverage World Models w...](http://arxiv.org/abs/2608.27508) | policy optimization | 用世界模型替代训练过程的真实环境，训练出的GUI智能体性能显著优于仅GRPO基线和推理时仿真... | 通过世界模型替代真实环境生成训练轨迹，设计多维规则奖励，优化GUI智能体的训练与... | 训练效果完全依赖世界模型的准确性，世界模型的误差会传递，影响最终... | ✅ |
| 6 | high | - | [APEx: Distillation of Agent Procedural Experience for Adaptive D...](http://arxiv.org/abs/2609.02253v1) | online distillation | APEx在7个基准测试上取得最优性能，相比GPT-5.4提升14.7个百分点，相比最强记忆增... | 通过执行器、蒸馏器、规划器的闭环架构，结合奖励引导技能蒸馏和技能对齐正则化，实现... | 仅在公开基准验证，未提及真实场景泛化性，实际部署的成本与稳定性未... | — |
| 7 | high | - | [ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Us...](http://arxiv.org/abs/2608.30685v1) | evaluation/benchmark | 该诊断框架生成的反馈支撑策略优化后，在线上A/B实验中同时提升了用户参与度、下游业务结果与人... | 通过双视野诊断输出反馈支撑智能体策略优化，将LLM裁判决策蒸馏得到低延迟低成本的... | 依赖真实业务日志的高置信度参考校准LLM裁判，大规模落地校准成本... | — |
| 8 | high | - | [Act More, Decide Less: Skill-Guided Adaptive Action Chunking for...](http://arxiv.org/abs/2609.02042v1) | policy optimization | 标准强化学习训练变长动作分块会出现两类失效，本文方法可提成功率7.0%-31.3%，最多减7... | 从成功轨迹诱导程序化技能，以子技能边界作为分块监督，蒸馏优化策略，自适应调整动作... | 依赖成功轨迹提取监督，仅在两个封闭基准验证，开放场景泛化性未验证 | — |
| 9 | high | - | [CARE: Contrastive Anchor-based Rubric Evolution for Large Langua...](http://arxiv.org/abs/2609.00892v1) | reward learning | CARE是唯一在300步训练中，对GPT-4.1锚点响应胜率保持持续提升的方法，在多个基准达... | 依托前沿模型生成的锚点响应演化动态评分准则，通过双分支修正奖励错配，维持高奖励区... | 依赖前沿大模型生成高质量锚点，锚点质量决定最终效果，训练过程计算... | — |
| 10 | high | - | [CAST: Critique-Aware Supervision for Training Reliable Long-Hori...](http://arxiv.org/abs/2608.30147v1) | policy optimization | 加入评论感知监督后，零售任务pass^4超出GPT-OSS-120B超10%，域外远程医疗任... | 从Agent轨迹合成动作有效性的结构化理由训练评论模型，再用评论模型构造监督信号... | 需要额外训练评论模型，增加了训练流程复杂度，理由合成质量会直接影... | — |
| 11 | high | - | [Cliff: Learning Process Rewards from the First Mistake](http://arxiv.org/abs/2609.02817v1) | reward learning | 即使使用能力一般的教师模型，Cliff方法也能提升推理性能，比在线蒸馏高15%，比标准GRP... | 通过识别推理轨迹的首个错误生成细粒度token级优势奖励，改进RLVR的监督信号... | 依赖教师模型识别首个错误，教师自身的识别错误会传递给学生，性能受... | — |
| 12 | high | - | [DE-Venus: A Data-Efficient RLVR Framework for Large Language Mod...](http://arxiv.org/abs/2609.03324v1) | reward learning | 仅需10%标注量或13%相关数据即可保持或提升模型质量，特定配置可将收敛步数降低63%~75... | 通过主动数据选择、弱监督构建、训练监督细化三个模块优化RLVR流程，提升数据效率... | 未披露公开基准的具体细分结果，通用性验证不够充分，落地需进一步验... | — |

## 方法族分布

- **policy optimization**：30 篇
- **reward learning**：10 篇
- **evaluation/benchmark**：9 篇
- **online distillation**：5 篇
- **multi-agent coordination**：5 篇
- **model steering**：4 篇
- **unlearning/safety**：3 篇
- **other**：3 篇
- **survey**：1 篇
- **知识蒸馏**：1 篇
- **policy optimization, online distillation**：1 篇
- **skill generation**：1 篇

## 失败模式与风险信号

- 顺序测试时缩放对上下文构建敏感，大推理预算下会降低翻译准确率
- 大语言模型数学推理中计算错误占不正确响应的比例较高
- 现有方法反馈与评分解耦、独立评估特征，导致评分反馈一致性差、与评分规则对齐性弱
- 长程稀疏奖励下信用分配不准确，现有方法无法利用验证器内部结构信息
- 教师引导与结果奖励不对齐，误导学生模型优化过程，降低最终模型性能
- 现有恶意上下文窃取攻击无法有效诱导Agent将运行上下文作为输入传入恶意工具
- 传统RLHF的标量奖励缺乏可解释性，无法捕捉响应质量多面性，还存在奖励黑客等问题。
- 强化训练依赖大量真实环境交互，训练成本高、稳定性差
- 长视野交互信用分配粗糙，特权监督与可执行动作存在监督-信用不匹配
- 直接生成分子结构未显式建模专业人员的分析工作流程

## 评测信号

- 对比两类测试时缩放在不同采样预算下的翻译表现，验证顺序缩放的鲁棒性与上下文敏感性
- 在无训练数据重叠的新Countdown基准上评测，工具整合提升约10个百分点pass@k，Tool-DAPO将pass@1提升至66.0%
- HiFTS在两个数据集上均取得优异的整体与特征级评分效果，同时可生成连贯、对齐评分规则的反馈。
- 在ALFWorld和WebShop上性能大幅优于仅结果训练，性能媲美近期细粒度信用方法，通过消融验证了设计有效性。
- 在Qwen3和DeepSeek-R1系列模型测试，RA-OPD在所有基准性能均显著优于对比基线，无额外计算成本。
- 攻击效果显著优于现有恶意工具攻击，在受害者与影子用户上下文差异较大时仍保持高攻击有效性。
- 本文为综述研究，未开展实证实验，摘要未提及具体的评测信号与实验结果。
- 在安卓移动基准测试中，WM-R1训练的GUI智能体表现显著优于GRPO-only基线和推理时仿真方法。
- 在三个智能体基准上相比GRPO绝对性能提升10.6%，对未见任务的泛化能力也更优异。
- 在多个基准上性能 consistently优于现有通用大模型与光谱专用模型，训练数据量仅为SpectraLLM的不到十分之一。

## 控制机制 / Harness 信号

- 本文通过评估对比不同测试时采样缩放策略，探究其对大语言模型翻译输出性能的影响规律
- 先通过监督微调教授工具使用模式，再基于自动验证的最终答案奖励，用强化学习优化工具调用行为
- 通过教师大模型的分层反馈知识蒸馏，结合基于复合奖励的策略优化，引导模型生成对齐规则的反馈与分数。
- 利用终端验证器内部任务结构，通过依赖边追溯动作信用并重分配优势，优化智能体训练，无需额外学习模块。
- 通过检查轨迹级蒸馏回报与结果奖励的一致性，过滤不对齐轨迹，用可靠轨迹完成同策略蒸馏优化学生模型。
- 该工作通过带定制奖励函数的强化学习微调攻击LLM，生成可诱导Agent泄露上下文的恶意工具实现攻击。
- 本文作为综述构建了领域统一分类框架，分析影响对齐可靠性的关键因素，梳理研究脉络与开放问题。
- 通过世界模型替代真实环境生成训练轨迹，设计多维规则奖励，优化GUI智能体的训练与推理行为。
- 结合特权监督信息，通过结果锚定的动作级信用重分配调整优化目标，改进策略性能，稳定训练过程。
- 通过技能码引导分析流程，结合监督微调和步级强化学习，约束智能体遵循专业分析逻辑生成结果。

## 可靠性 / 落地风险

- 仅在机器翻译任务验证结论，未验证该结论在其他任务上的泛化有效性
- 仅在Countdown任务验证，方法在其他复杂推理任务的泛化性未得到验证
- 方法效果依赖教师大模型的蒸馏质量，新增CFMS-34数据集规模较小，结论推广性有待验证。
- 依赖带有可编码检查信息的终端验证器，通用性受限，仅适用于可验证类任务。
- 仅在数学、代码两类任务验证，未覆盖更多通用场景，方法泛化能力有待进一步验证。
- 仅提出攻击未探索防御方案，落地Agent缺乏对应防护，容易发生用户隐私信息泄露。
- 本文为综述研究，无实证验证，梳理结论未经过实践检验，直接对工业落地的指导有限。
- 训练效果完全依赖世界模型的准确性，世界模型的误差会传递，影响最终智能体性能。
- 未披露具体基准细节，未在大规模真实场景验证，结果可复现性存在一定不确定性。
- 依赖自建光谱技能库，未验证大规模工业场景泛化性，泛化能力存在不确定性。

## 代码资源

- [AgenticRag-R1: Agentic Reinforcement Learning with Stack Memory for Multi-Step R...](https://github.com/jiangxinke/Harness-RL) · 435 stars
- [WM-R1: Training GUI Agents to Reason and leverage World Models with Reinforcemen...](https://github.com/genalyu/WM-R1) · 21 stars
- [StudentSim: Training LLM-based Student Simulators](https://github.com/microsoft/StudentSim.) · 14 stars
- [SemPOI-RL: Aligning LLM Semantic Reasoning for Interpretable Out-of-Town POI Seq...](https://github.com/Wind-Flipped/SemPOI-RL) · 2 stars
- [Learn from Whoever Is Right: Answer-Verified Multi-Teacher Distillation for Mult...](https://github.com/hexixiang/MT-SDPO.) · 1 stars
- [GenRubric: Self-Evolving Rubric Generation for Scalable LLM Evaluation](https://github.com/foggpoy/GenRubric.)
- [One Policy, Any Budget: Internalizing Budget-Aware Search via Reinforcement Lear...](https://github.com/xwsun01/AnySearch.)
- [Gradients Know What Outcomes Don't: Unlocking Reinforcement Learning for LLM Rea...](https://github.com/LQgdwind/GAR.)

## 常见基线方法

- **GRPO**：4 篇
- **GPT-5.4**：2 篇
- **摘要未提及具体基线**：2 篇
- **并行独立采样重排序**：1 篇
- **Tool-SFT**：1 篇
- **RLOO**：1 篇
- **RLOO++**：1 篇
- **现有反馈增强自动作文评分方法**：1 篇
- **仅结果训练**：1 篇
- **现有细粒度信用分配方法**：1 篇

## 常用数据集

- **摘要未提及**：5 篇
- **ALFWorld**：4 篇
- **WebShop**：3 篇
- **Countdown数学推理任务**：1 篇
- **1024题无重叠留存Countdown基准**：1 篇
- **CFMS-34**：1 篇
- **ASAP++**：1 篇
- **数学评测基准**：1 篇
- **代码评测基准**：1 篇
- **自制2000个挑战性任务数据集**：1 篇

---
*自动生成于 2026-09-06 | ArXiv_Daily_Digest*