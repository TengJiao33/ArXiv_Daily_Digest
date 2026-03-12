# 🧪 ArXiv AI 日报

📅 **2026-03-12 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **54,016** (¥0.0179)

## 🔥 今日必读

---

### 1. Leech Lattice Vector Quantization for Efficient LLM Compression

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.11021v1)

👤 Tycho F. A. van der Ouderaa, Mart van Baalen, Paul Whatmough 等


**中文标题**: 用于大语言模型高效压缩的利奇晶格矢量量化

**背景与痛点**: 大语言模型压缩中，标量量化受信息论瓶颈限制，低比特压缩精度损失严重；传统无结构矢量量化需要存储显式码本，存储和搜索成本随维度指数增长；现有低维晶格量化方法（如基于8维E8晶格的Quip#）仍未充分发挥高维晶格的理论优势。

**核心创新**: 本文将数学上具备最优球填充性质的24维利奇晶格，改造为适合大语言模型量化的实用无码本矢量量化方案LLVQ；充分利用利奇晶格的高维结构优势，突破低维晶格的率失真上限，无需显式存储码本即可实现更优的压缩精度权衡。

**技术细节**: 利奇晶格基于扩展格雷码构造，天然划分为多个不同半径的同心壳。本文扩展了原有利奇晶格最近邻搜索算法，支持多壳联合搜索，同时适配欧氏距离（球形整形）和角度距离（形状增益量化）两种场景；设计了壳-类-局部自由度的分层双射索引，无需显式码本即可实现索引与向量的互转；反量化通过整数除法和模运算逐层拆分索引重构向量，所有块独立计算可完全并行，适配GPU执行；采用形状增益架构分离方向与幅度量化，进一步提升率失真性能。

**实验结果**: 在Llama 2/3、Ministral、Qwen等多个主流大模型上测试，2比特每权重后训练量化场景下，困惑度和下游任务精度全面优于Quip#、QTIP、AQLM等现有SOTA方法；在高斯源测试中，2比特每维度下达到香农极限92%的信息保留率，比E8基方法提升6个百分点。

---

### 2. Beyond the Illusion of Consensus: From Surface Heuristics to Knowledge-Grounded Evaluation in LLM-as-a-Judge

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2603.11027v1)

👤 Mingyang Song, Mao Zheng, Chenning Xu


**中文标题**: 超越共识幻觉：大模型裁判范式——从表面启发式到知识锚定评价
**背景与痛点**: 当前大模型当裁判已经成为LLM排序、RLAIF奖励建模的核心范式，行业普遍默认不同前沿裁判的高一致性就代表评价可靠可信。现有方法大多使用通用静态评分规则，从未系统验证一致性是否真的反映对输出实质质量的共识。
**核心创新**: 本文首次形式化定义了「评价幻觉」现象：大模型裁判会写出看似专业的评价，实际评分锚定格式、流畅度、语气等共享表面启发式，而非输出实质质量。提出了元认知增强规则生成框架MERG，可诊断共识真实性，也能生成更贴合领域实质的评价。
**技术细节**: MERG分四步强制大模型从快速启发式思考转向慢深度思考：1.知识激活：提前梳理任务相关领域规则、专业标准和常见陷阱；2.元认知反思：预先识别自身可能的启发式偏见并制定缓解策略；3.动态生成任务专属定制评分规则，不用通用维度；4.校准评分，要求每个维度评分绑定文本证据后复核偏见。本文构建了含105600个实例的大规模测试集，覆盖32个不同能力层级LLM、3个不同厂商前沿裁判。
**实验结果**: 实验证实：模型级接近完美的一致性掩盖了样本级的脆弱一致，仅共享评分框架结构就贡献了62%的总一致性，高质量输出反而评价一致性最低；基于MERG训练的奖励模型，抗过优化能力是基线方法的3倍。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [LookaheadKV: Fast and Accurate KV Cache Eviction by Glimpsing into the Future wi...](http://arxiv.org/abs/2603.10899v1) `cs.LG (机器学习)` | 针对LLM推理KV缓存占用大、现有驱逐策略精度差的痛点，提出无需预生成的未来感知缓存驱逐方法，兼顾速度与输出精度。 |
| 5 | [Ranking Reasoning LLMs under Test-Time Scaling](http://arxiv.org/abs/2603.10960v1) 💻 `cs.LG (机器学习)` | 针对测试时缩放范式下推理大模型的排序问题，形式化定义了该场景的评测任务，填补了当前大模型推理评测领域的研究空白。 |
| 6 | [Safe RLHF Beyond Expectation: Stochastic Dominance for Universal Spectral Risk C...](http://arxiv.org/abs/2603.10938v1) `cs.LG (机器学习)` | 针对现有Safe RLHF仅约束期望成本、无法控制长尾安全风险的缺陷，提出基于随机占优的风险控制框架，提升大模型安全对齐可靠性。 |
| 7 | [A Systematic Study of Pseudo-Relevance Feedback with LLMs](http://arxiv.org/abs/2603.11008v1) `cs.IR` | 针对RAG和信息检索核心的伪相关反馈技术，系统梳理了LLM时代PRF的核心设计维度，对工业界RAG性能优化有很高参考价值。 |
| 8 | [GroundCount: Grounding Vision-Language Models with Object Detection for Mitigati...](http://arxiv.org/abs/2603.10978v1) `cs.CV (计算机视觉)` | 针对视觉语言模型普遍存在的计数幻觉痛点，提出结合目标检测 grounding的优化方案，有效提升计数准确率，实用性强。 |
| 9 | [Dynamics-Predictive Sampling for Active RL Finetuning of Large Reasoning Models](http://arxiv.org/abs/2603.10887v1) `cs.LG (机器学习)` | 针对大推理模型RL微调中样本选择效率低的问题，提出动态预测采样的主动RL微调方法，提升样本利用率与微调效果。 |
| 10 | [RCTs & Human Uplift Studies: Methodological Challenges and Practical Solutions f...](http://arxiv.org/abs/2603.11001v1) `cs.CY` | 针对前沿AI效果评估中RCT方法的诸多实践挑战，总结了系统性解决方案，对AI真实效果的科学评估有重要指导意义。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-12
