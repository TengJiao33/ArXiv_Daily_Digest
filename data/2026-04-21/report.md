# 🧪 ArXiv AI 日报

📅 **2026-04-21 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **38,662** (¥0.0130)

## 🔥 今日必读

---

### 1. WorldDB: A Vector Graph-of-Worlds Memory Engine with Ontology-Aware Write-Time Reconciliation

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.18478v1)

👤 Harish Santhanalakshmi Ganesan


**中文标题**: WorldDB：支持本体感知写时调和的世界向量图记忆引擎

**背景与痛点**: 长期运行的智能体系统以持久化一致记忆为核心瓶颈，传统RAG的扁平向量存储存在语义碎片化、无法处理知识更新、实体身份漂移问题；现有双时态知识图仍然是扁平结构，边类型仅带标签无内置执行语义，无法原生处理知识冲突与递归组合。

**核心创新**: 提出面向智能体的新型记忆引擎，三个核心非传统设计突破现有方案限制：节点是可任意递归嵌套的世界容器、所有节点内容寻址不可变天然生成默克尔审计轨迹、边类型自带写时处理逻辑，从结构层面保证长期记忆的一致性与可审计性。

**技术细节**: 每个节点是可递归嵌套的世界容器，自带内部子图、本体范围和组合嵌入，节点ID基于内容生成blake3哈希，编辑叶子会递归更新所有祖先哈希，天然获得完整修改审计轨迹；所有写操作必须经过边对应类型的写时句柄，自动完成关闭过时知识有效性、标记冲突、生成合并提案；检索采用BM25+HNSW+实体图遍历三路排名融合，后台自动生成摘要节点，总结类查询速度提升6.5倍。

**实验结果**: 在标准长期记忆基准LongMemEval-s测试，整体准确率达到96.40%，相比此前SOTA Hydra DB提升5.61个百分点；消融实验证明引擎的图结构设计独立贡献10.66个百分点的任务平均准确率提升，百万节点写入性能达5401次/秒，P95读延迟稳定在13ms以内。

---

### 2. Latent Phase-Shift Rollback: Inference-Time Error Correction via Residual Stream Monitoring and KV-Cache Steering

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.18567v1)

👤 Manan Gupta, Dhruv Kumar


**中文标题**: 潜相移回滚：基于残差流监控和KV缓存引导的推理时错误纠正

**背景与痛点**: 大语言模型多步推理过程中，中间步骤产生的错误会不断传播放大，最终导致整体推理失败。现有解决方案要么依赖训练调优，成本极高；要么推理时方案要么效果退化，要么需要多轮前向传播，计算开销大，且未利用模型内部隐状态的错误信号。

**核心创新**: 提出无需微调、无需梯度计算的推理时在线纠错方法LPSR，通过监控模型中间层残差流的方向变化检测推理错误，配合KV缓存回滚和预计算引导向量完成纠错；首次发现Transformer深度上的「检测-纠正解离」现象：错误检测精度最高的层，并非最终任务精度最优的纠错层。

**技术细节**: 推理时在目标中间层注册前向钩子抓取每步残差状态，计算当前与上一步归一化残差的余弦相似度，结合输出token分布熵做双门限检测，符合条件则判定为错误相移。预计算环节从校准集提取错误与正确轨迹的残差差值，经k-means聚类得到归一化纠错引导向量基。检测到错误后，回滚KV缓存到上一步，选择匹配度最高的引导向量注入后重新解码。

**实验结果**: 在MATH-500、GSM8K等数学推理基准测试，基于Llama-3-8B模型，LPSR在MATH-500上准确率达44.0%，相比标准自回归解码提升15.2个百分点，比Best-of-16高7.8个百分点，token成本低5.4倍，性能超过标准Llama-3-70B，参数减少8.75倍。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Sessa: Selective State Space Attention](http://arxiv.org/abs/2604.18580v1) `cs.LG (机器学习)` | 针对Transformer自注意力存在冗余、效率不足的问题，结合选择性状态空间和注意力的优势，提出新型序列建模架构Sessa，是基础模型架构的有价值探索 |
| 5 | [MASS-RAG: Multi-Agent Synthesis Retrieval-Augmented Generation](http://arxiv.org/abs/2604.18509v1) `cs.CL (计算语言学)` | 针对现有RAG在检索上下文存在噪声、不完整、异质性时效果不佳的痛点，提出多智能体合成检索增强框架MASS-RAG，提升复杂场景RAG的可用性 |
| 6 | [Train Separately, Merge Together: Modular Post-Training with Mixture-of-Experts](http://arxiv.org/abs/2604.18473v1) `cs.LG (机器学习)` | 解决预训练LLM扩展新领域能力时，单一体训练范式成本高、扩展性差的痛点，提出分开训练合并到MoE的模块化后训练方案，大幅降低扩展成本 |
| 7 | [MathNet: a Global Multimodal Benchmark for Mathematical Reasoning and Retrieval](http://arxiv.org/abs/2604.18584v1) `cs.AI (人工智能)` | 现有数学推理基准存在规模小、多语言覆盖不足、任务单一的缺陷，提出全球多模态数学推理与检索基准MathNet，填补了领域基准缺口 |
| 8 | [GSQ: Highly-Accurate Low-Precision Scalar Quantization for LLMs via Gumbel-Softm...](http://arxiv.org/abs/2604.18556v1) `cs.CL (计算语言学)` | 针对低精度LLM量化精度损失大的问题，提出基于Gumbel-Softmax采样的GSQ量化方法，在2-3bit低精度下保持高准确率，利于端侧LLM部署 |
| 9 | [LLM Safety From Within: Detecting Harmful Content with Internal Representations](http://arxiv.org/abs/2604.18519v1) `cs.AI (人工智能)` | 现有LLM有害内容检测仅依赖输出层表示，忽略模型内部的安全相关信息，提出利用内部表示检测有害内容，提升检测性能，思路新颖 |
| 10 | [Using large language models for embodied planning introduces systematic safety r...](http://arxiv.org/abs/2604.18463v1) `cs.AI (人工智能)` | 指出LLM作为机器人具身规划器存在系统性安全风险，构建了专门的评估基准DESPITE，填补了具身Agent安全研究的评估空白，很有启发 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-21
