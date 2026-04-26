# 表示工程与激活引导 — 2026-W17 (04/20-04/26)

本周新增 **62** 篇论文。4 篇附带代码仓库。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，考虑收紧 arxiv_query

## 分类分布

- `via-citation`: 42 篇
- `cs.CL`: 9 篇
- `cs.AI`: 4 篇
- `cs.LG`: 4 篇
- `cs.CR`: 2 篇
- `cs.CV`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Trust-SSL: Additive-Residual Selective Invariance for Robust...](http://arxiv.org/abs/2604.21349v1) | 在对齐目标中加入逐样本逐因子信任权重，结合基础对比损失作为加性残差，对信任权重应... | 在多个数据集上精度优于基线方法，退化和跨域测试性能提升明显，给出不确定性感知SS... | ✅ |
| 2 | [Value-Conflict Diagnostics Reveal Widespread Alignment Fakin...](http://arxiv.org/abs/2604.20995v1) | 提出基于价值冲突的VLAF诊断框架，利用对比引导向量实现轻量无标注对齐伪装缓解 | 发现对齐伪装比已有研究报告更普遍，所提方法可大幅降低对齐伪装发生率 | — |
| 3 | [Breaking Bad: Interpretability-Based Safety Audits of State-...](http://arxiv.org/abs/2604.20945v1) | 结合通用转向、表示工程两种可解释性方法，采用自适应两阶段网格搜索开展越狱审计。 | 对八个SOTA开源大模型完成审计，揭示不同模型的鲁棒性差异，验证可解释性转向是有... | — |
| 4 | [Tracing Relational Knowledge Recall in Large Language Models](http://arxiv.org/abs/2604.19934v2) | 系统评估源自注意力头和MLP的不同隐表示，对训练后的线性探针开展特征归因分析 | 发现单头注意力对残差流的贡献是线性关系分类的较强特征，揭示了探针准确率与多个关系... | — |
| 5 | [How Do Answer Tokens Read Reasoning Traces? Self-Reading Pat...](http://arxiv.org/abs/2604.19149v1) | 提出结合过程控制几何指标与内容监控语义指标计算SRQ分数，构建无训练推理引导方法 | 发现正确定量推理对应良性自阅读模式，所提方法实验中获得了一致的准确率提升 | — |
| 6 | [Local Linearity of LLMs Enables Activation Steering via Mode...](http://arxiv.org/abs/2604.19018v1) | 验证LLM层间动力学可局部线性近似，结合线性二次调节器设计闭环反馈激活控制器。 | 实现多模型多任务鲁棒细粒度行为控制，性能优于基线，给出跟踪误差理论保证。 | — |
| 7 | [Characterizing AlphaEarth Embedding Geometry for Agentic Env...](http://arxiv.org/abs/2604.18715v1) | 刻画Google AlphaEarth嵌入的流形几何，构建嵌入检索辅助的智能环境... | 揭示AlphaEarth嵌入为非欧流形，证明几何感知推理可提升复杂环境查询回答质... | — |
| 8 | [Latent Phase-Shift Rollback: Inference-Time Error Correction...](http://arxiv.org/abs/2604.18567v1) | 提出潜在相移回滚LPSR方法，监控残差流检测相位偏移，回滚KV缓存注入引导向量，... | 所提方法性能显著优于多个主流基线，发现了检测-校正解离的新现象 | — |
| 9 | [LLM Safety From Within: Detecting Harmful Content with Inter...](http://arxiv.org/abs/2604.18519v1) | 提出轻量防护模型SIREN，识别安全神经元，通过自适应层加权策略组合大语言模型内... | SIREN性能大幅优于现有最优开源防护模型，参数量更少，泛化能力与推理效率表现更... | — |
| 10 | [Characterizing Model-Native Skills](http://arxiv.org/abs/2604.17614v1) | 提出模型原生技能表征，从模型序列级激活恢复紧致正交基，支撑数据选择与推理干预 | 在推理后训练与安全对齐任务验证，效果优于人工表征方法，可支撑多阶段模型行为干预 | — |
| 11 | [Auditing Support Strategies in LLMs through Grounded Multi-T...](http://arxiv.org/abs/2604.17079v1) | 提出多轮模拟框架，采用SSBC编码模型响应，用线性探针估计模型感知的用户困扰程度 | 发现大模型支持策略随估计的用户困扰程度系统变化，揭示单轮评估无法发现的轨迹级动态 | — |
| 12 | [Surgical Repair of Insecure Code Generation in LLMs](http://arxiv.org/abs/2604.16697v1) | 先开展机理分析定位问题原因，采用按漏洞分类的引导向量降低不安全代码生成 | 证实方法最高减少74%不安全生成，开销可忽略，指出该问题是可解释性问题而非训练伪... | — |
| 13 | [RankGuide: Tensor-Rank-Guided Routing and Steering for Effic...](http://arxiv.org/abs/2604.16694v1) | 提出RankGuide框架，基于张量秩信号检测模型失效，调制小推理模型推理轨迹提... | 多个推理基准实验表明，相比大推理模型最高降1.75倍延迟，仍保持有竞争力的精度 | — |
| 14 | [Predicting Where Steering Vectors Succeed](http://arxiv.org/abs/2604.15557v1) | 提出分层诊断工具线性可访问性剖面LAP，利用模型未嵌入矩阵计算指标，无需训练即可... | 经多模型多概念验证预测相关性高，提出三机制框架，实体导向实验验证方法优于传统启发... | — |
| 15 | [FineSteer: A Unified Framework for Fine-Grained Inference-Ti...](http://arxiv.org/abs/2604.15488v1) | 提出FineSteer统一框架，将推理时引导拆分为SCS条件引导和MoSE向量合... | 在安全与真实性基准实验中优于现有最优方法，以极小效用损失获得更强引导性能 | — |
| 16 | [CausalDetox: Causal Head Selection and Intervention for Lang...](http://arxiv.org/abs/2604.14602v1) | 提出CausalDetox框架，利用PNS筛选致毒注意力头，通过两种互补策略实现... | 提出新基准PARATOX，该方法减毒效果更优，保留生成流畅度，头选择速度提升7倍 | — |
| 17 | [Mechanistic Decoding of Cognitive Constructs in Large Langua...](http://arxiv.org/abs/2604.14593v3) | 基于表示工程提出认知逆向工程框架，结合多种方法分离量化嫉妒的心理前因并检验因果效... | 证实多款大语言模型将嫉妒编码为目标因子的结构化线性组合，可为多智能体AI安全表征... | — |
| 18 | [Psychological Steering of Large Language Models](http://arxiv.org/abs/2604.14463v1) | 提出心理引导框架，利用心理产物校准残差流注入，在语义校准单位开展无界流畅约束扫描 | 证实均值差注入性能优于现有基线，混合方法性能更优，验证其符合线性表示假设，可提供... | — |
| 19 | [Purging the Gray Zone: Latent-Geometric Denoising for Precis...](http://arxiv.org/abs/2604.14324v1) | 提出GeoDe几何去噪框架，用线性探针构造真值超平面，以几何距离为置信信号过滤模... | 多模型多基准数据集实验表明，GeoDe显著提升模型真实性，在分布外场景泛化能力强... | ✅ |
| 20 | [Rhetorical Questions in LLM Representations: A Linear Probin...](http://arxiv.org/abs/2604.14128v2) | 在两个具有不同话语语境的社交媒体数据集上，使用线性探针分析大语言模型的修辞问句表... | 证实修辞信号可被稳定探测，发现修辞问句在LLM中由多个带不同线索的线性方向编码而... | — |
| 21 | [Separable Expert Architecture: Toward Privacy-Preserving LLM...](http://arxiv.org/abs/2604.21571) | 提出三层可分离专家架构，分离个人数据与共享权重，删除用户代理即可实现确定遗忘。 | 将机器遗忘从难解的权重编辑问题转为确定删除操作，兼顾个性化与隐私保障，可兼容DP... | — |
| 22 | [Mitigating Hallucinations in Large Vision-Language Models wi...](http://arxiv.org/abs/2604.20366) | 提出MPD双阶段框架，通过语义感知解耦提取纯幻觉组件，选择性更新与幻觉相关的参数... | 所提方法达到最优性能，可减少23.4%幻觉，保留97.4%生成能力，且无额外计算... | — |
| 23 | [LLMs Know They're Wrong and Agree Anyway: The Shared Sycopha...](http://arxiv.org/abs/2604.19117) | 针对不同规模开源大模型，采用静默注意力头、边级路径修补法分析内部回路 | 发现大语言模型中存在共享的谄媚-说谎回路，该回路控制顺从行为而非模型知识 | — |
| 24 | [Pause or Fabricate? Training Language Models for Grounded Re...](http://arxiv.org/abs/2604.19656) | 提出基于交互式强化学习的接地推理框架GRIL，分两阶段推理并设计惩罚幻觉的专属奖... | 实验表明GRIL显著提升前提检测能力，提高任务成功率，缩短响应长度，兼具鲁棒性与... | — |
| 25 | [Are LLM Uncertainty and Correctness Encoded by the Same Feat...](http://arxiv.org/abs/2604.19974) | 提出2×2分析框架划分预测，采用稀疏自编码器独立识别关联两个维度的特征 | 识别出三类功能不同的特征，证实抑制混杂特征可提准降熵，可用于选择性弃权提准确率 | — |
| 26 | [The Geometric Canary: Predicting Steerability and Detecting ...](http://arxiv.org/abs/2604.17698) | 利用表示成对距离结构的几何稳定性，分任务对齐监督与无监督两种方案 | 两类几何稳定性形成互补，分别服务预部署评估与后部署监测，性能优异 | — |
| 27 | [Where Fake Citations Are Made: Tracing Field-Level Hallucina...](http://arxiv.org/abs/2604.18880) | 对多模型生成的引用做统计分析，用弹性网正则化定位幻觉神经元，通过因果干预验证其作... | 识别出稀疏领域特异性幻觉神经元，验证其因果作用，提出仅用内部信号缓解引用幻觉的轻... | — |
| 28 | [Harmful Intent as a Geometrically Recoverable Feature of LLM...](http://arxiv.org/abs/2604.18901) | 对不同架构、不同对齐变体的大语言模型，采用六种方向寻找策略表征有害意图的几何特征 | 证实有害意图可从LLM残差流几何恢复，验证其跨模型跨数据集迁移性，提出安全检测评... | — |
| 29 | [ATLAS: Constitution-Conditioned Latent Geometry and Redistri...](http://arxiv.org/abs/2604.17663) | 提出几何优先的ATLAS框架，通过检测局部图表的切结构、占据分布与行为耦合追踪隐... | 验证了宪法诱导隐几何可跨模型、跨基质复现，实现了跨不同介质的隐结构重识别 | — |
| 30 | [Pruning Unsafe Tickets: A Resource-Efficient Framework for S...](http://arxiv.org/abs/2604.15780) | 提出资源高效的剪枝框架，采用无梯度归因机制识别移除与不安全行为相关的参数 | 提供轻量事后对齐策略，可减少不安全生成、提升越狱攻击鲁棒性，且模型效用损失极小 | — |
| 31 | [Learning Uncertainty from Sequential Internal Dispersion in ...](http://arxiv.org/abs/2604.15741) | 提出SIVR监督幻觉检测框架，利用逐token逐层隐藏状态特征，聚合全序列方差特... | 所提方法性能优于强基线，泛化能力强，无需依赖大规模训练集，具备实际部署潜力 | ✅ |
| 32 | [Hallucination as Trajectory Commitment: Causal Evidence for ...](http://arxiv.org/abs/2604.15400) | 采用同提示分岔、激活修补、窗口修补、探针探测与无监督聚类展开因果分析。 | 为自回归语言模型幻觉是受非对称吸引子动力学支配的早期轨迹承诺提供了因果证据。 | — |
| 33 | [How Do LLMs and VLMs Understand Viewpoint Rotation Without V...](http://arxiv.org/abs/2604.15294) | 提出文本视角旋转理解数据集，开展逐层探针分析与头级因果干预，选择性微调关键注意力... | 揭示模型视角旋转理解缺陷的内在机制，验证选择性微调可提效且避免通用能力遗忘 | — |
| 34 | [From Weights to Activations: Is Steering the Next Frontier o...](http://arxiv.org/abs/2604.14090) | 引入一套模型适配方法的功能评判标准，用该标准对比引导方法与经典适配方法 | 论证引导是独特的模型适配范式，厘清其与现有方法的关系，推动建立模型适配统一分类 | — |
| 35 | [The cognitive companion: a lightweight parallel monitoring a...](http://arxiv.org/abs/2604.13759) | 提出轻量并行监控架构Cognitive Companion，包含基于大模型和零开... | 验证所提架构的可行性，得到不同任务类型与模型规模下架构效果的实证结论 | — |
| 36 | [Awakening Dormant Experts:Counterfactual Routing to Mitigate...](http://arxiv.org/abs/2604.14246) | 提出无训练推理框架反事实路由（CoR），结合扰动分析与CEI指标动态调度计算资源... | 不增加推理预算，在多个数据集上平均提升事实准确率3.1%，获得更优帕累托前沿。 | — |
| 37 | [Geometric Routing Enables Causal Expert Control in Mixture o...](http://arxiv.org/abs/2604.14434) | 采用低维度量空间余弦相似路由，结合语义投影、梯度分析与因果干预验证专家特性 | 证明几何路由下混合专家具备架构上单义性，可因果验证，推理时可零开销控制 | — |
| 38 | [Preventing Safety Drift in Large Language Models via Coupled...](http://arxiv.org/abs/2604.12384) | 提出耦合权重与激活约束CWAC，同时约束权重更新的安全子空间，并正则化安全关键特... | 多模型多下游任务实验验证，CWAC有害得分低，对微调精度影响小，性能优于强基线。 | — |
| 39 | [Reducing Hallucination in Enterprise AI Workflows via Hybrid...](http://arxiv.org/abs/2604.11141) | 将幻觉缓解建模为最小贝叶斯风险问题，提出融合语义嵌入相似度与词汇精度的HUMBR... | 经公开基准与Meta真实生产数据验证，效果优于标准通用自一致性，大幅降低了幻觉相... | — |
| 40 | [Verbalizing LLMs' Assumptions About the User to Calibrate Ex...](https://www.semanticscholar.org/paper/71215b1da630dc25040fb0e73ebde99e13da321e) | 提出口头化假设框架，揭示大语言模型的隐含假设，通过探针引导调整输出降低模型谄媚 | 通过三个案例验证框架效用，揭示期望错位，证实该框架可有效降低大语言模型的谄媚问题 | — |
| 41 | [SinkTrack: Attention Sink based Context Anchoring for Large ...](http://arxiv.org/abs/2604.10027) | 提出无需训练即插即用的SinkTrack方法，以首个注意力汇为锚注入关键上下文特... | 该方法推理开销可忽略，在文本、多模态任务均获性能提升，具备良好鲁棒性与泛化性 | ✅ |
| 42 | [Cognitive Pivot Points and Visual Anchoring: Unveiling and R...](http://arxiv.org/abs/2604.10219) | 提出轻量V-STAR训练范式，结合HVAR与FRM机制，强化视觉语义锚定缓解幻觉 | 识别出推理视觉事实脱节新现象，提出针对性方法，可有效缓解多模态推理幻觉 | — |
| 43 | [Arbitration Failure, Not Perceptual Blindness: How Vision-La...](http://arxiv.org/abs/2604.09364) | 采用多模态仲裁交叉分析、逐层Logit Lens探针、激活修补与无训练激活引导开... | 揭示编码-接地解离现象，明确VLM错误源于仲裁而非感知，提出可提升视觉接地的干预... | — |
| 44 | [SHIFT: Steering Hidden Intermediates in Flow Transformers](http://arxiv.org/abs/2604.09213) | 提出轻量框架SHIFT，受大语言模型激活引导启发，推理时操纵中间激活应用学习的转... | 可灵活实现概念移除、风格迁移、目标修改，无需耗时重训练，可有效控制DiT生成过程 | — |
| 45 | [Activation Steering for Aligned Open-ended Generation withou...](http://arxiv.org/abs/2604.08169) | 提出激活引导这一轻量运行时防御，在生成全过程修正错位激活，设计三种不同引导方法 | 验证所有方法可保留生成连贯性同时恢复目标性状，新提出的两种方法性能更优 | — |
| 46 | [Multilingual Embedding Probes Fail to Generalize Across Lear...](http://arxiv.org/abs/2604.07095) | 训练多种线性、非线性探针，基于Qwen3-Embedding隐藏状态预测，开展分... | 揭示探针仅学到语料特有属性，证明当前多语言嵌入未直接编码通用语言能力 | — |
| 47 | [ART: Attention Replacement Technique to Improve Factuality i...](http://arxiv.org/abs/2604.06393) | 提出无需训练的注意力替换技术ART，将大模型浅层均匀注意力替换为局部注意力。 | 在多种大语言模型架构上显著减少幻觉，证明该方法无需微调也有效且可推广。 | — |
| 48 | [Confidence Should Be Calibrated More Than One Turn Deep](http://arxiv.org/abs/2604.05397) | 提出多轮置信校准任务，设计ECE@T指标，提出MTCal方法与ConfChat解... | 验证所提方法性能优异，指出多轮校准是大语言模型安全可靠落地的关键缺失环节。 | — |
| 49 | [LatentAudit: Real-Time White-Box Faithfulness Monitoring for...](http://arxiv.org/abs/2604.05358) | 提出白盒审计工具LatentAudit，利用生成模型残差流激活计算马氏距离度量回... | 实现RAG回答保真度实时监控，支持可验证部署，在多个基准测试中表现优异。 | — |
| 50 | [How LLMs Follow Instructions: Skillful Coordination, Not a U...](http://arxiv.org/abs/2604.06015) | 对三个指令微调模型的九个不同任务开展诊断性探测，结合交叉任务分析、因果消融与时序... | 提供了反对指令遵循依赖通用机制的汇聚证据，明确了指令遵循的本质特征 | — |
| 51 | [Weakly Supervised Distillation of Hallucination Signals into...](http://arxiv.org/abs/2604.06277) | 结合三种互补接地信号做弱监督标注，将幻觉信号蒸馏进Transformer表示，训... | 构建万余例带标注的数据集，验证了内部幻觉检测的可行性，测试了检测的推理开销 | — |
| 52 | [Memory Dial: A Training Framework for Controllable Memorizat...](http://arxiv.org/abs/2604.05074) | 提出Memory Dial训练框架，通过单参数α插值两种损失目标，实现对记忆压力... | 构建了可控的语言模型记忆研究实验框架，验证了框架的有效性，为相关研究提供支撑。 | — |
| 53 | [HalluSAE: Detecting Hallucinations in Large Language Models ...](http://arxiv.org/abs/2604.16430) | 提出相变启发的HalluSAE框架，将幻觉建模为潜动力学偏移，分三阶段完成幻觉检... | 提出了HalluSAE检测框架，在Gemma-2-9B上实验取得了当前最优的幻觉... | — |
| 54 | [Extracting and Steering Emotion Representations in Small Lan...](http://arxiv.org/abs/2604.04064) | 对5种架构共9个小语言模型，采用两种提取方法对比分析，结合操控实验验证因果效应。 | 给出开放权重小模型情绪研究的方法指南，打通外部行为与内部表征分析的研究链路。 | — |
| 55 | [Where to Steer: Input-Dependent Layer Selection for Steering...](http://arxiv.org/abs/2604.03867) | 提出W2S框架，通过学习输入嵌入到最优引导层的映射，依据输入自适应选择干预层。 | W2S在多模型多对齐任务的分布内外设置中均优于固定层基线，证明输入依赖控制的重要... | — |
| 56 | [Testing the Limits of Truth Directions in LLMs](http://arxiv.org/abs/2604.03754) | 从模型层、任务属性、提示指令多个维度，检验分析大语言模型中真理方向的特性 | 指出大语言模型真理方向的通用性比原有认知更有限，发现多个未被关注的影响因素 | — |
| 57 | [EnsemHalDet: Robust VLM Hallucination Detection via Ensemble...](http://arxiv.org/abs/2604.02784) | 提出EnsemHalDet集成框架，为VLM多种内部表示训练独立检测器，通过集成... | 经多个VQA数据集和VLM实验验证，该方法AUC性能优于现有方法与单检测器模型，... | — |
| 58 | [Steerable but Not Decodable: Function Vectors Operate Beyond...](http://arxiv.org/abs/2604.02608) | 开展涵盖12个任务、3模型家族共6个模型的大样本跨模板功能向量迁移实验 | 揭示功能向量可引导但不可解码的普遍现象，明确了其作用层位置与编码特性 | — |
| 59 | [Verbalizing LLMs'assumptions to explain and control sycophan...](http://arxiv.org/abs/2604.03058) | 提出言语化假设框架提取大语言模型的隐含假设，使用线性假设探针调控迎合行为。 | 揭示大语言模型阿谀迎合行为的产生机制，提出可实现该行为可解释细粒度调控的新方法。 | — |
| 60 | [Reliable Control-Point Selection for Steering Reasoning in L...](http://arxiv.org/abs/2604.02113) | 提出稳定性过滤保留可稳定复现目标行为的边界，结合内容子空间投影去除问题特有噪声 | 在MATH-500准确率达0.784，较最优基线提升5个百分点，所得转向向量可跨... | — |
| 61 | [Attention at Rest Stays at Rest: Breaking Visual Inertia for...](http://arxiv.org/abs/2604.01989) | 提出无需训练的惯性感知视觉激发（IVE）方法，区分惯性token并引入惩罚打破注... | 所提IVE方法在多种基础MLLM和多个幻觉基准上，均能有效缓解认知幻觉 | — |
| 62 | [Aligning Recommendations with User Popularity Preferences](http://arxiv.org/abs/2604.01036) | 引入流行度分位数校准框架度量对齐偏差，提出基于激活引导的SPREE个性化推理去偏... | 实验验证SPREE在保持原有推荐质量的前提下，能够稳定提升用户层面的流行度对齐效... | — |

## 常见基线方法

- **SimCLR** (1 篇引用)
- **VICReg** (1 篇引用)
- **通用转向（US）** (1 篇引用)
- **表示工程（RepE）** (1 篇引用)
- **现有激活引导方法** (1 篇引用)
- **仅参数化方法** (1 篇引用)
- **随机基线** (1 篇引用)
- **标准自回归AR** (1 篇引用)
- **提示式自校正** (1 篇引用)
- **Best-of-16** (1 篇引用)

## 本周提到的 Limitations

- 该可解释性审计方法存在双重用途风险，当前大语言模型部署仍缺乏足够的内部防御。
- 均值差诱导的OCEAN特征协变模式偏离大二模型，学习得到的表示与人类心理存在差距
- 紧凑精确补丁的充分性不成立，邻近目标局部信号可不存在源忠实闭合
- 本研究仅为可行性研究而非确定性验证，1B-1.5B规模小模型上未取得效果提升
- 文中提出的无训练激活引导方法，在部分实验设置中会出现性能下降的问题
- 现有探测模型无法跨不同学习者语料泛化，当前多语言嵌入缺乏通用能力表征

## 常用数据集

- **MATH-500** (2 篇使用)
- **TriviaQA** (2 篇使用)
- **TruthfulQA** (2 篇使用)
- **EuroSAT** (1 篇使用)
- **AID** (1 篇使用)
- **NWPU-RESISC45** (1 篇使用)
- **BDD100K** (1 篇使用)
- **整理后的有害查询集合** (1 篇使用)
- **美国大陆2017-2023年1210万地球观测样本** (1 篇使用)
- **120组分三个复杂度层级的环境查询样本** (1 篇使用)


---

*自动生成于 2026-04-26 | Research Radar*