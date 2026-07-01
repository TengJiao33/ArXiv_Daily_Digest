# representation-engineering — 2026-W22 (05/25-05/31)

本周新增 **31** 篇论文，**1** 篇附带代码。优先级：high 0 / medium 0 / low 31。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Multi-Adapter Representation Interventions via Energy Calibratio...](http://arxiv.org/abs/2605.28722) | 大模型对齐 | 不同输入样本所需的合适干预方向和强度差异很大，统一固定干预会降低良性输入的通用能力 | — | — | ✅ |
| 2 | low | - | [An Effective-Rank Audit of Alignment-Induced Activation Shifts: ...](http://arxiv.org/abs/2605.24583v1) | 大模型对齐审计 | 三类模型控聊天模板后rho_eps为0.0029、0.0048、0.0044，谱隙假设仅1/... | — | — | — |
| 3 | low | - | [Beyond Attack Success Rate: Temporal Logit Observability for LLM...](http://arxiv.org/abs/2605.29629v1) | 大模型安全评估 | ASR相近的不同攻击在TLO二维平面位置区分明显，基于TLO的早停可削减超半数成功越狱且对良... | — | — | — |
| 4 | low | - | [Beyond a Single Direction: Chain-of-Thought Disrupts Simple Stee...](http://arxiv.org/abs/2605.26772v1) | 大模型拒绝调控 | 固定CoT时激活转向仅反转39%拒绝，移除CoT升至70%，干预再生CoT后反转率达94%，... | — | — | — |
| 5 | low | - | [Can LLMs Introspect? A Reality Check](http://arxiv.org/abs/2605.26242) | 大模型内省能力 | 两个现有内省评估范式都无法证明模型有专属内部访问权，新增控制任务下模型表现接近随机 | — | — | — |
| 6 | low | - | [Causal Interventions on Continuous Variables: A Case Study on Ve...](http://arxiv.org/abs/2605.29971v1) | 语言模型因果干预 | 反事实编辑动词偏向可系统性改变下游结构偏好，转向向量编码的误差信号未被下游生成因果使用 | — | — | — |
| 7 | low | - | [Causal Physics Steering in Video World Models via Concept Activa...](http://arxiv.org/abs/2605.24322) | 物理推理引导 | 仅在物理涌现区PEZ内干预才生效，物理与运动方向分开编码，不同物理原理占表示空间不同方向 | — | — | — |
| 8 | low | - | [Causal Tongue-Tie: LLMs Can Encode Causal Direction, But Their Y...](http://arxiv.org/abs/2605.25891v1) | 因果推理评估 | 在反常识CLadder测试项中，探针从隐藏态恢复答案准确率约0.97，模型Yes/No输出准... | — | — | — |
| 9 | low | - | [Cultural Value Alignment Via Latent Activation Steering in Large...](http://arxiv.org/abs/2605.26365v1) | 文化价值对齐 | 发现大语言模型存在潜在纠缠现象，沿一个文化维度的干预会引发另一文化维度偏移 | — | — | — |
| 10 | low | - | [DFKI-MLT at SemEval-2026 TASK 7: Steering Multilingual Models To...](http://arxiv.org/abs/2605.23069v1) | 文化知识引导 | MCQ赛道获86.96%准确率，激活引导提升异质且分层敏感，提示设计与激活引导需联合优化。 | — | — | — |
| 11 | low | - | [Is Inference Mediated by Distinct Semantic Structures in LLMs? A...](http://arxiv.org/abs/2605.25520v1) | 大模型机制分析 | 语义变换效果解码准确率达84.8%-99%，对应子空间可因果影响预测，可导引性因模型不同存在... | — | — | — |
| 12 | low | - | [Memory-Induced Tool-Drift in LLM Agents](http://arxiv.org/abs/2605.24941v1) | 智能体工具漂移 | 偏置记忆作为隐式引导向量改变激活，还会重分配注意力，可使偏转分数在1-5分制上最高提升3.6... | — | — | — |

## 方法族分布

- **因果推理评估**：1 篇
- **大模型机制分析**：1 篇
- **认知机制检验**：1 篇
- **智能体工具漂移**：1 篇
- **大模型对齐审计**：1 篇
- **机制可解释性**：1 篇
- **安全对齐放松**：1 篇
- **文化知识引导**：1 篇
- **多语言引导**：1 篇
- **不确定性量化**：1 篇
- **医学VLM去幻觉**：1 篇
- **语言模型引导**：1 篇

## 代码资源

- [Multi-Adapter Representation Interventions via Energy Calibration](https://github.com/V1centNevwake/MARI.)

## 常见基线方法

- **大语言模型Yes/No输出**：1 篇
- **随机子空间**：1 篇
- **无偏基准**：1 篇
- **基于提示的相关性指令**：1 篇
- **内存过滤器**：1 篇
- **LRH基线方法**：1 篇
- **Arditi等人单拒绝方向方法**：1 篇
- **标准SAE通用性度量**：1 篇
- **常数均值预测**：1 篇
- **高成本重对齐方法**：1 篇

## 常用数据集

- **CLadder**：1 篇
- **MEMDRIFT基准数据集**：1 篇
- **MCP服务器工具集**：1 篇
- **Dyck-3**：1 篇
- **The Pile**：1 篇
- **FLORES**：1 篇
- **CrossSumm**：1 篇
- **MIMIC-CXR**：1 篇
- **IU-Xray**：1 篇
- **四任务语言模型算术基准**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*