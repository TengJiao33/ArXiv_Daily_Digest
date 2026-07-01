# 📡 representation-engineering — 方法版图
> 2026-W17 (04/20-04/26) | 本周 62 篇 | 自动生成

📊 **37** 个方法族 | **0** 篇 high priority | **4** 篇附带代码

---

### 🔬 大模型幻觉缓解（3 篇）

- **MPD可降低大视觉语言模型幻觉23.4%，同时保留原有模型97.4%的通用生成能力，无额外计算成本**
  _[Mitigating Hallucinations in Large Vision-Language Models without...](http://arxiv.org/abs/2604.20366)_

- **该方法生成的建议81%优于人工构建真值，几乎消除了关键召回失败，效果显著优于标准通用自一致性。**
  _[Reducing Hallucination in Enterprise AI Workflows via Hybrid Util...](http://arxiv.org/abs/2604.11141)_

- **SinkTrack在SQuAD2.0提升21.6%，在M3CoT提升22.8%，训练免费且推理开销可忽略** 💻
  _[SinkTrack: Attention Sink based Context Anchoring for Large Langu...](http://arxiv.org/abs/2604.10027)_


### 🔬 大模型幻觉检测（3 篇）

- **大语言模型层间内部表示的离散程度可反映不确定性，SIVR性能稳定优于现有多个强基线方法** 💻
  _[Learning Uncertainty from Sequential Internal Dispersion in Large...](http://arxiv.org/abs/2604.15741)_

- **M3在单折验证和留出测试集表现最佳，探针延迟仅0.15-6.66ms，实际检测开销可忽略**
  _[Weakly Supervised Distillation of Hallucination Signals into Tran...](http://arxiv.org/abs/2604.06277)_

- **将生成过程建模为势能面轨迹，可将幻觉归因于特定高能稀疏特征，在Gemma-2-9B上实现最优性能**
  _[HalluSAE: Detecting Hallucinations in Large Language Models via S...](http://arxiv.org/abs/2604.16430)_


### 🔬 大模型可解释性（2 篇）

- **不确定性与正确性分属三类特征，抑制混杂特征提准1.1%降熵75%，3个特征预测正确性AUROC约0.79**
  _[Are LLM Uncertainty and Correctness Encoded by the Same Features?...](http://arxiv.org/abs/2604.19974)_

- **人类在该任务上可达100%准确率，模型虽编码了视角信息，却无法绑定视角与对应观测，最终层产生幻觉**
  _[How Do LLMs and VLMs Understand Viewpoint Rotation Without Vision...](http://arxiv.org/abs/2604.15294)_


### 🔬 大模型安全对齐（2 篇）

- **大语言模型中存在引发有害行为的"不安全票"，剪枝后可得到维持性能且输出对齐的"安全票"**
  _[Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer ...](http://arxiv.org/abs/2604.15780)_

- **理论证明单独约束权重或激活不足以保障安全，CWAC可实现低有害响应同时几乎不损失微调精度。**
  _[Preventing Safety Drift in Large Language Models via Coupled Weig...](http://arxiv.org/abs/2604.12384)_


### 🔬 隐私保护个性化（1 篇）

- **删除用户代理后模型KL散度约0.21nats，验证通过率82-89%，跨用户污染接近零。**
  _[Separable Expert Architecture: Toward Privacy-Preserving LLM Pers...](http://arxiv.org/abs/2604.21571)_


### 🔬 大模型谄媚机制（1 篇）

- **同一小簇注意力头携带错误信号，静默后大幅翻转谄媚行为不影响准确性，RLHF降谄媚十倍仍保留该回路**
  _[LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-L...](http://arxiv.org/abs/2604.19117)_


### 🔬 接地推理（1 篇）

- **GRIL最高提升前提检测达45%，任务成功率提升30%，同时将平均响应长度缩短超20%**
  _[Pause or Fabricate? Training Language Models for Grounded Reasoni...](http://arxiv.org/abs/2604.19656)_


### 🔬 可控性漂移检测（1 篇）

- **监督对齐几何稳定性预测可引导性ρ达0.89-0.97，无监督漂移检测假警率较Procrustes低6倍**
  _[The Geometric Canary: Predicting Steerability and Detecting Drift...](http://arxiv.org/abs/2604.17698)_


### 🔬 引用幻觉定位（1 篇）

- **跨所有模型与设置，作者名引用幻觉率远高于其他字段，幻觉信号不跨领域泛化，存在稀疏领域特异性幻觉神经元**
  _[Where Fake Citations Are Made: Tracing Field-Level Hallucination ...](http://arxiv.org/abs/2604.18880)_


### 🔬 有害意图检测（1 篇）

- **最优检测平均AUROC达0.98，跨数据集迁移最差AUROC0.96，有害意图与拒绝行为功能分离**
  _[Harmful Intent as a Geometrically Recoverable Feature of LLM Resi...](http://arxiv.org/abs/2604.18901)_


### 🔬 隐几何探测（1 篇）

- **宪法诱导隐几何可跨模型与基质复现，未适配Phi模型AUC达0.984，ALM8数据平均AUC为0.72**
  _[ATLAS: Constitution-Conditioned Latent Geometry and Redistributio...](http://arxiv.org/abs/2604.17663)_


### 🔬 幻觉生成机制（1 篇）

- **发现第20层注入幻觉激活87.5%概率破坏正确轨迹，反向仅第24层33.3%概率恢复，步0残差预测幻觉率r=0.776**
  _[Hallucination as Trajectory Commitment: Causal Evidence for Asymm...](http://arxiv.org/abs/2604.15400)_


### 🔬 语言模型适配（1 篇）

- **引导是基于激活空间靶向干预的独特适配范式，无需参数更新即可实现局部可逆的模型行为改变**
  _[From Weights to Activations: Is Steering the Next Frontier of Ada...](http://arxiv.org/abs/2604.14090)_


### 🔬 推理退化监控（1 篇）

- **基于探针的Companion零推理开销，平均效应量+0.471，最佳交叉验证AUROC达0.840，效果依任务和模型规模变化**
  _[The cognitive companion: a lightweight parallel monitoring archit...](http://arxiv.org/abs/2604.13759)_


### 🔬 MoE幻觉缓解（1 篇）

- **静态Top-k路由偏好高频模式使长尾知识专家休眠，CoR不增推理预算平均提升事实准确率3.1%。**
  _[Awakening Dormant Experts:Counterfactual Routing to Mitigate MoE ...](http://arxiv.org/abs/2604.14246)_


### 🔬 混合专家可解释性（1 篇）

- **转向时间专家质心使时间类概率提升321%（44提示中位数），抑制地理专家使地理类概率下降23%**
  _[Geometric Routing Enables Causal Expert Control in Mixture of Exp...](http://arxiv.org/abs/2604.14434)_


### 🔬 抑制模型谄媚（1 篇）

- **在人类对话语境中通常寻求认可的查询上，用户期望大语言模型提供客观信息，模型却默认用户寻求认可，由此引发谄媚**
  _[Verbalizing LLMs' Assumptions About the User to Calibrate Expecta...](https://www.semanticscholar.org/paper/71215b1da630dc25040fb0e73ebde99e13da321e)_


### 🔬 多模态幻觉校正（1 篇）

- **发现多模态推理幻觉与高熵状态的认知分叉点强相关，根源是中间层视觉锚定失效，模型转而依赖语言先验**
  _[Cognitive Pivot Points and Visual Anchoring: Unveiling and Rectif...](http://arxiv.org/abs/2604.10219)_


### 🔬 VLM可解释性（1 篇）

- **对错样本编码视觉证据强度相近，最终层logit间隙预测接地结果相关系数ρ=0.847，图像token承担几乎全部因果影响**
  _[Arbitration Failure, Not Perceptual Blindness: How Vision-Languag...](http://arxiv.org/abs/2604.09364)_


### 🔬 扩散生成控制（1 篇）

- **对DiT的选定层和时间步动态应用转向向量，无需重训练即可灵活调控生成内容与风格**
  _[SHIFT: Steering Hidden Intermediates in Flow Transformers](http://arxiv.org/abs/2604.09213)_


### 🔬 激活引导对齐（1 篇）

- **三种激活引导方法均可恢复目标性状保留连贯性，StTP和StMP更能保持通用能力、减少多轮重复**
  _[Activation Steering for Aligned Open-ended Generation without Sac...](http://arxiv.org/abs/2604.08169)_


### 🔬 探针泛化分析（1 篇）

- **分布内探测QWK约0.7，中间层预测效果最佳，跨语料评估时所有探针性能均崩溃**
  _[Multilingual Embedding Probes Fail to Generalize Across Learner C...](http://arxiv.org/abs/2604.07095)_


### 🔬 幻觉缓解（1 篇）

- **发现大语言模型的浅层主要依赖均匀注意力模式，该模式会因无法聚焦相关信息引发幻觉**
  _[ART: Attention Replacement Technique to Improve Factuality in LLM...](http://arxiv.org/abs/2604.06393)_


### 🔬 多轮置信校准（1 篇）

- **用户反馈（例如说服）会劣化大语言模型多轮对话的置信校准效果，所提方法可有效改善该问题。**
  _[Confidence Should Be Calibrated More Than One Turn Deep](http://arxiv.org/abs/2604.05397)_


### 🔬 RAG保真度监控（1 篇）

- **在PubMedQA搭配Llama-3-8B达到0.942 AUROC，仅0.77ms开销，16位定点保留99.8%FP16的AUROC。**
  _[LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retr...](http://arxiv.org/abs/2604.05358)_


### 🔬 指令遵循机制（1 篇）

- **不存在指令遵循的通用机制，它是多样语言能力的技能化协调，约束满足是生成中的动态监测而非预生成规划**
  _[How LLMs Follow Instructions: Skillful Coordination, Not a Univer...](http://arxiv.org/abs/2604.06015)_


### 🔬 语言模型记忆控制（1 篇）

- **参数α可可靠控制记忆压力，见过样本准确率单调上升，未见样本准确率稳定，更大模型响应性更强。**
  _[Memory Dial: A Training Framework for Controllable Memorization i...](http://arxiv.org/abs/2604.05074)_


### 🔬 情绪表征提取（1 篇）

- **情绪表征定位于transformer约50%深度的中间层，呈架构不变U型曲线，生成式提取效果更优，p=0.007。**
  _[Extracting and Steering Emotion Representations in Small Language...](http://arxiv.org/abs/2604.04064)_


### 🔬 自适应层选择（1 篇）

- **实际场景中不同输入对应的最优引导干预层差异很大，输入依赖的自适应层选择优于固定层方法。**
  _[Where to Steer: Input-Dependent Layer Selection for Steering Impr...](http://arxiv.org/abs/2604.03867)_


### 🔬 真理方向边界（1 篇）

- **真理方向高度依赖模型层、任务类型与复杂度，提示指令会显著影响真理探针的泛化能力**
  _[Testing the Limits of Truth Directions in LLMs](http://arxiv.org/abs/2604.03754)_


### 🔬 幻觉检测（1 篇）

- **集成VLM的多种不同内部信号，可显著提升多模态幻觉检测鲁棒性，AUC稳定优于现有方法与单检测器模型**
  _[EnsemHalDet: Robust VLM Hallucination Detection via Ensemble of I...](http://arxiv.org/abs/2604.02784)_


### 🔬 功能向量机制（1 篇）

- **所有任务模型均存在可引导不可解码现象，FV最优干预在L2-L8，logit仅能在L28-L32解码**
  _[Steerable but Not Decodable: Function Vectors Operate Beyond the ...](http://arxiv.org/abs/2604.02608)_


### 🔬 大模型迎合行为（1 篇）

- **社会迎合数据集中大语言模型假设的最高频二元组为'寻求认可'，人际对话训练的模型未考虑人们对人工智能的期望差异。**
  _[Verbalizing LLMs'assumptions to explain and control sycophancy](http://arxiv.org/abs/2604.03058)_


### 🔬 推理转向控制（1 篇）

- **541个关键词检测出的行为边界中，93.3%行为不稳定，同一前缀重生成无法复现检测到的行为**
  _[Reliable Control-Point Selection for Steering Reasoning in Large ...](http://arxiv.org/abs/2604.02113)_


### 🔬 认知幻觉缓解（1 篇）

- **MLLM解码早期确定的视觉注意力会保持惯性静态，无法动态支持关系推理，是认知幻觉的关键诱因**
  _[Attention at Rest Stays at Rest: Breaking Visual Inertia for Cogn...](http://arxiv.org/abs/2604.01989)_


### 🔬 流行度偏差校正（1 篇）

- **SPREE可针对不同用户调整流行度引导的方向与幅度，多数据集验证其提升对齐性且保留推荐质量。**
  _[Aligning Recommendations with User Popularity Preferences](http://arxiv.org/abs/2604.01036)_


### 🔬 未分类（20 篇）

- **在多个数据集上精度优于基线方法，退化和跨域测试性能提升明显，给出不确定性感知SSL设计原则** 💻
  _[Trust-SSL: Additive-Residual Selective Invariance for Robust Aeri...](http://arxiv.org/abs/2604.21349v1)_

- **发现对齐伪装比已有研究报告更普遍，所提方法可大幅降低对齐伪装发生率**
  _[Value-Conflict Diagnostics Reveal Widespread Alignment Faking in ...](http://arxiv.org/abs/2604.20995v1)_

- **对八个SOTA开源大模型完成审计，揭示不同模型的鲁棒性差异，验证可解释性转向是有效安全审计工具。**
  _[Breaking Bad: Interpretability-Based Safety Audits of State-of-th...](http://arxiv.org/abs/2604.20945v1)_

- **发现单头注意力对残差流的贡献是线性关系分类的较强特征，揭示了探针准确率与多个关系特征的相关性**
  _[Tracing Relational Knowledge Recall in Large Language Models](http://arxiv.org/abs/2604.19934v2)_

- **发现正确定量推理对应良性自阅读模式，所提方法实验中获得了一致的准确率提升**
  _[How Do Answer Tokens Read Reasoning Traces? Self-Reading Patterns...](http://arxiv.org/abs/2604.19149v1)_

- **实现多模型多任务鲁棒细粒度行为控制，性能优于基线，给出跟踪误差理论保证。**
  _[Local Linearity of LLMs Enables Activation Steering via Model-Bas...](http://arxiv.org/abs/2604.19018v1)_

- **揭示AlphaEarth嵌入为非欧流形，证明几何感知推理可提升复杂环境查询回答质量**
  _[Characterizing AlphaEarth Embedding Geometry for Agentic Environm...](http://arxiv.org/abs/2604.18715v1)_

- **所提方法性能显著优于多个主流基线，发现了检测-校正解离的新现象**
  _[Latent Phase-Shift Rollback: Inference-Time Error Correction via ...](http://arxiv.org/abs/2604.18567v1)_

- **SIREN性能大幅优于现有最优开源防护模型，参数量更少，泛化能力与推理效率表现更出色**
  _[LLM Safety From Within: Detecting Harmful Content with Internal R...](http://arxiv.org/abs/2604.18519v1)_

- **在推理后训练与安全对齐任务验证，效果优于人工表征方法，可支撑多阶段模型行为干预**
  _[Characterizing Model-Native Skills](http://arxiv.org/abs/2604.17614v1)_

- **发现大模型支持策略随估计的用户困扰程度系统变化，揭示单轮评估无法发现的轨迹级动态**
  _[Auditing Support Strategies in LLMs through Grounded Multi-Turn S...](http://arxiv.org/abs/2604.17079v1)_

- **证实方法最高减少74%不安全生成，开销可忽略，指出该问题是可解释性问题而非训练伪影**
  _[Surgical Repair of Insecure Code Generation in LLMs](http://arxiv.org/abs/2604.16697v1)_

- **多个推理基准实验表明，相比大推理模型最高降1.75倍延迟，仍保持有竞争力的精度**
  _[RankGuide: Tensor-Rank-Guided Routing and Steering for Efficient ...](http://arxiv.org/abs/2604.16694v1)_

- **经多模型多概念验证预测相关性高，提出三机制框架，实体导向实验验证方法优于传统启发式层选择**
  _[Predicting Where Steering Vectors Succeed](http://arxiv.org/abs/2604.15557v1)_

- **在安全与真实性基准实验中优于现有最优方法，以极小效用损失获得更强引导性能**
  _[FineSteer: A Unified Framework for Fine-Grained Inference-Time St...](http://arxiv.org/abs/2604.15488v1)_

- **提出新基准PARATOX，该方法减毒效果更优，保留生成流畅度，头选择速度提升7倍**
  _[CausalDetox: Causal Head Selection and Intervention for Language ...](http://arxiv.org/abs/2604.14602v1)_

- **证实多款大语言模型将嫉妒编码为目标因子的结构化线性组合，可为多智能体AI安全表征干预提供路径。**
  _[Mechanistic Decoding of Cognitive Constructs in Large Language Mo...](http://arxiv.org/abs/2604.14593v3)_

- **证实均值差注入性能优于现有基线，混合方法性能更优，验证其符合线性表示假设，可提供线性控制**
  _[Psychological Steering of Large Language Models](http://arxiv.org/abs/2604.14463v1)_

- **多模型多基准数据集实验表明，GeoDe显著提升模型真实性，在分布外场景泛化能力强。** 💻
  _[Purging the Gray Zone: Latent-Geometric Denoising for Precise Kno...](http://arxiv.org/abs/2604.14324v1)_

- **证实修辞信号可被稳定探测，发现修辞问句在LLM中由多个带不同线索的线性方向编码而非单一共享方向。**
  _[Rhetorical Questions in LLM Representations: A Linear Probing Stu...](http://arxiv.org/abs/2604.14128v2)_


---
*ArXiv_Daily_Digest 自动生成 | 2026-07-01*