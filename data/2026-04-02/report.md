# 🧪 ArXiv AI 日报

📅 **2026-04-02 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **37,415** (¥0.0129)

## 🔥 今日必读

---

### 1. Universal YOCO for Efficient Depth Scaling

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.01220v1)

👤 Yutao Sun, Li Dong, Tianzhu Ye 等


**中文标题**: 面向高效深度缩放的通用YOCO

**背景与痛点**: 当前测试时计算缩放已成为大语言模型提升推理能力的核心方向，但传统Transformer的循环推理策略计算开销极高，KV缓存会随模型深度线性膨胀占用大量内存；全网络递归方案也存在冗余开销大、内存效率低的问题，无法兼顾能力与推理效率。

**核心创新**: 提出通用YOCO（YOCO-U），结合YOCO架构“仅缓存一次”的特性与递归计算，仅在浅层的高效注意力自解码器模块做参数共享的多轮递归，不新增参数量、几乎不增加额外KV缓存开销，就可提升模型表达能力，获得比单独使用两种方法更优的能力-效率权衡。

**技术细节**: 基于YOCO原有的解码器-解码器架构，将原本静态的自解码器替换为通用自解码器，对同一组自解码器参数做T次迭代计算不新增参数量；自解码器内部使用滑动窗口这类次平方复杂度的高效自注意力，迭代完成后仅生成一份全局KV缓存供所有交叉解码器层复用。全局KV缓存大小不随迭代次数增长，仅局部窗口缓存小幅增加，因为窗口远小于序列长度，整体额外开销可忽略，保留了线性预填充、低内存占用的优势。

**实验结果**: 在通用任务、长上下文、11项数学推理基准测试验证，相同FLOPs下相比原YOCO，下游平均精度提升4.45，数学推理平均准确率提升24.4%；性能和同类递归方案相当，但KV缓存占用比RINS低近18倍，预填充吞吐量比RINS高20倍，长上下文检索能力保持优异。

---

### 2. S0 Tuning: Zero-Overhead Adaptation of Hybrid Recurrent-Attention Models

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.01168v1)

👤 Jack Young


**中文标题**: S0调优：混合循环注意力模型的零开销适配

**背景与痛点**: 当前主流开源大模型已广泛采用循环+注意力的混合架构兼顾效率与上下文能力，但现有参数高效微调（PEFT）如LoRA都是为纯Transformer设计，仅适配权重矩阵，完全浪费了混合模型自带的循环状态这个天然适配面，小数据场景下LoRA易过拟合，还需要额外的权重合并步骤。

**核心创新**: 针对带全矩阵循环状态的混合架构，提出仅优化每个循环层的初始状态矩阵，冻住所有主干模型权重，实现结构层面的零推理开销，利用循环机制放大初始偏差 Steering生成轨迹，小标注数据场景性能显著优于LoRA，任务切换无需权重合并或重加载模型。

**技术细节**: 实现流程为：给每个循环层初始化一个和原生循环状态同形状的可学习初始状态S0，全部初始化为零；训练时仅优化所有S0，主干权重完全冻结，损失仅计算目标补全的交叉熵加S0的L2正则；推理阶段S0仅在第0步注入，后续随原生状态迭代自然传播，不增加任何额外计算，仅对全矩阵循环状态有效。

**实验结果**: 在HumanEval、MATH-500、GSM8K等基准测试，Qwen3.5-4B仅用48个验证过的训练样本，S0调优比最优LoRA提升10.8个百分点，pass@1达到72.2%，纯Transformer对照实验中前缀调优反而掉点13.9个百分点，验证了方法机理的有效性。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [$\texttt{YC-Bench}$: Benchmarking AI Agents for Long-Term Planning and Consisten...](http://arxiv.org/abs/2604.01212v1) `cs.CL (计算语言学)` | 当前LLM智能体缺乏成熟的长期规划与一致执行评估基准，该论文提出YC-Bench基准，填补领域评测空白，推动复杂Agent技术发展。 |
| 5 | [CliffSearch: Structured Agentic Co-Evolution over Theory and Code for Scientific...](http://arxiv.org/abs/2604.01210v1) `cs.LG (机器学习)` | 针对现有LLM引导科学算法发现能力不足的问题，提出理论与代码的结构化智能体协同进化框架，加速AI辅助科学发现进程。 |
| 6 | [Embarrassingly Simple Self-Distillation Improves Code Generation](http://arxiv.org/abs/2604.01193v1) `cs.CL (计算语言学)` | 现有代码生成性能提升依赖验证器、教师模型或强化学习，该研究提出简单自蒸馏方案，无需额外组件即可提效，低成本实用性强。 |
| 7 | [Online Reasoning Calibration: Test-Time Training Enables Generalizable Conformal...](http://arxiv.org/abs/2604.01170v1) 💻 `cs.LG (机器学习)` | 现有测试时缩放LLM推理存在成本过高的痛点，该研究提出在线推理校准方法，基于测试时训练提升泛化性，有效降低推理成本。 |
| 8 | [OmniMem: Autoresearch-Guided Discovery of Lifelong Multimodal Agent Memory](http://arxiv.org/abs/2604.01007v1) `cs.AI (人工智能)` | 长期运行的多模态AI Agent存在记忆保留、组织与召回的核心瓶颈，该研究提出自研究引导的终身记忆方案，突破Agent长期能力瓶颈。 |
| 9 | [Adversarial Moral Stress Testing of Large Language Models](http://arxiv.org/abs/2604.01108v1) `cs.AI (人工智能)` | 现有LLM安全评估难以应对持续对抗交互下的伦理鲁棒性测试，该研究提出对抗道德压力测试框架，完善LLM安全评估体系。 |
| 10 | [Revision or Re-Solving? Decomposing Second-Pass Gains in Multi-LLM Pipelines](http://arxiv.org/abs/2604.01029v1) `cs.SE (软件工程)` | 当前工业界广泛使用多LLM修订管道，普遍认为增益来自纠错，该研究拆解第二遍增益的真实来源，为管道设计提供重要指导。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-02
