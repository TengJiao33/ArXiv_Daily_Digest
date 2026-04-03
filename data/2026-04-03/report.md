# 🧪 ArXiv AI 日报

📅 **2026-04-03 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **54,952** (¥0.0180)

## 🔥 今日必读

---

### 1. Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.02288v1)

👤 Gengsheng Li, Tianyu Yang, Junfeng Fang 等


**中文标题**: 基于样本路由统一分组相对与自蒸馏策略优化

**背景与痛点**: 该研究针对大语言模型后训练阶段的可验证奖励强化学习任务。主流方法GRPO信用分配粗糙，对错误整序列统一惩罚，难以定位局部推理错误，样本效率偏低；SDPO提供稠密对数级监督，早期收敛快，但训练后期易性能崩溃，存在优化歧义与信号退化两大固有缺陷。

**核心创新**: 发现GRPO与SDPO具备互补的优化特性，提出样本路由策略优化SRPO，按样本学习状态分配适配的监督信号：正确样本用GRPO做奖励对齐强化，错误样本用SDPO做稠密对数修正，新增熵感知动态权重抑制不可靠蒸馏信号，同时兼顾训练效率与长期稳定性。

**技术细节**: 算法流程为：对输入prompt采样多个在线生成轨迹，先做正确性检查与教师可用性判断，仅将拥有正确教师信息的错误轨迹路由到SDPO分支，其余全部走GRPO分支。SDPO分支按自教师每个token预测的熵计算权重，熵越高权重越低，抑制不确定噪声。总损失按两个分支的有效token数归一化，无需额外混合超参数，自动适配训练过程的样本分布变化。

**实验结果**: 在5个科学推理与工具调用基准、Qwen3两种规模模型上测试，SRPO在Qwen3-8B上五基准平均准确率较GRPO提升3.4%，较SDPO提升6.3%，长期训练每步计算成本最多降低17.2%，兼具早期训练效率与长期稳定性，还能保持适中的响应长度。

---

### 2. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.02322v1)

👤 Bangji Yang, Hongbo Ma, Jiajun Fan 等


**中文标题**: 批处理上下文强化学习：面向高效推理的任务缩放定律

**背景与痛点**: 当前大语言模型的思维链推理性能优异，但存在推理token消耗过多、推理成本过高的问题。现有效率优化方法，如显式长度惩罚、辅助难度估计器、多阶段课程学习，要么会降低推理准确率，要么训练流程复杂，超参调优难度高，还容易出现优化崩溃问题。

**核心创新**: 提出极简单阶段训练范式BCR，仅修改训练输入结构，让模型在共享上下文窗口内同时解决多个问题，靠隐式token预算约束激活模型潜在的高效推理能力，不需要任何显式长度监督，还首次发现推理效率的任务缩放定律，打破了准确率与效率的固有取舍，出现了“免费午餐”现象。

**技术细节**: 训练阶段将数据按难度分层采样，打包为含N个问题的组，拼接成单个prompt输入模型，要求模型顺序输出所有问题的解答。采用GRPO做策略优化，奖励仅由单题准确率和格式合规性组成，无任何长度相关奖励；通过固定全局token预算制造隐式资源约束，让多个问题竞争共享资源，倒逼模型自动压缩冗余推理，从根源避免了显式长度惩罚的对抗梯度问题。

**实验结果**: 在五个主流数学推理基准、1.5B/4B两类模型上测试，标准单题推理下，BCR可降低15.8%-62.6%的单题token消耗，同时普遍保持或提升准确率，4B模型在AIME25上准确率提升13.3%；推理时增大N可单调降低token使用，准确率下降远平缓于基线，可作为部署时吞吐量-准确率的可控调节旋钮。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance...](http://arxiv.org/abs/2604.02280v1) `cs.AI (人工智能)` | 长周期自主AI Agent存在记忆无控制堆积、错误记忆传播的痛点，该研究提出新型记忆遗忘技术，平衡记忆相关性与推理效率，属于Agent方向前沿研究 |
| 5 | [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calli...](http://arxiv.org/abs/2604.02155v1) `cs.CL (计算语言学)` | 现有语言Agent普遍默认CoT越长效果越好，该研究实证发现功能调用Agent中CoT预算存在非单调效应，指出简洁推理更优，对Agent设计有重要指导意义 |
| 6 | [Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Langu...](http://arxiv.org/abs/2604.02194v1) `cs.CL (计算语言学)` | 检索增强大模型面对无关检索文本时容易发生性能退化，该工作提出神经元引导的指令调优方法，有效提升了RAG系统的鲁棒性，实用性很强 |
| 7 | [Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying ...](http://arxiv.org/abs/2604.02289v1) `cs.CV (计算机视觉)` | 3D原生基础模型训练受限于高质量标注3D数据不足的问题，该工作实现了用有限3D数据统一文生2D与3D生成，推进了多模态3D生成落地 |
| 8 | [The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expe...](http://arxiv.org/abs/2604.02178v1) `cs.CL (计算语言学)` | MoE是当前大模型缩放的主流架构，但长期缺乏专家层级的可解释性分析，该工作实现了MoE专家级可解释分析，对MoE架构优化有重要价值 |
| 9 | [De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory R...](http://arxiv.org/abs/2604.02276v1) `cs.AI (人工智能)` | 将冗长层级化的法规文本转化为机器可读规则的成本极高，该工作提出LLM迭代自精炼方案，实现规则结构化提取，垂直领域落地价值高 |
| 10 | [Taming the Exponential: A Fast Softmax Surrogate for Integer-Native Edge Inferen...](http://arxiv.org/abs/2604.02292v1) `cs.LG (机器学习)` | Softmax计算是Transformer在整数原生边缘推理中的核心计算瓶颈，该工作提出快速Softmax替代方案，降低端侧推理延迟，适配边缘部署需求 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-03
