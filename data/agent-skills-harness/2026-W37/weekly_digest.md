# Agent Skills 与 Harness — 2026-W37 (09/07-09/13)

本周新增 **101** 篇论文，**10** 篇附带代码。优先级：high 55 / medium 18 / low 28。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skil...](http://arxiv.org/abs/2609.04865v1) | skill generation | CoSkill在ALFWorld达98.4%成功率（+3.5个百分点），WebShop达90... | 将静态元技能转为可学习元技能智能体，通过与推理智能体联合端到端训练，实现分层技能... | 仅在两个中小规模基准验证，未测试大规模复杂任务泛化性，存在落地不... | ✅ |
| 2 | high | - | [ERPBench: Evaluating LLM Agents for Enterprise Decision-Making A...](http://arxiv.org/abs/2609.04667v1) | evaluation/benchmark | 不同竞争生态下领先模型不同，仅21%的问题中两种生态识别出相同任务赢家，Gemini末位率从... | 通过构建标准化双生态评测基准，为企业决策智能体提供表现验证框架，支撑不同模型能力... | 仅在模拟ERP环境中完成评测，未在真实企业业务场景验证，落地有效... | ✅ |
| 3 | high | - | [ExecCritic: Learn to Test, Test to Improve for Coding Agents](http://arxiv.org/abs/2609.09133v1) | agent harness | 分离测试生成与修复可避免误差共模，分角色微调后组合智能体解决率达72.6%，较基线提升11.... | 通过fail-closed harness冻结验证后的测试，分离测试与修复角色，... | 所用骨干模型参数规模较大，未验证小参数模型效果，对低算力部署不够... | ✅ |
| 4 | high | - | [From Interaction Traces to Persistent Skills: Online Evolution f...](http://arxiv.org/abs/2609.04869v1) | skill generation | 经五次空库预热后，全系统在OSWorld四个域平均得分比基线高5.7~18.6个百分点，GI... | 通过构建持久化版本化可复用技能库，基于证据更新技能，无需改动原模型参数，提升Ag... | 技能收益存在领域依赖性，技能版本稳定性随领域变化，重复修订可能无... | ✅ |
| 5 | high | - | [SkillAdam: Stable and Efficient Skill Evolution for Agents](http://arxiv.org/abs/2609.08944v1) | skill generation | 采用Adam风格的自适应优化机制后，技能演化可用更少迭代更低成本获得更稳定更优的性能 | 借助优化记忆积累历史修正稳定更新方向，通过波动率驱动编辑预算自适应控制技能更新幅... | 仅在公开基准测试验证，未在真实工业场景测试，方法的实际落地泛化性... | ✅ |
| 6 | high | - | [A Voice-Interactive Multi-Agent System for Smart Operating Rooms...](http://arxiv.org/abs/2609.11231v1) | agent harness | 基于字节级最长公共前缀复用的KV缓存预热可将重计算开销从约500ms降至数十毫秒，流式解析降... | 通过分层架构设计注册管理可用技能，结合渐进式技能提示动态过滤信息，配合推理优化实... | 仅针对特定手术场景验证，未提及跨场景泛化能力，缺乏真实临床环境的... | — |
| 7 | high | - | [A-JIT: Agentic Just-In-Time Software Construction](http://arxiv.org/abs/2609.10248v1) | agent harness | 将AI智能体与运行时harness集成到应用全生命周期，可实现软件随使用需求动态演进与人机协... | 通过运行时harness集成嵌入式AI智能体，基于实时执行轨迹动态特化软件逻辑，... | 动态生成修改代码未提及验证机制，存在可靠性隐患，且系统动态演进后... | — |
| 8 | high | - | [APPSim-Bench: Bridging Real-world Apps and Reproducible Evaluati...](http://arxiv.org/abs/2609.07712v1) | evaluation/benchmark | 最优模型仅完成50.27%的任务，28.55%的任务无任何智能体解决，失败集中在长流程、数值... | 通过构建带可控后端的模拟移动应用，消除环境随机干扰，支持确定性可复现的智能体评测... | 现有移动GUI智能体性能不足，近三成任务无法完成，远达不到真实场... | — |
| 9 | high | - | [Agentic ML Exploration (A-MLE) for Ads Ranking](http://arxiv.org/abs/2609.08248v1) | agent harness | 在固定智能体循环下，Claude Sonnet、Gemini、GPT系列大模型的执行可靠性和... | 采用分阶段工作流编排，各阶段设置人在回路检查点，依托沙箱执行层调用领域技能管控智... | 不同大模型的执行特性差异大，系统可靠性依赖基座大模型能力，落地稳... | — |
| 10 | high | - | [Artificial Id: Drive and Persistent Alignment in Agentic AI](http://arxiv.org/abs/2609.11911v1) | agent harness | 无通用推理能力、无任务特定目标的小型控制器可通过差异持久化涌现有用自适应控制，持久化也会留存... | 提出人工ID作为智能体自适应内部驱动，通过差异持久化自主决策行为启停，需设置持久... | 仅在小型虚拟实验验证，未实现可扩展方案，离实际工业落地还有较大距... | — |
| 11 | high | - | [Authority Is Not a String: A Capability-Scoped Harness for Promp...](http://arxiv.org/abs/2609.08371v1) | agent harness | CapScope将注入攻击成功率从基线的33-47/75降至3/75，防护提升显著，且任务完... | 在harness层面实现权限控制，将各子智能体能力存储在模型上下文外，每次工具调... | 仅在小规模五类Python编码任务验证，未测试更大规模复杂多任务... | — |
| 12 | high | - | [Auto-RecSys: Harnessing Autonomous Research Agents for Industry-...](http://arxiv.org/abs/2609.10922v1) | agent harness | 随着Auto-RecSys积累的操作手册不断成熟，可显著降低单实验周期人力投入，同时提升自主... | 通过三类harness设计实现分布式异步执行、中心化持久化存储、认知过程分离，结... | 依赖分布式多GPU与多服务器基础设施，未公开大规模落地数据，适配... | — |

## 方法族分布

- **agent harness**：34 篇
- **未分类**：24 篇
- **evaluation/benchmark**：22 篇
- **skill generation**：5 篇
- **survey**：4 篇
- **policy optimization**：3 篇
- **multi-agent coordination**：2 篇
- **tool-use control**：2 篇
- **unlearning/safety**：2 篇
- **other**：1 篇
- **reward learning**：1 篇
- **skill optimization**：1 篇

## 失败模式与风险信号

- LLM生成的决策解释与实际决策行为不一致，解释不可靠
- 该领域LLM应用落地程度极低，绝大多数研究停留在理论阶段，缺乏实际场景验证。
- 现有变点检测要么检测早但冗余告警过多，要么直接检测原始回报容易漏检环境变化
- 浅层检索、平坦技能归纳忽略依赖，导致智能体产生易失败的捷径行为
- 单轮问答格式不符合临床诊断实际，复杂诊断场景下大模型性能不足
- 预执行编排导致的早期错误累积、算力浪费、有效执行进度丢失
- 数据时间污染、多重选择偏差、前瞻错误、实现成本侵蚀收益
- 现有评测无法分离影响智能体表现的设计变量，评估结果不可复现难以审计
- 多智能体成本升高、关联故障，开放世界可靠性不足，缺乏可信授权机制
- 长周期多阶段研工流程高度依赖人工，缺乏自动化协调机制

## 评测信号

- 模型给出的Top3影响因子与实际必要性、充分性得分的斯皮尔曼相关仅约0.35-0.58，一致性较差。
- 从19325个高危CVE得到1033个检测规则打包为172个技能，在14个程序中检出644个带运行时证据的有效漏洞。
- 按证据真实性、部署准备度对现有研究分级，评估了不同方向LLM应用的产业落地成熟度。
- 主要评测不同变点检测方法在检测速度、告警冗余度、变化识别能力之间的性能权衡表现
- 在两个基准分别取得87.31%任务成功率、50.67%精确成功率，步数和无效动作更少，性能显著优于现有基线
- 在两类临床病例数据集上，DMoA相比GPT-4o，诊断准确率提升10.21个百分点，安全率提升11.36个百分点
- 基于不同LLM骨干的评测显示，TROVE相比多个现有基线实现了更优的任务质量与计算效率的权衡。
- 现有AI投资研究普遍存在偏差缺陷，缺乏审计后的实盘记录，无法证明AI可获得持续净投资收益
- 评测不同设计选择（分块方式、检索策略、智能体结构）对仓库级重构任务成功率和单成功任务成本的影响
- 现有研究对智能体动作接口扩展的论证，远充分于任务完成、恢复、授权、独立验证等核心能力。

## 控制机制 / Harness 信号

- 提出黑盒可靠性评测框架，通过受控干预评估解释可靠性，为智能体监督环节提供质量检查依据。
- 采用漏斗形分级管线，先用轻量方法过滤候选，规则引导LLM代理检测，最终经运行时验证和差分测试控制质量。
- 本研究为综述，提出LLM HVAC应用需明确人机决策责任边界，未来需关注运行约束与可验证安全性。
- 提出轻量基于奖励的在线变点检测工具，可可靠识别训练过程中的环境变化，为后续自适应调整提供支撑
- 从执行轨迹蒸馏归纳对齐成功的多级技能，借助验证器反馈优化技能塔，抑制智能体易失败的捷径行为
- 通过结构化辩论的多智能体框架，基于角色交互组织迭代诊断推理，规范推理过程提升诊断性能。
- 通过离线蒸馏历史轨迹得到技能与结果条件转移图，在线基于运行时证据做局部路径验证与编辑，实现自适应编排控制。
- 提出alpha转化链分析框架，明确可信AI投资研究需满足的多项严谨性条件，提升研究可信度
- 通过固定评估环境、隔离各类设计变量，结合AST验证机制，实现重构智能体的可控可复现评估。
- 提出合理授权启发式框架，主张仅在具备可追溯、故障检测、安全恢复、人工校准控制的场景扩展智能体动作范围。

## 可靠性 / 落地风险

- 工业落地中若依赖LLM自生成解释做智能体监控，易因解释不可靠导致错误的监控判断。
- 未与现有工业级漏洞检测方案对比，验证场景规模有限，实用性尚未得到充分检验。
- 现有研究缺乏现场落地验证，无持续运营数据，LLM应用的延迟与安全特性未得到验证。
- 仅在自定义小规模实验环境验证，未在实际大规模多智能体任务中验证方法泛化能力
- 未明确披露方法的算力消耗与可复现细节，缺乏真实工业场景的落地验证
- 依赖更强基础模型与更大token预算，未验证低算力场景，工业落地存在成本压力
- 依赖离线蒸馏的历史工作流轨迹，跨任务泛化性未验证，工业场景轨迹获取成本不明确。
- 现有研究数据污染、评测不严谨，缺乏实盘验证，盈利结论不可靠不可复现
- 仅针对代码重构任务，通用性有待验证，尚未在大规模真实工业场景测试
- 开放场景下可靠性不足，授权边界不清晰，多智能体关联故障风险高，难以直接落地。

## 代码资源

- [DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agen...](https://github.com/IBM/draco.) · 8 stars
- [CoSkill: Joint Reinforcement Learning of Reasoning and Meta-Skill Agents for Hie...](https://github.com/jinyuan-cookie/CoSkill.) · 4 stars
- [SkillAdam: Stable and Efficient Skill Evolution for Agents](https://github.com/ruc-datalab/SkillAdam) · 3 stars
- [ExecCritic: Learn to Test, Test to Improve for Coding Agents](https://github.com/MSR-Orchard/execcritic.) · 1 stars
- [ProMediConv: Benchmarking Proactive Conversational Agents in Legal Dispute Media...](https://github.com/ZsWei66/ProMediConv_repo.) · 1 stars
- [SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction](https://github.com/BokwaiHo/SCAFFOLD) · 1 stars
- [From Interaction Traces to Persistent Skills: Online Evolution for Computer-Use ...](https://github.com/LongtaoHu/Skill-Evo4GUI.)
- [ERPBench: Evaluating LLM Agents for Enterprise Decision-Making Across Competitiv...](https://github.com/GAIR-NLP/erp-bench.)
- [SchemeArena: Factorized Stress Testing of Scheming in LLM Agents](https://github.com/launchnlp/SchemeArena.)
- [Autonomous Chemical Mechanistic Discovery through Agentic Reasoning and Validati...](https://github.com/JetAstra/Arche-Harness.)

## 常见基线方法

- **传统机器学习**：1 篇
- **模型预测控制(MPC)**：1 篇
- **强化学习(RL)**：1 篇
- **基于本体的工具**：1 篇
- **平滑回报基线**：1 篇
- **原始回报直接检测**：1 篇
- **现有基线方法**：1 篇
- **GPT-4o**：1 篇
- **数据集级优化**：1 篇
- **查询级架构选择**：1 篇

## 常用数据集

- **摘要未提及**：3 篇
- **ALFWorld**：2 篇
- **WebShop**：2 篇
- **SWE-bench Verified**：2 篇
- **客户导师推荐合成用例**：1 篇
- **提示有害性风险判断合成用例**：1 篇
- **2022-2026年19325个高危CVE数据集**：1 篇
- **14个待检测目标程序**：1 篇
- **基于多智能体粒子环境的自定义Speaker-Listener环境**：1 篇
- **两种受控非平稳场景**：1 篇

---
*自动生成于 2026-09-13 | ArXiv_Daily_Digest*