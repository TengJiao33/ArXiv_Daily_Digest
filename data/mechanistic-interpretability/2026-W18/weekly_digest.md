# 机械可解释性 — 2026-W18 (04/27-05/03)

本周新增 **11** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.CL`: 5 篇
- `cs.LG`: 3 篇
- `cs.AI`: 2 篇
- `q-bio.MN`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Preference Heads in Large Language Models: A Mechanistic Fra...](http://arxiv.org/abs/2604.22345v1) | 提出无训练的差分偏好引导（DPS）框架，经因果掩码分析识别偏好头以实现可解释个性... | 提升多个大语言模型的个性化保真度，保留内容连贯性，给出Transformer中个... | — |
| 2 | [Differentiable Faithfulness Alignment for Cross-Model Circui...](http://arxiv.org/abs/2604.24302v1) | 提出可微忠实对齐DFA框架，通过可微学习对齐将小源模型电路信息迁移到目标大模型 | 提出DFA框架，性能优于简单基线，部分场景下电路忠实度可媲美甚至超过直接归因 | ✅ |
| 3 | [Domain-Filtered Knowledge Graphs from Sparse Autoencoder Fea...](http://arxiv.org/abs/2604.23829v1) | 通过对比激活与多阶段过滤构建领域概念集，构建双对齐图视图，自动标注生成知识图谱 | 将扁平稀疏自编码器特征库转化为结构化知识图谱，可还原领域结构，支持模型知识审计 | — |
| 4 | [AIPsy-Affect: A Keyword-Free Clinical Stimulus Battery for M...](http://arxiv.org/abs/2604.23719v1) | 构建去除情绪关键词的配对临床情绪刺激库，采用三种NLP方法验证其无混淆特性 | 公开了MIT许可的480项无关键词情绪刺激库AIPsy-Affect，消除了刺激... | — |
| 5 | [From Syntax to Emotion: A Mechanistic Analysis of Emotion In...](http://arxiv.org/abs/2604.25866v1) | 利用稀疏自动编码器分析跨层特征激活，结合分阶段因果追踪，提出可解释因果特征引导方... | 系统分析大语言模型情绪识别内部机制，提出的方法可提升性能且泛化性良好 | — |
| 6 | [From Insight to Action: A Novel Framework for Interpretabili...](http://arxiv.org/abs/2604.25167v1) | 提出可解释性引导的数据选择框架IGDS，识别因果任务特征后选特征共振数据微调大模... | 在多模型多任务验证IGDS的优异数据效率，效果优于全数据微调和现有基线方法 | — |
| 7 | [Learning biophysical models of gene regulation with probabil...](http://arxiv.org/abs/2604.25062v1) | 提出可扩展的概率流匹配（PFM）框架，直接从时间分辨单细胞测量学习符合生物物理的... | 证明PFM可容纳不平衡细胞群，建立了整合机制建模与单细胞组学的灵活可扩展框架。 | — |
| 8 | [A Unifying Framework for Unsupervised Concept Extraction](http://arxiv.org/abs/2604.24936v1) | 构建无监督概念提取统一理论框架，将任务建模为生成模型识别，提出可识别性通用元定理 | 所提元定理大幅简化概念提取方法可识别性保证的证明工作，为新方法开发铺平道路 | — |
| 9 | [MoRFI: Monotonic Sparse Autoencoder Feature Identification](http://arxiv.org/abs/2604.26866v1) | 开展受控微调实验，利用预训练稀疏自编码器，提出MoRFI捕捉与幻觉因果相关的潜在... | 提出MoRFI方法，可跨不同模型可靠识别致幻潜在方向，可通过单潜在干预恢复模型知... | — |
| 10 | [reward-lens: A Mechanistic Interpretability Library for Rewa...](http://arxiv.org/abs/2604.26130v1) | 以奖励模型奖励头的权重向量为核心轴，移植原有机械可解释工具链构建开源工具库。 | 推出适配奖励模型的开源可解释库reward-lens，支持多款主流模型，完成相关... | — |
| 11 | [Do Sparse Autoencoders Capture Concept Manifolds?](http://arxiv.org/abs/2604.28119v1) | 构建分析稀疏自编码器捕捉概念流形的理论框架，并开展对应的实证分析 | 阐明稀疏自编码器捕捉流形的两种方式，发现现有SAE的稀释问题，指明可解释性研究新... | — |

## 常见基线方法

- **直接节点归因** (1 篇引用)
- **简单基线** (1 篇引用)
- **富关键词情绪刺激** (1 篇引用)
- **原有96项刺激电池** (1 篇引用)
- **面向数据质量的数据选择基线** (1 篇引用)
- **面向数据多样性的数据选择基线** (1 篇引用)
- **原有生成大模型可解释工具** (1 篇引用)
- **线性归因方法** (1 篇引用)

## 本周提到的 Limitations

- 源目标模型规模差距越大、架构差异越大，电路迁移效果越差，Qwen-2.5上恢复度较低
- 现有稀疏自编码器无法最优恢复连续流形结构，会得到碎片化的稀释结果

## 常用数据集

- **造血数据集** (3 篇使用)
- **摘要未提及具体数据集** (1 篇使用)
- **生物学教科书** (1 篇使用)
- **AIPsy-Affect临床刺激库** (1 篇使用)
- **多个情绪识别数据集** (1 篇使用)
- **数学推理任务数据集** (1 篇使用)
- **摘要任务数据集** (1 篇使用)
- **翻译任务数据集** (1 篇使用)
- **七个不同单QA数据集** (1 篇使用)
- **RewardBench** (1 篇使用)


---

*自动生成于 2026-05-03 | Research Radar*