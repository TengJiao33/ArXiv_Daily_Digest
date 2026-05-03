# 表示工程与激活引导 — 2026-W18 (04/27-05/03)

本周新增 **13** 篇论文。1 篇附带代码仓库。

## 分类分布

- `via-citation`: 5 篇
- `cs.CL`: 4 篇
- `cs.AI`: 2 篇
- `cs.CV`: 1 篇
- `cs.AR`: 1 篇

## 论文列表

| # | 论文 | 核心方法 | 主要贡献 | 代码 |
|:-:|------|---------|---------|:----:|
| 1 | [How LLMs Detect and Correct Their Own Errors: The Role of In...](http://arxiv.org/abs/2604.22271) | 基于决策神经科学二阶置信框架，采用验证后纠正范式，结合因果干预检验PANL信号作... | 揭示大语言模型天然具备二阶置信架构，内部评估信号可编码答案正误与自我修复可能性。 | — |
| 2 | [Subliminal Steering: Stronger Encoding of Hidden Signals](http://arxiv.org/abs/2604.25783v1) | 提出阈下引导方法，使用训练好的引导向量而非系统提示实现教师模型的偏差编码 | 验证了可转移复杂多词偏差，给出阈下学习的机制证据，证实偏差编码具备高精度 | — |
| 3 | [Prefill-Time Intervention for Mitigating Hallucination in La...](http://arxiv.org/abs/2604.25642v1) | 提出预填充阶段干预PTI方法，在错误积累前增强初始KV缓存，分模态修正幻觉易感表... | PTI可有效减轻幻觉，泛化性强，可与现有解码方法即插即用结合进一步提升性能。 | ✅ |
| 4 | [Latent Agents: A Post-Training Procedure for Internalized Mu...](http://arxiv.org/abs/2604.24881v1) | 通过结合辩论结构学习、动态奖励调度与长度截断的两阶段微调，将多智能体辩论蒸馏到单... | 所得内化模型性能匹配或超越显式辩论，最高减少93%token，为内化推理行为控制... | — |
| 5 | [Contextual Linear Activation Steering of Language Models](http://arxiv.org/abs/2604.24693v1) | 提出上下文线性激活引导方法CLAS，可根据输入上下文动态适配调整引导强度 | CLAS在多个基准与模型族上表现更优，是可扩展可解释准确的大模型专门化引导方法 | — |
| 6 | [AIPsy-Affect: A Keyword-Free Clinical Stimulus Battery for M...](http://arxiv.org/abs/2604.23719v2) | 构建匹配对结构的无情绪关键词临床刺激库，采用三种NLP方法验证其无混淆特性。 | 推出四倍于旧版的480项AIPsy-Affect刺激库，消除关键词混淆，以MIT... | — |
| 7 | [TimingLLM: A Two-Stage Retrieval-Augmented Framework for Pre...](http://arxiv.org/abs/2604.23602v1) | 提出两阶段检索增强大语言模型框架TimingLLM，直接从Verilog预测WN... | 发布含6万个带合成报告模块的新Verilog语料，模型性能优于SOTA，预测速度... | — |
| 8 | [Ulterior Motives: Detecting Misaligned Reasoning in Continuo...](http://arxiv.org/abs/2604.23460v1) | 构建含12000个社会场景的MoralChain基准，用双触发范式训练带后门的连... | 提出专用检测基准，揭示错位推理的隐空间特性，验证检测有效性，指明安全监控方向 | — |
| 9 | [Representational Curvature Modulates Behavioral Uncertainty ...](http://arxiv.org/abs/2604.23985) | 将上下文曲率与下一token熵关联分析，开展扰动与正则化训练实验验证 | 证实表征轨迹曲率是影响大语言模型行为不确定性的任务对齐表征特征 | — |
| 10 | [Architecture Determines Observability in Transformers](http://arxiv.org/abs/2604.24801) | 定义可观测性为控制置信与激活范数后，冻结中层激活中逐词决策质量的线性可读性，以此... | 证明Transformer可观测性并非通用属性，架构决定可观测性，训练所得检测器... | — |
| 11 | [DPN-LE: Dual Personality Neuron Localization and Editing for...](http://arxiv.org/abs/2604.27929v1) | 提出DPN-LE方法，对比高低特质样本MLP激活筛选性格特异神经元，稀疏线性干预... | 所提方法仅干预约0.5%的神经元，实现有效性格控制同时，大幅保留模型的通用能力 | — |
| 12 | [Perturbation Probing: A Two-Pass-per-Prompt Diagnostic for F...](http://arxiv.org/abs/2604.27401) | 采用扰动探测法，每个提示两次前向传播无需反向传播，结合神经元干预扫描识别回路结构 | 识别出两种FFN行为回路结构，提出区分结构的预测指标，提供大模型精准编辑工具包 | — |
| 13 | [Latent Adversarial Detection: Adaptive Probing of LLM Activa...](http://arxiv.org/abs/2604.28129) | 提取大语言模型残差流中对抗躁动的标量轨迹特征，以此检测多轮攻击 | 证实对抗躁动是可靠的激活层攻击信号，明确了实际部署的数据要求，提升了检测性能 | — |

## 常见基线方法

- **一阶置信模型** (1 篇引用)
- **token对数概率** (1 篇引用)
- **语言置信信号** (1 篇引用)
- **行为信号** (1 篇引用)
- **基于系统提示的传统阈下学习方法** (1 篇引用)
- **显式多智能体辩论** (1 篇引用)
- **基础大语言模型** (1 篇引用)
- **标准线性激活引导** (1 篇引用)
- **ReFT** (1 篇引用)
- **LoRA** (1 篇引用)

## 本周提到的 Limitations

- 方向引导干预仅适用于满足条件的路由回路，在多类模型和多类任务回路中效果不佳
- 检测探针为模型特定，无法跨架构迁移，检测泛化能力依赖训练数据源

## 常用数据集

- **TriviaQA** (1 篇使用)
- **MNLI** (1 篇使用)
- **多个基准测试集** (1 篇使用)
- **摘要未提及具体数据集名称** (1 篇使用)
- **AIPsy-Affect临床刺激库** (1 篇使用)
- **早期96项情绪刺激库** (1 篇使用)
- **VerilogEval** (1 篇使用)
- **6万模块带合成报告Verilog语料** (1 篇使用)
- **MoralChain** (1 篇使用)
- **Pile** (1 篇使用)


---

*自动生成于 2026-05-03 | Research Radar*