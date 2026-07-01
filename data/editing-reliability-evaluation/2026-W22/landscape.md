# 📡 编辑可靠性与行为控制 — 方法版图
> 2026-W22 (05/25-05/31) | 本周 30 篇 | 自动生成

📊 **10** 个方法族 | **27** 篇 high priority | **6** 篇附带代码

---

### 🔬 locate-then-edit（8 篇）

- **现有多模态知识编辑问题源于因果错位和特征缠结，定位加解缠可同时提升编辑泛化性和局部性。** ⭐
  _[Towards Localized and Disentangled Knowledge Editing for Multimod...](http://arxiv.org/abs/2605.29826v1)_

  - 评测信号：在多个基准和不同MLLM上评测，验证方法向相关上下文传播编辑同时保持高局部性的性能。
  - 失败模式：因果错位导致编辑泛化不足，特征纠缠引发无关信息意外编辑

- **将任务向量投影到SAE特征子空间会丢弃约97%的修改能量，失效源于SAE激活方向与权重空间任务向量几何不对齐** ⭐
  _[Interpretability-Guided Layer Selection over Subspace Projection:...](http://arxiv.org/abs/2605.28649v1)_

  - 评测信号：在Minerva Math基准7个数学推理科目评测，5个科目显著提升，无显著下降，方法无额外推理成本
  - 失败模式：任务向量投影到SAE特征子空间形成信息瓶颈，丢弃大量修改能量导致编辑无效

- **相关上下文多任务RL设置中，网络仅用约1.5%的权重区分任务，其中约85%连接输入上下文变量与隐层。**
  _[Task-specific Subnetwork Discovery in Reinforcement Learning for ...](http://arxiv.org/abs/2604.21640v1)_

  - 评测信号：通过分析预训练多任务强化学习网络的内部权重分布，揭示任务区分的结构特性
  - 失败模式：多任务强化学习策略不透明，可解释性不足，阻碍实际落地部署

- **LightEdit结合选择性知识选择与解码抑制，在三个基准上性能优于现有方法，训练成本更低可扩展性更强** ⭐
  _[Towards Scalable Lifelong Knowledge Editing with Selective Knowle...](http://arxiv.org/abs/2604.19089v1)_

  - 评测信号：在ZSRE、Counterfact、RIPE三个基准上对比现有方法，评测编辑性能、可扩展性与训练成本
  - 失败模式：顺序编辑发生灾难性遗忘，现有方法可扩展性差，检索类方法训练成本高

- **HiEdit每次编辑仅扰动一半层数，性能比竞争方法RLEdit平均提升8.48%，自适应选层效果更优。** ⭐
  _[HiEdit: Lifelong Model Editing with Hierarchical Reinforcement Le...](http://arxiv.org/abs/2604.11214v1)_

  - 评测信号：评测模型编辑后的性能，同时统计每次编辑的参数扰动规模，验证方法的性能与效率优势。
  - 失败模式：忽略知识存储的层特异性，顺序编辑中易引发灾难性遗忘，降低新知识集成适应性。

- **Transformer中公式和描述集中在较早层，实例与中间层关联更强，DMLE比最强基线平均提实例迁移13.91、规则理解50.19个百分点** ⭐ 💻
  _[Distributed Multi-Layer Editing for Rule-Level Knowledge in Large...](http://arxiv.org/abs/2604.08284v1)_

  - 评测信号：在GPT-J-6B等四个主流大模型上评测，验证方法在实例可迁移性、规则理解上的性能提升
  - 失败模式：单一层/连续块干预编辑，无法可靠编辑跨多形式的规则层知识

- **识别特定推理任务的因果电路后，仅更新该电路内参数即可有效解决知识编辑后的推理鸿沟问题** ⭐
  _[Mechanistic Circuit-Based Knowledge Editing in Large Language Mod...](http://arxiv.org/abs/2604.05876v1)_

  - 评测信号：在MQuAKE-3K基准上评测所提方法在知识编辑后多跳推理任务的效果，验证了方法的有效性
  - 失败模式：现有知识编辑方法存在推理鸿沟，编辑后无法将事实应用到多步推理中

- **同一主体知识编辑泛化崩溃的几何根源是提示变化引发的激活漂移超出编辑后模型的泛化容差，标准协方差约束会形成协方差陷阱放大扰动** ⭐
  _[Beyond the Covariance Trap: Unlocking Generalization in Same-Subj...](http://arxiv.org/abs/2603.15518)_

  - 评测信号：重点评测方法提升同一主体知识编辑后，模型在不同用户指令下召回更新知识的泛化鲁棒性
  - 失败模式：同一主体知识编辑后，提示变化引发激活漂移导致泛化崩溃，无法召回更新知识


### 🔬 evaluation/benchmark（7 篇）

- **带共享协方差的向量求和是最可靠策略，大于默认的权重缩放、较低秩通常能获得更优性能** ⭐
  _[Merging Methods for Multilingual Knowledge Editing for Large Lang...](http://arxiv.org/abs/2605.13919v1)_

  - 评测信号：在大规模批量编辑场景下，评测不同向量合并方法的性能、抗干扰能力及超参数对性能的影响
  - 失败模式：多语言编辑之间相互串扰

- **恶意知识编辑可稳定诱导错误不安全推理，还能保留大模型通用能力，风险难检测，受三类关键因素影响** ⭐
  _[Benchmarking Safety Risks of Knowledge-Intensive Reasoning under ...](http://arxiv.org/abs/2605.10146v1)_

  - 评测信号：从攻击有效性、推理正确性、副作用三个维度，评测恶意知识编辑对知识密集推理的安全风险
  - 失败模式：现有基准缺乏对恶意知识编辑安全风险的系统评估，恶意编辑引发的风险难以检出

- **EIC源于现有方法无法区分I-E绑定与E-E关系知识，约束I-E阶段编辑可大幅降低EIC。** ⭐
  _[Uncovering Entity Identity Confusion in Multimodal Knowledge Edit...](http://arxiv.org/abs/2605.06096v1)_

  - 评测信号：构建诊断基准EC-Bench，探测编辑前后图像-实体绑定的偏移，分析实体混淆问题。
  - 失败模式：实体身份混淆，原实体身份的纯文本查询会意外返回新实体信息

- **在隐式表述依赖的最难案例中，五种LLM编辑系统ERA为0.148-0.705，最强模型仍漏约30%所需更新** ⭐
  _[EditPropBench: Measuring Factual Edit Propagation in Scientific M...](http://arxiv.org/abs/2605.02083v2)_

  - 评测信号：构建带句子级标注的事实图评测基准，提出ERA指标衡量所需下游更新的正确修改比例
  - 失败模式：局部事实修改后，依赖该事实的非局部隐式主张未同步更新，编辑传播不完整

- **当前知识编辑普遍存在表面合规，仅模仿目标输出未修改内部信念，递归修改会累积残留降低记忆可逆性** ⭐ 💻
  _[The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance...](http://arxiv.org/abs/2604.05995v1)_

  - 评测信号：关注大语言模型知识编辑是否完成真正的结构性记忆修改，检测表面合规问题与递归编辑的副作用
  - 失败模式：知识编辑仅表面合规未真修改内部信念，递归编辑累积残留引发认知不稳定，降低记忆可逆性

- **构建了覆盖多元伦理框架的道德判断编辑评估基准，可系统评测现有模型编辑技术的能力。**
  _[CounterMoral: Editing Morals in Language Models](http://arxiv.org/abs/2603.27338)_

  - 评测信号：提出CounterMoral基准，可评测现有模型编辑技术修改不同伦理框架下道德判断的效果。

- **SFT和RLHF易引发灾难性遗忘，知识编辑能更好保留通用能力，但在持续更新中存在明显局限** ⭐
  _[MMKU-Bench: A Multimodal Update Benchmark for Diverse Visual Know...](http://arxiv.org/abs/2603.15117)_

  - 评测信号：提供覆盖两类知识更新场景的综合基准，可系统评测不同多模态知识更新方法的能力表现
  - 失败模式：灾难性遗忘、持续更新能力不足


### 🔬 framework/tooling（6 篇）

- **现有零空间编辑方法因依赖近似零空间固有存在知识泄露，历史感知更新可有效缓解长程顺序编辑的性能衰退。** ⭐
  _[BetaEdit: Null-Space Constrained Sequential Model Editing](http://arxiv.org/abs/2605.09285v1)_

  - 评测信号：在两个标准基准的三个大语言模型上开展实验，验证所提方法在大规模顺序编辑中的性能优势。
  - 失败模式：知识泄露、大规模顺序编辑过程中的性能严重衰退

- **合成设置中可可靠恢复注入的已知行为变化，真实场景能区分大小干预，无效应时不产生幻觉差异** ⭐
  _[Automatically Finding and Validating Unexpected Side-Effects of I...](http://arxiv.org/abs/2605.05090v1)_

  - 评测信号：验证该方法能可靠识别干预的预期与意外副作用，无效应时不幻觉差异，可区分不同程度的干预
  - 失败模式：难以自动化发现干预的意外副作用，易幻觉出不存在的行为差异

- **匹配预算下，HiP-LoRA大幅降低预训练能力退化和多适配器融合失败，在干扰敏感任务优于基线** ⭐
  _[HiP-LoRA: Budgeted Spectral Plasticity for Robust Low-Rank Adapta...](http://arxiv.org/abs/2604.17751v1)_

  - 评测信号：评测预训练能力保留程度与多适配器融合效果，在持续调优、知识编辑任务验证方法鲁棒性
  - 失败模式：谱干扰引发预训练能力退化、灾难性遗忘、多适配器融合失败

- **将离散事实锚定在Transformer浅层、仅最小更新深层，可兼顾整体编辑性能与细粒度事实访问效果** ⭐ 💻
  _[FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](http://arxiv.org/abs/2604.12559v1)_

  - 评测信号：推出带细粒度问答对与事实级指标的诊断基准UnFine，评测方法的细粒度问答与整体编辑性能
  - 失败模式：现有非结构化模型编辑后缺乏可靠的细粒度事实访问能力

- **批序式编辑退化源于非目标参数的意外修改，B-EAC相对无压缩方案实现36.54%性能提升。** ⭐
  _[Reliable Batch-Sequential Model Editing via Enhanced Editing Anch...](https://www.semanticscholar.org/paper/973ec58e15df38145de8a202bb7f26b8c697abb3)_

  - 评测信号：在三个大语言模型的四个任务上开展实验，验证方法对编辑偏移的抑制效果与性能提升。
  - 失败模式：批序式多知识编辑导致模型通用能力偏移，甚至引发能力崩溃

- **KEditVis能够帮助用户选择合适的编辑目标层，探索无效编辑的原因，实现更精准有效的知识编辑** ⭐
  _[KEditVis: A Visual Analytics System for Knowledge Editing of Larg...](http://arxiv.org/abs/2603.29689)_

  - 评测信号：通过使用场景分析、专家访谈与用户研究三种方式，验证了KEditVis系统的有效性与可用性
  - 失败模式：难以确定最优编辑层，编辑策略选择缺乏透明有效的指导


### 🔬 other（3 篇）

- **原静态知识覆盖范式自我反驳率达95.6%，本文CODE方法可将其降至1.8%，多跳准确率可达83.5%。** ⭐ 💻
  _[From Fact Overwriting to Knowledge Evolution: Causal Editing via ...](http://arxiv.org/abs/2605.28303v1)_

  - 评测信号：在LLaMA-3.1和Qwen-2.5两个大模型上评测了自我反驳率与多跳推理准确率，验证方法效果。
  - 失败模式：静态事实覆盖破坏模型知识拓扑，引发认知失调，导致模型出现高自我反驳率。

- **标准SFT仅保留1%基础模型原有能力时，MixSD可100%保留原有能力同时维持近乎完美的训练准确率** ⭐
  _[MixSD: Mixed Contextual Self-Distillation for Knowledge Injection](http://arxiv.org/abs/2605.16865v2)_

  - 评测信号：评测不同模型规模下，知识注入后新记忆获取与原有预训练能力保留的权衡表现
  - 失败模式：知识注入后模型发生灾难性遗忘，原有预训练能力大幅下降

- **发现反直觉正累积效应：早期编辑可促进后续编辑成功，证明LN结合岭回归可让参数更新渐近正交、范数有界** ⭐ `ICML 2026`
  _[More Edits, More Stable: Understanding the Lifelong Normalization...](http://arxiv.org/abs/2605.11836v1)_

  - 评测信号：评测长时序顺序编辑下模型的稳定性与编辑性能，验证所提理论正确性与方法的竞争力
  - 失败模式：顺序长期编辑灾难性遗忘、模型性能崩溃


### 🔬 steering（1 篇）

- **将语义等价多模态输入归为知识单元，结合对抗生成与低秩对齐可有效提升多模态知识编辑的泛化鲁棒性** ⭐
  _[Beyond Binary Edits Robust Multimodal Knowledge Editing with Adve...](http://arxiv.org/abs/2605.23780v1)_

  - 评测信号：重点评测所提方法提升多模态知识编辑的鲁棒性，以及跨语义等价多模态变体的泛化能力
  - 失败模式：现有多模态知识编辑无法将编辑传播到语义等价的多模态变体，泛化性不足


### 🔬 在线编辑方法（1 篇）

- **模态解耦可避免视觉主导的更新偏差，正交低秩子空间可缓解长程编辑干扰，单编辑开销恒定。** ⭐ 💻
  _[Modality-Decoupled Online Recursive Editing](http://arxiv.org/abs/2605.20273v1)_

  - 评测信号：在多个多模态大模型骨干与在线编辑基准上，评测了方法的可靠性、通用性、局部性与效率。
  - 失败模式：现有方法应用于多模态在线编辑存在跨模态冲突与长程编辑间干扰


### 🔬 memory-based editor（1 篇）

- **HoReN可在ZsRE上支撑5万次顺序编辑，仍保持整体性能高于0.93，现有方法在1万次编辑前就已性能崩溃退化** ⭐ 💻
  _[HoReN: Normalized Hopfield Retrieval for Large-Scale Sequential M...](http://arxiv.org/abs/2605.08143v2)_

  - 评测信号：在标准、结构化、非结构化三类基准评测编辑性能，重点验证大规模顺序编辑下的性能稳定性
  - 失败模式：顺序编辑累积性能退化，万级编辑前发生性能崩溃，复述输入泛化能力差


### 🔬 meta-learning editor（1 篇）

- **仅用五类基础元任务训练，模型在21个编辑任务上整体性能提升15.8%，可有效泛化到未见编辑任务**
  _[Meta-CoT: Enhancing Granularity and Generalization in Image Editi...](http://arxiv.org/abs/2604.24625v1)_

  - 评测信号：在21个编辑任务上评测性能，验证对未见任务的泛化能力，公开了代码、基准与模型
  - 失败模式：现有CoT图像编辑无法同时兼顾编辑理解粒度与泛化能力


### 🔬 unlearning（1 篇）

- **仅需两步闭式投影且无需训练，耗时仅数秒，在多个生成模型上效果超SOTA，更忠实保留非目标概念** ⭐
  _[Closed-Form Concept Erasure via Double Projections](http://arxiv.org/abs/2604.10032v1)_

  - 评测信号：在多个不同生成模型上评测了概念擦除性能、非目标概念保留效果以及方法运行效率
  - 失败模式：现有概念擦除方法易扭曲无关非目标概念，依赖迭代优化导致运行效率低下


### 🔬 结构隔离编辑（1 篇）

- **基础模型冻结时，该方法单次编辑成功率98%，千次顺序编辑后仍超95%，幻觉降低3-5%，反向迁移得分最优** ⭐
  _[DSCA: Dynamic Subspace Concept Alignment for Lifelong VLM Editing](http://arxiv.org/abs/2604.07965v1)_

  - 评测信号：评测了编辑成功率、知识保留能力、反向迁移性能与幻觉降低幅度，验证了终身编辑下的稳定性
  - 失败模式：顺序编辑中的概念串扰、灾难性遗忘、推理退化与跨模态错位


---
*ArXiv_Daily_Digest 自动生成 | 2026-07-01*