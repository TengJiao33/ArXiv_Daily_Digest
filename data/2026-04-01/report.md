# 🧪 ArXiv AI 日报

📅 **2026-04-01 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **40,555** (¥0.0138)

## 🔥 今日必读

---

### 1. Architecting Secure AI Agents: Perspectives on System-Level Defenses Against Indirect Prompt Injection Attacks

🏷️ `cs.CR (加密与安全)` | 📄 [arXiv](http://arxiv.org/abs/2603.30016v1)

👤 Chong Xiang, Drew Zagieboylo, Shaona Ghosh 等


**中文标题**: 构建安全AI智能体：抵御间接提示注入攻击的系统级防御视角
**背景与痛点**: 大语言模型驱动的自主AI智能体普遍面临嵌入在外部未信任数据中的间接提示注入攻击，现有系统级防御要么采用静态规划执行隔离，在动态环境中易失效、任务完成率低，要么未约束安全决策大语言模型的输入范围，容易被攻击者操控，现有基准设计缺陷还容易造成虚假安全感。
**核心创新**: 本文提出以系统级设计作为安全智能体的核心骨架，明确三大核心设计立场：动态场景必须支持安全感知的重规划与策略更新，必须在严格约束输入和决策范围的前提下使用大语言模型做安全决策，歧义场景必须将个性化与人机交互作为核心设计要素。
**技术细节**: 提出分层模块化安全架构：编排器基于用户任务生成初始执行规划和安全允许策略，经规划/策略审批者审核后交付执行器生成具体动作，策略执行器基于规则拦截违规动作，执行结果会反馈回编排器触发更新；核心安全约束要求大语言模型仅处理结构化窄范围输入，不直接接触原始未信任环境文本，预留人机审核节点解决语义和目标歧义。
**实验结果**: 本文为立场性研究，未开展端到端对比实验，核心结论指出现有安全基准普遍缺少需要重规划的动态复杂任务，仅使用静态攻击载荷，会高估防御方法的安全性与可用性，呼吁开发支持自适应攻击的动态评估基准。

---

### 2. Think Anywhere in Code Generation

🏷️ `cs.SE (软件工程)` | 📄 [arXiv](http://arxiv.org/abs/2603.29957v1)

👤 Xue Jiang, Tianyu Zhang, Ge Li 等


**中文标题**: 《代码生成中的任意位置推理》

**背景与痛点**: 当前主流大模型代码推理都采用前置推理范式，要求模型完成全部推理后再生成最终代码。但代码生成中问题复杂度往往在实现过程中才逐步暴露，前置推理经常因思考不足产生bug，也无法根据代码各位置的难度自适应分配推理算力。

**核心创新**: 提出THINK-ANYWHERE推理机制，允许大模型在代码生成过程中的任意token位置按需触发推理，打破了推理必须前置的范式限制，让模型可以把计算资源精准分配到真正需要深度思考的复杂位置，同时提升了模型决策过程的可解释性。

**技术细节**: 采用两阶段训练流程，首先冷启动阶段：用强推理大模型自动构造符合格式要求的训练样本，通过监督微调让模型学会在代码中插入推理块；为消除分隔符语义歧义，设计了带语义感知初始化的专用单触发token。第二阶段采用GRPO强化学习优化，设计包含格式合规性、代码正确性的分层奖励，驱动模型自主学习按需触发推理的策略，最终删除推理块即可得到可执行代码。

**实验结果**: 在HumanEval、MBPP、LeetCode、LiveCodeBench四个主流基准测试，相比基线模型平均pass@1提升9.3个百分点，达到SOTA性能，对不同大小、不同架构的大模型均有一致增益，总推理token开销反而低于传统前置推理方法，还可泛化到数学推理任务。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Aligned, Orthogonal or In-conflict: When can we safely optimize Chain-of-Thought...](http://arxiv.org/abs/2603.30036v1) `cs.LG (机器学习)` | 当前CoT推理优化方法众多，但缺乏对优化安全性和边界的系统性讨论，分析了不同场景下CoT优化与原任务的对齐冲突关系，对推理优化有重要指导意义。 |
| 5 | [Reward-Based Online LLM Routing via NeuralUCB](http://arxiv.org/abs/2603.30035v1) `cs.LG (机器学习)` | 针对大语言模型路由的成本控制需求，基于NeuralUCB提出奖励驱动的在线路由方案，解决现有方法依赖标注、反馈不足的问题，适合工业级大模型部署。 |
| 6 | [Tucker Attention: A generalization of approximate attention mechanisms](http://arxiv.org/abs/2603.30033v1) `cs.LG (机器学习)` | 针对自注意力机制内存开销过大的痛点，提出基于Tucker分解的广义近似注意力框架，统一了现有多种近似注意力方法，为大模型架构优化提供新思路。 |
| 7 | [Hybrid Framework for Robotic Manipulation: Integrating Reinforcement Learning an...](http://arxiv.org/abs/2603.30022v1) `cs.RO (机器人)` | 结合大语言模型的高层常识规划能力和强化学习的低层级精准控制能力，提出机器人操作的混合框架，解决纯LLM精度不足、纯RL泛化差的痛点，落地价值高。 |
| 8 | [ATP-Bench: Towards Agentic Tool Planning for MLLM Interleaved Generation](http://arxiv.org/abs/2603.29902v1) `cs.AI (人工智能)` | 面向多模态大模型交错图文生成场景中的智能体工具规划任务，提出首个专项基准ATP-Bench，填补了该前沿方向的基准空白，推动领域研究发展。 |
| 9 | [Curvature-Guided LoRA: Steering in the pretrained NTK subspace](http://arxiv.org/abs/2603.29824v1) `cs.LG (机器学习)` | 针对现有参数高效微调方法LoRA性能往往弱于全微调的问题，提出曲率引导的改进方案，在不增加参数量的前提下提升微调效果，实用性强。 |
| 10 | [ShapE-GRPO: Shapley-Enhanced Reward Allocation for Multi-Candidate LLM Training](http://arxiv.org/abs/2603.29871v1) `cs.AI (人工智能)` | 面向大语言模型多候选生成场景的训练需求，提出基于Shapley值的增强奖励分配方法，改进了多候选场景的训练效果，对RL类大模型训练有实用价值。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-01
