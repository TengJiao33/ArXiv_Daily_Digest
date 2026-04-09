# 🧪 ArXiv AI 日报

📅 **2026-04-09 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **32,860** (¥0.0117)

## 🔥 今日必读

---

### 1. How Much LLM Does a Self-Revising Agent Actually Need?

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.07236v1)

👤 Seongwoo Jeong, Seonil Son


**中文标题**: 自修正智能体到底需要多少大语言模型？

**背景与痛点**: 当前主流LLM智能体普遍将世界建模、规划、反思等能力全部封装在单LLM推理循环内，各模块的能力贡献相互纠缠，无法量化区分“智能体能力来自LLM本身还是外部显式结构”，该核心科学问题一直缺乏可实证的研究框架。

**核心创新**: 提出声明式反射运行时协议，将智能体能力解耦为后验信念跟踪、显式世界建模规划、符号回合内反思、稀疏LLM修正四个可独立测量的层级，把原本隐式的反思过程转化为可观测、可消融的显式运行时结构，实现了LLM边际贡献的直接测量。

**技术细节**: 协议包含四大核心要素：显式存储的世界状态、预测记录与置信状态，从状态确定性计算的置信信号，带前置条件的守卫修正动作，用于动作预评估的假设状态转移。基于该协议构建了四组递进对比智能体，可单独消融每个模块的边际贡献，无需全程依赖LLM推理。

**实验结果**: 在带0.1噪声的协作战舰测试集上完成54局实验，显式世界建模相比贪婪基线胜率提升24.1个百分点、F1提升0.017；纯符号反思可正常运行但当前预设无聚合净收益；仅4.3%步数调用LLM的稀疏修正仅让F1微涨0.005，胜率反而下降，LLM贡献呈非单调性。

---

### 2. Personalized RewardBench: Evaluating Reward Models with Human Aligned Personalization

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.07343v1)

👤 Qiyao Ma, Dechen Gao, Rui Cai 等


**中文标题**: 个性化RewardBench：基于人类对齐个性化的奖励模型评估
**背景与痛点**: 随着大语言模型多元对齐发展，捕捉用户个性化偏好成为奖励模型的核心需求，但现有奖励模型评估基准多围绕通用回答质量设计，正负样本差异混淆了通用质量与个人偏好，且普遍缺乏基准性能与下游真实任务表现的相关性验证，存在严重的评估代理偏差。
**核心创新**: 本文提出首个严格评估奖励模型个性化能力的专用基准，核心设计思路是将偏好差异严格限定在对用户个性化规则的遵守上，正负样本保持同等的通用回答质量，从设计根源上隔离了通用质量对个性化能力评估的干扰，同时验证了基准性能对下游任务表现的高预测性。
**技术细节**: 该基准基于LaMP-QA数据集构建，选取艺术娱乐、生活个人发展、社会文化三个高个性化需求的主观领域，通过检索用户历史交互生成用户画像；利用大模型生成偏好对：正样本要求严格符合用户个性化规则，负样本要求刻意避开规则，人工验证确认正负样本通用质量接近，仅个性化对齐存在显著差异；评估以排序准确率为核心指标，额外设计规划模块将原始用户画像转化为结构化规则，解决训练测试不匹配问题。
**实验结果**: 测试近20款当前SOTA奖励模型，最优模型准确率仅75.94%，相比先知模型超过97%的准确率存在20%以上的性能缺口，证明现有奖励模型个性化能力严重不足；相关性验证显示，该基准排名与下游Best-of-N、PPO任务表现的相关性远高于现有同类基准，是更可靠的评估代理。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [A Systematic Study of Retrieval Pipeline Design for Retrieval-Augmented Medical ...](http://arxiv.org/abs/2604.07274v1) `cs.CL (计算语言学)` | 面向医疗问答这一重要落地场景，系统研究RAG流水线各模块设计的影响，总结实践经验，对医疗RAG落地开发有很高指导价值 |
| 5 | [TraceSafe: A Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling ...](http://arxiv.org/abs/2604.07223v1) `cs.CR (加密与安全)` | 针对LLM Agent工具调用的安全痛点，首次系统评估多步执行轨迹上安全护栏的效果，指出现有防护缺陷，为Agent安全设计提供重要参考 |
| 6 | [MoRight: Motion Control Done Right](http://arxiv.org/abs/2604.07348v1) `cs.CV (计算机视觉)` | 针对可控视频生成的核心痛点运动控制，实现了任意视点下解耦控制和物理一致的运动生成，推动可控视频生成技术落地发展 |
| 7 | [Measurement of Generative AI Workload Power Profiles for Whole-Facility Data Cen...](http://arxiv.org/abs/2604.07345v1) `eess.SY` | 针对生成AI快速增长带来的数据中心基建规划痛点，实测生成AI负载的完整功耗特征，为全设施数据中心规划提供关键数据支撑 |
| 8 | [Joint Optimization of Reasoning and Dual-Memory for Self-Learning Diagnostic Age...](http://arxiv.org/abs/2604.07269v1) `cs.CL (计算语言学)` | 面向LLM临床诊断Agent，提出联合优化推理与双记忆的自学习框架，模拟人类医生积累经验的过程，提升诊断能力，医疗落地价值高 |
| 9 | [OpenSpatial: A Principled Data Engine for Empowering Spatial Intelligence](http://arxiv.org/abs/2604.07296v1) `cs.CL (计算语言学)` | 空间智能是当前AI前沿方向，现有研究缺少跨领域通用数据支撑，该工作提出标准化空间智能数据引擎，填补缺口推动领域研究发展 |
| 10 | [Splats under Pressure: Exploring Performance-Energy Trade-offs in Real-Time 3D G...](http://arxiv.org/abs/2604.07177v1) `cs.GR` | 针对3D高斯Splatting在边缘端部署的痛点，系统探究受限GPU预算下性能与能耗的权衡，为3DGS的边缘端落地提供重要设计参考 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-09
