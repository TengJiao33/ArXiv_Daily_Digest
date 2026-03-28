# 🧪 ArXiv AI 日报

📅 **2026-03-28 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **45,859** (¥0.0151)

## 🔥 今日必读

---

### 1. Training the Knowledge Base through Evidence Distillation and Write-Back Enrichment

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.25737v1)

👤 Yuxing Lu, Xukai Zhao, Wei Wu 等


**中文标题**: 通过证据蒸馏与回写增强训练知识库（WRITEBACK-RAG）
**背景与痛点**: 当前检索增强生成（RAG）研究普遍聚焦优化检索器与生成器，将知识库视为一次性建好就固定不变的输入，不会根据下游任务信号调整。但实际查询所需知识往往分散在多个原始文档中，还被大量无关内容稀释，导致检索出的上下文不完整、质量低，限制了RAG的最终效果。
**核心创新**: 提出将知识库本身作为可训练组件的新思路，推出WRITEBACK-RAG框架：利用标注样本的RAG检索行为挖掘现有知识库的知识组织缺陷，将分散的有效证据蒸馏为紧凑通用知识单元回写增广知识库。该方法仅修改知识库，不改动原有RAG组件，无推理额外开销，可兼容任意现有RAG pipeline。
**技术细节**: 该方法为一次性离线预训练流程：首先通过两阶段门控筛选有效证据：效用门在样本层面筛选出检索确实能提升生成质量的样本，要求RAG得分减无检索得分大于阈值，且RAG绝对得分达标；文档门在样本内筛选出单独就能贡献正向收益的文档。之后调用大语言模型将筛选出的分散证据融合压缩为通用、紧凑的百科风格知识单元，写入独立的回写索引，推理阶段检索器同时检索原始库与回写库，原有RAG流程无需改动。
**实验结果**: 在6个覆盖不同知识任务的基准数据集、4种主流RAG方法、2个大语言模型主干上开展评测，所有设置均获得正向提升，平均绝对增益达2.14%。跨方法迁移实验验证了回写知识的通用性，对不同RAG pipeline均有增益。

---

### 2. Drive My Way: Preference Alignment of Vision-Language-Action Model for Personalized Driving

🏷️ `cs.RO (机器人)` | 📄 [arXiv](http://arxiv.org/abs/2603.25740v1)

👤 Zehao Wang, Huaide Jiang, Shuaiwu Dong 等


**中文标题**: 开我的车：面向个性化驾驶的视觉-语言-动作模型偏好对齐
**背景与痛点**: 现有端到端自动驾驶大多优化通用安全效率目标，仅提供少数固定驾驶模式，既无法捕捉用户差异化的长期驾驶习惯，也不能解读自然语言表达的实时个性化意图；已有个性化方法要么不支持自然语言交互，要么对新用户泛化能力差，难以适配动态复杂场景。
**核心创新**: 提出DMW个性化自动驾驶框架，首次同时实现用户长期驾驶习惯对齐与实时自然语言指令适配，还构建了首个包含30位不同背景驾驶员的多模态个性化驾驶数据集PDD，填补了该领域的研究数据空白，推动以人为中心的自动驾驶发展。
**技术细节**: 以SimLingo作为VLA骨干，通过对比学习对齐用户文本档案编码得到的长期偏好嵌入与实际驾驶轨迹编码的行为嵌入；新增可学习残差解码器对骨干输出的基础动作做个性化调整，采用GRPO做强化微调，基于大语言推理生成动态奖励权重，平衡安全、效率与舒适度，适配不同风格指令。
**实验结果**: 在Bench2Drive基准完成闭环测试，DMW对风格指令的适配能力显著优于SimLingo、StyleDrive等基线，对未见驾驶员的长期偏好对齐准确率达83%，远高于传统多目标强化学习方法，用户平均相似度评分达8分，同时保持了合格的安全驾驶性能。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation](http://arxiv.org/abs/2603.25702v1) `cs.CL (计算语言学)` | 解决扩散大语言模型生成速度慢的核心痛点，提出训练-free的自投机解码方案，实现扩散LLM的快速推理，对扩散大模型落地有重要实用价值。 |
| 5 | [PackForcing: Short Video Training Suffices for Long Video Sampling and Long Cont...](http://arxiv.org/abs/2603.25730v1) `cs.CV (计算机视觉)` | 解决自回归视频扩散模型长生成时KV缓存爆炸、时序重复、误差累积的痛点，仅需短视频训练即可支持长上下文推理，大幅降低长视频生成成本。 |
| 6 | [Back to Basics: Revisiting ASR in the Age of Voice Agents](http://arxiv.org/abs/2603.25727v1) `cs.AI (人工智能)` | 当前语音Agent落地中ASR在真实复杂场景泛化性差，现有基准未系统覆盖该问题，本文重新梳理ASR痛点，对语音Agent落地有重要指导意义。 |
| 7 | [Natural-Language Agent Harnesses](http://arxiv.org/abs/2603.25723v1) `cs.CL (计算语言学)` | 当前Agent的harness工程深度耦合在业务代码中，难以复用、对比和跨平台迁移，本文提出标准化框架，推动Agent工程的标准化发展。 |
| 8 | [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](http://arxiv.org/abs/2603.25562v1) `cs.LG (机器学习)` | 针对LLM后训练常用的在线策略蒸馏，系统分析了长任务中的常见失败模式，提出简单有效的修复方案，对LLM对齐落地有很高参考价值。 |
| 9 | [R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning](http://arxiv.org/abs/2603.25720v1) `cs.AI (人工智能)` | 解决当前多模态模型不同模态预测经常矛盾不一致的问题，提出循环一致强化学习框架，有效提升多模态推理的鲁棒性，研究方向前沿。 |
| 10 | [Is Mathematical Problem-Solving Expertise in Large Language Models Associated wi...](http://arxiv.org/abs/2603.25633v1) `cs.AI (人工智能)` | 针对LLM在数学教育中的应用痛点，厘清了LLM自身数学解题能力和对学习者推理评估表现的关联，为教育AI落地提供了关键实证依据。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-28
