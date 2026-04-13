# 🧪 ArXiv AI 日报

📅 **2026-04-13 周一** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **55,822** (¥0.0182)

## 🔥 今日必读

---

### 1. Large Language Models Generate Harmful Content Using a Distinct, Unified Mechanism

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.09544v1)

👤 Hadas Orgad, Boyi Wei, Kaden Zheng 等


**中文标题**: 大语言模型通过独特的统一机制生成有害内容

**背景与痛点**: 对齐训练后的大语言模型安全护栏仍十分脆弱，简单越狱即可轻易绕过，窄域微调也可能诱发跨域泛化的突发不对齐。现有安全方法多依赖表面行为约束，学界一直不清楚LLM内部对有害生成的编码是否存在连贯的统一结构，难以从机制层面解决安全脆弱性问题。

**核心创新**: 本文将针对性权重剪枝作为因果探针探测LLM内部结构，证实有害内容生成依赖一个紧凑统一的专用参数子集，既和良性能力分离又跨不同有害类型共享；该发现从机制层面解释了现有对齐的脆弱性和突发不对齐的成因，为更鲁棒的安全对齐开辟了新方向。

**技术细节**: 本文采用改进的SNIP剪枝准则，保留得分符号区分：负得分表示该权重会促进有害生成，将被选中剪枝；正得分表示该权重抑制有害生成，予以保留。采用双数据集校准：用有害prompt-响应对计算有害生成权重重要性，用过滤后的良性通用任务数据保护良性能力必需的权重，最终只剪符合要求的极小参数子集。

**实验结果**: 在Llama、Qwen等多个主流模型，AdvBench、HEx-PHI等标准安全测试集验证：仅剪约0.0005%的总参数，即可在几乎不损失通用能力的前提下，将越狱触发的有害生成降低90%以上；剪单类有害权重可跨域降低所有类别的有害生成，还能大幅缓解突发不对齐，同时保留模型对有害内容的检测、解释能力。

---

### 2. HiL-Bench (Human-in-Loop Benchmark): Do Agents Know When to Ask for Help?

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.09408v1)

👤 Mohamed Elfeki, Tu Trinh, Kelvin Luu 等


**中文标题**: HiL-Bench 人在回路基准：智能体知道何时该寻求帮助吗？
**背景与痛点**: 当前前沿AI智能体面对信息不全、需求模糊的实际任务时，普遍不会判断何时该向人类求助，大多靠自信猜测输出错误结果，是企业级智能体试点失败率超90%的核心原因。现有基准仅提供完整明确需求、只奖励执行正确性，无法区分瞎猜猜对和主动澄清的行为，存在根本性缺陷。
**核心创新**: 提出专门衡量智能体「选择性升级求助」能力的HiL-Bench基准，首次将真实场景中需要渐进探索才能发现的信息障碍引入评测，设计了防刷分的ASK-F1指标同时惩罚「不求助瞎猜」和「过度提问骚扰人类」两种问题，证实帮助寻求判断是可训练的跨领域通用能力。
**技术细节**: 基准最终包含300个任务，软件工程、文本转SQL各150个，每个任务人工注入3-5个经过7项严格质量标准验证的障碍，分为缺失信息、歧义需求、矛盾信息三类。所有障碍需要智能体在逐步探索执行中才能暴露，而非初始提示可见；智能体可调用askhuman工具，仅提问命中目标障碍才会获得正确答案。ASK-F1是问题精准率和障碍召回率的调和平均，天然防刷分；还设计了塑形强化学习奖励，分步奖励正确提问、惩罚无效提问，终局奖励障碍覆盖度。
**实验结果**: 对GPT、Claude、Gemini等前沿模型的测试显示，全信息下任务通过率为75%-89%，需自主判断求助时骤降到4%-24%，存在普遍的判断缺口。基于塑形ASK-F1奖励的强化学习，可让32B模型的ASK-F1最高提升28个百分点，通过率同步提升，增益可跨领域迁移。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [RecaLLM: Addressing the Lost-in-Thought Phenomenon with Explicit In-Context Retr...](http://arxiv.org/abs/2604.09494v1) `cs.CL (计算语言学)` | 解决长上下文LLM推理中「迷失在思考中」的信息丢失痛点，通过显式上下文内检索增强长上下文利用效果，实用性强适配工业需求。 |
| 5 | [VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Model...](http://arxiv.org/abs/2604.09529v1) `cs.CV (计算机视觉)` | 针对大视觉语言模型推理常伴随高置信度幻觉的问题，提出解耦式置信度校准方案，降低了大模型在高风险场景落地的核心障碍。 |
| 6 | [VISOR: Agentic Visual Retrieval-Augmented Generation via Iterative Search and Ov...](http://arxiv.org/abs/2604.09508v1) `cs.CV (计算机视觉)` | 提出智能体化视觉检索增强生成框架，结合迭代搜索与超范围推理，解决了复杂视觉文档多步查询的痛点，推动视觉RAG前沿发展。 |
| 7 | [From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large...](http://arxiv.org/abs/2604.09459v1) `cs.CL (计算语言学)` | 聚焦LLM基于强化学习训练智能体的核心痛点，分析了稀疏奖励下长轨迹信用分配的难题，为LLM Agent训练优化提供了重要方向。 |
| 8 | [Many-Tier Instruction Hierarchy in LLM Agents](http://arxiv.org/abs/2604.09443v1) `cs.CL (计算语言学)` | 指出LLM Agent多来源指令的优先级冲突痛点，提出多层级指令层级架构，解决了多源指令 Authority 差异的问题，推动Agent落地。 |
| 9 | [BERT-as-a-Judge: A Robust Alternative to Lexical Methods for Efficient Reference...](http://arxiv.org/abs/2604.09497v1) `cs.CL (计算语言学)` | 针对传统LLM生成评估方法不准确、效率低的痛点，提出鲁棒高效的BERT裁判方案，替代传统 lexical 方法，工业界实用性很强。 |
| 10 | [Efficient Unlearning through Maximizing Relearning Convergence Delay](http://arxiv.org/abs/2604.09391v1) `cs.LG (机器学习)` | 指出现有机器反学习只关注数据移除效果忽略对抗重学习的缺陷，提出通过最大化重学习收敛延迟提升反学习效果，满足数据合规刚需。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-13
