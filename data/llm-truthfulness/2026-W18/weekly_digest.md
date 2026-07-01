# llm-truthfulness — 2026-W18 (04/27-05/03)

本周新增 **29** 篇论文，**3** 篇附带代码。优先级：high 0 / medium 0 / low 29。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [BioGraphletQA: Knowledge-Anchored Generation of Complex QA Datas...](http://arxiv.org/abs/2604.26048v1) | 问答数据集生成 | 加入该生成数据集后，低资源下PubMedQA准确率从49.2%升至68.5%，全资源下Med... | — | — | ✅ |
| 2 | low | - | [Differentiable Faithfulness Alignment for Cross-Model Circuit Tr...](http://arxiv.org/abs/2604.24302v1) | 跨模型电路迁移 | Llama-3 1B迁移到3B时对齐电路性能媲美直接节点归因，源目标差异越大电路迁移恢复效果... | — | — | ✅ |
| 3 | low | - | [Evaluating Temporal Consistency in Multi-Turn Language Models](http://arxiv.org/abs/2604.23051v1) | 时间一致性评估 | 现有最优多轮语言模型时间范围稳定性常被违反，偏向当前假设，错误随交互长度增加，oracle上... | — | — | ✅ |
| 4 | low | - | [A Multi-Dimensional Audit of Politically Aligned Large Language ...](http://arxiv.org/abs/2604.24429v1) | 大语言模型审计 | 更大规模模型对齐政治意识形态更有效诚实，但公平性更差偏见更高；微调比角色扮演对齐更优，但推理... | — | — | — |
| 5 | low | - | [AI Safety Training Can be Clinically Harmful](http://arxiv.org/abs/2604.23445v1) | AI心理健康安全 | RLHF安全对齐会系统性干扰治疗作用机制，高严重度下三个模型治疗适当性仅0.22-0.33，... | — | — | — |
| 6 | low | - | [Bridging Reasoning and Action: Hybrid LLM-RL Framework for Effic...](http://arxiv.org/abs/2604.23345v1) | 任务型对话 | 经双重角色交叉验证可抑制LLM幻觉与跨轮不一致，所提框架长程任务性能显著优于强单模型基线 | — | — | — |
| 7 | low | - | [CacheRAG: A Semantic Caching System for Retrieval-Augmented Gene...](http://arxiv.org/abs/2604.26176v1) | 检索增强生成 | CacheRAG在CRAG数据集上相对现有最优基线，准确率提升13.2%，真实性提升17.5... | — | — | — |
| 8 | low | - | [Context-Fidelity Boosting: Enhancing Faithful Generation through...](http://arxiv.org/abs/2604.22335v1) | 生成忠实性提升 | 在多个开源大模型的摘要和问答任务中，CFB可一致提升生成忠实性指标，仅带来极小的生成开销 | — | — | — |
| 9 | low | - | [Dissociating Decodability and Causal Use in Bracket-Sequence Tra...](http://arxiv.org/abs/2604.22128v1) | 表征因果分析 | 遮蔽对真实栈顶位置的注意力会使长距离准确率骤降，消融残差流低维子空间的影响相对较小 | — | — | — |
| 10 | low | - | [Factual and Edit-Sensitive Graph-to-Sequence Generation via Grap...](http://arxiv.org/abs/2604.24104v1) | 图到序列生成 | 相对最强微调PLM基线，该方法FGT@0.5提升5.16%、ESR提升7.9%，性能优于多类... | — | — | — |
| 11 | low | - | [Faithful Autoformalization via Roundtrip Verification and Repair](http://arxiv.org/abs/2604.25031v1) | 忠实自动形式化 | 诊断引导修复将形式等价率从45%-61%提升至83%-85%，形式化等价性与语义漂移程度负相... | — | — | — |
| 12 | low | - | [From World-Gen to Quest-Line: A Dependency-Driven Prompt Pipelin...](http://arxiv.org/abs/2604.25482v1) | RPG内容生成 | 该依赖感知流水线复杂度提升时生成质量不下降，分离规划与扩展同时提升全局结构和本地叙事 | — | — | — |

## 方法族分布

- **生成忠实性提升**：1 篇
- **多源知识平衡**：1 篇
- **表征因果分析**：1 篇
- **多模态证据选择**：1 篇
- **大语言模型审计**：1 篇
- **跨模型电路迁移**：1 篇
- **私有库代码生成**：1 篇
- **图到序列生成**：1 篇
- **提示灵敏度基准**：1 篇
- **AI心理健康安全**：1 篇
- **任务型对话**：1 篇
- **大模型推理校准**：1 篇

## 代码资源

- [BioGraphletQA: Knowledge-Anchored Generation of Complex QA Datasets](https://github.com/ieeta-pt/BioGraphletQA) · 3 stars
- [Differentiable Faithfulness Alignment for Cross-Model Circuit Transfer](https://github.com/jasonshaoshun/dfa-circuits.)
- [Evaluating Temporal Consistency in Multi-Turn Language Models](https://github.com/yashkumaratri/ChronoScope)

## 常见基线方法

- **未提及具体基线**：1 篇
- **角色扮演对齐**：1 篇
- **微调对齐**：1 篇
- **直接节点归因**：1 篇
- **简单基线**：1 篇
- **现有检索增强生成RAG系统**：1 篇
- **现有基于记忆的持续学习方法**：1 篇
- **G2S扩散基线**：1 篇
- **微调自回归基线**：1 篇
- **零样本LLM迁移基线**：1 篇

## 常用数据集

- **未命名数据集1**：1 篇
- **未命名数据集2**：1 篇
- **Dyck语言**：1 篇
- **模板化自然语言数据集**：1 篇
- **M²RAG基准**：1 篇
- **摘要未提及**：1 篇
- **NdonnxEval**：1 篇
- **NumbaEval**：1 篇
- **三个文本图数据集**：1 篇
- **分子字幕数据集**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*