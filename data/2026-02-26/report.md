# 🧪 ArXiv AI 日报

📅 **2026-02-26 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **65,832** (¥0.0210)

## 🔥 今日必读

---

### 1. SWE-Protégé: Learning to Selectively Collaborate With an Expert Unlocks Small Language Models as Software Engineering Agents

🏷️ `cs.SE (软件工程)` | 📄 [arXiv](http://arxiv.org/abs/2602.22124v1)

👤 Patrick Tser Jern Kon, Archana Pradeep, Ang Chen 等


**中文标题**: SWE-Protégé：学习与专家选择性协作解锁小语言模型成为软件工程智能体

**背景与痛点**: 长周期软件工程任务（如GitHub真实问题修复）当前依赖大语言模型才能达到高性能，小语言模型（≤10B参数）具备部署成本低、推理延迟低、易微调适配的优势，但在该类任务上普遍存在动作退化循环、长期推进停滞的问题，即使采用大模型轨迹蒸馏方案，性能仍大幅落后，7B参数小模型原有SOTA Pass@1仅17%左右。

**核心创新**: 提出专家-徒弟结对编程的全新范式，将软件修复问题重构为协作问题：让小语言模型保留全部决策主导权，仅在自身进度停滞时选择性调用强专家大模型获得帮助，通过两阶段训练让小模型自主学会识别停滞状态、合理发起请求、忠实执行专家指导，以极低的专家成本获得接近大模型的性能。

**技术细节**: 仅在标准SWE-agent框架中新增ask_expert工具扩展动作空间，采用两阶段后训练：第一阶段对专家大模型生成的带自然专家交互的轨迹做监督微调，让小模型学会专家调用的交互格式与逻辑；第二阶段采用GRPO强化学习，设计复合奖励：显性惩罚重复动作的退化循环，复用专家作为隐形裁判，对不必要调用、不遵循指导的行为做惩罚，采用分阶段课程训练，先消除循环再优化多轮协作。

**实验结果**: 在标准基准SWE-bench Verified测试，基于Qwen2.5-Coder-7B训练得到的SWE-Protégé达到42.4% Pass@1，相比原小模型SOTA提升25.4个百分点，性能反超此前32B开源自模型；平均每任务仅调用专家4次，专家token仅占总token的11%，推理成本相比全专家执行降低4.2到8.2倍，性价比优势显著。

---

### 2. GUI-Libra: Training Native GUI Agents to Reason and Act with Action-aware Supervision and Partially Verifiable RL

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.22190v1)

👤 Rui Yang, Qianhui Wu, Zhaoyang Wang 等


**中文标题**: GUI-Libra：基于动作感知监督和部分可验证强化学习训练原生GUI智能体推理与行动
**背景与痛点**: 开源原生GUI智能体在需要多步推理的长周期导航任务上远落后于闭源系统，核心缺陷一是缺乏动作对齐的高质量推理数据，二是现有训练 pipeline 存在固有问题：带长思维链的监督微调会损害视觉定位精度，分步强化学习存在部分可验证性歧义——同一状态多个合法动作仅认可标注动作，导致奖励噪声大，离线指标无法预测在线任务表现。
**核心创新**: 提出一套面向原生GUI智能体的定制化后训练框架，同时开源81K高质量动作对齐GUI推理数据集，针对性解决了推理能力和定位精度的冲突，以及部分可验证奖励下强化学习不稳定、离线在线性能不对齐的问题，无需昂贵的在线环境交互就能获得显著性能提升。
**技术细节**: 整体为两阶段训练流程：首先基于现有开源轨迹做推理增强，经过动作一致性过滤、坐标对齐验证得到81K高质量SFT数据和40K平衡化RL子集；第一阶段动作感知监督微调，混合推理后动作、直接动作两种监督样本，给动作token和定位坐标token施加更高权重，缓解长思维链带来的定位退化；第二阶段强化学习采用带KL正则的GRPO，约束策略漂移，同时提出成功自适应负梯度缩放，对模糊负梯度降权，缓解奖励歧义。
**实验结果**: 在AndroidWorld、WebArena-Lite-v2、Online-Mind2Web等主流web和移动端基准测试，GUI-Libra-4B/8B相对对应基模型，在线任务成功率分别提升最高+15.6%和+12.2%，中小参数开源模型就能达到甚至超过大参数模型和闭源系统的性能，数据效率和参数效率优异。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Provable Last-Iterate Convergence for Multi-Objective Safe LLM Alignment via Opt...](http://arxiv.org/abs/2602.22146v1) `cs.LG (机器学习)` | 针对多目标安全LLM对齐问题，提出基于乐观原始对偶的方法，实现可证明的最后迭代收敛，为LLM对齐提供理论保障，是对齐领域重要理论进展 |
| 5 | [NoLan: Mitigating Object Hallucinations in Large Vision-Language Models via Dyna...](http://arxiv.org/abs/2602.22144v1) 💻 `cs.CV (计算机视觉)` | 针对大视觉语言模型的物体幻觉核心痛点，提出通过动态抑制语言先验缓解幻觉，方案简单有效，直击多模态大模型落地的关键问题，实用性强 |
| 6 | [DySCO: Dynamic Attention-Scaling Decoding for Long-Context LMs](http://arxiv.org/abs/2602.22175v1) 💻 `cs.CL (计算语言学)` | 针对长上下文语言模型随上下文长度增加精度下降的痛点，提出动态注意力缩放解码方法，无需改动模型就能提升长上下文推理性能，高效实用 |
| 7 | [When AI Writes, Whose Voice Remains? Quantifying Cultural Marker Erasure Across ...](http://arxiv.org/abs/2602.22145v1) `cs.HC` | 提出文化幽灵概念，量化了大模型写作场景对不同英语变体文化标记的抹除问题，揭示大模型应用对文化身份的冲击，有重要社会和应用价值 |
| 8 | [DualWeaver: Synergistic Feature Weaving Surrogates for Multivariate Forecasting ...](http://arxiv.org/abs/2602.22066v1) 💻 `cs.LG (机器学习)` | 针对时间序列基础模型难以从单变量预推广到多变量预测的痛点，提出协同特征编织方案，提升多变量预测性能，是时序AI领域实用进展 |
| 9 | [Improving Parametric Knowledge Access in Reasoning Language Models](http://arxiv.org/abs/2602.22193v1) `cs.CL (计算语言学)` | 针对大语言模型调用参数化知识时推理性能不足的问题，提出改进的推理框架，提升知识依赖推理任务准确率，触及LLM推理核心问题 |
| 10 | [Confidence-Driven Multi-Scale Model Selection for Cost-Efficient Inference](http://arxiv.org/abs/2602.22090v1) `cs.CL (计算语言学)` | 针对大模型推理成本高的工业痛点，提出置信度驱动的多尺度模型选择方法，在保证性能的前提下降低推理成本，适合工业部署降本 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-26
