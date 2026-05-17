# 机械可解释性 — 2026-W20 (05/11-05/17)

本周新增 **36** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.LG`: 20 篇
- `cs.CL`: 8 篇
- `cs.AI`: 4 篇
- `quant-ph`: 1 篇
- `hep-ph`: 1 篇
- `cs.CV`: 1 篇
- `cs.CR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [SLIM: Sparse Latent Steering for Interpretable and Property-...](http://arxiv.org/abs/2605.10831v1) | 提出即插即用SLIM框架，用带可学习重要门的稀疏自编码器分解隐态获得稀疏属性对齐... | 无需修改原模型参数即可提升编辑成功率，支持可解释分析，实验较基线最高提升42.4... | — |
| 2 | [The Open-Box Fallacy: Why AI Deployment Needs a Calibrated V...](http://arxiv.org/abs/2605.10601v1) | 结合现有实证证据论证核心观点，提出包含六个组分的可报告验证覆盖率标准 | 指出过度依赖机制可解释性的谬误，提出AI部署需校准验证制度与验证覆盖率指标 | — |
| 3 | [SCALAR: A Neurosymbolic Framework for Automated Conjecture a...](http://arxiv.org/abs/2605.10327v1) | 提出基于CUDA-Q构建的神经符号框架SCALAR，整合量子模拟、符号猜想生成与... | 可生成最优QAOA参数与图不变量的猜想界，还原已知结论，识别图结构与优化性质的关... | — |
| 4 | [The Geometric Wall: Manifold Structure Predicts Layerwise Sp...](http://arxiv.org/abs/2605.09887v1) | 对Gemma 2两个模型跨68层的844个SAE检查点，分两阶段拟合缩放规律并回... | 首次开展跨层SAE缩放研究，证实流形几何可预测逐层宽度指数，发现可跨模型迁移的几... | — |
| 5 | [Dissecting Jet-Tagger Through Mechanistic Interpretability](http://arxiv.org/abs/2605.09881v1) | 结合零消融、路径修补、两种互补流形干扰策略与残差流线性探测，分析网络内部结构 | 识别出保留绝大多数性能的稀疏六头分类回路，证明NLP机械可解释方法可用于喷注物理... | — |
| 6 | [Exploitation Without Deception: Dark Triad Feature Steering ...](http://arxiv.org/abs/2605.09773v1) | 采用稀疏自编码器特征操控放大目标大模型的黑暗三角特质，借助心理工具评估模型行为变... | 揭示大语言模型反社会倾向为可分离组件而非统一构念，发现不同特征发现方法的作用差异... | — |
| 7 | [Hidden Error Awareness in Chain-of-Thought Reasoning: The Si...](http://arxiv.org/abs/2605.09502v1) | 通过线性探针探测模型隐藏状态预测推理正确性，采用四种干预验证信号的实际作用 | 证实大语言模型存在隐藏错误感知，明确该信号仅具诊断性而非因果性，划定机制可解释性... | — |
| 8 | [SMIXAE: Towards Unsupervised Manifold Discovery in Language ...](http://arxiv.org/abs/2605.09224v1) | 提出稀疏混合自编码器SMIXAE架构，解决稀疏自编码器无法直接建模多维特征的问题 | 在Gemma 2开源模型中验证SMIXAE可学习已有流形结构，还能发现新的结构 | — |
| 9 | [Investigating Anisotropy in Visual Grounding under Controlle...](http://arxiv.org/abs/2605.09090v1) | 从机械可解释性视角出发，提出相似度控制的反事实描述生成协议，扰动部件分析模型行为 | 提出相似度控制的反事实描述生成方案，证实仅嵌入各向异性无法解释视觉定位反事实错误 | — |
| 10 | [From Mechanistic to Compositional Interpretability](http://arxiv.org/abs/2605.08934v1) | 提出基于范畴论的组合可解释性框架，将可解释性建模为约束优化问题，引入压缩精炼方法 | 为自动化发现与评估机制解释提供可衡量可优化的基础，将现有机制方法归入框架并解释其... | — |
| 11 | [Bilinear autoencoders find interpretable manifolds](http://arxiv.org/abs/2605.08891v1) | 提出双线性自编码器，采用二次潜变量，将神经网络激活分解为低秩二次形式建模。 | 得到非线性且数学易处理的可解释潜表示，可作为无监督流形发现工具，改善语言模型重建... | — |
| 12 | [Architecture, Not Scale: Circuit Localization in Large Langu...](http://arxiv.org/abs/2605.08853v1) | 在Pythia与Qwen2.5两类模型上研究三种电路，对比不同注意力架构的电路特... | 挑战了原有假设，证明注意力架构比参数规模对分析难度影响更大，合适架构让大模型更易... | — |
| 13 | [The Grounding Gap: How LLMs Anchor the Meaning of Abstract C...](http://arxiv.org/abs/2605.08837v1) | 在21个大语言模型上重复认知科学的属性生成、锚定分类实验，用稀疏自动编码器检视模... | 揭示了大语言模型与人类锚定抽象概念间存在稳定的接地鸿沟，明确了当前大语言模型的锚... | — |
| 14 | [Causal Dimensionality of Transformer Representations: Measur...](http://arxiv.org/abs/2605.08740v1) | 提出因果维度kappa，通过稀疏自编码器宽度扫描结合归因修补来估计该参数 | 确立kappa为Transformer层固有可测属性，明确了其亚线性增长、缩放不... | — |
| 15 | [The Echo Amplifies the Knowledge: Somatic Marker Analogues i...](http://arxiv.org/abs/2605.08611v1) | 基于Gemma模型识别情绪专属特征构建情绪向量，回忆阶段按上下文相似度重注入情绪... | 为语言模型引入类躯体标记的情绪记忆机制，复刻Damasio核心发现，提升模型决策... | — |
| 16 | [How Much Do Circuits Tell Us? Measuring the Consistency and ...](http://arxiv.org/abs/2605.08348v1) | 在六个任务七个模型上采用边归因补丁法，结合消融实验分析回路特性 | 揭示了语言模型回路的复用与重叠特性，指出现有回路发现存在任务特异性不足的问题 | — |
| 17 | [Position: Mechanistic Interpretability Must Disclose Identif...](http://arxiv.org/abs/2605.08012v1) | 对分属四个方法方向的多篇论文开展目的性审核与双人编码复现审核。 | 提出因果主张识别假设的披露规范，明确指出验证不等同于因果识别。 | — |
| 18 | [LLM Advertisement based on Neuron Auctions](http://arxiv.org/abs/2605.08326v1) | 提出神经元拍卖新范式，将拍卖对象移至大模型内部表示，设计基于连续菜单的拍卖机制。 | 该框架可保证策略防卫，优化平台收益，保留话语质量，平衡商业激励与用户满意度。 | — |
| 19 | [Tree SAE: Learning Hierarchical Feature Structures in Sparse...](http://arxiv.org/abs/2605.07922v2) | 结合激活约束与新提出的重构约束，提出可直接学习层级特征结构的Tree SAE模型... | Tree SAE学习层级特征对的表现远超现有SAE，可用于挖掘大语言模型的层级概... | — |
| 20 | [What Cohort INRs Encode and Where to Freeze Them](http://arxiv.org/abs/2605.08298v1) | 针对SIREN和FFMLP两种主干，遍历共享编码器冻结深度，采用稀疏自编码器分解... | 首次给出队列训练INR可迁移内容的机制解释，将INR激活转化为可检查的字典原子。 | — |
| 21 | [Mechanistic Interpretability of ASR models using Sparse Auto...](http://arxiv.org/abs/2605.12225v1) | 将稀疏自编码应用于Transformer架构的Whisper ASR，在编码器帧... | 证实稀疏自编码用于ASR可解释性研究的可行性，发现Whisper编码了丰富的语言... | — |
| 22 | [Disentangled Sparse Representations for Concept-Separated Di...](http://arxiv.org/abs/2605.12122v1) | 提出SAEParate，通过概念感知对比目标聚类概念隐表示，用GeLU变换增强编... | 所提方法在UnlearnCanvas上取得最优性能，在联合风格-对象去学习任务提... | — |
| 23 | [Do Language Models Encode Knowledge of Linguistic Constraint...](http://arxiv.org/abs/2605.12055v1) | 使用稀疏自编码器分解多义激活，引入敏感性评分与联合证伪框架筛选目标特征 | 提出识别约束违反偏好特征的敏感性评分，以及带三个评估标准的联合证伪框架 | — |
| 24 | [Domain Restriction via Multi SAE Layer Transitions](http://arxiv.org/abs/2605.11920v1) | 利用稀疏自动编码器编码LLM层转换的内部动态，用轻量方法学习提取域特定特征区分域... | 可更好解释LLM输入处理的内部演化，在gemma-2 2B和9B模型上验证了方法... | — |
| 25 | [Qwen-Scope: Turning Sparse Features into Development Tools f...](http://arxiv.org/abs/2605.11887v1) | 基于Qwen模型族构建开源Qwen-Scope稀疏自编码器套件，从四个方向支撑大... | 开源Qwen-Scope套件，证明稀疏自编码器可作为接口支持大模型诊断、控制、评... | — |
| 26 | [A Mechanistic Investigation of Supervised Fine Tuning](http://arxiv.org/abs/2605.11426v1) | 构建全新研究流程，采用预训练于基础模型的稀疏自编码器作为高分辨率诊断工具 | 发现微调中改变的语义特征具有任务与层特异性分布，得到安全对齐的层级更新特征 | ✅ |
| 27 | [When Are Two Networks the Same? Tensor Similarity for Mechan...](http://arxiv.org/abs/2605.15183v1) | 针对张量类模型提出基于权重的张量相似性度量，采用高效递归算法捕捉全局功能等价与跨... | 新度量比现有方法更高保真追踪功能训练动态，将相似性测量与保真验证转化为已解决代数... | — |
| 28 | [The Rate-Distortion-Polysemanticity Tradeoff in SAEs](http://arxiv.org/abs/2605.14694v1) | 结合toy建模开展理论推导与实证分析，推导多语义度量必要条件，基准测试现有代理指... | 提出SAE的速率-失真-多语义权衡关系，推导了多语义度量应满足的必要条件 | — |
| 29 | [Exploring Geographic Relative Space in Large Language Models...](http://arxiv.org/abs/2605.14535v1) | 运用机械可解释性的新兴工具激活修补，研究大语言模型处理相对地理空间的方式。 | 探索大语言模型中的地理相对空间处理机制，为地理领域大模型可解释性研究提供基础。 | — |
| 30 | [Exemplar Partitioning for Mechanistic Interpretability](http://arxiv.org/abs/2605.14347v1) | 提出无监督的样本划分（EP）方法，通过leader聚类对激活空间做Voronoi... | EP仅需同类方法千分之一的token与构建计算，支持跨层跨模型对比，性能优异 | — |
| 31 | [Rethinking Layer Relevance in Large Language Models Beyond C...](http://arxiv.org/abs/2605.14075v1) | 提出以移除层后模型准确率的实际下降幅度作为评估层相关性的鲁棒度量 | 指出余弦相似度与层移除后的实际性能下降相关性弱，提出更准确的层相关性评估度量 | — |
| 32 | [Mechanistic Interpretability of EEG Foundation Models via Sp...](http://arxiv.org/abs/2605.13930v1) | 对三种不同架构EEG transformer应用TopK稀疏自编码器，结合概念引... | 提出可解释性分析框架，揭示EEG基础模型的表征缺陷，转换得到可解释生理特征 | — |
| 33 | [XAI and Statistical Analysis for Reliable Intrusion Detectio...](http://arxiv.org/abs/2605.13922v1) | 测试多种集成模型与深度网络，结合SHAP可解释分析与多种统计检验方法开展研究 | 为无人机入侵检测提供了鲁棒可靠可解释的模型，明确了数据集中攻击的隐蔽特性 | — |
| 34 | [Descriptive Collision in Sparse Autoencoder Auto-Interpretab...](http://arxiv.org/abs/2605.12874v1) | 重新分析公开人类标注数据集，形式化区分度属性，提出两种校正描述碰撞的指标 | 识别出描述碰撞新问题，提出校正指标，指出忽略该问题会高估特征可解释性水平 | — |
| 35 | [Correcting Influence: Unboxing LLM Outputs with Orthogonal L...](http://arxiv.org/abs/2605.12809v1) | 基于潜在中介推理token级影响力，结合稀疏自编码器、雅可比向量积与逆黑森近似实... | 提出通用预测任务适用的token级影响力框架，提升模型可信度，支持模型审计 | — |
| 36 | [WriteSAE: Sparse Autoencoders for Recurrent State](http://arxiv.org/abs/2605.12770v2) | 提出WriteSAE，将每个解码器原子分解为原生写入形状，采用匹配Frobeni... | 提出首个可分解编辑循环语言模型矩阵缓存写入的稀疏自编码器，多项实验验证性能优异 | — |

## 常见基线方法

- **基于机制可解释性的部署授权** (1 篇引用)
- **传统AI部署监管方式** (1 篇引用)
- **原始未操控模型** (1 篇引用)
- **语义搜索发现特征** (1 篇引用)
- **文本表层分类器** (1 篇引用)
- **语言化置信度预测** (1 篇引用)
- **稀疏自编码器** (1 篇引用)
- **线性表示方法** (1 篇引用)
- **标准多头注意力** (1 篇引用)
- **人类对抽象概念的锚定反应** (1 篇引用)

## 本周提到的 Limitations

- 生成猜想的准确性对图类和量子电路深度存在敏感性，存在一定局限性
- 现有四种干预方法均无法利用检测到错误的信号，修正模型产生的推理错误
- 仅排除了嵌入各向异性对反事实错误的影响，尚未找到反事实错误的根本成因
- 现有识别的回路分量缺乏任务特异性，难以支持对模型行为的针对性理解与干预
- 本次审核中Dim B/D的精确计数受编码规则影响，计数结果存在敏感性。
- 当前大语言模型缺乏统一语法违反检测器，仅能为研究假设提供十分有限的支持
- 所提出的新层相关性评估度量计算开销较大，存在较高计算成本的局限性

## 常用数据集

- **Gemma 2 2B** (2 篇使用)
- **Gemma 2 9B** (2 篇使用)
- **摘要未提及** (2 篇使用)
- **MolEditRL** (1 篇使用)
- **MQLib基准数据集** (1 篇使用)
- **四类拓扑随机生成图数据集** (1 篇使用)
- **顶夸克标记参考数据集** (1 篇使用)
- **Qwen 3.5** (1 篇使用)
- **多个关键基准** (1 篇使用)
- **UnlearnCanvas** (1 篇使用)


---

*自动生成于 2026-05-17 | Research Radar*