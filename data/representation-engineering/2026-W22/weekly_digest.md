# 表示工程、激活引导与价值对齐干预 — 2026-W22 (05/25-05/31)

本周新增 **31** 篇论文。1 篇附带代码仓库。

## 分类分布

- `via-citation`: 12 篇
- `cs.CL`: 8 篇
- `cs.AI`: 5 篇
- `cs.LG`: 4 篇
- `cs.CR`: 1 篇
- `cs.MM`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Causal Tongue-Tie: LLMs Can Encode Causal Direction, But The...](http://arxiv.org/abs/2605.25891v1) | 使用固定线性探针从大语言模型隐藏状态提取因果信息，与模型Yes/No输出对比分析 | 指出大语言模型编码因果信息与输出存在错配，仅靠输出准确率评估因果推理能力并不合理 | — |
| 2 | [Is Inference Mediated by Distinct Semantic Structures in LLM...](http://arxiv.org/abs/2605.25520v1) | 使用单语义变换的控制推理样本，经SVD估计操作子空间，通过激活引导测试其因果相关... | 发现大模型不仅编码推理关系还部分编码语义操作，提出机制分析应在语义操作层面展开 | — |
| 3 | [Representation Without Control: Testing the Realization Effe...](http://arxiv.org/abs/2605.25151v1) | 以行为经济学的实现效应为研究对象，从三个层级评估大语言模型的行为表现 | 明确三类属性不会自动共存，成功潜在读出不足以证明模型决策依赖对应表征 | — |
| 4 | [Memory-Induced Tool-Drift in LLM Agents](http://arxiv.org/abs/2605.24941v1) | 构建包含105个场景的MEMDRIFT基准，在多类前沿模型与真实工具中开展实验分... | 发现记忆诱导工具漂移这一新的系统漏洞，揭示其作用机制，指出现有防护无法彻底消除该... | — |
| 5 | [An Effective-Rank Audit of Alignment-Induced Activation Shif...](http://arxiv.org/abs/2605.24583v1) | 利用对齐修正矩阵的有效秩，结合四变量分解、三层MLP校准开展分析 | 提出混杂控制测量方法，给出有效秩校准特性，明确秩诊断方法的适用边界 | — |
| 6 | [Polymorphism Is Rotation: Operational Mechanistic Interpreta...](http://arxiv.org/abs/2605.24577v1) | 对不同独立训练模型的单批次激活做正交Procrustes拟合，得到旋转矩阵实现跨... | 提出Transformer多态性概念，发现残差基为均匀随机旋转，单个旋转即可对齐... | — |
| 7 | [Palette: A Modular, Controllable, and Efficient Framework fo...](http://arxiv.org/abs/2605.24154v1) | 提出模块化Palette框架，多目标搜索获取拒绝方向轻量适配，支持模块化参数合并... | 实现精准安全控制不牺牲通用效用，无需重训即可按需多域授权，适配多样化专业需求 | — |
| 8 | [DFKI-MLT at SemEval-2026 TASK 7: Steering Multilingual Model...](http://arxiv.org/abs/2605.23069v1) | 采用激活引导方法，推理时在选定transformer层添加提取自平行数据的语言专... | 参与SemEval-2026任务7双赛道，MCQ赛道获86.96%准确率，位列1... | — |
| 9 | [Multilingual Steering by Design: Multilingual Sparse Autoenc...](http://arxiv.org/abs/2605.23036v1) | 训练多语言稀疏自编码器，提出基于多语言对齐与语言可分性交集的先验选层规则 | 所提方法稳定语言识别准确率与生成质量的权衡，提供多语言SAE引导的原则性解释 | — |
| 10 | [Reading Calibrated Uncertainty from Language Model Trajector...](http://arxiv.org/abs/2605.22864v1) | 提取11个尺度不变几何特征追踪每层MLP更新的累积路径，输入稀疏线性探针评估不确... | 所提稀疏线性探针性能优于基线，最高提升AURC达21个点，还可追溯误差的形成过程... | — |
| 11 | [Universal Boosts, Specific Suppressors: Sparse Autoencoder S...](http://arxiv.org/abs/2605.24977) | 无需更新模型权重，推理时基于逐标记稀疏自编码器做解码残差引导，结合抑制增强干预 | 所提方法有效提升多种放射VLM的报告生成质量，可零样本迁移，已发布相关工具资源 | — |
| 12 | [Riemannian-Manifold Steering: Geometry-Aware Generative Auto...](http://arxiv.org/abs/2605.24942) | 将流形引导重构为激活空间的黎曼测地线计算，基于海林格距离学习无标签编码器 | 提出统一的黎曼流形引导框架，实现无需标注质心与预设边界条件的无标签引导 | — |
| 13 | [Causal Physics Steering in Video World Models via Concept Ac...](http://arxiv.org/abs/2605.24322) | 提出无训练的物理引导方法，将PEZ层线性探针权重作为CAV注入推理阶段的隐藏状态 | 验证该干预可偏移模型物理判断，证明VideoMAE中的物理推理可读且可直接引导 | — |
| 14 | [Steered Generation via Gradient-Based Optimization on Sparse...](http://arxiv.org/abs/2605.23040) | 提出基于原型的稀疏引导框架，将稀疏自动编码器用于注意力查询激活，推理时梯度优化对... | 验证稀疏查询表示可实现特征解耦，能统一可解释地控制逻辑规划与风格细节 | — |
| 15 | [TRACE: Trajectory Correction from Cross-layer Evidence for H...](http://arxiv.org/abs/2605.18163) | 提出无需训练的TRACE算法，推理时基于模型内部跨层候选轨迹选择合适算子修正幻觉 | 在15个模型3个事实基准上所有评测单元均获提升，无需标签检索微调等额外步骤 | — |
| 16 | [Reinforcing Human Behavior Simulation via Verbal Feedback](http://arxiv.org/abs/2605.20506) | 提出DITTO模型，将口头反馈作为强化学习一级信号，使用GRPO联合优化蒸馏策略 | 提出DITTO模型与统一基准套件SOUL，验证了带口头反馈强化学习的提升效果 | — |
| 17 | [Position: AI Safety Requires Effective Controllability](http://arxiv.org/abs/2605.27117) | 提出将可控性作为AI安全一级目标，引入可控性评测基准ControlBench，提... | 明确定义AI可控性概念，推出可控性评测基准，提出可控AI系统核心设计原则 | — |
| 18 | [Unsupervised Identification and Removal of Spurious Correlat...](http://arxiv.org/abs/2605.27676) | 提出GRASP方法，对关联虚假模式做梯度投影，去除虚假相关同时保留预训练真实信号 | 在三个微调任务上验证有效性，去偏差与任务保留的权衡表现优于所有对比基线 | — |
| 19 | [Can LLMs Introspect? A Reality Check](http://arxiv.org/abs/2605.26242) | 重新审视两个已有的内省能力评估范式，新增重标记控制设置开展对照实验验证 | 指出仅行为证据不足以证实强内省主张，现有证据无法证明大模型具备元认知监控 | — |
| 20 | [PathCal: State-Aware Reflection-Marker Calibration for Effic...](http://arxiv.org/abs/2605.23074) | 提出无训练的解码控制器PathCal，区分反射标记类型，仅在局部不确定状态校准推... | 在六个推理基准实现更优效率-性能权衡，无需额外资源即可提升精度并缩短生成长度。 | — |
| 21 | [Multi-Adapter Representation Interventions via Energy Calibr...](http://arxiv.org/abs/2605.28722) | 提出基于能量校准的多适配器表征干预，自适应为不同样本确定合适的干预方向与强度。 | 在多类模型和多个基准实验取得SOTA对齐性能，提升目标表现同时保持甚至提升通用能... | ✅ |
| 22 | [UniSteer: Text-Guided Flow Matching in Activation Space for ...](http://arxiv.org/abs/2605.30076) | 提出UniSteer，学习激活空间的通用条件速度场，推理时依文本调整激活后注入冻... | 为多类大语言模型控制与分类任务提供统一接口，在三个目标LLM上验证了有效性 | — |
| 23 | [Unveiling the Visual Counting Bottleneck in Vision-Language ...](http://arxiv.org/abs/2605.30170v1) | 将视觉计数拆解为三个认知阶段，使用合成围棋棋盘与线性探针开展实验分析 | 定位了视觉计数失败的根源，提出碎裂量级假说，指出仅数据缩放无法解决该问题 | — |
| 24 | [Causal Interventions on Continuous Variables: A Case Study o...](http://arxiv.org/abs/2605.29971v1) | 基于与分级目标变量配对的激活向量定位低维方向，沿该方向编辑向量得到反事实目标值 | 提出面向连续变量的因果干预方法，验证大语言模型转向向量存在可干预的动词偏向因果表... | — |
| 25 | [Beyond Attack Success Rate: Temporal Logit Observability for...](http://arxiv.org/abs/2605.29629v1) | 提出无训练的时序对数可观测性TLO，解码时监控合规拒绝裕度，将模型攻击情况映射到... | 实现仅从对数观测大模型安全失败的演化过程，基于TLO的早停可减少超半数成功越狱且... | — |
| 26 | [When and How Long? The Readout-Mediator Angle in Temporal Re...](http://arxiv.org/abs/2605.29126v1) | 结合DAS、消融实验、电路逆向工程、稀疏自编码器分解计算读出-调解子空间夹角 | 揭示基于探针的可解释性方法普遍存在读出-调解子空间正交的失效模式，影响安全监测应... | — |
| 27 | [Refusal Before Decoding: Detecting and Exploiting Refusal Si...](http://arxiv.org/abs/2605.28553v1) | 在每个transformer块残差流激活上训练线性探针，提出探针引导的Mecha... | 证明拒绝信号是可利用的结构化中间激活信号，新方法效率提升且效果媲美原有方法 | — |
| 28 | [Rethinking Visual Neglect: Steering via Context-Preference f...](http://arxiv.org/abs/2605.27993v1) | 提出无训练的上下文偏好激活引导框架CAS，提取偏好向量推理时注入残差调控信息依赖 | 所提方法可大幅缓解物体幻觉，不增加解码延迟，同时保留模型原生文本生成质量 | — |
| 29 | [Pressure-Testing Deception Probes in LLMs: Scaling, Robustne...](http://arxiv.org/abs/2605.27958v1) | 针对四种欺骗编码假设，在Gemma 3模型家族开展多类压力测试与假设检验。 | 系统开展探针压力测试，诊断其失效原因，揭示了大模型欺骗表征的几何性质。 | — |
| 30 | [Beyond a Single Direction: Chain-of-Thought Disrupts Simple ...](http://arxiv.org/abs/2605.26772v1) | 设置固定CoT、移除CoT、干预再生CoT三种场景，开展激活转向实验验证 | 证明大推理模型的拒绝行为由残差流激活与思维链共同编码，揭示CoT的独立作用 | — |
| 31 | [Cultural Value Alignment Via Latent Activation Steering in L...](http://arxiv.org/abs/2605.26365v1) | 提出基于场景行为探测的文化评估干预框架，通过激活引导无需重训练即可调整文化对齐 | 建立计算高效的大语言模型文化引导框架，揭示大模型文化价值编码的结构复杂性 | — |

## 常见基线方法

- **大语言模型Yes/No输出** (1 篇引用)
- **随机子空间** (1 篇引用)
- **无偏基准** (1 篇引用)
- **基于提示的相关性指令** (1 篇引用)
- **内存过滤器** (1 篇引用)
- **LRH基线方法** (1 篇引用)
- **Arditi等人单拒绝方向方法** (1 篇引用)
- **标准SAE通用性度量** (1 篇引用)
- **常数均值预测** (1 篇引用)
- **高成本重对齐方法** (1 篇引用)

## 本周提到的 Limitations

- 现有标准防护仅能减轻记忆诱导工具漂移，无法彻底消除，当前防护体系未解决该漏洞
- 秩诊断无安全特异性，SVD主排序不匹配因果排序，匹配下界问题仍未解决
- 目前仅在小规模模型上验证，百亿参数以上前沿规模模型的结论复现仍未完成
- 激活引导带来的提升有限且异质，具有层敏感性，部分配置反而会降低模型性能。
- 仅依靠数据缩放无法解决视觉语言模型的视觉计数外推瓶颈问题
- 将连续变量相关研究与上下文学习建立有效连接目前仍然是未解决的挑战
- 所提出的固定词典方法存在局限性，在单个模型上无法匹配隐藏状态拒绝方向探测结果
- 大语言模型的文化价值以耦合结构编码，限制了文化价值对齐的精确度

## 常用数据集

- **CLadder** (1 篇使用)
- **MEMDRIFT基准数据集** (1 篇使用)
- **MCP服务器工具集** (1 篇使用)
- **Dyck-3** (1 篇使用)
- **The Pile** (1 篇使用)
- **FLORES** (1 篇使用)
- **CrossSumm** (1 篇使用)
- **MIMIC-CXR** (1 篇使用)
- **IU-Xray** (1 篇使用)
- **四任务语言模型算术基准** (1 篇使用)


---

*自动生成于 2026-05-31 | Research Radar*