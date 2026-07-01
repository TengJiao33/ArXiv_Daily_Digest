# mechanistic-interpretability — 2026-W22 (05/25-05/31)

本周新增 **31** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 31。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Every Component is a Lookup: Token Attribution and Composition f...](http://arxiv.org/abs/2605.23393v1) | 机制可解释性 | 在160M到6.9B参数的Pythia家族中，同姓名第一次提及信用强，重复检测位置信用被抑制... | — | — | ✅ |
| 2 | low | - | [BioRefusalAudit: Auditing Biosecurity Refusal Depth Using Genera...](http://arxiv.org/abs/2605.30162v1) | 生物安全审计 | Gemma 4 E2B-IT带格式拒绝65/75提示无格式为0，80token限制下所有Ge... | — | — | — |
| 3 | low | - | [Continuous-Depth Field Theory for Transformer Patching and Mecha...](http://arxiv.org/abs/2605.25225v1) | 机械可解释性 | 在GPT-2风格自回归Transformer中识别出有界局部线性区，跨深度和词元位置存在结构... | — | — | — |
| 4 | low | - | [Cultural Binding Heads in Language Models](http://arxiv.org/abs/2605.28543v1) | 文化绑定机制 | 每个模型存在2-3个中层注意力头因果影响文化绑定，模型已知知识是输出表现的3-5倍，瓶颈在路... | — | — | — |
| 5 | low | - | [Detecting Unfaithful Chain-of-Thought via Circuit-Guided Interna...](http://arxiv.org/abs/2605.25603v1) | CoT不忠实检测 | 结合模型内部可解释性信号与外部推理轨迹，降本同时在四个数据集取得SOTA的CoT不忠实检测性... | — | — | — |
| 6 | low | - | [Dissecting the Black Box: Circuit-Level Analysis of LLM Vulnerab...](http://arxiv.org/abs/2605.29901v1) | 大模型可解释性 | 模型主要依赖识别安全编码模式的检测器检测漏洞，仅用16%容量，消融L7的20个神经元准确率降... | — | — | — |
| 7 | low | - | [Feature Geometry of LoRA Adapters: A Sparse Autoencoder Analysis...](http://arxiv.org/abs/2605.28896v1) | LoRA特征几何分析 | LoRA诱导特征与预训练SAE特征几何对齐较弱，特征密度随秩和深度增加，几何分歧在不同秩间稳... | — | — | — |
| 8 | low | - | [Guiding LLM Post-training Data Engineering with Model Internals ...](http://arxiv.org/abs/2605.27354v1) | 后训练数据工程 | SAERL比原生GRPO平均准确率提升3.00%，达到目标准确率可减少20%训练步骤，SAE... | — | — | — |
| 9 | low | - | [Interpretability-Guided Layer Selection over Subspace Projection...](http://arxiv.org/abs/2605.28649v1) | 可解释模型编辑 | 原投影方法丢弃约97%的修改能量，失效源于SAE方向与任务向量几何不对齐，新方法提升数论准确... | — | — | — |
| 10 | low | - | [Latent Terms: Dense Retrievers Contain Trivially Extractable BM2...](http://arxiv.org/abs/2605.29384v1) | 稠密检索结构分析 | 训练好的单/多向量稠密检索器，可分解出符合齐夫分布、无需额外监督即可直接用于BM25的潜在词... | — | — | — |
| 11 | low | - | [Learning dynamical systems with biochemically informed neural or...](http://arxiv.org/abs/2605.24170v1) | 动力系统学习 | BINODE可在Monod、Lotka-Volterra、药代动力学、超日内分泌模型中恢复系... | — | — | — |
| 12 | low | - | [MechRL: Reinforcement Learning Agents Perform Circuit Discovery ...](http://arxiv.org/abs/2605.26343v1) | 机械可解释性 | 在未提供任何评估任务信号的域外任务上，五次最优规划可达到oracle上限的96%，优选头符合... | — | — | — |

## 方法族分布

- **机械可解释性**：2 篇
- **机制可解释性**：2 篇
- **大模型可解释性**：2 篇
- **CoT不忠实检测**：1 篇
- **大模型持续学习**：1 篇
- **医学VLM去幻觉**：1 篇
- **概念形成机制**：1 篇
- **动力系统学习**：1 篇
- **稀疏引导生成**：1 篇
- **多语言控制**：1 篇
- **大脑大模型对齐**：1 篇
- **模型可解释性**：1 篇

## 代码资源

- [Every Component is a Lookup: Token Attribution and Composition from a Single Dec...](https://github.com/Fun-Cry/unpacklm.) · 1 stars

## 常见基线方法

- **基于外部信号的CoT不忠实检测器**：1 篇
- **全推理电路构建的电路追踪方法**：1 篇
- **现有基于正则化的持续学习方法**：1 篇
- **RadVLM**：1 篇
- **LLaVA-Rad**：1 篇
- **CheXOne**：1 篇
- **标准峰值检测方法**：1 篇
- **标准SAE通用性度量**：1 篇
- **常数均值预测**：1 篇
- **匹配控制提示**：1 篇

## 常用数据集

- **摘要未提及具体数据集**：3 篇
- **FaithCoT-Bench**：1 篇
- **两个持续学习基准数据集**：1 篇
- **MIMIC-CXR**：1 篇
- **IU-Xray**：1 篇
- **Dyck-3**：1 篇
- **The Pile**：1 篇
- **间接宾语识别任务**：1 篇
- **Textualized Gridworld**：1 篇
- **高维教育领域数据集**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*