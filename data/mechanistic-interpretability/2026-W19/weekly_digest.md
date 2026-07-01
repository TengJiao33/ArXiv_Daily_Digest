# mechanistic-interpretability — 2026-W19 (05/04-05/10)

本周新增 **19** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 19。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Complexity Horizons of Compressed Models in Analog Circuit Analy...](http://arxiv.org/abs/2605.02285v1) | 压缩模型选择 | 前置知识图能够针对电路分析的不同复杂度，给出模型压缩与性能关系的细粒度映射 | — | — | ✅ |
| 2 | low | - | [Automated Interpretability and Feature Discovery in Language Mod...](http://arxiv.org/abs/2605.01555v1) | 大模型可解释性 | 在Gemma-2等模型上，智能体驱动循环比一次性标注的解释更清晰可证伪，可发现语言及安全相关... | — | — | — |
| 3 | low | - | [Bucketing the Good Apples: A Method for Diagnosing and Improving...](http://arxiv.org/abs/2605.02234v1) | 因果抽象可解释性 | 在玩具逻辑任务中，递归应用所提方法可从头恢复出高层因果假设，输入划分可助力更精确的机械可解释... | — | — | — |
| 4 | low | - | [Feature Starvation as Geometric Instability in Sparse Autoencode...](http://arxiv.org/abs/2605.05341v1) | 稀疏自编码优化 | 特征饥饿并非数据多样性不足带来的经验伪影，而是过完备字典存在的优化几何结构基本病理 | — | — | — |
| 5 | low | - | [From Packets to Patterns: Interpreting Encrypted Network Traffic...](http://arxiv.org/abs/2605.01616v1) | 加密流量行为感知 | 压力主要关联个体间稳定差异，孤独关联个体内变化，睡眠障碍关联两者，预定义流量特征无法捕获个体... | — | — | — |
| 6 | low | - | [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis of ...](http://arxiv.org/abs/2605.06494v1) | 特征可解释性 | 该方法的聚类可得到解码器余弦相似度聚类无法恢复的启发式模体家族，且聚类分配稳定 | — | — | — |
| 7 | low | - | [GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder Ann...](http://arxiv.org/abs/2605.01829v1) | 基础模型可解释性 | 仅用2%嵌入维度预测MCI转AD得AUC 0.746，特征跨队列复现性r=0.97，定位符合... | — | — | — |
| 8 | low | - | [LatentDiff: Scaling Semantic Dataset Comparison to Millions of I...](http://arxiv.org/abs/2605.00899v1) | 数据集语义对比 | 当仅5%到低于1%的图像存在语义差异时，LatentDiff仍保持高精度与鲁棒性，计算成本远... | — | — | — |
| 9 | low | - | [Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual Bia...](http://arxiv.org/abs/2605.03217v1) | 大模型偏见评估 | 大语言模型偏见呈U型曲线，推理蒸馏同参数下将偏见恢复到小模型水平，Gemini 1.5 Ti... | — | — | — |
| 10 | low | - | [Navigating by Old Maps: The Pitfalls of Static Mechanistic Local...](http://arxiv.org/abs/2605.06076v1) | 大模型机制定位 | 大语言模型参数更新过程中Transformer电路存在固有自由演化，当前静态机制存在时延，不... | — | — | — |
| 11 | low | - | [Negative Before Positive: Asymmetric Valence Processing in Large...](http://arxiv.org/abs/2605.05653v1) | 情绪效价加工 | 负面情绪效价加工定位在大语言模型早期层，正面情绪效价加工峰值出现在模型中后层 | — | — | — |
| 12 | low | - | [Neuron-Anchored Rule Extraction for Large Language Models via Co...](http://arxiv.org/abs/2605.03058v1) | 大模型规则提取 | 在Qwen2与GPT-J的算术、越狱任务中，MechaRule召回96.8%高效果激动神经元... | — | — | — |

## 方法族分布

- **大模型可解释性**：3 篇
- **压缩模型选择**：1 篇
- **因果抽象可解释性**：1 篇
- **基础模型可解释性**：1 篇
- **加密流量行为感知**：1 篇
- **数据集语义对比**：1 篇
- **大模型偏见评估**：1 篇
- **大模型规则提取**：1 篇
- **自适应稀疏编码**：1 篇
- **特征可解释性**：1 篇
- **分子语法学习**：1 篇
- **可解释性归因**：1 篇

## 代码资源

- [Complexity Horizons of Compressed Models in Analog Circuit Analysis](https://github.com/pacomesimon/LLM_prereq_graphs_circuit_analysis)

## 常见基线方法

- **传统评估方法**：1 篇
- **标准稀疏自编码器**：1 篇
- **共病标注特征方法**：1 篇
- **预定义网络流量特征**：1 篇
- **一次性自动解释**：1 篇
- **基于字幕的语义对比方法**：1 篇
- **小语言模型**：1 篇
- **指令调优基础模型**：1 篇
- **标准单特征可解释性协议**：1 篇
- **随机方向扰动法**：1 篇

## 常用数据集

- **模拟电子学数据集**：1 篇
- **ADNI数据集**：1 篇
- **AIBL数据集**：1 篇
- **Noisy-Diff**：1 篇
- **七级压力测试场景**：1 篇
- **犯罪偏见测试场景**：1 篇
- **摘要未提及**：1 篇
- **算术任务数据集**：1 篇
- **越狱任务数据集**：1 篇
- **合成混合领域语料**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*