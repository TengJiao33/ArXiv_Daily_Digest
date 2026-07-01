# llm-truthfulness — 2026-W22 (05/25-05/31)

本周新增 **29** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 29。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Language Bias in LVLMs: From In-Depth Analysis to Simple and Eff...](http://arxiv.org/abs/2605.25036v1) | 语言偏差缓解 | 大视觉语言模型语言偏差的根源是训练中的模态不对齐，VIT和DPO常优先文本改进，过度偏向语言... | — | — | ✅ |
| 2 | low | - | [AutoSG: LLM-Driven Solver Generation Solely from Task Prompts fo...](http://arxiv.org/abs/2605.25658v1) | 求解器自动生成 | 依托检索增强防幻觉、结构保留精修、无实例评判三大机制，生成的求解器性能显著优于所有对比基线 | — | — | — |
| 3 | low | - | [By Their Fruits You Will Know Them: Comparing Formalizations of ...](http://arxiv.org/abs/2605.25186v1) | 法律形式化比较 | 不同法律形式化的行为分歧与结构一致性基本无关，部分分歧对应法学评论中的真实争议 | — | — | — |
| 4 | low | - | [CommunityFact: A Dynamic, Multilingual, Multi-domain Benchmark f...](http://arxiv.org/abs/2605.30241v1) | 错误信息检测 | 联网给错误信息验证带来最大提升，联网大模型选源与人类标注有偏差，检索扩展或修剪可缩小该偏差 | — | — | — |
| 5 | low | - | [DiffSpot: Can VLMs Spot Fine-Grained Visual Differences in Web I...](http://arxiv.org/abs/2605.29615v1) | 视觉语言模型评估 | 零样本测试中最优模型仅识别40.7%真实变化，所有模型难样本召回低于23%，像素与CLIP距... | — | — | — |
| 6 | low | - | [Double Triangle Annotation: A Scalable Human-in-the-Loop Framewo...](http://arxiv.org/abs/2605.25781v1) | 历史文档标注 | 该框架在13595个字段中自动接受超85%标注，最终词错误率仅0.003，模型能力提升后自主... | — | — | — |
| 7 | low | - | [Faithfulness Metrics Don't Measure Faithfulness: A Meta-Evaluati...](http://arxiv.org/abs/2605.25052v1) | 保真度元评估 | 大多数指标性能接近随机，最佳CoT级仅0.70 AUROC，最佳步级仅0.59 AUROC，... | — | — | — |
| 8 | low | - | [From Automation to Collaboration: Human-in-the-Loop Methods for ...](http://arxiv.org/abs/2605.25226v1) | 安全可信NLP | 基于探针的审计发现大语言模型行为不一致，对抗文本生成发现低资源语言存在鲁棒性缺口。 | — | — | — |
| 9 | low | - | [Functional Entropy: Predicting Functional Correctness in LLM-Gen...](http://arxiv.org/abs/2605.28500v1) | 代码正确性预测 | 基于NLI的采样UQ方法因NLI无法区分功能差异聚类失效，提出的方法在15组中11组取得To... | — | — | — |
| 10 | low | - | [Graph Alignment Topology as an Inductive Bias for Grounding Dete...](http://arxiv.org/abs/2605.22963) | 大模型幻觉检测 | 以图对齐拓扑为归纳偏置的方法，在四个数据集上取得SOTA，性能超过GPT-4o等所有对比方法 | — | — | — |
| 11 | low | - | [Hallucination Behavior in Multimodal LLMs Across Agricultural Im...](http://arxiv.org/abs/2605.27595) | 农业大模型幻觉 | 图像解读零样本准确率63%-75%，少样本提升至86.8%；文本生图宽松提示下最高91%场景... | — | — | — |
| 12 | low | - | [Hallucination Detection-Guided Preference Optimization for Clini...](http://arxiv.org/abs/2605.28910v1) | 临床摘要去幻觉 | 在Llama-3.1-8B-Instruct模型上，两种方法分别减少24%和48%的幻觉，且... | — | — | — |

## 方法族分布

- **长期智能体记忆**：1 篇
- **大模型弃权学习**：1 篇
- **历史文档标注**：1 篇
- **求解器自动生成**：1 篇
- **安全可信NLP**：1 篇
- **法律形式化比较**：1 篇
- **可再生能源预测**：1 篇
- **保真度元评估**：1 篇
- **语言偏差缓解**：1 篇
- **金融RAG框架**：1 篇
- **医学VLM幻觉缓解**：1 篇
- **物体幻觉缓解**：1 篇

## 代码资源

- [Language Bias in LVLMs: From In-Depth Analysis to Simple and Effective Mitigatio...](https://github.com/lab-klc/LVLM-Language-Bias.)

## 常见基线方法

- **现有记忆基线**：1 篇
- **静态三元基线**：1 篇
- **多种对比基线**：1 篇
- **传统手工标注**：1 篇
- **大模型全自动标注流水线**：1 篇
- **人类设计SOTA框架**：1 篇
- **现有LLM生成求解器**：1 篇
- **经典预测方法**：1 篇
- **统计时间序列模型**：1 篇
- **深度学习架构**：1 篇

## 常用数据集

- **TriviaQA**：2 篇
- **LoCoMo**：1 篇
- **BEAM-100K**：1 篇
- **AbstentionBench全部测试数据集**：1 篇
- **Guides Rosenwald**：1 篇
- **摘要未提及**：1 篇
- **九个前沿LLM生成的十个欧盟法律条款形式化**：1 篇
- **BonaFide**：1 篇
- **FinanceBench**：1 篇
- **MIMIC-CXR**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*