# 🧪 ArXiv AI 日报

📅 **2026-04-04 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **55,169** (¥0.0181)

## 🔥 今日必读

---

### 1. Unifying Group-Relative and Self-Distillation Policy Optimization via Sample Routing

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.02288v1)

👤 Gengsheng Li, Tianyu Yang, Junfeng Fang 等


**中文标题**: 基于样本路由统一分组相对与自蒸馏策略优化

**背景与痛点**: 针对大语言模型可验证奖励强化学习后训练场景，现有主流方法各有缺陷：分组相对策略优化（GRPO）信用分配粒度粗，对失败样本全序列均匀惩罚，无法定位局部推理错误，样本效率低；自蒸馏策略优化（SDPO）提供稠密对数级监督，早期提升快，但长期训练会发生性能崩溃。

**核心创新**: 发现GRPO和SDPO具备互补优化特性，提出样本路由策略优化（SRPO）统一两种范式，按样本学习状态分配适配的监督信号，给SDPO分支新增熵感知动态权重机制，抑制不可靠的高熵蒸馏目标，既保留SDPO的早期快速提升，又获得GRPO的长期训练稳定性，无需额外外部教师或奖励模型。

**技术细节**: 算法流程为：对输入prompt采样多组在线rollout，先做正确性检查，仅把「推理错误且存在可用教师信息（同组正确兄弟样本）」的样本路由到SDPO分支，其余所有样本都走GRPO分支。SDPO分支按自教师每个token预测的熵计算权重，预测越不确定（熵越高）权重越低，总损失按两个分支的有效token数自动归一化，无需额外混合超参，训练后期自然向GRPO倾斜。

**实验结果**: 在五个基准（四个科学推理、一个工具调用）、两种Qwen3模型尺度上测试，Qwen3-8B五基准平均准确率比GRPO提升3.4%，比SDPO提升6.3%，长期训练每步计算成本最高降低17.2%，同时保持适中响应长度，验证了方法的有效性。

---

### 2. Batched Contextual Reinforcement: A Task-Scaling Law for Efficient Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.02322v1)

👤 Bangji Yang, Hongbo Ma, Jiajun Fan 等


**中文标题**: 批处理上下文强化学习：面向高效推理的任务缩放定律

**背景与痛点**: 针对大语言模型思维链推理token消耗过大、推理成本过高的痛点，现有效率优化方法要么会显著降低推理准确率，要么需要复杂的多阶段训练流程或额外辅助模块，显式长度惩罚还会产生对抗梯度，容易引发灾难性训练崩溃。

**核心创新**: 提出极简单阶段训练框架BCR，仅通过输入结构修改就解锁大模型潜在的高效推理能力：训练时让模型在同一个上下文窗口同时解决多个问题，仅靠隐式token预算和问题间资源竞争逼出压缩策略，无需任何显式长度监督，还发现了推理效率的新任务缩放定律。

**技术细节**: 将训练数据按难度分层抽样，打包为每组N个问题的批量，拼接为带结构标记的单个prompt，要求模型按格式依次输出所有问题的解答；采用GRPO优化策略，奖励仅包含单问题准确率和格式合规性，无任何长度相关惩罚；给整组回答设置固定全局token预算，将预算作为硬约束而非软惩罚，靠问题间资源竞争倒逼模型剪枝冗余推理，从根源避免了对抗梯度问题。

**实验结果**: 在AIME、AMC等五个主流数学推理基准、1.5B和4B两个模型系列上测试，标准单问题推理下BCR可降低15.8%~62.6%的token消耗，同时多个基准实现准确率提升，验证了「免费午餐」现象；推理时可通过调整并发数N灵活权衡吞吐量与准确率。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Novel Memory Forgetting Techniques for Autonomous AI Agents: Balancing Relevance...](http://arxiv.org/abs/2604.02280v1) `cs.AI (人工智能)` | 长周期自主AI代理存在记忆无控制积累，引发精度衰退、错误记忆传播的问题，本文提出新型记忆遗忘技术，平衡记忆相关性与运行效率，解决Agent长期运行核心痛点。 |
| 5 | [Neuro-RIT: Neuron-Guided Instruction Tuning for Robust Retrieval-Augmented Langu...](http://arxiv.org/abs/2604.02194v1) `cs.CL (计算语言学)` | 检索增强大语言模型容易受无关检索文档干扰出现性能下降，本文提出神经元引导的指令微调方法，提升RAG系统鲁棒性，改进RAG落地可靠性，实用性强。 |
| 6 | [Omni123: Exploring 3D Native Foundation Models with Limited 3D Data by Unifying ...](http://arxiv.org/abs/2604.02289v1) `cs.CV (计算机视觉)` | 现有3D原生基础模型依赖大量3D训练数据，门槛较高，本文提出用有限3D数据统一文本到2D与3D生成的原生3D基础模型，降低领域数据门槛，推动多模态3D发展。 |
| 7 | [Brief Is Better: Non-Monotonic Chain-of-Thought Budget Effects in Function-Calli...](http://arxiv.org/abs/2604.02155v1) `cs.CL (计算语言学)` | 当前语言Agent中普遍默认长CoT推理效果更好，本文实证发现函数调用Agent中存在非单调CoT预算效应，精简推理更优，对Agent设计有重要指导意义。 |
| 8 | [The Expert Strikes Back: Interpreting Mixture-of-Experts Language Models at Expe...](http://arxiv.org/abs/2604.02178v1) `cs.CL (计算语言学)` | 混合专家MoE是当前大模型缩放的主流架构，但缺乏专家层面的可解释性分析，本文从专家层级解释MoE语言模型，对MoE模型优化部署有重要参考价值。 |
| 9 | [Answering the Wrong Question: Reasoning Trace Inversion for Abstention in LLMs](http://arxiv.org/abs/2604.02230v1) `cs.AI (人工智能)` | 大语言模型可靠落地需要具备适时拒答的能力，本文提出推理轨迹反转方法提升LLM拒答性能，提升大模型部署可靠性，解决落地的安全痛点。 |
| 10 | [De Jure: Iterative LLM Self-Refinement for Structured Extraction of Regulatory R...](http://arxiv.org/abs/2604.02276v1) `cs.AI (人工智能)` | 从层级化密集监管文本提取结构化法律规则成本极高，本文提出迭代LLM自精炼方法De Jure，实现规则自动提取，降低领域工程成本，工业实用性强。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-04
