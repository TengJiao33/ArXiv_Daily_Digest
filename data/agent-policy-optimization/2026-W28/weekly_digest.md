# Agent 策略优化与在线蒸馏 — 2026-W28 (07/06-07/12)

本周新增 **42** 篇论文，**1** 篇附带代码。优先级：high 23 / medium 14 / low 5。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [When Implausible Tokens Get Reinforced: Tail-Aware Credit Calibr...](http://arxiv.org/abs/2607.07976v1) | policy optimization | 统一信用分配存在正信用污染失败模式，错误低概率尾token会获得同等正信用，TACO可提升长... | 通过计算融合上下文的尾风险评分识别风险token，调整风险token的正信用更新... | 仅在通用基准验证方法效果，未在实际下游agent任务测试，实际落... | ✅ |
| 2 | high | - | [ACPO: Adaptive Credit Policy Optimization via Fine-Grained Surro...](http://arxiv.org/abs/2607.03126v1) | policy optimization | 基于模局部代理熵的自适应信用分配可保持正确策略梯度，在推理编码任务上稳定优于多个强RL基线 | 通过token级自适应信用分配，基于代理熵不对称调整策略更新，提升大语言模型强化... | 仅在数学推理和编码任务验证，方法通用性尚未得到更多任务场景验证 | — |
| 3 | high | - | [CARL: Constraint-Aware Reinforcement Learning for Planning with ...](http://arxiv.org/abs/2607.04854v1) | policy optimization | 通过对比约束与无约束输入输出分布设计奖励的强化学习，可显著提升大模型规划的约束符合度，效果优... | 通过对比约束与无约束输入下的模型输出分布，设计约束感知奖励，用强化学习提升大模型... | 仅在小型合成规划基准验证，未测试大规模真实场景下的性能，工业落地... | — |
| 4 | high | - | [CompactionRL: Reinforcement Learning with Context Compaction for...](http://arxiv.org/abs/2607.05378v1) | policy optimization | 加入CompactionRL后，GLM-4.5-Air在SWE-bench Verified... | 通过引入上下文压缩，结合token级损失归一化与交叉轨迹广义优势估计，联合优化任... | 仅在智能体编码任务验证，未覆盖其他长视野场景，增加了模型训练流程... | — |
| 5 | high | - | [Compete Then Collaborate: Frontier AI Teachers Build a Verifiabl...](http://arxiv.org/abs/2607.08255v1) | online distillation | 已有能力的7B/32B编码学生做SFT模仿会性能下降，RLVR可让竞赛问题通过率获得49%的... | 通过执行验证公平排序多教师，构建可验证课程，基于可验证奖励的强化学习优化学生模型... | 依赖多个前沿闭源大模型作为教师，对硬件要求高，整体训练成本较高 | — |
| 6 | high | - | [CurateEvo: Data-Curation Evolving for Agentic Post-Training](http://arxiv.org/abs/2607.06140v1) | policy optimization | CurateEvo在标注和野数据设置下，平均得分相较现有方法分别提升3.2和2.7点，兼容多... | 基于留存开发集的失败轨迹迭代优化数据整理策略，动态生成适配后训练的数据，改进智能... | 依赖留存开发集的失败轨迹，若失败轨迹覆盖不足，可能影响整理策略的... | — |
| 7 | high | - | [Distill Where the Student Goes: Teacher-Regularized RL for Engli...](http://arxiv.org/abs/2607.02966v1) | online distillation | 教师正则锚点可避免纯奖励RL最多27个百分点的语言一致性崩塌，小尺寸学生有时性能超过70B教... | 通过教师正则化在线策略蒸馏，以强教师提供前缀级正则锚点约束学生，结合多分量奖励优... | 需要额外保留大尺寸强教师模型提供正则信号，仅适配特定场景，整体落... | — |
| 8 | high | - | [Do You Need a Frontier Model as a Citation Verifier? Benchmarkin...](http://arxiv.org/abs/2607.08700v1) | factuality benchmark | GPT-5-mini取得最高来源相关性F1 0.908，同等F1下不同评判的通过率漂移、错判... | 通过基准测试量化不同LLM评判的偏差，明确奖励信号使用前需校准，保障奖励信号可靠... | 未校准的LLM奖励评判存在方向偏差，会误导强化学习训练，降低任务... | — |
| 9 | high | - | [Entropy Pacing Policy Optimization for Multi-Task Agentic Reinfo...](http://arxiv.org/abs/2607.07178v1) | policy optimization | 多任务智能体强化学习中不同任务会产生熵交叉与频繁熵尖峰，简单任务与难任务探索节奏不匹配相互干... | 通过任务熵感知的动态剪裁机制，自适应调整不同任务的策略更新约束，协调任务间熵水平... | 仅在通用多任务基准验证，未在具体真实场景测试，方法泛化性未得到充... | — |
| 10 | high | - | [Geometric Self-Distillation for Reasoning Generalization](http://arxiv.org/abs/2607.06855v1) | online distillation | 标准自蒸馏匹配会在高熵状态抽走备选答案概率，得到错误答案的置信一致，GeoSD让OOD准确率... | 通过自蒸馏过程中的几何距离约束抑制预测漂移，优化模型预测行为，提升模型分布外推理... | 仅在数学推理任务验证，未覆盖更多通用场景与agent任务，方法泛... | — |
| 11 | high | - | [Information Gain-based Rollout Policy Optimization: An Adaptive ...](http://arxiv.org/abs/2607.06223v1) | policy optimization | 按节点信息性分配推演预算、利用诱导教师分布引导优化，相同预算下性能稳定优于现有强基线方法。 | 通过基于信息增益的自适应推演预算分配，结合诱导教师分布引导策略优化，提升LLM智... | 仅在搜索问答任务验证，未披露具体性能提升幅度，方法通用性有待进一... | — |
| 12 | high | - | [LLM-as-a-Tutor: Policy-Aware Prompt Adaptation for Non-Verifiabl...](http://arxiv.org/abs/2607.04412v1) | reward learning | 提示难度自适应是不可验证强化学习中策略感知的缺失维度，本文方法在基准上稳定优于各类现有方法 | 通过让单个LLM兼具检测非挑战性提示、追加原子约束调整提示难度的功能，生成自校准... | 依赖LLM自身能力完成检测与生成，对LLM能力要求高，训练推理的... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **policy optimization**：19 篇
- **reward learning**：8 篇
- **online distillation**：6 篇
- **model steering**：2 篇
- **other**：1 篇
- **tool-use control**：1 篇
- **multi-agent coordination**：1 篇
- **unlearning/safety**：1 篇
- **知识蒸馏**：1 篇
- **factuality benchmark**：1 篇
- **evaluation/benchmark**：1 篇

## 失败模式与风险信号

- 轨迹忽视：智能体在训练中间步骤丢失任务目标与交互历史
- 大语言模型规划生成违反任务约束
- 全在线同策略蒸馏训练成本高，多轮蒸馏存在前缀陷阱引发的双边分布偏移
- 离策略训练下梯度估计方差爆炸，模型鲁棒性差
- 奖励稀疏导致收敛慢，过程替代奖励与真实结果奖励不对齐偏置训练方向
- 动态更新LLM生成的奖励权重违反平稳性假设，污染经验回放缓冲，导致训练性能下降
- 原有研究未解释隐通道位置与容量，标准对数比率度量存在虚假频率偏差伪影。
- 原有同策略自蒸馏依赖推理不可得的外部特权信息，仅能蒸馏得到弱性能策略
- 提示难度与策略能力错位，奖励信号缺乏区分度
- 二元编译奖励设计不合理，GRPO策略优化未能获得优于SFT的效果

## 评测信号

- 在不同参数规模的开放GLM模型上，CompactionRL均可带来Pass@1指标3.1到7.0个百分点的绝对性能提升。
- 模型在多项音频任务取得SOTA性能，同时原纯文本基座的推理、对齐与智能体等核心能力几乎无退化。
- 评测智能体任务整体性能，验证对轨迹忽视问题的缓解效果，STAPO在三个基准上达到当前最优性能。
- CARL在三个基准上显著优于标准强化微调和现有SOTA推理模型，大幅提升了大模型规划的约束关注度。
- ReOPD可保持或提升原OPD的准确率，训练过程零工具调用，单步训练速度至少比原方法快4倍。
- 在不同结构大模型的数学与智能体基准上，SIS可稳定提升各项任务性能，大幅增强离策略数据下的模型鲁棒性。
- 验证RSPO在GRPO、PPO、GiGPO等多种RL算法、两个基准上均可获得一致的性能提升
- 不同能力基线的场景中，稳定化LLM奖励塑形都能获得更优或相当的成功率，朴素动态更新会大幅劣化性能。
- 通过五组控制实验验证机制，线性CKA与学生精度相关系数达0.98，发现标准对数比率度量存在循环伪影偏差。
- 在域内数学推理和域外代码生成两项任务上，dOPSD性能均优于监督基线和原有同策略基线

## 控制机制 / Harness 信号

- 通过引入上下文压缩，结合token级损失归一化与交叉轨迹广义优势估计，联合优化任务执行与摘要生成，提升长视野任务性能。
- 通过多阶段监督训练、纯文本级联强化学习与多域在线策略蒸馏，使模型获得音频能力同时保留原文本核心能力。
- 通过归一化熵定位轨迹忽视相关异常步骤，采用轨迹感知奖励加独立惩罚的联合机制优化智能体策略。
- 通过对比约束与无约束输入下的模型输出分布，设计约束感知奖励，用强化学习提升大模型内在约束感知能力。
- 通过基于预收集教师轨迹的重放前缀蒸馏，引入可靠性感知前缀采样，提升蒸馏效率与效果。
- 通过改进离策略训练的重要性采样方法，降低梯度估计方差，以即插即用方式提升大语言模型RL对齐的性能与鲁棒性。
- 设计奖励交换机制，利用密集过程奖励的丰富信号，保证优化目标与真实结果奖励一致，提升智能体性能上限
- 通过分阶段冻结和指数移动平均平滑约束奖励权重漂移，保证奖励信号平稳性，稳定多智能体训练。
- 本文从几何视角分析隐通道蒸馏中知识迁移的内在机制，揭示表示对齐对隐通道信息传输的门控作用。
- 通过同策略自蒸馏，利用模型自身去噪轨迹生成监督信号，改进扩散语言模型后训练的推理生成性能

## 可靠性 / 落地风险

- 仅在智能体编码任务验证，未覆盖其他长视野场景，增加了模型训练流程的复杂度。
- 模型参数量大，训练依赖超大规模异构数据，训练推理成本高，工业落地门槛较高。
- 仅在三个基准任务验证，未在更长周期的复杂大规模任务验证落地有效性。
- 仅在小型合成规划基准验证，未测试大规模真实场景下的性能，工业落地存在一定不确定性。
- 依赖预收集的教师轨迹，教师轨迹的质量与可靠性直接影响学生智能体的最终效果。
- 仅在公开基准任务验证，未在真实复杂工业场景测试，实际落地的泛化性有待验证。
- 仅在两个基准上验证，未覆盖大规模真实任务，方法通用性有待进一步验证
- 需要根据基线能力划分区间，不同场景需要适配策略，增加了实际应用的调优成本。
- 结论基于小型MLP与MNIST实验，推广到大规模大语言模型的有效性仍待验证。
- 仅在两个基准上验证，未测试更大规模复杂任务，评测覆盖范围较为有限

## 代码资源

- [When Implausible Tokens Get Reinforced: Tail-Aware Credit Calibration for LLM Re...](https://github.com/xiuyilou/TACO.)

## 常见基线方法

- **GRPO**：5 篇
- **监督微调（SFT）**：3 篇
- **DAPO**：2 篇
- **原始未压缩上下文训练模型**：1 篇
- **标准强化微调(RFT)**：1 篇
- **现有最优推理模型**：1 篇
- **在线同策略蒸馏(OPD)**：1 篇
- **标准重要性采样**：1 篇
- **PPO**：1 篇
- **GiGPO**：1 篇

## 常用数据集

- **ALFWorld**：3 篇
- **WebShop**：3 篇
- **摘要未提及**：3 篇
- **数学推理基准**：2 篇
- **SWE-bench Verified**：1 篇
- **Terminal-Bench 2.0**：1 篇
- **自建大规模音频文本对齐数据集**：1 篇
- **搜索增强问答基准**：1 篇
- **BlocksWorld**：1 篇
- **TravelPlanner**：1 篇

---
*自动生成于 2026-07-12 | ArXiv_Daily_Digest*