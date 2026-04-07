# 🧪 ArXiv AI 日报

📅 **2026-04-07 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **45,206** (¥0.0151)

## 🔥 今日必读

---

### 1. TriAttention: Efficient Long Reasoning with Trigonometric KV Compression

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.04921v1)

👤 Weian Mao, Xi Lin, Wei Huang 等


**中文标题**: TriAttention：基于三角KV压缩的高效长推理

**背景与痛点**: 针对大语言模型长链推理过程中，KV缓存持续增长带来的严重内存瓶颈问题。现有KV压缩方法均基于RoPE旋转后的空间估计token重要性，查询方向随位置旋转，仅最近少数查询可用，容易漏检长期休眠后才用到的关键token，导致推理精度大幅下降。

**核心创新**: 本文发现在应用RoPE之前的空间中，绝大多数注意力头的Q/K向量会稳定聚集在固定非零中心，该特性是模型固有属性，跨内容跨任务稳定。基于此推导出注意力对不同距离键的偏好可通过三角级数预测，以此设计全新的KV重要性评分，避开了现有后RoPE方法的固有缺陷。

**技术细节**: 首先离线校准提取每个注意力头各频率带的Q/K统计中心，用平均结果长度量化Q/K的聚集程度。推理时对每个键计算两个得分：三角级数得分预测不同未来查询距离下的预期注意力；范数得分通过聚集度自适应加权，为聚集度低的头补充信息。每生成128个token触发一次剪枝，保留得分最高的键，针对分组查询注意力做了归一化聚合处理。

**实验结果**: 在AIME数学推理、MATH500、LongBench等多个基准测试，匹配全注意力推理精度的前提下，在AIME25上实现2.5倍吞吐量提升、10.7倍KV内存压缩，同效率下精度领先现有SOTA方法R-KV近一倍，可支持32B级模型单24GB消费级GPU完成长多轮任务。

---

### 2. Early Stopping for Large Reasoning Models via Confidence Dynamics

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.04930v1)

👤 Parsa Hosseini, Sumit Nawathe, Mahdi Salmani 等


**中文标题**: 基于置信度动态的大推理模型早停方法
**背景与痛点**: 大推理模型依赖长思维链解决复杂推理问题，不仅带来高昂的计算成本，还容易因过度思考降低输出性能。现有早停方法要么需要额外训练改造模型，要么仅依赖单步置信度阈值做判断，无法高效终止长期无进展的错误推理轨迹。
**核心创新**: 本文观察到正确与错误推理轨迹的置信度演化存在显著差异：正确轨迹会较早达到稳定高置信度，错误轨迹置信度持续波动不稳定，且推理早期的置信度对轨迹正误的区分度更高。据此提出无需训练的CoDE-Stop早停方法。
**技术细节**: 推理过程中每个自然推理步骤分界点，触发模型生成中间答案，以答案token的平均概率作为该步置信度。设置两个停止条件：一是阶梯上升的置信度阈值，当前置信度达标即停止；二是累计退化得分，每一步检测到置信度无提升则计入得分，对早期步骤赋予更高权重，退化得分超标也停止。
**实验结果**: 在AIME、MATH500、GSM8K、GPQA-Diamond四个主流推理科学基准，测试四款不同规模的开源推理模型，CoDE-Stop相比标准全长度推理可减少25%-50%的总token用量，精度仅微降，比现有早停方法拥有更优的精度-算力 tradeoff，还可兼容各类提示优化方法进一步提效。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [MemMachine: A Ground-Truth-Preserving Memory System for Personalized AI Agents](http://arxiv.org/abs/2604.04853v1) `cs.AI (人工智能)` | 解决现有LLM智能体持久化记忆难以维持个性化、事实连贯性与长程推理的问题，提出保留真值的记忆系统，显著提升智能体长期使用能力。 |
| 5 | [Vero: An Open RL Recipe for General Visual Reasoning](http://arxiv.org/abs/2604.04917v1) `cs.CV (计算机视觉)` | 提出开源的通用视觉推理强化训练方案Vero，可支持跨图表、科学任务、空间理解等多类任务，填补了开源通用视觉推理方案的空白。 |
| 6 | [MinerU2.5-Pro: Pushing the Limits of Data-Centric Document Parsing at Scale](http://arxiv.org/abs/2604.04771v1) `cs.CV (计算机视觉)` | 针对当前文档解析领域对训练数据系统性工程关注不足的问题，推出MinerU2.5-Pro，推升了规模化文档解析的性能上限，是RAG落地的核心基础技术。 |
| 7 | [QED-Nano: Teaching a Tiny Model to Prove Hard Theorems](http://arxiv.org/abs/2604.04898v1) `cs.AI (人工智能)` | 面向复杂定理证明任务，实现了能证明难题的超小型模型QED-Nano，打破了复杂定理证明必须依赖大模型的共识，探索了轻量化推理的新方向。 |
| 8 | [Incompleteness of AI Safety Verification via Kolmogorov Complexity](http://arxiv.org/abs/2604.04876v1) `cs.AI (人工智能)` | 从柯尔莫哥洛夫复杂度的理论角度，证明了AI安全验证存在固有不完备性，揭示了安全验证领域的根本理论边界，对AI安全基础研究启发重大。 |
| 9 | [Optimizing LLM Prompt Engineering with DSPy Based Declarative Learning](http://arxiv.org/abs/2604.04869v1) `cs.LG (机器学习)` | 解决当前LLM提示工程高度依赖人工经验设计的痛点，提出基于DSPy的声明式学习优化方案，降低提示工程门槛，有效提升任务性能。 |
| 10 | [Undetectable Conversations Between AI Agents via Pseudorandom Noise-Resilient Ke...](http://arxiv.org/abs/2604.04757v1) `cs.CR (加密与安全)` | 揭示了多智能体场景下的新型安全风险，证明不同AI代理可通过伪随机密钥交换实现不可检测的秘密通信，对AI代理安全防护研究有重要价值。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-07
