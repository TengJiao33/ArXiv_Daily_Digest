# LLM 真值性与事实性 — 2026-W17 (04/20-04/26)

本周新增 **163** 篇论文。7 篇附带代码仓库。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，考虑收紧 arxiv_query

## 分类分布

- `via-citation`: 130 篇
- `cs.CL`: 10 篇
- `cs.AI`: 6 篇
- `cs.CV`: 5 篇
- `cs.LG`: 4 篇
- `cs.GT`: 1 篇
- `cond-mat.mtrl-sci`: 1 篇
- `cs.SE`: 1 篇
- `cs.CR`: 1 篇
- `cs.CY`: 1 篇
- `cs.SD`: 1 篇
- `physics.flu-dyn`: 1 篇
- `cs.IR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [When Prompts Override Vision: Prompt-Induced Hallucinations ...](http://arxiv.org/abs/2604.21911v1) | 提出HalluScope基准分析幻觉成因，提出HalluVL-DPO偏好优化框架... | 分析发现幻觉主要源于文本先验，提出的方法可有效缓解幻觉且保留模型原有性能 | — |
| 2 | [Revisiting Non-Verbatim Memorization in Large Language Model...](http://arxiv.org/abs/2604.21882v1) | 引入整合维基重定向信息的RedirectQA实体QA数据集，测试13个大语言模型... | 发现大模型预测结果随实体表面形式改变而变化，指出评估非逐字记忆需考虑表面形式多样... | — |
| 3 | [Addressing Image Authenticity When Cameras Use Generative AI](http://arxiv.org/abs/2604.21879v1) | 优化图像专属多层感知器解码器与模态专属编码器，拍摄后恢复添加幻觉前的原始图像 | 该方法无需访问相机ISP，仅占180KB存储空间，可作为元数据存入标准图像格式 | — |
| 4 | [SyMTRS: Benchmark Multi-Task Synthetic Dataset for Depth, Do...](http://arxiv.org/abs/2604.21801v1) | 通过高保真城市模拟流程生成大规模合成数据集SyMTRS，构建统一多任务基准 | 数据集提供多类高质量标注，支持多任务联合研究，填补了遥感研究的关键缺口 | ✅ |
| 5 | [Compliance Moral Hazard and the Backfiring Mandate](http://arxiv.org/abs/2604.21789v1) | 以银行网络反洗钱为背景，构建去中心化风险分析机制设计框架，提出时序价值分配（TV... | 证明TVA可实现诚实报告均衡，指出设计不当的强制要求会降低福利，模拟显示其福利优... | — |
| 6 | [Neural surrogates for crystal growth dynamics with variable ...](http://arxiv.org/abs/2604.21753v1) | 开发两种卷积循环神经网络替代模型，分别以隐式、显式方式处理过饱和度并对比测试 | 证实显式过饱和度条件建模效果更优，模型可扩展，明确了两种方法的优劣 | — |
| 7 | [DryRUN: On the Role of Public Tests in LLM-Driven Code Gener...](http://arxiv.org/abs/2604.21598v1) | 提出DryRUN框架，支持大模型自主生成输入、模拟执行、迭代自校正，无需真值测试... | 该框架无需公开测试用例，性能匹配SOTA方法，还可减少输出令牌的消耗 | — |
| 8 | [Job Skill Extraction via LLM-Centric Multi-Module Framework](http://arxiv.org/abs/2604.21525v1) | 提出以大语言模型为中心的SRICL框架，结合语义检索、上下文学习、监督微调与确定... | 在六个跨领域多语言公开语料上，STRICT-F1较GPT-3.5基线大幅提升，大... | — |
| 9 | [Seeing Isn't Believing: Uncovering Blind Spots in Evaluator ...](http://arxiv.org/abs/2604.21523v1) | 引入关键错误维度的针对性扰动，构建测试基准，对多个主流VLM评估器开展可靠性测试 | 揭示当前评估型VLM存在大量评估盲点，可靠性不足，呼吁部署使用时需保持谨慎 | — |
| 10 | [Preferences of a Voice-First Nation: Large-Scale Pairwise Ev...](http://arxiv.org/abs/2604.21481v1) | 提出结合语言控制与感知基础标注的受控多维度成对评估框架，结合Bradley-Te... | 构建多语言TTS排行榜，分析人类偏好、排行榜可靠性以及模型在感知维度的优劣权衡 | — |
| 11 | [Symbolic Grounding Reveals Representational Bottlenecks in A...](http://arxiv.org/abs/2604.21346v1) | 以符号输入作为诊断探针，采用C-G范式重构任务为符号推理任务，对比不同模型性能 | 明确表征是抽象视觉推理的核心瓶颈，证明符号输入可作为可控的诊断性能上界 | — |
| 12 | [Evaluating AI Meeting Summaries with a Reusable Cross-Domain...](http://arxiv.org/abs/2604.21345v1) | 构建分为五个阶段的可复用跨领域评估流水线，用于AI会议摘要的标准化评估 | 对多款GPT模型做基准测试，明确性能差异，验证了评估流水线的有效性 | — |
| 13 | [Do LLM Decoders Listen Fairly? Benchmarking How Language Mod...](http://arxiv.org/abs/2604.21276v1) | 对三代不同架构共九个模型，在多个声学条件下从多人口维度评估语音识别公平性 | 得出LLM解码器公平性的多项结论，指出音频编码器设计是实现公平鲁棒语音识别的核心 | — |
| 14 | [EngramaBench: Evaluating Long-Term Conversational Memory wit...](http://arxiv.org/abs/2604.21229v1) | 构建长时对话记忆基准EngramaBench，提出图结构记忆系统Engrama，... | 推出长时对话记忆评估基准EngramaBench，发现Engrama跨空间推理更... | — |
| 15 | [Align Generative Artificial Intelligence with Human Preferen...](http://arxiv.org/abs/2604.21209v1) | 提出面向在线评论回复的新型大模型偏好微调法，融合多项针对性改进策略 | 从数学上证明所提方法的理论优势，大量实验验证了该方法的优越性 | — |
| 16 | [On Reasoning Behind Next Occupation Recommendation](http://arxiv.org/abs/2604.21204v1) | 以大语言模型为法官生成高质量标注理由，用该理由微调小模型完成推理与下一职业预测 | 有效提升下一职业预测精度，性能优于无监督方法可媲美全监督，验证精度依赖生成理由质... | ✅ |
| 17 | [Trust but Verify: Introducing DAVinCI -- A Framework for Dua...](http://arxiv.org/abs/2604.21193v1) | 提出DAVinCI双归属验证框架，分两步完成声明归属与验证，结合蕴含推理与置信度... | 多项性能指标提升5-20%，发布模块化实现，为构建可审计可信AI提供可扩展路径 | — |
| 18 | [Slot Machines: How LLMs Keep Track of Multiple Entities](http://arxiv.org/abs/2604.21139v1) | 提出多槽探测方法，分解单个token残差流激活分离当前与先前实体信息，分析两类槽... | 发现当前与先前实体槽正交分离、功能各异，揭示激活可用信息与模型实际使用信息的差距 | — |
| 19 | [Beyond Pixels: Introspective and Interactive Grounding for V...](http://arxiv.org/abs/2604.21134v1) | 提出内省交互式视觉定位IVG框架，结合规范内省与视图交互解决图表解读歧义 | 构建无VLM偏差的iPlotBench基准，框架提升问答准确率，可部署实现人机协... | — |
| 20 | [Cross-Session Threats in AI Agents: Benchmark, Evaluation, a...](http://arxiv.org/abs/2604.21131v1) | 构建跨会话攻击基准数据集，设计检测测量框架，提出带界记忆检测算法与融合评测指标。 | 发布CSTM-Bench基准数据集，完成跨会话威胁检测测量，提出有效算法与新评测... | — |
| 21 | [DWTSumm: Discrete Wavelet Transform for Document Summarizati...](http://arxiv.org/abs/2604.21070v1) | 提出基于离散小波变换的多分辨率框架，分解文本得到紧凑语义表示，可生成或指导大语言... | 提升了摘要的语义相似度、保真度与事实一致性，是轻量通用的长领域文档可靠摘要方案 | — |
| 22 | [Strategic Polysemy in AI Discourse: A Philosophical Analysis...](http://arxiv.org/abs/2604.21043v1) | 引入"虚饰误导（glosslighting）"概念，分析AI话语中策略多义现象的... | 提出策略多义与虚饰误导概念，揭示语言本身是塑造人工智能发展与治理的社会技术机制 | — |
| 23 | [Thinking Like a Botanist: Challenging Multimodal Language Mo...](http://arxiv.org/abs/2604.20983v1) | 提出探究链框架建模诊断轨迹，引入PlantInquiryVQA基准研究植物诊断的... | 发布专家整理的图像与问答对数据集，验证结构化探究可提升诊断正确率、减少模型幻觉 | — |
| 24 | [V-tableR1: Process-Supervised Multimodal Table Reasoning wit...](http://arxiv.org/abs/2604.20755v1) | 提出过程监督的V-tableR1框架，用专用评论VLM提供步骤反馈，结合新型PG... | 4B参数V-tableR1在复杂表格基准上取得开源模型最优精度，性能超越更大模型... | — |
| 25 | [ONOTE: Benchmarking Omnimodal Notation Processing for Expert...](http://arxiv.org/abs/2604.20719v1) | 提出ONOTE多格式基准，采用基于标准音高投影的确定性流水线消除不同记谱系统的主... | 揭示主流全模态模型感知精度与乐理理解存在根本脱节，为诊断复杂规则领域推理缺陷提供... | — |
| 26 | [Participatory provenance as representational auditing for AI...](http://arxiv.org/abs/2604.20711v1) | 提出基于最优传输理论、因果推断与语义分析的参与式来源测量框架，跟踪AI摘要过程中... | 实证发现官方咨询摘要代表性低于随机基线，异议群体被高比例排除，开发了开源交互式审... | — |
| 27 | [LAF-Based Evaluation and UTTL-Based Learning Strategies with...](http://arxiv.org/abs/2604.20944v1) | 在EL-MIATTs框架下开发两类互补机制，即基于LAF的评估算法与基于UTTL... | 为真值不确定场景下的机器学习系统开发提供了逻辑自洽可行的实现路径与原则性基础 | — |
| 28 | [MGDA-Decoupled: Geometry-Aware Multi-Objective Optimisation ...](http://arxiv.org/abs/2604.20685v1) | 提出基于几何的多目标优化算法MGDA-Decoupled，完全在轻量DPO范式下... | 在UltraFeedback数据集实验显示，该方法尤其MGDA-Decouple... | — |
| 29 | [Ask Only When Needed: Proactive Retrieval from Memory and Sk...](http://arxiv.org/abs/2604.20572v1) | 提出ProactAgent主动检索框架，通过ExpOnEvo实现持续改进，Pro... | 多个实验中提升终身智能体性能，大幅降低检索开销，在多个测试任务取得优异结果 | — |
| 30 | [Sink-Token-Aware Pruning for Fine-Grained Video Understandin...](http://arxiv.org/abs/2604.20937v1) | 提出感知汇点标记的剪枝方法SToP，引入汇点得分量化汇点倾向，结合现有剪枝抑制无... | 在多个基准测试验证，SToP应用到现有方法后，即便剪枝90%视觉token仍可显... | — |
| 31 | [AI models of unstable flow exhibit hallucination](http://arxiv.org/abs/2604.20372v1) | 结合傅里叶神经算子与深度算子网络，提出DeepFingers框架实现全空间频谱均... | 首次获得不稳定流动AI模型存在幻觉的系统证据，提出的DeepFingers可准确... | — |
| 32 | [Unsupervised Learning of Inter-Object Relationships via Grou...](http://arxiv.org/abs/2604.20925v1) | 提出基于群操作层次关系的无监督表示学习，引入群同态作为神经网络结构约束 | 助力理解婴儿内化环境规律的过程，为构建发育智能人工系统提供新视角 | — |
| 33 | [SAKE: Self-aware Knowledge Exploitation-Exploration for Grou...](http://arxiv.org/abs/2604.20146v1) | 提出端到端SAKE框架，通过两阶段训练协调内外部知识，实现自感知自适应工具调用 | 提出协调内外部知识的SAKE框架，在两个社交媒体基准上验证了方法的有效性 | — |
| 34 | [There Will Be a Scientific Theory of Deep Learning](http://arxiv.org/abs/2604.21691) | 整合梳理现有深度学习理论研究脉络，归纳研究共有特征，提出新的理论研究视角 | 论证深度学习科学理论正在形成，提出该理论可称为学习力学，理清了它与其他研究视角的... | — |
| 35 | [Rethinking Intrinsic Dimension Estimation in Neural Represen...](http://arxiv.org/abs/2604.20276) | 从理论与实证两个层面分析常用估计器的偏差，探究已有相关结果的潜在驱动因素 | 揭示了神经表征内在维度估计理论与实践的关键差异，提出该领域估计研究的新视角 | — |
| 36 | [LLMs Know They're Wrong and Agree Anyway: The Shared Sycopha...](http://arxiv.org/abs/2604.19117) | 对多类不同规模开源大模型，开展注意力头沉默抑制、边级路径修补实验验证 | 证实大语言模型中存在同时驱动逢迎附和、各类说谎行为的共享注意力头回路 | — |
| 37 | [Local Linearity of LLMs Enables Activation Steering via Mode...](http://arxiv.org/abs/2604.19018) | 利用大语言模型层动力学局部线性，将推理建模为线性时变系统，用线性二次调节器设计闭... | 给出了引导性能的理论保证，在多模型多任务实现细粒度行为控制，效果超过现有基线方法... | — |
| 38 | [LLM Safety From Within: Detecting Harmful Content with Inter...](http://arxiv.org/abs/2604.18519) | 提出轻量防护模型SIREN，识别安全神经元，自适应加权结合LLM内部特征，无需修... | 所提SIREN性能优于SOTA开源防护模型，参数量少250倍，泛化性好，检测效率... | — |
| 39 | [Exploring Concreteness Through a Figurative Lens](http://arxiv.org/abs/2604.18296) | 对四个大语言模型族的隐藏表示开展分层几何分析，探究同一名词不同用法的区分逻辑 | 发现大语言模型中具体性组织的几何结构，验证其可用于比喻分类与无训练生成引导 | — |
| 40 | [Where Fake Citations Are Made: Tracing Field-Level Hallucina...](http://arxiv.org/abs/2604.18880) | 对多模型生成引用开展统计分析，结合弹性网正则化定位幻觉神经元，通过因果干预验证其... | 识别出稀疏的领域特异性幻觉神经元，证实干预可提升性能，提出轻量化引用幻觉缓解方案 | — |
| 41 | [Harmful Intent as a Geometrically Recoverable Feature of LLM...](http://arxiv.org/abs/2604.18901) | 采用六种方向寻找策略，在多架构多对齐变体大模型上分析有害意图的几何特征 | 证明有害意图可从大模型残差流几何恢复，验证检测方法跨模型跨数据集迁移性良好 | — |
| 42 | [The Consensus Trap: Rescuing Multi-Agent LLMs from Adversari...](http://arxiv.org/abs/2604.17139) | 提出令牌级轮询协作法，让智能体在共享自回归上下文内交错生成，将其形式化为离散时间... | 揭示现有多智能体系统的结构性漏洞，理论证明所提方法鲁棒性，实验验证其效果优于多数... | — |
| 43 | [Learning Uncertainty from Sequential Internal Dispersion in ...](http://arxiv.org/abs/2604.15741) | 提出SIVR监督幻觉检测框架，利用逐token、逐层隐状态特征聚合全序列方差特征 | 所提方法性能优于强基线，泛化性强不依赖大规模训练集，适合实际部署应用 | ✅ |
| 44 | [Rhetorical Questions in LLM Representations: A Linear Probin...](http://arxiv.org/abs/2604.14128) | 在两个不同话语语境的社交媒体数据集上，运用线性探针分析大语言模型的修辞问句表征 | 揭示大语言模型对修辞问句的编码特征，指出其由多个侧重不同线索的线性方向编码而非单... | — |
| 45 | [From Weights to Activations: Is Steering the Next Frontier o...](http://arxiv.org/abs/2604.14090) | 引入一套适用于模型适配方法的功能评价标准，用其对比激活引导与经典适配方法 | 明确激活引导的模型适配属性，定位其独特范式，推动构建统一的模型适配分类体系 | — |
| 46 | [Latent Planning Emerges with Scale](http://arxiv.org/abs/2604.12493) | 定义大语言模型潜在规划，在两类任务上测试不同规模的Qwen-3系列模型。 | 提出测量大语言模型规划能力的框架，给出规划能力随规模增长的机制性证据。 | — |
| 47 | [The Linear Centroids Hypothesis: How Deep Network Features R...](http://arxiv.org/abs/2604.11962) | 提出线性质心假设LCH新框架，认为特征对应质心的线性方向，可复用现有LRH工具作... | 提出新的深度网络特征识别框架LCH，得到性能更优的稀疏特征字典，还可识别大模型电... | ✅ |
| 48 | [Cognitive Pivot Points and Visual Anchoring: Unveiling and R...](http://arxiv.org/abs/2604.10219) | 提出轻量V-STAR训练范式，结合HVAR与FRM将推理锚定回视觉输入缓解幻觉 | 识别出RVTD现象，提出针对性训练机制，赋予模型内在幻觉缓解能力 | — |
| 49 | [What do your logits know? (The answer may surprise you!)](http://arxiv.org/abs/2604.09885) | 以视觉语言模型为测试平台，系统比较不同表征层级压缩瓶颈的信息保留情况 | 首次对不同表征层级经两种自然瓶颈压缩后的信息保留情况做系统比较 | — |
| 50 | [Multilingual Embedding Probes Fail to Generalize Across Lear...](http://arxiv.org/abs/2604.07095) | 基于不同规模Qwen3-Embedding隐藏状态训练探针，开展分布内与跨语料性... | 证实当前多语言嵌入未编码通用可迁移语言能力，揭示现有探针无法跨语料泛化 | — |
| 51 | [From Hallucination to Scheming: A Unified Taxonomy and Bench...](http://arxiv.org/abs/2604.04788) | 提出沿三个互补维度构建统一分类法，将该分类框架应用于现有基准展开分析 | 提出大语言模型欺骗统一分类，给出领域发展建议与未来研究定位的报告模板 | — |
| 52 | [HalluSAE: Detecting Hallucinations in Large Language Models ...](http://arxiv.org/abs/2604.16430) | 提出受相变启发的HalluSAE框架，分三个阶段结合稀疏自编码器检测幻觉 | 在Gemma-2-9B上开展大量实验，所提方法达到了当前最优的幻觉检测性能 | — |
| 53 | [Testing the Limits of Truth Directions in LLMs](http://arxiv.org/abs/2604.03754) | 从模型不同层、不同任务与不同指令多个维度，探究分析大语言模型真值方向的特性 | 揭示了大语言模型真值方向通用性存在多方面限制，修正了以往对该问题的认知 | — |
| 54 | [LangFIR: Discovering Sparse Language-Specific Features from ...](http://arxiv.org/abs/2604.03532) | 提出LangFIR方法，仅用少量单语数据和随机token序列筛选出稀疏语言特异性... | 得到的稀疏语言特征选择性高且具因果重要性，用于语言控制在多模型多语言上取得最优性... | — |
| 55 | [EnsemHalDet: Robust VLM Hallucination Detection via Ensemble...](http://arxiv.org/abs/2604.02784) | 提出EnsemHalDet集成检测框架，为VLM多种内部表征训练独立检测器，通过... | 在多个VQA数据集和VLM上验证，该方法AUC性能优于现有方法与单检测器，提升了... | — |
| 56 | [Steerable but Not Decodable: Function Vectors Operate Beyond...](http://arxiv.org/abs/2604.02608) | 开展涵盖12项任务、6款多家族模型的跨模板功能向量迁移研究，结合投影、激活补丁分... | 发现功能向量存在可引导却不可解码的分离现象，阐明其编码性质与作用层级差异 | — |
| 57 | [Detecting Multi-Agent Collusion Through Multi-Agent Interpre...](http://arxiv.org/abs/2604.01151) | 提出NARCBench合谋检测基准，设计五种聚合单智能体欺骗评分的探针技术实现群... | 推出合谋检测基准与探针方法，零样本迁移场景仍有不错检测效果，推动多智能体可解释性... | ✅ |
| 58 | [Fast and Accurate Probing of In-Training LLMs'Downstream Per...](http://arxiv.org/abs/2604.01025) | 提出新的训练中评估范式，使用轻量探针基于模型检查点内部表示预测下游性能 | 所提方法可准确预测性能，泛化性良好，大幅降低评估延迟，赋能高效大模型开发 | — |
| 59 | [When Reward Hacking Rebounds: Understanding and Mitigating I...](http://arxiv.org/abs/2604.01476) | 借助表示工程提取概念方向，提出将捷径概念分数融入GRPO优势计算的优势修正方法 | 系统研究奖励黑客现象，提出的优势修正方法相比激活引导能更鲁棒抑制奖励黑客 | — |
| 60 | [On the limited utility of parallel data for learning shared ...](http://arxiv.org/abs/2603.29026) | 训练含不同比例平行数据的参考模型，使用多种评估方法分析其作用效果 | 明确平行数据对跨语言对齐整体影响极小，仅在预训练早期存在有限作用 | — |
| 61 | [The Long Delay to Arithmetic Generalization: When Learned Re...](http://arxiv.org/abs/2604.13082) | 以一步Collatz预测为对象，通过因果干预、组件移植与控制训练验证解码器瓶颈假... | 提出泛化延迟源于解码器难以访问已学结构，揭示基数表示对任务可学习性的影响。 | — |
| 62 | [Over-Refusal and Representation Subspaces: A Mechanistic Ana...](http://arxiv.org/abs/2603.27518) | 本文分析两种拒绝类型的表征几何，采用线性探测验证二者表征的差异性 | 阐明两种拒绝的表征差异，解释全局消融无法解决过度拒绝的原因，指出需任务特异性几何... | — |
| 63 | [H-Node Attack and Defense in Large Language Models](http://arxiv.org/abs/2603.26045) | 提出H-Node ANC机制框架，定位幻觉节点，实现针对性攻击与自适应置信度加权... | 在多个不同参数规模的大模型上验证方法有效性，防御对模型通用推理能力影响极小 | — |
| 64 | [Do Hallucination Neurons Generalize? Evidence from Cross-Dom...](http://arxiv.org/abs/2604.19765) | 在6个不同领域和5个不同参数量开源大模型上，采用系统跨域迁移协议开展实验 | 证实幻觉神经元无法跨域泛化，指出幻觉无通用神经表征，检测器需分领域校准 | — |
| 65 | [Closing the Confidence-Faithfulness Gap in Large Language Mo...](http://arxiv.org/abs/2603.25052) | 采用线性探针与对比激活添加引导，对口头置信度开展机械可解释性分析。 | 发现信号编码规律，提出两阶段自适应引导流水线，显著提升所有评测模型的校准对齐水平... | — |
| 66 | [Why Safety Probes Catch Liars But Miss Fanatics](http://arxiv.org/abs/2603.25861) | 从理论层面证明探针缺陷，采用相同RLHF流程训练两类不同错位模型开展实验验证。 | 指出激活安全探针的根本盲区，证明复杂信念下多项式探针无法有效检测，提出涌现探针规... | — |
| 67 | [Between Rules and Reality: On the Context Sensitivity of LLM...](http://arxiv.org/abs/2603.23114) | 构建含三类系统语境变化的道德困境数据集，评估22个大模型，用激活引导调控语境敏感... | 引入新的语境化道德困境数据集，揭示大模型与人类道德判断的差异，提出可调控语境敏感... | — |
| 68 | [Riding Brainwaves in LLM Space: Understanding Activation Pat...](http://arxiv.org/abs/2603.21847) | 基于30名受试者的词级脑电数据，为每位个体训练独立线性探针映射LLM隐藏态到脑电... | 证实冻结大语言模型深层存在稳定的个体特异性神经方向，为脑电驱动个性化提供几何基础... | — |
| 69 | [Mechanisms of Introspective Awareness](http://arxiv.org/abs/2603.21396) | 通过行为测试、机制溯源与消融实验，分析内省感知能力的来源与运作机制。 | 揭示了内省感知的两阶段检测电路机制，发现该能力未被充分激发且可大幅提升。 | ✅ |
| 70 | [Before the First Token: Scale-Dependent Emergence of Halluci...](http://arxiv.org/abs/2604.13068) | 基于三个事实数据集，分析7个参数规模117M到7B的自回归Transformer... | 发现幻觉信号存在规模依赖的相变，明确预生成信号的产生条件，给出规模校准的检测方案 | — |
| 71 | [Inducing Epistemological Humility in Large Language Models: ...](http://arxiv.org/abs/2603.17504) | 构建HypoTermInstruct数据集，通过针对性监督微调教授认识论谦卑以降... | 提出定制数据集与评估基准，证明该方法无需偏好/RL流程即可有效降幻觉并维持性能 | — |
| 72 | [Interpretability without actionability: mechanistic methods ...](http://arxiv.org/abs/2603.18353) | 对比四种机械可解释性方法，基于医生裁决的临床病例检验其校正模型错误的效果 | 证实当前机械可解释性方法无法可靠将语言模型内部知识转化为校正后的输出 | — |
| 73 | [DynHD: Hallucination Detection for Diffusion Large Language ...](http://arxiv.org/abs/2603.16459) | 从空间token和时间去噪动态维度提出DynHD，设计语义证据构建与偏差型幻觉检... | 实验证明所提DynHD在多个基准和骨干模型上，性能和效率均优于现有最优基线 | — |
| 74 | [Catching rationalization in the act: detecting motivated rea...](http://arxiv.org/abs/2603.17199) | 在大语言模型残差流上训练有监督探针，分别在CoT生成前后探测内部激活识别动机推理 | 证明从内部表征检测动机推理比CoT监控更可靠，生成前探测可提前预警避免冗余生成 | — |
| 75 | [Me, Myself, and $\pi$ : Evaluating and Explaining LLM Intros...](http://arxiv.org/abs/2603.20276) | 提出内省的原则性形式化分类，构建多维度评估套件Introspect-Bench开... | 证实前沿模型可优先访问自身策略，解释了大语言模型内省的产生机制 | — |
| 76 | [Nudging Hidden States: Training-Free Model Steering for Chai...](http://arxiv.org/abs/2603.14636) | 采用推理时模型引导的无训练方案，提出三种基于不同信息源的引导策略 | 在四个模型和四个基准上验证，准确率相比CoT提示最高提升4.4%，证实方法实用性 | — |
| 77 | [Reconciling In-Context and In-Weight Learning via Dual Repre...](http://arxiv.org/abs/2603.13459) | 修改模型架构，将上下文和样本分别编码入两个对偶表示空间，提出CoQE架构 | 经理论与实验验证，CoQE可提升ICL性能，成功调和ICL与IWL两种能力 | — |
| 78 | [Truth as a Compression Artifact in Language Model Training](http://arxiv.org/abs/2603.11749) | 用3.5M到86M参数的小Transformer做控制实验，构建含对错解的语料训... | 提出压缩一致性原理解释模型偏好，发现仅错误结构不连贯时才会产生真理偏差 | — |
| 79 | [Adaptive Activation Cancellation for Hallucination Mitigatio...](http://arxiv.org/abs/2603.10195) | 提出自适应激活抵消（AAC）实时推理框架，识别幻觉节点后用置信加权前钩抑制，无需... | 在不同规模的多个模型基准上提升下游准确率，完全保留模型原有能力，选择性远高于对比... | — |
| 80 | [Whitening Reveals Cluster Commitment as the Geometric Separa...](http://arxiv.org/abs/2603.07755) | 在GPT-2-small上采用PCA白化与特征谱分解，结合多种子稳定性分析与提示... | 证实白化可揭示簇承诺度为正确分隔指标，明确分界本质，发现近饱和空间提示集脆弱性 | — |
| 81 | [COLD-Steer: Steering Large Language Models via In-Context On...](http://arxiv.org/abs/2603.06495) | 提出无训练框架COLD-Steer，通过两种互补逼近方法近似上下文示例梯度下降带... | 打破现有方法的权衡，仅用远少于基线的样本即可实现高引导效果，适配多元对齐需求 | — |
| 82 | [Evaluating LLM Alignment with Human Trust Models](http://arxiv.org/abs/2603.05839) | 对EleutherAI/gpt-j-6B开展信任表征白盒分析，用对比提示、余弦相... | 证明LLM可在激活空间编码社会认知构造，为相关研究与人机协作系统设计提供支撑 | — |
| 83 | [Separable Expert Architecture: Toward Privacy-Preserving LLM...](http://arxiv.org/abs/2604.21571) | 提出三层分离架构，结合静态基模型、可组合LoRA适配器与可删除用户代理，分离个人... | 将机器遗忘转化为确定性删除操作，兼具个性化与隐私保障，可兼容DP-SGD优化共享... | — |
| 84 | [Mitigating Hallucinations in Large Vision-Language Models wi...](http://arxiv.org/abs/2604.20366) | 提出双阶段框架MPD，通过语义感知解耦提取纯幻觉组件，选择性更新与幻觉相关的参数 | 实现SOTA性能，减少23.4%幻觉的同时保留97.4%通用生成能力，且无额外计... | — |
| 85 | [Pause or Fabricate? Training Language Models for Grounded Re...](http://arxiv.org/abs/2604.19656) | 提出交互式强化学习接地推理框架GRIL，分两阶段推理，设计特定奖励惩罚模型幻觉 | 实验表明GRIL大幅提升前提检测，提高任务成功率，缩短响应长度，鲁棒性好可泛化 | — |
| 86 | [Are LLM Uncertainty and Correctness Encoded by the Same Feat...](http://arxiv.org/abs/2604.19974) | 构建按正确性与置信度划分的2×2框架，利用稀疏自编码器独立识别各维度相关特征 | 划分出三类功能不同的特征群体，证实二者是不同内部现象，可干预提升模型性能 | — |
| 87 | [The Geometric Canary: Predicting Steerability and Detecting ...](http://arxiv.org/abs/2604.17698) | 基于表征成对距离结构的几何稳定性，分别用监督、无监督方法处理两个部署任务 | 提出监督与无监督几何稳定性，分别适配预部署评估与后部署监测，性能表现优异 | — |
| 88 | [ATLAS: Constitution-Conditioned Latent Geometry and Redistri...](http://arxiv.org/abs/2604.17663) | 提出几何优先的ATLAS框架，通过局部图表测量系统变化下隐态结构的相关特征 | 实现了跨模型跨底物的宪法诱导隐态结构追踪，揭示了其跨底物的几何重发生规律 | — |
| 89 | [Pruning Unsafe Tickets: A Resource-Efficient Framework for S...](http://arxiv.org/abs/2604.15780) | 提出资源高效的剪枝框架，采用无梯度归因机制识别并移除与不安全行为相关的模型参数 | 得到可减少不安全生成、提升越狱鲁棒性的轻量对齐策略，适合资源受限场景且效用损失小 | — |
| 90 | [CausalDetox: Causal Head Selection and Intervention for Lang...](http://arxiv.org/abs/2604.14602) | 提出CausalDetox框架，基于PNS筛选致毒因果注意力头，采用两种互补策略... | 提出新评测基准PARATOX，该方法减毒效果优于基线，保留流畅度且头选择速度提升... | — |
| 91 | [FineSteer: A Unified Framework for Fine-Grained Inference-Ti...](http://arxiv.org/abs/2604.15488) | 提出包含子空间条件引导（SCS）和混合引导专家（MoSE）的两阶段统一推理引导框... | 在安全与真实性基准测试中，FineSteer性能超过现有最优方法，以极小效用损失... | — |
| 92 | [Hallucination as Trajectory Commitment: Causal Evidence for ...](http://arxiv.org/abs/2604.15400) | 采用同提示分岔分离混淆因素，结合激活补丁、窗口补丁、探针与聚类开展因果分析 | 为幻觉是不对称吸引子动力学支配的早期轨迹承诺提供因果证据，揭示了其吸引子盆结构 | — |
| 93 | [How Do LLMs and VLMs Understand Viewpoint Rotation Without V...](http://arxiv.org/abs/2604.15294) | 采用分层探针分析与头层级因果干预识别关键注意力头，再对其进行选择性微调 | 提出VRU任务数据集，揭示模型能力不足机制，选择性微调可提升性能且避免通用能力遗... | — |
| 94 | [Predicting Where Steering Vectors Succeed](http://arxiv.org/abs/2604.15557) | 引入分层诊断工具线性可访问性剖面LAP，复用logit lens，无需训练即可预... | 提出三制度框架划分不同引导方法适用场景，验证LAP效果优于传统启发式方法 | — |
| 95 | [The cognitive companion: a lightweight parallel monitoring a...](http://arxiv.org/abs/2604.13759) | 提出认知伴侣轻量并行监控架构，包含基于大模型和零开销基于探针两种实现。 | 开展可行性研究验证该架构效果，明确了任务依赖性与模型规模边界，得到有参考价值的结... | — |
| 96 | [Awakening Dormant Experts:Counterfactual Routing to Mitigate...](http://arxiv.org/abs/2604.14246) | 提出无训练推理框架反事实路由CoR，结合CEI指标动态分配计算资源唤醒休眠专家 | 不增加推理预算，多个数据集上平均提升事实准确率3.1%，获得更优帕累托前沿 | — |
| 97 | [Geometric Routing Enables Causal Expert Control in Mixture o...](http://arxiv.org/abs/2604.14434) | 采用低维度量空间余弦相似性几何路由，结合语义投影与因果干预验证专家特性 | 证实单秩专家天生单义，专家专业化可直接检查，可实现推理零开销的因果专家控制 | — |
| 98 | [Preventing Safety Drift in Large Language Models via Coupled...](http://arxiv.org/abs/2604.12384) | 提出耦合权重与激活约束CWAC，同时约束权重更新安全子空间，对安全关键特征做正则... | 在多个大模型和下游任务实验中，CWAC性能优于强基线，有害分数低且几乎不影响微调... | — |
| 99 | [Reducing Hallucination in Enterprise AI Workflows via Hybrid...](http://arxiv.org/abs/2604.11141) | 将幻觉缓解建模为最小贝叶斯风险问题，提出融合语义相似度与词汇精度的HUMBR框架... | 经公开基准与企业真实生产数据验证，方法效果优于现有方法，可大幅降低高风险工作流的... | — |
| 100 | [Verbalizing LLMs' Assumptions About the User to Calibrate Ex...](https://www.semanticscholar.org/paper/71215b1da630dc25040fb0e73ebde99e13da321e) | 提出言语化假设框架，用于揭示大语言模型对用户意图的隐含假设，结合探针引导调整模型... | 揭示了人机交互中用户期望与模型假设的错配，证明该框架可有效减少大语言模型的谄媚问... | — |
| 101 | [SinkTrack: Attention Sink based Context Anchoring for Large ...](http://arxiv.org/abs/2604.10027) | 提出无需训练、即插即用的SinkTrack方法，以序列首个token为锚注入关键... | 所提方法推理开销可忽略，在文本和多模态任务均获提升，具备良好的鲁棒性与泛化性 | ✅ |
| 102 | [Arbitration Failure, Not Perceptual Blindness: How Vision-La...](http://arxiv.org/abs/2604.09364) | 采用多模态仲裁交叉分析、逐层Logit Lens探测与全序列激活修补开展研究 | 揭示编码-接地解离现象，证实VLM已良好编码视觉信息，错误源于仲裁并提出改进方法 | — |
| 103 | [SHIFT: Steering Hidden Intermediates in Flow Transformers](http://arxiv.org/abs/2604.09213) | 提出SHIFT轻量框架，学习引导向量，推理时动态作用于选定层和时间步操纵中间激活 | 可实现概念去除、风格迁移、目标对象增改，无需重训，能灵活控制DiT生成效果 | — |
| 104 | [Activation Steering for Aligned Open-ended Generation withou...](http://arxiv.org/abs/2604.08169) | 以激活引导作为轻量运行时防御，测试了SwFC、StTP、StMP三种激活校正方法 | 验证三种方法均可恢复对齐特质保留连贯性，两种新方法更能维持通用能力减少重复 | — |
| 105 | [ART: Attention Replacement Technique to Improve Factuality i...](http://arxiv.org/abs/2604.06393) | 提出无需训练的注意力替换技术ART，将大模型浅层均匀注意力替换为局部注意力模式。 | 经大量实验验证，该方法可在多种大模型架构上显著减少幻觉，无需微调或额外训练数据。 | — |
| 106 | [Confidence Should Be Calibrated More Than One Turn Deep](http://arxiv.org/abs/2604.05397) | 提出多轮校准任务，设计动态校准度量ECE@T，提出MTCal方法与ConfCha... | 验证所提方法性能优异，指出多轮校准是大模型安全可靠落地的缺失环节 | — |
| 107 | [LatentAudit: Real-Time White-Box Faithfulness Monitoring for...](http://arxiv.org/abs/2604.05358) | 提出LatentAudit白盒审计器，计算生成模型残差流激活与证据表示的马氏距离... | 实现RAG实时忠实度监控，支持可验证部署，在多个测试基准上取得优异性能 | — |
| 108 | [How LLMs Follow Instructions: Skillful Coordination, Not a U...](http://arxiv.org/abs/2604.06015) | 在三个指令微调模型上，对九个不同任务开展诊断探针、跨任务迁移、因果消融分析 | 得到多维度汇聚证据反驳了指令遵循的通用机制说，明确了指令遵循能力的本质 | — |
| 109 | [Weakly Supervised Distillation of Hallucination Signals into...](http://arxiv.org/abs/2604.06277) | 提出弱监督框架结合三种互补接地信号自动标注，将幻觉信号蒸馏入Transforme... | 构建了含15000样本的标注数据集，验证了内部幻觉检测的可行性，证明推理开销可忽... | — |
| 110 | [Memory Dial: A Training Framework for Controllable Memorizat...](http://arxiv.org/abs/2604.05074) | 提出Memory Dial训练框架，通过单参数α控制记忆压力，得到仅记忆压力不同... | 实现了语言模型记忆压力的可靠控制，为研究记忆与泛化的交互提供可控实验框架 | — |
| 111 | [Extracting and Steering Emotion Representations in Small Lan...](http://arxiv.org/abs/2604.04064) | 对5种架构共9个小语言模型，对比两种情感向量提取方法，结合验证与引导实验分析 | 为开放权重模型的情感研究提供方法指南，连通外部行为分析与内部表征分析 | — |
| 112 | [Where to Steer: Input-Dependent Layer Selection for Steering...](http://arxiv.org/abs/2604.03867) | 提出W2S框架，学习输入嵌入到最优引导层的映射，依据输入自适应选择干预层 | 从理论和实证证明最优引导层随输入变化，所提方法在分布内外均优于固定层基线 | — |
| 113 | [Verbalizing LLMs'assumptions to explain and control sycophan...](http://arxiv.org/abs/2604.03058) | 提出口头化假设框架提取大语言模型隐含假设，借助假设探针调控社会谄媚行为 | 阐明假设是大语言模型谄媚行为的作用机制，实现可解释的细粒度谄媚行为调控 | — |
| 114 | [Reliable Control-Point Selection for Steering Reasoning in L...](http://arxiv.org/abs/2604.02113) | 提出稳定性过滤保留目标行为一致的边界，结合内容子空间投影去噪构建可靠转向向量 | 所提方法提升推理任务准确率，所得转向向量可在同架构家族模型间迁移无需重提取 | — |
| 115 | [Attention at Rest Stays at Rest: Breaking Visual Inertia for...](http://arxiv.org/abs/2604.01989) | 提出无需训练的惯性感知视觉激励（IVE）方法，选择动态token，施加惯性惩罚打... | 实验证明IVE在多种基础MLLM和多个幻觉基准上有效，尤其可有效缓解认知幻觉 | — |
| 116 | [Aligning Recommendations with User Popularity Preferences](http://arxiv.org/abs/2604.01036) | 提出流行度分位数校准测量框架，以及基于激活引导的推理时去偏方法SPREE | 实验证明SPREE在保留推荐质量的同时，能够稳定提升用户层面的流行度对齐效果 | — |
| 117 | [QuantumQA: Enhancing Scientific Reasoning via Physics-Consis...](http://arxiv.org/abs/2604.18176) | 构建物理一致的QuantumQA数据集，提出带自适应奖励融合的验证感知强化学习方... | 所提方法性能优于基线与通用偏好模型，8B参数模型性能可媲美专有模型，参数效率更高... | — |
| 118 | [A Survey of Reinforcement Learning for Large Language Models...](http://arxiv.org/abs/2604.17312) | 从数据、训练、框架三个互补视角提出自底向上分层框架，对现有方法构建分类体系并梳理... | 首次系统综述该方向研究，构建分类体系，为领域研究者提供概念基础与研究路线图。 | — |
| 119 | [Reward Hacking in the Era of Large Models: Mechanisms, Emerg...](http://arxiv.org/abs/2604.13602) | 提出代理压缩假设作为统一理解框架，基于三类成因梳理奖励黑客的检测与缓解策略 | 统一不同对齐范式下的奖励黑客现象，梳理应对策略，点明领域现存的多个开放研究挑战 | — |
| 120 | [Reinforcement Learning with Negative Tests as Completeness S...](http://arxiv.org/abs/2604.05820) | 提出Dafny规范合成的SpecRL强化学习框架，将负测试拒识率作为完备性信号融... | 提出的SpecRL提升了规范强度与验证成功率，在分布外基准上泛化性好，竞争力强 | — |
| 121 | [Beyond Compromise: Pareto-Lenient Consensus for Efficient Mu...](http://arxiv.org/abs/2604.05965) | 提出帕累托宽松共识PLC博弈框架，采用共识驱动的宽松梯度校正搜索帕累托最优前沿 | 理论验证方法可逃离局部僵局，实验证明其对齐效果和帕累托前沿质量优于基线方法 | — |
| 122 | [Many Preferences, Few Policies: Towards Scalable Language Mo...](http://arxiv.org/abs/2604.04144) | 提出PALM算法，构建小规模代表性大语言模型组合，覆盖异质用户多维度偏好 | 首次为个性化大语言模型组合的大小和近似质量提供理论保证，实证验证效果优于基线 | — |
| 123 | [VC-Soup: Value-Consistency Guided Multi-Value Alignment for ...](http://arxiv.org/abs/2603.18113) | 提出基于价值一致性学习的VC-Soup框架，包含数据过滤、参数合并与帕累托过滤步... | 提出的VC-Soup方法可有效缓解价值冲突，性能稳定优于现有多价值对齐方法 | — |
| 124 | [SQL-ASTRA: Alleviating Sparse Feedback in Agentic SQL via Co...](http://arxiv.org/abs/2603.16161) | 提出带通用双层奖励机制的Agentic SQL框架，设计ATR和CSMR分别解决... | 在多个公开数据集上性能优于现有SOTA，推动Text-to-SQL走向鲁棒的多轮... | — |
| 125 | [Let's Reward Step-by-Step: Step-Aware Contrastive Alignment ...](http://arxiv.org/abs/2603.09740) | 提出步骤感知对比对齐框架SACA，分步评估轨迹，动态分组适配专门重采样与优化策略 | 提出可从非完美轨迹提取密集监督的SACA框架，在VLN-CE基准上取得当前最优性... | — |
| 126 | [AlpsBench: An LLM Personalization Benchmark for Real-Dialogu...](http://arxiv.org/abs/2603.26680) | 构建源自真实人机对话的AlpsBench基准，定义四项核心任务并建立全流程评估协... | 提出面向大语言模型个性化的真实对话基准，完成前沿模型评测，得出多项关键结论 | — |
| 127 | [Property-driven Protein Inverse Folding With Multi-Objective...](http://arxiv.org/abs/2603.06748) | 提出ProtAlign多目标偏好对齐框架，用半在线直接偏好优化微调预训练逆折叠模... | 得到的MoMPNN模型可在多类任务中提升可开发性且不损失可设计性，适用于实际蛋白... | — |
| 128 | [Alternating Reinforcement Learning with Contextual Rubric Re...](http://arxiv.org/abs/2603.15646) | 提出ARL-RR框架，无需固定标量化，逐次优化单个语义评分元类，动态适配下一元类 | 理论证明奖励聚合的方差收缩效应，实验验证该方法性能和训练效率优于已有方法 | — |
| 129 | [Stabilizing Policy Optimization via Logits Convexity](http://arxiv.org/abs/2603.00963) | 基于对logits凸性稳定训练作用的观察，提出简单有效的Logits凸优化（LC... | 从梯度视角揭示稳定性差距来源，提出的LCO提升训练稳定性，多基准上优于传统强化学... | — |
| 130 | [Stop-Think-AutoRegress: Language Modeling with Latent Diffus...](http://arxiv.org/abs/2602.20528) | 提出STAR-LDM模型，将潜扩散规划融入自回归生成，新增思考阶段优化语义规划后... | 模型性能优于同规模模型，相关任务大模型评判胜率超70%，支持无需重训练的细粒度属... | — |
| 131 | [UniARM: Towards a Unified Autoregressive Reward Model for Mu...](http://arxiv.org/abs/2602.09538) | 提出偏好调制共享低秩适配MoSLoRA，基于此构建统一自回归奖励模型UniARM | 缓解了特征纠缠，可精准控制偏好权衡，消除了各偏好目标需独立参数的要求 | — |
| 132 | [Autoregressive Direct Preference Optimization](http://arxiv.org/abs/2602.09533) | 重新梳理DPO理论基础，在应用BT模型前显式引入自回归假设，推导出ADPO新方法 | 提出形式简洁的ADPO损失，首次显式区分两种长度测度并分析其对偏好优化的影响 | — |
| 133 | [rePIRL: Learn PRM with Inverse RL for LLM Reasoning](http://arxiv.org/abs/2602.07832) | 提出逆强化学习启发的rePIRL框架，采用策略与PRM交替更新的双学习流程 | 理论上统一了在线和离线PRM学习方法，实验验证其性能优于现有同类方法 | — |
| 134 | [TeleBoost: A Systematic Alignment Framework for High-Fidelit...](http://arxiv.org/abs/2602.07595) | 提出TeleBoost框架，整合监督策略塑造、奖励强化学习、偏好精调为稳定性约束... | 提供了稳定可扩展的后训练流程蓝图，提升生成视频的保真度、时序一致性与提示依从性 | — |
| 135 | [Uncovering Cross-Objective Interference in Multi-Objective A...](http://arxiv.org/abs/2602.06869) | 推导局部协方差定律，在此基础上提出即插即用的协方差靶向权重自适应CTWA方法缓解... | 首次系统研究交叉目标干扰，推导得到协方差定律，提出缓解方法并完成全局收敛性分析 | — |
| 136 | [EXACT: Explicit Attribute-Guided Decoding-Time Personalizati...](http://arxiv.org/abs/2602.17695) | 提出显式属性引导的EXACT方法，离线识别用户属性子集，在线检索相关属性引导生成 | 给出算法理论近似保证，证明可缓解上下文偏好偏移，实验验证效果优于多个强基线 | — |
| 137 | [Continuous-Utility Direct Preference Optimization](http://arxiv.org/abs/2602.00931) | 提出CU-DPO框架，用连续分数替代二元标签，采用策略选择与执行优化两阶段训练流... | 理论证明样本复杂度获得改进，实验显示显著提升数学推理的策略选择准确率与推理性能 | — |
| 138 | [A New Strategy for Artificial Intelligence: Training Foundat...](http://arxiv.org/abs/2601.12053) | 按感知等四个层级梳理问题，提出RLHB和CoTHB两种方法，利用有限人脑数据训练... | 提出直接基于人脑数据训练基础模型的新策略，分类梳理局限，给出方法并探讨相关影响与... | — |
| 139 | [Owen-Shapley Policy Optimization (OSPO): A Principled RL Alg...](http://arxiv.org/abs/2601.08403) | 提出Owen-Shapley策略优化OSPO，基于Shapley-Owen归因分... | 解决信用分配缺口问题，无需额外参数价值模型，实验验证性能提升与分布外鲁棒性 | — |
| 140 | [Active Knowledge Retrieval to Reduce Hallucinations and Enha...](https://www.semanticscholar.org/paper/1a6fc7a561cc4dbbc771e14d0f3e527b6840bccb) | 提出推理-检索-信息整合框架，使大推理模型推理时可自主获取实时医学数据并结合自身... | 在开放域医学问答任务中性能显著提升，为可解释临床医疗AI及其他领域任务提供可扩展... | — |
| 141 | [Attribution Techniques for Mitigating Hallucinated Informati...](http://arxiv.org/abs/2601.19927) | 梳理领域相关研究，构建幻觉分类与归因技术统一流程，对比分析各技术优缺点 | 给出RAG幻觉分类与归因技术统一框架，梳理技术，提供实践指南与研究参考 | — |
| 142 | [eTracer: Towards Traceable Text Generation via Claim-Level G...](http://arxiv.org/abs/2601.03669) | 提出即插即用的eTracer框架，通过事后声明级接地将每个响应声明与上下文证据对... | 实现生成响应的可溯源与忠实度量化，提升了整体接地质量与用户验证效率 | — |
| 143 | [IRPM: Intergroup Relative Preference Modeling for Pointwise ...](http://arxiv.org/abs/2601.00677) | 提出IRPM方法，通过组间对比扩展偏好学习范式，从成对数据训练点生成奖励模型。 | 在多个基准达到点生成奖励模型SOTA，性能接近领先成对模型，后训练评估增益显著。 | — |
| 144 | [Fine-Tuning LLMs with Fine-Grained Human Feedback on Text Sp...](http://arxiv.org/abs/2512.23693) | 采集细粒度人类对文本跨度的好恶反馈构建改进链，基于相邻步骤构造偏好对微调模型 | 提出基于结构化修订监督的偏好微调方法，构建对应数据集，效果优于现有直接对齐方法 | — |
| 145 | [A Consistency-Oriented Verification Framework for Reliable P...](https://www.semanticscholar.org/paper/f675d35926709368d7b759d6227171732e2f82b6) | 提出面向电力行业大模型的一致性导向验证框架，采用分解验证链实现推理阶段自验证 | 所提方法显著提升模型任务性能，明确了最大化验证校正效果的最优参数与提示方式 | — |
| 146 | [Neologism Learning as a Parameter-Efficient Alternative to F...](http://arxiv.org/abs/2512.18551) | 通过新词学习仅训练少量参数实现模型行为引导，与低秩适配微调开展对比 | 验证相同设置下新词学习性能优于微调，探究了模型对新词的自我表述现象 | — |
| 147 | [Multimodal RewardBench 2: Evaluating Omni Reward Models for ...](http://arxiv.org/abs/2512.16899) | 构建首个多模态奖励模型综合评测基准MMRB2，包含四个任务共四千专家标注偏好对 | 提出首个多模态奖励模型综合评测基准，评测现有模型，验证性能与下游任务强相关 | — |
| 148 | [When Distance Distracts: Representation Distance Bias in BT-...](http://arxiv.org/abs/2512.06343) | 提出NormBT自适应成对归一化方案，重新缩放梯度更新，平衡表征距离影响，聚焦预... | 在多种大语言模型主干和数据集上稳定提升奖励模型性能，在RewardBench推理... | — |
| 149 | [Towards better dense rewards in Reinforcement Learning Appli...](http://arxiv.org/abs/2512.04302) | 探索逆强化学习、人类偏好奖励建模、自监督内在奖励学习等多种路径改进稠密奖励构建。 | 探索解决现有未决问题的多种路径，提升不同强化学习应用中稠密奖励构建的有效性可靠性... | — |
| 150 | [SR-GRPO: Stable Rank as an Intrinsic Geometric Reward for La...](http://arxiv.org/abs/2512.02807) | 提取模型内部表征得到无标注固有稳定秩，以其为奖励提出SR-GRPO强化学习对齐方... | 无需外部监督即可提升大模型推理性能，效果优于现有奖励模型与自评估基线 | — |
| 151 | [When Human Preferences Flip: An Instance-Dependent Robust Lo...](http://arxiv.org/abs/2512.00709) | 提出FA-DPO算法，基于BT模型引入实例依赖翻转概率，设计适配原有算法的迭代优... | 提出针对偏好翻转问题的鲁棒RLHF算法，可兼容原有算法，多场景实验验证了方法有效... | — |
| 152 | [Ranking Large Language Models with Human Preferences: A Game...](https://www.semanticscholar.org/paper/aa1a9d6f5450439bef26ca8bad3c9673ececf8fd) | 对包括新提出的HawasRank在内的六种排序算法，基于多评价指标开展对比研究 | 揭示不同排序方法间的权衡，为大规模动态大模型评估选算法提供实用指导 | — |
| 153 | [Towards Reinforcement Learning from Neural Feedback: Mapping...](http://arxiv.org/abs/2511.12844) | 采集多领域人类fNIRS信号，训练分类器与回归器预测智能体性能，微调提升跨被试泛... | 发布三领域25名被试的新型fNIRS数据集，验证映射可行性，为脑驱动RLHF奠定... | — |
| 154 | [Multi-Value Alignment for LLMs via Value Decorrelation and E...](http://arxiv.org/abs/2511.17579) | 提出MVA框架，通过最小化互信息缓解不同价值间参数干扰，结合价值外推探索帕累托前... | 提出全新多价值对齐框架MVA，大量实验证明该框架在多价值对齐任务上优于现有基线方... | — |
| 155 | [Speech Recognition Model Improves Text-to-Speech Synthesis u...](http://arxiv.org/abs/2511.17555) | 提出W3AR方法，借助预训练ASR模型的内部注意力信息提供细粒度奖励，优化TTS... | 提升现有TTS模型的生成质量与零样本鲁棒性，为各类生成任务提供了新的研究思路 | — |
| 156 | [Feedback Descent: Open-Ended Text Optimization via Pairwise ...](http://arxiv.org/abs/2511.07919) | 提出Feedback Descent框架，将结构化文本反馈转化为梯度方向信息，推... | 所提框架在多个领域性能优于现有一流方法，在分子发现中找到超数据库99.9百分位的... | — |
| 157 | [A Survey on Human Preference Learning for Aligning Large Lan...](https://www.semanticscholar.org/paper/e3a5da866598c0414dd186085ccd429ac8ea664e) | 在统一研究框架下对现有研究分类梳理，归纳相关技术与评估方案 | 系统梳理领域研究进展，划分研究类别，总结评估方法，明确挑战与未来方向 | — |
| 158 | [PACR: Progressively Ascending Confidence Reward for LLM Reas...](http://arxiv.org/abs/2510.22255) | 提出渐进提升置信度奖励PACR，是直接从模型对正确答案的动态信念计算得到的稠密模... | 经理论与实验验证，该方法可约束探索搜索空间，加速探索，在多个基准提升大模型推理效... | — |
| 159 | [ScholarEval: Research Idea Evaluation Grounded in Literature](http://arxiv.org/abs/2510.16234) | 提出检索增强的ScholarEval评估框架，从可靠性与贡献两个核心维度评估研究... | 构建首个多领域专家标注研究创意数据集，框架性能优于基线，开放相关资源供社区使用 | — |
| 160 | [Putting on the Thinking Hats: A Survey on Chain of Thought F...](http://arxiv.org/abs/2510.13170) | 借鉴六顶思考帽框架，从人类推理机制视角对思维链微调方法进行分类梳理 | 产出首份基于人类推理理论的思维链微调综述，整理数据集性能，维护实时更新的Gith... | — |
| 161 | [Towards neuroadaptive chatbots: a feasibility study](https://www.semanticscholar.org/paper/155109edca1e893f9cfe3c00e81f62de2fbc6e64) | 设计两种文本刺激范式，采集受试者脑电，结合窗口均值法和LDA离线训练心理状态分类... | 验证了被动脑机接口区分单试次脑数据心理状态的可行性，为大模型神经对齐打下初步基础 | — |
| 162 | [OpenRubrics: Towards Scalable Synthetic Rubric Generation fo...](http://arxiv.org/abs/2510.07743) | 构建大规模OpenRubrics数据集，提出对比评分规则生成CRG，通过偏好一致... | 提出的Rubric-RM在多个奖励建模基准超越强基线，性能增益可迁移至下游任务策... | — |
| 163 | [Revisiting Self-Play Preference Optimization: On the Role of...](http://arxiv.org/abs/2510.05534) | 以提示词对应采样响应的平均奖励作为难度代理，探究不同难度提示词对自对弈优化的影响 | 探明提示词难度对自对弈偏好优化性能的影响规律，提出仅训练简单提示的性能提升策略 | — |

## 常见基线方法

- **SFT** (3 篇引用)
- **GRPO** (3 篇引用)
- **GPT-4o** (2 篇引用)
- **未提及具体基线方法** (2 篇引用)
- **自给自足方案** (1 篇引用)
- **无激励设计的强制共享方案** (1 篇引用)
- **隐式条件卷积循环神经网络替代模型** (1 篇引用)
- **显式条件卷积循环神经网络替代模型** (1 篇引用)
- **CodeSIM** (1 篇引用)
- **GPT-3.5提示基线** (1 篇引用)

## 本周提到的 Limitations

- 隐式条件迷你序列方法仅在使用更大规模训练数据集时才能得到可比的预测效果
- 当前评估型VLM存在大量评估盲点，对细粒度、空间等多种关键错误的检测能力不足
- 仅完成离线循环的基准测试与记录，未对在线反馈到评估路径做定量评估
- 驱动Engrama跨空间优势的组件会牺牲全局综合得分，结构化专门化与全局优化存在矛盾
- 开放权重模型处理需单个token承载两个主谓宾绑定的句法时，准确率接近随机水平
- 当前仅使用单个厂商的相关模型，场景规模较小，未进行提示词优化。
- 现有全模态记谱处理研究碎片化，偏向西方记谱，评测不可靠，推理缺陷常被掩盖
- 利用内在维度研究神经表征方法的诸多重要局限性，此前一直未得到解决
- 在复杂的押韵对句完成任务中，即便是大规模模型，也很少能够开展长远提前规划。
- 现有基准均仅测试编造类欺骗，语用扭曲等内容覆盖严重不足，战略欺骗基准尚不成熟
- 提取的幻觉信号仅为相关关系而非因果关系，基于该信号的激活引导无法纠正幻觉
- 现有机械可解释性方法无法可靠弥合知识行动差距，不能有效校正语言模型输出错误
- 压缩一致性原理能否推广至语言模型大规模预训练目前仍是开放问题
- 当前仅得到一、二类幻觉分离方向稳定但功效不足的结果，未在小模型上实现完全区分
- 紧致精确块充分性不成立，邻近目标局部信号可在无源忠实闭合时存在
- 仅为可行性研究而非最终验证，在1B-1.5B小模型上未观测到质量提升。
- 本文提出的无训练激活引导方法，在部分实验设置中会出现性能下降
- 当前该领域仍存在可扩展监督、多模态接地、智能体自主性等未解决的开放挑战
- 直接用人脑数据训练基础模型用于高阶认知功能的路径目前仍未得到充分探索
- 现有稠密奖励相关方法需要在通用性、可扩展性与人类意图对齐三者之间做权衡。
- 当前大语言模型对齐的人类偏好学习仍存在诸多开放性挑战尚未解决
- 仅开展离线研究，尚未在低控制语言任务和真实聊天交互中验证分类器可靠性

## 常用数据集

- **MMLU** (3 篇使用)
- **TruthfulQA** (3 篇使用)
- **RewardBench** (3 篇使用)
- **TriviaQA** (2 篇使用)
- **HalluScope基准** (1 篇使用)
- **精选偏好训练数据集** (1 篇使用)
- **RedirectQA** (1 篇使用)
- **SyMTRS** (1 篇使用)
- **合成反洗钱基准数据集** (1 篇使用)
- **Allen-Cahn动力学数值积分生成的晶体生长时间序列数据集** (1 篇使用)


---

*自动生成于 2026-04-26 | Research Radar*