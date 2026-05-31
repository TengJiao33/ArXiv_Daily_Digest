# 机械可解释性 — 2026-W22 (05/25-05/31)

本周新增 **31** 篇论文。1 篇附带代码仓库。

## 分类分布

- `cs.LG`: 16 篇
- `cs.AI`: 6 篇
- `cs.CL`: 3 篇
- `cs.CV`: 2 篇
- `cs.IR`: 2 篇
- `math.DS`: 1 篇
- `cs.CR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Detecting Unfaithful Chain-of-Thought via Circuit-Guided Int...](http://arxiv.org/abs/2605.25603v1) | 提出CIE-Scorer框架，追踪紧凑句级电路构建内外推理图，用FGW距离衡量差... | 在FaithCoT-Bench的四个数据集上取得SOTA性能，同时有效降低了电路... | — |
| 2 | [SAE-FD: Sparse Autoencoder Feature Distillation for Continua...](http://arxiv.org/abs/2605.25525v1) | 提出稀疏自编码器特征蒸馏SAE-FD，锚定稀疏特征空间分解激活减少纠缠，实现针对... | 在两个基准三个模型架构实验，性能优于现有正则化方法，最高获52.70%平均准确率... | — |
| 3 | [Continuous-Depth Field Theory for Transformer Patching and M...](http://arxiv.org/abs/2605.25225v1) | 将残差流视为深度-词元场，构建场论框架，把各类修补干预转化为场论相关问题处理 | 建立了敏感度、传播场、格林算子切片等响应对象，为修补实验及相关推理提供数学基础 | — |
| 4 | [Universal Boosts, Specific Suppressors: Sparse Autoencoder S...](http://arxiv.org/abs/2605.24977v1) | 无需更新模型权重，推理阶段基于逐token稀疏自编码器做残差引导，结合抑制增强干... | 所提方法提升多类放射医学VLM报告质量，可零样本迁移，已发布相关特征集与交互工具 | — |
| 5 | [The Concept Allocation Zone: Tracking How Concepts Form Acro...](http://arxiv.org/abs/2605.24856v1) | 提出概念分配区(CAZ)，基于三个分层度量实现无需手动遍历的自动区间边界检测 | 引入概念分配区检测框架，经多架构多模型验证，提出七个可检验的研究预测 | — |
| 6 | [Polymorphism Is Rotation: Operational Mechanistic Interpreta...](http://arxiv.org/abs/2605.24577v1) | 对单批次激活做正交Procrustes拟合得到旋转矩阵，对齐不同独立训练模型的内... | 发现同功能独立训练Transformer残差基差异为均匀随机旋转，一次旋转即可实... | — |
| 7 | [Learning dynamical systems with biochemically informed neura...](http://arxiv.org/abs/2605.24170v1) | 提出整合生化先验信息的神经常微分方程BINODEs，保留机理计量结构，用神经网络... | 所提框架可融入生物侧信息，在多个经典模型中可准确恢复系统轨迹与过程级结构 | — |
| 8 | [Every Component is a Lookup: Token Attribution and Compositi...](http://arxiv.org/abs/2605.23393v1) | 利用注意力与MLP共享的键值模板结构，开发Unpack反向递归分解，单次前向得结... | 可得到任意组件交互强度、标注端到端路径和逐token归因，多规模模型验证方法有效 | ✅ |
| 9 | [Steered Generation via Gradient-Based Optimization on Sparse...](http://arxiv.org/abs/2605.23040v1) | 提出原型基稀疏引导框架，将稀疏自动编码器用于注意力查询激活，推理时梯度优化对齐目... | 通过实验验证，稀疏查询特征可实现特征解耦，支持对逻辑规划与风格细节的统一可解释控... | — |
| 10 | [Multilingual Steering by Design: Multilingual Sparse Autoenc...](http://arxiv.org/abs/2605.23036v1) | 在多语言数据上训练稀疏自动编码器，基于多语言对齐与语言可分性交集设计先验引导层选... | 稳定了语言识别准确率与生成质量的权衡，提供了原则性可预测的多语言SAE引导的表示... | — |
| 11 | [Sparse Autoencoders Map Brain-LLM Alignment onto Cortical Se...](http://arxiv.org/abs/2605.23035v1) | 将机制可解释性领域的稀疏自编码器与神经编码模型结合，分解大语言模型得到可解释特征... | 证明稀疏自编码器发现的特征可重现更细粒度的皮层语义组织，结果可跨多语言推广。 | — |
| 12 | [Transcoders Trace Visual Grounding and Hallucinations in Vis...](http://arxiv.org/abs/2605.22902v1) | 采用基于Transcoders的功能中心框架，分解连接图像到文本生成的可解释计算... | 验证所提方法归因效果优于SAE，可借助分解特征预测视觉语言模型的幻觉生成 | — |
| 13 | [Towards Verifiable Transformers: Solver-Checkable Circuit Ex...](http://arxiv.org/abs/2605.24033v1) | 提出可验证Transformer框架，将任务局部电路转换为SMT求解器可验证的断... | 给出了将Transformer机械电路解释转换为可证伪形式命题的具体路径，验证了... | — |
| 14 | [Guiding LLM Post-training Data Engineering with Model Intern...](http://arxiv.org/abs/2605.27354v1) | 提出SAERL框架，利用稀疏自动编码器提取模型内部信息，实现多维度后训练数据工程... | 所提框架有效提升大模型强化学习性能，验证了模型内部信号是后训练工程的有效信号源。 | — |
| 15 | [MechRL: Reinforcement Learning Agents Perform Circuit Discov...](http://arxiv.org/abs/2605.26343v1) | 将电路发现重构为强化学习问题，采用单PPO策略在向量化多任务环境训练智能体。 | 验证了基于因果干预的强化学习是可行可迁移的电路识别方案，可互补现有路径修补方法。 | — |
| 16 | [BioRefusalAudit: Auditing Biosecurity Refusal Depth Using Ge...](http://arxiv.org/abs/2605.30162v1) | 采用通用及领域微调稀疏自编码器，计算差异得分D对比模型表面响应与内部激活进行审计 | 提出生物安全拒绝深度审计方法，发布两个微调领域稀疏自编码器，指出激活层审计可发现... | — |
| 17 | [No More K-means:Single-Stage Sparse Coding for Efficient Mul...](http://arxiv.org/abs/2605.30120v1) | 提出单阶段稀疏检索SSR，用稀疏自编码器获得高维稀疏表示，依托倒排索引实现检索 | 在BEIR基准上实现三重提升，降低索引与检索延迟，同时提升了检索性能 | — |
| 18 | [Robust and Generalizable Safety Steering for Text-to-Image D...](http://arxiv.org/abs/2605.30049v1) | 提出SafeDIG安全引导框架，将DiT安全适配建模为位置感知稀疏特征迁移，推理... | 在主流DiT模型验证，该框架可降低不安全生成率，同时保留原有安全性与图像生成质量 | — |
| 19 | [Dissecting the Black Box: Circuit-Level Analysis of LLM Vuln...](http://arxiv.org/abs/2605.29901v1) | 采用机制可解释性方法，借助Circuit Tracer追踪模型计算通路，结合消融... | 识别出漏洞检测的关键神经组件，揭示LLM漏洞检测依赖稀疏可解释电路，为优化提供支... | — |
| 20 | [Latent Terms: Dense Retrievers Contain Trivially Extractable...](http://arxiv.org/abs/2605.29384v1) | 提出潜在词方法，用无检索特定调整的稀疏自编码器从稠密检索器分解出适配BM25的稀... | 可适配任意稠密检索器，性能匹配或优于现有方法，在LIMIT任务大幅超越基准单向量... | — |
| 21 | [Scaling Monosemanticity: Extracting Interpretable Features f...](http://arxiv.org/abs/2605.29358v1) | 借助缩放定律指导超参数选择，在Claude 3 Sonnet中间层残差流训练稀疏... | 成功从Claude 3 Sonnet提取出多语言多模态可解释特征，可用于引导模型... | — |
| 22 | [When and How Long? The Readout-Mediator Angle in Temporal Re...](http://arxiv.org/abs/2605.29126v1) | 计算读出子空间与因果中介子空间夹角，结合逆向电路分析与稀疏自编码分解验证 | 发现读出-中介正交性是探针类可解释方法的通用失效模式，指出探针用于安全监测存在缺... | — |
| 23 | [Interpretability-Guided Layer Selection over Subspace Projec...](http://arxiv.org/abs/2605.28649v1) | 利用SAE进行层级别诊断得到特异性得分，仅向筛选出的层注入未过滤的原始任务向量。 | 提出了可解释性引导的模型编辑新框架，在数学推理基准取得显著性能提升，无额外推理成... | — |
| 24 | [Semantic Optimal Transport for Sparse Autoencoder Feature Ma...](http://arxiv.org/abs/2605.28567v1) | 将每个特征表示为激活加权分布，投影到共享空间用沃瑟斯坦距离计算语义距离 | 提出统一语义度量方法，理论证明其优良性质，实验表现优于已有基线方法 | — |
| 25 | [Cultural Binding Heads in Language Models](http://arxiv.org/abs/2605.28543v1) | 采用机制可解释性结合因子设计，基于N4文化挪用基准分析八个大语言模型的注意力头 | 识别出影响文化绑定的中层注意力头，揭示文化绑定形成于预训练，输出瓶颈在路由而非知... | — |
| 26 | [Mechanistically Interpreting the Role of Sample Difficulty i...](http://arxiv.org/abs/2605.28388v1) | 采用分难度分析、单样本分析与时序稀疏自编码器分析RLVR，提出难度自适应硬样本利... | 明确样本难度是支配RLVR优化动态与表示演化的关键因素，提出改进RLVR的难度自... | — |
| 27 | [Feature Geometry of LoRA Adapters: A Sparse Autoencoder Anal...](http://arxiv.org/abs/2605.28896v1) | 引入delta激活框架分离适配器贡献，利用稀疏自编码器分析LoRA诱导表征的几何... | 获得LoRA诱导表征结构的实证发现，对大语言模型可解释性等研究具有参考意义。 | — |
| 28 | [Sign-Aware Gated Sparse Autoencoders: Modeling Anticorrelate...](http://arxiv.org/abs/2605.28149v1) | 提出符号感知门控稀疏自动编码器SA-GSAE，采用双侧门控，搭配新型Bi-Jum... | 实现反相关特征的双极共享，保持参数高效，性能优于基线，大幅降低死神经元比例 | — |
| 29 | [Where Does Toxicity Live? Mechanistic Localization and Targe...](http://arxiv.org/abs/2605.27997v1) | 提出Meow2X与TRNE两个无需重训练的框架，定位毒性到特定神经元后在推理阶段... | 打通机制可解释性与实际解毒路径，验证可在保留模型性能的同时有效降低毒性 | — |
| 30 | [ReSAE: Residualized Sparse Autoencoders for Multi-Layer Tran...](http://arxiv.org/abs/2605.27819v1) | 提出残差稀疏自编码器ReSAE，跨层拟合仿射映射，基于未解释残差训练后层稀疏自编... | 该方法降低解码器冗余，提升多数场景下的任务性能，多层替换可恢复更多Transfo... | — |
| 31 | [Residualized Temporal Sparse Autoencoders for Interpreting D...](http://arxiv.org/abs/2605.27813v1) | 提出残差化时序稀疏自编码器，将扩散模型完整激活轨迹做残差化表示后训练稀疏自编码器 | 提供了研究扩散模型时序结构化激活的有效框架，经多类实验验证了框架的实用性 | — |

## 常见基线方法

- **基于外部信号的CoT不忠实检测器** (1 篇引用)
- **全推理电路构建的电路追踪方法** (1 篇引用)
- **现有基于正则化的持续学习方法** (1 篇引用)
- **RadVLM** (1 篇引用)
- **LLaVA-Rad** (1 篇引用)
- **CheXOne** (1 篇引用)
- **标准峰值检测方法** (1 篇引用)
- **标准SAE通用性度量** (1 篇引用)
- **常数均值预测** (1 篇引用)
- **匹配控制提示** (1 篇引用)

## 本周提到的 Limitations

- 提出的七个可检验预测中，一个预测前提失效，两个预测存在统计功效不足的问题
- 仅在小参数模型完成验证，10B以上参数规模的前沿模型复现仍未完成
- GPT-2及更大规模模型下，原生直接SMT验证仍然难以处理，存在可处理性瓶颈
- 仅覆盖Gemma家族模型，测试范围窄，仅做样本内校准，研究结论为初步结果
- 提取的特征集合不完备，缺乏严格方法评估特征是否忠实捕获模型的计算过程
- 全宽度SA-GSAE在SmolLM3-3B残差位置会出现可复现的重构崩溃

## 常用数据集

- **摘要未提及具体数据集** (3 篇使用)
- **FaithCoT-Bench** (1 篇使用)
- **两个持续学习基准数据集** (1 篇使用)
- **MIMIC-CXR** (1 篇使用)
- **IU-Xray** (1 篇使用)
- **Dyck-3** (1 篇使用)
- **The Pile** (1 篇使用)
- **间接宾语识别任务** (1 篇使用)
- **Textualized Gridworld** (1 篇使用)
- **高维教育领域数据集** (1 篇使用)


---

*自动生成于 2026-05-31 | Research Radar*