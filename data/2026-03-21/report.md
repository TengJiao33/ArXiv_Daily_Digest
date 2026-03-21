# 🧪 ArXiv AI 日报

📅 **2026-03-21 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **54,729** (¥0.0181)

## 🔥 今日必读

---

### 1. Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.19220v1)

👤 Zhuolin Yang, Zihan Liu, Yang Chen 等


**中文标题**: Nemotron-Cascade 2：基于级联强化学习与多领域在线蒸馏的大语言模型后训练
**背景与痛点**: 当前大语言模型多领域强化学习后训练普遍存在跨任务干扰、灾难性遗忘问题，顶尖竞赛级推理能力高度依赖千亿级超大参数，中小参数模型难以达到该水平，原有级联RL框架覆盖领域有限，也无法解决训练过程中的性能回退问题。
**核心创新**: 本文扩展了级联RL框架覆盖全领域推理与智能体任务，提出多领域在线蒸馏（MOPD）方法解决级联训练的性能回退问题，在仅30B总参数、3B激活参数的MoE模型上实现了顶尖竞赛级推理能力，大幅提升了模型智力密度。
**技术细节**: 后训练遵循有序级联流程：SFT精调后依次执行指令遵循RL、非冲突多领域联合RL、MOPD蒸馏、RLHF对齐、长上下文RL、代码RL、软件工程智能体RL。全程用在线GRPO优化，移除KL正则项提升稳定性。MOPD复用级联过程中各领域最优中间 checkpoint做老师，采用逆KL做token级稠密蒸馏，收敛速度远快于稀疏奖励的RL，高效修复性能回退。
**实验结果**: 在2025IMO、IOI、ICPC世界总决赛均获得金牌，是继DeepSeek大模型后第二个开放权重达成该成绩的模型，总参数比前沿大模型少20倍，推理性能追平千亿级开放模型，多个推理、对齐基准超过同规模竞品。

---

### 2. Box Maze: A Process-Control Architecture for Reliable LLM Reasoning

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.19182v1)

👤 Zou Qiang


**中文标题**: Box Maze：面向大语言模型可靠推理的过程控制架构
**背景与痛点**: 现有大语言模型在对抗性提示、情绪胁迫场景下极易产生幻觉，推理一致性差。当前主流安全方案如RLHF、输出过滤都仅在行为层面优化合规性，属于后验调优或过滤，没有在推理架构层面引入硬约束，很容易被间接提示注入、渐进式边界侵蚀绕过，无法保障推理过程完整性。
**核心创新**: 提出Box Maze这一中间件层过程控制架构，将端到端推理拆分为三层显式约束模块，通过架构级硬约束从结构上避免边界违规，而非仅靠训练降低违规概率。该方案模型无关，适配任意底座大模型，填补了现有工作缺乏不可绕过推理边界的空白。
**技术细节**: Box Maze在底座大模型和输出接口之间引入三层互锁约束循环：一是记忆循环，为每一步推理添加不可变时间戳记录，防止回溯编造虚假记忆，核心是时间不可变性而非语义检索；二是逻辑循环，对推理链做因果一致性检查，发现矛盾就强制停止生成，避免“连贯胡说”；三是核心的心脏锚模块，用互斥规则硬锁认知边界，遇到违规胁迫就触发硬停止，额外配套认知谦逊协议，强制区分事实与推理，明确标记未知，禁止猜测补全。
**实验结果**: 研究在50个渐进式边界侵蚀对抗场景，对DeepSeek-V3、豆包、通义千问三个模型做模拟验证，原生RLHF对齐基线的边界违规率约40%，Box Maze将违规率降到1%以下，消融实验验证心脏锚是核心有效模块，跨底座模型均保持稳定鲁棒性，当前仅为概念验证，完整工程实现仍在推进中。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encode...](http://arxiv.org/abs/2603.19209v1) `cs.CV (计算机视觉)` | 打破当前VLM普遍使用Transformer作为视觉编码器的定势，系统评估状态空间模型作为VLM视觉编码器的效果，为VLM架构优化开辟新方向 |
| 5 | [DyMoE: Dynamic Expert Orchestration with Mixed-Precision Quantization for Effici...](http://arxiv.org/abs/2603.19172v1) `cs.LG (机器学习)` | 针对MoE模型端侧推理内存占用大、IO开销高的痛点，提出动态专家编排结合混合精度量化方案，推动MoE在边缘设备落地 |
| 6 | [FinTradeBench: A Financial Reasoning Benchmark for LLMs](http://arxiv.org/abs/2603.19225v1) `cs.CE` | 针对真实金融决策需要整合异构信号推理的痛点，构建了专门面向LLM的金融推理基准，方便评估模型实际能力，工业价值很高 |
| 7 | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](http://arxiv.org/abs/2603.19191v1) `cs.AI (人工智能)` | 针对通用GUI智能体强化学习训练依赖高质量奖励函数的痛点，提出可扩展的通用GUI奖励评论框架，有效提升GUI Agent鲁棒性 |
| 8 | [How Uncertainty Estimation Scales with Sampling in Reasoning Models](http://arxiv.org/abs/2603.19118v1) `cs.AI (人工智能)` | 研究扩展链-of-thought推理场景下，不确定性估计随采样缩放的变化规律，对推理大模型落地的风险控制有重要指导意义 |
| 9 | [DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction an...](http://arxiv.org/abs/2603.19219v1) `cs.CV (计算机视觉)` | 针对自动驾驶大模型需要可扩展视觉分词接口的需求，提出统一的3D驾驶场景分词方案，支撑多任务处理，推动自动驾驶大模型落地 |
| 10 | [Evaluating Counterfactual Strategic Reasoning in Large Language Models](http://arxiv.org/abs/2603.19167v1) `cs.CL (计算语言学)` | 针对大语言模型的战略能力究竟是真推理还是记忆模式的争议，在重复博弈场景评估反事实推理，对研究LLM推理本质有重要价值 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-21
