# 🧪 ArXiv AI 日报

📅 **2026-03-27 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **58,741** (¥0.0192)

## 🔥 今日必读

---

### 1. Training the Knowledge Base through Evidence Distillation and Write-Back Enrichment

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.25737v1)

👤 Yuxing Lu, Xukai Zhao, Wei Wu 等


**中文标题**: 通过证据蒸馏与回写增强训练知识库

**背景与痛点**: 当前检索增强生成（RAG）研究大多聚焦优化检索器和生成器，始终将知识库视为固定输入。原始知识库中查询所需的事实往往分散在多个文档、夹杂大量无关噪声，导致检索上下文不完整且被稀释。现有上下文优化方法都在推理时单次运行，知识增益无法累积复用。

**核心创新**: 首次提出将RAG的知识库作为可训练组件优化，而非固定输入。提出WRITEBACK-RAG框架，利用标注样本挖掘检索行为中的知识缺口，将分散有效证据蒸馏为通用知识单元后回写增广知识库，作为一次性离线步骤，可兼容任意现有RAG pipeline，不增加推理开销。

**技术细节**: 离线训练采用两级门控筛选：效用门在样本层筛选出检索能带来明确增益、且回答正确的训练样本；文档门在文档层筛选出对回答有实质贡献的证据片段，过滤噪声。之后用大模型将分散证据融合压缩为百科风格的通用紧凑知识单元，不暴露金标避免答案泄漏，单独构建回写索引。推理时检索同时覆盖原始库与回写库，无需修改原有逻辑。

**实验结果**: 在6个主流知识任务基准、4种RAG方法、2种大语言模型主干上验证，所有48个测试设置均获得性能提升，平均绝对增益达2.14%。跨方法迁移实验证实，回写知识可跨RAG复用，增益确实来自知识库本身的优化。

---

### 2. S2D2: Fast Decoding for Diffusion LLMs via Training-Free Self-Speculation

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.25702v1)

👤 Ligong Han, Hao Wang, Han Gao 等


**中文标题**: S2D2：面向扩散大语言模型的无训练自投机快速解码

**背景与痛点**: 块扩散大语言模型通过块内并行去噪获得比自回归更快的生成速度，但在实际加速需要的少去噪步场景下，主流的置信度阈值解码非常脆弱：激进阈值会严重损失生成质量，保守阈值仍会带来不必要的计算开销，现有改进方案要么需要额外训练，要么会增加推理时的额外计算量。

**核心创新**: 利用块扩散模型本身的结构特性——将块大小缩小到1时模型天然退化为自回归模型，因此同一个预训练模型可以同时充当投机解码的草稿器和验证器，实现了完全无训练、无需额外模型的自投机解码框架，仅靠推理时的策略调整就提升了速度与质量的平衡。

**技术细节**: 每个去噪步先由标准块扩散模式生成草稿token和对应概率，然后通过轻量路由策略判断是否值得启动验证，路由支持最小跨度、分数阈值、迟滞等多种规则，仅对第一个连续待解码mask区间做验证；通过构造特殊的验证注意力掩码，一次前向就能算出所有位置的自回归验证概率，再按标准投机采样规则接受token，遇到拒绝则重采样后回到标准扩散流程，无需额外训练即可适配现有块扩散模型。

**实验结果**: 在GSM8K数学推理、MBPP/HumanEval代码生成、IFEval指令跟随多个基准测试了3个主流块扩散家族共5个模型，SDAR上最高获得相对于自回归4.7倍加速，比调优后的动态基线快1.57倍同时准确率提升4.5个点；LLaDA2.1上可获得相对于静态基线4.4倍加速，准确率还略高， consistently提升了速度精度边界。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Back to Basics: Revisiting ASR in the Age of Voice Agents](http://arxiv.org/abs/2603.25727v1) `cs.AI (人工智能)` | 当前语音Agent落地中ASR在真实场景失败率高，现有评测未覆盖该问题，该文重新系统梳理ASR痛点，对语音Agent工程落地有重要指导意义 |
| 5 | [PackForcing: Short Video Training Suffices for Long Video Sampling and Long Cont...](http://arxiv.org/abs/2603.25730v1) `cs.CV (计算机视觉)` | 针对自回归视频扩散模型长生成时KV缓存膨胀、时序重复、误差累积的痛点，提出短视频训练适配长视频推理，大幅降低长视频生成瓶颈 |
| 6 | [Drive My Way: Preference Alignment of Vision-Language-Action Model for Personali...](http://arxiv.org/abs/2603.25740v1) `cs.RO (机器人)` | 针对现有端到端自动驾驶模型无法适配不同用户个性化驾驶习惯的痛点，对视觉语言动作模型做偏好对齐，支持个性化驾驶，落地价值高 |
| 7 | [Natural-Language Agent Harnesses](http://arxiv.org/abs/2603.25723v1) `cs.CL (计算语言学)` | 当前Agent开发中harness设计分散在业务代码，难以迁移和对比，该文提出标准化的Agent harness框架，极大便利Agent的开发与迭代 |
| 8 | [Revisiting On-Policy Distillation: Empirical Failure Modes and Simple Fixes](http://arxiv.org/abs/2603.25562v1) `cs.LG (机器学习)` | 针对LLM后训练常用的在线策略蒸馏在长视野任务中的失效问题，实证分析失败模式并给出简单修复方案，大幅降低LLM后训练成本，实用性强 |
| 9 | [R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning](http://arxiv.org/abs/2603.25720v1) `cs.AI (人工智能)` | 针对当前多模态模型常出现跨模态预测矛盾的问题，提出循环一致强化学习框架，有效提升多模态推理的鲁棒性与一致性 |
| 10 | [Are LLMs Overkill for Databases?: A Study on the Finiteness of SQL](http://arxiv.org/abs/2603.25568v1) `cs.DB` | 针对当前NL2SQL领域过度依赖大参数LLM的现状，研究SQL问题的有限性，探讨小模型的可行性，对降低数据库应用成本有重要启发 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-27
