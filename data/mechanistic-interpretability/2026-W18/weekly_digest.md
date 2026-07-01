# mechanistic-interpretability — 2026-W18 (04/27-05/03)

本周新增 **11** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 11。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Differentiable Faithfulness Alignment for Cross-Model Circuit Tr...](http://arxiv.org/abs/2604.24302v1) | 跨模型电路迁移 | Llama-3 1B→3B迁移中对齐电路可媲美直接节点归因，模型与架构差异越大迁移效果越差 | — | — | ✅ |
| 2 | low | - | [A Unifying Framework for Unsupervised Concept Extraction](http://arxiv.org/abs/2604.24936v1) | 无监督概念提取 | 该元定理将可识别性保证证明转化为刻画两个集合交集的问题，可大幅简化各类常用方法的证明工作 | — | — | — |
| 3 | low | - | [AIPsy-Affect: A Keyword-Free Clinical Stimulus Battery for Mecha...](http://arxiv.org/abs/2604.23719v1) | 情绪可解释性 | 语境分类器可检测该库中情绪存在（p<10^-15），类别识别top-1准确率仅5.2%，远低... | — | — | — |
| 4 | low | - | [Do Sparse Autoencoders Capture Concept Manifolds?](http://arxiv.org/abs/2604.28119v1) | 概念流形捕捉 | 稀疏自编码器可通过全局子空间、局部分块两种方式捕捉流形，现有SAE混合二者得到碎片化稀释结果 | — | — | — |
| 5 | low | - | [Domain-Filtered Knowledge Graphs from Sparse Autoencoder Feature...](http://arxiv.org/abs/2604.23829v1) | 知识图谱构建 | 在生物学教科书案例中，该方法还原连贯章、子章结构，揭示跨主题概念，得到模型活动紧凑可读视图 | — | — | — |
| 6 | low | - | [From Insight to Action: A Novel Framework for Interpretability-G...](http://arxiv.org/abs/2604.25167v1) | 可解释性数据选择 | Gemma-2-2B数学任务中IGDS仅用50%数据，效果超出全数据微调17.4%，特征放大... | — | — | — |
| 7 | low | - | [From Syntax to Emotion: A Mechanistic Analysis of Emotion Infere...](http://arxiv.org/abs/2604.25866v1) | 情绪推理机制 | 大语言模型情绪推理存在一致三阶段信息流，厌恶情绪比其他情绪表征更微弱更分散 | — | — | — |
| 8 | low | - | [Learning biophysical models of gene regulation with probability ...](http://arxiv.org/abs/2604.25062v1) | 基因调控建模 | 相同插值精度的模型可编码根本不同的动力学，仅符合生物物理的模型能准确捕获谱系转换，PFM可同... | — | — | — |
| 9 | low | - | [MoRFI: Monotonic Sparse Autoencoder Feature Identification](http://arxiv.org/abs/2604.26866v1) | 大模型幻觉机制 | 逐步引入新知识会提升幻觉程度，训练越久效应越显著，未知事实会沿残差流特定方向破坏已有知识检索 | — | — | — |
| 10 | low | - | [Preference Heads in Large Language Models: A Mechanistic Framewo...](http://arxiv.org/abs/2604.22345v1) | 可解释个性化 | 大语言模型中存在稀疏编码用户偏好的偏好注意力头，基于该机制可实现低开销无训练的可解释个性化 | — | — | — |
| 11 | low | - | [reward-lens: A Mechanistic Interpretability Library for Reward M...](http://arxiv.org/abs/2604.26130v1) | 奖励模型可解释性 | 线性归因无法预测因果打补丁效应，Skywork上平均斯皮尔曼ρ=-0.256，ArmoRM上... | — | — | — |

## 方法族分布

- **可解释个性化**：1 篇
- **跨模型电路迁移**：1 篇
- **知识图谱构建**：1 篇
- **情绪可解释性**：1 篇
- **情绪推理机制**：1 篇
- **可解释性数据选择**：1 篇
- **基因调控建模**：1 篇
- **无监督概念提取**：1 篇
- **大模型幻觉机制**：1 篇
- **奖励模型可解释性**：1 篇
- **概念流形捕捉**：1 篇

## 代码资源

- [Differentiable Faithfulness Alignment for Cross-Model Circuit Transfer](https://github.com/jasonshaoshun/dfa-circuits.)

## 常见基线方法

- **直接节点归因**：1 篇
- **简单基线**：1 篇
- **富关键词情绪刺激**：1 篇
- **原有96项刺激电池**：1 篇
- **面向数据质量的数据选择基线**：1 篇
- **面向数据多样性的数据选择基线**：1 篇
- **原有生成大模型可解释工具**：1 篇
- **线性归因方法**：1 篇

## 常用数据集

- **造血数据集**：3 篇
- **摘要未提及具体数据集**：1 篇
- **生物学教科书**：1 篇
- **AIPsy-Affect临床刺激库**：1 篇
- **多个情绪识别数据集**：1 篇
- **数学推理任务数据集**：1 篇
- **摘要任务数据集**：1 篇
- **翻译任务数据集**：1 篇
- **七个不同单QA数据集**：1 篇
- **RewardBench**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*