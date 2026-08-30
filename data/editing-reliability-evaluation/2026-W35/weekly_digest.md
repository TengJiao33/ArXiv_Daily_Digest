# 编辑可靠性与行为控制 — 2026-W35 (08/24-08/30)

本周新增 **61** 篇论文，**4** 篇附带代码。优先级：high 30 / medium 16 / low 15。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debia...](http://arxiv.org/abs/2608.25375v1) | model steering | GGSS在4种生成式VLM上平均偏差最低，3个骨干网络统计显著，MMStar精度仅波动在±0... | 在推理阶段通过测地门控球面引导校正带偏差的视觉令牌，实现生成结果去偏，同时保留模... | 仅在4种生成式VLM上验证，未测试更多架构与真实场景的泛化能力。 | ✅ |
| 2 | high | - | [INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment](http://arxiv.org/abs/2608.27348v1) | tool-use control | 调用意图工具的概率可提供无裁判的细粒度行为信号，能补充CoT监测，识别推理过程中在线干预的关... | 通过添加面向意图的专用工具获取模型行为倾向的细粒度信号，监测失对齐并识别可在线干... | 未披露跨场景泛化测试结果，方法的实际稳定性未验证，落地效果不明确... | ✅ |
| 3 | high | - | [A Judge Should Know What Changed:Construct Validity for LLM-as-a...](http://arxiv.org/abs/2608.24419v1) | evaluation/benchmark | 当不变性S≥0.90时，LLM裁判平均S=0.945但构念敏感性R仅0.319，超五成公开标... | 通过提出构念效度的二维评测框架，暴露现有评估缺陷，为提升LLM裁判评估可靠性提供... | 现有LLM裁判评估构念效度不足，高一致性不代表评估有效，评测结果... | — |
| 4 | high | - | [Adaptive Triggering for Bias Correction in LLM Reasoning](http://arxiv.org/abs/2608.25379v1) | model steering | 自适应黑盒触发可恢复固定间隔干预损失的大部分消歧精度，且干预次数大幅减少，白盒信号会降低多数... | 通过在线变点检测动态判断推理过程中的偏差，仅当累计偏差过阈值才注入修正，支持白盒... | 白盒信号对偏差的分辨能力不足，会损害正常推理的精度，白盒方案适用... | — |
| 5 | high | - | [Beyond End-to-End Success: Diagnosing Failures in Long-Horizon S...](http://arxiv.org/abs/2608.20563v1) | evaluation/benchmark | Gemini 2.5 Flash多数失败发生在目标状态观测前，添加引导可将状态观测率从65.... | 通过构建带检查点的诊断评测框架定位失败位置，为改进长周期智能体可靠性提供反馈依据... | 仅提出诊断框架未给出改进方案，结论仅在两个Gemini模型验证，... | — |
| 6 | high | - | [CARD: Diagnosing Belief to Action Routing Failures in Vision Lan...](http://arxiv.org/abs/2608.20763v1) | evaluation/benchmark | 开放权重VLMs存在关键路由失效，无法将内部已有的协作伙伴信念表征融入下一步动作预测，浪费了... | 通过激活steering控制模型沿特定轴的激活，以此诊断信念到动作预测的路由问题... | 仅完成失效诊断未提出解决方案，仅在自制基准验证，方法泛化性未得到... | — |
| 7 | high | - | [Calibrating Criterion Revision in LLM Agents: Failure Modes and ...](http://arxiv.org/abs/2608.20729v1) | evaluation/benchmark | 本次全部模型测试均不满足准则修订的五个条件，Qwen2.5-7B可在无修订状态下完成迁移与保... | 通过设计带明确约束的评测框架，提出轨迹锚定协议，提升对Agent准则修订行为评测... | 现有评测方案区分度不足，无法有效判定Agent是否真正完成了准则... | — |
| 8 | high | - | [Claim-Level Confidence Calibration for Reliable Decision Making ...](http://arxiv.org/abs/2608.22483v1) | evaluation/benchmark | 声明级分解结合事后校准可降低事实问题的预期校准误差，但在对抗假前提问题上存在失效。 | 通过对输出分解为原子声明做事后置信校准，对低置信度内容触发选择性干预，提升决策环... | 需要分解原子声明、多次采样获取一致性信号，推理成本较高，对抗场景... | — |
| 9 | high | - | [Coalition-Aware Skill Reliability for Self-Evolving Agents](http://arxiv.org/abs/2608.22610v1) | agent harness | 自进化智能体技能库存在联盟污染、跨域技能效用反转两类常见可靠性失效，孤立评估存在局限。 | 在技能累积阶段选择联盟感知的可靠技能，迁移后掩码无用负向技能，优化技能库构成提升... | 需要采样计算技能边际贡献，存在额外计算开销，对现有技能库架构有适... | — |
| 10 | high | - | [Consilience: Conformally Calibrated Communication Control for Hi...](http://arxiv.org/abs/2608.20564v1) | multi-agent coordination | 带认证的自适应通信控制比提升信息可用性更有价值，在隐信息任务中效果甚至超过全信息基线 | 通过推理时编排与逐轮共形校准为通信行为提供保证，筛除不可行方案，引导规范多智能体... | 需要逐轮计算校准，增加推理耗时，仅在特定隐信息任务验证，通用性有... | — |
| 11 | high | - | [Don't Repeat Yourself: Stopping Verbatim Loops at Sampling Time](http://arxiv.org/abs/2608.22761v1) | model steering | DRY可将循环后缀延伸率降低47%，对半降低大模型循环率且保留基准性能，现有基线方法存在明显... | 在采样阶段调整模型输出对数概率，通过匹配上下文已有后缀惩罚会延长逐字循环的候选t... | 仅针对逐字循环问题，未验证在更长、更复杂生成场景下的泛化效果 | — |
| 12 | high | - | [Don't Solve, Just Compare: Tiny Advisors for Runtime Interventio...](http://arxiv.org/abs/2608.21027v1) | model steering | 辅助模型任务求解能力远弱于原智能体时，依然可以实现有效的构造性运行时干预，提升原智能体性能。 | 通过经配对监督训练的微型比较器比较原方案与备选方案优劣，判断是否干预，给出非绑定... | 需要采样多个备选方案做比较，会增加额外推理耗时，未验证在更复杂长... | — |

## A 会 / Venue 标签

- **KDD 2026**：1 篇
- **ICML 2026**：1 篇

## 方法族分布

- **model steering**：20 篇
- **evaluation/benchmark**：16 篇
- **other**：10 篇
- **policy optimization**：4 篇
- **tool-use control**：3 篇
- **multi-agent coordination**：3 篇
- **survey**：1 篇
- **agent harness**：1 篇
- **consistency detection**：1 篇
- **unlearning/safety**：1 篇
- **skill generation**：1 篇

## 失败模式与风险信号

- 大模型无法可靠遵守个性化隐私披露策略，违规率高
- 现有评估存在弱测试预言机、数据泄露、agent harness不固定、仅做代理安全检查等缺陷。
- 纯数据驱动因果发现失效，大语言模型输出不一致、相互矛盾
- 长程任务运行错误，仅故障检测不足以恢复，现有有效运行时干预成本与开销过高
- 现有知识修改方法改变原检查点、更新不可撤销、引发跨域遗忘
- 信念到动作路由失败，无法利用已有的协作伙伴信念信息辅助动作预测
- Agent无法满足准则修订的全部判定条件，可未真正修订就完成测试任务
- 隐信息场景多智能体通信中，现有协议无法保证对话行为合理性，协调效果不佳
- 早期上游失败提前终止任务，无法定位失败根源，最终结果无法反映真实能力
- 现有安全评测仅关注输出结果，无法识别模型因错误原因产生的看似安全的输出

## 评测信号

- 在公开空气质量数据集上，ConceptTS预测准确率与强黑盒基线相当，同时可生成语义有效的概念激活结果。
- 现有基于prompt的个性化隐私策略违规率很高，所提Repair方法可显著降低违规，提升隐私策略合规性。
- 现有评估存在多种有效性威胁，单一基准分数不足以衡量模型能力，需要多维度任务适配证据支撑。
- 以专家验证的因果图为金标准，验证该方法可恢复全部已验证因果边，同时发现新的合理因果关联。
- 在三个环境搭配三个不同原智能体的共九个评测设置中性能均得到提升，表现优于所有对比基线。
- 摘要未提及具体评测信号与评测结果
- 验证CellFill在保持事实召回性能的同时，相比基线方法显著降低知识更新带来的跨域遗忘
- 微调后的Llama-3.1-8B下一POI预测准确率达49.1%，在雨天等欠采样场景仍保持较强性能，泛化效果良好。
- 通过测量steering激活后另一轴预测的响应变化，判断模型信念到动作的路由是否正常有效
- 以是否满足五个非补偿性条件为核心标准，统计无效实验数量，分析不同方案的实际失效情况

## 控制机制 / Harness 信号

- 通过将预测决策组织为显式人类可读的概念瓶颈结构，支持直接概念级干预来管控模型决策过程。
- 在推理阶段对模型注意力头进行干预，调整模型信息披露行为，使其符合用户个性化的隐私策略要求。
- 提出多维度保证框架与研究报告规范，通过规范评估保障代码代理的安全与行为可靠性。
- 通过经验数据对LLM生成的因果假设评分，利用高分结果更新模型上下文，引导生成向更优假设空间收敛。
- 通过经配对监督训练的微型比较器比较原方案与备选方案优劣，判断是否干预，给出非绑定建议供原智能体重规划。
- 本文未涉及模型或Agent行为的控制改进，仅开展深度学习信息处理机制的概念分析。
- 将新知识约束在量化单元内的权重残差学习，冻结原模型量化参数，实现更新可撤销，限制更新副作用
- 通过微调大语言模型，将预训练得到的通用人类行为知识适配到目的地特定预测任务。
- 通过激活steering控制模型沿特定轴的激活，以此诊断信念到动作预测的路由问题，定位模型失效
- 通过设计带明确约束的评测框架，提出轨迹锚定协议，提升对Agent准则修订行为评测的区分度

## 可靠性 / 落地风险

- 仅在单数据集完成验证，泛化性未测试，依赖大模型生成概念存在概念偏差风险。
- 仅在两个7B及以下参数模型验证，未测试更大规模模型，方法通用性有待验证。
- 现有研究评估不规范，存在多种有效性威胁，结果难以复现，无法同时保障功能正确与安全。
- 仅在单个临床数据集评测，未做多场景验证，结果的普适性缺乏充分验证。
- 需要采样多个备选方案做比较，会增加额外推理耗时，未验证在更复杂长程任务上的效果。
- 本文属于基础概念性研究，未涉及实际落地场景，暂未体现明确的工业落地可靠性风险。
- 仅适用于量化大模型，可承载的新知识规模受限于量化间隙的容量大小
- 仅在单个小规模实地数据集上验证，方法在更多类型目的地的泛化性未得到检验。
- 仅完成失效诊断未提出解决方案，仅在自制基准验证，方法泛化性未得到充分验证
- 现有评测方案区分度不足，无法有效判定Agent是否真正完成了准则修订

## 代码资源

- [INTENT-AS-A-TOOL Makes it Easy to Track Agentic Misalignment](https://github.com/RebeccaZhang22/intent-as-a-tool.) · 2 stars
- [GGSS: Geodesic-Gated Spherical Steering for Inference-Time Debiasing of Generati...](https://github.com/dukesun99/GGSS.) · 1 stars
- [AgentFold: Closed-Loop Agentic Search for Protein Folding Model Design](https://github.com/lmqfly/AgentFold.) · 1 stars
- [Lexical Perturbations Disrupt LLM Reasoning: An Empirical Study of Attention Div...](https://github.com/Jiaqian-Janelle/Attention-Diversion)

## 常见基线方法

- **强黑盒基线模型**：1 篇
- **基于prompt的隐私策略**：1 篇
- **专家构建因果图**：1 篇
- **现有基于专家求解器的干预方法**：1 篇
- **现有任务评论家干预方法**：1 篇
- **特征组合范式**：1 篇
- **无约束参考更新方法**：1 篇
- **未合并的Adapter**：1 篇
- **无状态推理**：1 篇
- **仅追加历史**：1 篇

## 常用数据集

- **摘要未提及**：4 篇
- **ALFWorld**：2 篇
- **MT-Bench**：2 篇
- **HotpotQA**：2 篇
- **北京多站点空气质量数据集**：1 篇
- **P3Bench 个性化隐私保护基准**：1 篇
- **不良妊娠结局真实临床数据集**：1 篇
- **WebShop**：1 篇
- **tau^3-Retail**：1 篇
- **1.7B量化大语言模型**：1 篇

---
*自动生成于 2026-08-30 | ArXiv_Daily_Digest*