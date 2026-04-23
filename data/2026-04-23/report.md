# 🧪 ArXiv AI 日报

📅 **2026-04-23 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **60,657** (¥0.0198)

## 🔥 今日必读

---

### 1. SWE-chat: Coding Agent Interactions From Real Users in the Wild

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.20779v1)

👤 Joachim Baumann, Vishakh Padmakumar, Xiang Li 等


**中文标题**: SWE-chat：来自真实用户野外场景的编码智能体交互数据集

**背景与痛点**: 目前AI编码智能体已大规模落地应用，但学界对真实场景下开发者如何与智能体交互、智能体输出的实际使用率和常见失效模式缺乏大规模实证数据。现有基准多为人工整理的离线任务，现有数据集均不包含完整交互轨迹加行级人机代码归属标注，无法支撑对真实开发工作流的研究。

**核心创新**: 推出了首个大规模来自真实开源开发者的编码智能体交互数据集SWE-chat，是可自动持续更新的"活数据集"，首次实现了完整交互日志、智能体工具轨迹和行级人机代码作者归属的结合。基于该数据集完成了首个真实场景下编码智能体使用行为和失效模式的大规模实证分析。

**技术细节**: 数据采集通过开源工具Entire.io CLI，给公开GitHub仓库安装git钩子，由开发者自愿加入，自动记录多类主流编码智能体的完整会话日志，同步关联git diff生成行级人机代码作者归属。当前数据集包含205个公开仓库的6000个会话、6.3万用户prompt、35.5万次工具调用，总计270万日志事件，随后用经过人类验证的LLM完成多维度标注，设计了代码存活率、单位代码成本、漏洞引入率等量化指标。

**实验结果**: 实证分析发现真实编码模式呈两极分化：41%会话为"vibe coding"（智能体贡献99%以上代码），仅23%为纯人工编码。仅44%智能体产出代码最终保留到提交中，vibe coding单位代码成本是协作编码的3倍，引入安全漏洞率是纯人工编码的9倍，用户在44%回合中会对智能体输出进行纠正或打断。

---

### 2. MGDA-Decoupled: Geometry-Aware Multi-Objective Optimisation for DPO-based LLM Alignment

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.20685v1)

👤 Andor Vári-Kakas, Ji Won Park, Natasa Tagasovska


**中文标题**: MGDA-Decoupled：面向基于DPO的大语言模型对齐的几何感知多目标优化

**背景与痛点**: 大语言模型对齐需要同时满足有用性、真实性、无害性等多个潜在冲突目标，现有固定标量化方法会系统性偏向易优化、数据占比高的目标，引发公平性问题；现有几何感知多目标方法要么对梯度幅度敏感，要么依赖RL或额外奖励模型，丢失了DPO轻量高效的优势。

**核心创新**: 提出MGDA-Decoupled算法，将多梯度混合系数计算与最终梯度聚合解耦，通过损失归一化引入目标收敛动态信息，隐式优先优化距离收敛更远的目标，既解决了传统MGDA对小梯度偏置、归一化MGDA丢弃收敛信息的缺陷，又全程基于轻量DPO框架，不需要额外训练组件。

**技术细节**: 训练框架为每个目标维护独立偏好数据集，每步单独计算各目标的DPO梯度与损失，再动态计算梯度混合系数得到更新方向。MGDA-Decoupled将各梯度除以自身当前损失后，在梯度凸包上求解最小模向量得到混合系数，再将系数应用于原始梯度完成更新，隐式给离收敛更远的目标分配更高权重，LLM对齐场景下（通常目标数不超过10个）求解开销可忽略。

**实验结果**: 在标准UltraFeedback多目标对齐数据集测试两个主流开源模型，MGDA-Decoupled获得所有对比方法中最高的整体净胜率：Gemma-2-2B相对SFT基线提升2.3%（统计显著），Qwen2.5-0.5B相对基线提升4.7%（统计显著），多数单目标性能也优于其他对比方法。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Stream-CQSA: Avoiding Out-of-Memory in Attention Computation via Flexible Worklo...](http://arxiv.org/abs/2604.20819v1) `cs.LG (机器学习)` | 针对长上下文大语言模型自注意力二次内存开销导致的OOM问题，提出灵活负载调度方案，降低长上下文模型推理部署门槛，工程价值高 |
| 5 | [OMIBench: Benchmarking Olympiad-Level Multi-Image Reasoning in Large Vision-Lang...](http://arxiv.org/abs/2604.20806v1) `cs.CV (计算机视觉)` | 当前大视觉语言模型的奥林匹克级复杂推理基准缺少多图像场景的专项测评，该工作推出的新基准，能有力推动LVLM复杂推理能力研究 |
| 6 | [Coverage, Not Averages: Semantic Stratification for Trustworthy Retrieval Evalua...](http://arxiv.org/abs/2604.20763v1) `cs.IR` | 针对RAG系统检索评估依赖平均指标、偏差大的痛点，提出语义分层的评估方法，提升检索评估的可靠性，对RAG落地优化有重要价值 |
| 7 | [Can "AI" Be a Doctor? A Study of Empathy, Readability, and Alignment in Clinical...](http://arxiv.org/abs/2604.20791v1) `cs.CL (计算语言学)` | 针对临床大语言模型落地中，沟通符合临床标准的对齐缺乏量化评估的问题，从多维度开展测评，为临床LLM优化提供重要依据 |
| 8 | [Supplement Generation Training for Enhancing Agentic Task Performance](http://arxiv.org/abs/2604.20727v1) `cs.LG (机器学习)` | 针对Agent任务训练计算成本高、随基础模型迭代快速过时的痛点，提出补充生成训练方法，低开销提升大模型Agent任务性能，实用性强 |
| 9 | [ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control](http://arxiv.org/abs/2604.20816v1) `cs.LG (机器学习)` | 针对当前扩散模型偏好对齐仅支持单标量奖励的局限，提出后训练方法实现多目标的连续奖励控制，可满足生成任务多需求平衡，创新性强 |
| 10 | [Diagnosing CFG Interpretation in LLMs](http://arxiv.org/abs/2604.20811v1) `cs.AI (人工智能)` | 面向Agent系统中LLM需要遵循动态定义机器接口的需求，测评了LLM上下文内解释CFG的能力，为Agent工程化优化提供重要参考 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-23
