# Agent Skills 与 Harness — 2026-W33 (08/10-08/16)

本周新增 **186** 篇论文，**13** 篇附带代码。优先级：high 142 / medium 37 / low 7。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [@skills: Attention is all you have](http://arxiv.org/abs/2608.12610v1) | agent harness | 现有技能交付将内容、持久化、自动触发捆绑驻留提示词，实际仅自动触发需要占用提示词触发槽位。 | 通过分离技能功能，仅保留必要触发信息占用提示词空间，实现轻量化Agent技能管理... | 未经过实际下游任务评测，方案有效性缺乏验证，落地效果待确认。 | ✅ |
| 2 | high | - | [ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork...](http://arxiv.org/abs/2608.09476v1) | evaluation/benchmark | 固定harness下攻击成功率为10.1%-94.4%，固定模型下为73.7%-94.4%，... | 本文构建协同Agent行为安全评测基准，通过双证据验证机制从执行轨迹层面验证Ag... | 现有主流Agent harness普遍存在较高行为安全漏洞，易被... | ✅ |
| 3 | high | - | [AgentPatch: Coarse-to-Fine Weak-Task Repair for Merging Agentic ...](http://arxiv.org/abs/2608.06699v1) | agent harness | 无需训练的粗到精补丁，可在不使用路由或集成的前提下，缓解合并后弱任务退化，更好平衡不同能力保... | 通过无训练的弱任务残差恢复和智能体引导行为补丁，修复合并后能力退化，兼顾能力保留... | 未在真实工业场景验证，所有结论来自公开基准，实际落地的泛化性尚不... | ✅ |
| 4 | high | - | [An End-to-End Agent Auditing Engine](http://arxiv.org/abs/2608.07346v1) | evaluation/benchmark | 不同模型与智能体harness的组合在不同类型任务上性能差异显著，不存在能在所有任务上持续最... | 通过构建端到端多维度的智能体harness评测框架，输出标准化评测结果，为模型与... | 未披露评测的算力消耗，未在真实工业场景验证，实际落地适配性有待进... | ✅ |
| 5 | high | - | [DSAgentBench: Can Agents Automate End-to-End Data-Science Workfl...](http://arxiv.org/abs/2608.10366v1) | evaluation/benchmark | 最强智能体Claude-4.6-Sonnet任务成功率仅56.70%，所有开源智能体均低于1... | 构建标准化评测基准，提供确定性评估反馈，为开发接地可验证的自主数据科学智能体提供... | 现有智能体在真实环境复杂数据科学工作流下可靠性低，开源模型能力远... | ✅ |
| 6 | high | - | [Long-Horizon Agent Trajectory Attribution: A Unified Benchmark a...](http://arxiv.org/abs/2608.06909v1) | evaluation/benchmark | 不同归因设置下参考基线性能差异显著，长程和结构化归因任务比局部归因难度更高。 | 构建统一轨迹归因基准与可复用标注框架，为智能体行为分析提供评测反馈支撑。 | 仅推出基准框架，未验证归因结果对实际改进工业智能体的实际效用 | ✅ |
| 7 | high | - | [OpenCodeReview: Determinism over Non-Determinism for Cost-Effect...](http://arxiv.org/abs/2608.09290v1) | agent harness | 为Agent流水线注入确定性约束，可使代码评审SEM-F1最高提升2.17倍，同时减少5-1... | 在流水线三个关键节点注入确定性约束，通过规则分发、限定工具集、去偏反射过滤规范A... | 依赖定制规则实现分发，仅在自建基准评测，跨场景泛化能力未经验证。 | ✅ |
| 8 | high | - | [Practice Makes Unsafe: Skill Misevolution in Self-Improving LLM ...](http://arxiv.org/abs/2608.12851v1) | agent harness, evaluatio... | 所有21种测试的演化配置都会生成不安全工件，SafeEvolve降危害17.3-26.7个百... | 提出全生命周期感知的技能版本化harness框架，通过SafeEvolve封装修... | 自改进智能体的持久化技能易留存不安全内容，风险跨会话延续，现有演... | ✅ |
| 9 | high | - | [SKILLER: Language-Level Reinforcement Learning for Reusable Skil...](http://arxiv.org/abs/2608.10538v1) | skill generation | SKILLER让9B参数小模型性能最高提升20.4个百分点，在SkillsBench单技能任... | 通过生成小模型适配的可复用技能约束行为空间，基于语言级强化学习，利用强模型提供自... | 训练阶段依赖强大模型提供信号，训练过程仍需要大模型支持，存在一定... | ✅ |
| 10 | high | - | [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval ...](http://arxiv.org/abs/2608.12282v1) | evaluation/benchmark | 最优模型单跳任务仅70.4%正确率，策略约束下不可回答问题正确率低至2.4%，失败集中在语言... | 采用固定ReAct harness隔离模型能力与agent架构影响，通过基准评测... | 现有大模型在企业场景带约束的工具推理任务中性能极差，距离实际落地... | ✅ |
| 11 | high | - | [A Modular Agentic Framework for Synthetically Constrained Multi-...](http://arxiv.org/abs/2608.11483v1) | agent harness | SABLE仅评估枚举搜索空间的子集，即可有效富集符合用户多目标约束的候选化合物，架构灵活可替... | 采用模块化架构设计，通过自然语言编排实现任务路由，支持修改配置更换工具，满足多目... | 未给出量化对比评测结果，缺乏实际药物研发场景的落地验证，实际性能... | — |
| 12 | high | - | [A Unified Issue Resolution Benchmark for Requirement Clarificati...](http://arxiv.org/abs/2608.09072) | evaluation/benchmark | 现有主流编码智能体在该基准上平均解决率仅31.5%，隐式需求恢复失败占失败运行的24.5%-... | 通过构建带有中间环节真值的评测基准，为编码智能体的过程诊断和能力改进提供反馈支撑... | 现有编码智能体仓库级任务解决率仅三成，基准仅覆盖两类语言公开仓库... | — |

## 方法族分布

- **agent harness**：72 篇
- **evaluation/benchmark**：63 篇
- **skill generation**：12 篇
- **tool-use control**：11 篇
- **policy optimization**：7 篇
- **multi-agent coordination**：6 篇
- **unlearning/safety**：5 篇
- **online distillation**：2 篇
- **survey**：2 篇
- **knowledge distillation**：1 篇
- **skill optimization**：1 篇
- **reward learning**：1 篇

## 失败模式与风险信号

- 现有技能进化缺乏显式结果反馈，无专门知识整合机制，易引发性能退化。
- 临床诊断过早闭合，容易漏诊高危信号，对抗场景下诊断准确率低
- 现有智能体harness评测仅关注正确性，无法细粒度区分不同harness的多维度能力差异。
- 小模型难以生成成功任务轨迹，工具调用容易出错
- 不安全工具调用
- 世界模型状态预测遗漏关键事实、应用错误转移规则的系统性预测错误
- 单分数技能优化无法区分过拟合尖峰与可继续优化的宽高原，难以持续改进技能。
- 传统知识生成方法要么刚性无法适配新兴技能，要么碎片化知识不稳定。
- 持久载体引入的跨边界延迟安全风险，现有评测无法揭示该类风险的传播规律。
- 长周期任务执行存在性能缺陷

## 评测信号

- SkillProx相比最强梯度基线平均准确率提升3.0个百分点，两个核心模块具备互补效果。
- 对抗条件下诊断准确率较基线提升7.0%，漏诊红牌率降低31%，盲测临床专家87.6%偏好该训练后智能体。
- 除任务正确性外，从执行效率、工具使用、任务规划、错误恢复多维度细粒度刻画不同harness的能力差异。
- 4B-8B学生模型在三个基准上平均准确率分别提升27.2%p、11.2%p、3.4%p，性能优于现有基线。
- 在2000个真实场景中F1达88.5%，假阳性率1.1%，相对所有对比基线都有统计显著的效果提升
- 记忆增强可将结构化状态保真度最高提升206.3%，下游任务成功率相对基线获得最高65.4%的相对增益。
- 在冻结30B参数智能体的三个基准中，相较基线方法和无技能智能体均获得显著的held-out准确率提升。
- 摘要未给出具体量化评测结果，仅说明框架具备可扩展性、可解释性与自修复能力，可适配多语言噪声数据。
- 通过多阶段轨迹评估观测攻击链推进程度与阻断位置，揭示不同配置下Agent harness的风险遏制效果差异。
- 45项任务总结果得分达84.59，比次优方法高出18.07分，验证了工作流的透明可追溯性。

## 控制机制 / Harness 信号

- 通过闭环诊断回退性能退化，结合留一法效用审计筛选整合技能单元，优化智能体技能行为。
- 通过模拟临床环境中的强化学习，基于对齐多维度临床要求的结构化奖励优化智能体行为，提升对抗鲁棒性。
- 通过构建端到端多维度的智能体harness评测框架，输出标准化评测结果，为模型与harness优化提供反馈指导。
- 通过从大教师智能体蒸馏分层结构化记忆，采用主动注入加反应式检索改进小模型智能体行为。
- 通过锁定意图合约，使用独立验证器验证工具调用，生成零知识证明验证通过后才允许工具执行，实现可验证行为约束
- 依托外部精心整理的世界记忆库约束世界模型预测，为策略提供检索技能与校正引导，改进智能体行为。
- 通过可进化性引导的树搜索优化自然语言形式的技能文本，无额外开销即可改进冻结智能体的行为。
- 通过自顶向下锚定稳定知识实体、自底向上动态生成新节点的混合模式，结合智能体迭代反思，兼顾稳定性和扩展性。
- 通过构建安全性评测基准，提出多阶段轨迹追踪评估方法定位攻击链阻断位置，为改进Agent harness安全性提供依据。
- 通过三层分层架构搭建智能体执行框架，将用户意图转为可执行工作流，基于中间结果调整执行，整合专用工具。

## 可靠性 / 落地风险

- 未在具体真实工业任务场景验证，未披露落地所需的具体算力开销数据。
- 未经过真实世界临床工作流验证，模拟与真实场景存在差异，临床落地存在不确定性风险。
- 未披露评测的算力消耗，未在真实工业场景验证，实际落地适配性有待进一步验证。
- 依赖大教师生成高质量轨迹，效果受教师学生兼容性限制，一定程度提升了落地成本
- 单合规操作证明生成增加约2.26秒延迟，时延较高，难以满足低延迟实时工业场景需求
- 需要人工精心整理构建任务专属记忆库，规模化落地的成本与扩展性有待验证。
- 未公开具体基准细节，结果的可复现性尚未得到充分的公开验证。
- 未提供量化评测结果验证方法效果，也未披露算力开销，工业落地的支撑不足。
- Agent harness中持久载体的残留风险会跨会话传播，威胁后续良性任务，现有评测难以有效识别该风险。
- 仅在分子设计领域完成验证，长周期执行能力不足，跨场景通用可靠性尚未验证。

## 代码资源

- [OpenCodeReview: Determinism over Non-Determinism for Cost-Effective Agent-Based ...](https://github.com/alibaba/open-code-review.) · 19972 stars
- [VAKRA: Evaluating Multi-Hop Reasoning Across APIs and Retrieval Under Tool-Use P...](https://github.com/IBM/VAKRA.) · 64 stars
- [An End-to-End Agent Auditing Engine](https://github.com/datamllab/A2E.) · 17 stars
- [Vero: Can AI Agents Build Formally Verified Software Repositories?](https://github.com/sunblaze-ucb/vero.) · 4 stars
- [Agentic Reinforcement Learning with Observation-Calibrated Self-Distillation](https://github.com/yiy1x/OCSD.) · 4 stars
- [@skills: Attention is all you have](https://github.com/SylphAI-Inc/atskills) · 3 stars
- [ActBench: Self-Evolving Benchmark of Behavioral Safety in Cowork Agents](https://github.com/zjuicsr/ActBench.) · 2 stars
- [DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Comp...](https://github.com/vis-nlp/DSAgentBench.) · 2 stars
- [SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in ...](https://github.com/DANG-ai/SKILLER.) · 1 stars
- [FinReportBench: Measuring and Improving Institution-Grade Financial Report Gener...](https://github.com/MisterBrookT/finreportbench.) · 1 stars

## 常见基线方法

- **GEPA**：2 篇
- **未明确具体基线名称**：2 篇
- **Claude Code**：2 篇
- **Codex**：2 篇
- **基于梯度的基线方法**：1 篇
- **base大语言模型**：1 篇
- **仅基于正确性的评估**：1 篇
- **现有基于记忆的基线方法**：1 篇
- **NeMo Guardrails**：1 篇
- **Llama Prompt Guard 2**：1 篇

## 常用数据集

- **ALFWorld**：7 篇
- **WebShop**：6 篇
- **AppWorld**：4 篇
- **摘要未提及**：4 篇
- **SWE-bench Verified**：4 篇
- **SkillsBench**：3 篇
- **BFCL V3**：2 篇
- **Agent-SafetyBench**：2 篇
- **AgentDojo**：2 篇
- **WebArena**：2 篇

---
*自动生成于 2026-08-16 | ArXiv_Daily_Digest*