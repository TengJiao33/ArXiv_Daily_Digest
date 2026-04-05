# 🧪 ArXiv AI 日报

📅 **2026-04-05 周日** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **55,868** (¥0.0185)

## 🔥 今日必读

---

### 1. Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.02288v1)

👤 Gengsheng Li, Tianyu Yang, Junfeng Fang 等


**中文标题**: 基于样本路由统一组相对策略优化与自蒸馏策略优化

**背景与痛点**: 大语言模型基于可验证奖励的强化学习后训练是当前提升推理能力的主流范式，现有两类主流方法各有缺陷：GRPO采用统一序列级信用分配，无法定位错误样本的局部推理错误，样本效率低；SDPO提供稠密token级监督，早期收敛快，但长期训练存在优化歧义，教师信号质量持续下降，易发生性能崩溃。

**核心创新**: 发现GRPO的奖励对齐强化和SDPO的稠密纠错监督具有天然互补性，提出统一框架SRPO，将正确样本路由给GRPO做稳定的奖励对齐优化，错误样本路由给SDPO做稠密logit级纠错，额外设计熵感知动态加权过滤不可靠自蒸馏信号，无需手动调整混合比例。

**技术细节**: 对每个输入prompt，当前策略采样多组输出轨迹后做正确性检查，仅将存在有效教师信息（同组正确兄弟输出）的错误轨迹路由到SDPO分支，其余所有轨迹走GRPO分支。SDPO分支按自教师token输出分布的熵计算动态权重，熵越高权重越低，总损失按分支token数归一化，自动适配训练进程。

**实验结果**: 在五个科学推理与工具调用基准、两个Qwen3模型尺寸上测试，Qwen3-8B五基准平均准确率较GRPO提升3.4个百分点，较SDPO提升6.3个百分点，长期训练每步计算开销最高降17.2%，同时兼顾早期训练效率与长期优化稳定性。

---

### 2. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.02322v1)

👤 Bangji Yang, Hongbo Ma, Jiajun Fan 等


**中文标题**: 批处理上下文强化学习：面向高效推理的任务缩放定律

**背景与痛点**: 大语言模型的思维链推理性能优异，但普遍存在推理过程冗余、token消耗过大的问题，大幅推高推理成本。现有效率优化方法要么添加显式长度惩罚导致准确率下降，要么依赖复杂多阶段 pipeline、辅助模型，易出现优化不稳定，无法平衡准确率与效率。

**核心创新**: 提出极简单阶段训练范式BCR，仅通过将多个问题打包进同一个上下文窗口共享token预算，靠问题间的资源竞争诱导模型自主压缩冗余推理，不需要任何显式长度监督；还发现了新的推理效率缩放维度，验证了准确率不降反升的“免费午餐”现象。

**技术细节**: 训练时按问题难度分层抽样，将N个问题打包为一个训练组，拼接成单个prompt让模型在同一个上下文窗口内顺序求解所有问题，采用GRPO算法优化策略。奖励仅包含单问题准确率、输出格式合规性两项，无任何长度惩罚。对整组输出设置固定全局token预算，冗余推理会挤压后续问题空间拉低总奖励，因此模型会自主学习压缩冗余、分配推理深度。

**实验结果**: 在AIME25、AMC23等5个主流数学推理基准测试1.5B、4B两类模型，标准单问题推理下token用量减少15.8%~62.6%，且准确率普遍保持或提升，4B模型在AIME25准确率提升13.3%；并发推理时随N增大，准确率下降远平缓于基线，可作为可控的吞吐量-准确率调节旋钮。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance...](http://arxiv.org/abs/2604.02280v1) `cs.AI (人工智能)` | 长周期自主AI Agent存在记忆无控制累积，引发错误传播与性能衰减的核心痛点，本文研究新型记忆遗忘技术，平衡相关性与效率，推动Agent实用化。 |
| 5 | [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calli...](http://arxiv.org/abs/2604.02155v1) `cs.CL (计算语言学)` | 现有语言智能体普遍认为更长的思维链推理效果更好，本文发现推理长度与准确率呈非单调关系，证明短推理更优，对Agent设计有重要启发。 |
| 6 | [Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying ...](http://arxiv.org/abs/2604.02289v1) `cs.CV (计算机视觉)` | 原生3D基础模型训练受限于标注3D数据不足，本文提出在有限3D数据下统一文本到2D与3D生成，探索低数据量原生3D大模型，方向前沿。 |
| 7 | [Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Langu...](http://arxiv.org/abs/2604.02194v1) `cs.CL (计算语言学)` | 检索增强大模型遇到无关检索内容时性能下降明显，本文提出神经元引导的指令微调方法，提升RAG模型的鲁棒性，对RAG落地实用性强。 |
| 8 | [The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expe...](http://arxiv.org/abs/2604.02178v1) 💻 `cs.CL (计算语言学)` | 混合专家MoE是当前大模型缩放的主流架构，但缺乏专家层级的可解释性研究，本文从专家层解析MoE，对后续架构优化有较高研究价值。 |
| 9 | [Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs](http://arxiv.org/abs/2604.02230v1) `cs.AI (人工智能)` | 大模型可靠部署需要有效识别超出能力范围的问题并拒答，本文提出推理轨迹反转的拒答方案，提升大模型拒答性能，助力大模型安全落地。 |
| 10 | [SKILL0: In-Context Agentic Reinforcement Learning for Skill Internalization](http://arxiv.org/abs/2604.02268v1) 💻 `cs.LG (机器学习)` | 当前LLM智能体依赖推理时动态加载技能，运行效率较低，本文提出上下文智能体强化学习方法，实现技能内化，提升Agent推理效率。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-05
