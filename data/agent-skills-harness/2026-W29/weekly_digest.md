# Agent Skills 与 Harness — 2026-W29 (07/13-07/19)

本周新增 **174** 篇论文，**9** 篇附带代码。优先级：high 133 / medium 36 / low 5。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | ICML 2026 | [AutoVSR: Automatic Visual-to-Symbolic Reasoning for Symbolic Exp...](http://arxiv.org/abs/2607.11338v1) | agent harness | 相较于端到端VLM方法和专用方法，准确率分别提升30.01--59.45%和41.96--5... | 通过可执行中间表示、组件规则检索加验证反馈，结合带符号工具库的规划智能体约束推理... | 仅在电路符号生成任务验证效果，方法在其他领域的泛化能力未验证，存... | ✅ |
| 2 | high | - | [Copy-on-Write Scoring: Application-Specific Agent Evaluations](http://arxiv.org/abs/2607.14336v1) | evaluation/benchmark | 该框架可低成本定位工具面具体问题，修复对应问题后，受影响模型获得了可衡量的性能提升。 | 通过输出细粒度低成本的评估结果，为智能体harness与工具面的迭代优化提供反馈... | 仅适配基于PostgreSQL存储的应用，仅在单个项目验证，方案... | ✅ |
| 3 | high | - | [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-C...](http://arxiv.org/abs/2607.11818v1) | evaluation/benchmark | 存在规模相关的规划-精度交叉现象：最优模型成功率低于50%，大模型53%失败源于图像信息提取... | 构建标准化统一评测框架，通过失效分析定位不同规模模型的能力瓶颈，为模型改进提供方... | 现有不同规模的视觉工具调用智能体均存在明显能力短板，鲁棒性不足距... | ✅ |
| 4 | high | - | [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](http://arxiv.org/abs/2607.13027v1) | agent harness | 封装带清晰边界原生设备能力的端侧框架，相比最强基线任务成功率提升11.5%，完成时间降低94... | 通过原生端侧框架将设备能力封装为带清晰执行边界的显式设备工具，实现对智能体动作执... | 未提及多机型、不同端侧大模型的兼容性，缺乏大规模实际场景落地验证... | ✅ |
| 5 | high | - | [SCALECUA: Scaling Computer Use Agents with Verifiable Task Synth...](http://arxiv.org/abs/2607.11185v1) | agent harness | 训练速度比逐步分解提升2.83倍，在OSWorld达68.7%、ScienceBoard达5... | 通过可验证任务合成提供带可信奖励的训练数据，结合采样优化和上下文分割提升训练效率... | 未验证跨复杂GUI场景的泛化能力，工业落地需进一步测试实际场景鲁... | ✅ |
| 6 | high | - | [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforce...](http://arxiv.org/abs/2607.14777v1) | online distillation | SEED在文本与视觉类智能体任务中可稳定提升性能与样本效率，对未见场景具备稳定的鲁棒泛化能力 | 通过从已完成的同策略轨迹提取可复用后见技能，生成稠密token级蒸馏监督信号，联... | 未披露方法的具体算力消耗，也未在真实工业场景验证，落地有效性有待... | ✅ |
| 7 | high | - | [SPORK: Self-Speculative Forking to Accelerate Agentic LLM Infere...](http://arxiv.org/abs/2607.03333) | agent harness | 分叉探针预测Qwen3-32B工具名称准确率达74.6%-99.6%，可将GAIA的P95端... | 作为轻量控制器叠加在标准推理API上，通过自投机分支提前调度工具调用，重叠推理与... | 投机工具预测错误会产生额外的探针计算开销，极端场景可能小幅增加总... | ✅ |
| 8 | high | - | [StructureClaw: Traceable LLM Agents and an Executable Benchmark ...](http://arxiv.org/abs/2607.14896v1) | agent harness; evaluatio... | 完整自动工作流的任务成功率从通用技能基线的56.8%提升至88.6%，现存两大挑战为无效输入... | 通过以工件为中心的框架，采用受控工程技能、类型化工具与执行断言，规范约束LLM智... | 仅适配结构工程垂直领域，跨领域通用性未经验证，落地应用范围有限。 | ✅ |
| 9 | high | - | [ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memo...](http://arxiv.org/abs/2607.11126v1) | tool-use control | 工具侧维护的共享工具记忆可跨环境跨智能体框架无重训迁移，pass@1最高较基线提升24.16... | 通过在工具侧构建经执行验证的持久化工具知识记忆，供下游智能体查询，提升工具知识可... | 仅在MCP小规模基准验证，未在大规模真实工业工具场景验证方法有效... | ✅ |
| 10 | high | - | [A Formal Hierarchical Architecture for Agentic Orchestration wit...](http://arxiv.org/abs/2607.11138v1) | agent harness | 该架构的内存与提示成本随探索路径而非全局工具库规模缩放，可实现不同执行分支的完全隔离。 | 通过分层技能组织、栈式执行与懒加载发现，缩小工具决策空间，隔离不同执行分支，满足... | 仅完成受控基准测试，未在大规模复杂真实业务场景完成充分验证。 | — |
| 11 | high | - | [A Learning-Rate-Gated Failure of GRPO in a Small Language and Vi...](http://arxiv.org/abs/2607.12640v1) | policy optimization | 在已被小参数Web智能体基本掌握的任务上，GRPO无法提升性能，中高学习率反而会降性能，失效... | 构建包含多组超参数、随机种子的控制实验网格，通过可控对照分析GRPO对智能体性能... | 小参数智能体在已掌握任务上用GRPO微调不仅无提升，还会导致原有... | — |
| 12 | high | - | [A Workflow-Aware Serving Layer for Agentic Applications](http://arxiv.org/abs/2607.02942) | agent harness | 将强模型与验证资源集中到错误传播最远的工作流节点，预解策略可在不增加负载切换时延的前提下兼顾... | 通过工作流感知的调度策略，基于预解整数规划方案，依负载动态调整节点资源分配，将优... | 未经过公开基准或实际工业场景验证，整数规划预解会带来一定的前期部... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇
- **ACL 2026**：1 篇

## 方法族分布

- **agent harness**：63 篇
- **evaluation/benchmark**：56 篇
- **multi-agent coordination**：9 篇
- **tool-use control**：9 篇
- **skill generation**：8 篇
- **survey**：5 篇
- **policy optimization**：5 篇
- **other**：4 篇
- **unlearning/safety**：4 篇
- **model steering**：3 篇
- **reward learning**：2 篇
- **online distillation**：2 篇

## 失败模式与风险信号

- 现有面向人类的缺陷报告不匹配Agent需求，易导致Agent搜索空间过大，修复成功率偏低
- 全量持久化引入过时痕迹偏置，全新会话丢弃过往有效可复用上下文信息
- 上下文爆炸、生成内容冲突不一致、生成内容质量缺乏自动化保障
- 大模型隐式时间推理能力不足，长程决策性能高度依赖模型即时上下文
- 现有LLM科学智能体的推理过程隐藏在非结构化日志中，无法被审计验证。
- 长视界上下文累积后验证难度上升，分布偏移下智能体整体可靠性下降
- 聊天场景校准的激活引导安全结论无法直接推广到工具智能体部署，存在不可预测的安全风险。
- 流程僵化无法动态适配测试策略，上下文提取不贴合测试需求，无法捕获细粒度代码依赖
- 无法正确遵循技能中的逻辑关系，引发各类不安全违规行为
- 长周期规划、长上下文管理与迭代调试能力不足

## 评测信号

- 260次攻击测试中整体成功率达95.0%，多数攻击执行时间低于两分钟，token开销低，单场景最高成功率可达100%。
- 摘要未提及具体量化评测信号，仅梳理领域研究进展与待解决的挑战问题。
- 分析不同信息类型与软件修复Agent修复通过率的关联，验证了对人类有用的信息不一定对Agent有帮助。
- 在包含四个诊断模态的胶质瘤队列中，该方法降低55%平均获取负担，同时保持有竞争力的预测精度
- 在三类不同任务上，RashomonLLM的预测准确率与解释质量均显著优于SOTA基线，性能对分布偏移等鲁棒。
- 企业场景任务完成率达96%，零令牌刷新降低任务耗时14倍，token成本降低97倍，公开数据集验证泛化性
- FirstProof挑战赛10道题中6道提交被判定至多少量修改即正确，收集的30道开放题中有5道被判定完全正确。
- 在20个不同的世界构建任务中成功率达95.0%，生成每个世界耗时18-31分钟，可输出无冲突的自洽概念。
- STEEL在AMD XDNA NPU上的能耗、延迟表现远超CPU、GPU及现有SOTA，端侧节能效果十分显著。
- 评测不同方案在长程临床任务上的性能，发现隐式时间推理和长程决策是现有大模型的主要性能短板

## 控制机制 / Harness 信号

- 通过任务分工构建双智能体架构，将漏洞利用流程拆分为检测与执行两个阶段，结合工具实现流程控制。
- 本文为综述性研究，梳理智能体AI在EDA领域的应用演进，为大模型整合入EDA提供系统性研究框架。
- 通过分析缺陷报告不同信息对Agent修复效果的影响，明确有效信息类型，引导Agent缩小修复搜索空间。
- 通过自进化积累可复用决策模式，结合临床工具与两类记忆，引导智能体做出平衡精度与负担的模态决策
- 通过耦合解释与预测目标，迭代对齐自然语言解释与模型预测，以解释保真度约束模型行为。
- 通过选择性保留共享可复用持久上下文、丢弃无用会话痕迹，结合权限访问控制优化智能体行为
- 采用作者-评论家架构，通过多角色协作校验推理过程，提升开放数学问题求解的输出正确性。
- 采用技能驱动架构，结合冲突检测、分层上下文压缩、专项评审智能体，控制生成内容的一致性与质量。
- 通过稀疏感知流水线调度与数据流优化，提升NPU上大模型注意力推理效率，降低端侧Agent推理能耗。
- 构建标准化的长程临床决策评测基准，通过评测结果反馈暴露现有医疗智能体的能力缺陷

## 可靠性 / 落地风险

- 仅在受控模拟环境中验证，未提及真实物联网场景的适配性，实际落地存在不确定性。
- 仅为综述性研究，未给出具体可落地方案，缺乏实际工业场景的落地验证。
- 实验仅基于公开基准开展，未验证结论在工业真实软件开发场景中的泛化性。
- 仅在胶质瘤临床数据集验证，未适配其他疾病场景，落地需调整适配不同诊疗流程
- 未公开实现细节与开源信息，可复现性未验证，也未说明工业落地的算力需求。
- 未提及大规模多用户场景下共享记忆的维护、冲突解决与回滚机制，存在潜在落地风险
- 仅面向开放数学领域，评测依赖人类专家，未验证通用任务可用性，对工业落地通用性不足。
- 仅在两个闭源大模型后端验证，未和现有方法做对比，泛化性仍需更多场景验证。
- 仅适配AMD XDNA架构NPU，通用性不足，未在真实Agent任务上验证落地效果。
- 评测仅基于公开MIMIC-IV数据，覆盖真实临床场景多样性不足，落地适配性有待验证

## 代码资源

- [PalmClaw: A Native On-Device Agent Framework for Mobile Phones](https://github.com/ModalityDance/PalmClaw.) · 1108 stars
- [StructureClaw: Traceable LLM Agents and an Executable Benchmark for Structural E...](https://github.com/structureclaw/structureclaw.) · 160 stars
- [SEED: Self-Evolving On-Policy Distillation for Agentic Reinforcement Learning](https://github.com/jinyangwu/SEED.) · 41 stars
- [Copy-on-Write Scoring: Application-Specific Agent Evaluations](https://github.com/trail-ml/agent-cow-python) · 10 stars
- [SPORK: Self-Speculative Forking to Accelerate Agentic LLM Inference](https://github.com/baihuajun24/spork.) · 7 stars
- [MM-ToolSandBox: A Unified Framework for Evaluating Visual Tool-Calling Agents](https://github.com/apple/ml-mmtoolsandbox) · 5 stars
- [AutoVSR: Automatic Visual-to-Symbolic Reasoning for Symbolic Expression Generati...](https://github.com/LongfeiLi1/AutoVSR.) · 4 stars
- [SCALECUA: Scaling Computer Use Agents with Verifiable Task Synthesis and Efficie...](https://github.com/THUDM/SCALE-CUA.) · 4 stars
- [ToolAtlas: Learning Once, Reusing Everywhere with Tool-Side Memory](https://github.com/PuppyKnightUniversity/ToolAtlas.) · 1 stars

## 常见基线方法

- **Codex**：2 篇
- **Claude Code**：2 篇
- **检索增强生成(RAG)**：2 篇
- **Reflexion**：2 篇
- **逻辑回归**：2 篇
- **随机森林**：2 篇
- **GPT-5.4**：2 篇
- **现有SOTA预测方法**：1 篇
- **现有SOTA可解释AI方法**：1 篇
- **无持久化记忆方案**：1 篇

## 常用数据集

- **SWE-bench Verified**：3 篇
- **Terminal-Bench 2.0**：3 篇
- **OSWorld-Verified**：2 篇
- **OSWorld**：2 篇
- **Terminal-Bench 2.1**：2 篇
- **tau-bench retail**：2 篇
- **SWE-bench**：2 篇
- **GAIA**：2 篇
- **IoTGoat**：1 篇
- **Metasploitable2**：1 篇

---
*自动生成于 2026-07-19 | ArXiv_Daily_Digest*