# llm-truthfulness — 2026-W19 (05/04-05/10)

本周新增 **39** 篇论文，**2** 篇附带代码。优先级：high 0 / medium 0 / low 39。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [SERE: Structural Example Retrieval for Enhancing LLMs in Event C...](http://arxiv.org/abs/2605.03701v1) | 事件因果识别 | 整合概念路径度量、句法度量、因果模式过滤的结构检索，可有效缓解因果幻觉，提升事件因果识别准确... | — | — | ✅ |
| 2 | low | - | [TriBench-Ko: Evaluating LLM Risks in Judicial Workflows](http://arxiv.org/abs/2605.03792v1) | 司法模型风险评估 | 多款当代大语言模型频繁存在显著风险，尤其在先例检索任务中表现差，无法捕捉关键法律信息 | — | — | ✅ |
| 3 | low | - | [A Few Good Clauses: Comparing LLMs vs Domain-Trained Small Langu...](http://arxiv.org/abs/2605.05532v1) | 结构化合同提取 | Olava Extract宏F1为0.812、微F1为0.842，推理成本较前沿模型降低78... | — | — | — |
| 4 | low | - | [A Multi-View Media Profiling Suite: Resources, Evaluation, and A...](http://arxiv.org/abs/2605.01336v1) | 多视图媒体画像 | 所提方法在ACL-2020数据集上取得当前最优结果，在新建MBFC-2025数据集上建立了强... | — | — | — |
| 5 | low | - | [Automated Clinical Report Generation for Remote Cognitive Remedi...](http://arxiv.org/abs/2605.06594v1) | 临床报告自动生成 | 两种方法存在临床可靠性与语言质量的清晰权衡，模板法多维度得分更高，GPT-4输出更简洁，对比... | — | — | — |
| 6 | low | - | [CAST: Mitigating Object Hallucination in Large Vision-Language M...](http://arxiv.org/abs/2605.04641) | 对象幻觉缓解 | 观察到大视觉语言模型回答描述查询比非描述查询对视觉信息注意力显著更强，该方法平均降低6.03... | — | — | — |
| 7 | low | - | [Cited but Not Verified: Parsing and Evaluating Source Attributio...](http://arxiv.org/abs/2605.06635v1) | 来源归因评估 | 前沿模型链接有效性超94%、相关性超80%，事实准确率仅39-77%，检索量增加事实准确率平... | — | — | — |
| 8 | low | - | [Compositional Multi-hop Factual Error Correction via Decompositi...](http://arxiv.org/abs/2605.02277v1) | 多跳事实纠错 | 基于分解注入范式的CECoR，多跳事实纠错性能优于两类对比基线，同时具备良好的泛化性与抗噪性 | — | — | — |
| 9 | low | - | [CuraView: A Multi-Agent Framework for Medical Hallucination Dete...](http://arxiv.org/abs/2605.03476v1) | 医疗幻觉检测 | 微调Qwen3-14B检测模型E4F1达0.831，E3+E4F1达0.823，相对基模提升... | — | — | — |
| 10 | low | - | [Detecting Hallucinations in Large Language Models via Internal A...](http://arxiv.org/abs/2605.05025v1) | 大模型幻觉检测 | 注意力发散信号集中在模型中间层，且主要分布在命名实体、数字这类事实性令牌上。 | — | — | — |
| 11 | low | - | [EditPropBench: Measuring Factual Edit Propagation in Scientific ...](http://arxiv.org/abs/2605.02083v1) | 事实编辑评测 | 在硬隐式自由分层中，五个LLM编辑系统ERA得分0.148-0.705，最强模型仍漏约30%... | — | — | — |
| 12 | low | - | [Estimating the Black-box LLM Uncertainty with Distribution-Align...](http://arxiv.org/abs/2605.05777v1) | 不确定性量化 | 仅占目标黑盒大语言模型大小1%的轻量代理模型，就可以实现可靠的黑盒LLM不确定性量化 | — | — | — |

## 方法族分布

- **大模型幻觉检测**：3 篇
- **流程执行诊断**：1 篇
- **大模型信息检索**：1 篇
- **个性化LLM摘要**：1 篇
- **幻觉在线自校准**：1 篇
- **大模型幻觉评测**：1 篇
- **多跳事实纠错**：1 篇
- **事实编辑评测**：1 篇
- **AI合规缺口**：1 篇
- **幻觉缓解**：1 篇
- **视觉语言推理**：1 篇
- **表格推理RAG**：1 篇

## 代码资源

- [TriBench-Ko: Evaluating LLM Risks in Judicial Workflows](https://github.com/holi-lab/TriBench-Ko) · 5 stars
- [SERE: Structural Example Retrieval for Enhancing LLMs in Event Causality Identif...](https://github.com/DMIRLAB-Group/SERE.)

## 常见基线方法

- **专家撰写的静态简明摘要**：1 篇
- **NLI验证**：1 篇
- **RAV方法**：1 篇
- **远监督方法**：1 篇
- **少样本大语言模型基线**：1 篇
- **确定性替换基线**：1 篇
- **IFEval**：1 篇
- **SWE-bench**：1 篇
- **BFCL**：1 篇
- **COMPASS**：1 篇

## 常用数据集

- **摘要未提及**：2 篇
- **ReLay**：1 篇
- **HalluScan基准**：1 篇
- **多跳事实纠错基准**：1 篇
- **EditPropBench**：1 篇
- **arXiv cs.CL基准数据集论文**：1 篇
- **BS-Bench**：1 篇
- **Multi-Table-RAG-Lib**：1 篇
- **LOCOMO**：1 篇
- **LongMemEval**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*