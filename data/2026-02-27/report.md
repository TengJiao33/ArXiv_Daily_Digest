# 🧪 ArXiv AI 日报

📅 **2026-02-27 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **50,085** (¥0.0166)

## 🔥 今日必读

---

### 1. InnerQ: Hardware-aware Tuning-free Quantization of KV Cache for Large Language Models

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.23200v1)

👤 Sayed Mohammadreza Tayaranian Hosseini, Amir Ardakani, Warren J. Gross


**中文标题**: InnerQ：面向大语言模型KV缓存的硬件感知免调优量化

**背景与痛点**: 大语言模型长序列生成时，KV缓存随序列长度增长会占据绝大多数内存开销。现有KV缓存量化方法为规避通道离群点普遍沿缓存矩阵外维分组，该方式和GPU解码阶段向量矩阵乘法执行流不匹配，去量化时内存访问冗余、延迟偏高，不少方法还需要额外校准开销。

**核心创新**: 提出沿缓存矩阵内维做分组量化，对齐GPU向量矩阵乘的访问模式，实现缩放因子复用、减少内存访问以降低解码延迟；搭配多个轻量精度补偿策略，全程免调优无额外运行开销，在压缩率相当的情况下同时提升推理速度和模型精度。

**技术细节**: InnerQ对KV缓存的每个token行沿通道（内维）划分量化组，同一组共享缩放因子和零点，在融合乘加计算中实现缩放因子复用，大幅减少内存加载次数。额外搭配三个轻量优化：每个分组根据本地误差自动选对称/非对称量化，额外计算利用访存间隙完成不增加延迟；双高精度窗口同时保留初始注意力沉token和最新生成token用高精度存储；预填充阶段计算key逐通道归一化，归一化因子折叠进权重无运行时开销。

**实验结果**: 在Llama 1B~13B模型的GSM8k少样本评测中，InnerQ精度和未量化KV缓存相当，优于KIVI等现有方法；相比半精度原始计算最高提速88%，比现有外维分组量化最高降延迟22%，缓存大小和现有方法相当。

---

### 2. ParamMem: Augmenting Language Agents with Parametric Reflective Memory

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.23320v1)

👤 Tianjun Yao, Yongqiang Chen, Yujia Zheng 等


**中文标题**: ParamMem：为语言智能体增强参数化反思记忆
**背景与痛点**: 反思迭代型语言智能体常生成重复反思内容，限制了代码生成、数学推理、多跳问答等复杂任务的性能。现有提升多样性方案，要么提示层修改效果有限，要么检索式跨样本记忆存在嵌入坍缩，难以捕捉组合反思模式。
**核心创新**: 提出参数化反思记忆模块ParamMem，通过轻量微调将跨样本反思模式编码进模型参数，推理时靠温度采样生成多样化新反思，机制上区别于提示修改和检索式方法，进一步构建了整合三类记忆的ParamAgent框架。
**技术细节**: 先构造辅助训练集：针对不同任务生成对应格式的反思信号，代码/数学任务生成潜在错误反思，多跳QA任务生成问题分解子任务，再用LoRA轻量微调得到ParamMem模块。推理时每轮迭代，在原有情景、跨样本记忆基础上，拼接ParamMem采样的反思输入给动作模型，通过动态调整采样温度（首轮0.2，后续1.0）提升多样性。
**实验结果**: 在代码生成、数学推理、多跳问答共6个标准数据集测试，不同规模骨干模型均显著超过现有SOTA基线。仅需500训练样本即可生效，支持无外部强模型依赖的自提升，也可实现弱模型到强模型的能力迁移。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Mitigating Legibility Tax with Decoupled Prover-Verifier Games](http://arxiv.org/abs/2602.23248v1) `cs.AI (人工智能)` | 针对大模型输出难被低能力系统核查验证的痛点，提出解耦的证明者-验证者博弈框架，缓解可解读性代价，提升高风险场景大模型输出的可靠性 |
| 5 | [Scale Can't Overcome Pragmatics: The Impact of Reporting Bias on Vision-Language...](http://arxiv.org/abs/2602.23351v1) `cs.CL (计算语言学)` | 指出当前视觉语言模型推理能力不足的核心根源是训练数据的报告偏差，证明模型规模增长无法解决语用问题，对VLM研究有重要指导意义 |
| 6 | [FlashOptim: Optimizers for Memory Efficient Training](http://arxiv.org/abs/2602.23349v1) `cs.LG (机器学习)` | 针对神经网络混合精度训练中优化器内存开销过大的痛点，设计内存高效的FlashOptim，支持有限硬件训练更大模型，实用性强，对工业训练价值高 |
| 7 | [AgentDropoutV2: Optimizing Information Flow in Multi-Agent Systems via Test-Time...](http://arxiv.org/abs/2602.23258v1) 💻 `cs.AI (人工智能)` | 针对多智能体系统中单个智能体错误引发级联失效的问题，提出测试时矫正-拒绝剪枝优化信息流，大幅提升多智能体系统推理的可靠性 |
| 8 | [SeeThrough3D: Occlusion Aware 3D Control in Text-to-Image Generation](http://arxiv.org/abs/2602.23359v1) `cs.CV (计算机视觉)` | 发现3D布局条件文生图中遮挡推理被长期忽视，提出遮挡感知的3D控制方案，可生成深度一致的被遮挡物体，大幅提升3D生成质量 |
| 9 | [Why Diffusion Language Models Struggle with Truly Parallel (Non-Autoregressive) ...](http://arxiv.org/abs/2602.23225v1) 💻 `cs.CL (计算语言学)` | 解答了扩散语言模型宣称支持完全并行解码，实际却收敛到类自回归解码的核心问题，为扩散大模型后续研究提供了关键启发 |
| 10 | [LLM Novice Uplift on Dual-Use, In Silico Biology Tasks](http://arxiv.org/abs/2602.23329v1) `cs.AI (人工智能)` | 验证了大语言模型对计算生物学任务中新手用户的能力提升效果，明确了LLM赋能非专家科研的实际价值，推动LLM在科学领域落地 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-27
