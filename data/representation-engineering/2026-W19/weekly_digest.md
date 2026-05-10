# 表示工程与激活引导 — 2026-W19 (05/04-05/10)

本周新增 **18** 篇论文。0 篇附带代码仓库。

## 分类分布

- `cs.LG`: 6 篇
- `cs.CL`: 4 篇
- `via-citation`: 4 篇
- `cs.AI`: 3 篇
- `cs.CV`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Do Large Language Models Plan Answer Positions? Position Bia...](http://arxiv.org/abs/2605.01846v1) | 在三类多选题生成任务上测试多类模型，结合探测实验分析机制，采用激活调控操控答案位... | 发现大模型生成多选题存在结构化位置偏差，提供了研究隐式位置规划的实用框架 | — |
| 2 | [Concepts Whisper While Syntax Shouts: Spectral Anti-Concentr...](http://arxiv.org/abs/2605.01609v1) | 采用匹配谱随机化检验、因果干预、探针分析等方法分析Transformer激活表示 | 揭示Transformer表示存在对偶几何结构，发现概念与句法分布于不同谱子空间 | — |
| 3 | [Minimizing Collateral Damage in Activation Steering](http://arxiv.org/abs/2605.01167v1) | 将激活引导建模为约束优化问题，基于激活经验二阶矩矩阵加权最小化预期平方附带变化。 | 对附带损伤做了数学形式化，提出新框架，可实现更精准控制并降低无关任务性能退化。 | — |
| 4 | [Attention Is Where You Attack](http://arxiv.org/abs/2605.00236) | 提出白盒对抗攻击ARA，识别安全关键注意力头，构造对抗token将注意力重定向远... | 提出针对注意力软最大化几何结构的新攻击，可低步数低token数绕过多种大模型安全... | — |
| 5 | [Steer Like the LLM: Activation Steering that Mimics Promptin...](http://arxiv.org/abs/2605.03907v1) | 将提示引导建模为激活引导，提出PSR模型，训练其模仿提示干预，估计各token专... | 实验显示PSR优于现有激活引导方法，在AxBench和人格引导任务上表现可媲美提... | — |
| 6 | [The Right Answer, the Wrong Direction: Why Transformers Fail...](http://arxiv.org/abs/2605.03258v1) | 采用线性探针、logit透镜分析，结合输出头更新、LoRA两类干预开展验证研究 | 明确计数失败是输出通路几何错位的读出瓶颈而非内部表征缺失，LoRA干预可有效提升... | — |
| 7 | [Implicit Representations of Grammaticality in Language Model...](http://arxiv.org/abs/2605.05197v1) | 研究语言模型内部表征，在扰动自然语料得到的数据集上训练语法性线性探针 | 证实预训练语言模型隐藏层一定程度获得独立于概率的隐式语法性区分，探针性能更优 | — |
| 8 | [Don't Lose Focus: Activation Steering via Key-Orthogonal Pro...](http://arxiv.org/abs/2605.06342v1) | 提出基于关键正交投影的引导方法SKOP，保留推理依赖的聚焦token注意力模式，... | 在多个引导基准获得最优引导-效用权衡，原生引导无效的长上下文检索场景也能保持稳健... | — |
| 9 | [Molecules Meet Language: Confound-Aware Representation Learn...](http://arxiv.org/abs/2605.06303v1) | 基于预训练Transformer-VAE，引入含残差化、对齐分析的混淆感知评估，... | 提出混淆感知评估方法，验证控制混淆后可在纠缠潜在空间实现有化学意义的性质调控 | — |
| 10 | [Memory Inception: Latent-Space KV Cache Manipulation for Ste...](http://arxiv.org/abs/2605.06225v1) | 提出无训练的记忆起始（MI）方法，仅在大模型选定层插入文本衍生KV组实现隐空间引... | 在多种任务性能优于现有基线，可大幅降低KV存储占用，支持对话中途行为切换 | — |
| 11 | [Taming the Entropy Cliff: Variable Codebook Size Quantizatio...](http://arxiv.org/abs/2605.06207v1) | 提出可变码本大小量化VCQ，使码本大小沿序列从小到大单调增长，不改变原有训练流程 | 在ImageNet生成任务上大幅降低gFID提升性能，可自然诱导出由粗到细的语义... | — |
| 12 | [The Granularity Axis: A Micro-to-Macro Latent Direction for ...](http://arxiv.org/abs/2605.06196v1) | 定义基于对比的粒度轴，投影角色隐藏状态，通过激活调控验证其因果相关性 | 证明社会角色粒度是大模型中结构化、可因果操纵的潜在方向，验证其稳定性与可迁移性 | — |
| 13 | [Towards Steering without Sacrifice: Principled Training of S...](http://arxiv.org/abs/2605.05983v1) | 提出联合训练引导因子与方向，引入仅对少量提示词干预的仅提示引导向量PrOSV。 | 解决了现有方法的两个局限，PrOSV性能更优，取得更好的模型效用与鲁棒性权衡。 | — |
| 14 | [TACT: Mitigating Overthinking and Overacting in Coding Agent...](http://arxiv.org/abs/2605.05980v1) | 提出TACT方法，在残差流中提前检测漂移，将漂移激活拉回校准区域缓解问题。 | 在多个主流基准上提升任务解决率，缩短求解步骤，验证了TACT的有效性。 | — |
| 15 | [Causal Probing for Internal Visual Representations in Multim...](http://arxiv.org/abs/2605.05593v1) | 提出基于激活引导的因果框架，对多模态大语言模型的内部视觉表征开展主动探测与系统性... | 揭示不同类型视觉概念的编码差异，厘清模型缩放的机制驱动，发现感知与生成、推理间的... | — |
| 16 | [Manifold Steering Reveals the Shared Geometry of Neural Netw...](http://arxiv.org/abs/2605.05115) | 分别拟合激活表示流形与行为输出流形，通过激活空间的流形引导干预验证二者关联 | 证明表示几何与行为几何存在双向关联，将神经网络引导核心从找方向转为找正确几何 | — |
| 17 | [Hallucination as an Anomaly: Dynamic Intervention via Probab...](http://arxiv.org/abs/2605.05953) | 提出PCNET概率电路检测事实流形上的几何异常幻觉，搭配PC-LDCD仅对异常做... | 在多个基准测试取得优异性能，幻觉检测AUROC最高达99%，有效降低错误修正率提... | — |
| 18 | [Knowing but Not Correcting: Routine Task Requests Suppress F...](http://arxiv.org/abs/2605.05957) | 构建300个错误前提的评估基准，开展机制分析，提出两种无训练干预方法CDS和DP... | 证实校正抑制是普遍严重现象，提出的方法提升修正效果，引入事实严格性作为模型可靠性... | — |

## 常见基线方法

- **谱正则化** (1 篇引用)
- **向量加法干预** (1 篇引用)
- **各向同性干预方法** (1 篇引用)
- **语义或输出logit层面的现有越狱方法** (1 篇引用)
- **清零排名靠前安全头的消融方法** (1 篇引用)
- **现有激活引导方法** (1 篇引用)
- **基于提示的引导方法** (1 篇引用)
- **原始预训练Transformer模型** (1 篇引用)
- **仅更新输出头数字行方法** (1 篇引用)
- **基于语言模型概率的语法性判断** (1 篇引用)

## 本周提到的 Limitations

- 仅更新输出头数字行的改进方法无法解决Transformer自回归生成的计数问题
- 现有微调引导向量需逐选引导因子，全序列过度干预会牺牲生成质量。

## 常用数据集

- **AxBench** (2 篇使用)
- **HarmBench** (1 篇使用)
- **三个引导基准数据集** (1 篇使用)
- **字符计数任务** (1 篇使用)
- **加法任务** (1 篇使用)
- **列表长度任务** (1 篇使用)
- **MMLU** (1 篇使用)
- **GSM8K** (1 篇使用)
- **DROP** (1 篇使用)
- **扰动自然语料构建的语法非语法句数据集** (1 篇使用)


---

*自动生成于 2026-05-10 | Research Radar*