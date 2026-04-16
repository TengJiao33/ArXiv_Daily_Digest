# 🧪 ArXiv AI 日报

📅 **2026-04-16 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **57,418** (¥0.0187)

## 🔥 今日必读

---

### 1. TREX: Automating LLM Fine-tuning via Agent-Driven Tree-based Exploration

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.14116v1)

👤 Zerun Ma, Guoqiang Wang, Xinchen Xie 等


**中文标题**: TREX：基于智能体驱动树搜索的大语言模型微调自动化

**背景与痛点**: 当前AI研究智能体多聚焦于目标明确、计算成本低的孤立任务，无法实现大语言模型微调全流程自动化。LLM微调需要统筹数据构建、算法选型、超参数调优等开放式任务，且单轮训练计算开销大，现有进化搜索方法效率极低，也缺乏专用评测基准。

**核心创新**: 提出首个面向大语言模型全流程自动微调的多智能体框架TREX，将多轮迭代的微调优化建模为搜索树问题，用蒙特卡洛树搜索平衡有效方案利用和新方案探索，适配有限计算预算，同时构建了首个专门评测自动微调能力的FT-Bench基准。

**技术细节**: 框架采用双智能体分工：Researcher智能体负责解析任务需求，检索文献，基于历史实验制定细化实验计划，一次生成3-5组并行配置提升集群利用率；Executor智能体基于OpenHands开发，对接GPU集群调度，将计划转化为可执行代码，完成全流程落地。自研AIDP库提供模块化LLM数据处理原语，降低数据 pipeline 构建失败率，搭配压缩上下文记忆机制和坏例归因分析，提供细粒度优化反馈。

**实验结果**: 在包含10个真实场景任务的FT-Bench上测试，TREX可在限定迭代次数内持续提升模型性能，多个任务的最终效果超过人类专家设计的微调 pipeline，消融实验验证了所有核心设计的有效性。

---

### 2. LongCoT: Benchmarking Long-Horizon Chain-of-Thought Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.14140v1)

👤 Sumeet Ramesh Motwani, Daniel Nichols, Charles London 等


**中文标题**: LongCoT：长程思维链推理基准测试
**背景与痛点**: 随着大模型上下文窗口不断扩大，面向复杂自主任务的长程多步推理成为核心能力，但现有基准要么测试长输入检索、要么依赖工具使用、要么仅覆盖短推理链，无法单独分离出大模型本身的长程思维链推理能力缺陷，阻碍该方向技术迭代。
**核心创新**: 提出首个专门针对长程思维链推理的标准化基准LongCoT，通过将多个大模型可单独求解的子问题构造成带依赖的图结构问题，将难度完全聚焦于长程推理本身，排除领域知识、工具使用等混淆因素，可直接衡量长程推理核心能力。
**技术细节**: LongCoT包含2500道专家设计问题，覆盖数学、化学、计算机科学、国际象棋、逻辑5个领域，分为两种构造模式：显式组合模板直接给出子问题依赖图，后续输入依赖前序结果；隐式过程模板仅给规则，需要模型自行探索隐含依赖。问题分三档，500道Easy题组成LongCoT-mini适配中小模型，所有结果可自动验证。
**实验结果**: 在全基准测试8款当前前沿大模型，最强的GPT 5.2仅达到9.83%准确率，Gemini 3 Pro仅为6.08%，准确率随问题长度下降远快于独立误差预期，证明现有大模型长程推理存在本质缺陷，引入代码工具后组合类问题准确率仍接近零。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Correct Prediction, Wrong Steps? Consensus Reasoning Knowledge Graph for Robust ...](http://arxiv.org/abs/2604.14121v1) `cs.CL (计算语言学)` | 针对LLM思维链推理存在步骤逻辑错误、幻觉等缺陷，提出基于共识推理知识图谱的鲁棒CoT生成方法，有效提升了LLM推理可靠性 |
| 5 | [HiVLA: A Visual-Grounded-Centric Hierarchical Embodied Manipulation System](http://arxiv.org/abs/2604.14125v1) `cs.CV (计算机视觉)` | 针对端到端VLA模型微调后丢失通用推理能力的痛点，提出以视觉 grounding 为中心的层级化具身操纵系统，提升了机器人操纵的综合性能 |
| 6 | [How Can We Synthesize High-Quality Pretraining Data? A Systematic Study of Promp...](http://arxiv.org/abs/2604.13977v1) `cs.CL (计算语言学)` | 针对LLM预训练合成数据设计缺乏系统对比的问题，系统梳理了三个核心维度对数据质量的影响，对大模型预训练实践有很高参考价值 |
| 7 | [CollabCoder: Plan-Code Co-Evolution via Collaborative Decision-Making for Effici...](http://arxiv.org/abs/2604.13946v1) `cs.SE (软件工程)` | 针对现有多代理代码生成存在静态规划、效率偏低的问题，提出规划-代码协同进化的协作框架，有效提升自动代码生成的效率和质量 |
| 8 | [From Weights to Activations: Is Steering the Next Frontier of Adaptation?](http://arxiv.org/abs/2604.14090v1) `cs.CL (计算语言学)` | 梳理现有大模型后训练适配范式，提出激活引导可能是大模型适配的下一个前沿方向，启发了该领域新的研究思路 |
| 9 | [Reward Design for Physical Reasoning in Vision-Language Models](http://arxiv.org/abs/2604.13993v1) `cs.AI (人工智能)` | 针对当前多模态大模型物理推理能力不足的核心痛点，针对性设计了专用奖励机制，有效提升了VLM的多步物理推理性能 |
| 10 | [[Emerging Ideas] Artificial Tripartite Intelligence: A Bio-Inspired, Sensor-Firs...](http://arxiv.org/abs/2604.13959v1) `cs.AI (人工智能)` | 针对物理AI面临的延迟、能耗、可靠性约束，提出生物启发的传感器优先新架构，开辟了物理AI领域的新研究方向 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-16
