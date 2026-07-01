# llm-truthfulness — 2026-W21 (05/18-05/24)

本周新增 **25** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 25。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [APCD: Adaptive Path-Contrastive Decoding for Reliable Large Lang...](http://arxiv.org/abs/2605.09492) | 大模型解码优化 | APCD通过熵判定预测不确定性决定分支时机，随预测分布散度增大动态衰减路径间影响，兼顾准确率... | — | — | ✅ |
| 2 | low | - | [A Comparative Study of Language Models for Khmer Retrieval-Augme...](http://arxiv.org/abs/2605.22099v1) | 检索增强问答 | BGE-M3嵌入模型Hit Rate@3达0.285，性能最优，检索器选择是高棉语RAG主要... | — | — | — |
| 3 | low | - | [ACL-Verbatim: hallucination-free question answering for research](http://arxiv.org/abs/2605.21102v1) | 无幻觉研究问答 | 150M参数的ModernBERT token分类器词级F1达53.6，优于最强对比LLM抽... | — | — | — |
| 4 | low | - | [AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowledge-I...](http://arxiv.org/abs/2605.17352v1) | 知识密集型问答 | AMATA在五个知识密集型QA基准上持续优于各类对比方法，同时能够有效减少模型的token消... | — | — | — |
| 5 | low | - | [Architecture, Not Scale: Circuit Localization in Large Language ...](http://arxiv.org/abs/2605.08853) | 机械可解释性 | 同规模下分组查询注意力的电路比标准多头更集中稳定；Qwen2.5事实回忆电路过临界规模后坍缩... | — | — | — |
| 6 | low | - | [Assisted Counterspeech Writing at the Crossroads of Hate Speech ...](http://arxiv.org/abs/2605.22435v1) | 辅助对抗话语生成 | 大语言模型生成的对抗话语仅40%合格，结合多源知识的混合策略效果最优，专家编辑可大幅提升生成... | — | — | — |
| 7 | low | - | [ConflictRAG: Detecting and Resolving Knowledge Conflicts in Retr...](http://arxiv.org/abs/2605.17301v1) | RAG知识冲突处理 | 该框架冲突检测F1达88.7%，相对最强基线正确性提升5.3-6.1%，降62%API成本仍... | — | — | — |
| 8 | low | - | [Do Factual Recall Mechanisms Carry over from Text to Speech in M...](http://arxiv.org/abs/2605.22170v1) | 事实回忆迁移 | 基于集成离散语音标记的SpiritLM发现，文到文与语音到文本结果存在差异，事实回忆机制仅部... | — | — | — |
| 9 | low | - | [Dual-Pathway Circuits of Object Hallucination in Vision-Language...](http://arxiv.org/abs/2605.13156) | 幻觉回路分析 | 抑制幻觉通路成分最多可减少76%物体幻觉且精度损失极小，该回路选择性转移至关系而非属性幻觉 | — | — | — |
| 10 | low | - | [FedSDR: Federated Self-Distillation with Rectification](http://arxiv.org/abs/2605.18028v1) | 联邦自蒸馏 | 发现无约束自蒸馏存在重写悖论，会增加幻觉与冗余，双分支选择性聚合可得到全局对齐的忠实模型 | — | — | — |
| 11 | low | - | [Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v2) | 法律RAG基准 | 当前最优的法律RAG系统，在检索、生成和主张级分析三个方面均存在明显局限性 | — | — | — |
| 12 | low | - | [HalluScore: Large Language Model Hallucination Question Answerin...](http://arxiv.org/abs/2605.17007v1) | 幻觉评测基准 | 阿拉伯语大语言模型的幻觉不止事实不准确，还存在文化理解、语言推理、逻辑一致性挑战 | — | — | — |

## 方法族分布

- **大模型幻觉检测**：2 篇
- **思维链忠实性**：1 篇
- **机械可解释性**：1 篇
- **知识时间漂移**：1 篇
- **幻觉回路分析**：1 篇
- **大模型解码优化**：1 篇
- **大模型劝说机制**：1 篇
- **事实回忆缩放规律**：1 篇
- **跨层幻觉校正**：1 篇
- **联邦自蒸馏**：1 篇
- **RAG预测预取**：1 篇
- **临床文本评估**：1 篇

## 代码资源

- [APCD: Adaptive Path-Contrastive Decoding for Reliable Large Language Model Gener...](https://github.com/zty-king/APCD.) · 2 stars

## 常见基线方法

- **SAPLMA**：2 篇
- **Qwen2.5**：1 篇
- **DeepSeek-R1-Distill**：1 篇
- **标准多头注意力**：1 篇
- **token熵**：1 篇
- **语义熵**：1 篇
- **CCS**：1 篇
- **ReDeEP**：1 篇
- **传统算法**：1 篇
- **同步RAG**：1 篇

## 常用数据集

- **七个推理基准**：1 篇
- **RAGTruth**：1 篇
- **LLM-AggreFact**：1 篇
- **POPE-adversarial**：1 篇
- **AMBER**：1 篇
- **八个评测基准**：1 篇
- **多个基准数据集**：1 篇
- **MIMIC**：1 篇
- **五个已建立知识密集型QA基准**：1 篇
- **三个基准数据集，未提及具体名称**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*