# 🧪 ArXiv AI 日报

📅 **2026-02-18 周三** | 🤖 扫描/精选: **50/13**

> 📊 Tokens: **92,254** (¥0.0300)

## 🔥 今日必读

---

### 1. GLM-5: from Vibe Coding to Agentic Engineering

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.15763v1) | 💻 [GitHub](https://github.com/zai-org/GLM-5.) ⭐1052

👤 GLM-5 Team, :, Aohan Zeng 等


**中文标题**: GLM-5：从随性编码到智能体工程

**背景与痛点**: 当前大模型正从被动知识库转向主动问题求解者，复杂端到端软件工程、长周期智能体任务面临两大核心瓶颈：一是长上下文训练推理计算成本过高，二是传统同步强化学习存在同步等待瓶颈，GPU利用率低，现有开源模型的工程能力远落后于闭源模型，也缺乏成熟的国产硬件全栈适配。

**核心创新**: GLM-5是面向智能体工程设计的下一代开源基座大模型，核心通过架构和训练框架革新解决上述痛点，采用动态稀疏注意力降低计算开销，设计全新异步强化学习架构解耦生成与训练，突破长周期任务的迭代瓶颈，同时完成全栈国产GPU适配，让开源模型性能首次接近顶级闭源模型。

**技术细节**: 架构为744B总参数MoE模型（激活40B），采用稀疏注意力DSA，在不损失长上下文性能的前提下降本1.5-2倍；改进多隐注意力MLA，提出Muon Split优化器让MLA性能追平GQA，优化多token预测参数共享提升投机解码效率。训练分三阶段，后训练采用分阶段RL加跨阶段蒸馏避免遗忘；智能体RL用全异步架构，TITO机制解决重分词偏差，双侧重要性采样控制离策略误差，全栈适配7款国产GPU，单节点性能追平国际双GPU方案。

**实验结果**: GLM-5是当前开源性能第一的大模型，相比前代GLM-4.7平均提升20%性能，是首个在Artificial Analysis智能指数v4拿到50分的开源模型，在SWE-bench Verified达到77.8%解决率，端到端软件工程能力接近闭源顶级模型Claude Opus 4.5。

---

### 2. The Geometry of Alignment Collapse: When Fine-Tuning Breaks Safety

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.15799v1)

👤 Max Springer, Chung Peng Lee, Blossom Metevier 等


**中文标题**: 对齐崩塌的几何：微调何时会破坏安全性

**背景与痛点**: 开放权重大模型微调部署已成主流，但大量实证发现，哪怕在完全无害的任务（如数学辅导、对话摘要）上微调，也会不可预测地破坏已有的安全护栏。现有理论认为高维空间中微调更新近似正交于安全敏感子空间，因此天然安全，现有主流防御（零空间投影、梯度过滤）也都基于静态一阶约束，完全无法解释和预防这种非对抗性的安全退化。

**核心创新**: 本文跳出静态几何假设，揭示安全退化是梯度下降动态下的固有几何效应：哪怕初始更新完全正交于安全敏感子空间，微调损失的二阶曲率也会系统性地把微调轨迹“掰”进敏感区域引发安全崩溃。提出对齐不稳定条件（AIC）刻画引发退化的核心几何条件，推导得到安全退化随训练时间四次方增长的定量规律，点明这是固有属性而非可修补的bug。

**技术细节**: 本文将对齐拆分为多个独立安全技能，用Fisher信息矩阵度量参数空间局部曲率，定义安全敏感子空间为Fisher矩阵前d大特征向量张成的低维空间。提出对齐不稳定条件的三个必要性质：一是低秩敏感性，对齐的高曲率集中在极小的低维子空间，微小位移就会引发显著安全损失；二是初始正交性，微调初始梯度几乎没有投影到敏感子空间，给人安全的假象；三是曲率耦合，微调损失的二阶项会产生指向敏感子空间的恒定加速度。最终证明敏感子空间投影随训练时间二次增长，安全损失为投影的二次函数，因此总安全损失随训练时间四次方增长。

**实验结果**: 在Qwen3-1.7B-Instruct、LLaMA-3.2-3B-Instruct两个模型上，对三类不同风险的微调数据集做验证，实验证实Fisher信息矩阵的低秩结构符合AIC假设，本文提出的几何重叠分数可以在训练前有效预测微调任务引发的安全退化程度，全微调下的实验结果完全符合理论预测。

---

### 3. CrispEdit: Low-Curvature Projections for Scalable Non-Destructive LLM Editing

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.15823v1)

👤 Zarif Ikram, Arad Firouzkouhi, Stephen Tu 等


**中文标题**: CrispEdit：面向可扩展非破坏性大语言模型编辑的低曲率投影

**背景与痛点**: 大语言模型编辑需要修正特定知识或行为，同时保留原有通用能力。现有方法要么采用启发式约束，易出现编辑后通用能力退化，类似奖励黑客问题；要么约束过于保守，限制编辑效果，还大多依赖预训练模型收敛的不切实际假设，在真实自回归生成场景下性能下滑严重。

**核心创新**: 从第一性原理出发，将LLM编辑建模为「最小化编辑损失+约束能力损失变化」的优化问题，核心思路是把参数更新限制在能力损失曲面的低曲率子空间，这类方向参数变动几乎不影响原有能力，同时能容纳编辑需求，还证明了现有启发式编辑方法是该框架的保守特例。

**技术细节**: 首先用Bregman散度衡量能力损失的偏离，二阶展开后恰好得到高斯-牛顿海森矩阵，不需要依赖原模型预训练收敛的假设。接着用K-FAC近似曲率，将每层的大曲率矩阵分解为输入激活协方差和输出梯度协方差两个小矩阵的克罗内克积，存储复杂度从参数平方降到输入输出维度平方之和。再利用克罗内克积的特征结构设计无矩阵投影，不需要构造大型投影矩阵，仅对两个小矩阵做特征分解即可完成梯度投影，曲率可预计算复用，还支持顺序编辑的流式更新。

**实验结果**: 在ZsRE、CounterFact、WikiBigEdit三个标准编辑数据集的真实WILD自回归评估下，CrispEdit在LLaMA3-8B等模型上，编辑成功率和泛化性能显著优于MEMIT、AlphaEdit等现有方法，平均通用能力退化不到1%，3000次批量编辑仅需4分钟，对超参数和能力数据集大小鲁棒，可扩展到万级规模编辑。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Recursive Concept Evolution for Compositional Reasoning in Large Language Models](http://arxiv.org/abs/2602.15725v1) `cs.AI (人工智能)` | 针对大语言模型组合推理能力不足的瓶颈，提出递归概念演化方法，在ARC-AGI-2、GPQA等高难度推理基准上提升显著。 |
| 5 | [Understanding vs. Generation: Navigating Optimization Dilemma in Multimodal Mode...](http://arxiv.org/abs/2602.15772v1) 💻 `cs.CV (计算机视觉)` | 针对当前多模态模型普遍存在的生成能力与理解能力此消彼长的优化困境，分析了权衡本质，指明了多模态模型后续优化方向。 |
| 6 | [Developing AI Agents with Simulated Data: Why, what, and how?](http://arxiv.org/abs/2602.15816v1) `cs.AI (人工智能)` | 针对AI智能体开发普遍面临的数据量不足、质量差的核心障碍，系统梳理了模拟数据开发AI agent的路径与价值，落地指导性强。 |
| 7 | [Perceptive Humanoid Parkour: Chaining Dynamic Human Skills via Motion Matching](http://arxiv.org/abs/2602.15827v1) `cs.RO (机器人)` | 针对当前人形机器人无法实现高动态敏捷运动的问题，提出通过运动匹配链接人类动态技能的方案，实现了感知人形跑酷，推进了具身能力。 |
| 8 | [Dex4D: Task-Agnostic Point Track Policy for Sim-to-Real Dexterous Manipulation](http://arxiv.org/abs/2602.15828v1) `cs.RO (机器人)` | 针对通用灵巧操纵难以大规模收集真实数据的痛点，提出任务无关的点追踪策略Dex4D，实现灵巧操纵的Sim-to-Real落地，通用性强。 |
| 9 | [This human study did not involve human subjects: Validating LLM simulations as b...](http://arxiv.org/abs/2602.15785v1) `cs.AI (人工智能)` | 针对当前大量社科研究用LLM替代人类被试却缺乏有效性验证的问题，系统验证了LLM模拟作为行为实验证据的合理性，对交叉研究意义重大。 |
| 10 | [A Content-Based Framework for Cybersecurity Refusal Decisions in Large Language ...](http://arxiv.org/abs/2602.15689v1) `cs.CL (计算语言学)` | 针对大语言模型应用于网络安全任务的双用途风险，提出基于内容的网络安全请求拒绝决策框架，填补了该场景的安全防护空白。 |
| 11 | [ChartEditBench: Evaluating Grounded Multi-Turn Chart Editing in Multimodal Langu...](http://arxiv.org/abs/2602.15758v1) `cs.CL (计算语言学)` | 针对多模态大模型实际探索性数据分析中，多轮图表编辑能力缺乏标准化评估的问题，构建ChartEditBench基准，推动该领域技术发展。 |
| 12 | [PERSONA: Dynamic and Compositional Inference-Time Personality Control via Activa...](http://arxiv.org/abs/2602.15669v1) `cs.AI (人工智能)` | 现有大模型人格控制依赖静态提示或微调，无法实现动态组合控制，提出基于激活向量代数的推理时动态控制方案，灵活高效实用性强。 |
| 13 | [Under-resourced studies of under-resourced languages: lemmatization and POS-tagg...](http://arxiv.org/abs/2602.15753v1) `cs.CL (计算语言学)` | 针对低资源历史语言缺少标注数据的痛点，提出用大语言模型作为标注器完成词性标注与词形还原，为低资源语言NLP提供了新思路。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-18
