# 📡 llm-truthfulness — 方法版图
> 2026-W21 (05/18-05/24) | 本周 25 篇 | 自动生成

📊 **24** 个方法族 | **0** 篇 high priority | **1** 篇附带代码

---

### 🔬 大模型幻觉检测（2 篇）

- **7款不同规模模型的AUC仅跨度2.3个百分点，同家族3B LLaMA检测效果优于8B LLaMA**
  _[Hallucination Detection via Activations of Open-Weight Proxy Anal...](http://arxiv.org/abs/2605.07209)_

- **六个常用幻觉检测基准中四个将真值答案嵌入输入提示，控制缺陷后仅SAPLMA和DRIFT性能稳定优于随机猜测**
  _[PARALLAX: Separating Genuine Hallucination Detection from Benchma...](http://arxiv.org/abs/2605.17028v1)_


### 🔬 思维链忠实性（1 篇）

- **平均仅61.9%的步骤中隐式答案承诺与显式轨迹对齐，58.0%错配为答案确定后的虚构延续。**
  _[When Reasoning Traces Become Performative: Step-Level Evidence th...](http://arxiv.org/abs/2605.11746)_


### 🔬 机械可解释性（1 篇）

- **同规模下分组查询注意力的电路比标准多头更集中稳定；Qwen2.5事实回忆电路过临界规模后坍缩为单瓶颈**
  _[Architecture, Not Scale: Circuit Localization in Large Language M...](http://arxiv.org/abs/2605.08853)_


### 🔬 知识时间漂移（1 篇）

- **时间漂移编码方向在残差流中正交于正确性与不确定性，线性探针检测AUROC达0.83--0.95，基线接近随机**
  _[The Geometry of Forgetting: Temporal Knowledge Drift as an Indepe...](http://arxiv.org/abs/2605.09195)_


### 🔬 幻觉回路分析（1 篇）

- **抑制幻觉通路成分最多可减少76%物体幻觉且精度损失极小，该回路选择性转移至关系而非属性幻觉**
  _[Dual-Pathway Circuits of Object Hallucination in Vision-Language ...](http://arxiv.org/abs/2605.13156)_


### 🔬 大模型解码优化（1 篇）

- **APCD通过熵判定预测不确定性决定分支时机，随预测分布散度增大动态衰减路径间影响，兼顾准确率与效率** 💻
  _[APCD: Adaptive Path-Contrastive Decoding for Reliable Large Langu...](http://arxiv.org/abs/2605.09492)_


### 🔬 大模型劝说机制（1 篇）

- **少量中间层注意力头决定模型输出，劝说通过重定向路由使输出顶点跳转到目标，移除特征可阻断劝说**
  _[How LLMs Are Persuaded: A Few Attention Heads, Rerouted](http://arxiv.org/abs/2605.09314)_


### 🔬 事实回忆缩放规律（1 篇）

- **事实回忆质量符合模型参数量和训练主题频率对数线性组合的sigmoid曲线，两变量可解释60%-94%性能方差。**
  _[Predictable Confabulations: Factual Recall by LLMs Scales with Mo...](http://arxiv.org/abs/2605.18732v1)_


### 🔬 跨层幻觉校正（1 篇）

- **在15个模型、3个事实基准中所有评测单元均获提升，平均MC1升12.26点、MC2升8.65点，无衰退**
  _[TRACE: Trajectory Correction from Cross-layer Evidence for Halluc...](http://arxiv.org/abs/2605.18163v1)_


### 🔬 联邦自蒸馏（1 篇）

- **发现无约束自蒸馏存在重写悖论，会增加幻觉与冗余，双分支选择性聚合可得到全局对齐的忠实模型**
  _[FedSDR: Federated Self-Distillation with Rectification](http://arxiv.org/abs/2605.18028v1)_


### 🔬 RAG预测预取（1 篇）

- **所提方法最高降低43.5%端到端延迟，提升62.4%首token时间，答案质量与同步RAG基线相当**
  _[Predictive Prefetching for Retrieval-Augmented Generation](http://arxiv.org/abs/2605.17989v1)_


### 🔬 临床文本评估（1 篇）

- **分块改写可大幅缓解合成笔记的细粒度细节丢失，但不完全上下文会降低事实精确度，合成笔记可增强罕见ICD编码训练**
  _[Systematic Evaluation of the Quality of Synthetic Clinical Notes ...](http://arxiv.org/abs/2605.17775v1)_


### 🔬 生成式AI评估（1 篇）

- **QQJ相比传统自动指标和无约束LLM评估器，与人类判断对齐性更强，重复评估更稳定，故障识别能力更优**
  _[QQJ: Quantifying Qualitative Judgment for Scalable and Human-Alig...](http://arxiv.org/abs/2605.17382v1)_


### 🔬 知识密集型问答（1 篇）

- **AMATA在五个知识密集型QA基准上持续优于各类对比方法，同时能够有效减少模型的token消耗**
  _[AMATA: Adaptive Multi-Agent Trajectory Alignment for Knowledge-In...](http://arxiv.org/abs/2605.17352v1)_


### 🔬 RAG知识冲突处理（1 篇）

- **该框架冲突检测F1达88.7%，相对最强基线正确性提升5.3-6.1%，降62%API成本仍保90.8%准确率**
  _[ConflictRAG: Detecting and Resolving Knowledge Conflicts in Retri...](http://arxiv.org/abs/2605.17301v1)_


### 🔬 大模型包幻觉（1 篇）

- **五款前沿模型包幻觉率在4.62%~6.10%，存在127个共有的幻觉包名，Python幻觉率高于JavaScript**
  _[The Range Shrinks, the Threat Remains: Re-evaluating LLM Package ...](http://arxiv.org/abs/2605.17062v1)_


### 🔬 幻觉评测基准（1 篇）

- **阿拉伯语大语言模型的幻觉不止事实不准确，还存在文化理解、语言推理、逻辑一致性挑战**
  _[HalluScore: Large Language Model Hallucination Question Answering...](http://arxiv.org/abs/2605.17007v1)_


### 🔬 AI幻觉神经机制（1 篇）

- **误判的AI生成幻觉无法触发标准的神经认知事实验证通路，误判与正确判断的幻觉神经响应存在显著差异**
  _[How do Humans Process AI-generated Hallucination Contents: a Neur...](http://arxiv.org/abs/2605.16953v1)_


### 🔬 预训练数据时序性（1 篇）

- **时序排序预训练模型通用能力与打乱基线相当，知识更新更精确，打乱预训练在旧数据上表现更好**
  _[Understanding Data Temporality Impact on Large Language Models Pr...](http://arxiv.org/abs/2605.22769v1)_


### 🔬 辅助对抗话语生成（1 篇）

- **大语言模型生成的对抗话语仅40%合格，结合多源知识的混合策略效果最优，专家编辑可大幅提升生成质量**
  _[Assisted Counterspeech Writing at the Crossroads of Hate Speech a...](http://arxiv.org/abs/2605.22435v1)_


### 🔬 事实回忆迁移（1 篇）

- **基于集成离散语音标记的SpiritLM发现，文到文与语音到文本结果存在差异，事实回忆机制仅部分从文本迁移到语音**
  _[Do Factual Recall Mechanisms Carry over from Text to Speech in Mu...](http://arxiv.org/abs/2605.22170v1)_


### 🔬 检索增强问答（1 篇）

- **BGE-M3嵌入模型Hit Rate@3达0.285，性能最优，检索器选择是高棉语RAG主要瓶颈，不同生成模型各有所长。**
  _[A Comparative Study of Language Models for Khmer Retrieval-Augmen...](http://arxiv.org/abs/2605.22099v1)_


### 🔬 无幻觉研究问答（1 篇）

- **150M参数的ModernBERT token分类器词级F1达53.6，优于最强对比LLM抽取器的48.7**
  _[ACL-Verbatim: hallucination-free question answering for research](http://arxiv.org/abs/2605.21102v1)_


### 🔬 法律RAG基准（1 篇）

- **当前最优的法律RAG系统，在检索、生成和主张级分析三个方面均存在明显局限性**
  _[Fine-grained Claim-level RAG Benchmark for Law](http://arxiv.org/abs/2605.21071v2)_


---
*ArXiv_Daily_Digest 自动生成 | 2026-07-01*