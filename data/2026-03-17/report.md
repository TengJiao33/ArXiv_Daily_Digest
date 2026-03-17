# 🧪 ArXiv AI 日报

📅 **2026-03-17 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **46,134** (¥0.0154)

## 🔥 今日必读

---

### 1. Mixture-of-Depths Attention

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.15619v1) | 💻 [GitHub](https://github.com/hustvl/MoDA) ⭐8

👤 Lianghui Zhu, Yuxin Fang, Bencheng Liao 等


**中文标题**: 深度混合注意力（MoDA）

**背景与痛点**: 加深模型深度是大语言模型性能提升的核心驱动因素，但深度提升后会出现信号退化问题：浅层生成的高信息量特征会被多次残差更新逐步稀释，深层难以有效恢复利用，制约了大模型的深度缩放效果。

**核心创新**: 核心提出每个注意力头不仅处理当前层的键值对，还可接入前面所有层的跨层深度键值对，通过跨层特征复用保留浅层有效信息，同时设计了硬件友好的实现方案解决非连续访存瓶颈，额外计算开销极低。

**技术细节**: 具体实现中，每个注意力头会将当前层生成的键值序列，与前面所有层缓存的深度键值序列拼接后做注意力计算；针对跨层键值分散存储导致的访存低效问题，设计了硬件友好的重排算法，将分散的跨层键值连续存储适配FlashAttention的IO优化，在64k序列长度下仍能达到FlashAttention2 97.3%的运行效率，额外FLOPs开销仅3.7%。

**实验结果**: 在1.5B参数模型上测试，10个验证基准上平均困惑度降低0.2，10个下游任务平均性能提升2.11%，同时验证出MoDA搭配后归一化的效果优于预归一化。

---

### 2. Mamba-3: Improved Sequence Modeling using State Space Principles

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.15569v1)

👤 Aakash Lahoti, Kevin Y. Li, Berlin Chen 等


**中文标题**: Mamba-3：基于状态空间原理改进的序列建模

**背景与痛点**: 当前大语言模型推理效率需求持续提升，Transformer自注意力计算复杂度为平方级，KV缓存内存占用随序列长度线性增长，现有次线性序列模型如Mamba-2、Gated DeltaNet普遍存在性能折损，状态跟踪能力不足，且理论高效的推理实际硬件算术强度低、利用率差。

**核心创新**: 遵循推理优先的设计原则，从状态空间模型视角出发提出三项核心改进，在不增加推理延迟的前提下提升模型表达能力，解决现有线性模型的状态跟踪缺陷，同时提升硬件利用率，大幅推进了性能-效率的帕累托前沿。

**技术细节**: 首先提出指数调整离散化框架，从理论上证明了Mamba-1/2原启发式离散的合理性，新的指数梯形离散化是原方法的泛化，自带隐式状态输入卷积，配合B、C通道偏置可替代原有架构必须的外部短卷积；其次引入复值状态空间，通过分块旋转矩阵等价转换为实值计算，等价于对输入输出投影做数据依赖旋转位置编码，解决了实值SSM无法表示旋转动力学的缺陷；最后改为多输入多输出结构，不增加状态大小的前提下提升推理算术强度，适配GPU张量核心。

**实验结果**: 在FineWeb-Edu数据集预训练，1.5B参数量下，Mamba-3 SISO比次优基线Gated DeltaNet平均下游准确率高0.6个百分点，MIMO版本再提升1.2个百分点；同等困惑度下状态大小仅为Mamba-2的一半，可完美解决原有线性模型无法完成的奇偶校验等状态跟踪任务。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [HorizonMath: Measuring AI Progress Toward Mathematical Discovery with Automatic ...](http://arxiv.org/abs/2603.15617v1) `cs.LG (机器学习)` | 提出带自动验证的基准，评测大模型推进数学发现的能力，探索AI解决开放性未决数学问题的潜力，是LLM科学推理方向的重要工作。 |
| 5 | [OpenSeeker: Democratizing Frontier Search Agents by Fully Open-Sourcing Training...](http://arxiv.org/abs/2603.15594v1) `cs.AI (人工智能)` | 全开源前沿搜索Agent的完整训练数据，打破工业界对高性能搜索Agent的技术垄断，降低了开源社区研发门槛，行业影响力大。 |
| 6 | [SmartSearch: How Ranking Beats Structure for Conversational Memory Retrieval](http://arxiv.org/abs/2603.15599v1) `cs.LG (机器学习)` | 点出当前对话记忆系统过度工程化的痛点，证明无需预结构化和学习式检索，简单排序就能取得更优效果，轻量化实用性强。 |
| 7 | [Beyond the Covariance Trap: Unlocking Generalization in Same-Subject Knowledge E...](http://arxiv.org/abs/2603.15518v1) `cs.CL (计算语言学)` | 解决LLM知识编辑领域同主体知识更新泛化失败的核心痛点，破解了同主题编辑的协方差陷阱，提升知识编辑的实用可靠性。 |
| 8 | [Agentic workflow enables the recovery of critical materials from complex feedsto...](http://arxiv.org/abs/2603.15491v1) `cond-mat.mtrl-sci` | 将多Agent工作流结合自动化实验仪器，实现从复杂原料中回收关键战略材料，是AI Agent落地实体工业领域的创新实践。 |
| 9 | [Agent Lifecycle Toolkit (ALTK): Reusable Middleware Components for Robust AI Age...](http://arxiv.org/abs/2603.15473v1) `cs.AI (人工智能)` | 针对AI Agent从Demo落地企业生产的痛点，提供可复用的健壮中间件组件，解决Agent部署的可靠性工程问题，适配工业落地需求。 |
| 10 | [Invisible failures in human-AI interactions](http://arxiv.org/abs/2603.15423v1) 💻 `cs.CL (计算语言学)` | 基于大规模真实人类-AI交互数据，发现78%的AI故障是隐形不可见的，点出领域内被忽略的核心问题，对对齐和产品设计启发很大。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-17
