# llm-truthfulness — 2026-W20 (05/11-05/17)

本周新增 **25** 篇论文，**2** 篇附带代码。优先级：high 0 / medium 0 / low 25。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Instruction Lens Score: Your Instruction Contributes a Powerful ...](http://arxiv.org/abs/2605.12258v1) | 物体幻觉检测 | 指令token嵌入会隐式编码视觉信息，同时可有效过滤误导性视觉嵌入引入的错误信息 | — | — | ✅ |
| 2 | low | - | [Towards Order Fairness: Mitigating LLMs Order Sensitivity throug...](http://arxiv.org/abs/2605.11974v1) | 顺序偏差缓解 | DGAO在提升大语言模型顺序公平性的同时，还能提升RAG、数学推理和分类任务的性能 | — | — | ✅ |
| 3 | low | - | [Allegory of the Cave: Measurement-Grounded Vision-Language Learn...](http://arxiv.org/abs/2605.11727v1) | 视觉语言学习 | PRISM-VL-8B较基线BLEU提升0.1074，ROUGE-L提升0.1071，LLM... | — | — | — |
| 4 | low | - | [Beyond Reasoning: Reinforcement Learning Unlocks Parametric Know...](http://arxiv.org/abs/2605.07153) | 大模型知识解锁 | RL带来约27%平均相对增益，仅18%最难训练样本驱动83%增益，主要重分配已有知识概率质量 | — | — | — |
| 5 | low | - | [Bridging Legal Interpretation and Formal Logic: Faithfulness, As...](http://arxiv.org/abs/2605.14049v1) | AI法律推理 | 当前大语言模型并非仅存在事实幻觉，还会系统性做出超出原文支撑的推论，将带假设结论伪装为符合逻... | — | — | — |
| 6 | low | - | [Collider-Bench: Benchmarking AI Agents with Particle Physics Ana...](http://arxiv.org/abs/2605.13950v1) | AI智能体基准 | 在Collider-Bench评测中，所有受试通用编码智能体平均都无法可靠击败物理学家在环解... | — | — | — |
| 7 | low | - | [Derivation Prompting: A Logic-Based Method for Improving Retriev...](http://arxiv.org/abs/2605.14053v1) | 检索增强生成 | 在本次案例研究中，相较于传统RAG和长上下文窗口方法，该方法可显著减少问答任务的不可接受回答 | — | — | — |
| 8 | low | - | [Do We Really Need External Tools to Mitigate Hallucinations? SIR...](http://arxiv.org/abs/2605.14621v1) | 幻觉缓解 | 在POPE等三个数据集测试显示，SIRA稳定降幻觉保覆盖率，开销低于双次对比解码 | — | — | — |
| 9 | low | - | [GKnow: Measuring the Entanglement of Gender Bias and Factual Gen...](http://arxiv.org/abs/2605.12299v1) | 性别偏见分析 | 性别偏见与事实性别在电路和神经元层面严重纠缠，神经元消融去偏不可靠，现有评测会掩盖事实知识下... | — | — | — |
| 10 | low | - | [GeoBuildBench: A Benchmark for Interactive and Executable Geomet...](http://arxiv.org/abs/2605.13167v1) | 几何构造基准 | 在有界迭代设置下，现有SOTA多模态模型虽有一定成功率，但常出幻觉漏对象，不满足约束，自修正... | — | — | — |
| 11 | low | - | [Geometric Factual Recall in Transformers](http://arxiv.org/abs/2605.12426v1) | 事实记忆机制 | 梯度下降可得到符合预测结构的解，MLP学到通用选择机制，能零样本迁移到全新双射 | — | — | — |
| 12 | low | - | [Grounded or Guessing? LVLM Confidence Estimation via Blind-Image...](http://arxiv.org/abs/2605.10893v1) | LVLM置信度估计 | BICR参数比最强探针基线少4-18倍，跨LVLM平均校准和判别性能同时达到最优 | — | — | — |

## 方法族分布

- **大模型幻觉检测**：2 篇
- **大模型知识解锁**：1 篇
- **事实记忆机制**：1 篇
- **性别偏见分析**：1 篇
- **物体幻觉检测**：1 篇
- **知识冲突缓解**：1 篇
- **隐私行为模拟评测**：1 篇
- **顺序偏差缓解**：1 篇
- **视觉语言学习**：1 篇
- **大模型知识冲突**：1 篇
- **哲学对齐**：1 篇
- **大模型法官置信估计**：1 篇

## 代码资源

- [Instruction Lens Score: Your Instruction Contributes a Powerful Object Hallucina...](https://github.com/Fraserlairh/Instruction-Lens-Score.) · 3 stars
- [Towards Order Fairness: Mitigating LLMs Order Sensitivity through Dual Group Adv...](https://github.com/Hyalinesky/DGAO.) · 1 stars

## 常见基线方法

- **训练时基线**：1 篇
- **推理时基线**：1 篇
- **步骤级检测方法**：1 篇
- **QwQ-32B**：1 篇
- **现有物体幻觉检测方法**：1 篇
- **对比解码方法**：1 篇
- **动态解码方法**：1 篇
- **无persona条件下的隐私行为模拟**：1 篇
- **RGB Qwen3-VL-8B**：1 篇
- **少样本提示**：1 篇

## 常用数据集

- **事实类问答基准**：1 篇
- **DiFair**：1 篇
- **GKnow**：1 篇
- **StereoSet**：1 篇
- **多个基准数据集**：1 篇
- **ConflictKG**：1 篇
- **六个QA数据集**：1 篇
- **五项公开隐私领域用户研究数据**：1 篇
- **一千名用户真实隐私响应数据集**：1 篇
- **150K质量控制指令调优集**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*