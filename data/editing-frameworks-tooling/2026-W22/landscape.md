# 📡 editing-frameworks-tooling — 方法版图
> 2026-W22 (05/25-05/31) | 本周 20 篇 | 自动生成

📊 **5** 个方法族 | **8** 篇 high priority | **2** 篇附带代码

---

### 🔬 steering（12 篇）

- **在FLUX.1 Dev与Stable Diffusion 3.5 Large上，SafeDIG可稳定降低目标域不安全生成率，同时保留原安全性与生成质量** ⭐
  _[Robust and Generalizable Safety Steering for Text-to-Image Diffus...](http://arxiv.org/abs/2605.30049v1)_

  - 评测信号：评测目标域与整体不安全生成率，同时验证源域安全保留效果与生成图像质量，检验方法鲁棒泛化性
  - 失败模式：固定层安全引导不稳定，已知风险学习的引导机制无法可靠迁移到新风险域

- **BRACS可降低CHAIR$_s$ 9.4个点、提升POPE F1 2.7个点，平均推理速度比基线高1.3倍。** ⭐
  _[Mitigating Hallucination in Vision-Language Models through Barrie...](http://arxiv.org/abs/2605.29881v1)_

  - 评测信号：在LLaVA-1.5-7B和Qwen-VL-Chat两个模型上测试，幻觉基准性能更优，不损失通用任务性能。
  - 失败模式：解码过程中视觉grounding退化，模型生成不存在物体的幻觉，现有方法干预不合理。

- **对Qwen-2.5模型族分析发现，性能更优的数学推理具备更少步骤、单步信息密度更高的特性**
  _[DenseSteer: Steering Small Language Models towards Dense Math Rea...](http://arxiv.org/abs/2605.29247v1)_

  - 评测信号：在数学推理基准上验证，该方法可在不增加token级负对数似然的前提下稳定提升推理准确率

- **仅更新模型0.11%的总参数，在少样本与领域偏移设置下性能始终优于现有最优方法。** ⭐ 💻
  _[Evi-Steer: Learning to Steer Biomedical Vision-Language Models th...](http://arxiv.org/abs/2605.26292v1)_

  - 评测信号：在15个覆盖8器官8模态的生物医学数据集的少样本、域泛化设置下评测，性能优于SOTA，已公开代码。
  - 失败模式：现有确定性参数适配方法在领域偏移、图文对齐模糊场景下性能不佳

- **结合结果正确性与对数几率引导校准教师对数，可稳定自蒸馏，性能优于标准同策略自蒸馏**
  _[OGLS-SD: On-Policy Self-Distillation with Outcome-Guided Logit St...](http://arxiv.org/abs/2605.12400v1)_

  - 评测信号：在多个不同推理基准上开展实验，验证所提方法相比现有同策略自蒸馏的推理性能提升
  - 失败模式：同策略自蒸馏中教师响应偏移导致师生不匹配、令牌级监督校准错误

- **分阶段的条件引导与混合专家合成设计，让FineSteer在极小效用损失下获得优于SOTA的引导效果** ⭐
  _[FineSteer: A Unified Framework for Fine-Grained Inference-Time St...](http://arxiv.org/abs/2604.15488v1)_

  - 评测信号：在安全和真实性两类基准上开展实验，对比现有最优方法，验证引导效果与效用保留能力
  - 失败模式：现有推理引导一刀切刚性设计，适应性不足，无法兼顾效果、效用与训练效率

- **均值差注入在14个LLM中11个优于基线，增益3.6%-16.4%，混合方法在13个模型上性能更优**
  _[Psychological Steering of Large Language Models](http://arxiv.org/abs/2604.14463v1)_

  - 评测信号：基于IPIP-NEO-120数据集，在14个大语言模型的开放式生成任务中评测心理引导方法的效果
  - 失败模式：现有心理干预方法搜索空间受限，扫描单位未校准，易错过最优干预条件

- **通过多视角分析证实，大语言模型人格存在情境依赖性，且具有稳定一致的情境-行为关联模式**
  _[Beyond Static Personas: Situational Personality Steering for Larg...](http://arxiv.org/abs/2604.13846v3)_

  - 评测信号：在公开基准PersonalityBench和自建SPBench上评测，验证方法对未知情境、不同模型架构的泛化性与鲁棒性
  - 失败模式：现有个性化方法可控性差、资源需求高，静态人格建模缺乏跨情境适应性

- **稀疏解耦表征的相位引导效果优于稠密或纠缠表征，静态干预无法适应该动态场景**
  _[Sparse Autoencoders as a Steering Basis for Phase Synchronization...](http://arxiv.org/abs/2604.04946v1)_

  - 评测信号：在统一干预流程下对比不同表征空间的相位校正效果，验证稀疏解耦表征的性能优势
  - 失败模式：基于图的CFD代理振荡流预测的相位漂移

- **在去噪早期修正计数偏差可避免结构错误固化，动态调整比静态引导以少量计算换得更高计数准确率，高目标计数提升显著。**
  _[ATHENA: Adaptive Test-Time Steering for Improving Count Fidelity ...](http://arxiv.org/abs/2603.19676v1)_

  - 评测信号：在多个标准基准与新增复杂数据集、多个扩散骨干上验证，证明方法可提升计数保真度且保持良好精度耗时权衡。
  - 失败模式：文生图扩散模型物体计数控制系统性失效

- **VLM的安全决策高度依赖语义线索，依赖习得图文关联而非接地视觉理解，易被自动引导流程利用** ⭐
  _[SAVeS: Steering Safety Judgments in Vision-Language Models via Se...](http://arxiv.org/abs/2603.19092v1)_

  - 评测信号：提出SAVeS基准与评测协议，可区分行为拒绝、接地安全推理和错误拒绝三类情形
  - 失败模式：多模态安全决策依赖浅层图文关联而非接地视觉理解，存在被诱导利用的漏洞

- **基于多特质子空间引导生成的黑暗模型，在单轮和多轮评估中均能稳定产生有害交互与有害结果**
  _[Multi-Trait Subspace Steering to Reveal the Dark Side of Human-AI...](http://arxiv.org/abs/2603.18085v1)_

  - 评测信号：通过单轮与多轮对话评估，验证所生成黑暗模型能够稳定产生有害交互与对应结果
  - 失败模式：现有方法难以在可控环境中模拟持续发展的自然有害人机交互


### 🔬 framework/tooling（5 篇）

- **为编辑区域分配更高噪声、未编辑区域分配更低噪声，可同时提升编辑效果与内容一致性**
  _[Tuning-free Instruction-based Video Editing Via Structural Noise ...](http://arxiv.org/abs/2605.15533v1)_

  - 评测信号：仅提及方法取得更好视觉质量与当前最优性能，未给出具体评测指标与数值细节
  - 失败模式：现有免微调视频编辑未充分利用噪声隐空间信息，编辑效果差、内容一致性不足

- **仅960M参数的EditMGT在多个基准取得最优图像相似性，编辑速度比扩散方法快6倍**
  _[Masked Generative Transformer Is What You Need for Image Editing](http://arxiv.org/abs/2605.10859v1)_

  - 评测信号：在多个图像编辑基准上取得最优图像相似性，相比扩散方法编辑速度提升6倍，模型仅960M参数
  - 失败模式：编辑串扰，修改会蔓延至不应改变的非目标区域

- **设计合理的编辑范式下，顺序分解随任务复杂度提升仍能带来鲁棒性能提升，合成学到的分解能力可迁移到真实图像**
  _[Towards Robust Sequential Decomposition for Complex Image Editing](http://arxiv.org/abs/2605.09233v1)_

  - 评测信号：重点评测复杂指令编辑的鲁棒性，以及合成数据学习得到的分解能力在真实场景的泛化迁移能力
  - 失败模式：单轮编辑错误解析指令导致错误编辑、顺序编辑误差累积降低结果保真度

- **相比先前时间一致性最优基线，词错率降低近70%，在基础TTS上WDTW降低27%，取得SOTA性能。**
  _[AST: Adaptive, Seamless, and Training-Free Precise Speech Editing](http://arxiv.org/abs/2604.16056v1)_

  - 评测信号：提出WDTW指标评估未编辑区域时间一致性，构建公开基准数据集LibriSpeech-Edit，验证模型性能提升。
  - 失败模式：编辑后未编辑区域时间保真度低，编辑边界存在伪影，编辑质量与一致性难以兼顾

- **采用三层分工的分层多智能体框架，在视频混剪的客观指标和人工评估中均显著优于现有最优方法** 💻
  _[DIRECT: Video Mashup Creation via Hierarchical Multi-Agent Planni...](http://arxiv.org/abs/2604.04875v1)_

  - 评测信号：构建了带视觉连续性、听觉对齐定制指标的Mashup-Bench基准，通过客观指标和人工主观评测验证效果
  - 失败模式：现有自动视频混剪缺乏跨层级多模态协调，导致片段脱节、转场突兀、音画错位


### 🔬 meta-learning editor（1 篇）

- **AEvo相对最强基线取得26%的相对提升，相同迭代预算下开放优化任务达到当前最优性能** ⭐
  _[Harnessing Agentic Evolution](http://arxiv.org/abs/2605.13821v1)_

  - 评测信号：在智能体推理基准与三个开放端优化任务上，对比多个基线评测长周期进化搜索的性能
  - 失败模式：长周期进化易漂移，无法有效利用积累的进化证据


### 🔬 evaluation/benchmark（1 篇）

- **恶意知识编辑可稳定诱导错误不安全推理，同时基本保留模型通用能力，这类风险难以检测，受三类关键因素影响** ⭐
  _[Benchmarking Safety Risks of Knowledge-Intensive Reasoning under ...](http://arxiv.org/abs/2605.10146v1)_

  - 评测信号：从攻击有效性、推理正确性、副作用三个维度，评估注入恶意知识对下游推理行为和可靠性的影响
  - 失败模式：现有基准缺失相关评估，恶意知识编辑的安全风险隐蔽难以检测


### 🔬 locate-then-edit（1 篇）

- **经3000次顺序编辑后，SCAN仍可在MMLU、GSM8K保持模型完整性，现有方法会逐渐恶化最终发生模型崩溃** ⭐
  _[SCAN: Sparse Circuit Anchor Interpretable Neuron for Lifelong Kno...](http://arxiv.org/abs/2603.15226v1)_

  - 评测信号：评测多类大语言模型多次顺序编辑后的通用能力保留效果，验证编辑后模型的完整性
  - 失败模式：顺序知识编辑累积后引发模型崩溃与灾难性遗忘


---
*ArXiv_Daily_Digest 自动生成 | 2026-07-01*