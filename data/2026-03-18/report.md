# 🧪 ArXiv AI 日报

📅 **2026-03-18 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **64,676** (¥0.0209)

## 🔥 今日必读

---

### 1. Efficient Reasoning on the Edge

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.16867v1)

👤 Yelysei Bondarenko, Thomas Hehn, Rob Hesselink 等


**中文标题**: 边缘端大语言模型高效推理

**背景与痛点**: 带思维链的大语言模型推理性能出色，但冗长的推理轨迹、大KV缓存需求让它难以部署在资源受限的边缘设备；现有方案大多直接将大模型的冗长推理轨迹蒸馏到小模型，冗余度高、推理延迟大、内存占用超标，无法满足移动场景的严格资源约束。

**核心创新**: 提出一套端到端的边缘推理优化框架，通过模块化LoRA适配分离通用对话和推理能力，结合动态按需激活、长度压缩、并行提准和硬件感知量化，在极小额外参数开销下实现接近全参数蒸馏大模型的推理性能，兼顾日常交互效率和复杂任务推理能力。

**技术细节**: 以冻结的通用指令大模型为骨干，用LoRA做推理适配：先通过监督微调学习推理能力，再用GRPO强化学习，设计乘法软屏障预算惩罚避免奖励作弊，压缩冗余推理；添加轻量分类器Switcher，动态判断是否激活推理LoRA，通过masked LoRA训练实现两种模式KV缓存复用，无需重编码prompt；推理时利用边缘解码的内存瓶颈特性，并行生成多候选，加轻量验证头做加权多数投票提准；最后对base做4bit量化，训练LoRA时适配量化分布，LoRA用8bit存储。

**实验结果**: 在Qwen2.5 3B/7B上测试，覆盖数学、科学、编码多类基准，7B模型仅更新4.24%参数，推理性能接近全参数蒸馏的DeepSeek-R1 7B；平均推理长度压缩2.4倍后精度损失不到2%，4bit量化后整体精度仅降约2%，可稳定运行在移动端。

---

### 2. Is Conformal Factuality for RAG-based LLMs Robust? Novel Metrics and Systematic Insights

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.16817v1)

👤 Yi Chen, Daiwei Chen, Sukrut Madhav Chikodikar 等


**中文标题**: 基于RAG的大语言模型保形事实性是否具备鲁棒性？新型指标与系统性洞察
**背景与痛点**: RAG可缓解大语言模型幻觉，但无法提供输出事实性的统计保证；保形事实过滤通过后处理滤除错误声明可提供形式化无分布保证，但现有评估仅统计正确率，会高估空输出等无意义结果的性能，且缺乏对该框架实际部署鲁棒性的系统分析。
**核心创新**: 提出四类新型评估指标，联合度量保形过滤后输出的事实正确性与信息有用性，弥补了传统指标的设计缺陷；首次系统性分析了RAG下保形事实框架在分布偏移、干扰输入下的鲁棒性，厘清了验证器规模、性能与效率的权衡关系。
**技术细节**: 设计四类新指标：非空率、非空经验事实性从声明层级惩罚无用空输出；充分正确性、条件充分正确性从任务层级度量输出是否保留足够信息回答查询。在三个跨任务基准、多个模型家族上开展测试，对比轻量蕴含验证器与大模型置信验证器，通过校准偏移、干扰注入测试鲁棒性，统计FLOPs分析效率。
**实验结果**: 在FActScore、MATH、自然问题三个基准测试发现：保形过滤在高目标事实性下会因过度过滤产出大量无用输出，分布偏移与干扰输入会击穿保形框架的事实性保证，轻量蕴含验证器性能匹配甚至超过大模型打分器，计算量降低100倍以上。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Chronos: Temporal-Aware Conversational Agents with Structured Event Retrieval fo...](http://arxiv.org/abs/2603.16862v1) `cs.CL (计算语言学)` | 解决长周期对话大模型长期记忆管理效率低的痛点，提出时间感知的结构化事件检索方案，提升对话Agent长周期交互能力，落地价值高。 |
| 5 | [Anticipatory Planning for Multimodal AI Agents](http://arxiv.org/abs/2603.16777v1) `cs.AI (人工智能)` | 当前多模态AIAgent多为反应式，仅优化当前动作缺乏对未来的推理，该工作研究预期规划，推动长周期自主Agent能力提升，属于方向前沿。 |
| 6 | [Nonstandard Errors in AI Agents](http://arxiv.org/abs/2603.16744v1) `cs.AI (人工智能)` | 针对当前AI编码代理的可复现性问题，实证发现相同研究任务下SOTA代理结果差异显著，揭示了AIAgent研究普遍存在的非标准误差问题，意义重大。 |
| 7 | [Mediocrity is the key for LLM as a Judge Anchor Selection](http://arxiv.org/abs/2603.16848v1) `cs.CL (计算语言学)` | LLM-as-judge是当前开放生成评估的主流范式，该工作解决锚点选择的核心痛点，发现中等质量锚点效果更优，降低评估成本提升可扩展性。 |
| 8 | [DexGrasp-Zero: A Morphology-Aligned Policy for Zero-Shot Cross-Embodiment Dexter...](http://arxiv.org/abs/2603.16806v1) `cs.RO (机器人)` | 解决跨形态灵巧抓取需要重复训练的痛点，提出形态对齐策略，实现零样本跨实体灵巧抓取，对服务机器人领域落地有很高实用价值。 |
| 9 | [Understanding Quantization of Optimizer States in LLM Pre-training: Dynamics of ...](http://arxiv.org/abs/2603.16731v1) `cs.LG (机器学习)` | 针对大模型预训练优化器状态量化的动力学机制不清晰的问题，分析了状态陈旧性的动态规律，给出有效的重置方案，支撑高效大模型预训练。 |
| 10 | [Surg$Σ$: A Spectrum of Large-Scale Multimodal Data and Foundation Models for Sur...](http://arxiv.org/abs/2603.16822v1) `cs.AI (人工智能)` | 解决现有手术AI任务特定、泛化性差的痛点，推出大规模多模态手术数据集和通用基础模型体系，推动手术智能领域通用化落地发展。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-18
