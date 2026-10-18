# Agent Skills 与 Harness — 2026-W42 (10/12-10/18)

本周新增 **210** 篇论文，**20** 篇附带代码。优先级：high 1 / medium 0 / low 209。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Understanding and Mitigating Cross-Session Attacks via Persisten...](http://arxiv.org/abs/2610.13227v1) | tool-use control | 现有主流代码Agent跨会话技能组合攻击成功率达46.7%-77.4%，所提防御可将其降至1... | 通过恢复工件来源上下文，增加预执行审查环节，保留agent最终执行决策权，防御跨... | 未防护的跨会话持久工件引入隐蔽攻击面，恶意攻击可影响智能体后续正... | — |
| 2 | low | - | [AM-Bench: Understanding Agents under Task Underspecification acr...](http://arxiv.org/abs/2610.18090v1) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 3 | low | - | [APEX: Active Protection at Execution Boundaries for LLM Agents](http://arxiv.org/abs/2610.06966) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 4 | low | - | [Agent-Reflex: Teaching Language Agents to Act Reflectively](http://arxiv.org/abs/2610.17953v1) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 5 | low | - | [AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agent...](http://arxiv.org/abs/2610.13335v1) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 6 | low | - | [BACAM: Behavior-Aware Continual Agent Merging for Multi-Turn Int...](http://arxiv.org/abs/2610.04966) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 7 | low | - | [DRYLAB-Bench: Benchmarking the Biosecurity Risk of Agentic LLM M...](http://arxiv.org/abs/2610.13116v1) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 8 | low | - | [Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiab...](http://arxiv.org/abs/2610.16867) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 9 | low | - | [Inducing Process Supervision from Outcome-Only Reinforcement Lea...](http://arxiv.org/abs/2609.36641) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 10 | low | - | [JevAgentHarness: Benchmarking, Deploying and Training Decision M...](http://arxiv.org/abs/2610.21412v1) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 11 | low | - | [LatentRiskBench: Measuring State-Dependent Risks in Enterprise A...](http://arxiv.org/abs/2610.17685) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |
| 12 | low | - | [MASBench: Benchmarking LLM-based Multi-Agent Collaboration under...](http://arxiv.org/abs/2610.04672) | 未分类 | 提取失败 | 提取失败 | 提取失败 | ✅ |

## 方法族分布

- **未分类**：209 篇
- **tool-use control**：1 篇

## 失败模式与风险信号

- 跨会话持久工件导致恶意效应跨技能执行传播，引发各类安全后果

## 评测信号

- 所提防御将整体攻击成功率从69.5%降至10.9%，同时将合法任务完成率从79.6%提升至87.5%。

## 控制机制 / Harness 信号

- 通过恢复工件来源上下文，增加预执行审查环节，保留agent最终执行决策权，防御跨会话攻击。

## 可靠性 / 落地风险

- 未防护的跨会话持久工件引入隐蔽攻击面，恶意攻击可影响智能体后续正常执行，带来安全隐患。

## 代码资源

- [Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Polic...](https://github.com/Alibaba-NLP/qqr.) · 317 stars
- [OpenGameEval: Benchmarking Agentic Programming and Exploration in a Stateful Gam...](https://github.com/Roblox/open-game-eval.) · 73 stars
- [Agent-Reflex: Teaching Language Agents to Act Reflectively](https://github.com/RUC-NLPIR/Agent-Reflex.) · 20 stars
- [Work2Skill: Capturing Human GUI Experience for Reusable Agent Skill Induction](https://github.com/china-qijizhifeng/Work2Skill.) · 13 stars
- [AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents](https://github.com/Lexsi-Labs/AgentTune) · 9 stars
- [Self-Evolving Agent Harness](https://github.com/zgcagi/Harness-RSI.) · 4 stars
- [MASBench: Benchmarking LLM-based Multi-Agent Collaboration under Partial Observa...](https://github.com/BUPT-GAMMA/MASBench) · 4 stars
- [JevAgentHarness: Benchmarking, Deploying and Training Decision Models That Share...](https://github.com/JevAgentHarness/JevAgentHarness.) · 3 stars
- [BACAM: Behavior-Aware Continual Agent Merging for Multi-Turn Interaction](https://github.com/shuaitongli/BACAM.) · 3 stars
- [Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation of Small Languag...](https://github.com/waldiez/slm-callsite-eval.) · 2 stars

## 常见基线方法

- **Codex CLI**：1 篇
- **Gemini CLI**：1 篇
- **Claude Code**：1 篇

## 常用数据集

- **SkillRelayBench**：1 篇

---
*自动生成于 2026-10-18 | ArXiv_Daily_Digest*