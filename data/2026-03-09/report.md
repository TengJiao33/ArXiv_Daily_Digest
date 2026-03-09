# 🧪 ArXiv AI 日报

📅 **2026-03-09 周一** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **50,122** (¥0.0165)

## 🔥 今日必读

---

### 1. SAHOO: Safeguarded Alignment for High-Order Optimization Objectives in Recursive Self-Improvement

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.06333v1)

👤 Subramanyam Sahoo, Aman Chadha, Vinija Jain 等


**中文标题**: SAHOO：递归自改进中高阶优化目标的防护式对齐框架
**背景与痛点**: 递归自改进正从理论走向工程落地，当前大模型已能自主完成输出的评估、修订和迭代改进，但多轮自修改过程中容易产生难以察觉的对齐累积漂移，现有方法缺乏可落地的系统化防护机制，无法兼顾能力提升和对齐稳定性。
**核心创新**: 提出SAHOO这套可落地的对齐漂移监控控制框架，通过三类互补防护机制系统性约束自改进过程中的对齐风险，所有阈值和权重都从小规模校准集数据驱动学习得到，无需人工预设超参数，还提出能力对齐比量化自改进的核心权衡。
**技术细节**: SAHOO包含三层核心防护：一是目标漂移指数GDI，融合语义、词汇、结构、分布四个维度的漂移信号，通过校准集学习组合权重，综合量化对齐偏离程度；二是约束保留检查，对语法正确性、不幻觉等安全关键不变量做硬校验，违规施加惩罚，严重违规直接终止迭代；三是回归风险量化，通过历史质量波动估计后续能力回退概率，风险超标触发停止，额外提出能力对齐比衡量单位漂移对应的能力增益。
**实验结果**: 在HumanEval、TruthfulQA、GSM8K三个领域共189个任务测试，仅用18个任务做校准，最终代码生成提升18.3%，数学推理提升16.8%，诚实性提升3.8%，代码和数学实现零约束违规，诚实性约束保留率达98.7%，证实框架可在控制对齐风险的前提下获得稳定能力提升。

---

### 2. Talk Freely, Execute Strictly: Schema-Gated Agentic AI for Flexible and Reproducible Scientific Workflows

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.06394v1)

👤 Joel Strickland, Arjun Vijeta, Chris Moores 等


**中文标题**: 畅所欲言，严格执行：面向灵活可复现科研工作流的模式门控智能体AI

**背景与痛点**: 当前大语言模型驱动的科研工作流存在固有矛盾：纯生成式方案支持自然语言对话探索的灵活性，但无法保证执行确定性、可复现性和可审计性；传统工作流管理系统能提供强确定性，却交互僵硬，不支持迭代式探索。工业界研发从业者同时要求两类特性，现有架构无法同时满足。

**核心创新**: 提出模式门控编排架构原则，通过分离对话权限与执行权限，将模式验证设为执行的必经边界：只有完整的、满足机器可验证规范（含跨步依赖）的操作才会执行，从架构上解耦了长期存在的灵活性-确定性权衡，适配工业科研的合规与迭代需求。

**技术细节**: 设计分层参考架构，大语言模型仅保留对话权限，负责意图解析、任务分解和交互澄清；执行权限完全交给模式验证层，所有工具、工作流都预先注册并完成模式合规检查；编排控制器在执行前对完整工作流做全链路验证，检查图无环性、跨步类型兼容性、参数合法性，不通过则触发对话澄清，遵循执行前澄清、约束计划-执行、工具到工作流级门控三大原则。

**实验结果**: 对20款代表性现有系统做了多大模型盲评，三个主流大模型家族共15轮独立打分，对执行确定性和对话灵活性打分的一致性达到克里彭多夫alpha值0.80和0.98，证实现有系统存在灵活性-确定性帕累托前沿，无系统同时达到双高，仅模式门控类架构落在双高目标区域。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Beyond Rows to Reasoning: Agentic Retrieval for Multimodal Spreadsheet Understan...](http://arxiv.org/abs/2603.06503v1) `cs.CL (计算语言学)` | 企业级电子表格存在百万单元格、跨表依赖等难点，现有多模态RAG难以处理，该工作提出Agentic检索方案，解决了企业办公场景的核心痛点 |
| 5 | [BEVLM: Distilling Semantic Knowledge from LLMs into Bird's-Eye View Representati...](http://arxiv.org/abs/2603.06576v1) `cs.CV (计算机视觉)` | 自动驾驶BEV表示缺乏足够语义理解能力，该工作将LLM的语义知识蒸馏到BEV表示中，推进了大模型与自动驾驶感知的融合，工业落地价值高 |
| 6 | [COLD-Steer: Steering Large Language Models via In-Context One-step Learning Dyna...](http://arxiv.org/abs/2603.06495v1) `cs.LG (机器学习)` | 现有LLM推理阶段激活引导存在效果与样本效率的 trade-off，该工作提出上下文单步动力学引导，无需重训即可更好控制模型行为，实用性强 |
| 7 | [Physical Simulator In-the-Loop Video Generation](http://arxiv.org/abs/2603.06408v1) `cs.CV (计算机视觉)` | 现有扩散视频生成结果普遍违背物理规律，该工作将物理模拟器嵌入生成环路，提升了生成内容的物理一致性，解决了当前视频生成的核心缺陷 |
| 8 | [MoEless: Efficient MoE LLM Serving via Serverless Computing](http://arxiv.org/abs/2603.06350v1) `cs.DC` | MoE大模型工业部署普遍存在推理效率低、成本高的痛点，该工作提出基于无服务器计算的MoE serving方案，大幅优化部署成本与效率 |
| 9 | [From Entropy to Calibrated Uncertainty: Training Language Models to Reason About...](http://arxiv.org/abs/2603.06317v1) `cs.LG (机器学习)` | 现有LLM不确定性估计多依赖后处理采样，效率低校准性差，该工作直接训练模型自带可解释校准的不确定性，适配医疗等高风险场景需求 |
| 10 | [When One Modality Rules Them All: Backdoor Modality Collapse in Multimodal Diffu...](http://arxiv.org/abs/2603.06508v1) `cs.LG (机器学习)` | 多模态扩散模型的安全风险研究尚不充分，该工作发现了后门攻击下的模态崩溃新漏洞，揭示了多模态生成的新安全问题，对领域研究有重要价值 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-09
