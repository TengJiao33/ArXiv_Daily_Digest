# 机械可解释性 — 2026-W21 (05/18-05/24)

本周新增 **18** 篇论文。2 篇附带代码仓库。

## 分类分布

- `cs.LG`: 8 篇
- `cs.CV`: 4 篇
- `cs.CL`: 4 篇
- `cs.CR`: 1 篇
- `cs.RO`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Aligned Training: A Parameter-Free Method to Improve Feature...](http://arxiv.org/abs/2605.18629v1) | 提出无参数的对齐训练方法，对SAE重参数化，约束每个特征编解码器方向内积为1 | 同时提升SAE重构质量，消除死特征，增强训练稳定性，适配现有技术，基准测试获帕累... | — |
| 2 | [Are Sparse Autoencoder Benchmarks Reliable?](http://arxiv.org/abs/2605.18229v1) | 从固定SAE重播种噪声、合成SAE真值相关性、训练轨迹可区分性三个维度审计SAE... | 审计了标准SAE评测套件SAEBench的各质量指标，明确了不同评测指标的可靠性... | — |
| 3 | [Babel: Jailbreaking Safety Attention via Obfuscation Distrib...](http://arxiv.org/abs/2605.17971v1) | 构建刻画有效文本混淆边界的数学越狱模型，提出迭代优化混淆采样的Babel黑盒攻击... | 在多个前沿商用大模型实现SOTA效果，为大模型安全研究提供可靠红队测试方法 | — |
| 4 | [A Distributional View for Visual Mechanistic Interpretabilit...](http://arxiv.org/abs/2605.17504v1) | 建立分布理论视角，提出KL最小软约束原则模型，通过能量引导扩散后验采样实现 | 建立了视觉机制可解释性的理论分布视角，实验验证所提范式理论合理且实际有效 | — |
| 5 | [Beyond Linear Superposition: Discovering Climate Features in...](http://arxiv.org/abs/2605.17493v1) | 提出KAN-SAE，将编码器的标准ReLU替换为KAN的可学习单特征B样条激活，... | 可获得更多有效特征、更低特征冗余，无监督识别出可解释的典型气候特征 | — |
| 6 | [Event-Grounded Sparse Autoencoders for Vision-Language-Actio...](http://arxiv.org/abs/2605.17204v1) | 提出将稀疏自编码器SAE特征分析锚定到行为事件的事件接地可解释流水线 | 首次将基于SAE的VLA分析锚定到闭环行为事件，多组实验验证了方法有效性 | ✅ |
| 7 | [Mechanistically Interpretable Neural Encoding Reveals Fine-G...](http://arxiv.org/abs/2605.16468v1) | 提出机制可解释神经编码框架MINE，定位驱动体素活动的图像特征，生成可解释体素功... | 建立了可因果验证神经功能细粒度假设的路径，揭示人类视觉皮层的细粒度功能结构 | — |
| 8 | [Reading Task Failure Off the Activations: A Sparse-Feature A...](http://arxiv.org/abs/2605.22719v1) | 构建稀疏特征审计流程，结合统计检验、效应量筛选与三类控制实验验证关联 | 提出廉价、模型无关的稀疏特征审计流程，开放了相关实验代码、语料与数据 | — |
| 9 | [Conceptualizing Embeddings: Sparse Disentanglement for Visio...](http://arxiv.org/abs/2605.22679v1) | 提出后处理方法CEDAR，通过带top-k稀疏瓶颈的可逆变换，不升维实现预训练嵌... | 实现有竞争力的重建-稀疏权衡，所得解释更可解释，更贴合人类感知，无需过完备扩展 | — |
| 10 | [SegCompass: Exploring Interpretable Alignment with Sparse Au...](http://arxiv.org/abs/2605.22658v1) | 提出SegCompass模型，利用稀疏自编码器构建显式可微的可解释对齐路径，联合... | 在五个基准上达到比肩或超越SOTA的性能，实现可检查的增强对齐，提升推理分割可解... | ✅ |
| 11 | [From Correlation to Cause: A Five-Stage Methodology for Feat...](http://arxiv.org/abs/2605.22462v1) | 提出包含探针设计、因果验证等五个阶段的Transformer语言模型因果特征分析... | 提出五阶段因果特征分析方法论，在GPT-2的IOI任务完成端到端验证，证明多阶段... | — |
| 12 | [Geometry-Adaptive Explainer for Faithful Dictionary-Based In...](http://arxiv.org/abs/2605.21849v1) | 提出几何自适应解释器GAE，仅用无标注分布外激活对齐字典，无需梯度更新 | 形式化定义忠实性间隙，证明GAE优于原方法，实验显示其效果超过多数训练基线 | — |
| 13 | [Post-Hoc Understanding of Metaphor Processing in Decoder-Onl...](http://arxiv.org/abs/2605.21391v1) | 提出源自小波的条件尺度熵CSE，度量各层位置Transformer计算在频率尺度... | 证明CSE对更新幅度不变，发现隐喻处理特征，为Transformer跨深度结构分... | — |
| 14 | [From Circuit Evidence to Mechanistic Theory: An Inductive Lo...](http://arxiv.org/abs/2605.21303v1) | 将电路解释视为归纳理论构建，提出因果功能特征CFS，用归纳逻辑编程学习尺度不变架... | 构建了累积机制研究的形式连贯层，使机制主张可明确比较，且可跨模型尺度迁移。 | — |
| 15 | [A Sharper Picture of Generalization in Transformers](http://arxiv.org/abs/2605.20988v1) | 从目标函数傅里叶谱角度切入，先证明低稀疏布尔函数存在平坦极小值，再应用PAC-B... | 证明稀疏低阶谱可构造泛化性良好的低锐度模型，得到非空泛化界，实证支持理论构造的合... | — |
| 16 | [Mechanistic Interpretability for Learning Assurance of a Vis...](http://arxiv.org/abs/2605.20607v1) | 针对视觉着陆Transformer模型，用K-SVD分解嵌入分离内容风格，实现O... | 给出EASA要求的表征级学习保证证据，提出新型OOMS检测满足航空安全要求 | — |
| 17 | [Mechanics of Bias and Reasoning: Interpreting the Impact of ...](http://arxiv.org/abs/2605.20410v1) | 结合基准评估、机械可解释性技术与推理链分析，探究CoT对大语言模型性别偏差的影响 | 证实CoT提示无法持续缩小偏差缺口，揭示其对性别偏差仅为表面缓解而非真正消除 | — |
| 18 | [Where Does Authorship Signal Emerge in Encoder-Based Languag...](http://arxiv.org/abs/2605.19908v1) | 运用机制可解释性工具与因果干预，分析不同评分机制的梯度结构与模型训练动态 | 解释了相同训练条件下作者归因模型的性能差异成因，明确评分机制决定作者信号聚合位置 | — |

## 常见基线方法

- **基于Rademacher复杂度推导泛化界** (2 篇引用)
- **普通稀疏自编码器** (1 篇引用)
- **现有SAE改进变体** (1 篇引用)
- **目标探针扰动TPP** (1 篇引用)
- **伪相关去除SCR** (1 篇引用)
- **k稀疏探测** (1 篇引用)
- **top-K激活检索方法** (1 篇引用)
- **带正则化的优化方法** (1 篇引用)
- **线性基线稀疏自编码器** (1 篇引用)
- **随机对照** (1 篇引用)

## 本周提到的 Limitations

- 即使测试中最可靠的sae-probes，也难以区分同一稀疏自编码器架构的不同变体
- SAE是稀疏但不完美的干预基础，可用性受架构位点影响，激进干预存安全与可解释性限制
- 单阶段特征分析无法得到全面结论，检测鲁棒性与因果鲁棒性之间存在缺口

## 常用数据集

- **摘要未提及** (2 篇使用)
- **SAEBench** (1 篇使用)
- **300条IOI任务提示语料** (1 篇使用)
- **Bloom(2024)层8残差流SAE特征集** (1 篇使用)
- **五个挑战性基准** (1 篇使用)
- **IOI任务数据集** (1 篇使用)
- **VUA数据集** (1 篇使用)
- **LARDv2** (1 篇使用)


---

*自动生成于 2026-05-24 | Research Radar*