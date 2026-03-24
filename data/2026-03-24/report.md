# 🧪 ArXiv AI 日报

📅 **2026-03-24 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **47,963** (¥0.0161)

## 🔥 今日必读

---

### 1. Chimera: Latency- and Performance-Aware Multi-agent Serving for Heterogeneous LLMs

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.22206v1)

👤 Kangqi Ni, Wenyue Hua, Xiaoxiang Shi 等


**中文标题**: 奇美拉（Chimera）：面向异构大语言模型的延迟与性能感知多智能体推理调度服务

**背景与痛点**: 当前多智能体任务多为多阶段依赖的工作流，每个阶段都需要调用大模型。现有大语言模型推理服务大多假设同构模型集群，现有路由方法忽略动态负载变化，调度机制未适配异构多阶段工作流，无法同时兼顾端到端延迟和任务性能。

**核心创新**: 提出Chimera，面向异构大模型集群多智能体工作流的轻量级预测式调度中间件。它联合语义路由、工作流级输出长度预测、实时负载监测做模型选择和队列优化，在极低额外开销下同时提升端到端延迟和任务性能，还支持灵活调整二者的权衡。

**技术细节**: 系统分为四个核心模块：1）语义路由用微调后的ModernBERT输出每个候选模型的置信分，估计模型解决当前请求的成功率；2）用CPU轻量运行的分位数随机森林，预测工作流剩余阶段总输出token数，支撑最短总作业优先调度；3）活动监视器统计各引擎在途请求token总量估算负载延迟；4）负载均衡选满足延迟约束的最高置信度模型，同一工作流复用模型分配，搭配老化机制防止饥饿。

**实验结果**: 在APPS代码生成、MATH数学推理两个代表性多智能体任务上测试，对比vLLM、MLFQ、LTR等主流基线，平均降低端到端延迟1.2倍~2.4倍，提升任务性能8.0~9.5个百分点，额外调度开销占总延迟比例不超过2.2%，几乎可忽略。

---

### 2. Scaling DoRA: High-Rank Adaptation via Factored Norms and Fused Kernels

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.22276v1)

👤 Alexandra Zelenin, Alexandra Zhuravlyova


**中文标题**: 扩展DoRA：基于分解范数和融合核的高秩适配

**背景与痛点**: DoRA作为LoRA的改进版本，通过分离权重的方向和幅值提升微调效果，但主流框架计算行范数时必须先生成完整的BA稠密乘积矩阵，高秩配置下单层就需要数百MB临时内存，几百个适配层叠加后，普通单GPU容易出现OOM，速度也会大幅下降。

**核心创新**: 本文不提出新的适配架构，而是针对DoRA做系统级优化，核心有两点：一是提出因式分解的范数计算方法，无需生成完整BA稠密矩阵，大幅降低临时内存占用；二是开发融合Triton核，把原DoRA的四步组合操作合并为单次遍历，减少4倍访存，还解决了近单位缩放区的数值灾难性抵消问题。

**技术细节**: 分解范数将W加sBA的行平方范数拆分为基础项、交叉项和Gram项三部分，所有项都仅用低秩中间量，分块计算控制内存占用，理论内存最高可降低71倍。融合核采用显式保留小修正项的稳定形式，避免缩放因子接近1时的数值抵消；设计三级运行时自动分发：训练用融合反向核、推理用仅前向融合核，小尺寸或CPU自动回退到原生PyTorch执行。

**实验结果**: 在6个8B到32B的视觉语言模型、跨4代共6款NVIDIA GPU上测试，相比HF PEFT原生DoRA实现，推理速度提升1.5到2.0倍，梯度计算速度提升1.5到1.9倍，峰值显存最高降低7GB，精度和收敛性与原生实现一致。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [On the Direction of RLVR Updates for LLM Reasoning: Identification and Exploitat...](http://arxiv.org/abs/2603.22117v1) `cs.LG (机器学习)` | 深入分析RLVR提升大模型推理能力的参数更新方向，明确优化路径，对进一步改进大模型推理能力有重要研究指导意义 |
| 5 | [Confidence-Based Decoding is Provably Efficient for Diffusion Language Models](http://arxiv.org/abs/2603.22248v1) `cs.LG (机器学习)` | 针对扩散语言模型的解码问题，从理论上证明置信度解码的效率，推动扩散语言模型这一新方向的实用化发展 |
| 6 | [ThinkJEPA: Empowering Latent World Models with Large Vision-Language Reasoning M...](http://arxiv.org/abs/2603.22281v1) `cs.CV (计算机视觉)` | 将大视觉语言推理能力整合到潜世界模型中，解决现有潜世界模型缺乏推理能力的缺陷，推动世界模型前沿发展 |
| 7 | [MARCUS: An agentic, multimodal vision-language model for cardiac diagnosis and m...](http://arxiv.org/abs/2603.22179v1) `cs.AI (人工智能)` | 面向心脏疾病诊断管理打造了Agentic多模态大模型，解决临床心脏检测结果解读难的痛点，医疗AI落地价值高 |
| 8 | [UniMotion: A Unified Framework for Motion-Text-Vision Understanding and Generati...](http://arxiv.org/abs/2603.22282v1) `cs.CV (计算机视觉)` | 是首个支持动作、文本、视觉三大模态同时完成理解与生成的统一框架，填补领域空白，多模态统一建模创新度高 |
| 9 | [Autoregressive vs. Masked Diffusion Language Models: A Controlled Comparison](http://arxiv.org/abs/2603.22075v1) `cs.CL (计算语言学)` | 在相同条件下控制变量对比自回归和掩码扩散语言模型，给出可靠实证结论，为该领域研究提供重要基准参考 |
| 10 | [SPA: A Simple but Tough-to-Beat Baseline for Knowledge Injection](http://arxiv.org/abs/2603.22213v1) 💻 `cs.LG (机器学习)` | 提出简单高效的大模型知识注入基线，效果媲美复杂方法，大幅降低领域知识注入落地成本，实用性很强 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-24
