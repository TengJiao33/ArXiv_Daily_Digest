# 📡 llm-truthfulness — 方法版图
> 2026-W19 (05/04-05/10) | 本周 39 篇 | 自动生成

📊 **37** 个方法族 | **0** 篇 high priority | **2** 篇附带代码

---

### 🔬 大模型幻觉检测（3 篇）

- **利用响应与元判断标签的固有逻辑关联，经互学习整合双视角信号后，检测性能优于全部8个对比基线**
  _[Logical Consistency as a Bridge: Improving LLM Hallucination Dete...](http://arxiv.org/abs/2605.03971v1)_

- **基于Koopman算子构造的差分残差得分可实现单样本低开销检测，在三个基准上取得了最先进性能**
  _[Low-Cost Black-Box Detection of LLM Hallucinations via Dynamical ...](http://arxiv.org/abs/2605.05134v1)_

- **注意力发散信号集中在模型中间层，且主要分布在命名实体、数字这类事实性令牌上。**
  _[Detecting Hallucinations in Large Language Models via Internal At...](http://arxiv.org/abs/2605.05025v1)_


### 🔬 流程执行诊断（1 篇）

- **对14个模型测试发现，平均首答准确率从5步流程的61%降至95步流程的20%，失败类型多样**
  _[When LLMs Stop Following Steps: A Diagnostic Study of Procedural ...](http://arxiv.org/abs/2605.00817v1)_


### 🔬 大模型信息检索（1 篇）

- **去噪即最大化上下文窗口内可用证据密度和可验证性，是面向LLM全信息获取流程的核心瓶颈**
  _[LLM-Oriented Information Retrieval: A Denoising-First Perspective](http://arxiv.org/abs/2605.00505v1)_


### 🔬 个性化LLM摘要（1 篇）

- **个性化PLS可提升读者理解程度与感知质量，但会增加强化用户偏见和引入幻觉的风险，存在明确权衡**
  _[ReLay: Personalized LLM-Generated Plain-Language Summaries for Be...](http://arxiv.org/abs/2605.00468v1)_


### 🔬 幻觉在线自校准（1 篇）

- **大视觉语言模型存在生成-判别间隙，模型在判别验证任务上的准确率高于开放式生成任务**
  _[Online Self-Calibration Against Hallucination in Vision-Language ...](http://arxiv.org/abs/2605.00323v1)_


### 🔬 大模型幻觉评测（1 篇）

- **HalluScore与人类判断相关系数0.41，NLI验证AUROC达0.88，ADR降本2倍仅降0.1%AUROC**
  _[HalluScan: A Systematic Benchmark for Detecting and Mitigating Ha...](http://arxiv.org/abs/2605.02443v1)_


### 🔬 多跳事实纠错（1 篇）

- **基于分解注入范式的CECoR，多跳事实纠错性能优于两类对比基线，同时具备良好的泛化性与抗噪性**
  _[Compositional Multi-hop Factual Error Correction via Decompositio...](http://arxiv.org/abs/2605.02277v1)_


### 🔬 事实编辑评测（1 篇）

- **在硬隐式自由分层中，五个LLM编辑系统ERA得分0.148-0.705，最强模型仍漏约30%所需级联更新**
  _[EditPropBench: Measuring Factual Edit Propagation in Scientific M...](http://arxiv.org/abs/2605.02083v1)_


### 🔬 AI合规缺口（1 篇）

- **默认框架下六个前沿模型流程合规率均为0%，仅靠文本无法检测该缺口，移除委托工具后合规率升至75%**
  _[The Compliance Gap: Why AI Systems Promise to Follow Process Inst...](http://arxiv.org/abs/2605.01771v1)_


### 🔬 幻觉缓解（1 篇）

- **LIME不修改模型参数无需额外训练，可提升模态贡献，得到更局部语义对齐的相关性模式**
  _[Mitigating Multimodal LLMs Hallucinations via Relevance Propagati...](http://arxiv.org/abs/2605.01766v1)_


### 🔬 视觉语言推理（1 篇）

- **MIRL在六个推理基准取得70.22%平均准确率，仅用10次预采样选前6就超过16次完整轨迹采样性能，少25%完整轨迹**
  _[MIRL: Mutual Information-Guided Reinforcement Learning for Vision...](http://arxiv.org/abs/2605.01520v1)_


### 🔬 表格推理RAG（1 篇）

- **FT-RAG较最优基线，表级命中率提23.5%，单元级提59.2%，精确值准确率召回提升62.2%**
  _[FT-RAG: A Fine-grained Retrieval-Augmented Generation Framework f...](http://arxiv.org/abs/2605.01495v1)_


### 🔬 大模型幻觉治理（1 篇）

- **当前大模型事实性提升均来自扩展知识边界，而非提升对自身知识边界的感知，消除幻觉与保留效用存在固有权衡。**
  _[Hallucinations Undermine Trust; Metacognition is a Way Forward](http://arxiv.org/abs/2605.01428v1)_


### 🔬 大模型记忆检索（1 篇）

- **结合选择性存储、溯源富表示、查询自适应检索的MemORAI，在两个基准实现任务SOTA性能**
  _[MemORAI: Memory Organization and Retrieval via Adaptive Graph Int...](http://arxiv.org/abs/2605.01386v1)_


### 🔬 多视图媒体画像（1 篇）

- **所提方法在ACL-2020数据集上取得当前最优结果，在新建MBFC-2025数据集上建立了强性能基准**
  _[A Multi-View Media Profiling Suite: Resources, Evaluation, and An...](http://arxiv.org/abs/2605.01336v1)_


### 🔬 大模型幻觉抑制（1 篇）

- **自适应遗忘可降低81%的包幻觉率，分布变化仅集中在包相关生成，基本不影响通用编码性能**
  _[LLM Ghostbusters: Surgical Hallucination Suppression via Adaptive...](http://arxiv.org/abs/2605.01047v1)_


### 🔬 司法模型风险评估（1 篇）

- **多款当代大语言模型频繁存在显著风险，尤其在先例检索任务中表现差，无法捕捉关键法律信息** 💻
  _[TriBench-Ko: Evaluating LLM Risks in Judicial Workflows](http://arxiv.org/abs/2605.03792v1)_


### 🔬 事件因果识别（1 篇）

- **整合概念路径度量、句法度量、因果模式过滤的结构检索，可有效缓解因果幻觉，提升事件因果识别准确率** 💻
  _[SERE: Structural Example Retrieval for Enhancing LLMs in Event Ca...](http://arxiv.org/abs/2605.03701v1)_


### 🔬 医疗幻觉检测（1 篇）

- **微调Qwen3-14B检测模型E4F1达0.831，E3+E4F1达0.823，相对基模提升50.0%**
  _[CuraView: A Multi-Agent Framework for Medical Hallucination Detec...](http://arxiv.org/abs/2605.03476v1)_


### 🔬 可回答性探测（1 篇）

- **数学提示下检测ROC-AUC达0.78-0.84，信号源于早层逐渐衰减，事实提示无可靠信号**
  _[Geometric Deviation as an Unsupervised Pre-Generation Reliability...](http://arxiv.org/abs/2605.03196v1)_


### 🔬 推理模型评估（1 篇）

- **相比非推理模型，推理模型准确率仅高2-11%，仍有26-42%的错误预设未被挑战，且易受预设表述强度影响**
  _[Evaluating Reasoning Models for Queries with Presuppositions](http://arxiv.org/abs/2605.03050v1)_


### 🔬 关系幻觉分析（1 篇）

- **即使是轻度的旋转与噪声扰动，也会显著降低多模型多数据集上的关系推理性能，现有方法仅能部分改善**
  _[When Relations Break: Analyzing Relation Hallucination in Vision-...](http://arxiv.org/abs/2605.05045v1)_


### 🔬 直接偏好优化（1 篇）

- **基于令牌级认知不确定性调整不同令牌的学习压力，可缓解自指偏差，有效提升多模态大模型对齐性能**
  _[Uncertainty-Aware Exploratory Direct Preference Optimization for ...](http://arxiv.org/abs/2605.04874v1)_


### 🔬 因果推理基准（1 篇）

- **结合显式因果符号结构引导的方法在NoisyCausal上显著优于基线，无需任务微调即可泛化到Cladder**
  _[NoisyCausal: A Benchmark for Evaluating Causal Reasoning Under St...](http://arxiv.org/abs/2605.04313v1)_


### 🔬 医学幻觉检测（1 篇）

- **EtHER在词级编造基准上超出现有最优检测器15%以上，且跨结构相似性下性能保持稳定**
  _[MedFabric and EtHER: A Data-Centric Framework for Word-Level Fabr...](http://arxiv.org/abs/2605.04180v1)_


### 🔬 大模型幻觉研究（1 篇）

- **Grok的HI为0.67、Copilot为0.70，Gemini为0.53、ChatGPT为0.57，大模型幻觉还与任务类型、提示条件相关**
  _[Not All That Is Fluent Is Factual: Investigating Hallucinations o...](http://arxiv.org/abs/2605.04171v1)_


### 🔬 大模型激活引导（1 篇）

- **热门激活引导方法不契合提示引导机制，提示引导仅对部分token强干预，对其余token几乎无影响**
  _[Steer Like the LLM: Activation Steering that Mimics Prompting](http://arxiv.org/abs/2605.03907)_


### 🔬 来源归因评估（1 篇）

- **前沿模型链接有效性超94%、相关性超80%，事实准确率仅39-77%，检索量增加事实准确率平均降约42%**
  _[Cited but Not Verified: Parsing and Evaluating Source Attribution...](http://arxiv.org/abs/2605.06635v1)_


### 🔬 大模型评估（1 篇）

- **在多个评估任务、不同大模型上，DAPRO满足预算约束，覆盖率更接近标称水平，方差低于静态基线**
  _[How Many Iterations to Jailbreak? Dynamic Budget Allocation for M...](http://arxiv.org/abs/2605.06605v1)_


### 🔬 临床报告自动生成（1 篇）

- **两种方法存在临床可靠性与语言质量的清晰权衡，模板法多维度得分更高，GPT-4输出更简洁，对比无统计显著性。**
  _[Automated Clinical Report Generation for Remote Cognitive Remedia...](http://arxiv.org/abs/2605.06594v1)_


### 🔬 高效不确定性估计（1 篇）

- **大语言模型仅需部分生成就能实现效果良好的不确定性估计，纯输入元估计器在多场景也有竞争力。**
  _[Towards Generation-Efficient Uncertainty Estimation in Large Lang...](http://arxiv.org/abs/2605.06053v1)_


### 🔬 大模型事实纠错（1 篇）

- **纠正抑制率为19%-90%，八个模型中四个超80%，模型内部知晓错误，仅在响应选择阶段不纠错**
  _[Knowing but Not Correcting: Routine Task Requests Suppress Factua...](http://arxiv.org/abs/2605.05957v1)_


### 🔬 幻觉检测校正（1 篇）

- **PCNET幻觉检测AUROC最高达99%，PC-LDCD将正确内容破坏率降至53.7%，保留率达79.3%**
  _[Hallucination as an Anomaly: Dynamic Intervention via Probabilist...](http://arxiv.org/abs/2605.05953v1)_


### 🔬 不确定性量化（1 篇）

- **仅占目标黑盒大语言模型大小1%的轻量代理模型，就可以实现可靠的黑盒LLM不确定性量化**
  _[Estimating the Black-box LLM Uncertainty with Distribution-Aligne...](http://arxiv.org/abs/2605.05777v1)_


### 🔬 多模态RAG去偏（1 篇）

- **重污染由双重注意力崩溃驱动，一是视觉注意力受抑制引发视觉盲，二是优先边界token的结构位置偏差**
  _[The Cost of Context: Mitigating Textual Bias in Multimodal Retrie...](http://arxiv.org/abs/2605.05594v1)_


### 🔬 结构化合同提取（1 篇）

- **Olava Extract宏F1为0.812、微F1为0.842，推理成本较前沿模型降低78%-97%，性能最优幻觉更少**
  _[A Few Good Clauses: Comparing LLMs vs Domain-Trained Small Langua...](http://arxiv.org/abs/2605.05532v1)_


### 🔬 对象幻觉缓解（1 篇）

- **观察到大视觉语言模型回答描述查询比非描述查询对视觉信息注意力显著更强，该方法平均降低6.03%对象幻觉**
  _[CAST: Mitigating Object Hallucination in Large Vision-Language Mo...](http://arxiv.org/abs/2605.04641)_


---
*ArXiv_Daily_Digest 自动生成 | 2026-07-01*