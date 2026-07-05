# Agent 策略优化与在线蒸馏 — 2026-W27 (06/29-07/05)

本周新增 **64** 篇论文，**6** 篇附带代码。优先级：high 29 / medium 27 / low 8。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | ICML 2026 | [Geometry-Preserving Orthonormal Initialization for Low-Rank Adap...](http://arxiv.org/abs/2606.31813v1) | policy optimization | SFT上表现更优的PiSSA、MiLoRA在RLVR中性能劣于标准LoRA，正交初始化能最小... | 通过改进RLVR中低秩适配的初始化方式，稳定RLVR训练过程，缩小LoRA与全微... | 仅在数学推理基准验证，未在多类agent任务测试，方法通用性有待... | ✅ |
| 2 | high | - | [ATOD: Annealed Turn-aware On-policy Distillation for Multi-turn ...](http://arxiv.org/abs/2606.27814v1) | online distillation | 三种学生尺寸下，ATOD平均成功率比OPD高3.03个点、比GRPO高23.62个点，还超出... | 通过退火调度结合同策略蒸馏与强化学习，配合轮级分歧不确定性重加权，优化多轮智能体... | 仅在中小规模公开基准评测，未验证在大规模复杂任务上的泛化落地效果... | — |
| 3 | high | - | [BV-Blend: Uncertainty-Weighted Historical Baselines for Stable C...](http://arxiv.org/abs/2606.28707v1) | policy optimization | GRPO在提示组所有采样奖励相同时会得到零优势导致训练停滞，加入加权历史基线可有效缓解该问题... | 通过混合提示局部统计与语义簇历史奖励矩，用不确定性加权得到稳定优势估计，优化RL... | 仅在封闭可验证推理基准验证，未测试开放域多步agent任务中的泛... | — |
| 4 | high | - | [Beyond Next-Token Prediction: An RLVR Proof of Concept for Tool-...](http://arxiv.org/abs/2607.01465v1) | policy optimization | 在4个非退化奖励场景中，RL训练将平均奖励从基线0.35-0.92提升至0.95-1.00，... | 通过基于工具调用轨迹手工设计的可验证规则奖励，训练优化Agent的工具调用策略，... | 手工设计可验证奖励扩展性不足，仅支持少量端点，难以推广到大规模企... | — |
| 5 | high | ICML 2026 | [Can Agents Generalize to the Open World? Unveiling the Fragility...](http://arxiv.org/abs/2607.01084v1) | evaluation/benchmark | 经监督微调和强化学习训练的静态工具智能体，面对开放环境分布偏移均会出现不同程度的性能下降 | 通过在监督微调阶段引入扰动增强训练，提升工具使用智能体应对开放环境分布偏移的鲁棒... | 仅在自建可控沙盒验证，未测试真实开放场景，结论落地有效性有待进一... | — |
| 6 | high | - | [DOPD: Dual On-policy Distillation](http://arxiv.org/abs/2606.30626v1) | online distillation | 引入特权信息提升蒸馏质量会引发特权幻觉，且整个监督序列中仅少量token携带关键能力相关信号 | 通过优势感知动态分配不同token的监督信号，采用双蒸馏范式传递可信能力，缓解特... | 未在实际下游agent任务验证，方法在真实场景的落地效果尚不明确 | — |
| 7 | high | - | [DRIFT: Difficulty Routing Self-DIstillation with Rhythm-Gated Ex...](http://arxiv.org/abs/2606.30345v1) | online distillation | 结合难度路由的在线自蒸馏在五个基准平均得分达79.5%，比GRPO高9.5%，比SDPO高7... | 通过难度路由动态分配优化信号，节奏门控聚焦关键推理位置探索，结合成功缓冲与课程学... | 仅披露一个基准的具体名称，全部评测基准信息未公开，存在可复现性风... | — |
| 8 | high | - | [DecompRL: Solving Harder Problems by Learning Modular Code Gener...](http://arxiv.org/abs/2607.02390v1) | policy optimization | 分解为n个模块各生成k个实现可得到k^n个候选解，GPU令牌成本降低约50倍，可解决标准方法... | 通过强化学习引导模型学习问题分解与分层模块化代码生成，转移推理瓶颈，降低GPU计... | 依赖问题可分解为独立子模块的特性，不可分解的难题无法适用该方法。 | — |
| 9 | high | - | [Don't Let Gains FADE: Breaking Down Policy Gradient Weights in R...](http://arxiv.org/abs/2607.01490v1) | policy optimization | 优势更新的两种权衡随训练阶段动态变化，FADE在7B规模比最优静态基线早20k步达到峰值pa... | 通过动态自适应调整优势函数的梯度权重，稳定强化学习后训练，缓解多样性坍缩，加快收... | 仅在代码推理任务验证，方法通用性未得到多场景验证，存在泛化不确定... | — |
| 10 | high | - | [DuoMem: Towards Capable On-Device Memory Agents via Dual-Space D...](http://arxiv.org/abs/2606.29961v1) | online distillation | 双空间蒸馏可将4B参数智能体任务成功率从4.3%提升至77.9%，推理速度比72B教师快3倍... | 通过双空间蒸馏将大教师模型的问题求解能力迁移到小参数学生模型，分别在上下文和参数... | 仅在单个基准验证效果，未在更多类型的端侧智能体任务上验证方法的通... | — |
| 11 | high | ICML 2026 | [Experience Augmented Policy Optimization for LLM Reasoning](http://arxiv.org/abs/2606.30420v1) | policy optimization | 在Qwen-2.5-math 7B和Qwen-3-8B五个基准上，EAPO相比现有最优RLV... | 通过策略自适应的经验复用结合适配重要性采样，基于可验证奖励强化学习优化大模型推理... | 仅在7B、8B规模模型上验证，未测试更大规模模型，方法泛化性待工... | — |
| 12 | high | - | [From Search to Synthesis: Training LLMs as Zero-Shot Workflow Ge...](http://arxiv.org/abs/2606.30704v1) | reward learning | 单轮推理下MetaFlow域内任务性能媲美SOTA，对未训练任务和新算子集具备出色零样本泛化... | 先通过合成工作流数据监督微调学习任务模式，再利用执行反馈的可验证奖励强化学习优化... | 依赖合成训练数据，未在真实复杂工业场景验证，实际部署的可靠性有待... | — |

## A 会 / Venue 标签

- **ICML 2026**：6 篇

## 方法族分布

- **policy optimization**：30 篇
- **online distillation**：8 篇
- **reward learning**：8 篇
- **other**：7 篇
- **evaluation/benchmark**：5 篇
- **model steering**：2 篇
- **unlearning/safety**：1 篇
- **skill generation**：1 篇
- **知识蒸馏**：1 篇
- **multi-agent coordination**：1 篇

## 失败模式与风险信号

- RLVR推理分布漂移、可读性差，强模型推理模式不兼容弱模型与人类
- 同策略蒸馏性能饱和，强化学习早期学习效率低下
- 对抗投毒输入下，现有事实验证方法的准确率不足
- 历史旁路导致潜在表示不可识别，模型预测绕过瓶颈表示
- 现有大模型易被对抗输入规避安全防护，多步推理与工具使用场景下易发生安全失效
- 长周期任务中智能体为反应式，后训练微调前瞻能力仅能得到无真实基础的表面模仿。
- 无法正确更新记忆，保留过时事实导致推理准确率大幅下降
- 奖励信号获取成本高，自主评估噪声导致奖励不准，降低智能体任务成功率
- 原有编排器每步都需调用前沿大模型API，单任务推理成本过高
- 可读的挖掘技能结构无法有效转化为跨域下游策略的性能提升

## 评测信号

- 评测了单模型推理能力、跨模型交接鲁棒性、分布漂移程度与思维链可读性，验证方法实际收益。
- 在三个基准、三种学生尺寸下，ATOD平均成功率较基线显著提升，最高较GRPO提升23.62个点，且超过对应教师模型。
- 在多个骨干大语言模型上评测，相比基线性能提升4-24个百分点，对抗投毒样本上提升更显著
- 保留一步预测精度的前提下，最高提升57%表示质量、98% rollout性能，性能增益随任务复杂度提升而增大。
- 8B参数Yuvion在多项安全任务超越更大尺寸SOTA基线，对抗条件下鲁棒性优势显著，同时保持合格的整体模型能力。
- 在多个细粒度基准上优于多个现有蒸馏方法，在Waterbirds上大幅提升最坏组分类准确率，增强对伪相关的鲁棒性
- 所提方法在搜索和数学推理两类任务上，性能稳定优于所有对比的训练基线方法，验证了训练流水线的有效性。
- 对比不同记忆设置下的过时事实处理准确率，验证训练方案能提升未见对话的记忆更新准确率
- 核心评测信号为CUA在多OS基准环境下的任务完成成功率，对比不同奖励方式的性能提升幅度
- 任务成功率达到或超过GPT-5-mini基线，接近Gemini-3-Flash，编排成本降低超一个数量级，调用量降40%-50%

## 控制机制 / Harness 信号

- 通过团队联合奖励引导强模型生成适配弱模型的推理，采用GRPO损失优化强模型的策略。
- 通过退火调度结合同策略蒸馏与强化学习，配合轮级分歧不确定性重加权，优化多轮智能体训练。
- 通过强化学习训练多源检索与证据评估两个agent，构建层次化证据树实现可解释的声明验证
- 提出分解GRPO强化学习方法，在世界模型训练中强制执行严格中介约束，约束模型依赖瓶颈表示生成预测。
- 通过对抗感知数据构建、知识增强持续预训练，结合基于强化学习的安全策略后训练，提升模型对抗鲁棒性。
- 通过跨模态知识蒸馏，利用大语言模型生成的概念软标签作为辅助监督，引导视觉学生模型学习
- 通过三阶段能力优先的训练流水线，向策略注入世界模型预测能力，再用强化学习优化校准前瞻预测。
- 构建带事实时效性奖励的强化学习环境，通过GRPO微调优化智能体策略，缩小记忆更新鸿沟
- 利用视觉语言模型做自主任务评估提供奖励信号，建模并修正评估噪声，改进PPO奖励估计以优化智能体策略。
- 利用外部验证器认证的正确规划精修轨迹做监督信号，微调小模型得到编排策略，结合硬编码规则降低推理成本。

## 可靠性 / 落地风险

- 仅在竞赛数学单任务验证，未验证开放域泛化性，协同生成推理会增加额外的步骤开销。
- 仅在中小规模公开基准评测，未验证在大规模复杂任务上的泛化落地效果。
- 未披露具体评测数据集与实现细节，方法的可复现性存在一定不确定性
- 该方法仅在小型文本游戏环境验证，复杂真实场景下的泛化性和稳定性尚未得到验证。
- 评测全部基于自建基准开展，缺乏真实大规模落地场景验证，实际部署的鲁棒性仍待验证。
- 该研究针对视觉任务，未验证在agent场景下的泛化性，与当前研究方向匹配度较低
- 三阶段训练流水线工程复杂度较高，仅在简单任务验证，未测试大规模真实场景的泛化性。
- 目前仅在小模型上验证了有限提升，大模型上的训练效果和泛化性尚未得到验证
- 自主评估的固有错误无法被完全消除，不同任务下评估一致性波动，影响性能稳定性
- 依赖外部验证器提供训练轨迹，验证器自身错误会传导到编排策略，影响结果可靠性

## 代码资源

- [GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screensho...](https://github.com/fansunqi/GUICrafter.) · 3 stars
- [Geometry-Preserving Orthonormal Initialization for Low-Rank Adaptation in RLVR](https://github.com/Richard-ZZZ/geometry-preserving-orthonormal-init-rlvr.) · 1 stars
- [Large Language Model Teaches Visual Students: Cross-Modality Transfer of Fine-Gr...](https://github.com/lliangthomas/lavid.)
- [Breaking Failure Cascades: Step-Aware Reinforcement Learning for Medical Multimo...](https://github.com/dmis-lab/MRPO)
- [SLIM-RL: Risk-Budgeted Random-Masking RL for Diffusion LLMs Without Trajectory S...](https://github.com/laolaorkkkkk/SLIM-RL)
- [FaithMed: Training LLMs For Faithful Evidence-Based Medical Reasoning](https://github.com/cxcscmu/FaithMed.)

## 常见基线方法

- **GRPO**：6 篇
- **标准强化学习**：2 篇
- **多数投票**：2 篇
- **vanilla GRPO**：1 篇
- **OPD**：1 篇
- **GPT-5.4**：1 篇
- **Qwen3-MAX**：1 篇
- **MaKD**：1 篇
- **DKD**：1 篇
- **MLKD**：1 篇

## 常用数据集

- **摘要未提及**：5 篇
- **数学推理任务**：3 篇
- **五个推理基准**：3 篇
- **数学推理基准**：3 篇
- **ALFWorld**：2 篇
- **AIME**：2 篇
- **LiveCodeBench**：2 篇
- **竞赛数学推理**：1 篇
- **WebShop**：1 篇
- **Search-QA**：1 篇

---
*自动生成于 2026-07-05 | ArXiv_Daily_Digest*