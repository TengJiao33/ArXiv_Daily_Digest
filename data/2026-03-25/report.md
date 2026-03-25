# 🧪 ArXiv AI 日报

📅 **2026-03-25 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **38,217** (¥0.0129)

## 🔥 今日必读

---

### 1. SpecEyes: Accelerating Agentic Multimodal LLMs via Speculative Perception and Planning

🏷️ `cs.CV (计算机视觉)` | 📄 [arXiv](http://arxiv.org/abs/2603.23483v1)

👤 Haoyu Huang, Jinfa Huang, Zhongwei Wan 等


**中文标题**: SpecEyes：基于投机感知与规划加速智能体多模态大语言模型

**背景与痛点**: 当前智能体范式的多模态大语言模型通过迭代调用视觉工具实现精细推理，但工具调用链的严格顺序依赖导致延迟随推理步数线性增长，还破坏了GPU批处理并发能力，现有加速方法仅优化单步推理，无法消除多余的工具调用循环。

**核心创新**: 首次将投机加速范式从token级提升到智能体层级，采用“快思考慢思考”异构架构：用轻量无工具小模型投机解决不需要多步推理的简单查询，仅把复杂查询交给大智能体模型，从根上消除不必要的串行工具调用开销。

**技术细节**: 整体是四阶段漏斗流水线：1、大模型先做轻量二元判断，筛选出不需要工具的查询；2、轻量无工具小模型并行生成候选答案和输出logits；3、设计认知门控：对每个token计算答案可分性分数，即topK logit中第一名与其余竞争者的标准化间距，再取所有token的最小分数做置信度判断，高于阈值直接返回；4、低置信度查询回退给大模型走完整推理。前端全可批并行，仅少部分走串行。

**实验结果**: 在V* Bench、HR-Bench、POPE三个主流基准测试，基于两个主流智能体多模态骨干，实现了1.1倍到3.35倍的端到端加速，同时精度不降反升，最高提升6.7%，平均精度提升超2个百分点。

---

### 2. SortedRL: Accelerating RL Training for LLMs through Online Length-Aware Scheduling

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.23414v1)

👤 Yiqi Zhang, Huiqiang Jiang, Xufang Luo 等


**中文标题**: SortedRL：通过在线长度感知调度加速大语言模型的强化学习训练
**背景与痛点**: 当前大语言模型强化学习训练中，rollout生成阶段占总训练时间最高70%，是核心效率瓶颈。由于生成长度服从长尾分布，全批次同步更新会导致大量GPU计算空泡，现有方案要么拉大batch引入过多离策略数据导致训练不稳定，要么灵活性不足适配性差。
**核心创新**: 提出在线长度感知调度方案SortedRL，通过按输出长度重排序rollout样本、短样本优先更新的策略，同时实现大rollout批、灵活更新批、近同策略微课程三个目标，额外引入缓存机制可控离策略训练程度，配套专用调度基础设施，同时提升硬件利用率与训练样本效率。
**技术细节**: 核心分为三个模块：1.在线长度感知调度：采用超额订阅策略向rollout引擎喂入超过队列容量的prompt，达到长度阈值后提前收割完成样本，将相近长度样本分组，自然形成从易到难的在线微课程，控制器可选择性分批调度给训练器。2.可控离策略：支持全同策略/部分离策略两种模式，部分模式缓存未完成样本的旧对数概率，恢复生成后拼接保证重要采样正确性。3.配套专用基础设施：带状态的rollout缓冲区管理中间结果，长度感知控制器维护全流程状态。
**实验结果**: 在LogicRL逻辑推理、DAPO-Math-17k数学推理数据集，基于LLaMA-3.1-8B和Qwen-2.5-32B测试，将训练空泡率从74%降到6%以内，rollout吞吐最高提升近40%，相同数据量下推理精度提升3.9%到18.4%。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [SafeSeek: Universal Attribution of Safety Circuits in Language Models](http://arxiv.org/abs/2603.23268v1) `cs.LG (机器学习)` | 针对大模型安全行为的机制解释中功能组件定位难的问题，提出通用的安全电路归因方法，助力大模型安全对齐的机制研究，实用价值高 |
| 5 | [VISion On Request: Enhanced VLLM efficiency with sparse, dynamically selected, v...](http://arxiv.org/abs/2603.23495v1) `cs.CV (计算机视觉)` | 针对现有大视觉语言模型降token提效率带来的信息瓶颈痛点，提出动态稀疏选择视觉交互的方案，兼顾效率与性能，优化VLM落地体验 |
| 6 | [MedObvious: Exposing the Medical Moravec's Paradox in VLMs via Clinical Triage](http://arxiv.org/abs/2603.23501v1) `cs.CV (计算机视觉)` | 揭示医疗领域VLM存在的莫拉维克悖论：流畅诊断文本不代表正确视觉临床理解，在临床分流中暴露安全隐患，对医疗AI落地有重要警示意义 |
| 7 | [Code Review Agent Benchmark](http://arxiv.org/abs/2603.23448v1) `cs.SE (软件工程)` | 当前AI代码Agent快速发展，但缺少专门的代码审查Agent评估基准，该工作填补了空白，规范代码审查AI的评估，助力软件工程AI落地 |
| 8 | [Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Rep...](http://arxiv.org/abs/2603.23404v1) `cs.CV (计算机视觉)` | 针对现有多模态大语言模型3D空间推理能力不足的痛点，提出文本表示引导推理的方案，有效提升空间推理性能，补全多模态核心能力短板 |
| 9 | [Off-Policy Value-Based Reinforcement Learning for Large Language Models](http://arxiv.org/abs/2603.23355v1) `cs.LG (机器学习)` | 针对大语言模型强化学习中轨迹生成成本高、数据利用率低的痛点，提出离策略价值强化学习方法，提升数据效率，降低LLM对齐训练成本 |
| 10 | [Steering LLMs for Culturally Localized Generation](http://arxiv.org/abs/2603.23301v1) `cs.CL (计算语言学)` | 针对当前大语言模型存在的文化偏差、本地化不足的痛点，提出可引导的文化本地化生成方案，助力大模型全球化部署，实用性强 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-25
