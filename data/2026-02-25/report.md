# 🧪 ArXiv AI 日报

📅 **2026-02-25 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **66,301** (¥0.0215)

## 🔥 今日必读

---

### 1. Aletheia tackles FirstProof autonomously

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2602.21201v1) | 💻 [GitHub](https://github.com/google-deepmind/superhuman) ⭐540

👤 Tony Feng, Junehyuk Jung, Sang-hyun Kim 等


**中文标题**: Aletheia自主攻克FirstProof测评
**背景与痛点**: FirstProof是职业数学家提出的10道原创研究级数学开放问题，用于测评AI解决真实前沿数学问题的自主能力。此前AI解决开放数学问题大多依赖人类专家在回路中提供思路、修正内容，鲜有符合规则的全自主解题验证实践。
**核心创新**: 本文验证了Google DeepMind开发的、基于Gemini 3 Deep Think的自主数学智能体Aletheia的前沿解题能力，严格遵守FirstProof对自主性的最高要求，全程无人类提供数学内容或修正，自动生成符合学术出版标准的完整证明，同时公开全部原始交互保证可验证性。
**技术细节**: Aletheia采用生成+验证的双智能体架构，直接输入未修改的FirstProof原始问题文本；验证环节用预定义prompt让大模型自主检查候选证明的逻辑漏洞、修正格式，直接输出符合学术规范的LaTeX代码。智能体优先保障可靠性，无解时会主动输出“未找到解”，实验采用best-of-2策略从两个不同基模型的结果中选最优，仅最终评估环节人类介入，不修改模型输出内容。
**实验结果**: 在FirstProof的10道研究级问题上，经独立数学专家评估，Aletheia自主正确解决了6道问题，仅第8题未达成一致评估（5/7专家认为正确）。所有结果在官方截止前提交，不存在数据泄露，证明大模型智能体已经具备解决部分前沿开放数学问题的能力。

---

### 2. Untied Ulysses: Memory-Efficient Context Parallelism via Headwise Chunking

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.21196v1)

👤 Ravi Ghadia, Maksim Abraham, Sergei Vorobyov 等


**中文标题**: 解开的尤利西斯：基于头分块的内存高效上下文并行

**背景与痛点**: 当前长上下文大模型训练普遍依赖上下文并行技术，主流方案如DeepSpeed Ulysses、Ring Attention未优化注意力阶段的中间激活内存，内存开销随序列长度线性增长，无法支持超百万级长序列；现有内存优化方案如FPDT依赖CPU卸载，会大幅降低训练吞吐量，ALST等方案未解决注意力层的内存瓶颈。

**核心创新**: 本文提出UPipe（Untied Ulysses）方法，核心洞察是长序列训练下仅处理部分注意力头即可占满GPU计算资源，因此通过头维度分块串行执行注意力，复用内存缓冲区，相比现有沿序列分块的方案，能在不损失吞吐量的前提下大幅降低注意力层峰值内存，还适配了现代大模型常用的分组查询注意力（GQA）。

**技术细节**: UPipe基于DeepSpeed Ulysses改造，将全部注意力头拆分为多个块，每个阶段仅处理一个块的注意力，处理完成后复用QKV和all-to-all通信缓冲区，峰值内存从与总头数成正比降为与单次处理头数成正比，最小可降至与上下文并行设备数相等。针对GQA设计特殊调度：第一阶段通信所有唯一KV头，后续阶段仅通信对应查询头，避免冗余通信，可即插即用适配现有训练流程。

**实验结果**: 在Llama3-8B、Qwen3-32B上测试，单8卡H100节点训练Llama3-8B可支持500万token上下文长度，相比前代SOTA提升25%；对32B模型可降低最多87.5%的注意力层中间激活内存，训练吞吐量和主流Ulysses方案基本持平。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Test-Time Training with KV Binding Is Secretly Linear Attention](http://arxiv.org/abs/2602.21204v1) `cs.LG (机器学习)` | 重新分析了带KV绑定的测试时训练，修正了其为在线元学习的原有认知，证明其本质是线性注意力，为测试时自适应方法提供了全新理论理解 |
| 5 | [Prompt-Level Distillation: A Non-Parametric Alternative to Model Fine-Tuning for...](http://arxiv.org/abs/2602.21103v1) `cs.CL (计算语言学)` | 针对思维链推理成本高、微调小模型损失精度的痛点，提出非参数的prompt级蒸馏方案，无需微调即可实现高效推理，适配落地需求 |
| 6 | [Scaling State-Space Models on Multiple GPUs with Tensor Parallelism](http://arxiv.org/abs/2602.21144v1) `cs.DC` | 针对热门长上下文 backbone 选择性状态空间模型（SSM）多GPU部署推理性能差的问题，提出适配的张量并行扩展方法，助力SSM规模化落地 |
| 7 | [SELAUR: Self Evolving LLM Agent via Uncertainty-aware Rewards](http://arxiv.org/abs/2602.21158v1) `cs.LG (机器学习)` | 针对LLM多步决策Agent的奖励设计痛点，提出基于不确定性感知奖励的LLM Agent自进化框架，推动Agent自主迭代优化方向发展 |
| 8 | [Multi-Vector Index Compression in Any Modality](http://arxiv.org/abs/2602.21202v1) `cs.IR` | 面向任意模态迟交互多向量检索的效率痛点，研究了多向量索引压缩方案，提升多模态检索的效率，对多模态RAG落地有重要实用价值 |
| 9 | [VAUQ: Vision-Aware Uncertainty Quantification for LVLM Self-Evaluation](http://arxiv.org/abs/2602.21054v1) `cs.CV (计算机视觉)` | 针对大视觉语言模型的幻觉问题，提出视觉感知的不确定性量化方法，实现LVLM的自我评估，提升多模态模型落地的安全性 |
| 10 | [Tool Building as a Path to "Superintelligence"](http://arxiv.org/abs/2602.21061v1) `cs.AI (人工智能)` | 围绕LLM通过工具构建实现能力扩展的前沿路线，设计了衡量步骤成功率的基准，为探索LLM自主进化路线提供了核心评测基础 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-25
