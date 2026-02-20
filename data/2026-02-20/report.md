# 🧪 ArXiv AI 日报

📅 **2026-02-20 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **61,191** (¥0.0198)

## 🔥 今日必读

---

### 1. KLong: Training LLM Agent for Extremely Long-horizon Tasks

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2602.17547v1)

👤 Yue Liu, Zhiyuan Hu, Flood Sung 等


**中文标题**: KLong：面向超长周期任务训练大语言模型智能体
**背景与痛点**: 当前大模型智能体解决长周期任务多依赖免训练的系统级上下文管理方案，仅能优化系统流程无法提升模型内在的长周期任务能力，现有训练方法仅能支持百轮以内交互的常规长任务，无法应对需数百上千轮交互、远超上下文窗口、耗时数小时的超长周期任务（如论文复现、端到端机器学习工程）。
**核心创新**: 本文提出面向超长周期任务的开源大模型智能体KLong，核心思路是先通过轨迹分割监督微调冷启动模型基础能力，再通过渐进式强化学习逐步缩放能力；同时提出全自动的Research-Factory管道，自动生成论文复现任务的高质量训练数据和评估标准，解决超长轨迹无法训练的问题。
**技术细节**: 首先通过Research-Factory自动从顶会收集高质量论文，做测试集去污染后自动生成结构化评估规则，再蒸馏Claude 4.5 Sonnet得到数千条超长交互轨迹。轨迹分割监督微调设计三个核心规则：固定任务说明、论文阅读前缀到每个子轨迹开头，逐步截断后续内容适配上下文窗口，相邻子轨迹保留重叠保证上下文连续性。渐进强化学习分多阶段逐步增加任务允许的最大运行时间，缓解稀疏奖励和信用分配难题，同时优化基础设施解决长任务训练的流水线拥塞问题。
**实验结果**: 在论文复现基准PaperBench上，106B参数的KLong平均得分达到62.59，比1T参数的开源SOTA Kimi K2 Thinking高11.28个百分点；在SWE-bench Verified、MLE-bench、安全编码SEC-bench等多个跨领域长周期任务上均取得一致性能提升，证明能力可有效泛化。

---

### 2. MASPO: Unifying Gradient Utilization, Probability Mass, and Signal Reliability for Robust and Sample-Efficient LLM Reasoning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.17550v1)

👤 Xiaoliang Fu, Jiaye Lin, Yangyi Fang 等


**中文标题**: MASPO：统一梯度利用、概率质量与信号可靠性的鲁棒高效大语言模型推理优化

**背景与痛点**: 针对大语言模型推理优化场景的可验证奖励强化学习（RLVR）范式，现有主流方法GRPO继承了PPO的刚性硬裁剪信任区机制，存在三个核心缺陷：硬裁剪二值截断浪费边界有效梯度、统一比例约束忽略token概率分布差异导致探索失衡、正负样本信噪比不对称引发过拟合和灾难性遗忘。

**核心创新**: 提出质量自适应软策略优化框架MASPO，从概率质量位移和最大熵原理出发重新设计RLVR的信任区约束，将软梯度保留、概率自适应约束、不对称风险控制三个模块统一到单个目标函数中，从根本上修正了原有机制与LLM优化动力学的错配，同步提升了样本效率和训练鲁棒性。

**技术细节**: 首先用可导的单边软高斯门控替换刚性硬裁剪，仅对越界更新做平滑衰减而非直接置零，保留近边界探索的有效梯度，通过停梯度操作保证门控仅做置信权重，不偏移优化目标。其次加入质量自适应限幅，将信任区宽度与原策略token概率成反比调整：给长尾低概率token放宽约束鼓励探索，给高概率头部token收紧约束防止策略坍塌。最后加入不对称风险控制器，给大优势的高价值正样本放宽约束加速学习，给大绝对值负优势的低置信错误样本收紧约束，避免灾难性遗忘。

**实验结果**: 在AIME、AMC、MATH500、奥赛等多个数学推理基准测试，在1.5B、7B、14B不同规模的DeepSeek-Qwen主干模型上，MASPO平均比GRPO提升约2.8-3.0个百分点的平均准确率，训练过程熵更稳定，样本效率和最终性能均优于GRPO、SAPO等一众主流基线方法。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Sink-Aware Pruning for Diffusion Language Models](http://arxiv.org/abs/2602.17664v1) `cs.CL (计算语言学)` | 扩散语言模型存在推理成本过高的痛点，现有剪枝大多沿用自回归LLM的启发式规则，本文提出Sink感知剪枝，针对性优化DLM推理效率。 |
| 5 | [ODESteer: A Unified ODE-Based Steering Framework for LLM Alignment](http://arxiv.org/abs/2602.17560v1) `cs.AI (人工智能)` | 现有推理时LLM对齐的激活转向方法缺乏统一框架，本文提出基于ODE的统一对齐框架ODESteer，轻量高效，推进表示工程方向落地。 |
| 6 | [Modeling Distinct Human Interaction in Web Agents](http://arxiv.org/abs/2602.17588v1) `cs.CL (计算语言学)` | 当前网页Agent缺乏对任务过程中动态人机交互的建模，无法支持人类实时修正偏好与错误，本文提出规范化建模方案，推进人机协作Agent发展。 |
| 7 | [MolHIT: Advancing Molecular-Graph Generation with Hierarchical Discrete Diffusio...](http://arxiv.org/abs/2602.17602v1) `cs.AI (人工智能)` | 分子生成是AI药物研发的核心任务，现有图扩散模型存在结构生成缺陷，本文提出分层离散扩散模型MolHIT，推进AI驱动药物发现发展。 |
| 8 | [When to Trust the Cheap Check: Weak and Strong Verification for Reasoning](http://arxiv.org/abs/2602.17633v1) `cs.LG (机器学习)` | 当前LLM推理普遍内置验证循环，但缺乏低成本弱验证和高成本强验证的选择策略，本文给出决策框架，兼顾推理效率与可靠性。 |
| 9 | [AutoNumerics: An Autonomous, PDE-Agnostic Multi-Agent Pipeline for Scientific Co...](http://arxiv.org/abs/2602.17607v1) `cs.AI (人工智能)` | 传统PDE数值求解依赖大量专家经验与手动调参，本文提出PDE无关的自主多Agent科学计算管线，降低科学计算门槛，创新性突出。 |
| 10 | [Reverso: Efficient Time Series Foundation Models for Zero-shot Forecasting](http://arxiv.org/abs/2602.17634v1) `cs.LG (机器学习)` | 现有时间序列基础模型零样本预测效率偏低，难以满足工业落地需求，本文提出Reverso高效架构，提升零样本时间序列 forecasting的性能效率。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-20
