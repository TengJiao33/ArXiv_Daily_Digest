# Agent Skills 与 Harness — 2026-W34 (08/17-08/23)

本周新增 **148** 篇论文，**9** 篇附带代码。优先级：high 130 / medium 16 / low 2。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [JailbreakSkill: Scaling Automated Red-Teaming with Reusable and ...](http://arxiv.org/abs/2608.16465v1) | skill generation | 该方法在AdvBench上宏平均攻击成功率提升17.5个百分点，HarmBench提升13.... | 将攻击策略封装为模块化可复用技能，构建攻击经验到技能进化的闭环，持续迭代扩充技能... | 作为攻击红队框架，进化出的未知攻击策略存在被滥用风险，且未明确说... | ✅ |
| 2 | high | - | [Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decr...](http://arxiv.org/abs/2608.13987v1) | agent harness | 修复bug后，32GiB共享内存下上下文宽度拓展2.7倍，MCPMark子集任务完成率从0%... | 通过修复部署bug、提出分块预填充策略降低内存开销，提供适配端侧的检查点与评估框... | 仅适配Apple Silicon端侧，多工具调用能力不足，通用性... | ✅ |
| 3 | high | - | [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchm...](http://arxiv.org/abs/2608.19741v1) | evaluation/benchmark | 最强模型在该基准上pass@1达65.36%，但20次尝试后的通过率仅25.25%，单次成功... | 构建隔离的工具交互沙盒与带可执行任务校验的基准，为智能体行为可靠性评测提供支撑。 | 现有依赖单次成功的评测低估了智能体在业务场景的不可靠性，无法反映... | ✅ |
| 4 | high | - | [ReCache: Efficient KV Cache Reuse and Compression for Tool-Augme...](http://arxiv.org/abs/2608.19662v1) | agent harness | 资源感知注意力Inv-F1达82.3%（原始为82.4%），首Token延迟加速3.655倍... | 通过缓存架构设计结合资源感知注意力与剪枝，控制工具增强智能体的推理资源开销，提升... | 仅在公开整合数据集验证，未测试工业级复杂多工具场景下的通用性与稳... | ✅ |
| 5 | high | - | [SemaPLC: A Project-Grounded, Verification-Gated Agent Harness fo...](http://arxiv.org/abs/2608.18565v1) | agent harness | 动态运行得分对方法的区分度远高于静态评分，SemaPLC动态得分为52.2，基线仅为22.4... | 采用验证门控的智能体框架，依靠外部规范、编译、动态运行检查管控生成过程，不依赖模... | 依赖真实PLC运行时环境做验证，大规模测试场景下的部署和验证成本... | ✅ |
| 6 | high | - | [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queri...](http://arxiv.org/abs/2608.16071v1) | agent harness | 显式利用技能内部结构生成伪查询，可在多种检索设置下平均提升Recall@1达6.7个百分点，... | 通过显式利用技能内部结构生成高质量伪查询，优化检索器，提升技能检索质量，进而改进... | 大规模技能库场景下，技能知识图谱构建与伪查询生成存在一定计算开销... | ✅ |
| 7 | high | - | [StepJack: Benchmarking Computer-Use Agent Safety Against Multi-S...](http://arxiv.org/abs/2608.06477) | evaluation/benchmark | 固定分解深度下，多步攻击最高让CUAs的攻击成功率提升31.2个百分点，五个可用CUAs平均... | 构建针对多步间接提示注入的专用安全性评测基准，为计算机使用智能体的安全性验证提供... | 面向实际场景的计算机使用智能体普遍未防御多步间接注入，存在较高的... | ✅ |
| 8 | high | - | [Task-CoEvolve: Efficient Harness Optimization via Adaptive Valid...](http://arxiv.org/abs/2608.20169v1) | agent harness | 自适应选择信息性任务可在保持和全量搜索一致性能的前提下，将harness优化的评估次数减少8... | 通过自适应选择信息性验证任务迭代优化harness代码，无需更新模型权重，兼顾性... | 基于采样估计全量性能，若采样分布偏移可能带来性能估计偏差，影响h... | ✅ |
| 9 | high | - | [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Tra...](http://arxiv.org/abs/2608.05139) | evaluation/benchmark, po... | 评测发现高技能熵任务存在技能切换缺口，模型准确率随技能熵升高下降；Qwen3-4B经训练准确... | 通过技能熵设计奖励信号，要求模型预测每一步所用技能，对齐金标准技能序列，优化改进... | 仅在通义千问系列小模型上验证，未在更多真实场景测试，泛化能力待验... | ✅ |
| 10 | high | - | [$R^3$-Bench: LLMs Struggle with Resource-Rational Reasoning unde...](http://arxiv.org/abs/2608.16033v1) | evaluation/benchmark | 评测的72个单元中，经验神谕平均成绩在71个单元中严格高于原生分配成绩，无策略可在所有领域占... | 构建共享预算约束下的资源理性推理评测基准，通过对标单问题能力校准模型共享预算场景... | 缺乏跨领域通用的共享资源调度方案，模型能力无法落地到共享预算实际... | — |
| 11 | high | - | [A Graph-Based Reinforcement Learning Framework for Structured Dr...](http://arxiv.org/abs/2608.14109v1) | agent harness | 单个小型语言模型即可做出正确的漂移恢复决策，且输出能够严格遵守指定的结构化输出模式。 | 在主智能体外部添加即插即用的图结构漂移恢复模块，用强化学习训练小模型实现结构化漂... | 仅在单一公开基准验证，未测试更多复杂真实场景下的泛化能力 | — |
| 12 | high | ICML 2026 | [A Two-Tier Perspective on Inference-Time Parallelism in Multi-Ag...](http://arxiv.org/abs/2608.05791) | agent harness | 两类并行对不同复杂度任务有互补效应，中等难度任务收益最大，过度激进并行不一定获得更好性能 | 通过双层并行建模，提出统一可控执行框架TIPEX，在统一语义下协调两类并行优化推... | 并行推理会增加token消耗，推高计算成本，对低算力场景落地不够... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **agent harness**：62 篇
- **evaluation/benchmark**：39 篇
- **skill generation**：13 篇
- **multi-agent coordination**：8 篇
- **tool-use control**：7 篇
- **policy optimization**：7 篇
- **survey**：5 篇
- **unlearning/safety**：3 篇
- **model steering**：2 篇
- **evaluation/benchmark, policy optimization**：1 篇
- **consistency detection**：1 篇

## 失败模式与风险信号

- LLM改造后科学软件存在相依赖并行死锁、降精度下虚假收敛
- 预训练模型直接处理未知规则任务性能极低，传统手工建模泛化性差成本高
- 长程智能体执行早期错误传播，错误影响难以通过后续动作逆转
- 固定提示策略无法适配不同种子任务的差异化难度需求，限制智能体训练效果
- 时序有效性失效、外生上下文误用、环境适配失败
- 智能体运行失败后遗留持久非预期无效副作用，破坏业务数据正确性。
- 运行时行为漂移，偏离原任务引发外部系统不可逆副作用
- 技能池扩大后检索精度大幅下降，技能易在假设脆弱、上下文不兼容、适配不足时失效
- 长程视频推理上下文细节丢失、数据依赖高、域外迁移性能差
- 原模型部署缺陷多、内存开销过高，修复后仍存在多工具调用失败问题

## 评测信号

- 超2200次运行测试显示，原与改造后内核在200组配对注入中全部一致，暴露了相依赖并行死锁与降精度虚假收敛。
- 相同基础模型下，原生基础模型得分仅7.8%，现成harness得61.1%，本文方法提升至93.3%，整体通关率达97.8%。
- 在多类任务、不同模型、执行策略与智能体框架下，AgentRewind稳定提升长程任务的成功率和平均进度。
- 该方法在4B至35B不同规模大模型上均能稳定提升性能，在tb-core基准上Pass@1可提升6.8-9.2个百分点。
- 不同层级大语言模型智能体的性能差距，以及智能体在时序有效性等核心能力上的失败表现。
- 在结构化企业数据集上验证了该框架产出的对话分析结果具备较高语义保真度与答案相关性，可支撑规模化端到端商业智能。
- 除任务有效完成外，重点评测智能体运行的安全失败与非原子副作用，关注工业场景运行安全性。
- 验证小模型可输出正确恢复决策，输出符合指定schema，各节点对应语义内容恰当合规。
- 仅使用更小规模训练数据，ART在仿真与真实任务上的任务成功率较主流基线提升20%，具备轻量可扩展特性
- 统计分析了技能使用模式占比、不同规模技能池的检索精度，以及相对基线的任务提升幅度。

## 控制机制 / Harness 信号

- 构建差分故障注入测试harness，通过对比原代码与改造后代码的故障响应，验证LLM改造的可靠性。
- 通过专属harness施加约束，要求世界模型复现所有历史观测转移，利用预测不匹配修复模型后再输出动作。
- 通过记录对齐的智能体上下文与受控环境检查点，实现运行时错误回滚，抑制早期错误的传播影响。
- 通过基于验证器奖励的动态环境合成，仅保留验证通过的训练环境，优化训练任务难度匹配，提升智能体训练效果。
- 通过构建适配演化环境的实时基准评测智能体行为，暴露能力缺陷，为智能体改进提供评测依据。
- 采用监督式架构，通过动态任务协调层实现多智能体任务分配的自适应实时协调、恢复与优化，管控分析工作流。
- 通过构建原子性感知评测框架，引入任务专用状态验证器，规范工业级GUI自动化智能体的运行安全。
- 在主智能体外部添加即插即用的图结构漂移恢复模块，用强化学习训练小模型实现结构化漂移管控。
- 通过工具注入框架将模块化工具整合进VLA模型，缩小动作解空间，优化智能体行为，实现轻量高效部署
- 通过系统性评估明确Agent技能的生效与失效规律，为设计和把控可靠Agent技能提供指导依据。

## 可靠性 / 落地风险

- 仅在单个科学软件案例验证，方法通用性待验证，未说明推广到其他场景的成本。
- 依赖前沿大编码智能体生成世界模型，多轮修复过程的耗时和稳定性仍不确定。
- 摘要未说明方法的算力开销与可复现性，也未在更多通用基准验证泛化能力
- 仅在代码任务场景完成验证，方法在其他类型智能体任务上的泛化性尚未得到验证。
- 作为实时基准需要持续更新维护，当前仅覆盖6个领域，整体场景覆盖范围有限。
- 未公开具体实验细节与对比基准，未说明算力需求，可复现性不明确，验证说服力不足。
- 非原子运行产生的持久无效业务变更会污染业务记录，难以回滚，阻碍工业落地。
- 仅在单一公开基准验证，未测试更多复杂真实场景下的泛化能力
- 未在更多大规模复杂真实场景验证，未明确代码数据开放情况，可复现性待确认
- 仅输出规律性结论，未在具体工业场景验证，未提出可直接落地的改进方案。

## 代码资源

- [Toward Skill-Native LLMs: Skill Entropy for Benchmarking and Training Long-Horiz...](https://github.com/Gen-Verse/Skill-Entropy-RL) · 34 stars
- [SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code Gener...](https://github.com/midea-ai/SemaPLC.) · 30 stars
- [One Success Isn't Reliability: Thinkingbox, a Sandbox and Benchmark for Agents i...](https://github.com/microsoft/thinkingbox) · 6 stars
- [StepJack: Benchmarking Computer-Use Agent Safety Against Multi-Step Indirect Pro...](https://github.com/BorealisAI/StepJack.) · 3 stars
- [Nanbeige4.2-3B on Apple Silicon: Fixing Deployment Bugs and Decreasing Looped Tr...](https://github.com/johnhalloran321/Nanbeige4.2-3B-mps-fix.) · 1 stars
- [Task-CoEvolve: Efficient Harness Optimization via Adaptive Validation Task Selec...](https://github.com/Agent4Science-UTokyo/Task-CoEvolve.) · 1 stars
- [ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents](https://github.com/EIT-NLP/ReCache.) · 1 stars
- [JailbreakSkill: Scaling Automated Red-Teaming with Reusable and Ever-Evolving Sk...](https://github.com/BattleWen/JailbreakSkill.)
- [Skill2Query: Exploiting Skill Structure to Generate Pseudo-Queries for Agent Ski...](https://github.com/MatZaharia/Skill2Query.)

## 常见基线方法

- **Reflexion**：3 篇
- **ReAct**：2 篇
- **原始未改造的科学软件实现**：1 篇
- **直接使用的基础模型**：1 篇
- **现成通用harness**：1 篇
- **现有长程智能体执行方法**：1 篇
- **Base基线**：1 篇
- **最强固定配方基线方法**：1 篇
- **前沿LLM智能体**：1 篇
- **专家手工构造提示**：1 篇

## 常用数据集

- **摘要未提及**：4 篇
- **Terminal-Bench 2.1**：4 篇
- **SWE-bench Verified**：3 篇
- **ALFWorld**：3 篇
- **GAIA**：3 篇
- **BFCL**：2 篇
- **SWE-bench**：2 篇
- **OSWorld-Verified**：2 篇
- **tau2-bench**：2 篇
- **BFCL-v4**：2 篇

---
*自动生成于 2026-08-23 | ArXiv_Daily_Digest*