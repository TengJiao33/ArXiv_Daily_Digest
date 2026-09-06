# 编辑可靠性与行为控制 — 2026-W36 (08/31-09/06)

本周新增 **58** 篇论文，**5** 篇附带代码。优先级：high 26 / medium 16 / low 16。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLM...](http://arxiv.org/abs/2609.01161v1) | evaluation/benchmark | 不同干预层级对应不同合规-效用权衡，DPO几乎消除字面泄露，但在LLaMA-3.1-8B上会... | 构建统一协议的跨层级评测基准，对比不同层级干预对大模型版权泄露行为的控制效果。 | 现有版权防御方法无法平衡合规性与模型可用性，部分方法会引发高比例... | ✅ |
| 2 | high | - | [Latent Mechanisms of Language Control in Multilingual Language M...](http://arxiv.org/abs/2609.00325v1) | model steering | 三种方法筛选出的语言控制潜在子集互不重叠但各自功能完整，语言控制存在冗余性，不存在单一规范语... | 通过从跨层transcoder识别语言控制相关潜在维度，对其开展定向干预，实现对... | 仅在中小规模多语言模型上验证，未测试更大规模模型，结论的通用性有... | ✅ |
| 3 | high | - | [SCoNE: Selective Context-aware Neuron Editing for Robust Retriev...](http://arxiv.org/abs/2609.00689v1) | model steering | 仅通过少量样本挖掘、选择性增强符合条件的FFN神经元，无需微调就能有效提升RAG抗检索噪声的... | 通过识别高归因、高交叉输入变异性的上下文感知FFN神经元，选择性增强对应神经元，... | 仅在标准问答基准验证，未测试真实复杂场景泛化性，方法普适性与潜在... | ✅ |
| 4 | high | - | [ALTSTEER: Selective Safety Steering for Moving Beyond Hard Refus...](http://arxiv.org/abs/2608.30197v1) | model steering | 在Llama-3.1和Qwen2.5上，ALTSTEER可保留良性请求效用，改善原本易生成短... | 在推理阶段利用模型内部拒绝相关信号决定干预时机，通过分阶段激活引导将生成转向建设... | 依赖模型内部拒绝相关信号，信号稳定性未经过多场景充分验证，缺乏大... | — |
| 5 | high | - | [ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Us...](http://arxiv.org/abs/2608.30685v1) | evaluation/benchmark | 双视角诊断评估可有效定位工业工具使用智能体缺陷，在线实验同时提升用户参与度、业务指标和人工审... | 通过双视角诊断评估输出结构化反馈，支撑智能体策略优化，改进工业工具使用智能体的服... | 评估依赖特定业务的真实日志校准，通用性不足，切换业务场景需要重新... | — |
| 6 | high | - | [Controlling Refusal Behavior of LLMs via Stiefel-Constrained Rot...](http://arxiv.org/abs/2608.30986v1) | model steering | 基于施蒂费尔约束的自包含旋转引导方案，相比依赖辅助构造的现有方法干预效率更优，核心设计对效果... | 通过在激活空间学习满足施蒂费尔约束的参数高效旋转变换，推理时引导模型，控制大语言... | 未给出具体评测基准与副作用分析，方法在实际场景中的可靠性尚未得到... | — |
| 7 | high | - | [Do VLMs Share Safety Neurons Across Modalities?](http://arxiv.org/abs/2608.30750v1) | unlearning/safety | VLM文本安全仅集中在约88个神经元，而视觉安全在单神经元层面高维弥散，需要至少50个子空间... | 通过神经元层面的因果分析揭示VLM安全机制，构建基准为后续VLM安全行为控制提供... | 仅停留在机制分析层面，未提出可落地的VLM安全防护改进方案。 | — |
| 8 | high | - | [EvoUndo: Recoverability-Constrained Self-Evolution for LLM Agent...](http://arxiv.org/abs/2608.28363v1) | agent harness | 扩展恢复语言可将预言机恢复率从24.4%提升至97%，精确寻址可将原语言下恢复率从0提升至7... | 通过协同设计可恢复性验证、状态接地、恢复语言表达能力，保障代理自修改的可回滚性与... | 自修改出现异常后无法安全回滚到原有状态，不可控持久影响会严重降低... | — |
| 9 | high | - | [From Reweighting to Rewriting: Unlocking the Intervention Effect...](http://arxiv.org/abs/2609.02771v1) | model steering | 相同影响力样本下，响应重写可产生更强、更持久的双向行为偏移，重加权效果弱且不稳定。 | 通过识别训练数据中的影响力样本，修改目标样本的响应标注而非调整权重，实现更有效的... | 该方法需要访问并修改训练数据，闭源模型难以应用，跨场景泛化性尚未... | — |
| 10 | high | - | [GAPS: Dimension-Level Gates for Conditional Activation Steering](http://arxiv.org/abs/2609.01878v1) | model steering | 固定能力预算下，DSAS结合GAPS可将Gemma-3的毒性率从6.52%降至0.48%，远... | 通过维度级门控筛选需要干预的神经元，仅对符合条件的神经元施加激活引导，抑制模型不... | 仅在4B及以下参数规模的模型上验证，未测试更大参数模型，方法通用... | — |
| 11 | high | - | [How Do Language Models Choose Between Context and Memory?](http://arxiv.org/abs/2609.00753v1) | model steering | 本文干预可复现30%-68%的权威诱导偏移，跨任务迁移仅缩小9%权威差距，任务内局部方向可缩... | 通过估计权威方向、交换匹配提示间坐标的反事实干预，检验激活方向调控模型信息源选择... | 权威方向依赖具体任务无法跨任务复用，通用模型行为调控的可靠性存在... | — |
| 12 | high | - | [Influence Is Not Authority: When Causal Guardrail Signals Make L...](http://arxiv.org/abs/2608.29942v1) | evaluation/benchmark | 24个测试案例中，Llama与Gemma评分器均将合法输入来源迁移判定为攻击，该偏移的平均幅... | 提出授权等价审计方法评测现有因果护栏的误判缺陷，指出参考构建与路由是安全决策的核... | 现有因果护栏误报率高，会不必要干预合法工具使用，降低系统效用，增... | — |

## 方法族分布

- **evaluation/benchmark**：22 篇
- **model steering**：13 篇
- **other**：9 篇
- **unlearning/safety**：5 篇
- **agent harness**：3 篇
- **policy optimization**：2 篇
- **survey**：2 篇
- **reward learning**：1 篇
- **multi-agent coordination**：1 篇

## 失败模式与风险信号

- LLM代理自演化产生的修改无法回滚，留下不可逆转的持久异常影响
- 小骨干LLM智能体容易漂移进入持续失效模式
- 跨模态冲突下，模型后层依赖内部偏好先验，弱锚定输入信息，导致组合泛化失败
- 关键必要上下文缺失后，模型不遵守弃权要求，过度依赖先验知识强行输出答案
- 传统LLM裁判式安全评估仅观测生成行为，无法揭示底层安全机制的隐藏脆弱性，易受评分流程干扰。
- 后训练目标改进易引发原有任务性能退化，全量重训成本高不符合工业预算约束。
- 现有旋转引导的拒绝行为控制方法依赖拒绝向量等额外辅助构造
- 现有VLM对齐未闭合视觉安全缺口，视觉安全的弥散结构导致安全防护难度更高。
- 现有外部安全护栏推理成本高、安全信号延迟、与底座模型能力不匹配
- 最终结果评估掩盖缺陷位置，长期交互服务偏离早期交互上下文

## 评测信号

- 不同设计方案下失败自修改的恢复成功率，验证了两个核心瓶颈对可恢复性的实际影响幅度。
- 相同成本下相比三类基线路由方法成功率提升7.4-11.1个百分点，在两个基准上取得最高留外成功率。
- 跨模态冲突下，多个VideoLLaMA 2配置精度接近随机，现成InternVideo2准确率下降32.3%，指令跟随失败增加17.3%
- 评测三个前沿大模型在关键上下文缺失后的行为，发现模型极少在信息不足时弃权，仍经常输出答案
- 通过SafetyAUC结合自助法置信区间，可统计显著区分不同安全强度的模型，捕获不同量化等级的安全效果差异。
- 代码生成基准的pass@1/pass@3获得统计显著提升，内部数学任务的性能退化控制在预设容忍范围内。
- 验证了所提旋转引导方案相比依赖辅助构造的现有方法干预效率更优，同时验证了核心设计选择的重要性。
- 不同干预未带来交互模式的显著差异，未检测到干预有害影响，主动干预组满意度有提升趋势。
- 通过目标消融实验分析不同干预对VLM拒绝有害请求能力的影响，对比文本与视觉安全的结构差异。
- 在评测中性能优于参数量更大的独立护栏与专用幻觉检测器，仅约2M参数，额外推理开销低于0.5%。

## 控制机制 / Harness 信号

- 通过协同设计可恢复性验证、状态接地、恢复语言表达能力，保障代理自修改的可回滚性与可靠性。
- 通过学习基于累积轨迹和删失监督的切换策略，择机切换到大模型骨干，兼顾成本与智能体可靠性。
- 本文未提出模型行为控制改进方案，仅开展失败模式分析与机制定位，为后续研究提供基础
- 通过构建专门评测框架量化模型上下文依赖程度，发现模型行为缺陷，为后续模型行为改进提供依据
- 本文未直接改进模型行为控制，提出无需外部裁判的安全识别评估协议，可比较不同模型与量化版本的安全能力。
- 通过收益工程设计的限定混合补丁，基于已有检查点做后训练改进，控制目标改进过程中原任务的性能退化。
- 通过在激活空间学习满足施蒂费尔约束的参数高效旋转变换，推理时引导模型，控制大语言模型的拒绝行为。
- 设置不同类型和干预强度的开发者-LLM交互调整方案，对照评估干预对交互体验的影响。
- 通过神经元层面的因果分析揭示VLM安全机制，构建基准为后续VLM安全行为控制提供支撑。
- 复用大语言模型推理产生的内部隐藏状态，在token层级预测生成风险，基于风险分数指导约束安全解码。

## 可靠性 / 落地风险

- 自修改出现异常后无法安全回滚到原有状态，不可控持久影响会严重降低代理可靠性。
- 依赖教师标注删失干预时间，标注成本较高，需预先在开发集选择运行点，灵活性不足。
- 现有音视频大模型应对冲突多模态输入可靠性不足，易出现先验主导失效，影响应用稳定性
- 模型作答过度依赖自身先验记忆而非给定上下文，在要求基于上下文推理的任务中存在可靠性缺陷
- 该方法仅在有限模型和量化场景验证，通用性在更多安全场景尚未得到验证。
- 多轮补丁累积更新的长期效应未验证，零和混合设计可能带来潜在的长期性能风险。
- 未给出具体评测基准与副作用分析，方法在实际场景中的可靠性尚未得到充分验证。
- 研究对象为在读学生开发者，结论向工业界专业开发场景的推广性存在不确定性。
- 仅停留在机制分析层面，未提出可落地的VLM安全防护改进方案。
- 方法仅在自建基准与医学场景验证，跨不同底座模型、更多场景的泛化能力未充分验证

## 代码资源

- [Harness-of-Harness: Multi-Day Autonomous Software Development with Continual Imp...](https://github.com/Flesymeb/HarnessOfHarness) · 2 stars
- [Beyond Scores: Understanding LLM-as-a-Judge Mechanisms in Summarization Evaluati...](https://github.com/himil-v/judge-mech)
- [CopyShield: A Cross-Level Benchmark of Copyright Defenses in LLMs](https://github.com/spotai-mbzuai/CopyShield.git.)
- [SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Gen...](https://github.com/HYU-ARK-Lab/SCoNE.)
- [Latent Mechanisms of Language Control in Multilingual Language Models](https://github.com/rm-3284/Latent-Mechanism-Multilingual.)

## 常见基线方法

- **随机对照**：2 篇
- **常规修复策略**：1 篇
- **基于原恢复语言的确定性预言机方法**：1 篇
- **任务级路由**：1 篇
- **步级路由**：1 篇
- **固定前缀路由**：1 篇
- **VideoLLaMA 2-7B-AV**：1 篇
- **InternVideo2**：1 篇
- **LLM-as-judge安全评估方法**：1 篇
- **StrongREJECT grader行为评估**：1 篇

## 常用数据集

- **摘要未提及**：5 篇
- **600个未见单次自演化任务**：1 篇
- **ALFWorld**：1 篇
- **DABench**：1 篇
- **AVHBench**：1 篇
- **53道英国语言学奥林匹克谜题**：1 篇
- **StrongREJECT**：1 篇
- **XSTest**：1 篇
- **OKTest**：1 篇
- **CodeForces**：1 篇

---
*自动生成于 2026-09-06 | ArXiv_Daily_Digest*