# representation-engineering — 2026-W19 (05/04-05/10)

本周新增 **18** 篇论文，**0** 篇附带代码。优先级：high 0 / medium 0 / low 18。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Attention Is Where You Attack](http://arxiv.org/abs/2605.00236) | 大模型越狱攻击 | 清零顶级安全头最多仅1次拒绝翻转，ARA可翻转Mistral的72/200、LLaMA-3的... | — | — | — |
| 2 | low | - | [Causal Probing for Internal Visual Representations in Multimodal...](http://arxiv.org/abs/2605.05593v1) | 因果探针分析 | 实体概念为局部编码存储，抽象概念全局分布，增加模型深度仅对抽象概念编码必要，感知与推理存在脱... | — | — | — |
| 3 | low | - | [Concepts Whisper While Syntax Shouts: Spectral Anti-Concentratio...](http://arxiv.org/abs/2605.01609v1) | 表征几何分析 | 发现Transformer存在对偶几何，概念反集中于谱尾，8个模型中6个句法优先编码在高方差... | — | — | — |
| 4 | low | - | [Do Large Language Models Plan Answer Positions? Position Bias in...](http://arxiv.org/abs/2605.01846v1) | 位置偏差分析 | 同模型家族的大语言模型生成多选题的位置偏差模式相似，问题干隐藏表征编码了正确答案位置的预测信... | — | — | — |
| 5 | low | - | [Don't Lose Focus: Activation Steering via Key-Orthogonal Project...](http://arxiv.org/abs/2605.06342v1) | 激活引导 | SKOP可将效用退化降低5-7倍，同时保留95%以上的原生引导效果，长上下文可避免注意力重路... | — | — | — |
| 6 | low | - | [Hallucination as an Anomaly: Dynamic Intervention via Probabilis...](http://arxiv.org/abs/2605.05953) | 幻觉检测校正 | PCNET幻觉检测AUROC最高达99%，PC-LDCD错误修正率降至53.7%，正确内容保... | — | — | — |
| 7 | low | - | [Implicit Representations of Grammaticality in Language Models](http://arxiv.org/abs/2605.05197v1) | 语法性探测 | 英文训练的线性语法探针可跨语言泛化，探针分数与字符串概率仅呈弱相关，语法判断优于概率法 | — | — | — |
| 8 | low | - | [Knowing but Not Correcting: Routine Task Requests Suppress Factu...](http://arxiv.org/abs/2605.05957) | 事实校正抑制 | 校正抑制率范围为19%至90%，四款模型超80%，该现象发生在响应选择而非知识编码阶段 | — | — | — |
| 9 | low | - | [Manifold Steering Reveals the Shared Geometry of Neural Network ...](http://arxiv.org/abs/2605.05115) | 流形引导 | 沿激活流形引导得到的行为轨迹遵循行为流形，沿行为流形优化得到的激活轨迹贴合激活流形曲率 | — | — | — |
| 10 | low | - | [Memory Inception: Latent-Space KV Cache Manipulation for Steerin...](http://arxiv.org/abs/2605.06225v1) | 大语言模型引导 | 该方法在HARDMath和PHYSICS的10/12子集优于可见提示，最高可将KV存储缩减1... | — | — | — |
| 11 | low | - | [Minimizing Collateral Damage in Activation Steering](http://arxiv.org/abs/2605.01167v1) | 激活引导优化 | 基于激活经验二阶矩对不同特征方向扰动做非均匀加权，可提升控制精度并降低无关任务性能退化。 | — | — | — |
| 12 | low | - | [Molecules Meet Language: Confound-Aware Representation Learning ...](http://arxiv.org/abs/2605.06303v1) | 分子性质调控 | 经混淆感知评估，cLogP等六种化学性质可实现鲁棒单调调控，部分适配全局方向部分适配局部梯度 | — | — | — |

## 方法族分布

- **位置偏差分析**：1 篇
- **表征几何分析**：1 篇
- **激活引导优化**：1 篇
- **大模型越狱攻击**：1 篇
- **大模型激活引导**：1 篇
- **计数失败机制**：1 篇
- **语法性探测**：1 篇
- **激活引导**：1 篇
- **分子性质调控**：1 篇
- **大语言模型引导**：1 篇
- **自回归视觉生成**：1 篇
- **角色粒度分析**：1 篇

## 常见基线方法

- **谱正则化**：1 篇
- **向量加法干预**：1 篇
- **各向同性干预方法**：1 篇
- **语义或输出logit层面的现有越狱方法**：1 篇
- **清零排名靠前安全头的消融方法**：1 篇
- **现有激活引导方法**：1 篇
- **基于提示的引导方法**：1 篇
- **原始预训练Transformer模型**：1 篇
- **仅更新输出头数字行方法**：1 篇
- **基于语言模型概率的语法性判断**：1 篇

## 常用数据集

- **AxBench**：2 篇
- **HarmBench**：1 篇
- **三个引导基准数据集**：1 篇
- **字符计数任务**：1 篇
- **加法任务**：1 篇
- **列表长度任务**：1 篇
- **MMLU**：1 篇
- **GSM8K**：1 篇
- **DROP**：1 篇
- **扰动自然语料构建的语法非语法句数据集**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*