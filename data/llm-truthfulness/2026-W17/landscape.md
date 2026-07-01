# 📡 llm-truthfulness — 方法版图
> 2026-W17 (04/20-04/26) | 本周 155 篇 | 自动生成

📊 **120** 个方法族 | **0** 篇 high priority | **6** 篇附带代码

---

### 🔬 大模型幻觉缓解（4 篇）

- **替换通用指令数据后，HypoTermScore中位数提升0.19%至25.91%，FactScore提升0.39%至0.86%，MMLU仅下降0.26%至0.3...**
  _[Inducing Epistemological Humility in Large Language Models: A Tar...](http://arxiv.org/abs/2603.17504)_

- **AAC可让WikiText-103困惑度和MMLU准确率零退化，在LLaMA 3-8B上选择性比ITI高3.5-5.94倍**
  _[Adaptive Activation Cancellation for Hallucination Mitigation in ...](http://arxiv.org/abs/2603.10195)_

- **该方法生成的建议81%优于人工真值，基本消除关键召回失败，性能显著优于标准通用自一致性**
  _[Reducing Hallucination in Enterprise AI Workflows via Hybrid Util...](http://arxiv.org/abs/2604.11141)_

- **大语言模型的浅层主要依赖均匀注意力模式，该模式会让模型无法聚焦相关信息进而引发幻觉。**
  _[ART: Attention Replacement Technique to Improve Factuality in LLM...](http://arxiv.org/abs/2604.06393)_


### 🔬 表征几何分析（2 篇）

- **大语言模型在早期层分离字面与比喻用法，中后层将具体性压缩为跨模型一致的一维方向**
  _[Exploring Concreteness Through a Figurative Lens](http://arxiv.org/abs/2604.18296)_

- **在未适配Phi模型中对比分离AUC达0.984，ALM8扰动数据五折平均AUC为0.72，隐几何跨底物可检测**
  _[ATLAS: Constitution-Conditioned Latent Geometry and Redistributio...](http://arxiv.org/abs/2604.17663)_


### 🔬 幻觉检测（2 篇）

- **将幻觉建模为大语言模型潜动力学的关键转变，幻觉错误可归因于特定高能量稀疏特征**
  _[HalluSAE: Detecting Hallucinations in Large Language Models via S...](http://arxiv.org/abs/2604.16430)_

- **集成VLM多种不同内部信号，相比单检测器与现有方法，可稳定提升多模态幻觉检测的AUC性能与鲁棒性。**
  _[EnsemHalDet: Robust VLM Hallucination Detection via Ensemble of I...](http://arxiv.org/abs/2604.02784)_


### 🔬 大模型幻觉检测（2 篇）

- **结合空间token筛选与时间去噪动态偏差建模，DynHD检测性能和效率均优于现有最优方法**
  _[DynHD: Hallucination Detection for Diffusion Large Language Model...](http://arxiv.org/abs/2603.16459)_

- **分层Transformer探针M3在单折验证和留出测试集表现最佳，探针推理延迟仅0.15~6.66ms，实际开销可忽略**
  _[Weakly Supervised Distillation of Hallucination Signals into Tran...](http://arxiv.org/abs/2604.06277)_


### 🔬 大模型可解释性（2 篇）

- **抑制混淆特征可实现1.1%准确率提升与75%熵降，3个混淆特征预测正确性AUROC约0.79**
  _[Are LLM Uncertainty and Correctness Encoded by the Same Features?...](http://arxiv.org/abs/2604.19974)_

- **当前大模型VRU任务表现远差于人类，模型虽编码视角信息，但无法绑定视角与对应观测，最终层产生幻觉**
  _[How Do LLMs and VLMs Understand Viewpoint Rotation Without Vision...](http://arxiv.org/abs/2604.15294)_


### 🔬 大模型安全对齐（2 篇）

- **大语言模型中存在负责有害行为的"不安全票"，剪枝后可得到兼顾性能与安全的"安全票"**
  _[Pruning Unsafe Tickets: A Resource-Efficient Framework for Safer ...](http://arxiv.org/abs/2604.15780)_

- **仅单独约束权重或激活都不足以保持大语言模型安全性，CWAC在高有害数据占比下仍优于强基线。**
  _[Preventing Safety Drift in Large Language Models via Coupled Weig...](http://arxiv.org/abs/2604.12384)_


### 🔬 多价值对齐（2 篇）

- **经价值一致性过滤训练得到的策略模型保留了更好的线性模式连通性，VC-Soup性能优于现有多价值对齐方法**
  _[VC-Soup: Value-Consistency Guided Multi-Value Alignment for Large...](http://arxiv.org/abs/2603.18113)_

- **最小化不同人类价值间的互信息可缓解参数干扰，所提MVA框架多价值对齐性能优于现有所有基线**
  _[Multi-Value Alignment for LLMs via Value Decorrelation and Extrap...](http://arxiv.org/abs/2511.17579)_


### 🔬 多目标对齐（2 篇）

- **MoSLoRA通过共享偏好无关特征加条件调制，可缓解特征纠缠，实现推理阶段偏好权衡的精准控制**
  _[UniARM: Towards a Unified Autoregressive Reward Model for Multi-O...](http://arxiv.org/abs/2602.09538)_

- **交叉目标干扰普遍存在且具有强模型依赖性，目标收益与标量化得分正协方差时目标一阶提升**
  _[Uncovering Cross-Objective Interference in Multi-Objective Alignm...](http://arxiv.org/abs/2602.06869)_


### 🔬 大模型偏好优化（2 篇）

- **设计基于DPO的大语言模型偏好优化算法时，需要同时考虑token长度与反馈长度两种不同长度测度**
  _[Autoregressive Direct Preference Optimization](http://arxiv.org/abs/2602.09533)_

- **跨七个基模型，策略选择准确率从35-46%提升至68-78%，分布内推理增益最高达6.6个百分点**
  _[Continuous-Utility Direct Preference Optimization](http://arxiv.org/abs/2602.00931)_


### 🔬 AI流体建模幻觉（1 篇）

- **流体动力学AI模型的幻觉源于其光谱偏误，高流速、高粘度反差下该偏误占主导，幻觉违反物理守恒律**
  _[AI models of unstable flow exhibit hallucination](http://arxiv.org/abs/2604.20372v1)_


### 🔬 无监督关系学习（1 篇）

- **在无任何真值标签情况下可分割多物体，物体间相对运动可准确映射到一维加法潜在空间**
  _[Unsupervised Learning of Inter-Object Relationships via Group Hom...](http://arxiv.org/abs/2604.20925v1)_


### 🔬 多模态命名实体识别（1 篇）

- **量化模型实体级不确定性得到知识缺口信号，混合奖励惩罚不必要检索，实现精准检索决策提升GMNER性能**
  _[SAKE: Self-aware Knowledge Exploitation-Exploration for Grounded ...](http://arxiv.org/abs/2604.20146v1)_


### 🔬 深度学习理论（1 篇）

- **指向深度学习科学理论的研究可分为五大方向，该新兴理论可命名为学习力学，与机械可解释性存在共生关系**
  _[There Will Be a Scientific Theory of Deep Learning](http://arxiv.org/abs/2604.21691)_


### 🔬 内在维度估计（1 篇）

- **常用的神经表征内在维度估计器实际上并未跟踪表征真实的潜在内在维度，存在理论与实践的关键偏差**
  _[Rethinking Intrinsic Dimension Estimation in Neural Representatio...](http://arxiv.org/abs/2604.20276)_


### 🔬 大模型逢迎机制（1 篇）

- **携带错误信号的注意力头沉默后大幅翻转逢迎行为且不影响准确率，RLHF降逢迎十倍但共享头仍保留**
  _[LLMs Know They're Wrong and Agree Anyway: The Shared Sycophancy-L...](http://arxiv.org/abs/2604.19117)_


### 🔬 大模型激活引导（1 篇）

- **尽管Transformer块是非线性结构，多种架构、不同规模大语言模型的逐层动力学都可被局部线性模型良好近似。**
  _[Local Linearity of LLMs Enables Activation Steering via Model-Bas...](http://arxiv.org/abs/2604.19018)_


### 🔬 大模型安全检测（1 篇）

- **基于LLM内部跨层特征的SIREN检测性能超SOTA开源防护模型，可训练参数量仅为其1/250，支持实时流式检测。**
  _[LLM Safety From Within: Detecting Harmful Content with Internal R...](http://arxiv.org/abs/2604.18519)_


### 🔬 幻觉神经元定位（1 篇）

- **所有模型与设置下作者名字段引用错误远多于其他字段，幻觉信号无法跨领域泛化，调控特定神经元可改变幻觉程度**
  _[Where Fake Citations Are Made: Tracing Field-Level Hallucination ...](http://arxiv.org/abs/2604.18880)_


### 🔬 有害意图检测（1 篇）

- **软AUC优化线性方向检测平均AUROC达0.98、TPR@1%FPR达0.80，有害意图与拒绝行为功能分离**
  _[Harmful Intent as a Geometrically Recoverable Feature of LLM Resi...](http://arxiv.org/abs/2604.18901)_


### 🔬 多智能体对抗防御（1 篇）

- **当被污染智能体占多数时，多数投票准确率崩溃，令牌级轮询仍能维持稳健的推理准确率。**
  _[The Consensus Trap: Rescuing Multi-Agent LLMs from Adversarial Ma...](http://arxiv.org/abs/2604.17139)_


### 🔬 不确定性估计（1 篇）

- **SIVR利用大模型跨层内部表示离散度估计不确定性，性能优于强基线，泛化性强且无需大规模训练集** 💻
  _[Learning Uncertainty from Sequential Internal Dispersion in Large...](http://arxiv.org/abs/2604.15741)_


### 🔬 线性探针分析（1 篇）

- **修辞问句跨数据集检测AUROC约0.7-0.8，不同数据集训练探针的Top结果重叠常低于0.2，由多线性方向编码**
  _[Rhetorical Questions in LLM Representations: A Linear Probing Stu...](http://arxiv.org/abs/2604.14128)_


### 🔬 模型适配范式（1 篇）

- **激活引导是激活空间定向干预的适配范式，无需参数更新即可实现局部可逆的模型行为改变**
  _[From Weights to Activations: Is Steering the Next Frontier of Ada...](http://arxiv.org/abs/2604.14090)_


### 🔬 大模型潜在规划（1 篇）

- **Qwen-3系列（0.6B-14B）的潜在规划能力随模型规模提升增长，复杂押韵任务中大模型也很少做长远规划。** `ICLR 2026`
  _[Latent Planning Emerges with Scale](http://arxiv.org/abs/2604.12493)_


### 🔬 特征可解释性（1 篇）

- **将LRH工具作用于质心而非隐层激活，得到DINO ViT更稀疏且下游性能更好的特征字典，可识别GPT2-Large电路。** 💻
  _[The Linear Centroids Hypothesis: How Deep Network Features Repres...](http://arxiv.org/abs/2604.11962)_


### 🔬 多模态幻觉缓解（1 篇）

- **幻觉与高熵状态的认知分叉点强相关，源于中间层视觉语义锚定失效，模型转而依赖语言先验**
  _[Cognitive Pivot Points and Visual Anchoring: Unveiling and Rectif...](http://arxiv.org/abs/2604.10219)_


### 🔬 模型信息泄露（1 篇）

- **模型易获取的top logit值瓶颈也会泄露图像查询的任务无关信息，部分场景信息量与全残差流直接投影相当**
  _[What do your logits know? (The answer may surprise you!)](http://arxiv.org/abs/2604.09885)_


### 🔬 探针分析（1 篇）

- **分布内评估探针QWK约0.7，性能远超基线，但所有探针跨语料评估性能均崩塌，仅学到语料特有属性**
  _[Multilingual Embedding Probes Fail to Generalize Across Learner C...](http://arxiv.org/abs/2604.07095)_


### 🔬 大模型欺骗分类（1 篇）

- **分析50个现有基准发现，全部基准都测试了编造类欺骗，语用扭曲等三类内容覆盖严重不足，战略欺骗基准仍不成熟**
  _[From Hallucination to Scheming: A Unified Taxonomy and Benchmark ...](http://arxiv.org/abs/2604.04788)_


### 🔬 大模型真值方向（1 篇）

- **真值方向高度依赖模型层、任务类型与复杂度，模型指令会显著影响真值探针的泛化能力**
  _[Testing the Limits of Truth Directions in LLMs](http://arxiv.org/abs/2604.03754)_


### 🔬 语言生成控制（1 篇）

- **识别出的语言特异性特征极度稀疏，对目标语言高选择性，方向消融仅增加对应语言的交叉熵损失**
  _[LangFIR: Discovering Sparse Language-Specific Features from Monol...](http://arxiv.org/abs/2604.03532)_


### 🔬 功能向量引导（1 篇）

- **所有任务模型的FV引导准确率均高于对数透镜，最大差距达0.91，FV最优干预在早层L2-L8，对数透镜仅晚层能检出**
  _[Steerable but Not Decodable: Function Vectors Operate Beyond the ...](http://arxiv.org/abs/2604.02608)_


### 🔬 多智能体合谋检测（1 篇）

- **探针分布内AUROC达1.00，零样本迁移AUROC为0.60-0.86，合谋信号位于token级，处理编码消息时激活突增。** 💻
  _[Detecting Multi-Agent Collusion Through Multi-Agent Interpretabil...](http://arxiv.org/abs/2604.01151)_


### 🔬 大模型探针评估（1 篇）

- **该探针预测下游性能平均AUROC大于0.75，可将评估延迟从约1小时降至约3分钟，具备跨检查点泛化能力**
  _[Fast and Accurate Probing of In-Training LLMs'Downstream Performa...](http://arxiv.org/abs/2604.01025)_


### 🔬 奖励黑客缓解（1 篇）

- **发现在编码任务中奖励黑客存在可重复的三阶段反弹模式，捷径概念方向可紧密追踪黑客行为**
  _[When Reward Hacking Rebounds: Understanding and Mitigating It wit...](http://arxiv.org/abs/2604.01476)_


### 🔬 多语言表示学习（1 篇）

- **平行数据仅能加速预训练早期表示共享、减少语言特异性神经元，无它也可达到相近跨语言对齐水平**
  _[On the limited utility of parallel data for learning shared multi...](http://arxiv.org/abs/2603.29026)_


### 🔬 算术泛化延迟（1 篇）

- **冻结已收敛编码器仅训解码器可消除泛化平台，对齐运算的基数达99.8%准确率，二进制完全失败。**
  _[The Long Delay to Arithmetic Generalization: When Learned Represe...](http://arxiv.org/abs/2604.13082)_


### 🔬 拒绝机制分析（1 篇）

- **有害拒绝方向任务无关，可被单个全局向量捕获，过度拒绝是任务依赖的高维子空间，二者在Transformer早期层就表征不同**
  _[Over-Refusal and Representation Subspaces: A Mechanistic Analysis...](http://arxiv.org/abs/2603.27518)_


### 🔬 大模型幻觉攻防（1 篇）

- **可将幻觉信号定位到少量高方差幻觉节点，检测AUC达0.90，防御将鲁棒性从8%提升至最高0.69**
  _[H-Node Attack and Defense in Large Language Models](http://arxiv.org/abs/2603.26045)_


### 🔬 幻觉神经元泛化（1 篇）

- **域内训练的分类器AUROC为0.783，跨域迁移后仅0.563，降幅0.220，p<0.001，幻觉神经元无法跨域泛化**
  _[Do Hallucination Neurons Generalize? Evidence from Cross-Domain T...](http://arxiv.org/abs/2604.19765)_


### 🔬 置信度校准（1 篇）

- **校准与口头置信度信号均线性编码但互相正交，推理会干扰置信方向加剧误校准，称推理污染效应。**
  _[Closing the Confidence-Faithfulness Gap in Large Language Models](http://arxiv.org/abs/2603.25052)_


### 🔬 安全探针检测（1 篇）

- **相同RLHF训练、行为一致的两类模型，说谎者检测率超95%，一致错位的狂热者几乎完全躲避检测。**
  _[Why Safety Probes Catch Liars But Miss Fanatics](http://arxiv.org/abs/2603.25861)_


### 🔬 大模型道德判断（1 篇）

- **评估22个大语言模型发现几乎所有模型都具语境敏感性，模型与人类受不同语境变化触发，基础对齐不代表语境敏感性对齐。**
  _[Between Rules and Reality: On the Context Sensitivity of LLM Mora...](http://arxiv.org/abs/2603.23114)_


### 🔬 大模型脑电分析（1 篇）

- **个体特异性信号集中在LLM深层，28层中于第24层达峰值，高伽马功率预测rho=0.183，为群体探针的九倍。**
  _[Riding Brainwaves in LLM Space: Understanding Activation Patterns...](http://arxiv.org/abs/2603.21847)_


### 🔬 内省感知机制（1 篇）

- **内省检测为两阶段电路，消融拒绝方向提检测53%，训练偏置向量提75%且不增加假阳性** 💻
  _[Mechanisms of Introspective Awareness](http://arxiv.org/abs/2603.21396)_


### 🔬 幻觉信号涌现（1 篇）

- **低于400M参数模型无可靠幻觉信号，超1B参数模型信号峰值在首token生成前，该效应需指令调优才会出现**
  _[Before the First Token: Scale-Dependent Emergence of Hallucinatio...](http://arxiv.org/abs/2604.13068)_


### 🔬 机械可解释性（1 篇）

- **线性探针区分病例AUROC达98.2%，模型输出灵敏度仅45.1%，最优方法仅纠正24%漏诊，余76%未纠正**
  _[Interpretability without actionability: mechanistic methods canno...](http://arxiv.org/abs/2603.18353)_


### 🔬 动机推理检测（1 篇）

- **生成前探测动机推理效果与访问完整CoT轨迹的LLM监控器相当，生成后探测效果优于该监控器**
  _[Catching rationalization in the act: detecting motivated reasonin...](http://arxiv.org/abs/2603.17199)_


### 🔬 大模型内省（1 篇）

- **前沿模型预测自身行为优于同类模型，LLM无需显式训练即可学会内省，内省机制经注意力扩散涌现**
  _[Me, Myself, and $\pi$ : Evaluating and Explaining LLM Introspecti...](http://arxiv.org/abs/2603.20276)_


### 🔬 无训练模型引导（1 篇）

- **发现跨模态迁移现象，少量文本得到的引导向量可有效引导语音推理，准确率最高提升4.4%**
  _[Nudging Hidden States: Training-Free Model Steering for Chain-of-...](http://arxiv.org/abs/2603.14636)_


### 🔬 双表示空间编码（1 篇）

- **经小模型合成实验发现，Transformer中上下文与样本共享编码空间是ICL与IWL冲突的潜在来源**
  _[Reconciling In-Context and In-Weight Learning via Dual Representa...](http://arxiv.org/abs/2603.13459)_


### 🔬 真理偏好机制（1 篇）

- **梯度下降偏好最可压缩的答案簇而非真理，单一致错误准确率45-51%，10个竞争规则时达88%**
  _[Truth as a Compression Artifact in Language Model Training](http://arxiv.org/abs/2603.11749)_


### 🔬 幻觉几何分隔（1 篇）

- **经PCA白化后，簇承诺度排序符合预测：错阱收敛>中心漂移>覆盖缺口，一、二类分离不存在于任何谱带**
  _[Whitening Reveals Cluster Commitment as the Geometric Separator o...](http://arxiv.org/abs/2603.07755)_


### 🔬 大模型行为引导（1 篇）

- **COLD-Steer可达到最高95%的引导效果，相比最优基线所需样本数量减少了50倍** `ICLR 2026`
  _[COLD-Steer: Steering Large Language Models via In-Context One-ste...](http://arxiv.org/abs/2603.06495)_


### 🔬 大模型信任分析（1 篇）

- **EleutherAI/gpt-j-6B的内部信任表征与Castelfranchi社会认知模型对齐程度最高，其次为Marsh模型**
  _[Evaluating LLM Alignment with Human Trust Models](http://arxiv.org/abs/2603.05839)_


### 🔬 大模型隐私遗忘（1 篇）

- **删除用户代理后模型KL散度约0.21 nats，验证通过率82-89%，跨用户污染接近零**
  _[Separable Expert Architecture: Toward Privacy-Preserving LLM Pers...](http://arxiv.org/abs/2604.21571)_


### 🔬 幻觉缓解（1 篇）

- **提出的MPD框架可降低23.4%的幻觉，同时保留原模型97.4%的通用生成能力，无额外计算成本**
  _[Mitigating Hallucinations in Large Vision-Language Models without...](http://arxiv.org/abs/2604.20366)_


### 🔬 接地推理训练（1 篇）

- **GRIL最高提升前提检测达45%，任务成功率提升30%，平均响应长度缩短超20%**
  _[Pause or Fabricate? Training Language Models for Grounded Reasoni...](http://arxiv.org/abs/2604.19656)_


### 🔬 LLM部署诊断（1 篇）

- **监督对齐几何稳定性预测可导向性ρ达0.89-0.97，无监督漂移检测假警率比Procrustes低6倍**
  _[The Geometric Canary: Predicting Steerability and Detecting Drift...](http://arxiv.org/abs/2604.17698)_


### 🔬 语言模型解毒（1 篇）

- **CausalDetox对比基线最高多实现5.34%的毒性降低，保留语言流畅度，头选择速度提升7倍。**
  _[CausalDetox: Causal Head Selection and Intervention for Language ...](http://arxiv.org/abs/2604.14602)_


### 🔬 细粒度推理引导（1 篇）

- **SCS通过避免不必要引导保留模型效用，MoSE生成查询特定引导向量，FineSteer性能优于现有SOTA且效用损失极小**
  _[FineSteer: A Unified Framework for Fine-Grained Inference-Time St...](http://arxiv.org/abs/2604.15488)_


### 🔬 幻觉产生机制（1 篇）

- **44.3%的提示会在首个生成token分岔，注入幻觉激活破坏87.5%正确轨迹，反向仅恢复33.3%**
  _[Hallucination as Trajectory Commitment: Causal Evidence for Asymm...](http://arxiv.org/abs/2604.15400)_


### 🔬 引导效果预测（1 篇）

- **峰值A_lin预测引导效果相关系数ρ为0.86~0.91，预测层选择ρ为0.63~0.92，LAP推荐层效果更优**
  _[Predicting Where Steering Vectors Succeed](http://arxiv.org/abs/2604.15557)_


### 🔬 推理退化监控（1 篇）

- **基于大模型的伴侣减少52-62%重复、开销约11%；探针式零开销，平均效应量+0.471，最佳AUROC达0.840**
  _[The cognitive companion: a lightweight parallel monitoring archit...](http://arxiv.org/abs/2604.13759)_


### 🔬 MoE幻觉缓解（1 篇）

- **静态Top-k路由偏好高频模式使长尾知识专家休眠，CoR不增推理预算平均提升事实准确率3.1%**
  _[Awakening Dormant Experts:Counterfactual Routing to Mitigate MoE ...](http://arxiv.org/abs/2604.14246)_


### 🔬 混合专家可解释性（1 篇）

- **转向时间专家质心可提升时间类别概率321%，抑制地理专家使其概率降23%，仅余弦路由具备几何透明性**
  _[Geometric Routing Enables Causal Expert Control in Mixture of Exp...](http://arxiv.org/abs/2604.14434)_


### 🔬 缓解模型谄媚（1 篇）

- **在人类通常寻求验证的查询中，用户期望大语言模型提供客观信息，大语言模型却默认用户寻求验证，该错配引发谄媚。**
  _[Verbalizing LLMs' Assumptions About the User to Calibrate Expecta...](https://www.semanticscholar.org/paper/71215b1da630dc25040fb0e73ebde99e13da321e)_


### 🔬 上下文锚定（1 篇）

- **SinkTrack在SQuAD2.0提升21.6%，在M3CoT提升22.8%，跨不同模型架构规模均有稳定增益** 💻
  _[SinkTrack: Attention Sink based Context Anchoring for Large Langu...](http://arxiv.org/abs/2604.10027)_


### 🔬 VLM可解释性（1 篇）

- **最终层logit差距预测接地结果相关性达0.847，替换MAC识别层全序列可改变60%~84%的输出**
  _[Arbitration Failure, Not Perceptual Blindness: How Vision-Languag...](http://arxiv.org/abs/2604.09364)_


### 🔬 扩散生成控制（1 篇）

- **对DiT选定层和时间步动态施加学习得到的引导向量，无需耗时重训即可实现灵活多样的生成控制**
  _[SHIFT: Steering Hidden Intermediates in Flow Transformers](http://arxiv.org/abs/2604.09213)_


### 🔬 激活引导对齐（1 篇）

- **三种激活引导都可恢复对齐特质保留连贯性，StTP与StMP比SwFC更能维持通用能力、减少多轮重复**
  _[Activation Steering for Aligned Open-ended Generation without Sac...](http://arxiv.org/abs/2604.08169)_


### 🔬 多轮置信校准（1 篇）

- **研究发现用户反馈（例如说服类内容）会降低大语言模型多轮对话的置信度校准效果**
  _[Confidence Should Be Calibrated More Than One Turn Deep](http://arxiv.org/abs/2604.05397)_


### 🔬 RAG忠实度监控（1 篇）

- **在PubMedQA结合Llama-3-8B达0.942 AUROC仅0.77ms开销，16位定点保留99.8%FP16 AUROC**
  _[LatentAudit: Real-Time White-Box Faithfulness Monitoring for Retr...](http://arxiv.org/abs/2604.05358)_


### 🔬 指令遵循机制（1 篇）

- **指令遵循是多样语言能力的灵巧协调而非单一通用机制，不同复杂度任务分层分布在模型不同层**
  _[How LLMs Follow Instructions: Skillful Coordination, Not a Univer...](http://arxiv.org/abs/2604.06015)_


### 🔬 语言模型记忆控制（1 篇）

- **参数α可可靠控制记忆压力，见过样本准确率单调提升，未见过样本准确率稳定，大模型对记忆压力更敏感**
  _[Memory Dial: A Training Framework for Controllable Memorization i...](http://arxiv.org/abs/2604.05074)_


### 🔬 情感表征提取（1 篇）

- **情感表征定位在Transformer约50%深度的中间层，基于生成提取法情感分离更优（p=0.007，Cohen's d=-107.5）**
  _[Extracting and Steering Emotion Representations in Small Language...](http://arxiv.org/abs/2604.04064)_


### 🔬 引导层选择（1 篇）

- **LLM对齐引导中，最优干预层会随输入不同发生很大变化，W2S在分布内外性能均优于固定层方法**
  _[Where to Steer: Input-Dependent Layer Selection for Steering Impr...](http://arxiv.org/abs/2604.03867)_


### 🔬 大模型谄媚调控（1 篇）

- **社会谄媚数据集中，大语言模型假设最高频二元组为“寻求验证”，训练于人人对话的大模型未区分人机需求差异**
  _[Verbalizing LLMs'assumptions to explain and control sycophancy](http://arxiv.org/abs/2604.03058)_


### 🔬 转向控制点选择（1 篇）

- **541个关键词检测得到的推理行为边界中，93.3%行为不稳定，无法从相同前缀重生成中复现目标行为**
  _[Reliable Control-Point Selection for Steering Reasoning in Large ...](http://arxiv.org/abs/2604.02113)_


### 🔬 认知幻觉缓解（1 篇）

- **多模态大语言模型视觉注意力存在惯性，解码早期稳定后保持静态，是引发认知幻觉的关键因素**
  _[Attention at Rest Stays at Rest: Breaking Visual Inertia for Cogn...](http://arxiv.org/abs/2604.01989)_


### 🔬 流行度偏差校正（1 篇）

- **SPREE可依据用户个人流行度偏差自适应调整激活方向与大小，效果优于均匀降流行度的全局去偏方法**
  _[Aligning Recommendations with User Popularity Preferences](http://arxiv.org/abs/2604.01036)_


### 🔬 科学推理增强（1 篇）

- **优化后的8B参数模型性能可媲美专有模型，RL循环加入可验证规则反馈是纯缩放的参数高效替代方案。**
  _[QuantumQA: Enhancing Scientific Reasoning via Physics-Consistent ...](http://arxiv.org/abs/2604.18176)_


### 🔬 大模型强化学习（1 篇）

- **可从数据、训练、框架三个互补视角自底向上构建该领域方法分类体系，为研究提供清晰概念基础。**
  _[A Survey of Reinforcement Learning for Large Language Models unde...](http://arxiv.org/abs/2604.17312)_


### 🔬 大模型奖励黑客（1 篇）

- **奖励黑客源于目标压缩、优化放大、评估器-策略共适应三者交互，局部捷径可泛化为更广泛错位**
  _[Reward Hacking in the Era of Large Models: Mechanisms, Emergent M...](http://arxiv.org/abs/2604.13602)_


### 🔬 形式化规范合成（1 篇）

- **将候选规范拒绝负测试的比例作为完备性信号融入训练奖励，性能优于SFT和二元奖励强化学习**
  _[Reinforcement Learning with Negative Tests as Completeness Signal...](http://arxiv.org/abs/2604.05820)_


### 🔬 多偏好LLM对齐（1 篇）

- **PLC可在存在足够优势联盟盈余时容忍局部退化，帮助优化轨迹逃离局部次优均衡，得到更优帕累托前沿**
  _[Beyond Compromise: Pareto-Lenient Consensus for Efficient Multi-P...](http://arxiv.org/abs/2604.05965)_


### 🔬 大模型个性化（1 篇）

- **小规模大语言模型组合即可实现近最优用户个性化，输出多样性优于常见基线，明确了系统成本与个性化的权衡关系**
  _[Many Preferences, Few Policies: Towards Scalable Language Model P...](http://arxiv.org/abs/2604.04144)_


### 🔬 文本转SQL（1 篇）

- **ATR被证明是能量耗散算子，可保证无环策略单调收敛，在BIRD上较binary-reward GRPO获得5%性能增益**
  _[SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Column-...](http://arxiv.org/abs/2603.16161)_


### 🔬 视觉语言导航（1 篇）

- **SACA可逐步评估将失败轨迹拆分为有效前缀和精确分歧点，提取密集监督实现最优性能**
  _[Let's Reward Step-by-Step: Step-Aware Contrastive Alignment for V...](http://arxiv.org/abs/2603.09740)_


### 🔬 大模型个性化基准（1 篇）

- **模型难以提取潜在用户特征，强模型记忆更新存性能天花板，大干扰池下检索准确率骤降，显式记忆不保证偏好对齐**
  _[AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Mem...](http://arxiv.org/abs/2603.26680)_


### 🔬 交替强化学习（1 篇）

- **奖励聚合存在方差收缩效应，在HealthBench上，ARL-RR在1.7B到14B不同规模均优于标量化方法**
  _[Alternating Reinforcement Learning with Contextual Rubric Rewards](http://arxiv.org/abs/2603.15646)_


### 🔬 强化学习策略优化（1 篇）

- **监督微调损失对模型logits的凸性会诱导优化产生良好梯度方向，PPO缺乏该稳定性质**
  _[Stabilizing Policy Optimization via Logits Convexity](http://arxiv.org/abs/2603.00963)_


### 🔬 扩散语言建模（1 篇）

- **加入预生成思考阶段用潜扩散优化语义规划，性能优于同规模模型，大模型评判胜率超70%**
  _[Stop-Think-AutoRegress: Language Modeling with Latent Diffusion P...](http://arxiv.org/abs/2602.20528)_


### 🔬 过程奖励模型学习（1 篇）

- **rePIRL可统一在线与离线PRM学习，在标准化数学、编码推理任务上效果优于现有方法**
  _[rePIRL: Learn PRM with Inverse RL for LLM Reasoning](http://arxiv.org/abs/2602.07832)_


### 🔬 解码时个性化（1 篇）

- **基于相似度的属性检索机制可有效缓解上下文偏好偏移，EXACT性能始终优于多个现有强基线**
  _[EXACT: Explicit Attribute-Guided Decoding-Time Personalization](http://arxiv.org/abs/2602.17695)_


### 🔬 基础模型训练策略（1 篇）

- **该研究按感知、估值、执行、整合四个层级分类梳理问题，提出了RLHB、CoTHB两种具体训练方法**
  _[A New Strategy for Artificial Intelligence: Training Foundation M...](http://arxiv.org/abs/2601.12053)_


### 🔬 策略优化算法（1 篇）

- **在Amazon ESCI与H&M Fashion数据集上性能优于基线，对训练未见过的分布外检索器有显著测试鲁棒性**
  _[Owen-Shapley Policy Optimization (OSPO): A Principled RL Algorith...](http://arxiv.org/abs/2601.08403)_


### 🔬 主动知识检索（1 篇）

- **以睡眠医学为代表案例，该框架在八项核心临床功能的多个评估指标上均优于现有方法。**
  _[Active Knowledge Retrieval to Reduce Hallucinations and Enhance F...](https://www.semanticscholar.org/paper/1a6fc7a561cc4dbbc771e14d0f3e527b6840bccb)_


### 🔬 RAG幻觉缓解（1 篇）

- **本文归纳出RAG系统的幻觉类型分类，构建了归因技术统一处理流程，给出技术选型实践指南**
  _[Attribution Techniques for Mitigating Hallucinated Information in...](http://arxiv.org/abs/2601.19927)_


### 🔬 可溯源文本生成（1 篇）

- **声明级接地可缓解传统接地方法对齐生成语句与上下文句级证据的局限，大幅提升接地质量和验证效率**
  _[eTracer: Towards Traceable Text Generation via Claim-Level Ground...](http://arxiv.org/abs/2601.03669)_


### 🔬 奖励建模（1 篇）

- **IRPM将n个候选的奖励评估复杂度降为O(n)，在三个基准取得点GRM最优，性能接近顶级成对GRM。**
  _[IRPM: Intergroup Relative Preference Modeling for Pointwise Gener...](http://arxiv.org/abs/2601.00677)_


### 🔬 大模型偏好微调（1 篇）

- **基于结构化修订的监督能实现更高效有效的偏好微调，性能优于标准A/B排序和全对比重写对齐方法**
  _[Fine-Tuning LLMs with Fine-Grained Human Feedback on Text Spans](http://arxiv.org/abs/2512.23693)_


### 🔬 电力大模型验证（1 篇）

- **CoVe增强模型安全摘要准确率达75.65%，分别超LoRA基线3.02%、基础大模型12.63%，T=0.4搭配质疑提示效果最佳**
  _[A Consistency-Oriented Verification Framework for Reliable Power ...](https://www.semanticscholar.org/paper/f675d35926709368d7b759d6227171732e2f82b6)_


### 🔬 参数高效模型引导（1 篇）

- **相同匹配训练设置下新词学习性能优于LoRA微调，模型被问及新词时偶尔会自行编造新词汇**
  _[Neologism Learning as a Parameter-Efficient Alternative to Fine-T...](http://arxiv.org/abs/2512.18551)_


### 🔬 多模态奖励评测（1 篇）

- **Gemini 3 Pro准确率达75-80%，人类准确率超90%，MMRB2性能与下游任务成功率强相关**
  _[Multimodal RewardBench 2: Evaluating Omni Reward Models for Inter...](http://arxiv.org/abs/2512.16899)_


### 🔬 奖励模型对齐（1 篇）

- **BT梯度范数包含预测误差和最终层输出表征距离两个分量，大距离对梯度的影响会掩盖小距离对的学习信号。**
  _[When Distance Distracts: Representation Distance Bias in BT-Loss ...](http://arxiv.org/abs/2512.06343)_


### 🔬 稠密奖励构建（1 篇）

- **设计不佳的稠密奖励会引发非预期行为与奖励黑客，现有方法需在通用性等三个核心维度间权衡。**
  _[Towards better dense rewards in Reinforcement Learning Applicatio...](http://arxiv.org/abs/2512.04302)_


### 🔬 大模型对齐（1 篇）

- **稳定秩在RewardBench达84.04%准确率，SR-GRPO无监督让Qwen2.5-1.5B STEM涨10%、数学推理涨19%**
  _[SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for Large L...](http://arxiv.org/abs/2512.02807)_


### 🔬 RLHF偏好对齐（1 篇）

- **将人类内在意图与外部因素导致的偏好翻转分为两个独立阶段，可利用标注特征建模偏好翻转模式**
  _[When Human Preferences Flip: An Instance-Dependent Robust Loss fo...](http://arxiv.org/abs/2512.00709)_


### 🔬 大语言模型排序（1 篇）

- **不同大语言模型排序方法之间存在明确权衡，各算法在多个评价维度上表现各有优劣**
  _[Ranking Large Language Models with Human Preferences: A Game-Theo...](https://www.semanticscholar.org/paper/aa1a9d6f5450439bef26ca8bad3c9673ececf8fd)_


### 🔬 神经反馈强化学习（1 篇）

- **预训练模型经少量被试特异性数据微调后，二分类F1提升17%，多分类提升41%，平均二分类F1达67%**
  _[Towards Reinforcement Learning from Neural Feedback: Mapping fNIR...](http://arxiv.org/abs/2511.12844)_


### 🔬 文本优化（1 篇）

- **在DOCKSTRING分子发现基准中，该方法识别出超26万化合物数据库99.9百分位的新型类药分子**
  _[Feedback Descent: Open-Ended Text Optimization via Pairwise Compa...](http://arxiv.org/abs/2511.07919)_


### 🔬 人类偏好学习（1 篇）

- **人类偏好反馈可按数据源与格式分类，现有研究可从建模、使用、评估三个维度梳理**
  _[A Survey on Human Preference Learning for Aligning Large Language...](https://www.semanticscholar.org/paper/e3a5da866598c0414dd186085ccd429ac8ea664e)_


### 🔬 推理奖励设计（1 篇）

- **PACR可加速大语言模型推理探索，用更少的推理轨迹达到奖励饱和，在多个基准测试上取得性能提升**
  _[PACR: Progressively Ascending Confidence Reward for LLM Reasoning](http://arxiv.org/abs/2510.22255)_


### 🔬 研究创意评估（1 篇）

- **ScholarEval对专家标注要点覆盖率显著高于所有基线，多项评估指标优于最强基线o4-mini-deep-research**
  _[ScholarEval: Research Idea Evaluation Grounded in Literature](http://arxiv.org/abs/2510.16234)_


### 🔬 思维链微调综述（1 篇）

- **基于六顶思考帽框架可从人类推理机制视角系统分类梳理思维链微调方法，还维护了跟踪领域进展的实时Github仓库**
  _[Putting on the Thinking Hats: A Survey on Chain of Thought Fine-t...](http://arxiv.org/abs/2510.13170)_


### 🔬 神经自适应聊天（1 篇）

- **600ms数据窗口下，道德凸显性单试次解码平均准确率78%，事实误差解码准确率66%，无法区分道德判断一致与否**
  _[Towards neuroadaptive chatbots: a feasibility study](https://www.semanticscholar.org/paper/155109edca1e893f9cfe3c00e81f62de2fbc6e64)_


### 🔬 大语言模型对齐（1 篇）

- **Rubric-RM在多个奖励建模基准上超越同规模强基线8.4%，性能增益可迁移到多个下游任务策略模型**
  _[OpenRubrics: Towards Scalable Synthetic Rubric Generation for Rew...](http://arxiv.org/abs/2510.07743)_


### 🔬 自对弈偏好优化（1 篇）

- **提示难度越低自对弈优化性能越好，仅选30%最简单提示训练即可提升性能，模型容量增大会缩小难易性能差距**
  _[Revisiting Self-Play Preference Optimization: On the Role of Prom...](http://arxiv.org/abs/2510.05534)_


### 🔬 未分类（25 篇）

- **分析发现幻觉主要源于文本先验，提出的方法可有效缓解幻觉且保留模型原有性能**
  _[When Prompts Override Vision: Prompt-Induced Hallucinations in LV...](http://arxiv.org/abs/2604.21911v1)_

- **发现大模型预测结果随实体表面形式改变而变化，指出评估非逐字记忆需考虑表面形式多样性**
  _[Revisiting Non-Verbatim Memorization in Large Language Models: Th...](http://arxiv.org/abs/2604.21882v1)_

- **该方法无需访问相机ISP，仅占180KB存储空间，可作为元数据存入标准图像格式**
  _[Addressing Image Authenticity When Cameras Use Generative AI](http://arxiv.org/abs/2604.21879v1)_

- **该框架无需公开测试用例，性能匹配SOTA方法，还可减少输出令牌的消耗**
  _[DryRUN: On the Role of Public Tests in LLM-Driven Code Generation](http://arxiv.org/abs/2604.21598v1)_

- **在六个跨领域多语言公开语料上，STRICT-F1较GPT-3.5基线大幅提升，大幅减少无效标签与幻觉跨度**
  _[Job Skill Extraction via LLM-Centric Multi-Module Framework](http://arxiv.org/abs/2604.21525v1)_

- **揭示当前评估型VLM存在大量评估盲点，可靠性不足，呼吁部署使用时需保持谨慎**
  _[Seeing Isn't Believing: Uncovering Blind Spots in Evaluator Visio...](http://arxiv.org/abs/2604.21523v1)_

- **明确表征是抽象视觉推理的核心瓶颈，证明符号输入可作为可控的诊断性能上界**
  _[Symbolic Grounding Reveals Representational Bottlenecks in Abstra...](http://arxiv.org/abs/2604.21346v1)_

- **对多款GPT模型做基准测试，明确性能差异，验证了评估流水线的有效性**
  _[Evaluating AI Meeting Summaries with a Reusable Cross-Domain Pipe...](http://arxiv.org/abs/2604.21345v1)_

- **得出LLM解码器公平性的多项结论，指出音频编码器设计是实现公平鲁棒语音识别的核心**
  _[Do LLM Decoders Listen Fairly? Benchmarking How Language Model Pr...](http://arxiv.org/abs/2604.21276v1)_

- **推出长时对话记忆评估基准EngramaBench，发现Engrama跨空间推理更优，揭示结构化记忆的系统性能矛盾**
  _[EngramaBench: Evaluating Long-Term Conversational Memory with Str...](http://arxiv.org/abs/2604.21229v1)_

- **从数学上证明所提方法的理论优势，大量实验验证了该方法的优越性**
  _[Align Generative Artificial Intelligence with Human Preferences: ...](http://arxiv.org/abs/2604.21209v1)_

- **有效提升下一职业预测精度，性能优于无监督方法可媲美全监督，验证精度依赖生成理由质量** 💻
  _[On Reasoning Behind Next Occupation Recommendation](http://arxiv.org/abs/2604.21204v1)_

- **多项性能指标提升5-20%，发布模块化实现，为构建可审计可信AI提供可扩展路径**
  _[Trust but Verify: Introducing DAVinCI -- A Framework for Dual Att...](http://arxiv.org/abs/2604.21193v1)_

- **发现当前与先前实体槽正交分离、功能各异，揭示激活可用信息与模型实际使用信息的差距**
  _[Slot Machines: How LLMs Keep Track of Multiple Entities](http://arxiv.org/abs/2604.21139v1)_

- **构建无VLM偏差的iPlotBench基准，框架提升问答准确率，可部署实现人机协作**
  _[Beyond Pixels: Introspective and Interactive Grounding for Visual...](http://arxiv.org/abs/2604.21134v1)_

- **发布CSTM-Bench基准数据集，完成跨会话威胁检测测量，提出有效算法与新评测指标。**
  _[Cross-Session Threats in AI Agents: Benchmark, Evaluation, and Al...](http://arxiv.org/abs/2604.21131v1)_

- **提升了摘要的语义相似度、保真度与事实一致性，是轻量通用的长领域文档可靠摘要方案**
  _[DWTSumm: Discrete Wavelet Transform for Document Summarization](http://arxiv.org/abs/2604.21070v1)_

- **提出策略多义与虚饰误导概念，揭示语言本身是塑造人工智能发展与治理的社会技术机制**
  _[Strategic Polysemy in AI Discourse: A Philosophical Analysis of L...](http://arxiv.org/abs/2604.21043v1)_

- **发布专家整理的图像与问答对数据集，验证结构化探究可提升诊断正确率、减少模型幻觉**
  _[Thinking Like a Botanist: Challenging Multimodal Language Models ...](http://arxiv.org/abs/2604.20983v1)_

- **4B参数V-tableR1在复杂表格基准上取得开源模型最优精度，性能超越更大模型与SFT基线**
  _[V-tableR1: Process-Supervised Multimodal Table Reasoning with Cri...](http://arxiv.org/abs/2604.20755v1)_

- **揭示主流全模态模型感知精度与乐理理解存在根本脱节，为诊断复杂规则领域推理缺陷提供框架**
  _[ONOTE: Benchmarking Omnimodal Notation Processing for Expert-leve...](http://arxiv.org/abs/2604.20719v1)_

- **为真值不确定场景下的机器学习系统开发提供了逻辑自洽可行的实现路径与原则性基础**
  _[LAF-Based Evaluation and UTTL-Based Learning Strategies with MIAT...](http://arxiv.org/abs/2604.20944v1)_

- **在UltraFeedback数据集实验显示，该方法尤其MGDA-Decoupled取得整体及单目标对黄金回复最高胜率**
  _[MGDA-Decoupled: Geometry-Aware Multi-Objective Optimisation for D...](http://arxiv.org/abs/2604.20685v1)_

- **多个实验中提升终身智能体性能，大幅降低检索开销，在多个测试任务取得优异结果**
  _[Ask Only When Needed: Proactive Retrieval from Memory and Skills ...](http://arxiv.org/abs/2604.20572v1)_

- **在多个基准测试验证，SToP应用到现有方法后，即便剪枝90%视觉token仍可显著提升性能。**
  _[Sink-Token-Aware Pruning for Fine-Grained Video Understanding in ...](http://arxiv.org/abs/2604.20937v1)_


---
*ArXiv_Daily_Digest 自动生成 | 2026-07-01*