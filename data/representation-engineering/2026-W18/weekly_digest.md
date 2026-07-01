# representation-engineering — 2026-W18 (04/27-05/03)

本周新增 **13** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 13。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Prefill-Time Intervention for Mitigating Hallucination in Large ...](http://arxiv.org/abs/2604.25642v1) | 大模型幻觉缓解 | PTI仅在预填充阶段干预一次，将键引向视觉接地目标、值过滤噪声，可与现有解码方法正交集成。 | — | — | ✅ |
| 2 | low | - | [AIPsy-Affect: A Keyword-Free Clinical Stimulus Battery for Mecha...](http://arxiv.org/abs/2604.23719v2) | 情绪可解释性 | 上下文分类器可检测该库的情绪存在（p<10^-15），但情绪类别top-1准确率仅5.2%，... | — | — | — |
| 3 | low | - | [Architecture Determines Observability in Transformers](http://arxiv.org/abs/2604.24801) | Transformer可观测性 | 24层16头Transformer配置可观测性约为0.10，其余配置在0.21-0.38，训... | — | — | — |
| 4 | low | - | [Contextual Linear Activation Steering of Language Models](http://arxiv.org/abs/2604.24693v1) | 大模型激活引导 | 在11个引导基准、4个模型族中，CLAS持续优于标准线性激活引导，有限标注数据下性能匹配或超... | — | — | — |
| 5 | low | - | [DPN-LE: Dual Personality Neuron Localization and Editing for Lar...](http://arxiv.org/abs/2604.27929v1) | 大模型性格编辑 | 神经元具有多功能性，同时关联性格特质与通用知识，对立性格特质呈现互斥表示模式 | — | — | — |
| 6 | low | - | [How LLMs Detect and Correct Their Own Errors: The Role of Intern...](http://arxiv.org/abs/2604.22271) | 大模型自我纠错 | PANL信号可超出对数概率、语言置信预测错误检测，还能预测可纠正错误，对错误检测存在因果作用... | — | — | — |
| 7 | low | - | [Latent Adversarial Detection: Adaptive Probing of LLM Activation...](http://arxiv.org/abs/2604.28129) | 大模型攻击检测 | 多轮攻击存在对抗躁动特征，加入该特征将检测准确率从76.2%提升至93.8%，探针无法跨架构... | — | — | — |
| 8 | low | - | [Latent Agents: A Post-Training Procedure for Internalized Multi-...](http://arxiv.org/abs/2604.24881v1) | 多智能体辩论蒸馏 | 内化会生成对应不同智能体视角的激活可解释子空间，匹配性能时最高减93%token，控有害行为... | — | — | — |
| 9 | low | - | [Perturbation Probing: A Two-Pass-per-Prompt Diagnostic for FFN B...](http://arxiv.org/abs/2604.27401) | FFN回路探测 | 安全拒绝任务中仅约0.014%（50个）神经元控制拒绝模板，消融后仅3/520样本出现有害合... | — | — | — |
| 10 | low | - | [Representational Curvature Modulates Behavioral Uncertainty in L...](http://arxiv.org/abs/2604.23985) | 大模型表征研究 | 在GPT-2 XL和Pythia-2.8B中，上下文曲率与下token熵相关，轨迹对齐曲率干... | — | — | — |
| 11 | low | - | [Subliminal Steering: Stronger Encoding of Hidden Signals](http://arxiv.org/abs/2604.25783v1) | 阈下偏差编码 | 阈下学习不仅转移目标行为偏差，还会转移定位在教师对应层的原引导向量，新向量与原向量余弦相似度... | — | — | — |
| 12 | low | - | [TimingLLM: A Two-Stage Retrieval-Augmented Framework for Pre-Syn...](http://arxiv.org/abs/2604.23602v1) | 预合成时序预测 | 在VerilogEval上该方法R_WNS达0.91、R_TNS达0.97，速度比以往方法快... | — | — | — |

## 方法族分布

- **大模型自我纠错**：1 篇
- **阈下偏差编码**：1 篇
- **大模型幻觉缓解**：1 篇
- **多智能体辩论蒸馏**：1 篇
- **大模型激活引导**：1 篇
- **情绪可解释性**：1 篇
- **预合成时序预测**：1 篇
- **错位推理检测**：1 篇
- **大模型表征研究**：1 篇
- **Transformer可观测性**：1 篇
- **大模型性格编辑**：1 篇
- **FFN回路探测**：1 篇

## 代码资源

- [Prefill-Time Intervention for Mitigating Hallucination in Large Vision-Language ...](https://github.com/huaiyi66/PTI.) · 2 stars

## 常见基线方法

- **一阶置信模型**：1 篇
- **token对数概率**：1 篇
- **语言置信信号**：1 篇
- **行为信号**：1 篇
- **基于系统提示的传统阈下学习方法**：1 篇
- **显式多智能体辩论**：1 篇
- **基础大语言模型**：1 篇
- **标准线性激活引导**：1 篇
- **ReFT**：1 篇
- **LoRA**：1 篇

## 常用数据集

- **TriviaQA**：1 篇
- **MNLI**：1 篇
- **多个基准测试集**：1 篇
- **摘要未提及具体数据集名称**：1 篇
- **AIPsy-Affect临床刺激库**：1 篇
- **早期96项情绪刺激库**：1 篇
- **VerilogEval**：1 篇
- **6万模块带合成报告Verilog语料**：1 篇
- **MoralChain**：1 篇
- **Pile**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*