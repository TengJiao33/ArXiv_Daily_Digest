# llm-truthfulness — 2026-W17 (04/20-04/26)

本周新增 **155** 篇论文，**6** 篇附带代码。优先级：high 0 / medium 0 / low 155。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Detecting Multi-Agent Collusion Through Multi-Agent Interpretabi...](http://arxiv.org/abs/2604.01151) | 多智能体合谋检测 | 探针分布内AUROC达1.00，零样本迁移AUROC为0.60-0.86，合谋信号位于tok... | — | — | ✅ |
| 2 | low | - | [Learning Uncertainty from Sequential Internal Dispersion in Larg...](http://arxiv.org/abs/2604.15741) | 不确定性估计 | SIVR利用大模型跨层内部表示离散度估计不确定性，性能优于强基线，泛化性强且无需大规模训练集 | — | — | ✅ |
| 3 | low | - | [Mechanisms of Introspective Awareness](http://arxiv.org/abs/2603.21396) | 内省感知机制 | 内省检测为两阶段电路，消融拒绝方向提检测53%，训练偏置向量提75%且不增加假阳性 | — | — | ✅ |
| 4 | low | - | [On Reasoning Behind Next Occupation Recommendation](http://arxiv.org/abs/2604.21204v1) | 未分类 | — | — | — | ✅ |
| 5 | low | - | [SinkTrack: Attention Sink based Context Anchoring for Large Lang...](http://arxiv.org/abs/2604.10027) | 上下文锚定 | SinkTrack在SQuAD2.0提升21.6%，在M3CoT提升22.8%，跨不同模型架... | — | — | ✅ |
| 6 | low | - | [The Linear Centroids Hypothesis: How Deep Network Features Repre...](http://arxiv.org/abs/2604.11962) | 特征可解释性 | 将LRH工具作用于质心而非隐层激活，得到DINO ViT更稀疏且下游性能更好的特征字典，可识... | — | — | ✅ |
| 7 | low | - | [A Consistency-Oriented Verification Framework for Reliable Power...](https://www.semanticscholar.org/paper/f675d35926709368d7b759d6227171732e2f82b6) | 电力大模型验证 | CoVe增强模型安全摘要准确率达75.65%，分别超LoRA基线3.02%、基础大模型12.... | — | — | — |
| 8 | low | - | [A New Strategy for Artificial Intelligence: Training Foundation ...](http://arxiv.org/abs/2601.12053) | 基础模型训练策略 | 该研究按感知、估值、执行、整合四个层级分类梳理问题，提出了RLHB、CoTHB两种具体训练方... | — | — | — |
| 9 | low | - | [A Survey of Reinforcement Learning for Large Language Models und...](http://arxiv.org/abs/2604.17312) | 大模型强化学习 | 可从数据、训练、框架三个互补视角自底向上构建该领域方法分类体系，为研究提供清晰概念基础。 | — | — | — |
| 10 | low | - | [A Survey on Human Preference Learning for Aligning Large Languag...](https://www.semanticscholar.org/paper/e3a5da866598c0414dd186085ccd429ac8ea664e) | 人类偏好学习 | 人类偏好反馈可按数据源与格式分类，现有研究可从建模、使用、评估三个维度梳理 | — | — | — |
| 11 | low | - | [AI models of unstable flow exhibit hallucination](http://arxiv.org/abs/2604.20372v1) | AI流体建模幻觉 | 流体动力学AI模型的幻觉源于其光谱偏误，高流速、高粘度反差下该偏误占主导，幻觉违反物理守恒律 | — | — | — |
| 12 | low | - | [ART: Attention Replacement Technique to Improve Factuality in LL...](http://arxiv.org/abs/2604.06393) | 大模型幻觉缓解 | 大语言模型的浅层主要依赖均匀注意力模式，该模式会让模型无法聚焦相关信息进而引发幻觉。 | — | — | — |

## A 会 / Venue 标签

- **ICLR 2026**：2 篇

## 方法族分布

- **未分类**：25 篇
- **大模型幻觉缓解**：4 篇
- **表征几何分析**：2 篇
- **幻觉检测**：2 篇
- **大模型幻觉检测**：2 篇
- **大模型可解释性**：2 篇
- **大模型安全对齐**：2 篇
- **多价值对齐**：2 篇
- **多目标对齐**：2 篇
- **大模型偏好优化**：2 篇
- **AI流体建模幻觉**：1 篇
- **无监督关系学习**：1 篇

## 代码资源

- [Mechanisms of Introspective Awareness](https://github.com/safety-research/introspection-mechanisms.) · 21 stars
- [SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://github.com/67L1/SinkTrack.) · 10 stars
- [Detecting Multi-Agent Collusion Through Multi-Agent Interpretability](https://github.com/aaronrose227/narcbench.) · 3 stars
- [The Linear Centroids Hypothesis: How Deep Network Features Represent Data](https://github.com/ThomasWalker1/LinearCentroidsHypothesis) · 1 stars
- [On Reasoning Behind Next Occupation Recommendation](https://github.com/Sarasarahhhhh/job_prediction.)
- [Learning Uncertainty from Sequential Internal Dispersion in Large Language Model...](https://github.com/ponhvoan/internal-variance.)

## 常见基线方法

- **SFT**：3 篇
- **GRPO**：3 篇
- **GPT-4o**：2 篇
- **未提及具体基线方法**：2 篇
- **CodeSIM**：1 篇
- **GPT-3.5提示基线**：1 篇
- **基于原始图像的端到端视觉语言模型**：1 篇
- **强视觉基线模型**：1 篇
- **独立声明评分器**：1 篇
- **Typed DeepEval对比基线**：1 篇

## 常用数据集

- **MMLU**：3 篇
- **TruthfulQA**：3 篇
- **RewardBench**：3 篇
- **TriviaQA**：2 篇
- **HalluScope基准**：1 篇
- **精选偏好训练数据集**：1 篇
- **RedirectQA**：1 篇
- **LiveCodeBench v6**：1 篇
- **六个公开跨领域跨语言职位广告句子跨度标注语料**：1 篇
- **包含超4000个扰动实例的综合评估基准**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*