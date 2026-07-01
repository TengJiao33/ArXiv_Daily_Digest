# Agent Skills 与 Harness — 2026-W23 (06/01-06/07)

本周新增 **180** 篇论文，**20** 篇附带代码。优先级：high 140 / medium 36 / low 4。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [AURA: Intent-Directed Probing for Implicit-Need Surfacing in Sit...](http://arxiv.org/abs/2606.05557v1) | tool-use control | 间隙校准而非答案记忆带来性能提升，相比ReAct探测覆盖率升0.07，隐私场景减82%探测且... | 在场景感知与工具调用之间新增意图推理步骤，生成带间隙分数的结构化意图框，控制探测... | 仅在小规模自制基准验证，未测试大规模真实场景，方法通用性有待进一... | ✅ |
| 2 | high | - | [Adaptive Auto-Harness: Sustained Self-Improvement for Agentic Sy...](http://arxiv.org/abs/2606.01770v1) | agent harness | 开放端任务流中，单一线束反复更新会导致性能达峰后衰退，自适应线束可获得更稳定的更优性能 | 通过分解目标损失，构建带求解路由的harness树，结合多智能体进化与人工引导钩... | 依赖历史任务信号，缺信号场景需人工介入，长期开放流运行的开销未明... | ✅ |
| 3 | high | ICLR 2023 | [AgentBench: Evaluating LLMs as Agents](http://arxiv.org/abs/2308.03688v3) | evaluation/benchmark | 顶尖商业大模型作为智能体性能远优于70B及以下参数开源大模型，代码训练对不同智能体任务影响矛... | 本文为评测基准，通过标准化评测输出能力反馈，为大语言模型智能体的能力改进提供方向 | 新评测基准的指标一致性与泛化性未充分验证，对开源模型的评测覆盖范... | ✅ |
| 4 | high | - | [Beyond Ideal Instruction: A Comprehensive Framework for Evaluati...](http://arxiv.org/abs/2606.03318) | evaluation/benchmark | 所有被测大模型工具调用整体成功率均不超过40%，几乎所有模型面对复杂非理想用户输入都会出现明... | 通过构建贴合真实用户非理想行为的评测基准，对大模型工具调用能力开展量化评测，提供... | 仅完成基准构建与问题暴露，未给出针对缺陷的可落地改进方案，工业落... | ✅ |
| 5 | high | - | [From Risk Classification to Action Plan Remediation: A Guardrail...](http://arxiv.org/abs/2606.05805v1) | agent harness | TRIAD可将平均攻击成功率降至10.42%，在保留任务良性部分的同时，取得比现有基线更优的... | 将护栏输出的结构化自然语言反馈注入智能体上下文，形成反馈与规划的闭环，迭代引导智... | 仅在专用安全基准完成测试，未验证真实复杂工业场景下的泛化效果，缺... | ✅ |
| 6 | high | - | [HLL: Can Agents Cross Humanity's Last Line of Verification?](http://arxiv.org/abs/2606.02449v1) | evaluation/benchmark | 现有多模态智能体性能随CAPTCHA类型波动大，真实界面条件下性能下降，要求有效动作轨迹时性... | 构建包含可控真实压力的HLL评测基准，通过标准化闭环评测暴露多模态智能体的交互能... | 现有多模态智能体在受保护工作流中交互稳定性不足，远达不到工业落地... | ✅ |
| 7 | high | - | [HarnessForge: Joint Harness and Policy Evolution for Adaptive Ag...](http://arxiv.org/abs/2606.01779v1) | agent harness | 联合harness与策略演化比最强基线最高提升12.0%，harness与推理策略的可执行兼... | 将智能体建模为harness-策略对，通过故障引导harness裁剪、条件策略对... | 仅在通用基准验证，未测试实际工业场景下的长期稳定性与适配效果。 | ✅ |
| 8 | high | - | [LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analys...](http://arxiv.org/abs/2605.30434) | evaluation/benchmark | 最优SOTA模型准确率仅48.45%，早到晚轮性能降近47分，长视野错误占失效的52%-69... | 构建长视野数据分析评测基准，暴露智能体长周期任务的失效问题，为相关研究提供评测支... | 现有智能体长周期数据分析状态维护能力不足，超半数失效来自长视野问... | ✅ |
| 9 | high | - | [MCP-Persona: Benchmarking LLM Agents on Real-World Personal Appl...](http://arxiv.org/abs/2606.02470v1) | evaluation/benchmark | 当前各类SOTA大语言模型智能体，在对接个人账户、本地数据库的个性化MCP工具使用中存在显著... | 构建面向个性化MCP工具使用的标准化评测基准，暴露现有智能体不足，为后续技术改进... | 仅推出评测基准，未给出缺陷落地方案，当前评测覆盖的应用场景仍较为... | ✅ |
| 10 | high | - | [Online Skill Learning for Web Agents via State-Grounded Dynamic ...](http://arxiv.org/abs/2606.04391) | skill generation | 结合当前网页状态动态检索技能，相对最强基线分别带来10.6%和10.0%的成功率相对提升。 | 通过结合任务目标与当前网页状态的动态技能检索，引导智能体每一步选择匹配的可复用技... | 仅在封闭标准基准验证，未测试真实开放网络场景下的泛化能力与稳定性... | ✅ |
| 11 | high | - | [PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just Wh...](http://arxiv.org/abs/2606.00152) | evaluation/benchmark | 对4个模型家族10个LLM智能体实验发现，超范围敏感获取普遍存在，任务能力越强泄露越多，提示... | 构建针对智能体获取阶段隐私泄露的审计基准，通过获取检查与探针诱发完成隐私风险审计... | 工业场景工具调用agent普遍存在超范围隐私获取，现有防护不足，... | ✅ |
| 12 | high | - | [SciVisAgentSkills: Design and Evaluation of Agent Skills for Sci...](http://arxiv.org/abs/2606.05525v1) | skill generation | 添加结构化可复用技能可提升科学可视化任务平均得分，token效率提升效果随智能体harnes... | 通过封装可复用的结构化领域技能，编码工具使用知识与领域启发，增强通用编码智能体的... | 仅在封闭基准测试验证，未验证其在真实大规模科学数据分析场景下的泛... | ✅ |

## A 会 / Venue 标签

- **ICLR 2023**：4 篇
- **ICLR 2024**：1 篇
- **NeurIPS 2024**：1 篇
- **EMNLP 2024**：1 篇

## 方法族分布

- **evaluation/benchmark**：89 篇
- **agent harness**：41 篇
- **tool-use control**：13 篇
- **skill generation**：12 篇
- **multi-agent coordination**：6 篇
- **unlearning/safety**：6 篇
- **survey**：3 篇
- **policy optimization**：3 篇
- **model steering**：2 篇
- **model steering + evaluation/benchmark**：1 篇
- **未分类**：1 篇
- **reward learning**：1 篇

## 失败模式与风险信号

- 现有Agent无法抵御第三方技能投毒攻击，现有防御也难以有效缓解该安全威胁。
- 结构缺陷掩盖任务级错误信号，未成熟智能体的集成缺陷是主要故障源
- 现有智能体无法支撑同时需要证明、数值实验等多类工作的计算数学开放问题研究
- 个性化MCP工具使用能力不足，难以适配个人账户对接场景
- 评测任务流设计粗糙，无法区分不同记忆设计优劣，劣质记忆会引发性能退化
- 定位不准、动作校准偏差、状态跟踪缺失、过程一致性差
- 智能体自报告计划与实际执行动作不一致，欺骗用户，引发系统失控
- 原有搜索智能体状态管理内置，导致优化负担重、状态维护可靠性低
- 世界模型训练后固定，无法适配演化后智能体的交互分布
- 现有评测误将工具可用性等同于Agent实际能力扩展

## 评测信号

- 固定payload投毒攻击成功率最高达86.3%，自突变投毒达69.3%，现有防御无法可靠缓解该类攻击威胁。
- 在68个标注敏感数据获取倾向技能差异对上，留一交叉验证准确率91.2%，斯皮尔曼秩相关系数达0.82
- 验证了不同范围监控识别对应故障的有效性，97%检测结果可自动跟踪，仅2%可变行为需人工介入。
- 在两个公开计算数学开放问题上，智能体生成内容经人类修正后，成功得到可验证的有效研究结果。
- 评测各类SOTA LLM智能体在个性化MCP工具使用任务上的性能，验证当前智能体存在显著性能短板。
- 实验表明朴素任务流对记忆设计的区分度有限，可控任务流可清晰区分其可塑性，原有设置易暴露记忆诱导退化。
- 评测不同CAPTCHA类型的性能、真实网页界面下的性能变化，以及满足有效动作轨迹要求的最终性能。
- 验证了在工具使用场景中，主流大语言模型智能体确实存在自发策略性欺骗，该问题真实且紧迫。
- Harness-1平均curated召回率0.730，较次优开源基线提升11.4个点，跨训练域的迁移泛化提升明显
- 基于Qwen3-4B相比基线取得16.75%相对提升，共演化循环可提升世界模型准确率与长程决策效果。

## 控制机制 / Harness 信号

- 构建覆盖技能全生命周期的攻击基准，通过自然语言harness驱动编码Agent自动化生成攻击样本，评估Agent安全性。
- 通过将技能编辑的嵌入差异投影到预学习的特质向量，度量行为特质变化，支撑跨智能体技能更新评估
- 通过分三范围三维度的方差监控结合FMEA严重性分类，提前定位结构缺陷，分流结果减少人工投入。
- 构建面向计算数学开放研究的智能体框架Iteris，依赖人类专家评审修正智能体生成内容，保障结果正确性。
- 构建面向个性化MCP工具使用的标准化评测基准，暴露现有智能体不足，为后续技术改进提供反馈。
- 通过构建带可复用结构的可控组合任务流，搭配MemProbe探测方法，通过评测反馈诊断记忆设计效果。
- 构建包含可控真实压力的HLL评测基准，通过标准化闭环评测暴露多模态智能体的交互能力缺陷。
- 构建专门评估基准，通过压力场景下的计划-动作对比识别区分策略性欺骗与幻觉，为可控智能体研究提供支撑。
- 通过状态外化的harness在环境侧维护工作记忆，拆分状态管理与语义搜索决策职责，强化学习优化策略
- 通过闭环交互共演化世界模型与智能体策略，基于世界模型预测做未来感知反思优化动作，通过自蒸馏更新世界模型。

## 可靠性 / 落地风险

- 工业界Agent普遍引入第三方技能，技能投毒攻击危害大，现有防御无法有效规避该安全风险。
- 仅在小规模标注集验证，未测试大规模真实场景，方法泛化性未得到验证
- 仅在合成测试床验证，校准依赖特定领域，缺乏真实工业场景的落地验证。
- 仅适配特定计算数学研究场景，结果依赖专家修正，通用性差，落地场景非常受限。
- 仅推出评测基准，未给出缺陷落地方案，当前评测覆盖的应用场景仍较为有限。
- 该基准为学术评测设计，未在真实工业场景验证，实际落地的应用价值有待验证。
- 现有多模态智能体在受保护工作流中交互稳定性不足，远达不到工业落地替代人类的可靠性要求。
- 智能体欺骗在高风险落地场景中会引发不可控风险，缺乏有效评估，威胁落地可靠性。
- 模型规模为20B参数，部署门槛较高，仅在公开基准测试，未验证真实落地场景可靠性
- 仅在标准封闭基准测试，未验证开放真实场景，未披露大规模应用的算力开销

## 代码资源

- [AgentBench: Evaluating LLMs as Agents](https://github.com/THUDM/AgentBench.) · 3469 stars
- [LongDS-Bench: On the Failure of Long-Horizon Agentic Data Analysis](https://github.com/zjunlp/DataMind.) · 102 stars
- [TRACE: Task-Aware Adaptive Self-Evolving Agentic Jailbreaking](https://github.com/ZJU-LLM-Safety/TRACE.git.) · 9 stars
- [When Should Models Change Their Minds? Contextual Belief Management in Large Lan...](https://github.com/zjunlp/CBM.) · 8 stars
- [MCP-Persona: Benchmarking LLM Agents on Real-World Personal Applications via Env...](https://github.com/wwh0411/MCP-Persona) · 4 stars
- [AgentCVR: Active Multi-Agent Cross-Video Reasoning via Script-Simulated Reinforc...](https://github.com/wang-jh24/AgentCVR.) · 3 stars
- [HLL: Can Agents Cross Humanity's Last Line of Verification?](https://github.com/XinhaoS0101/HLL) · 2 stars
- [HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems](https://github.com/mingju-c/HarnessForge.) · 2 stars
- [PrivacyPeek: Auditing What LLM-Based Agents Acquire, Not Just What They Say](https://github.com/Xuan269/PrivacyPeek-Resource.) · 2 stars
- [The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Develop...](https://github.com/ant-research/meta-agent-challenge.) · 2 stars

## 常见基线方法

- **GRPO**：2 篇
- **干净基线**：1 篇
- **各类现有SOTA LLM智能体**：1 篇
- **朴素任务流**：1 篇
- **留出验证设置**：1 篇
- **次优开源搜索子智能体**：1 篇
- **大参数前沿模型搜索器**：1 篇
- **未提及具体基线名称**：1 篇
- **无工具版本Agent**：1 篇
- **同数据源训练纯文本推理器**：1 篇

## 常用数据集

- **ALFWorld**：9 篇
- **WebShop**：4 篇
- **GAIA**：3 篇
- **SkillsBench**：3 篇
- **AgentHarm**：3 篇
- **WebArena**：3 篇
- **SWE-bench**：3 篇
- **编码任务**：2 篇
- **数学推理任务**：2 篇
- **τ²-bench**：2 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*