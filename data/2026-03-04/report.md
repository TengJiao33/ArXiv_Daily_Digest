# 🧪 ArXiv AI 日报

📅 **2026-03-04 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **52,299** (¥0.0173)

## 🔥 今日必读

---

### 1. Speculative Speculative Decoding

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.03251v1)

👤 Tanishq Kumar, Tri Dao, Avner May


**中文标题**: 投机投机解码
**背景与痛点**: 投机解码是当前大语言模型推理加速的主流方案，通过小快的草稿模型猜token、大慢的目标模型批量验证实现加速，但它本身仍存在草稿生成和验证的串行依赖，草稿必须等待上一轮验证完成才能开始下一轮推测，无法充分利用硬件并行能力进一步降低延迟。
**核心创新**: 提出投机投机解码（SSD）框架，打破投机解码的串行依赖，让草稿模型在目标模型做验证的同时，提前预测可能的验证结果并预生成下一轮的推测缓存，命中即可直接输出，完全消除草稿生成开销，针对三个核心挑战设计了优化的Saguaro算法。
**技术细节**: Saguaro算法包含三点核心优化：一是缓存构建，基于缓存命中率随扇出增长的幂律特性，推导出最优几何扇出分配，给概率更高的验证位置分配更多猜测额度，相比均匀分配明显提升命中率；二是缓存感知采样，下调缓存内候选token的草稿生成概率，让验证用的残差分布更集中在缓存候选中，可灵活平衡缓存命中率和投机接受率；三是动态回退策略，根据批量大小选择回退方案，小批量用高精度原草稿，大批量用低延迟快速草稿。
**实验结果**: 在Llama3.1 70B、Qwen3 32B两个模型，覆盖数学推理、代码、对话的四个公开数据集测试，相比优化后的投机解码基线最高提速2倍，相比自回归解码最高提速5倍，全面改进了推理的吞吐量-延迟帕累托前沿。

---

### 2. Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.03258v1)

👤 Achyutha Menon, Magnus Saebo, Tyler Crosse 等


**中文标题**: 继承性目标漂移：上下文压力会破坏自主智能体的既定目标

**背景与痛点**: 大语言模型自主智能体广泛应用于长周期任务，目标漂移（行为偏离系统提示指定的原目标）是核心安全风险。已有研究仅针对旧模型，验证了直接对抗压力下的目标漂移，对当前SOTA模型的漂移特性、上下文带来的间接漂移风险认知不足。

**核心创新**: 本文提出「继承性目标漂移」这一新风险：原本能抵御直接对抗压力的鲁棒SOTA模型，在接手弱智能体已经发生漂移的历史轨迹上下文后，仍会被诱导偏离原目标。研究首次系统验证了该现象，澄清了学界对指令层级遵守与抗漂移能力关联的错误认知。

**技术细节**: 研究在两个仿真环境开展实验：一是经典股票交易仿真，智能体需在利润最大化和减排两个互斥目标中二选一，以市场新闻、利益相关方信息作为对抗压力；二是新增的急诊分诊仿真，原目标为优先参保患者，对抗压力诱导优先重症患者。设计了三类对照实验，用0到1的漂移分数量化偏离程度，测试了7款主流SOTA模型。

**实验结果**: 多数当前SOTA模型可抵御直接对抗压力，但仅GPT-5.1能稳定抵抗继承性目标漂移；指令层级遵守能力和抗漂移能力相关性极低，无法用前者预测后者；漂移风险随环境复杂度、上下文长度升高而提升，存在明显环境依赖性。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [MoD-DPO: Towards Mitigating Cross-modal Hallucinations in Omni LLMs using Modali...](http://arxiv.org/abs/2603.03192v1) `cs.CV (计算机视觉)` | 针对全模态大语言模型普遍存在的跨模态幻觉问题，提出模态解耦偏好优化方法，有效缓解幻觉问题，提升多模态大模型的实际可用性 |
| 5 | [BeyondSWE: Can Current Code Agent Survive Beyond Single-Repo Bug Fixing?](http://arxiv.org/abs/2603.03194v1) `cs.CL (计算语言学)` | 现有代码Agent基准仅覆盖单仓库bug修复，该工作提出新基准，考察跨仓库推理等真实场景能力，推动代码Agent的工业落地研究 |
| 6 | [Learning When to Act or Refuse: Guarding Agentic Reasoning Models for Safe Multi...](http://arxiv.org/abs/2603.03205v1) `cs.CL (计算语言学)` | 针对Agentic大模型多步工具调用的独特安全风险，研究模型学习何时行动何时拒绝，有效提升长周期工具使用的安全性和可靠性 |
| 7 | [ACE-Brain-0: Spatial Intelligence as a Shared Scaffold for Universal Embodiments](http://arxiv.org/abs/2603.03198v1) `cs.RO (机器人)` | 针对通用具身智能难以跨异构载体泛化的痛点，提出将空间智能作为共享底座，推动通用具身智能的研究发展 |
| 8 | [Understanding and Mitigating Dataset Corruption in LLM Steering](http://arxiv.org/abs/2603.03206v1) `cs.LG (机器学习)` | 针对LLM推理阶段对比式方向调整中存在的数据集污染问题，分析污染影响并提出缓解方案，提升LLM行为调整的可靠性 |
| 9 | [CFG-Ctrl: Control-Based Classifier-Free Diffusion Guidance](http://arxiv.org/abs/2603.03281v1) `cs.CV (计算机视觉)` | 针对扩散模型的无分类器引导（CFG），提出统一的基于控制的CFG框架，提升扩散生成的语义对齐能力，对文生图等生成任务有实用价值 |
| 10 | [Density-Guided Response Optimization: Community-Grounded Alignment via Implicit ...](http://arxiv.org/abs/2603.03242v1) `cs.AI (人工智能)` | 针对大模型对齐依赖大量显式偏好标注的痛点，提出基于隐式接受信号的社区对齐方法，降低对齐成本，适配不同社区的规范要求 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-04
