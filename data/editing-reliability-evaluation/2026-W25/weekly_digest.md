# 编辑可靠性与行为控制 — 2026-W25 (06/15-06/21)

本周新增 **53** 篇论文，**5** 篇附带代码。优先级：high 14 / medium 22 / low 17。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [A Low-Rank Subspace Analysis of LLM Interventions](http://arxiv.org/abs/2606.14388v1) | model steering | 不同行为共享表征，干预影响不对称；行为子空间重叠越高，源子空间越靠近决策子空间，干预副作用越... | 通过分析LLM激活空间中行为子空间的几何特性，解释干预副作用的产生机制，为精准行... | 行为共享表征导致干预易产生非预期副作用，难以实现工业所需的精准靶... | — |
| 2 | high | - | [Auditing Machine Unlearning: A Systematic Research on Whether Mo...](http://arxiv.org/abs/2606.16110v1) | evaluation/benchmark | 基于去优化、Fisher/Hessian的方法都无法实现真正遗忘，重训练、微调类即使目标数据... | 提出基于无知证明的机器遗忘审计框架，识别未真正完成遗忘的算法，提升机器遗忘的可靠... | 现有多数机器遗忘方法无法真正遗忘，缺乏可靠审计会带来实际应用中的... | — |
| 3 | high | - | [Can Editing 1 Neuron Fix Repetition Loops in LLMs?](http://arxiv.org/abs/2606.13705) | model steering | Gemma模型长事实列举的重复循环发生率最高达95%，小模型仅编辑单个神经元即可修复且保留通... | 通过分层消融与神经元归因定位致病神经元，对目标参数执行静态权重编辑，抑制致病单元... | 仅对特定可定位的生成病理有效，无法解决知识缺失类问题，方法适用范... | — |
| 4 | high | - | [Capability Minimization as a Safety Primitive: Risk-Aware Causal...](http://arxiv.org/abs/2606.13884v1) | unlearning/safety | 基于反事实因果风险的门控策略，在匹配弃权率下大幅降低高成本误差，同时保留原策略大部分效用。 | 通过反事实因果风险估计对智能体决策做门控，推导满足安全约束的阈值，设计自适应策略... | 依赖因果路径建模假设，未在大规模真实LLM Agent任务中验证... | — |
| 5 | high | - | [Constitutional Value Potentials: reading and steering internal p...](http://arxiv.org/abs/2606.15420v1) | model steering | 价值冲突违规信号出现在答案生成初期，预测冲突违规AUROC最高达0.95，沿价值方向移动可按... | 在激活空间学习价值势能，基于势能差构建违规监测，通过沿价值方向移动引导模型调整价... | 仅在合成冲突场景验证，未在真实开放场景测试，实际通用性有待验证。 | — |
| 6 | high | - | [Creative Collision: Directorial Persona Steering and Competition...](http://arxiv.org/abs/2606.16240v1) | model steering | 斯皮尔伯格表征方向几乎在全插值范围压制斯科塞斯，两人人设均最大定位于40层Transform... | 推理阶段向Transformer残流叠加混合两个对立语义的激活引导向量，以此引导... | 仅在单个40层解码器Transformer上验证结论，结论的跨模... | — |
| 7 | high | - | [Dynamic Rollout Editing for Reducing Overthinking in RL-Trained ...](http://arxiv.org/abs/2606.17890v1) | policy optimization | GRPO训练初期，相同提示下成功轨迹的过度思考程度略高于失败轨迹，序列级信用分配会放大该初始... | 在GRPO训练过程中干预存在过度思考的成功轨迹，保留正确前缀、编辑多余内容，通过... | 方法仅适配GRPO类强化训练框架，未验证跨框架泛化性，缺乏大规模... | — |
| 8 | high | - | [Frame-Conditioned Moral Computation in LLaMA 3.1-8B-Instruct: A ...](http://arxiv.org/abs/2606.15507v1) | evaluation/benchmark | 发现情境锚定效应：大模型伦理能力基本稳定，伦理特征显著性高度依赖prompt框架，还找到跨温... | 通过机械可解释性审计分析大模型伦理推理的内部机制，提出行为对齐需补充机制对齐思路... | 仅测试54个prompt，样本量较小，结论通用性不足，未形成实际... | — |
| 9 | high | - | [GEMS: Geometric Constraints Enable Multi-Semantic Superposition ...](http://arxiv.org/abs/2606.19946v1) | model steering | 多方向叠加崩溃可分解为分布偏移和方向干扰两个独立来源，GEMS处理后GSM8K准确率达98%... | 推理阶段无需训练，通过对激活施加范数约束和实时正交化两类几何约束实现多方向语义引... | 仅验证了少量方向叠加的效果，未测试更多方向、更多任务下的方法稳定... | — |
| 10 | high | - | [Gaze Heads: How VLMs Look at What They Describe](http://arxiv.org/abs/2606.14703v1) | model steering | 不到9%的Top注视头做单注意力掩码干预就能以83.1%准确率 steering输出到指定区... | 通过机制分析识别出特定功能注意力头，在推理时施加注意力掩码干预，无需重训练即可 ... | 仅在部分VLM架构中生效，通用性不足，控制场景局限于图像描述任务... | — |
| 11 | high | - | [High-Dimensional Random Projection for Activation Steering in La...](http://arxiv.org/abs/2606.15092v1) | model steering | 高维随机投影后的激活加法，可捕获线性均值差方法无法得到的判别结构，性能提升且不增加显著计算开... | 通过高维随机投影将激活变换到高维空间，在投影空间执行激活加法，实现更有效的大语言... | 仅在通用基准验证性能，未验证该方法在下游任务中的长期调控可靠性与... | — |
| 12 | high | - | [Leverage Is Not Reach: A Control-Window Law for Single-Neuron St...](http://arxiv.org/abs/2606.19831v1) | model steering | 预测控制天花板平均绝对误差为0.14，大块层仅0.07；仅3/6的Llama枢纽在长输出范围... | 通过残差流与神经元写方向的对齐构建控制窗，基于该框架构建前向对比筛选，实现单神经... | 仅在少量神经元样本上验证，仅针对单神经元控制场景，多神经元协同场... | — |

## 方法族分布

- **model steering**：16 篇
- **evaluation/benchmark**：13 篇
- **other**：9 篇
- **tool-use control**：3 篇
- **unlearning/safety**：2 篇
- **policy optimization**：2 篇
- **factuality benchmark**：1 篇
- **未分类**：1 篇
- **survey**：1 篇
- **reward learning**：1 篇
- **skill generation**：1 篇
- **online distillation**：1 篇

## 失败模式与风险信号

- 部分冻结编码器架构的VLM不存在可用于控制的同类注视头集合
- 医疗MLLM推理中来源不明的分阶段幻觉错误
- LLM直接控制实验导致的不安全探索、性能不稳定
- 行为干预的非预期副作用，靶向行为控制难度大
- 模型输出自信却错误，引发下游高成本决策误差
- 视觉语言模型伪造视觉理解，虚高基准评测分数，无法反映真实能力
- 大语言模型幻觉、推理不透明、知识来源不透明
- 现有文化对齐忽略训练流程中文化信号流失，导致对齐缺乏数据基础
- 长事实列举生成陷入重复循环，长思考预算下出现无法收敛的末日循环
- 现有电路学习方法要么可解释性差，要么计算成本过高，难以扩展到高维SAE特征。

## 评测信号

- 指定区域描述重定向准确率达83.1%，随机头干预无法生效，全头干预会破坏模型生成质量。
- 聚焦医疗MLLM推理不同阶段的幻觉来源，评测修正特定阶段错误对最终回答质量的影响
- 对比不同架构的跨人群泛化、零样本迁移、微调后预测性能，量化了不同场景下的性能差异。
- CARE在两个基准上最终最优结果较公开基准 incumbent分别提升8.5和8.2，性能优于所有对比方法。
- 探究干预副作用大小与行为子空间重叠度、行为子空间和决策子空间夹角的相关性。
- 仅完成2型糖尿病场景的情景演示，未给出任何量化的评测结果信号。
- 在匹配弃权率下，RACG相比基线大幅降低高成本决策误差，同时保留原无门控策略的大部分效用。
- 验证了幻影行为可从VLM内部激活线性解码，成功区分出两种性质不同的幻影失败模式
- 通过专家多维度评估获取反馈，验证来源透明等设计要素对用户信任和有用性判断的影响。
- 观测到LLM后训练阶段文化信号的大幅下降趋势，验证了文化标记方法对下游文化基准性能的提升作用。

## 控制机制 / Harness 信号

- 通过机制分析识别出特定功能注意力头，在推理时施加注意力掩码干预，无需重训练即可 steering模型行为。
- 构建细粒度幻觉诊断基准定位幻觉来源，通过迹监督微调训练减少推理各阶段的幻觉错误
- 本研究为移动健康行为预测架构的基准比较研究，未涉及模型或agent行为控制相关内容。
- 设置可审计的公共证据干预门，默认保留非LLM优化路径，仅授权有证据支持的变更并留存日志。
- 通过分析LLM激活空间中行为子空间的几何特性，解释干预副作用的产生机制，为精准行为控制提供依据。
- 本文不涉及针对大语言模型或Agent的行为控制与改进。
- 通过反事实因果风险估计对智能体决策做门控，推导满足安全约束的阈值，设计自适应策略应对分布偏移。
- 通过提出探测框架与分类指数，区分幻影行为的不同失败模式，为后续针对性改进提供基础
- 采用来源优先的设计思路，通过突出证据可追溯性、结构化合成与交互支架，提升对话AI输出的可信度。
- 提出文化对齐需将研究焦点从推理时干预转向训练数据流水线优化，发布文化标记数据集支撑相关研究。

## 可靠性 / 落地风险

- 仅在部分VLM架构中生效，通用性不足，控制场景局限于图像描述任务。
- 仅针对医疗领域场景，未验证方法在通用大模型上的通用性，缺乏落地的可控性方案
- 本研究属于移动健康行为预测领域，与当前研究方向不相关，未涉及本方向的可靠性风险。
- 仅在封闭科学实验基准验证，未测试开放场景，方法的通用性有待进一步验证。
- 行为共享表征导致干预易产生非预期副作用，难以实现工业所需的精准靶向行为控制。
- 不属于LLM/Agent可靠性研究领域，未针对目标方向做任何可靠性相关验证。
- 依赖因果路径建模假设，未在大规模真实LLM Agent任务中验证泛化性
- 现有VLM评测无法识别幻影行为，得到虚高性能，容易误导模型研发迭代方向
- 仅开展小样本专家评估，样本量有限，结论的通用性和可推广性有待进一步验证。
- 文化信号流失会导致文化对齐偏向性，影响模型输出的文化可靠性，给对齐落地带来风险。

## 代码资源

- [ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM ...](https://github.com/alibaba-damo-academy/ClinHallu.) · 5 stars
- [Medical world models: representing medical states, modelling clinical dynamics a...](https://github.com/1999kevin/awesome_medical_world_models.) · 4 stars
- [The Quality-Utility Paradox: Why High-Reward Data Impairs Small Model Mathematic...](https://github.com/Dracoqhl/Quality-Utility-Paradox.)
- [DifFRACT: Diffusion Feature Reconstruction and Attribution for Circuit Tracing](https://github.com/Artalmaz31/DifFRACT)
- [Is Code Better Than Language for Algorithmic Reasoning](https://github.com/TerryTong-Git/ToolProj.)

## 常见基线方法

- **随机注意力头干预**：1 篇
- **全注意力头干预**：1 篇
- **统计基线**：1 篇
- **TCN**：1 篇
- **MLP**：1 篇
- **Transformer**：1 篇
- **PatchTST**：1 篇
- **TimesFM**：1 篇
- **公开现有非LLM优化器**：1 篇
- **其他对比方法**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **漫画分镜测试集**：1 篇
- **COCO自然图像数据集**：1 篇
- **ClinHallu**：1 篇
- **三个公开移动健康行为时间序列数据集**：1 篇
- **Minerva/Olympus**：1 篇
- **ChemLex**：1 篇
- **模拟干预场景**：1 篇
- **真实世界决策基准**：1 篇
- **城市级循环性评估可持续发展报告**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*