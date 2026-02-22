# 🧪 ArXiv AI 日报

📅 **2026-02-22 周日** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **61,688** (¥0.0201)

## 🔥 今日必读

---

### 1. KLong: Training LLM Agent for Extremely Long-horizon Tasks

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2602.17547v1)

👤 Yue Liu, Zhiyuan Hu, Flood Sung 等


**中文标题**: KLong：面向超长周期任务的大语言模型智能体训练

**背景与痛点**: 当前大语言模型智能体应对超长周期任务（如复现顶会论文、完成机器学习工程全流程）存在显著短板：这类任务交互轮次是普通长周期任务的10倍，天然超出模型上下文窗口限制；现有方案多为系统级上下文管理，不提升智能体原生能力，现有训练方案也仅支持百轮以内交互，无法适配真实场景。

**核心创新**: 本文提出开源KLong智能体，针对超长周期任务设计了从数据生成到训练的全流程方案：自动构建高质量复现论文训练数据的Research-Factory流水线，搭配轨迹拆分监督微调、渐进强化学习两大训练技术，解决了超长轨迹超出上下文窗口、强化学习稀疏不稳定的核心问题，能力可跨任务泛化。

**技术细节**: 数据层面，Research-Factory自动从顶会收集筛选论文，去除测试集污染，封禁原官方代码避免作弊，自动生成结构化评估标准，再蒸馏Claude 4.5 Sonnet得到数千条高质量超长轨迹。训练分两步：1）轨迹拆分监督微调，固定开头任务/论文阅读前缀保留全局信息，对后续内容渐进截断，子轨迹间保留重叠保证上下文连贯，将可支持交互轮次从115轮提升到732轮；2）渐进强化学习，分阶段逐步延长任务超时限制，解决奖励稀疏问题，同时优化调度解决资源拥塞。

**实验结果**: 在PaperBench、SWE-bench Verified、MLE-bench等5个长周期智能体基准测试，106B参数的KLong在PaperBench上平均得分超过1T参数的Kimi K2 Thinking 11.28个百分点，在软件工程、机器学习工程、代码安全等多个任务上均实现一致性能提升，验证了方法的有效性和跨任务泛化性。

---

### 2. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.17550v1)

👤 Xiaoliang Fu, Jiaye Lin, Yangyi Fang 等


**中文标题**: MASPO：统一梯度利用、概率质量与信号可靠性的鲁棒样本高效大语言模型推理
**背景与痛点**: 针对大语言推理任务的可验证奖励强化学习（RLVR），主流方法GRPO沿用PPO的刚性硬截断、均匀对称置信域机制，存在三大缺陷：硬截断浪费越界有效梯度、统一约束忽略token分布头尾概率差异、对称更新不区分正负样本信噪比差异，导致训练低效、性能上限低。
**核心创新**: 提出质量自适应软策略优化MASPO，从梯度、概率、信号三个维度统一解决现有方法的优化错配问题，将刚性置信域改造为连续自适应软约束，同时适配token概率分布和反馈信号置信度，是鲁棒高效的一站式RLVR改进方案。
**技术细节**: 核心包含三个协同模块：1）可微软高斯门控，仅对越界更新做平滑梯度衰减，保留近边界探索样本的有效梯度，解决硬截断的梯度浪费问题；2）质量自适应限制器，将置信域宽度与旧策略token概率成反比调整，给长尾低概率token放宽约束鼓励探索，给头部高概率token收紧约束防止策略坍缩；3）不对称风险控制器，放大难题正确样本的更新步长加速学习，压缩简单歧义负样本的更新步长避免灾难性遗忘。
**实验结果**: 在AIME、AMC、MATH500等多个数学推理基准测试，覆盖1.5B、7B、14B三种尺度模型，相比GRPO平均准确率提升2.8-3个百分点，Pass@32提升2.6-3.7个百分点，训练熵更稳定，收敛更快，性能显著优于所有对比的GRPO改进基线。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [MARS: Margin-Aware Reward-Modeling with Self-Refinement](http://arxiv.org/abs/2602.17658v1) `cs.LG (机器学习)` | 针对RLHF等LLM对齐流程中奖励模型训练不可靠的核心痛点，提出边际感知奖励建模加自精炼框架，能有效提升对齐流程的稳定性和最终效果。 |
| 5 | [ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment](http://arxiv.org/abs/2602.17560v1) `cs.AI (人工智能)` | 针对当前基于激活转向的LLM推理时对齐缺乏统一框架的问题，提出基于ODE的统一 steering 框架，实现轻量化对齐，创新性较强。 |
| 6 | [Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting](http://arxiv.org/abs/2602.17634v1) `cs.LG (机器学习)` | 针对时间序列基础模型零样本推理效率低的痛点，提出高效的Reverso架构，优化缩放效率，提升零样本时序预测性能，工业应用价值高。 |
| 7 | [The Cascade Equivalence Hypothesis: When Do Speech LLMs Behave Like ASR$\rightar...](http://arxiv.org/abs/2602.17598v1) `cs.CL (计算语言学)` | 提出语音大模型的级联等价假设，通过分析证明多数现有语音LLM在常见任务中等价于Whisper+LLM级联 pipeline，对该领域研究有重要启发。 |
| 8 | [MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusio...](http://arxiv.org/abs/2602.17602v1) `cs.AI (人工智能)` | 针对AI药物研发中分子图生成的质量痛点，提出分层离散扩散模型MolHIT，改进分子生成的结构合理性，对AI药物发现方向实用价值高。 |
| 9 | [FAMOSE: A ReAct Approach to Automated Feature Discovery](http://arxiv.org/abs/2602.17641v1) `cs.LG (机器学习)` | 针对表格机器学习领域特征工程的长期瓶颈，结合ReAct Agent框架实现自动化特征发现，能在指数级特征空间高效搜索，实用性很强。 |
| 10 | [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning](http://arxiv.org/abs/2602.17633v1) `cs.LG (机器学习)` | 针对当前LLM推理验证流程中弱验证（低成本）和强验证（高成本）的选择问题，提出决策框架平衡成本和可靠性，助力工业系统降本增效。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-22
