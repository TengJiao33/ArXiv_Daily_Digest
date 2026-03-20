# 🧪 ArXiv AI 日报

📅 **2026-03-20 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **54,753** (¥0.0181)

## 🔥 今日必读

---

### 1. Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.19220v1)

👤 Zhuolin Yang, Zihan Liu, Yang Chen 等


**中文标题**: Nemotron-Cascade 2：基于级联强化学习和多域同策略蒸馏的大语言模型后训练

**背景与痛点**: 当前大语言模型多领域后训练中，联合强化学习易出现跨域干扰与训练不稳定，顺序强化学习又难以避免灾难性遗忘导致性能回退；现有顶尖推理大模型普遍参数规模极大，部署成本高，亟需小参数模型实现顶尖竞赛级推理能力。

**核心创新**: 本文在第一代Nemotron-Cascade级联强化学习框架基础上，引入多领域同策略蒸馏（MOPD）机制，有效修复级联训练过程中的性能回退，最终用仅3B激活参数的30B MoE模型，实现了媲美大参数前沿模型的竞赛级推理能力。

**技术细节**: 整体后训练流程为：高质量多域监督微调后，按顺序执行指令跟随RL、多域RL、多域同策略蒸馏（MOPD）、人类偏好RLHF、长上下文RL、代码RL、软件工程RL七个级联阶段。MOPD选取级联过程中每个领域性能最优的中间 checkpoint作为领域教师，对学生做稠密token级反向KL蒸馏，相比GRPO的稀疏序列奖励，训练收敛更快、样本效率更高，全程采用同策略GRPO，移除KL散度正则项提升训练稳定性。

**实验结果**: 该模型在2025年国际数学奥林匹克（IMO）、国际信息学奥林匹克（IOI）、ICPC世界总决赛三大顶级竞赛均取得金牌，是全球第二个达成该成绩的开源大模型；数学、代码推理性能超过同激活规模的Qwen3.5 35B-A3B，接近十倍参数的前沿大模型。

---

### 2. Box Maze: A Process-Control Architecture for Reliable LLM Reasoning

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.19182v1)

👤 Zou Qiang


**中文标题**: Box Maze：面向大语言模型可靠推理的过程控制架构
**背景与痛点**: 大语言模型在对抗提示、胁迫场景下极易产生幻觉，推理一致性差。当前主流的RLHF对齐、输出后过滤等方案仅在行为或参数层做概率性约束，缺乏推理过程层面的硬约束机制，很容易被对抗攻击绕过，无法从结构上避免边界突破与内容编造。
**核心创新**: 提出Box Maze这一过程控制概念架构，在基础大模型与输出接口之间插入三层显式控制中间件，将可靠性保障从传统的结果/参数层面转移到推理过程层面，用硬逻辑边界替代概率性约束，从结构上避免对抗场景出错，且是模型无关的通用方案。
**技术细节**: Box Maze由三个嵌套控制循环构成中间件层：1.记忆循环：为所有推理步骤添加不可修改的时间戳，建立可追溯认知链，防止模型编造虚假历史记忆；2.逻辑循环：对推理链做因果一致性验证，发现矛盾就强制暂停生成，避免输出逻辑通顺但事实错误的内容；3.心脏锚：作为不可变的边界约束核心，遇到边界侵犯就触发硬停止，配套协议要求严格区分事实与推断、显式标记未知。
**实验结果**: 在50个对抗胁迫场景，跨DeepSeek-V3、豆包、通义千问三个底座大模型做模拟验证，原生RLHF对齐模型的边界违反率约为40%，Box Maze将该指标降到1%以下，消融实验证实心脏锚约束是核心有效组件，方案适配任意底座模型。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encode...](http://arxiv.org/abs/2603.19209v1) `cs.CV (计算机视觉)` | 现有VLMs普遍采用Transformer做视觉骨干，本文系统评估状态空间模型作为VLM视觉编码器的效果，对下一代高效VLM架构设计有重要参考 |
| 5 | [FinTradeBench: A Financial Reasoning Benchmark for LLMs](http://arxiv.org/abs/2603.19225v1) `cs.CE` | 针对大模型真实金融决策推理缺乏合适评估基准的痛点，构建融合基本面与交易信号的金融推理基准，填补领域空白，助力LLM金融落地 |
| 6 | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](http://arxiv.org/abs/2603.19191v1) `cs.AI (人工智能)` | 通用GUI Agent训练高度依赖奖励质量，现有方案泛化性差，本文提出可扩展的通用GUI奖励评判框架，解决了GUI Agent训练的核心痛点 |
| 7 | [F2LLM-v2: Inclusive, Performant, and Efficient Embeddings for a Multilingual Wor...](http://arxiv.org/abs/2603.19223v1) `cs.CL (计算语言学)` | 推出覆盖8种尺寸（80M到14B）的新一代通用多语言嵌入模型，性能均衡高效，可满足不同部署场景下的多语言检索任务需求 |
| 8 | [DyMoE: Dynamic Expert Orchestration with Mixed-Precision Quantization for Effici...](http://arxiv.org/abs/2603.19172v1) `cs.LG (机器学习)` | 针对MoE模型在边缘设备推理时内存开销大、I/O overhead高的痛点，提出动态专家编排加混合精度量化方案，大幅提升边缘MoE推理效率 |
| 9 | [How Uncertainty Estimation Scales with Sampling in Reasoning Models](http://arxiv.org/abs/2603.19118v1) `cs.AI (人工智能)` | 针对推理大语言模型中不确定性估计的研究空白，系统分析并行采样下不确定性估计的缩放规律，对大模型推理部署可靠性设计有指导意义 |
| 10 | [DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction an...](http://arxiv.org/abs/2603.19219v1) `cs.CV (计算机视觉)` | 自动驾驶大模型亟需高效可扩展的视觉token化方案，本文提出统一3D驾驶场景tokenization方法，支持多任务处理，助力自动驾驶大模型落地 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-20
