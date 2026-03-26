# 🧪 ArXiv AI 日报

📅 **2026-03-26 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **55,850** (¥0.0183)

## 🔥 今日必读

---

### 1. Claudini: Autoresearch Discovers State-of-the-Art Adversarial Attack Algorithms for LLMs

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.24511v1)

👤 Alexander Panfilov, Peter Romov, Igor Shilov 等


**中文标题**: Claudini：自动研究发现大语言模型的SOTA对抗攻击算法

**背景与痛点**: 当前大语言模型对抗红队依赖人类设计攻击算法，已公开的三十余种方法仍存在明显性能瓶颈；传统自动优化仅做超参数搜索，无法改进算法结构，难以挖掘离散token优化攻击的最大潜力。

**核心创新**: 基于Claude Code代码智能体实现对抗攻击算法的自动迭代研发，智能体不直接生成越狱prompt，而是从已有方法出发，自主设计、实现、评估并迭代改进攻击算法，相比传统AutoML超参数搜索能实现更大幅度的性能提升。

**技术细节**: 将Claude Opus部署在沙箱计算集群，开放GPU作业提交权限，初始提供30余种已有攻击的代码、训练集损失评分函数和固定FLOPs计算预算约束，智能体自动循环迭代：分析现有结果→提出新算法变体→编码实现→GPU评测→基于结果优化。核心改进方向包括重组不同已有攻击的核心模块、嵌套超参数调优、新增逃逸局部最优的扰动机制。

**实验结果**: 对GPT-OSS-Safeguard-20B的越狱任务，最佳Claudini攻击成功率达40%，现有方法最高不超过10%；对鲁棒性极强的Meta-SecAlign-70B提示注入任务，达到100%攻击成功率，最优基线仅56%，新算法跨模型跨任务泛化性良好。

---

### 2. Polynomial Speedup in Diffusion Models with the Multilevel Euler-Maruyama Method

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.24594v1)

👤 Arthur Jacot


**中文标题**: 基于多级欧拉-丸山方法的扩散模型多项式加速

**背景与痛点**: 扩散模型采样的计算成本由分数网络的评估次数主导，要达到更小生成误差，必须增加采样步数同时增大网络规模，传统欧拉-丸山方法的总计算量随误差呈负(伽马+1)次缩放，现有加速方法大多只能带来常数级提升，无法改进计算量的指数阶。

**核心创新**: 提出多级欧拉-丸山（ML-EM）方法，受多级蒙特卡洛思想启发，利用预训练的不同规模、精度、计算成本的分数网络，以低概率调用最高精度大网络、高概率调用低成本小网络，在伽马大于2的HTMC区域，将采样计算量复杂度从误差负(伽马+1)次降至负伽马次，实现多项式加速，可与现有加速方法结合。

**技术细节**: ML-EM在每一步采样中，将漂移项分解为不同精度网络的差分项加权和，对每一层网络用伯努利采样决定是否调用，采样概率随网络精度升高指数降低，保证输出期望等于最大网络的漂移估计，满足无偏要求。理论证明在伽马大于2时可达到目标复杂度，还支持通过低方差梯度估计+前向梯度法，用SGD学习时间相关的调用概率，进一步优化效率，只需预训练不同规模UNet，小网络训练成本可忽略。

**实验结果**: 在降采样至64×64的CelebA人脸数据集上验证，实测分数近似的伽马约为2.5，符合HTMC假设，DDPM生成达到相同MSE误差时最高可获得4倍速度提升，相同计算成本下误差可降低一个数量级，更大网络会带来更显著的加速效果。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [CUA-Suite: Massive Human-annotated Video Demonstrations for Computer-Use Agents](http://arxiv.org/abs/2603.24440v1) `cs.LG (机器学习)` | 针对计算机使用智能体数据稀缺的行业瓶颈，发布大规模人工标注的视频演示数据集CUA-Suite，将推动通用桌面智能体的技术进展。 |
| 5 | [Retrieval Improvements Do Not Guarantee Better Answers: A Study of RAG for AI Po...](http://arxiv.org/abs/2603.24580v1) `cs.CL (计算语言学)` | 纠正RAG领域「检索性能提升必然带来答案质量提升」的普遍误区，针对政策问答RAG做实证分析，对RAG工程落地有重要指导意义。 |
| 6 | [UI-Voyager: A Self-Evolving GUI Agent Learning via Failed Experience](http://arxiv.org/abs/2603.24533v1) `cs.LG (机器学习)` | 针对现有多模态大模型驱动的移动端GUI代理学习效率低的痛点，提出从失败经验学习的自进化框架，显著提升了代理的学习能力。 |
| 7 | [Composer 2 Technical Report](http://arxiv.org/abs/2603.24477v1) `cs.SE (软件工程)` | 发布面向智能体软件工程的专用模型Composer 2，具备出色的长程规划与编码能力，契合当前工业界软件开发Agent的落地需求。 |
| 8 | [MARCH: Multi-Agent Reinforced Self-Check for LLM Hallucination](http://arxiv.org/abs/2603.24579v1) 💻 `cs.CL (计算语言学)` | 针对RAG系统中LLM幻觉的核心痛点，提出多智能体强化自校验框架MARCH，有效提升LLM生成内容的可靠性，实用性很强。 |
| 9 | [AI-Supervisor: Autonomous AI Research Supervision via a Persistent Research Worl...](http://arxiv.org/abs/2603.24402v1) `cs.AI (人工智能)` | 针对现有自动AI研究系统无状态、线性流水线的缺陷，提出基于持久研究世界模型的自主监督框架，探索了AI自动研究的新方向。 |
| 10 | [Analysing the Safety Pitfalls of Steering Vectors](http://arxiv.org/abs/2603.24543v1) `cs.CR (加密与安全)` | 针对当前流行的LLM激活转向技术，系统分析了其被忽略的安全隐患，填补了该方向安全研究的空白，对LLM对齐安全有重要价值。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-26
