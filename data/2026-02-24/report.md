# 🧪 ArXiv AI 日报

📅 **2026-02-24 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **57,724** (¥0.0190)

## 🔥 今日必读

---

### 1. Position: General Alignment Has Hit a Ceiling; Edge Alignment Must Be Taken Seriously

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2602.20042v1)

👤 Han Bao, Yue Huang, Xiaoda Wang 等


**中文标题**: 《观点：通用对齐已经触及天花板，必须重视边缘对齐》

**背景与痛点**: 当前大模型主流对齐范式为通用对齐，通过RLHF、DPO等方法将多元人类价值观压缩为单个标量奖励优化，在价值冲突、多元利益相关方诉求、固有不确定性等复杂真实场景中存在结构性缺陷，会引发价值扁平化、少数观点丢失、不确定性盲视等问题，已经触及理论天花板。

**核心创新**: 本文提出「边缘对齐」全新对齐范式，核心是将对齐从“单轮静态优化任务”重构为“全生命周期动态规范治理问题”，通过保留多维价值结构、支持多元价值表达、引入交互式不确定性澄清机制，从根本上解决通用对齐的结构性缺陷，同时给出了可落地的三阶段七支柱研究框架。

**技术细节**: 边缘对齐框架分为三阶段共七个相互依赖的支柱：第一阶段重构目标结构，包含多目标向量优化逼近帕累托前沿、词典序分层约束保障安全等核心目标的优先级；第二阶段推进规范治理，包含保留多套冲突价值体系、适配不同场景与用户的个性化偏好、用社会选择方法保障偏好聚合的程序正义；第三阶段激活认知能力，包含风险敏感的不确定性量化、主动歧义澄清的交互式协商机制。

**实验结果**: 本文为观点性论文，未开展全新训练测试实验，文献计量分析显示2025年82.9%的大模型对齐研究仍聚焦通用对齐，边缘对齐相关研究才刚刚起步；多个公开行业案例实证了通用对齐的三类结构性缺陷，验证了新范式的必要性。

---

### 2. Agents of Chaos

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2602.20021v1)

👤 Natalie Shapira, Chris Wendler, Avery Yen 等


**中文标题**: 混沌智能体

**背景与痛点**: 现有大语言模型驱动的自主智能体正快速落地，普遍具备工具执行、持久内存、跨渠道多主体交互能力，但现有安全评测多局限于人工约束的基准测试，缺乏真实开放部署环境下的系统性红队探索，集成自主能力后产生的新型安全隐私漏洞尚未得到充分实证研究。

**核心创新**: 本研究是针对自主大模型智能体的探索性实地红队研究，在真实实验室环境部署了带完整系统工具权限的自主智能体，由20名AI研究者开展开放性对抗测试，聚焦智能体集成层而非底层大模型本身的漏洞，首次系统性披露了真实部署场景下多类新型安全风险，填补了领域实证空白。

**技术细节**: 本研究基于OpenClaw智能体框架搭建测试环境，为每个智能体分配独立隔离的云虚拟机，赋予24小时运行权限、持久化存储、Discord公共/私有通信通道、独立ProtonMail邮箱，开放完整shell执行权限，允许智能体自主修改自身配置和内存。底层采用Claude Opus和开源自权重Kimi K2.5两种主流大模型，邀请研究者开展两周开放性测试，整理出成功与失败攻击的典型案例。

**实验结果**: 本研究共验证出11类可被利用的高危漏洞，包括非所有者越权操作、明文敏感信息泄露、资源耗尽型DoS、跨通道身份仿冒绕过验证、多智能体恶意行为传播、间接提示注入持久控权等，实证表明当前自主智能体真实部署中存在大量未被重视的安全风险，亟需系统性应对。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [CodeCompass: Navigating the Navigation Paradox in Agentic Code Intelligence](http://arxiv.org/abs/2602.20048v1) `cs.AI (人工智能)` | 解决了当前代码智能Agent处理百万级token上下文时，难以定位相关代码文件的导航痛点，有效提升大代码Agent的实际可用性，工业价值高 |
| 5 | [How Retrieved Context Shapes Internal Representations in RAG](http://arxiv.org/abs/2602.20091v1) `cs.CL (计算语言学)` | 深入探究了检索到的外部上下文对RAG中LLM内部表示的影响，解答了RAG领域长期模糊的作用机制问题，对RAG优化有基础研究价值 |
| 6 | [Skill-Inject: Measuring Agent Vulnerability to Skill File Attacks](http://arxiv.org/abs/2602.20156v1) `cs.CR (加密与安全)` | 针对当前LLM Agent支持第三方技能扩展的新特性，提出了技能文件攻击的漏洞评测方法，填补了Agent扩展场景下安全研究的空白 |
| 7 | [CausalFlip: A Benchmark for LLM Causal Judgment Beyond Semantic Matching](http://arxiv.org/abs/2602.20094v1) `cs.AI (人工智能)` | 构建了脱离语义匹配陷阱的LLM因果判断评测基准，解决了现有评测无法测出LLM真因果推理能力的问题，推动因果推理领域研究 |
| 8 | [ReSyn: Autonomously Scaling Synthetic Environments for Reasoning Models](http://arxiv.org/abs/2602.20117v1) `cs.AI (人工智能)` | 针对强化学习训练推理模型时合成环境规模不足的问题，提出自主扩展合成环境的方案，降低推理大模型训练成本，可扩展性强 |
| 9 | [NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Pla...](http://arxiv.org/abs/2602.20119v1) `cs.RO (机器人)` | 提出闭环视频语言规划方案，实现零样本长程机器人操纵任务，突破了现有具身智能长程任务泛化能力不足的瓶颈 |
| 10 | [BarrierSteer: LLM Safety via Learning Barrier Steering](http://arxiv.org/abs/2602.20102v1) `cs.LG (机器学习)` | 提出基于学习障碍引导的LLM安全防护方法，缓解了LLM易受对抗攻击、生成违规内容的问题，为大模型安全提供了新思路 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-24
