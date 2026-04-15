# 🧪 ArXiv AI 日报

📅 **2026-04-15 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **60,644** (¥0.0198)

## 🔥 今日必读

---

### 1. Rethinking On-Policy Distillation of Large Language Models: Phenomenology, Mechanism, and Recipe

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.13016v1)

👤 Yaxuan Li, Yuxin Zuo, Bingxiang He 等


**中文标题**: 重新思考大语言模型的在线策略蒸馏：现象、机制与实践方案

**背景与痛点**: 在线策略蒸馏（OPD）是当前大语言模型后训练的核心技术，被Qwen3、GLM-5等主流模型采用，可缓解离线蒸馏的曝光偏差问题。但现有研究仅关注其收益，缺乏对训练动力学和失效机制的系统分析，实践中常出现更强老师反而蒸馏失败的反常现象。

**核心创新**: 本文首次系统拆解了OPD成功的核心规则，打破了“老师基准性能越强，蒸馏效果越好”的普遍认知，揭示了OPD的token级训练机制，提出了两套可落地方案修复失效的OPD，还指出了当前OPD在长序列场景下的固有局限。

**技术细节**: 通过控制实验总结出OPD成功的两个必要条件：一是师生思维模式一致，初始top-k token重叠率决定最终效果上限；二是老师必须具备学生未见过的新知识，同 pipeline 训练的大尺度老师往往无新知识可转移。研究证实97%到99%的梯度信号来自师生共享的高概率重叠token，只优化重叠token即可达到全量OPD的效果，进而提出两套修复策略。

**实验结果**: 在AIME、AMC等数学推理基准，结合DeepSeek、Qwen多组模型测试，所提策略可让原本失效的OPD将师生性能缺口回收率提升15%到58%，同时证实OPD奖励质量随轨迹长度增加退化，长推理序列存在明显的性能坍缩风险。

---

### 2. Lightning OPD: Efficient Post-Training for Large Reasoning Models with Offline On-Policy Distillation

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.13010v1)

👤 Yecheng Wu, Song Han, Hai Cai


**中文标题**: 《Lightning OPD：面向大推理模型的离线同策略蒸馏高效后训练》

**背景与痛点**: 当前大推理模型后训练中，同策略蒸馏（OPD）效果优于传统强化学习方案，但标准OPD训练全程需要运行在线大模型教师推理服务，基础设施开销极高；朴素的离线预计算教师对数概率方案无法达到标准OPD的性能，存在突出的性能-效率矛盾。

**核心创新**: 本文首次指出OPD训练必须满足「教师一致性」核心条件，证明SFT阶段和OPD阶段的教师不匹配会引入不可消除的梯度偏置，导致在线/离线OPD都收敛到次优解；在此基础上提出全离线Lightning OPD框架，完全消除对在线教师服务的依赖，理论证明其最优解与标准OPD一致，还自带隐式正则防止策略漂移。

**技术细节**: 整体遵循两阶段设计：1）SFT阶段：要求生成SFT训练轨迹的教师，和后续OPD阶段的参考教师为同一模型，用该教师生成的轨迹微调学生基座，得到SFT初始化的参考策略；2）离线OPD阶段：先对参考策略采样的生成结果一次性预计算所有位置的教师对数概率，构建固定离线数据集，训练时直接读取预存值计算优势信号更新学生，全程不需要在线教师。理论证明其与标准OPD共享最优固定点，梯度误差有界，不需要额外显式KL惩罚。

**实验结果**: 在数学推理（AIME、HMMT）和代码生成（LiveCodeBench）基准测试验证，基于Qwen3-8B基座达到AIME 2024 69.9%的准确率，总训练仅需30GPU小时，相比标准OPD获得4倍加速，性能匹配甚至超过标准OPD，消融实验验证了教师一致性的核心作用。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Drawing on Memory: Dual-Trace Encoding Improves Cross-Session Recall in LLM Agen...](http://arxiv.org/abs/2604.12948v1) `cs.AI (人工智能)` | 针对现有LLM Agent持久记忆无法支持跨会话时序推理、变化跟踪的痛点，提出双轨迹编码方案，显著提升跨会话回忆能力，推动长周期Agent发展 |
| 5 | [One Token Away from Collapse: The Fragility of Instruction-Tuned Helpfulness](http://arxiv.org/abs/2604.13006v1) `cs.CL (计算语言学)` | 发现指令调优大模型的惊人脆弱性：仅禁止单个常用token就会导致模型有用性完全崩溃，对大模型鲁棒性、安全性研究有重要警示价值 |
| 6 | [Accelerating Speculative Decoding with Block Diffusion Draft Trees](http://arxiv.org/abs/2604.12989v1) `cs.CL (计算语言学)` | 针对投机解码推理加速的现有瓶颈，提出基于块扩散草稿树的加速方案，进一步提升大模型推理吞吐，对大模型落地部署有很高实用价值 |
| 7 | [RePAIR: Interactive Machine Unlearning through Prompt-Aware Model Repair](http://arxiv.org/abs/2604.12820v1) `cs.AI (人工智能)` | 针对大语言模型难以选择性删除训练吸收的有害、隐私数据的痛点，提出提示感知模型修复的交互式机器遗忘方案，满足合规需求，实用性强 |
| 8 | [AISafetyBenchExplorer: A Metric-Aware Catalogue of AI Safety Benchmarks Reveals ...](http://arxiv.org/abs/2604.12875v1) `cs.AI (人工智能)` | 系统梳理当前LLM安全评估的基准生态，揭示了现有基准测量碎片化、治理薄弱的核心问题，为AI安全评估领域后续发展指明方向 |
| 9 | [Don't Show Pixels, Show Cues: Unlocking Visual Tool Reasoning in Language Models...](http://arxiv.org/abs/2604.12896v1) `cs.CV (计算机视觉)` | 针对现有多模态大模型无法有效利用视觉工具生成线索推理的痛点，提出感知程序框架，解锁大模型视觉工具推理能力，推动多模态Agent发展 |
| 10 | [ROSE: An Intent-Centered Evaluation Metric for NL2SQL](http://arxiv.org/abs/2604.12988v1) `cs.DB` | 针对现有NL2SQL主流评价指标执行准确率敏感度高、可靠性差的问题，提出意图中心的新评价指标ROSE，更准确反映模型能力，利于NL2SQL技术落地 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-15
