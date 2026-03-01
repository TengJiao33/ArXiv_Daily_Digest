# 🧪 ArXiv AI 日报

📅 **2026-03-01 周日** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **44,774** (¥0.0151)

## 🔥 今日必读

---

### 1. InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.23200v1)

👤 Sayed Mohammadreza Tayaranian Hosseini, Amir Ardakani, Warren J. Gross


**中文标题**: InnerQ：面向大语言模型KV缓存的硬件感知免调优量化方法

**背景与痛点**: 大语言模型解码阶段，KV缓存大小随生成长度线性增长，是内存占用和推理延迟的核心瓶颈。现有主流KV缓存量化方法普遍沿缓存矩阵外维度分组，和GPU解码阶段向量-矩阵乘法执行流不匹配，导致去量化访存开销大、延迟高，还存在精度损失问题。

**核心创新**: 核心将量化分组维度从现有方法的外维度改为内维度，让分组布局对齐GPU向量-矩阵乘法的计算流，实现尺度因子复用、减少访存，同时配套多项精度补偿技术，在不牺牲精度、无需调优校准的前提下降低解码延迟。

**技术细节**: 具体包含四项关键设计：①沿缓存矩阵内维度划分量化组，同一行内连续元素共享量化尺度与零点，去量化时尺度因子可在GPU计算单元间复用，大幅减少内存访问；②每个分组根据本地分布动态选择对称/非对称量化，额外计算利用内存界操作的空闲算力，不增加延迟；③同时保留最早注意力汇点和最新token两个高精度窗口，缓解异常值精度泄露；④Key缓存逐通道归一化在预填充阶段预计算并折叠到权重，无运行时开销。

**实验结果**: 在多个Llama模型的GSM8K少样本评测中，2位量化的InnerQ精度接近未量化KV基线，准确率优于KIVI等现有免调优方法；相比半精度乘法最高加速88%，相比外维度分组量化最高加速22%，缓存大小与现有方法相当。

---

### 2. FlashOptim: Optimizers for Memory Efficient Training

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.23349v1)

👤 Jose Javier Gonzalez Ortiz, Abhay Gupta, Chris Renard 等


**中文标题**: FlashOptim：内存高效训练的优化器

**背景与痛点**: 当前大模型训练中，AdamW每个参数需要存储主权重、梯度、动量、方差共16字节，训练70亿参数模型就需要百GB级显存，普通研究者单卡难以承受。现有方案要么依赖多卡分布、要么CPU卸载有额外开销，压缩精度方案通常会损失模型效果。

**核心创新**: 提出FlashOptim，一套针对优化器全链路的内存压缩方案，通过改进权重拆分、优化器状态量化两个核心技术，将AdamW单参数内存从16字节降到7字节，开启梯度释放可进一步降到5字节，压缩率超50%，且保持原优化器语义、模型精度无损失，可直接替换现有优化器使用。

**技术细节**: 第一，改进权重拆分：利用舍入后误差范围必然落在当前权重最小精度单位半区间的性质，仅用整数存储误差相对位置，16位下采样权重加8位整数误差，实现24位有效精度，相比原有拆分重构误差大幅降低。第二，优化器状态压缩：针对动量用软符号非线性重分布、针对Adam方差用平方根重分布，把重尾分布拉均匀，配合分组8位量化，每个优化器状态仅占1字节，所有操作融合为单一内核，计算开销可忽略。

**实验结果**: 在ImageNet分类、GPT-2预训练、Llama-3.1-8B微调等标准任务上验证，所有任务模型精度与全精度 baseline 完全一致。Llama-3.1-8B微调峰值显存从175GiB降至113GiB，模型检查点缩小超一半，优化器步骤速度几乎无下降。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [ParamMem: Augmenting Language Agents with Parametric Reflective Memory](http://arxiv.org/abs/2602.23320v1) `cs.LG (机器学习)` | 针对现有语言智能体自反射机制容易产生重复输出、限制推理性能的问题，提出参数化反射记忆增强方案，有效提升多步推理表现 |
| 5 | [Mitigating Legibility Tax with Decoupled Prover-Verifier Games](http://arxiv.org/abs/2602.23248v1) `cs.AI (人工智能)` | 针对大模型输出可校验性差，低能力模型难以验证大模型输出的痛点，提出解耦证明者-验证者博弈，降低可解释性损耗，提升安全性 |
| 6 | [Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) ...](http://arxiv.org/abs/2602.23225v1) 💻 `cs.CL (计算语言学)` | 针对扩散语言模型宣称支持并行解码却实际退化为类自回归解码的矛盾，分析了问题本质根源，为真并行扩散LLM研发指明方向 |
| 7 | [Fine-Tuning Without Forgetting In-Context Learning: A Theoretical Analysis of Li...](http://arxiv.org/abs/2602.23197v1) `cs.CL (计算语言学)` | 针对大语言模型微调后上下文学习能力容易遗忘的痛点，在线性注意力框架下给出理论分析，为解决该问题提供核心支撑 |
| 8 | [CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays](http://arxiv.org/abs/2602.23276v1) `cs.AI (人工智能)` | 针对现有多模态大模型胸片诊断常生成无依据错误推理的问题，提出基于证据的诊断推理智能体，提升医疗AI的可靠性 |
| 9 | [Evaluating Stochasticity in Deep Research Agents](http://arxiv.org/abs/2602.23271v1) `cs.AI (人工智能)` | 当前深度研究智能体快速发展，但领域缺乏对其核心特性随机性的系统评估，本文填补了评估空白，对Agent研发有指导意义 |
| 10 | [SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via O...](http://arxiv.org/abs/2602.23353v1) `cs.LG (机器学习)` | 基于柏拉图表征假设，提出基于最优传输的半监督单模态视觉语言对齐方法，无需配对多模态数据，降低对齐成本，创新性强 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-01
