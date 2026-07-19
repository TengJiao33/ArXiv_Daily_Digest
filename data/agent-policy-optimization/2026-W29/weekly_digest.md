# Agent 策略优化与在线蒸馏 — 2026-W29 (07/13-07/19)

本周新增 **50** 篇论文，**4** 篇附带代码。优先级：high 29 / medium 15 / low 6。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [SCALECUA: Scaling Computer Use Agents with Verifiable Task Synth...](http://arxiv.org/abs/2607.11185) | policy optimization | ScaleCUA在OSWorld达到68.7%、ScienceBoard达到54.0%，训练... | 通过可验证任务合成获取训练数据，结合前沿采样与视觉上下文分割优化在线RL训练，提... | 需要百级并发工作节点生成训练数据，流程复杂度高，工业落地部署成本... | ✅ |
| 2 | high | - | [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforce...](http://arxiv.org/abs/2607.14777v1) | online distillation | SEED让辅助蒸馏监督随策略共同进化，始终与当前轨迹分布对齐，在未见场景也能稳定提升性能。 | 通过自进化从已完成同策略轨迹提取事后技能，转化为密集蒸馏信号，联合强化学习优化策... | 未在具体主流基准任务上验证，技能提取质量依赖当前策略的现有水平。 | ✅ |
| 3 | high | - | [To Answer or to Abstain: Mitigating Search-Agent Hallucinations ...](http://arxiv.org/abs/2607.10738v1) | reward learning | AWA-RL相比非弃权基线，最高提升绝对精度10.3%，RA-F1提升2.9%，仅小幅牺牲原... | 通过设计感知弃权的奖励函数，利用强化学习优化搜索Agent策略，惩罚编造回答缓解... | 仅在开放域问答任务验证，未测试更多复杂搜索场景，方法泛化能力未得... | ✅ |
| 4 | high | - | [A Learning-Rate-Gated Failure of GRPO in a Small Language and Vi...](http://arxiv.org/abs/2607.12640) | policy optimization | GRPO仅在任务还有提升空间时生效，中高学习率会引发退化甚至崩溃，失效具有小模型尺度依赖性。 | 控制学习率、KL权重、种子、初始化等多个变量，开展对照实验分析GRPO对智能体性... | GRPO微调小模型智能体时，学习率选择不当会导致已有能力退化，存... | — |
| 5 | high | - | [ARMOR: Stabilizing On-Policy LLM RL with Off-Policy Anchor Sampl...](http://arxiv.org/abs/2607.10481v1) | policy optimization | 现有标准反向KL正则化无法保证参考分布的全面覆盖，不足以解决LLM同策略RL的过优化不稳定问... | 通过引入离策略参考策略的锚点样本，重构策略优化目标，抑制模型过优化，稳定训练过程... | 依赖额外的离策略参考数据，增加了训练的存储开销与计算成本。 | — |
| 6 | high | - | [AgentKGV: Agentic LLM-RAG Framework with Two-Stage Training for ...](http://arxiv.org/abs/2607.09092v1) | policy optimization | 两阶段训练相比单轮RAG提升macro-F1达9.4个百分点，GRPO将平均搜索调用次数从3... | 通过轮级蒸馏将大模型推理能力迁移到小模型，使用GRPO优化搜索策略，减少冗余检索... | 仅在单一公开基准完成测试，未在复杂真实工业知识图谱场景验证落地效... | — |
| 7 | high | - | [Agentic-DPO: From Imitation to Agentic Policy Optimization on Ex...](http://arxiv.org/abs/2607.10601v1) | policy optimization | 9B参数模型在tau-bench上准确率从SFT的21.7%提升至41.4%，效果匹配在线G... | 将专家轨迹转化为状态条件动作偏好，用DPO风格偏好目标对比优化，引导智能体规避错... | 方法完全依赖专家轨迹，性能受轨迹质量影响大，未验证开放复杂环境的... | — |
| 8 | high | ICML 2026 | [Beyond Euclidean Clipping: Overcoming Exploration Collapse in LL...](http://arxiv.org/abs/2607.10169v1) | policy optimization | PPO-Clip用欧几里得度量衡量策略差异，与策略黎曼流形几何不匹配是探索崩溃的根源，RIP... | 通过修正策略更新的度量适配策略黎曼流形固有几何，提出新的策略优化方法平衡探索与利... | 依赖黎曼流形相关计算，算法复杂度高于传统PPO类方法，训练成本更... | — |
| 9 | high | - | [Branching Policy Optimization: Sandbox-Native Language Agent Rei...](http://arxiv.org/abs/2607.14171v1) | policy optimization | BPO相比GRPO和RLOO，同等计算下成功率提升3.6-6.1个百分点，梯度范数方差减半，... | 通过改进强化学习的采样拓扑与优势估计方法，降低梯度方差，提升语言智能体的训练效率... | 方法依赖沙箱具备可快照、确定性的特性，在不满足该条件的环境中通用... | — |
| 10 | high | - | [Demystifying On-Policy Distillation: Roles, Pathologies, and Reg...](http://arxiv.org/abs/2607.13399v1) | online distillation | 同策略蒸馏的效果完全取决于引导信号质量而非教师规模，存在师生不匹配、长度利用两类病态。 | 通过优势裁剪与对数压缩两种轻量信号调控，优化同策略蒸馏引导信号质量，规范学生模型... | 仅在通用基准验证，未提及实际场景适配，调控方法的泛化性尚不明确。 | — |
| 11 | high | - | [EasyOPD: An Easy-to-use On-Policy Distillation Framework for Lar...](http://arxiv.org/abs/2607.11012v1) | online distillation | 基于同一verl后端实现的多种同策略蒸馏方法可正常运行，同时保留各自方法特性与对应任务的性能... | 通过统一模块化的同策略蒸馏框架，分离各模块职责，支持多种同策略蒸馏方法的复现与扩... | 未在大规模真实复杂agent场景验证框架的性能与稳定性，通用性有... | — |
| 12 | high | - | [EvoCUA-1.5: Online Reinforcement Learning for Multi-turn Compute...](http://arxiv.org/abs/2607.09773) | policy optimization | 所提组件可提升训练稳定性，在OSWorld-Verified取得63.2%成功率，超越同规模... | 基于可验证任务结果获取奖励信号，通过策略优化和自适应课程学习改进智能体策略，提升... | 在线训练需要反复与沙箱环境交互，环境反馈速度慢，整体训练的时间与... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **policy optimization**：20 篇
- **online distillation**：8 篇
- **reward learning**：6 篇
- **other**：3 篇
- **evaluation/benchmark**：3 篇
- **unlearning/safety**：2 篇
- **tool-use control**：2 篇
- **model steering**：1 篇
- **consistency detection**：1 篇
- **knowledge distillation**：1 篇
- **agent harness, evaluation/benchmark, policy optimization**：1 篇
- **知识蒸馏**：1 篇

## 失败模式与风险信号

- 欺诈崩塌，异常检测陷入零召回陷阱
- 奖励窃取，代理奖励提升但实际任务性能下降，RL优化会产生新的失败样本
- prompt格式不当会导致推理正确却无法输出指定格式的答案选项
- 长多智能体轨迹下过程奖励模型计算开销过高
- 文档级检索表层形式不匹配，大规模场景下检索冗余、部署成本高
- 稀疏最终奖励无法为推理过程提供有效反馈，无法区分不同质量的推理路径
- 现有方法将单轨迹分数广播到所有轮次，导致多轮越狱学习的信用错配问题
- 现有同策略蒸馏实现碎片化，不同方法差异大，存在难以复现、不易扩展的问题
- 原有基于比率的方向判定与散度变化符号不一致，干扰强化学习训练过程。
- 动作级过滤无法消除合成训练数据引入的隐性错对齐，通用安全基准无法识别该风险。

## 评测信号

- 在两个金融数据集上验证，该方法打破零召回陷阱，少数类召回优于标量化基线，可牺牲有限运营摩擦提升异常发现能力。
- 测试不同奖励设计、RL算法、模型规模下的奖励窃取率变化，验证不同验证方式对窃取的抑制效果
- 在ImageCLEF 2026留存测试集上准确率达84.1%，登顶Visual MCQ排行榜，明确了不同测试时缩放方案的性能差异。
- 性能匹配或优于基线的同时，最高可减少5000倍评分FLOPs、37倍延迟、34倍单序列内存占用
- 在T-REx基准长尾测试集上，相比单轮RAG提升macro-F1 9.4个百分点，检索调用量减半且精度不下降
- 所得码长较基线缩短多个数量级，给出的泛化界性能优于零误差训练后量化得到的泛化界。
- 验证了稠密奖励可提升推理准确率、降低token开销，且该增益与现有RLVR策略更新方法互补。
- 动态、静态加权DC-GRPO的ASR5@3分别达98.26%和97.88%，大幅优于现有SOTA的86%左右水平。
- 验证了基于统一后端实现的多种同策略蒸馏方法，可保留原有方法的目标与对应任务的性能表现。
- 8B规模Qwen3-8B在Terminal-Bench 2.0取得12%通过率，为同规模RL训练模型最优，DeepSeek-V4-Flash通过率提升3-4个百分点。

## 控制机制 / Harness 信号

- 通过设计解耦金融效能、运营摩擦等目标的向量奖励，映射帕累托前沿动态调整agent决策，平衡不对称成本。
- 提出NRFR指标量化奖励窃取带来的新增失败，分析不同设置下的窃取规律，指导设计可靠的奖励与验证器
- 通过调整测试时解码预算、prompt格式，引入标准答案提示与引导修复步骤，优化小VLM的测试时缩放效果。
- 通过复用生成阶段KV缓存的高效过程奖励建模，降低多智能体测试时扩展的计算开销，提升系统运行效率。
- 通过轮级蒸馏将大模型推理能力迁移到小模型，使用GRPO优化搜索策略，减少冗余检索，提升性能与部署效率。
- 本文聚焦模型压缩与泛化性分析，不涉及对Agent或模型行为的显式控制与改进。
- 通过分阶段设计稠密化奖励信号，在成功前后分别为推理路径提供反馈，优化大语言模型推理策略。
- 通过设计轮级分解的信用分配规则改进群体相对策略优化，提升多轮越狱攻击模型的成功率。
- 通过统一模块化的同策略蒸馏框架，分离各模块职责，支持多种同策略蒸馏方法的复现与扩展。
- 通过统一验证机制生成难度自适应、多样性充足的规模化终端训练环境，为终端智能体强化学习训练提供可靠支撑。

## 可靠性 / 落地风险

- 仅在两个公开数据集验证，未验证大规模真实工业场景，泛化能力不明确。
- 不完美奖励会引发大量奖励窃取，高奖励不对应高性能，严重影响MLLM对齐的实际可靠性
- 复杂测试时缩放方法计算成本远高于简单方法，但性能反而更差，效果提升高度依赖基础模型。
- 仅在数学推理任务验证，方法在其他类型多智能体任务的通用性尚未验证
- 仅在单一公开基准完成测试，未在复杂真实工业知识图谱场景验证落地效果。
- 未在实际落地场景验证压缩效果，缺乏部署相关测试，对工业落地的支撑不足。
- 仅在数学推理任务验证，方法在其他类型任务上的泛化性未得到验证。
- 该越狱攻击方法可能被恶意利用，会给大语言模型的应用安全带来潜在风险。
- 未在大规模真实复杂agent场景验证框架的性能与稳定性，通用性有待进一步验证。
- 仅在单个基准完成验证，合成环境的分布外泛化能力未验证，落地应用存在不确定性。

## 代码资源

- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://github.com/jinyangwu/SEED.) · 56 stars
- [SCALECUA: Scaling Computer Use Agents with Verifiable Task Synthesis and Efficie...](https://github.com/THUDM/SCALE-CUA.) · 18 stars
- [Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?](https://github.com/GAIR-Lab/Light-MER.) · 5 stars
- [To Answer or to Abstain: Mitigating Search-Agent Hallucinations via Abstention-A...](https://github.com/zfj1998/AWA-RL.)

## 常见基线方法

- **RLOO**：2 篇
- **自一致性**：2 篇
- **多数投票**：2 篇
- **GRPO**：2 篇
- **标量化基线**：1 篇
- **SFT基线**：1 篇
- **DAPO**：1 篇
- **PRM引导束搜索**：1 篇
- **无训练生成评判器**：1 篇
- **训练式多模态PRM**：1 篇

## 常用数据集

- **数学推理基准**：3 篇
- **GSM8K**：2 篇
- **科学推理基准**：2 篇
- **数学推理任务**：2 篇
- **ALFWorld**：2 篇
- **电商欺诈数据集**：1 篇
- **UCI信用卡数据集**：1 篇
- **安全视觉问答(safety VQA)**：1 篇
- **图表视觉问答(chart VQA)**：1 篇
- **EXAMS-V**：1 篇

---
*自动生成于 2026-07-19 | ArXiv_Daily_Digest*