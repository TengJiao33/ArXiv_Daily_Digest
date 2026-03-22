# 🧪 ArXiv AI 日报

📅 **2026-03-22 周日** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **54,656** (¥0.0180)

## 🔥 今日必读

---

### 1. Nemotron-Cascade 2: Post-Training LLMs with Cascade RL and Multi-Domain On-Policy Distillation

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.19220v1)

👤 Zhuolin Yang, Zihan Liu, Yang Chen 等


**中文标题**: Nemotron-Cascade 2：基于级联强化学习和多域在线蒸馏的大语言模型后训练

**背景与痛点**: 当前大语言模型多领域后训练中，传统联合强化学习易出现跨域干扰、灾难性遗忘，初代级联RL虽缓解该问题，但覆盖领域有限，训练过程中仍会出现基准性能退化，难以在推理、智能体这类高复杂度任务上维持稳定性能增益。

**核心创新**: 本文在初代级联RL框架基础上做了两大改进：一是将级联RL扩展覆盖推理、智能体等更广的高优先级任务域；二是引入多领域在线蒸馏（MOPD），在级联训练过程中用各域最强中间 checkpoint 做老师蒸馏，有效恢复性能退化，持续获得性能增益。

**技术细节**: 训练遵循顺序级联范式：SFT后按最小化跨域干扰排序训练阶段：指令遵循RL→多领域混合RL→MOPD→人类偏好RLHF→长上下文RL→代码RL→软件工程智能体RL。MOPD以同流程各域最优中间模型为老师，用逆KL做token级稠密蒸馏，无额外分布偏移，样本效率远高于稀疏奖励的GRPO；RL全程用全在线GRPO，移除KL项，训练稳定。

**实验结果**: 该30B总参数、3B激活参数的开源MoE模型，是继DeepSeek大模型之后第二个在2025 IMO、IOI、ICPC世界总决赛都拿到金牌的开源模型，仅用对手1/20的激活参数，数学、编码推理性能追平数百B参数的前沿模型，对齐性能也远超同规模模型，全文开源模型与训练数据。

---

### 2. Box Maze: A Process-Control Architecture for Reliable LLM Reasoning

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.19182v1)

👤 Zou Qiang


**中文标题**: Box Maze：面向大语言模型可靠推理的过程控制架构

**背景与痛点**: 针对大语言模型在对抗提示下易出现幻觉、推理可靠性不足的问题，现有主流方法如RLHF、输出过滤、过程监督都仅停留在行为优化或后处理层面，缺乏对推理过程的显式硬约束，对抗场景下极易被绕过，无法从结构上避免边界突破和内容虚构。

**核心创新**: 提出中间件层面的过程控制架构Box Maze，通过在基模型与输出之间插入三层显式控制约束，从架构层面保障推理过程完整性，而非依赖参数层面的概率性对齐。该架构与基模型无关，可适配任意现有大语言模型，实现结构化错误预防而非事后过滤。

**技术细节**: Box Maze由三层相互约束的循环模块组成：1 记忆循环：为所有推理步骤添加不可变时间戳锚定，构建不可篡改的推理历史链，核心保障时序不变性，区别于RAG的语义检索逻辑；2 逻辑循环：对推理链做因果一致性校验，发现矛盾就进入约束状态，禁止生成无依据猜测，避免“连贯胡说”；3 心锚约束层：强制执行互斥边界规则，遇不可调和冲突触发硬停止，同时配套认知谦逊协议，强制区分事实与推断，明确标记未知。

**实验结果**: 在50个对抗胁迫场景做模拟验证，跨DeepSeek-V3、豆包、通义千问三个异构模型，原生对齐大模型的边界违反率为40%，Box Maze将其降到1%以下，消融实验验证了心锚约束的核心作用，证明过程级架构约束可显著提升大模型对抗推理可靠性。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Do VLMs Need Vision Transformers? Evaluating State Space Models as Vision Encode...](http://arxiv.org/abs/2603.19209v1) `cs.CV (计算机视觉)` | 当前VLM普遍采用Transformer作为视觉编码器，该工作系统评估状态空间模型作为VLM编码器的可行性，为VLM轻量化设计提供新方向 |
| 5 | [OS-Themis: A Scalable Critic Framework for Generalist GUI Rewards](http://arxiv.org/abs/2603.19191v1) `cs.AI (人工智能)` | 当前通用GUI智能体强化学习训练面临奖励质量差的核心瓶颈，提出可扩展的通用GUI奖励评判框架，助力GUI Agent技术落地发展 |
| 6 | [SOL-ExecBench: Speed-of-Light Benchmarking for Real-World GPU Kernels Against Ha...](http://arxiv.org/abs/2603.19173v1) `cs.LG (机器学习)` | 现有AI生成GPU内核的基准仅对比软件基线，该工作提出新基准，以贴近硬件极限作为评价标准，推动高效AI生成代码发展 |
| 7 | [F2LLM-v2: Inclusive, Performant, and Efficient Embeddings for a Multilingual Wor...](http://arxiv.org/abs/2603.19223v1) `cs.CL (计算语言学)` | 推出覆盖80M到14B共8种尺寸的新一代多语言通用嵌入模型，兼顾性能与效率，可适配多语言RAG等不同场景需求 |
| 8 | [DyMoE: Dynamic Expert Orchestration with Mixed-Precision Quantization for Effici...](http://arxiv.org/abs/2603.19172v1) `cs.LG (机器学习)` | 针对MoE模型端侧推理内存占用大、IO开销高的痛点，提出动态专家编排结合混合精度量化方案，推动MoE模型端侧落地 |
| 9 | [Evaluating Counterfactual Strategic Reasoning in Large Language Models](http://arxiv.org/abs/2603.19167v1) `cs.CL (计算语言学)` | 现有研究无法区分LLM的策略能力来自真实推理还是记忆模式，该工作在重复博弈下评估LLM反事实推理，填补领域评估空白 |
| 10 | [DriveTok: 3D Driving Scene Tokenization for Unified Multi-View Reconstruction an...](http://arxiv.org/abs/2603.19219v1) `cs.CV (计算机视觉)` | 针对自动驾驶中大模型接口的视觉 token 化可扩展性痛点，提出3D驾驶场景统一分词方案，支持多视图重建与理解，推进自动驾驶大模型落地 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-22
