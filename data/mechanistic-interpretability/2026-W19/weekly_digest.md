# 机械可解释性 — 2026-W19 (05/04-05/10)

本周新增 **19** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.LG`: 9 篇
- `cs.AI`: 4 篇
- `cs.CL`: 4 篇
- `cs.CV`: 2 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Complexity Horizons of Compressed Models in Analog Circuit A...](http://arxiv.org/abs/2605.02285v1) | 提出基于前置知识有向无环图的性能感知压缩策略，动态选择适配的压缩模型 | 构建含数据生成流水线和评估引擎的框架，可按需选最小适配压缩模型，实验验证有效 | ✅ |
| 2 | [Bucketing the Good Apples: A Method for Diagnosing and Impro...](http://arxiv.org/abs/2605.02234v1) | 依据成对交换干预行为划分输入空间，提出诊断改进因果抽象的四步实现方法 | 将因果抽象从全局评估转为诊断工具，可识别缺失内容改进解释，多场景获得有效误差分析 | — |
| 3 | [GeoSAE: Geometric Prior-Guided Layer-Wise Sparse Autoencoder...](http://arxiv.org/abs/2605.01829v1) | 提出几何先验引导的GeoSAE框架，利用预训练模型流形结构防特征坍塌，经去年龄混... | 从冻结脑MRI基础模型提取出可跨队列复现的可解释生物标志物，预测MCI转AD性能... | — |
| 4 | [From Packets to Patterns: Interpreting Encrypted Network Tra...](http://arxiv.org/abs/2605.01616v1) | 采用带用户适配器的Transformer建模，结合稀疏自编码器提特征，用广义估计... | 证实加密网络流量是可行的被动行为感知模态，学习表征可捕获预定义特征得不到的行为动... | — |
| 5 | [Automated Interpretability and Feature Discovery in Language...](http://arxiv.org/abs/2605.01555v1) | 提出包含解释精炼、特征发现两个耦合循环的自主多智能体可解释性框架 | 实验验证效果优于一次性自动解释，可发现相关特征，生成可审计的解释轨迹 | — |
| 6 | [LatentDiff: Scaling Semantic Dataset Comparison to Millions ...](http://arxiv.org/abs/2605.00899v1) | 在预训练视觉编码器的潜空间中，结合稀疏自编码器差异检验与密度比估计实现语义对比 | 提出可扩展LatentDiff框架与Noisy-Diff基准，LatentDif... | — |
| 7 | [Moral Sensitivity in LLMs: A Tiered Evaluation of Contextual...](http://arxiv.org/abs/2605.03217v1) | 先通过七级压力测试计算道德敏感指数MSI做行为分析，再用电路分析做机械验证。 | 提出分级评估框架与MSI指标，揭示了大语言模型偏见产生的电路层面机制。 | — |
| 8 | [Pairwise matrices for sparse autoencoders: single-feature in...](http://arxiv.org/abs/2605.03160v1) | 提出成对矩阵协议，在联合条件下共同改变引导系数，在多个大语言模型上开展验证 | 发现标准协议遗漏的三类结论，验证了单特征标注的错误，可定位大模型中关键因果特征 | — |
| 9 | [Neuron-Anchored Rule Extraction for Large Language Models vi...](http://arxiv.org/abs/2605.03058v1) | 提出MechaRule流水线，通过对比分层消融自适应定位稀疏激动神经元，将规则提... | 提出锚定大语言模型内部电路的规则提取方法，实验验证了方法的定位效率与行为抑制效果 | — |
| 10 | [SoftSAE: Dynamic Top-K Selection for Adaptive Sparse Autoenc...](http://arxiv.org/abs/2605.06610v1) | 提出SoftSAE，引入动态Top-K选择机制，利用可微Soft Top-K算子... | 解决固定稀疏度的缺陷，可按输入复杂度调整活跃特征数，实验验证其能找到有效适配的特... | — |
| 11 | [From Token Lists to Graph Motifs: Weisfeiler-Lehman Analysis...](http://arxiv.org/abs/2605.06494v1) | 将每个稀疏自编码器特征建模为token共现图，使用定制WL频率分箱图核度量特征结... | 提出SAE特征的图结构表示，可挖掘出原有分析方法无法捕捉的特征高阶结构关系 | — |
| 12 | [Patch-Effect Graph Kernels for LLM Interpretability](http://arxiv.org/abs/2605.06480v1) | 将激活修补轮廓表示为模型组件上的修补效应图，采用三种构建方法结合图核分析。 | 提供了压缩与评估流程，可在受控基线比较修补结构，区分鲁棒证据与因果回路主张。 | — |
| 13 | [SMolLM: Small Language Models Learn Small Molecular Grammar](http://arxiv.org/abs/2605.06322v1) | 训练53K参数权值共享Transformer模型SMolLM，结合多类分析方法探... | 获得紧致且机制可解释的分子生成器，为形式语言域迭代计算研究提供测试平台 | — |
| 14 | [Playing the network backward: A Game Theoretic Attribution F...](http://arxiv.org/abs/2605.06212v1) | 将反向归因重构为扩展网络图上的双人博弈，构建基于博弈论的统一归因分析框架 | 提出统一归因框架，推导现有方法的博弈论表达，衍生新反向归因规则，适配后性能优于现... | — |
| 15 | [Navigating by Old Maps: The Pitfalls of Static Mechanistic L...](http://arxiv.org/abs/2605.06076v1) | 全程追踪监督微调过程中Transformer电路结构演化，引入三个新指标从多维度... | 揭示参数更新中电路的固有自由演化特性，指出静态机制存在时延缺陷，强调需要预见性机... | — |
| 16 | [Negative Before Positive: Asymmetric Valence Processing in L...](http://arxiv.org/abs/2605.05653v1) | 在开源大语言模型上采用激活修补与方向引导技术，分析不同效价的加工位置 | 证实大语言模型中情绪效价可定位、具因果性且可引导，为可解释性监管提供明确靶点 | — |
| 17 | [SLAM: Structural Linguistic Activation Marking for Language ...](http://arxiv.org/abs/2605.05443v1) | 提出SLAM新型白盒水印方案，将水印写入结构几何，生成时引导编码语言结构的残差方... | 在Gemma-2模型实现100%检测准确率，质量损失远低于现有方法，文本质量接近... | — |
| 18 | [Feature Starvation as Geometric Instability in Sparse Autoen...](http://arxiv.org/abs/2605.05341v1) | 提出全可微的自适应弹性网稀疏自编码器AEN-SAEs，结合L2结构项与自适应L1... | 理论证明其满足利普希茨稳定，实验验证无需辅助启发即可缓解特征饥饿，保持重建能力 | — |
| 19 | [Superposition Is Not Necessary: A Mechanistic Interpretabili...](http://arxiv.org/abs/2605.05151v1) | 运用机械可解释性工具稀疏自编码器，探测PatchTST模型的内部表征特性 | 证明时间序列预测取得有竞争力性能无需叠加，解释了简单线性模型具备竞争力的原因 | — |

## 常见基线方法

- **传统评估方法** (1 篇引用)
- **标准稀疏自编码器** (1 篇引用)
- **共病标注特征方法** (1 篇引用)
- **预定义网络流量特征** (1 篇引用)
- **一次性自动解释** (1 篇引用)
- **基于字幕的语义对比方法** (1 篇引用)
- **小语言模型** (1 篇引用)
- **指令调优基础模型** (1 篇引用)
- **标准单特征可解释性协议** (1 篇引用)
- **随机方向扰动法** (1 篇引用)

## 本周提到的 Limitations

- 本文提出的图视角贡献为互补性而非主导性，整体聚类纯度低于token直方图基线
- 现有基于静态机制定位的方法存在效果幻觉，静态机制不足以有效指导未来参数更新
- SLAM能够抵抗单词级编辑，但易被重构语法结构的释义攻击破坏水印

## 常用数据集

- **模拟电子学数据集** (1 篇使用)
- **ADNI数据集** (1 篇使用)
- **AIBL数据集** (1 篇使用)
- **Noisy-Diff** (1 篇使用)
- **七级压力测试场景** (1 篇使用)
- **犯罪偏见测试场景** (1 篇使用)
- **摘要未提及** (1 篇使用)
- **算术任务数据集** (1 篇使用)
- **越狱任务数据集** (1 篇使用)
- **合成混合领域语料** (1 篇使用)


---

*自动生成于 2026-05-10 | Research Radar*