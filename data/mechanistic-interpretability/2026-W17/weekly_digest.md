# 机械可解释性 — 2026-W17 (04/20-04/26)

本周新增 **20** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.LG`: 7 篇
- `cs.AI`: 5 篇
- `cs.CL`: 3 篇
- `physics.ed-ph`: 1 篇
- `stat.ML`: 1 篇
- `physics.ao-ph`: 1 篇
- `cs.CR`: 1 篇
- `cs.CV`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Locating acts of mechanistic reasoning in student team conve...](http://arxiv.org/abs/2604.21870v1) | 提出引入特定归纳偏置的可解释概率机器学习模型，结合学生与团队发言识别机械推理 | 证明引入的归纳偏置可提升模型泛化能力，为STEM教育研究提供了实用工具 | — |
| 2 | [There Will Be a Scientific Theory of Deep Learning](http://arxiv.org/abs/2604.21691v1) | 整合梳理深度学习理论领域现有的五大研究脉络，分析其特征并对比不同的理论研究视角 | 论证深度学习科学理论正在逐步形成，提出学习力学这一新兴理论视角，回应了相关质疑 | — |
| 3 | [Mechanistic Interpretability Tool for AI Weather Models](http://arxiv.org/abs/2604.20467v1) | 整合机械可解释性概念，整理模型内部潜在表征，结合余弦相似度、主成分分析开展分析 | 开发出开源高适配性的可解释分析工具，验证了其识别对应气象特征潜在通道组合的能力 | — |
| 4 | [Are LLM Uncertainty and Correctness Encoded by the Same Feat...](http://arxiv.org/abs/2604.19974v1) | 构建沿正确性和置信轴划分预测的2x2框架，采用稀疏自编码器独立识别各维度关联特征 | 识别出三类功能不同的特征群体，证实二者为不同内部现象，靶向干预可提升模型性能 | — |
| 5 | [Towards Understanding the Robustness of Sparse Autoencoders](http://arxiv.org/abs/2604.18756v1) | 推理时将预训练稀疏自编码器集成到Transformer残差流，不修改模型权重也不... | 证实该方法可降低越狱成功率与攻击迁移性，揭示了稀疏性和层位置对防御的影响规律 | — |
| 6 | [Probing for Reading Times](http://arxiv.org/abs/2604.18712v1) | 在涵盖五种语言的两个眼动追踪语料上，使用正则化线性回归对比不同模型层表示与标量预... | 发现最优预测因子因语言和眼动指标不同而异，模型早期层预测早期阅读指标优于标量惊奇... | — |
| 7 | [Committed SAE-Feature Traces for Audited-Session Substitutio...](http://arxiv.org/abs/2604.18179v1) | 提出提交-打开协议，服务商提前提交探测层SAE特征轨迹草图，验证者随机抽样验证一... | 可有效检出各类替换模型的攻击者，额外开销低于2.1%，原基线方法都被攻击者规避 | — |
| 8 | [The Topological Dual of a Dataset: A Logic-to-Topology Encod...](http://arxiv.org/abs/2604.18050v1) | 提出逻辑到拓扑的编码方法，利用观察逻辑，基于可证性与拓扑的对偶性构建输入编码器 | 提出数据集拓扑对偶概念，连通多领域，为神经符号AI的可解释性研究提供了合理路径 | — |
| 9 | [Where is the Mind? Persona Vectors and LLM Individuation](http://arxiv.org/abs/2604.17031v1) | 运用机制可解释性方法，结合近年有关人格向量、人格空间的实证研究展开分析 | 提出两种新的人格相关观点，论证三种观点都是该研究问题的有力候选方案 | — |
| 10 | [Large Language Models Meet Biomedical Knowledge Graphs for M...](http://arxiv.org/abs/2604.19815v1) | 提出整合生物医学知识图谱结构与大语言模型机制推理的混合框架DrugKLM，实现基... | 验证该框架性能优于多个基线，可输出具备机制可解释性与临床依据的可靠治疗假设 | — |
| 11 | [Predicting Where Steering Vectors Succeed](http://arxiv.org/abs/2604.15557v1) | 提出分层诊断工具线性可访问性剖面LAP，无需训练，用模型未嵌入矩阵计算指标预测转... | 实验验证预测指标相关性较高，提出三机制框架说明适用场景，验证其效果优于传统启发式... | — |
| 12 | [Improving Sparse Autoencoder with Dynamic Attention](http://arxiv.org/abs/2604.14925v1) | 基于交叉注意力架构构建新型稀疏自编码器，采用sparsemax动态注意力自动推断... | 该方法实现更低重构损失，同时获得高质量特征概念，在top-n分类任务中表现优异 | — |
| 13 | [Seeing Through Circuits: Faithful Mechanistic Interpretabili...](http://arxiv.org/abs/2604.14477v1) | 提出自动视觉电路发现方法Vi-CD，用于从视觉Transformer中提取特定任... | 证明可从视觉Transformer中恢复出有洞察可操作的基于边的电路，提升了模型... | — |
| 14 | [Causal Drawbridges: Characterizing Gradient Blocking of Synt...](http://arxiv.org/abs/2604.13950v1) | 对Transformer各模块执行因果干预隔离功能相关子空间，投影大语料推导语言... | 证实Transformer可复现人类句法判断，提出连词表征差异新假说，展示可解释... | — |
| 15 | [Weight Patching: Toward Source-Level Mechanistic Localizatio...](http://arxiv.org/abs/2604.13694v1) | 提出权重修补方法，针对能力不同的配对同架构模型，通过替换模块权重做参数空间干预分... | 揭示出目标能力相关模块层级结构，所得评分可指导模型合并，提升了跨专家选择性融合效... | — |
| 16 | [Can Cross-Layer Transcoders Replace Vision Transformer Activ...](http://arxiv.org/abs/2604.13304v1) | 提出采用跨层转码器CLT作为ViT中MLP块的深度感知稀疏代理，重构激活得到分层... | CLT重构保真度高，可保留甚至提升零样本分类精度，跨层贡献分数可实现可信归因 | — |
| 17 | [Interpretable Relational Inference with LLM-Guided Symbolic ...](http://arxiv.org/abs/2604.12806v1) | 提出可微分框架COSINE，联合发现交互图与稀疏符号动力学，结合大语言模型自适应... | 在合成和真实流行病数据上验证，可实现稳健结构恢复，得到符合机制的简洁动力学表达式 | — |
| 18 | [Do Transformers Use their Depth Adaptively? Evidence from a ...](http://arxiv.org/abs/2604.12426v1) | 基于家庭故事构建可控多跳关系推理任务，通过对数透镜与因果补丁法监测模型行为 | 发现预训练模型有有限的自适应深度使用证据，微调后模型该特征更清晰一致，弱约束微调... | — |
| 19 | [Preventing Safety Drift in Large Language Models via Coupled...](http://arxiv.org/abs/2604.12384v1) | 提出耦合权重与激活约束CWAC，同时约束权重更新的预计算安全子空间，对安全关键特... | 理论证明单一约束不足以保障安全，实验表明CWAC优于强基线，有害得分低且对微调精... | — |
| 20 | [The Linear Centroids Hypothesis: How Deep Network Features R...](http://arxiv.org/abs/2604.11962v1) | 提出线性质心假设LCH框架，认为深度网络特征对应输入空间局部区域功能质心的线性方... | 在DINO视觉Transformer得到更稀疏且下游表现更好的特征字典，可识别G... | ✅ |

## 常见基线方法

- **未引入特定归纳偏置组件的训练模型** (1 篇引用)
- **无防御基线模型** (1 篇引用)
- **惊奇值** (1 篇引用)
- **信息价值** (1 篇引用)
- **对数透镜惊奇值** (1 篇引用)
- **SVIP风格并行服务基线** (1 篇引用)
- **仅知识图谱基线方法** (1 篇引用)
- **仅大语言模型基线方法** (1 篇引用)
- **TxGNN** (1 篇引用)
- **标准启发式中间层选层方法** (1 篇引用)

## 本周提到的 Limitations

- 原有线性表示假设LRH忽略个体组件、易识别伪特征，无法跨多个子组件应用

## 常用数据集

- **ARC-Challenge** (1 篇使用)
- **RACE** (1 篇使用)
- **涵盖五种语言的眼动追踪语料1** (1 篇使用)
- **涵盖五种语言的眼动追踪语料2** (1 篇使用)
- **基准数据集** (1 篇使用)
- **12种TCGA癌症数据集** (1 篇使用)
- **24个受控二元概念族** (1 篇使用)
- **实体转向测试样本** (1 篇使用)
- **摘要未提及** (1 篇使用)
- **CIFAR-100** (1 篇使用)


---

*自动生成于 2026-04-26 | Research Radar*