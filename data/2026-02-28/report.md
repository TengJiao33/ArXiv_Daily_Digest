# 🧪 ArXiv AI 日报

📅 **2026-02-28 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **50,195** (¥0.0167)

## 🔥 今日必读

---

### 1. InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.23200v1)

👤 Sayed Mohammadreza Tayaranian Hosseini, Amir Ardakani, Warren J. Gross


**中文标题**: InnerQ：面向大语言模型KV缓存的硬件感知无调优量化

**背景与痛点**: 大语言模型解码阶段，KV缓存的大小随序列长度线性增长，是内存占用和推理延迟的核心瓶颈。现有主流KV缓存量化方法均沿缓存矩阵外维度分组，该布局不匹配解码阶段向量-矩阵乘法的计算流程，会导致内存访问次数多、反量化开销大，难以兼顾精度和推理速度。

**核心创新**: InnerQ从硬件感知角度重新设计KV缓存的量化分组维度，选择沿缓存矩阵的内维度做分组量化，让分组布局对齐解码阶段向量-矩阵乘法的计算流，实现缩放因子复用减少内存访问和反量化延迟，同时配套无额外开销的精度优化，全程无需调优和校准。

**技术细节**: 具体包含四个关键设计：① 内维度分组量化：缓存矩阵每一行内的同组元素共享缩放和零点参数，可让GPU计算单元复用参数，大幅减少内存访问；② 逐分组混合量化：每个分组根据本地分布动态选对称或非对称量化，额外计算在访存间隙完成，不增加延迟；③ 双高精度窗口：同时保留开头的注意力汇点token和最新token用高精度存储，缓解异常值精度损失；④ Key缓存逐通道归一化，归一化因子prefill阶段计算后折叠进权重，运行时无额外开销。

**实验结果**: 在多个尺寸Llama模型的GSM8K少样本评测中，2bit量化的InnerQ推理精度和非量化KV缓存相当，优于现有主流KV缓存量化方法；相比半精度原生计算最高获得88%加速，比外维度分组的SOTA方法最高提速22%。

---

### 2. ParamMem: Augmenting Language Agents with Parametric Reflective Memory

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.23320v1)

👤 Tianjun Yao, Yongqiang Chen, Yujia Zheng 等


**中文标题**: ParamMem：为语言智能体增强参数化反思记忆
**背景与痛点**: 现有基于反思的语言智能体普遍存在反思输出重复、多样性不足的问题，严重限制推理性能。当前提升多样性的方案要么是提示级修改，要么是检索式跨样本记忆，检索方法受嵌入坍缩限制，难以捕捉组合泛化模式，性能提升有限。
**核心创新**: 核心提出参数化反思记忆模块ParamMem，通过轻量微调将跨样本反思模式编码进模型参数，靠温度采样生成多样化反思，替代检索式方案；进一步构建了统一情景记忆、跨样本记忆、参数化记忆的ParamAgent框架，支持免强大模型依赖的自我改进与弱到强迁移。
**技术细节**: 首先构造任务适配的辅助反思数据集：编程任务输出潜在错误和bug示例，数学任务输出常见易错点，多跳问答输出查询分解和子任务，随后用LoRA做轻量微调得到参数化记忆模块。推理时每次迭代除已有情景记忆、可选检索的跨样本轨迹，额外从ParamMem采样反思信号输入生成模型，采用温度调度：第一轮低温度保证基础稳定性，后续轮次高温度促进反思多样性。
**实验结果**: 在代码生成、数学推理、多跳问答三大领域共7个基准数据集测试，ParamAgent系列全面超过当前SOTA基线；仅需约500训练样本即可生效，支持弱模型训练的参数记忆增强强大模型智能体，可完全基于自身生成数据完成无外依赖的自我提升。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Evaluating Stochasticity in Deep Research Agents](http://arxiv.org/abs/2602.23271v1) `cs.AI (人工智能)` | 针对新兴的深度研究Agent领域，系统研究了输出随机性对任务性能的影响，填补了该方向评估方法论的空白，对Agent落地有重要指导意义。 |
| 5 | [Scale Can't Overcome Pragmatics: The Impact of Reporting Bias on Vision-Language...](http://arxiv.org/abs/2602.23351v1) `cs.CL (计算语言学)` | 纠正了“扩大规模就能提升VLM推理能力”的领域误区，指出VLM推理不足核心根源是训练数据的报告偏差，对VLM数据构建有重要指导价值。 |
| 6 | [SOTAlign: Semi-Supervised Alignment of Unimodal Vision and Language Models via O...](http://arxiv.org/abs/2602.23353v1) `cs.LG (机器学习)` | 基于柏拉图表征假说，提出基于最优传输的半监督单模态视觉语言模型对齐方案，无需配对多模态训练数据，大幅降低对齐成本。 |
| 7 | [FlashOptim: Optimizers for Memory Efficient Training](http://arxiv.org/abs/2602.23349v1) `cs.LG (机器学习)` | 针对大模型训练中参数、梯度、优化器状态占用过多显存的痛点，提出内存高效的优化器框架，降低大模型训练的硬件门槛，实用性强。 |
| 8 | [CXReasonAgent: Evidence-Grounded Diagnostic Reasoning Agent for Chest X-rays](http://arxiv.org/abs/2602.23276v1) `cs.AI (人工智能)` | 针对现有大视觉语言模型在胸部X线诊断中易生成无依据输出的问题，构建了证据驱动的诊断推理Agent，医疗AI落地应用价值高。 |
| 9 | [Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) ...](http://arxiv.org/abs/2602.23225v1) 💻 `cs.CL (计算语言学)` | 回答了扩散语言模型领域的核心困惑，解释了为何扩散LM宣传支持并行解码实际却退化为类自回归动态，对后续研究有重要启发。 |
| 10 | [Spatio-Temporal Token Pruning for Efficient High-Resolution GUI Agents](http://arxiv.org/abs/2602.23235v1) `cs.CV (计算机视觉)` | 针对纯视觉高分辨率GUI Agent存在的严重效率瓶颈，提出时空token剪枝方案，减少冗余计算，大幅提升推理效率，助力GUI Agent落地。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-28
