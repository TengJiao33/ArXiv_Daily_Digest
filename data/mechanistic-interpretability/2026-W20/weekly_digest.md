# mechanistic-interpretability — 2026-W20 (05/11-05/17)

本周新增 **36** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 36。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [A Mechanistic Investigation of Supervised Fine Tuning](http://arxiv.org/abs/2605.11426v1) | 监督微调机制 | SFT前后大模型激活余弦相似度很高，经预训练SAE投影后底层稀疏隐变量显著分化，安全对齐有特... | — | — | ✅ |
| 2 | low | - | [Architecture, Not Scale: Circuit Localization in Large Language ...](http://arxiv.org/abs/2605.08853v1) | 电路可解释性 | 同等规模下分组查询注意力比标准多头注意力的电路更集中、机制更稳定，超临界规模事实回忆电路会发... | — | — | — |
| 3 | low | - | [Bilinear autoencoders find interpretable manifolds](http://arxiv.org/abs/2605.08891v1) | 可解释表示学习 | 不同几何先验的双线性自编码器尽管字典条目不同，仍可恢复出相同输入子空间，多维几何普遍存在。 | — | — | — |
| 4 | low | - | [Causal Dimensionality of Transformer Representations: Measuremen...](http://arxiv.org/abs/2605.08740v1) | 因果维度测量 | 表征容量增长15.6倍时因果容量仅增4.35倍，kappa不随模型缩放改变，深度增加时归因阈... | — | — | — |
| 5 | low | - | [Correcting Influence: Unboxing LLM Outputs with Orthogonal Laten...](http://arxiv.org/abs/2605.12809v1) | LLM影响力归因 | 所提方法可在医疗基准任务中识别出共同影响LLM预测结果的稀疏可解释token集合 | — | — | — |
| 6 | low | - | [Descriptive Collision in Sparse Autoencoder Auto-Interpretabilit...](http://arxiv.org/abs/2605.12874v1) | 自动可解释性 | 82.1%的特征共享标注，平均标注被3.07个特征复用，忽略碰撞会高估可解释性约1/3识别特... | — | — | — |
| 7 | low | - | [Disentangled Sparse Representations for Concept-Separated Diffus...](http://arxiv.org/abs/2605.12122v1) | 扩散模型去学习 | 在联合风格-对象去学习挑战性场景中，所提方法大幅缓解了目标与非目标概念间的干扰，性能优于现有... | — | — | — |
| 8 | low | - | [Dissecting Jet-Tagger Through Mechanistic Interpretability](http://arxiv.org/abs/2605.09881v1) | 机械可解释性 | 识别出稀疏六头分类回路：早层单头为因果源，中层多头中继，晚层单头读出，残差流偏好能量相关基与... | — | — | — |
| 9 | low | - | [Do Language Models Encode Knowledge of Linguistic Constraint Vio...](http://arxiv.org/abs/2605.12055v1) | 语言知识编码 | 所有语言现象未共同满足证伪标准，不存在全类别共享的特征，仅部分现象存在部分选择性因果结构证据 | — | — | — |
| 10 | low | - | [Domain Restriction via Multi SAE Layer Transitions](http://arxiv.org/abs/2605.11920v1) | 域外文本检测 | 基于稀疏自动编码器编码的层转换可捕捉细粒度输入细节，能有效区分域外文本，还可解释LLM内部处... | — | — | — |
| 11 | low | - | [Exemplar Partitioning for Mechanistic Interpretability](http://arxiv.org/abs/2605.14347v1) | 机制可解释性 | 在Gemma-2-2B-it L20的AxBench任务中，EP以千分之一构建计算获0.88... | — | — | — |
| 12 | low | - | [Exploitation Without Deception: Dark Triad Feature Steering Reve...](http://arxiv.org/abs/2605.09773v1) | 大模型反社会研究 | 放大黑暗三角特质后行为效应量d=10.62，两种特征发现方法行为差异d=12.65，剥削与欺... | — | — | — |

## A 会 / Venue 标签

- **ICLR 2026**：1 篇

## 方法族分布

- **机制可解释性**：3 篇
- **机械可解释性**：2 篇
- **模型可解释性**：2 篇
- **大模型可解释性**：2 篇
- **大模型分子编辑**：1 篇
- **AI部署监管**：1 篇
- **量子电路分析**：1 篇
- **SAE缩放定律**：1 篇
- **大模型反社会研究**：1 篇
- **隐藏错误感知**：1 篇
- **语言模型流形发现**：1 篇
- **视觉定位可解释性**：1 篇

## 代码资源

- [A Mechanistic Investigation of Supervised Fine Tuning](https://github.com/ruhzi/sae-investigation.)

## 常见基线方法

- **基于机制可解释性的部署授权**：1 篇
- **传统AI部署监管方式**：1 篇
- **原始未操控模型**：1 篇
- **语义搜索发现特征**：1 篇
- **文本表层分类器**：1 篇
- **语言化置信度预测**：1 篇
- **稀疏自编码器**：1 篇
- **线性表示方法**：1 篇
- **标准多头注意力**：1 篇
- **人类对抽象概念的锚定反应**：1 篇

## 常用数据集

- **Gemma 2 2B**：2 篇
- **Gemma 2 9B**：2 篇
- **摘要未提及**：2 篇
- **MolEditRL**：1 篇
- **MQLib基准数据集**：1 篇
- **四类拓扑随机生成图数据集**：1 篇
- **顶夸克标记参考数据集**：1 篇
- **Qwen 3.5**：1 篇
- **多个关键基准**：1 篇
- **UnlearnCanvas**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*