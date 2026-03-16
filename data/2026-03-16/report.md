# 🧪 ArXiv AI 日报

📅 **2026-03-16 周一** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **58,743** (¥0.0190)

## 🔥 今日必读

---

### 1. When Right Meets Wrong: Bilateral Context Conditioning with Reward-Confidence Correction for GRPO

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.13134v1) | 💻 [GitHub](https://github.com/Skylanding/BiCC) ⭐0

👤 Yu Li, Tian Lan, Zhengling Qi


**中文标题**: 当正确遇见错误：面向GRPO的带奖励置信度校正的双边上下文条件化

**背景与痛点**: GRPO是当前训练大语言推理模型的主流强化学习方法，无需单独训练评论家网络，依赖同组样本计算相对优势。但原生GRPO将每个输出视为独立样本，忽略了同组内正确、错误解答天然存在的对比结构信号，同时默认奖励和重要性权重独立，容易导致梯度方差偏大。

**核心创新**: 该研究首先将GRPO目标重写为对比形式，揭示其隐式最大化正确、错误样本策略间隔的本质。在此基础上提出两项轻量改进：交叉参考对错样本的双边上下文条件化，基于协方差校正基线的方差降低方法，无需额外采样或辅助模型，可适配所有GRPO变种。

**技术细节**: 双边上下文条件化将同组解答按奖励分为正确、错误子集，计算样本策略概率时，原查询拼接对侧子集作为输入：正确样本拼接错误解答，错误样本拼接正确解答，该上下文仅训练可用，推理零开销，所有GRPO变种仅需修改输入即可适配。奖励置信度校正通过一阶近似推导得出，最优基线需在分组平均奖励基础上加两倍的奖励与对数概率偏移的协方差，仅增加线性于分组大小的计算量，有效降低梯度方差。

**实验结果**: 在四个难度递增的数学推理基准、两个不同 base 模型上测试，该方法对所有GRPO变种均可带来0.3-1.9个百分点的准确率提升，基线能力越弱的模型收益越大，RCC可降低25%-35%的梯度方差，加快训练收敛。

---

### 2. Structured Distillation for Personalized Agent Memory: 11x Token Reduction with Retrieval Preservation

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.13017v1)

👤 Sydney Lewis


**中文标题**: 面向个性化智能体记忆的结构化蒸馏：保留检索性能的11倍Token压缩

**背景与痛点**: 个性化AI代理与用户长期对话会积累大量历史，全量携带原始对话Token成本极高，极易超出上下文窗口；现有方法多采用无结构滚动摘要压缩，会迭代丢失关键信息，且原始文本虽已存储却未建立可检索的索引层，无法支撑高效历史召回。

**核心创新**: 提出面向单用户对话历史的结构化蒸馏方案，将压缩后的对话作为可检索的路由索引，保留原始对话用于最终展示，通过结构化提取保留检索所需核心信息，实现11倍Token压缩的同时几乎不损失召回质量，验证了不同检索机制对压缩的鲁棒性差异。

**技术细节**: 将每个完整对话交换蒸馏为四组件结构化对象：LLM生成对话核心结论、具体技术细节、主题分类，正则提取对话涉及的文件路径；遵循「保留原词汇」原则，要求LLM复用用户原始术语保障检索匹配。蒸馏后单交换平均仅38个Token（原始平均371个），为原始文本和蒸馏文本分别构建独立检索索引，共测试107种不同检索配置。

**实验结果**: 在单开发者6个软件项目的4182份对话数据集上测试，最优纯蒸馏配置保留了96%的原始检索MRR；所有矢量搜索配置压缩后无统计显著质量退化，所有BM25关键词搜索均显著退化；融合原始关键词搜索+蒸馏矢量搜索的跨层方案MRR略超纯原始文本基线。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Neuron-Aware Data Selection In Instruction Tuning For Large Language Models](http://arxiv.org/abs/2603.13201v1) `cs.CL (计算语言学)` | 针对指令调优中过量数据会降低LLM性能的痛点，提出神经元感知的数据选择方法，有效提升指令调优的效率与最终模型效果。 |
| 5 | [PISmith: Reinforcement Learning-based Red Teaming for Prompt Injection Defenses](http://arxiv.org/abs/2603.13026v1) 💻 `cs.LG (机器学习)` | 提示注入是LLM应用尤其是自主Agent的核心安全风险，提出基于强化学习的红队测试方法，有效提升现有防御方案的鲁棒性。 |
| 6 | [Semantic Invariance in Agentic AI](http://arxiv.org/abs/2603.13173v1) `cs.AI (人工智能)` | 针对当前LLM Agent部署中普遍存在的语义不一致问题，提出语义不变性研究方向，为提升Agent落地可靠性提供了新思路。 |
| 7 | [Beyond Final Answers: CRYSTAL Benchmark for Transparent Multimodal Reasoning Eva...](http://arxiv.org/abs/2603.13099v1) `cs.AI (人工智能)` | 填补多模态推理缺少透明可追溯评估基准的空白，推出CRYSTAL诊断基准，包含6372个测试实例，推动多模态推理研究发展。 |
| 8 | [Steve-Evolving: Open-World Embodied Self-Evolution via Fine-Grained Diagnosis an...](http://arxiv.org/abs/2603.13131v1) `cs.AI (人工智能)` | 针对开放世界具身Agent长周期任务的经验进化瓶颈，提出细粒度诊断+双轨知识蒸馏的自进化框架，推进具身Agent前沿研究。 |
| 9 | [Fractals made Practical: Denoising Diffusion as Partitioned Iterated Function Sy...](http://arxiv.org/abs/2603.13069v1) `cs.LG (机器学习)` | 从分形理论角度揭示确定性DDIM扩散反向过程本质是分块迭代函数系统，为扩散模型提供了全新的理论解释，有重要理论价值。 |
| 10 | [daVinci-Env: Open SWE Environment Synthesis at Scale](http://arxiv.org/abs/2603.13023v1) `cs.SE (软件工程)` | 解决软件工程Agent训练缺少大规模可执行验证环境的痛点，推出开源的大规模SWE环境合成框架，赋能SWE Agent领域研究。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-16
