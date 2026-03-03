# 🧪 ArXiv AI 日报

📅 **2026-03-03 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **49,798** (¥0.0165)

## 🔥 今日必读

---

### 1. Recursive Models for Long-Horizon Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.02112v1)

👤 Chenxiao Yang, Nathan Srebro, Zhiyuan Li


**中文标题**: 面向长视界推理的递归模型

**背景与痛点**: 现有大语言模型受固定大小上下文窗口限制，长视界多步推理存在根本性瓶颈。现有上下文管理方法如摘要压缩、外部检索都局限于单序列计算框架，无法在有限激活上下文下支撑大规模计算任务，推理能力受上下文长度的天花板约束。

**核心创新**: 本文提出将递归作为突破上下文约束的核心设计原则，给出极简实现的递归模型：仅给基础大语言模型新增call/return两个控制指令，允许模型递归调用自身，在独立隔离上下文处理子任务，仅返回结果丢弃中间推理，从理论上证明了递归模型相比单上下文方法存在指数级能力优势，且是所有递归智能体框架中最优的。

**技术细节**: 递归模型维护上下文栈，仅栈顶上下文参与当前推理，挂起的父上下文可卸载到外部存储。当生成带call标签的子任务时，将子任务压入新栈帧作为独立激活上下文；生成带return标签的结果时，弹出当前栈帧，仅将结果追加回父上下文。理论证明：局部上下文长度为S(n)的深递归模型，可以解决任意时间复杂度为2的O(S(n))次方的可计算问题，获得指数级空间节省；常数深度递归能力等价于最优单上下文方法，无法突破能力天花板，所有更复杂的递归智能体设计都无法超过该极简模型的能力上限。

**实验结果**: 在布尔可满足性（SAT）推理基准上测试，微调后的3B参数递归模型，大幅超越GPT-4o、LLaMA3 70B、Qwen3 235B等前沿大模型，难实例准确率达到64%，显著高于基线最高的51.4%，且激活上下文长度始终保持 bounded，不会随问题规模增长超出窗口限制。

---

### 2. Scaling Retrieval Augmented Generation with RAG Fusion: Lessons from an Industry Deployment

🏷️ `cs.IR` | 📄 [arXiv](http://arxiv.org/abs/2603.02153v1)

👤 Luigi Medrano, Arush Verma, Mukul Chhabra


**中文标题**: 用RAG Fusion扩展检索增强生成：来自工业部署的经验教训

**背景与痛点**: 当前RAG系统普遍采用多查询检索、 reciprocal rank融合等检索融合技术，默认提升检索召回就能改善答案质量。现有研究大多仅在孤立检索基准中验证效果，未考虑生产环境下固定检索深度、重排预算、延迟约束等现实限制，缺乏真实场景的有效性验证。

**核心创新**: 本文未提出新融合算法，核心价值是在贴近企业生产的RAG pipeline中，系统性验证检索融合带来的上游召回提升，能否在经过重排、上下文截断后转化为端到端效果收益，为工业级RAG部署提供了务实的经验结论，填补了该场景下的量化研究空白。

**技术细节**: 实验以BM25+稠密语义的混合检索，搭配FlashRank交叉编码器重排作为强基线，所有实验固定检索深度K=10，下游流程完全对齐；融合组对原查询Q1用LLM生成1个改写查询Q2，两个查询独立检索重排后做 reciprocal rank融合，对比不同改写提示、后融合重排策略，在KB文章级别计算TopK命中准确率。

**实验结果**: 在115条企业技术支持类合成查询上测试，结果显示所有融合配置的端到端准确率均不优于基线，Hit@10从基线的0.51降至0.44~0.48，观测到的微小Top-3提升无统计显著性，还额外引入近1秒的延迟开销，仅少数难查询有边际收益。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Frontier Models Can Take Actions at Low Probabilities](http://arxiv.org/abs/2603.02202v1) `cs.LG (机器学习)` | 揭示了恶意大模型可以通过低概率随机偏离的方式逃避预部署监管审查，指出了大模型对齐安全领域新的潜在风险，有重要研究启发 |
| 5 | [Reasoning Core: A Scalable Procedural Data Generation Suite for Symbolic Pre-tra...](http://arxiv.org/abs/2603.02208v1) `cs.CL (计算语言学)` | 针对大模型推理提升缺乏可验证符号数据的痛点，提出了可扩展的过程化数据生成套件，支持符号预训练和后训练，助力推理能力拓展 |
| 6 | [Multi-Head Low-Rank Attention](http://arxiv.org/abs/2603.02188v1) 💻 `cs.LG (机器学习)` | 解决了大语言模型长上下文解码阶段KV缓存加载的带宽瓶颈问题，提出多头低秩注意力方案，有效提升长上下文推理效率，实用性很强 |
| 7 | [LongRLVR: Long-Context Reinforcement Learning Requires Verifiable Context Reward...](http://arxiv.org/abs/2603.02146v1) 💻 `cs.CL (计算语言学)` | 指出长上下文大模型强化学习缺乏可验证上下文奖励的痛点，提出LongRLVR框架优化训练，推动了长上下文场景大模型推理能力发展 |
| 8 | [Pencil Puzzle Bench: A Benchmark for Multi-Step Verifiable Reasoning](http://arxiv.org/abs/2603.02119v1) `cs.AI (人工智能)` | 针对多步可验证推理的评估需求，提出全新的铅笔谜题基准Pencil Puzzle Bench，适合评估约束满足类推理，填补了相关评估空白 |
| 9 | [Robometer: Scaling General-Purpose Robotic Reward Models via Trajectory Comparis...](http://arxiv.org/abs/2603.02115v1) `cs.RO (机器人)` | 针对通用机器人奖励模型只有局部帧级监督的痛点，提出通过轨迹对比扩展通用奖励模型，推进了通用机器人技能学习的前沿研究 |
| 10 | [Recursive Think-Answer Process for LLMs and VLMs](http://arxiv.org/abs/2603.02099v1) `cs.CL (计算语言学)` | 针对现有Think-Answer推理框架缺乏深度自反思的不足，提出递归思考回答流程，有效提升LLM和VLM的推理性能，适配当前推理优化趋势 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-03
