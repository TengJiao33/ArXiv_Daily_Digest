# 表示工程与激活引导 — 2026-W20 (05/11-05/17)

本周新增 **21** 篇论文。0 篇附带代码仓库。

## 分类分布

- `cs.CL`: 7 篇
- `cs.LG`: 5 篇
- `cs.AI`: 4 篇
- `cs.CV`: 2 篇
- `hep-ph`: 1 篇
- `via-citation`: 1 篇
- `stat.AP`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Prompt-Activation Duality: Improving Activation Steering via...](http://arxiv.org/abs/2605.10664v1) | 提出门控裁剪注意力增量引导（GCAD），从系统prompt贡献提取引导信号，配合... | 该方法保留特质控制的同时大幅提升长程连贯性，在多轮对话基准上性能提升显著。 | — |
| 2 | [Route Before Retrieve: Activating Latent Routing Abilities o...](http://arxiv.org/abs/2605.10235v1) | 提出Pre-Route主动路由框架，在回答前基于轻量元数据做结构化推理生成可解释... | 激活大语言模型的潜在路由能力，实验验证该框架优于多个基线，拥有更优成本效益。 | — |
| 3 | [Tensor Product Representation Probes Reveal Shared Structure...](http://arxiv.org/abs/2605.09967v1) | 以奥赛罗游戏的已知线性表示模型为对象，训练TPR探针分解线性探针的共享结构。 | 揭示线性方向表示是更结构化底层表示的投影，发现TPR探针存在对应几何特征。 | — |
| 4 | [Dissecting Jet-Tagger Through Mechanistic Interpretability](http://arxiv.org/abs/2605.09881v1) | 结合零消融、路径补丁、两种互补流形腐败策略与残差流线性探测分析模型结构 | 识别出性能接近全模型的稀疏六头分类电路，验证NLP可解释方法可用于喷物理分类器 | — |
| 5 | [Do Linear Probes Generalize Better in Persona Coordinates?](http://arxiv.org/abs/2605.09391v1) | 借助对比人设提示构建欺骗与奉承的人设轴，经无监督PCA提取主成分方向 | 证明基于人设投影的探针泛化更优，整合多行为的统一轴可提升跨场景泛化 | — |
| 6 | [LLM Agents Already Know When to Call Tools -- Even Without R...](http://arxiv.org/abs/2605.09252v1) | 提出When2Tool基准，设计Probe&Prefill方法，用轻量线性探针读... | 构建了分三类可控难度的When2Tool基准，新方法大幅减少工具调用且精度损失极... | — |
| 7 | [Repeated-Token Counting Reveals a Dissociation Between Repre...](http://arxiv.org/abs/2605.09239v1) | 在大语言模型各后嵌入层残差流使用线性探针，结合注意力模式分析探究失败原因 | 明确大语言模型重复token计数失败的真正机制，纠正了此前的错误归因 | — |
| 8 | [The Geometry of Forgetting: Temporal Knowledge Drift as an I...](http://arxiv.org/abs/2605.09195v1) | 通过几何分析研究残差流表示结构，训练线性探针检测大语言模型的时序知识漂移 | 证明时序知识漂移是结构问题而非工程问题，验证其正交性，线性探针检测效果优异 | — |
| 9 | [Emergent Semantic Role Understanding in Language Models](http://arxiv.org/abs/2605.09187v1) | 冻结仅解码器Transformer，训练线性探针提取语义角色，依据性能推断信息编... | 明确预训练本身可产生部分但不完全的语义角色理解，揭示模型规模对表征方式的影响 | — |
| 10 | [MC-RFM: Geometry-Aware Few-Shot Adaptation via Mixed-Curvatu...](http://arxiv.org/abs/2605.08557v1) | 提出MC-RFM混合曲率黎曼流匹配框架，在混合曲率乘积流形上建模冻结视觉骨干的小... | 该方法轻量且骨干无关，在多个视觉基准多数设置下取得最优性能，验证了几何建模的有效... | — |
| 11 | [Where's the Plan? Locating Latent Planning in Language Model...](http://arxiv.org/abs/2605.07984v1) | 以押韵对句完成为测试任务，对多系列多尺度模型应用线性探针、激活补丁、两阶段路径补... | 揭示不同大模型对未来信息编码的因果依赖差异，定位Gemma-3-27B中规划相关... | — |
| 12 | [ProteinJEPA: Latent prediction complements protein language ...](http://arxiv.org/abs/2605.07554v1) | 提出仅在掩码位置预测隐目标，保留MLM交叉熵的掩码位置MLM+JEPA训练方案 | 验证了匹配时间预算下，JEPA结合MLM优于纯MLM，能在多数下游任务取得性能提... | — |
| 13 | [Mathematical Reasoning via Intervention-Based Time-Series Ca...](http://arxiv.org/abs/2605.07600) | 提出CIKA框架，将LLM自身作为干预模拟器，设计ICP探针分离混淆诊断概念使用... | 验证了ICP可区分因果相关概念，可预测解题成功，冻结权重7B大模型获优异推理性能 | — |
| 14 | [Stories in Space: In-Context Learning Trajectories in Concep...](http://arxiv.org/abs/2605.12412v1) | 以故事理解为动态信念更新场景，结合行为与表征分析研究大模型上下文学习信念轨迹 | 提出概念信念空间假说，给出大模型上下文学习信念动态的几何解释 | — |
| 15 | [Metaphor Is Not All Attention Needs](http://arxiv.org/abs/2605.12128v1) | 对注意力模式开展可解释性分析，结合输入消融、表示构建、聚类与线性探针研究 | 明确文学越狱并非模型识别失败，而是累积风格异常改变提示处理，规避后训练安全触发 | — |
| 16 | [Structural Interpretations of Protein Language Model Represe...](http://arxiv.org/abs/2605.10985v1) | 提出即插即用框架，将ESM-2表示投影到蛋白质接触图，用SoftBlobGIN学... | 无需重训蛋白质语言模型，在多个预测任务取得优异性能，可提供可审计的结构解释 | — |
| 17 | [Probing Persona-Dependent Preferences in Language Models](http://arxiv.org/abs/2605.13339v1) | 在Gemma-3-27B与Qwen-3.5-122B的残差流激活上训练线性探针，... | 识别出可追踪偏好变化的真实偏好向量，发现偏好表示跨不同角色大体共享 | — |
| 18 | [KamonBench: A Grammar-Based Dataset for Evaluating Compositi...](http://arxiv.org/abs/2605.13322v1) | 基于语法规则生成合成纹章数据，构建KamonBench基准，支持多维度组合因子恢... | 推出含两万张合成纹章的KamonBench基准，为稀疏组合视觉识别提供可控测试平... | — |
| 19 | [When Attention Closes: How LLMs Lose the Thread in Multi-Tur...](http://arxiv.org/abs/2605.12922v1) | 提出通道转换假说，引入目标可及比GAR指标，结合滑动窗口消融与残差流探针开展研究 | 提出诊断指标GAR、通道转换机制解释框架，可预测窗口注意力关闭下故障的发生时机 | — |
| 20 | [Steer-to-Detect: Probing Hidden Representations for Detectio...](http://arxiv.org/abs/2605.12890v1) | 提出两阶段S2D框架，先学习引导向量注入冻结观测LLM隐藏态提升类别可分性，再经... | 给出检测错误的有限样本高概率理论保证，实证该方法在多场景下取得稳定优异的检测性能 | — |
| 21 | [Inference-Time Machine Unlearning via Gated Activation Redir...](http://arxiv.org/abs/2605.12765v1) | 提出无训练无梯度的GUARD-IT，推理时做输入依赖的门控激活重定向，不改变原模... | 效果匹配或超过12种梯度基线，支持无需重训练的持续遗忘，量化场景下仍保持有效 | — |

## 常见基线方法

- **标准残差流激活引导** (1 篇引用)
- **Always-RAG** (1 篇引用)
- **Always-LC** (1 篇引用)
- **Self-Route** (1 篇引用)
- **原始激活训练的线性探针** (1 篇引用)
- **仅提示（Prompt-only）方法** (1 篇引用)
- **先推理后行动（Reason-then-Act）方法** (1 篇引用)
- **token熵方法** (1 篇引用)
- **语义熵方法** (1 篇引用)
- **CCS** (1 篇引用)

## 本周提到的 Limitations

- 从零开始预训练结果好坏参半，部分任务效果不如纯MLM，无MLM纯JEPA几乎全部实验失效

## 常用数据集

- **LaRA** (1 篇使用)
- **LongBench-v2** (1 篇使用)
- **奥赛罗棋盘游戏数据** (1 篇使用)
- **顶夸克标记参考数据集** (1 篇使用)
- **10个评估数据集** (1 篇使用)
- **When2Tool基准** (1 篇使用)
- **七个视觉识别基准** (1 篇使用)
- **SCOPe-40** (1 篇使用)
- **TAPE** (1 篇使用)
- **Omni-MATH** (1 篇使用)


---

*自动生成于 2026-05-17 | Research Radar*