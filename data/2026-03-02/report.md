# 🧪 ArXiv AI 日报

📅 **2026-03-02 周一** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **51,349** (¥0.0169)

## 🔥 今日必读

---

### 1. CUDA Agent: Large-Scale Agentic RL for High-Performance CUDA Kernel Generation

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.24286v1)

👤 Weinan Dai, Hanlin Wu, Qiying Yu 等


**中文标题**: CUDA Agent：面向高性能CUDA核生成的大规模智能体强化学习

**背景与痛点**: 自动生成高性能CUDA核是深度学习基础设施的核心需求，但该任务高度依赖硬件专家经验。现有LLM生成方法要么依赖测试时无训练优化，性能被基础模型本身能力上限限制，要么采用固定多轮循环微调，无法从根本提升模型内在CUDA优化能力，性能始终不及torch.compile这类编译器工具。

**核心创新**: 提出一套面向CUDA核生成的大规模智能体强化学习系统，从训练数据、智能体环境、强化学习算法三个维度系统性改进，通过执行反馈驱动的RL训练，让基础模型真正习得CUDA优化能力，打破现有方法的性能上限，首次让LLM生成的CUDA核显著领先传统编译器和顶级通用大模型。

**技术细节**: 首先设计可扩展数据合成 pipeline，从PyTorch、Transformers爬取基础算子，用LLM组合生成多算子融合任务，经过执行过滤得到6000个去污染的训练样本；其次构建技能增强开发环境，规范化CUDA开发流程，通过权限隔离防止奖励黑客，设计基于正确性和速度里程碑的离散奖励，避免原始速度奖励的偏差；最后提出多阶段RL预热策略，先做单轮RL，再用高质量轨迹拒绝微调初始化actor、价值预训练初始化critic，解决训练不稳定问题，支持150步稳定训练、最长200轮交互。

**实验结果**: 在标准基准KernelBench的250个任务上测试，相比torch.compile，在Level 1/2/3三个难度集上的快占比分别达到100%、100%、92%，整体几何平均加速2.11倍，最难的Level 3集比Claude Opus 4.5、Gemini 3 Pro领先约40%，证明LLM方法优于传统编译器启发式优化。

---

### 2. Taming Momentum: Rethinking Optimizer States Through Low-Rank Approximation

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.24283v1) | 💻 [GitHub](https://github.com/mrflogs/LoRA-Pre.) ⭐6

👤 Zhengbo Wang, Jian Liang, Ran He 等


**中文标题**: 驯服动量：基于低秩近似重新设计优化器状态

**背景与痛点**: 大语言模型训练所用的Adam等动量优化器，需要存储完整的一阶、二阶动量状态，带来三倍于模型参数的内存开销，严重限制大模型训练的可扩展性。现有低秩优化方法多依赖周期性子空间更新，会产生误差累积，适配性差，预训练性能损失明显。

**核心创新**: 本文从数学上证明了优化器中常用的指数移动平均动量更新，本质等价于在线线性回归器的梯度流训练，提出了压缩动量而非压缩参数/梯度的新思路，直接对动量本身做低秩分解，每步动态更新梯度子空间，从根源解决了现有方法周期性更新带来的误差累积问题。

**技术细节**: LoRA-Pre将完整动量矩阵分解为两个低秩小矩阵的乘积，把原动量优化目标转化为低秩因子的最小二乘问题，通过牛顿法推导得到闭形式更新规则，天然匹配标准指数移动平均的衰减特性。针对二阶动量的正性要求，设计了逐元素平方的重参数化方案，满足开平方计算需求，可适配Adam、Muon任意动量优化器，内存复杂度大幅降低。

**实验结果**: 在C4数据集预训练60M到1B规模的Llama模型，LoRA-Pre仅用基准方法1/8的秩就能达到相当性能，所有规模性能都优于现有低秩方法；下游微调数学任务中，相比标准LoRA，在Llama-3.1-8B和Llama-2-7B上平均准确率分别提升3.14和6.17个点，兼顾预训练和微调的效率与性能。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Mode Seeking meets Mean Seeking for Fast Long Video Generation](http://arxiv.org/abs/2602.24289v1) `cs.CV (计算机视觉)` | 针对长视频生成领域高质量长数据稀缺的核心瓶颈，将模态搜索与均值搜索结合，实现快速长视频生成，推动长视频生成技术向前发展。 |
| 5 | [Controllable Reasoning Models Are Private Thinkers](http://arxiv.org/abs/2602.24210v1) 💻 `cs.CL (计算语言学)` | 解决推理型AI智能体推理痕迹难管控导致敏感用户数据泄露的痛点，提出可控推理框架让模型实现私有思考，兼顾推理能力和隐私安全。 |
| 6 | [DARE-bench: Evaluating Modeling and Instruction Fidelity of LLMs in Data Science](http://arxiv.org/abs/2602.24288v1) `cs.AI (人工智能)` | 针对现有LLM数据科学任务基准缺乏对建模能力和指令保真度准确评估的缺陷，提出DARE-bench基准，填补领域评测空白，推动技术发展。 |
| 7 | [AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generat...](http://arxiv.org/abs/2602.24134v1) `cs.CV (计算机视觉)` | 针对多模态RAG处理复杂视觉文档效率低下的痛点，提出按需解析的AgenticOCR方案，只提取RAG需要的内容，显著提升多模态RAG运行效率。 |
| 8 | [LemmaBench: A Live, Research-Level Benchmark to Evaluate LLM Capabilities in Mat...](http://arxiv.org/abs/2602.24173v1) `cs.AI (人工智能)` | 现有LLM数学能力评测多为静态的竞赛/教材题目，推出动态更新的研究级数学评测基准LemmaBench，更准确衡量LLM前沿数学研究能力。 |
| 9 | [Toward Guarantees for Clinical Reasoning in Vision Language Models via Formal Ve...](http://arxiv.org/abs/2602.24111v1) `cs.CV (计算机视觉)` | 针对医疗视觉语言模型常出现逻辑不一致、诊断结论不可靠的问题，提出通过形式验证为临床推理提供可靠性保证，推动医疗AI安全落地。 |
| 10 | [SafeGen-LLM: Enhancing Safety Generalization in Task Planning for Robotic System...](http://arxiv.org/abs/2602.24235v1) `cs.RO (机器人)` | 解决机器人安全关键任务规划中现有方法可扩展性差、安全泛化能力不足的问题，提升LLM驱动机器人规划的安全泛化性，助力机器人智能体落地。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-02
