# 🧪 ArXiv AI 日报

📅 **2026-03-07 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **52,511** (¥0.0173)

## 🔥 今日必读

---

### 1. FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.05451v1)

👤 Ted Zadouri, Markus Hoehnerbach, Jay Shah 等


**中文标题**: FlashAttention-4：面向非对称硬件扩展的算法与内核流水线协同设计

**背景与痛点**: 当前AI数据中心已大规模部署英伟达Blackwell架构B200/GB200 GPU，该架构存在非对称硬件扩展特性：张量核心吞吐量较上一代Hopper翻倍，但共享内存带宽、指数功能单元吞吐量基本不变。原针对Hopper优化的FlashAttention-3无法适配新瓶颈，直接移植会浪费大量性能。

**核心创新**: 本文针对Blackwell架构的非对称硬件瓶颈，提出算法与内核流水线协同设计方案，核心思路是通过算法改造抵消非矩阵运算与共享内存带宽瓶颈，尽可能让高吞吐量张量核心持续跑满，同时大幅提升内核开发编译效率。

**技术细节**: 前向阶段重新设计乒乓流水线，重叠异步张量核心运算和softmax计算；通过三阶多项式近似软件模拟指数运算，分摊硬件指数单元瓶颈，引入条件软max缩放，仅在最大值变化超过阈值时做中间重缩放，跳过冗余操作。反向阶段利用新增的片上张量内存存储中间结果，借助Blackwell的2-CTA MMA模式将共享内存流量减半，同时将dQ梯度的全局原子加次数减半；新增负载感知调度和低开销确定性执行模式，全程基于Python嵌入式CuTe-DSL开发，编译速度比C++模板实现快20-30倍。

**实验结果**: 在Blackwell B200 GPU BF16精度下测试，FlashAttention-4对比cuDNN 9.13最高获得1.3倍提速，对比Triton官方实现最高获得2.7倍提速，峰值达到1613 TFLOPs/s，张量核心利用率71%，长序列场景下性能优势稳定。

---

### 2. Reasoning Theater: Disentangling Model Beliefs from Chain-of-Thought

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.05488v1)

👤 Siddharth Boppana, Annabel Ma, Max Loeffler 等


**中文标题**: 推理剧场：从思维链中分离模型的内在信念

**背景与痛点**: 当前推理大模型普遍输出思维链（CoT），学界普遍认为CoT可忠实反映模型内部推理过程，常被用于安全审计与可解释性分析。但已有研究发现CoT存在不忠实问题，纯文本CoT监控无法识别模型提前确定答案却生成冗余推理的“表演性推理”现象。

**核心创新**: 本文提出用注意力激活探针从模型中间激活中提取内在信念，通过对比探针解码、模型强制提前回答、纯文本监控三类方法的解码能力，量化区分表演性推理与真实推理，还可基于探针置信度实现自适应推理提前退出，有效降低推理成本。

**技术细节**: 本文选取不同规模的主流推理大模型，针对简单知识回忆任务MMLU-Redux和困难多跳推理任务GPQA-Diamond，收集全推理过程各层各token的激活。设计注意力探针：通过注意力加权池化任意长度前缀的激活，训练轻量分类器预测模型最终答案，训练时采样不同长度前缀保证泛化，用三类方法的准确率差量化表演性程度，同时分析推理拐点与内部信念变化的关联。

**实验结果**: 实验验证发现，简单任务、更大参数模型的CoT表演性更强，困难多跳任务的CoT更忠实，推理拐点（回溯、顿悟时刻）几乎都对应真实的内部信念更新。基于探针的提前退出可在保持精度不变的前提下，为MMLU节省80% tokens，为GPQA-Diamond节省30% tokens。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [RoboPocket: Improve Robot Policies Instantly with Your Phone](http://arxiv.org/abs/2603.05504v1) `cs.RO (机器人)` | 解决机器人模仿学习数据采集效率低的核心痛点，提出用普通消费级手机即可快速采集数据、即时优化机器人策略，大幅降低机器人策略迭代门槛。 |
| 5 | [Building AI Coding Agents for the Terminal: Scaffolding, Harness, Context Engine...](http://arxiv.org/abs/2603.05344v1) `cs.AI (人工智能)` | 针对终端原生AI编码Agent开发，整理了脚手架、测试框架、上下文工程等实践方案与经验，对当前火爆的编码Agent落地有很强指导价值。 |
| 6 | [POET-X: Memory-efficient LLM Training by Scaling Orthogonal Transformation](http://arxiv.org/abs/2603.05500v1) `cs.LG (机器学习)` | 针对大语言模型训练内存占用高、稳定性不足的痛点，基于正交变换重参数实现了内存高效的大模型训练，提升了训练的稳定性与可扩展性。 |
| 7 | [Judge Reliability Harness: Stress Testing the Reliability of LLM Judges](http://arxiv.org/abs/2603.05399v1) 💻 `cs.AI (人工智能)` | 当前LLM评委被广泛用于各类AI benchmark评测，但其可靠性缺乏系统验证，该工作开源了压力测试框架，大幅提升AI评测结果的可信度。 |
| 8 | [InfoFlow KV: Information-Flow-Aware KV Recomputation for Long Context](http://arxiv.org/abs/2603.05353v1) `cs.LG (机器学习)` | 针对长上下文RAG推理中预填充大段检索内容的性能瓶颈，提出信息流感知的KV重计算方法，有效提升长上下文RAG的推理效率。 |
| 9 | [On-Policy Self-Distillation for Reasoning Compression](http://arxiv.org/abs/2603.05433v1) `cs.LG (机器学习)` | 针对大模型推理过程冗余度高、生成速度慢的问题，提出在线自蒸馏方法实现推理压缩，可在不损失推理精度的前提下生成更简洁的推理过程。 |
| 10 | [RealWonder: Real-Time Physical Action-Conditioned Video Generation](http://arxiv.org/abs/2603.05449v1) `cs.CV (计算机视觉)` | 当前视频生成缺乏对3D动作物理后果的结构理解，提出实时物理动作条件视频生成方法，推动具身生成、机器人仿真等方向发展。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-07
