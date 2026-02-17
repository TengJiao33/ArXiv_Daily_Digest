# 🧪 ArXiv AI 日报

📅 **2026-02-17 周二** | 🤖 扫描/精选: **50/13**

> 📊 Tokens: **86,282** (¥0.0281)

## 🔥 今日必读

---

### 1. Goldilocks RL: Tuning Task Difficulty to Escape Sparse Rewards for Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.14868v1)

👤 Ilia Mahrooghi, Aryo Lotfi, Emmanuel Abbe


**中文标题**: 《金发姑娘强化学习：调整任务难度破解推理任务的稀疏奖励问题》

**背景与痛点**: 大语言模型推理任务的RL微调依赖稀疏二元最终奖励，样本效率极低，大量计算浪费在无梯度的过简单或过难样本上。现有课程学习方法要么需要模型重复观测样本估计难度，要么依赖预定义的难度分类，无法适配大规模无标注流式推理数据，泛化性差。

**核心创新**: 本文从理论上推导证明GRPO的梯度范数正比于√(p_q(1-p_q))，当问题对当前学生的正确率p_q接近0.5时学习信号最强。据此提出动态课程采样框架Goldilocks，基于当前学生能力实时预测未见过样本的学习效用，始终挑选难度适中的高信号样本，避免无效计算浪费。

**技术细节**: 学生为待微调的目标推理大语言模型，采用GRPO做强化学习优化；教师为基于预训练LM的效用预测器，对输入问题做句嵌入均值池化，经线性投影加缩放sigmoid输出预测的样本学习效用。训练时每次随机采样K个候选问题，以ε-greedy策略选高效用样本给学生，学生生成多rollout后计算实际目标y_q=√(p_q(1-p_q))存入滑动回放缓冲，定期用MSE损失异步更新教师，全程控制相同总计算预算做对比。

**实验结果**: 在包含3M样本的OpenMathReasoning数学推理数据集测试，1B到4B规模的多款主流模型均获得一致提升：Olmo2-1B Pass@1准确率从11.7%提升到14.9%，Phi-4 4B从37.1%提升到41.0%，相同计算预算下稳定优于纯GRPO基线，且对DAPO、带熵正则GRPO等不同RL损失都有正交增益。

---

### 2. BFS-PO: Best-First Search for Large Reasoning Models

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2602.14917v1)

👤 Fiorenzo Parascandolo, Wenhui Tan, Enver Sangineto 等


**中文标题**: BFS-PO：面向大推理模型的最佳优先搜索

**背景与痛点**: 当前o1、DeepSeek-R1这类大推理模型依赖长推理链获得高性能，普遍存在“过度思考”问题，冗余步骤多、计算存储开销大，且GRPO/DAPO等主流强化学习方法会进一步加剧该问题；现有推理链压缩方法大多以牺牲推理准确率为代价缩短长度，无法兼顾精度和推理效率。

**核心创新**: 提出基于最佳优先搜索策略的强化学习算法BFS-PO，摒弃了依赖人工标注短推理链做监督微调的传统范式，也不需要额外训练过程奖励模型（PRM）引导搜索，通过模型自探索逐步得到更短的正确推理链，打破了“缩长度必降精度”的固有矛盾。

**技术细节**: 训练阶段对每个问题先初始化生成G个输出，每次迭代选当前最短的正确推理路径，选取路径中未分支过的熵最高token作为回溯分支点（已有研究证明高熵token对应模型关键决策点），从该点条件采样G个新路径加入搜索树，重复K次；将GRPO的全局优势估计扩展为分支优势，在每个回溯节点的子树内计算token级优势，共享路径可复用KV缓存，相比DAPO实现1.37倍训练加速。

**实验结果**: 在GSM8K、MATH-500、AIME等多个推理基准、3B~8B不同规模基模型上测试，BFS-PO全面领先现有SOTA方法，在域内、域外场景都同时提升准确率、缩短推理长度，Llama-3.1-8B在域外AIME数据集上准确率超出DAPO超过4个百分点，兼顾精度效率的AES指标始终排名第一。

---

### 3. On the Learning Dynamics of RLVR at the Edge of Competence

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.14872v1)

👤 Yu Huang, Zixin Wen, Yuejie Chi 等


**中文标题**: 能力边缘的带可验证奖励强化学习（RLVR）学习动力学研究

**背景与痛点**: 当前大语言模型复杂推理的核心进展依赖带可验证奖励的强化学习（RLVR），该范式仅依赖终点的结果稀疏反馈就能驱动长推理学习，但一直缺乏对其训练机制的严谨理论解释，现有结论仅经验性指出RLVR仅在模型“能力边缘”有效，未说明背后的动力学本质。

**核心创新**: 本文针对Transformer的组合推理RL训练建立了完整的学习动力学理论，首次明确RLVR的效果由训练数据的难度谱平滑性决定，从优化层面解释了RLVR仅在能力边缘生效的核心原因，预言了两种典型训练动态，为RLVR数据设计提供了可落地的理论指导。

**技术细节**: 本文采用极简Transformer设置：固定预训练好的MLP（已掌握单步原子推理能力），仅优化注意力层参数，用REINFORCE算法优化仅终点二元奖励的RL目标。技术上创新性引入有限群傅里叶分析，将L步组合推理的终点成功条件转化为傅里叶域的卷积乘积，得到梯度大小的闭式刻画：梯度与单步正确概率的L次方成正比。难度跳度过大时高难度任务梯度会被指数抑制，训练陷入长平台；平滑难度下简单任务的梯度持续提升能力，让高难度任务提前获得可用梯度，实现接力进步。

**实验结果**: 本文在合成组合推理任务上验证理论结论，固定长度训练验证了短范围可高效学习、长范围初始梯度指数平坦的结论；混合难度训练验证了：中等难度比（R=3）可实现平滑接力学习，大难度比（R=7）会产生grokking式长停滞平台，所有实验结果完全匹配理论预言。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Scaling Beyond Masked Diffusion Language Models](http://arxiv.org/abs/2602.15014v1) `cs.LG (机器学习)` | 当前离散扩散语言模型中掩码扩散路线占据主导，本文探索拓展掩码扩散之外的扩散语言模型路线，为替代自回归生成提供了新的方向。 |
| 5 | [Boundary Point Jailbreaking of Black-Box LLMs](http://arxiv.org/abs/2602.15001v1) `cs.LG (机器学习)` | 针对前沿黑盒大模型的安全防护，提出边界点越狱攻击方法，揭示了现有LLM安全防护的新漏洞，对LLM安全攻防研究有很高参考价值。 |
| 6 | [ReusStdFlow: A Standardized Reusability Framework for Dynamic Workflow Construct...](http://arxiv.org/abs/2602.14922v1) `cs.AI (人工智能)` | 针对当前企业级Agent AI存在的可复用性困境与结构幻觉痛点，提出标准化可复用框架ReusStdFlow，有效解决Agent工业落地的核心问题。 |
| 7 | [Hunt Globally: Deep Research AI Agents for Drug Asset Scouting in Investing, Bus...](http://arxiv.org/abs/2602.15019v1) `cs.AI (人工智能)` | 针对当前全球生物医药创新中多数新药资产来自非英语区域难以发掘的痛点，提出深度研究AI Agent实现药物资产搜寻，产业价值极大。 |
| 8 | [PhyScensis: Physics-Augmented LLM Agents for Complex Physical Scene Arrangement](http://arxiv.org/abs/2602.14968v1) `cs.RO (机器人)` | 针对复杂物理场景排列任务中现有LLM Agent忽略物理一致性约束的痛点，提出物理增强的LLM Agent框架，助力机器人仿真数据规模化生成。 |
| 9 | [Use What You Know: Causal Foundation Models with Partial Graphs](http://arxiv.org/abs/2602.14972v1) `cs.LG (机器学习)` | 针对传统因果估计依赖定制化估计器、缺乏统一方案的痛点，提出支持部分已知因果图的因果基础模型，推动因果大模型实用化发展。 |
| 10 | [Variance-Reduced $(\varepsilon,δ)-$Unlearning using Forget Set Gradients](http://arxiv.org/abs/2602.14938v1) `cs.LG (机器学习)` | 针对机器遗忘任务中现有方法难以满足严格隐私保证要求的问题，提出方差缩减的(ε,δ)遗忘方法，提供了更可靠的遗忘效果保证。 |
| 11 | [ThermEval: A Structured Benchmark for Evaluation of Vision-Language Models on Th...](http://arxiv.org/abs/2602.14989v1) `cs.CV (计算机视觉)` | 针对现有视觉语言模型难以泛化到热成像场景、缺乏标准化评估基准的痛点，提出ThermEval基准，推动多模态模型在特殊传感场景落地。 |
| 12 | [PDE foundation models are skillful AI weather emulators for the Martian atmosphe...](http://arxiv.org/abs/2602.15004v1) `cs.LG (机器学习)` | 验证了预训练PDE基础模型可通过微调得到高性能火星大气天气预报模拟器，是科学大模型落地跨领域科学预测的优秀示范。 |
| 13 | [BPP: Long-Context Robot Imitation Learning by Focusing on Key History Frames](http://arxiv.org/abs/2602.15010v1) `cs.RO (机器人)` | 针对长上下文机器人模仿学习需要处理大量历史帧、效率低下的痛点，提出BPP方法聚焦关键历史帧，有效提升长上下文机器人任务性能。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-17
