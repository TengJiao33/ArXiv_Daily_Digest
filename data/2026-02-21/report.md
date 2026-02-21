# 🧪 ArXiv AI 日报

📅 **2026-02-21 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **61,155** (¥0.0198)

## 🔥 今日必读

---

### 1. KLong: Training LLM Agent for Extremely Long-horizon Tasks

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2602.17547v1)

👤 Yue Liu, Zhiyuan Hu, Flood Sung 等


**中文标题**: KLong：面向超长周期任务训练大语言模型智能体

**背景与痛点**: 现有大模型智能体多针对普通长周期任务设计，而复现论文、机器学习工程这类超长周期任务的交互轮次、总耗时达普通任务的10倍，天然超出上下文窗口。现有方案多为系统级上下文优化，无法提升模型内在能力，直接训练存在轨迹过长、奖励稀疏不稳定的问题。

**核心创新**: 提出开源超长周期任务大模型智能体KLong，打造从自动化数据构建到定制化训练的全流程方案，针对超长任务的特性设计了轨迹拆分监督微调与渐进强化学习方案，从训练层面提升模型内在的超长周期任务解决能力。

**技术细节**: 首先通过Research-Factory流水线自动采集顶会论文，去除测试集污染，封禁官方代码避免作弊，自动生成结构化评估标准，蒸馏Claude 4.5 Sonnet得到数千条高质量超长交互轨迹；轨迹拆分SFT为每个子轨迹固定保留开头核心上下文，渐进截断后续内容，子轨迹间保留重叠保证上下文连续性；渐进RL分多阶段逐步延长任务超时，配合异步 partial rollout 解决管线拥塞，提升训练稳定性与资源利用率。

**实验结果**: 在PaperBench、SWE-bench Verified、MLE-bench等5类智能体基准测试，106B参数的KLong在PaperBench上平均得分超出1T参数的Kimi K2 Thinking 11.28个百分点，学到的长周期能力可泛化到其他任务，取得一致性能提升。

---

### 2. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.17550v1)

👤 Xiaoliang Fu, Jiaye Lin, Yangyi Fang 等


**中文标题**: MASPO：统一梯度利用、概率质量与信号可靠性，实现鲁棒且样本高效的大语言模型推理

**背景与痛点**: 本研究针对大语言模型推理优化的主流可验证奖励强化学习（RLVR）范式，指出现有GRPO等方法继承的刚性、均匀、对称信任域机制存在三大缺陷：硬二元截断浪费有效梯度、均匀约束不匹配令牌概率的长尾分布、对称处理忽略正负样本的信噪比差异，导致样本效率低、训练不稳定。

**核心创新**: 提出质量自适应软策略优化（MASPO）框架，首次系统性统一解决上述三类核心优化对齐问题，用连续软约束替代刚性截断，按令牌概率分配探索预算，按信号置信度调整更新幅度，无需额外评论家模型，相比现有GRPO变体实现更稳定高效的推理优化。

**技术细节**: 具体包含三个核心模块：1）软高斯门控：用可导的高斯指数衰减权重替代硬二元截断，对越界样本保留衰减后的非零梯度，引入停梯度保证仅做权重调制不干扰优化；2）质量自适应限制器：信任域宽度与旧策略令牌概率成反比调整，放宽长尾低概率令牌约束鼓励探索，收紧头部高概率令牌约束避免策略坍缩；3）不对称风险控制器：放大难任务正样本更新幅度，收紧简单任务近失负样本的惩罚，避免灾难性遗忘。

**实验结果**: 在AIME、AMC、MATH500等多个数学推理基准测试，基于1.5B/7B/14B不同规模的DeepSeek模型，MASPO相比GRPO平均Avg@32提升约2.8至3个百分点，训练过程保持健康策略熵，跨规模稳定提升性能，样本效率更优。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [MARS: Margin-Aware Reward-Modeling with Self-Refinement](http://arxiv.org/abs/2602.17658v1) `cs.LG (机器学习)` | 针对当前对齐流程中奖励模型可靠性不足的痛点，提出边际感知奖励建模结合自细化框架，改进RLHF/RLAIF核心组件性能。 |
| 5 | [Sink-Aware Pruning for Diffusion Language Models](http://arxiv.org/abs/2602.17664v1) `cs.CL (计算语言学)` | 针对扩散语言模型推理成本过高、现有剪枝沿用自回归LLM启发式不适配的问题，提出Sink感知剪枝，有效提升DLM推理效率。 |
| 6 | [Modeling Distinct Human Interaction in Web Agents](http://arxiv.org/abs/2602.17588v1) `cs.CL (计算语言学)` | 针对当前Web Agent缺乏过程中人类交互建模的痛点，提出建模人类偏好输入与行为纠错的方案，推进实用化Web Agent发展。 |
| 7 | [ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment](http://arxiv.org/abs/2602.17560v1) `cs.AI (人工智能)` | 针对现有激活转向方法缺乏统一框架的问题，提出基于ODE的统一LLM对齐转向框架，为轻量推理时对齐提供新方案。 |
| 8 | [MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusio...](http://arxiv.org/abs/2602.17602v1) `cs.AI (人工智能)` | 针对现有分子图扩散生成的不足，提出分层离散扩散模型MolHIT，提升分子生成质量，推进AI辅助药物发现领域发展。 |
| 9 | [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning](http://arxiv.org/abs/2602.17633v1) `cs.LG (机器学习)` | 针对LLM推理验证环中弱验证和强验证如何选择的痛点，提出决策框架，兼顾推理效率与验证准确性，优化推理验证流程。 |
| 10 | [Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting](http://arxiv.org/abs/2602.17634v1) `cs.LG (机器学习)` | 针对现有时间序列基础模型效率不足的问题，提出高效的Reverso模型，提升零样本预测性能，满足工业场景落地需求。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-21
