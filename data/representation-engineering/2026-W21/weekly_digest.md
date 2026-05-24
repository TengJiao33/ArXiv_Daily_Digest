# 表示工程、激活引导与价值对齐干预 — 2026-W21 (05/18-05/24)

本周新增 **52** 篇论文。2 篇附带代码仓库。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，考虑收紧 arxiv_query

## 分类分布

- `via-citation`: 38 篇
- `cs.LG`: 6 篇
- `cs.AI`: 3 篇
- `cs.CR`: 2 篇
- `cs.RO`: 1 篇
- `cs.CL`: 1 篇
- `cs.CV`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [Diagnosing and Correcting Concept Omission in Multimodal Dif...](http://arxiv.org/abs/2605.14270) | 通过对文本token线性探测获得概念遗漏信号，提出OSI方法放大信号催化缺失概念... | 在两个主流模型上实验验证，OSI可显著缓解概念遗漏问题，极端场景下也有效 | — |
| 2 | [Non-linear Interventions on Large Language Models](http://arxiv.org/abs/2605.14749) | 提出适配非线性表示特征的通用干预公式，以及适用于隐式特征的干预学习流程 | 所提框架在拒绝绕过引导任务上，对大语言模型的引导精度优于线性基线方法 | — |
| 3 | [Dual-Pathway Circuits of Object Hallucination in Vision-Lang...](http://arxiv.org/abs/2605.13156) | 提出双路径回路分析框架，结合激活补丁与条件路径分析识别幻觉相关回路 | 识别出视觉接地路径与幻觉路径，抑制幻觉路径最高降低76%幻觉且精度损失极小 | — |
| 4 | [Not Just RLHF: Why Alignment Alone Won't Fix Multi-Agent Syc...](http://arxiv.org/abs/2605.12991) | 在四个模型家族开展对比测试，采用激活补丁技术定位成因，结合干预分析作用机制 | 证实预训练基座模型也存在该问题，定位问题所在模型层，指出应从流水线层面设计缓解方... | — |
| 5 | [Senses Wide Shut: A Representation-Action Gap in Omnimodal L...](http://arxiv.org/abs/2605.13737) | 构建2×2设计的IMAVB基准，测试多类全模态大模型，提出探针引导对数调整PGL... | 发现全模态大模型存在表征-动作缺口，定位全模态接地瓶颈在转换而非感知，PGLA可... | — |
| 6 | [Toward Stable Value Alignment: Introducing Independent Modul...](http://arxiv.org/abs/2605.11712) | 提出带独立价值模块的SVGT，通过独立价值建模和桥接Token显式引导生成过程 | 实验验证该方法可降低有害评分超70%，同时保持生成流畅性，验证了架构的有效性 | ✅ |
| 7 | [Exploitation Without Deception: Dark Triad Feature Steering ...](http://arxiv.org/abs/2605.09773) | 采用稀疏自编码器特征引导放大目标大模型的黑暗三角特质，结合心理工具评估行为变化 | 证明大语言模型反社会倾向为可分离成分而非统一建构，为其检测管控提供启示 | — |
| 8 | [Permit: Permission-Aware Representation Intervention for Con...](http://arxiv.org/abs/2605.09480) | 提出权限感知的Permit框架，识别权限敏感子空间，在子空间对隐藏状态做轻量级干... | 效果优于现有最优方法，信息泄露近乎为零，F1提升超18%，可训练参数减少98%以... | — |
| 9 | [How LLMs Are Persuaded: A Few Attention Heads, Rerouted](http://arxiv.org/abs/2605.09314) | 通过多步因果干预，追踪定位大语言模型中与诱导事实错误相关的注意力头与特征通路。 | 揭示了大语言模型诱导性事实错误的紧凑因果机制，发现该机制为可监控的狭窄回路。 | — |
| 10 | [How Much Do Circuits Tell Us? Measuring the Consistency and ...](http://arxiv.org/abs/2605.08348) | 对六个任务、七个模型开展边归因修补与组件消融，测量语言模型电路的一致性与特异性 | 量化分析语言模型电路特性，揭示电路跨任务高度重叠、任务特异性组件占比较低的特征 | — |
| 11 | [Safety Geometry Collapse in Multimodal LLMs and Adaptive Dri...](http://arxiv.org/abs/2605.18104v1) | 从表征几何视角分析问题，提出无训练推理方法ReGap，利用自整流自适应校正模态漂... | 揭示安全几何坍缩失效模式，验证ReGap可提升多模态大模型安全性且不损害通用能力 | — |
| 12 | [When a Zero-Shooter Cheats: Improving Age Estimation via Act...](http://arxiv.org/abs/2605.17658v1) | 提出激活引导方法，通过干预视觉语言模型的隐藏状态抑制身份捷径 | 提升了各类身份的年龄估计准确率，主流基准上平均绝对误差最高降低25% | — |
| 13 | [Ablating Safety: Mechanisms for Removing Alignment in Langua...](http://arxiv.org/abs/2605.17413v1) | 将对齐移除作为授权安全任务的受控变换评估协议，对比多种不同去对齐方案。 | 构建Security-AR测试套件，系统对比不同去对齐方法，指出对齐移除需权衡效... | — |
| 14 | [FishBack: Pullback Fisher Geometry for Optimal Activation St...](http://arxiv.org/abs/2605.17231v1) | 基于拉回Fisher信息度量推导闭式激活引导方程，得到最小失真最优方向，提出Fi... | 揭示现有方法隐式采用不同近似度量，提出的Fish框架性能优于多个现有激活引导基线 | — |
| 15 | [Contrastive Conceptor Activation Steering (COAST): Unlocking...](http://arxiv.org/abs/2605.17144v1) | 提出COAST方法，从少量成功失败样本识别任务成功子空间，推理时引导VLA隐态进... | 提供轻量免训练的VLA能力解锁路径，仿真、真实任务成功率分别提升超20%与40% | — |
| 16 | [VSPO: Vector-Steered Policy Optimization for Behavioral Cont...](http://arxiv.org/abs/2605.15604v1) | 提出向量引导策略优化VSPO，修改GRPO以不同引导强度采样，上采样稀有行为缓解... | 理论证明其迭代复杂度优于对比方法，实验表明可在维持精度同时改进目标行为控制。 | — |
| 17 | [Reasoning Models Don't Just Think Longer, They Move Differen...](http://arxiv.org/abs/2605.15454v1) | 分析多领域思维链生成的隐状态轨迹，将轨迹统计对长度做残差校正后开展分析 | 明确长度校正是生成阶段轨迹分析的前提，证明推理训练关联独特校正轨迹几何，效应强度... | — |
| 18 | [Fair outputs, Biased Internals: Causal Potency and Asymmetry...](http://arxiv.org/abs/2605.15217v1) | 针对开放权重模型房贷承销任务，采用匹配样本、激活引导与跨层干预开展研究 | 揭示公平输出可掩盖可利用内部偏差，指出现有输出审计不足，提出高风险决策的双层测试... | — |
| 19 | [CLIPer: Tailoring Diverse User Preference via Classifier-Gui...](http://arxiv.org/abs/2605.07162) | 提出CLIPer轻量个性化方法，推理阶段借助分类器动态引导大模型生成适配不同偏好 | 省去大量微调工作，额外计算开销可忽略，可实现多维度可控个性化，实验验证其有效性与... | — |
| 20 | [Decodable but Not Corrected by Fixed Residual-Stream Linear ...](http://arxiv.org/abs/2605.05715) | 以医疗问答中的过度思维（OT）故障为研究对象，测试多种固定线性引导的故障校正效果 | 揭示了可解码故障的分类-校正鸿沟，发现其可用于生成后模型可靠性估计 | — |
| 21 | [Geometric Deviation as an Unsupervised Pre-Generation Reliab...](http://arxiv.org/abs/2605.03196) | 通过测量大语言模型隐藏状态相对可回答参考集的几何偏差，无监督提取预生成可回答性信... | 证明几何偏差可作为轻量预生成可回答性信号，明确了其在不同任务下的泛化边界 | — |
| 22 | [Sparse Personalized Text Generation with Multi-Trajectory Re...](http://arxiv.org/abs/2604.24996) | 提出PAT推理框架，从两类对齐用户检索互补信息，采用强化学习迭代双推理整合信号 | 实验验证该方法可提升稀疏数据下生成质量与对齐，为冷启动个性化提供了有效方案 | — |
| 23 | [Many Preferences, Few Policies: Towards Scalable Language Mo...](http://arxiv.org/abs/2604.04144) | 提出PALM算法，选择小型代表性大语言模型组合，覆盖异质用户的多维度偏好 | 首次为个性化大语言模型组合提供规模与近似质量的理论保证，实证验证方法有效性 | — |
| 24 | [VC-Soup: Value-Consistency Guided Multi-Value Alignment for ...](http://arxiv.org/abs/2603.18113) | 提出价值一致性引导的VC-Soup框架，过滤低一致性数据训练后，线性合并模型并做... | 所提VC-Soup框架可有效缓解多价值冲突，性能持续优于已有的多价值对齐方法 | — |
| 25 | [AlpsBench: An LLM Personalization Benchmark for Real-Dialogu...](http://arxiv.org/abs/2603.26680) | 构建源自真实人机对话的AlpsBench基准，定义四项核心任务并建立全周期评估规... | 推出基于真实对话的LLM个性化评估基准，测试前沿模型得到多项有参考价值的结论 | — |
| 26 | [EXACT: Explicit Attribute-Guided Decoding-Time Personalizati...](http://arxiv.org/abs/2602.17695) | 提出显式属性引导的EXACT方法，离线识别用户属性子集，在线检索相关属性注入引导... | 给出算法理论近似保证，证明可缓解上下文偏好偏移，实验性能优于多个强基线方法 | — |
| 27 | [Owen-Shapley Policy Optimization: A Principled RL Algorithm ...](http://arxiv.org/abs/2601.08403) | 提出Owen-Shapley策略优化OSPO，基于Shapley-Owen归因分... | 解决大语言模型RL的信用分配缺口，实验验证算法相比基线有一致增益，对分布外检索器... | — |
| 28 | [Multi-Value Alignment for LLMs via Value Decorrelation and E...](http://arxiv.org/abs/2511.17579) | 提出MVA框架，通过最小化价值间互信息缓解参数干扰，结合价值外推探索帕累托前沿 | 提出新型多价值对齐框架，实验证明其在大语言模型多价值对齐上优于现有基线 | — |
| 29 | [Human Values Matter: Investigating How Misalignment Shapes C...](http://arxiv.org/abs/2604.05339) | 构建基于社会科学理论的可控多智能体环境CIVA，开展全面的模拟仿真实验 | 识别出影响集体动态的关键价值观，发现相关宏观与微观行为，提供了量化研究证据 | — |
| 30 | [Steering LLMs for Culturally Localized Generation](http://arxiv.org/abs/2603.23301) | 借助机械可解释性，利用稀疏自动编码器识别文化特征，构建CuE实现白盒引导干预 | 提供大语言模型文化表示的诊断洞察，给出可控引导方法，提升生成的文化忠实度 | — |
| 31 | [Controllable Value Alignment in Large Language Models throug...](http://arxiv.org/abs/2602.07356) | 提出NeVA神经元级编辑框架，识别稀疏价值相关神经元，推理时编辑激活，无需参数更... | 提出值泄漏概念与对应归一化度量，NeVA提升对齐效果，减少泄漏且通用能力降解更小 | — |
| 32 | [VISPA: Pluralistic Alignment via Automatic Value Selection a...](http://arxiv.org/abs/2601.12758) | 提出无训练的VISPA多元对齐框架，通过动态选择与内部激活引导控制价值表达 | 验证该框架在多元对齐任务上性能优异适配性强，为多元对齐提供可扩展路径 | — |
| 33 | [RISER: Orchestrating Latent Reasoning Skills for Adaptive Ac...](http://arxiv.org/abs/2601.09269) | 提出即插即用的RISER框架，构建可复用推理向量库，用轻量路由动态组合适配输入推... | 在七个基准获得平均3.4-6.5%的零样本准确率提升，比CoT令牌效率高2-3倍... | — |
| 34 | [Selective Safety Steering via Value-Filtered Decoding](http://arxiv.org/abs/2605.14746) | 提出基于价值安全准则过滤token的测试时引导方法，用单个阈值控制误干预概率边界 | 该方法在多组实验中优于现有基线，实现安全性、有用性与基模型相似度的更优平衡 | — |
| 35 | [From Helpfulness to Toxic Proactivity: Diagnosing Behavioral...](http://arxiv.org/abs/2602.04197) | 提出基于双模型困境驱动交互的新型评估框架，模拟分析多步行为轨迹中的代理行为 | 证实毒性主动性是普遍现象，揭示其两种主要趋势，构建了跨场景的系统化评估基准 | — |
| 36 | [Beyond Forgetting: Machine Unlearning Elicits Controllable S...](http://arxiv.org/abs/2601.21702) | 从线性表征假设视角出发，重新研究表征误导类大语言模型机器遗忘方法，分析其额外特性 | 通过多类任务验证相关假设，指出机器遗忘可带来可控侧行为与更强能力，明确该现象的双... | — |
| 37 | [MSRS: Adaptive Multi-Subspace Representation Steering for At...](http://arxiv.org/abs/2508.10599) | 提出MSRS框架，为各属性分配正交子空间减少干扰，结合混合子空间与词元级动态引导 | 显著降低属性冲突，性能超越现有方法，可有效泛化到多种不同下游任务 | — |
| 38 | [The Blessing and Curse of Dimensionality in Safety Alignment](http://arxiv.org/abs/2507.20333) | 对不同规模模型的各类概念线性子空间做可视化，通过降维投影消除危险线性结构 | 证实降维可显著降低大模型被越狱攻击的风险，给出线性越狱方法的相关理论见解 | — |
| 39 | [Misaligned Roles, Misplaced Images: Structural Input Perturb...](http://arxiv.org/abs/2504.03735) | 提出不修改查询内容、操纵输入结构的角色模态攻击，用对抗训练提升模型鲁棒性 | 发现攻击可组合得到更强攻击，提出的方法可降攻击成功率且保留模型通用效用 | — |
| 40 | [Representation Engineering for Large-Language Models: Survey...](http://arxiv.org/abs/2502.17601) | 形式化表征工程的目标与方法，利用对比输入样本检测编辑大模型高层概念表征 | 梳理出新兴学科表征工程的完整研究图景，对比替代方法并梳理出该方向存在的风险 | — |
| 41 | [Efficient Safety Retrofitting Against Jailbreaking for LLMs](http://arxiv.org/abs/2502.13603) | 基于直接偏好优化DPO，利用自建多主题多攻击风格的数据集对大模型进行安全改造 | 构建多主题多攻击风格的安全数据集，低成本降低越狱攻击成功率，开放相关数据与模型 | — |
| 42 | [SafeSwitch: Steering Unsafe LLM Behavior via Internal Activa...](http://arxiv.org/abs/2502.01042) | 提出SafeSwitch动态框架，利用基于探针的内部状态监测检测有害意图，仅在必... | 有害查询中降低约80%有害输出，仅微调不到6%参数，兼顾安全与效用，达到帕累托最... | ✅ |
| 43 | [Differentially Private Steering for Large Language Model Ali...](http://arxiv.org/abs/2501.18532) | 提出带有差分隐私保证的PSA私有引导对齐算法，为大语言模型激活编辑提供隐私保护 | 首次研究私有数据集下的大语言模型对齐，提出隐私算法，开发出专用的成员推断攻击方法 | — |
| 44 | [Robust LLM safeguarding via refusal feature adversarial trai...](http://arxiv.org/abs/2409.20089) | 基于对抗攻击的拒绝特征消融机制，提出ReFAT算法，通过RFA模拟输入攻击开展高... | 提出ReFAT算法，显著提升多款常用大模型对抗鲁棒性，计算开销远低于现有同类方法 | — |
| 45 | [Unlocking Decoding-time Controllability: Gradient-Free Multi...](http://arxiv.org/abs/2408.05094) | 提出MCA方法，为每个对齐目标构建专家与对抗提示，解码阶段通过对比结合平衡各目标 | 验证该方法优于已有方法，可在不同对齐目标间获得分布良好的帕累托前沿 | — |
| 46 | [Refusal in Language Models Is Mediated by a Single Direction](http://arxiv.org/abs/2406.11717) | 在多个开源聊天模型中定位拒绝介导的一维方向，提出白盒越狱方法并开展机制分析。 | 发现拒绝行为的介导机制，提出微创白盒越狱方法，揭示当前安全微调方法的脆弱性。 | — |
| 47 | [Represented Is Not Computed: A Causal Test of Candidate Algo...](http://arxiv.org/abs/2605.22488v1) | 以基位提取算术任务训练Transformer，结合线性探针、因果测试和稀疏电路搜... | 区分了算法中间量的表示与实际使用，指出探针结论可与因果观测产生显著分歧 | — |
| 48 | [Interpreting and Enhancing Emotional Circuits in Large Visio...](http://arxiv.org/abs/2605.21980v1) | 引入基于导向向量的因果归因框架，构建专用数据集解析大模型情感回路机制 | 发现情感回路功能解耦现象，提出调节方法，实验证实可提升性能缓解情感幻觉 | — |
| 49 | [Manifold-Guided Attention Steering](http://arxiv.org/abs/2605.21770v1) | 提出轨迹感知的MAGS方法，学习正确性低维子空间，推理时监测偏离并做靶向投影校正 | 在多类任务基准上性能优于基线与静态方法，证明正确性流形是LLM注意力几何的通用特... | — |
| 50 | [Latent-space Attacks for Refusal Evasion in Language Models](http://arxiv.org/abs/2605.21706v1) | 将拒止抑制重建模为针对线性探针的隐空间规避攻击，提出带优化置信度的可控隐空间规避... | 在15种不同类型模型上取得最优攻击成功率，优于现有拒止消融基线与专用越狱攻击 | — |
| 51 | [LLM Pretraining Shapes a Generalizable Manifold: Insights in...](http://arxiv.org/abs/2605.20449v1) | 通过线性探测、低秩分析、子空间对齐等方式，探究大语言模型到时间序列的跨模态迁移机... | 提出大语言模型到时间序列迁移的几何解释，揭示了预训练与微调各自的作用机制。 | — |
| 52 | [Adaptive Probe-based Steering for Robust LLM Jailbreaking](http://arxiv.org/abs/2605.20286v1) | 利用模型提取思想引导学习的引导向量逼近理想向量，基于对比激活统计自适应调整引导强... | 所提方法无需额外对比提示与手动调参，大幅提升探针引导越狱的有效性和鲁棒性 | — |

## 常见基线方法

- **线性干预方法** (1 篇引用)
- **指令微调Instruct模型** (1 篇引用)
- **提示级防御** (1 篇引用)
- **八个开源全模态大语言模型** (1 篇引用)
- **Gemini 3.1 Pro** (1 篇引用)
- **对比发现特征法** (1 篇引用)
- **语义搜索特征法** (1 篇引用)
- **授权上下文提示** (1 篇引用)
- **可逆拒绝方向激活投影** (1 篇引用)
- **表示控制投影** (1 篇引用)

## 本周提到的 Limitations

- 现有语言模型电路缺乏任务特异性，难以有效支撑对模型行为的靶向理解与干预
- 可解码故障信号无法通过固定线性引导实现校正，仍未找到有效的故障校正利用方法
- 该信号并非通用，仅在结构化领域可靠，事实类提示不存在可靠的几何信号
- 现有多价值对齐方法需按价值组合单独训练，成本极高，价值冲突会大幅降低对齐性能
- 表征工程目前存在性能下降、计算时间增加、模型可控性不佳等问题
- 现有拒止规避方法仅停留在决策边界，未将表征进一步推至模型回答的合规区域

## 常用数据集

- **POPE-adversarial** (1 篇使用)
- **AMBER** (1 篇使用)
- **IMAVB** (1 篇使用)
- **多模态安全基准数据集** (1 篇使用)
- **通用效用基准数据集** (1 篇使用)
- **Security-AR** (1 篇使用)
- **摘要未提及** (1 篇使用)
- **MATH** (1 篇使用)
- **MMLU-Pro** (1 篇使用)
- **竞争性编程** (1 篇使用)


---

*自动生成于 2026-05-24 | Research Radar*