# representation-engineering — 2026-W20 (05/11-05/17)

本周新增 **21** 篇论文，**0** 篇附带代码。优先级：high 0 / medium 0 / low 21。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Dissecting Jet-Tagger Through Mechanistic Interpretability](http://arxiv.org/abs/2605.09881v1) | 机械可解释性 | 识别出稀疏六头分类电路，早中晚层头分工明确，残差流更偏好对齐能量相关算子基 | — | — | — |
| 2 | low | - | [Do Linear Probes Generalize Better in Persona Coordinates?](http://arxiv.org/abs/2605.09391v1) | 线性探针泛化 | 在10个评估数据集上，人设PC投影训练的探针比原始激活探针泛化更好，多行为统一轴泛化更优 | — | — | — |
| 3 | low | - | [Emergent Semantic Role Understanding in Language Models](http://arxiv.org/abs/2605.09187v1) | 语义角色涌现 | 冻结预训练表征包含大量语义角色信息，性能不及微调模型，模型规模越大越偏向分布式表征 | — | — | — |
| 4 | low | - | [Inference-Time Machine Unlearning via Gated Activation Redirecti...](http://arxiv.org/abs/2605.12765v1) | 推理时机器遗忘 | GUARD-IT是唯一在所有测试设置中同时保留效用、抑制记忆、避免灾难性崩溃的方法，量化场景... | — | — | — |
| 5 | low | - | [KamonBench: A Grammar-Based Dataset for Evaluating Compositional...](http://arxiv.org/abs/2605.13322v1) | 组合因子恢复评估 | KamonBench每个样本带有已知容器、修饰、基序生成因子，支持多维度评估，超越仅描述级准... | — | — | — |
| 6 | low | - | [LLM Agents Already Know When to Call Tools -- Even Without Reaso...](http://arxiv.org/abs/2605.09252v1) | 工具调用决策 | 工具必要性可从预生成表示线性解码，六模型AUROC达0.89-0.96，Probe&Pref... | — | — | — |
| 7 | low | - | [MC-RFM: Geometry-Aware Few-Shot Adaptation via Mixed-Curvature R...](http://arxiv.org/abs/2605.08557v1) | 小样本适配 | 在五个骨干、1/4/16-shot设置下，MC-RFM多数实验最优，对Transformer... | — | — | — |
| 8 | low | - | [Mathematical Reasoning via Intervention-Based Time-Series Causal...](http://arxiv.org/abs/2605.07600) | 大模型数学推理 | 已解决Omni-MATH问题的ATE比未解决高6.1倍，CIKA在基础模型失败题中贡献33.... | — | — | — |
| 9 | low | - | [Metaphor Is Not All Attention Needs](http://arxiv.org/abs/2605.12128v1) | 大模型越狱分析 | 模型能高准确率区分诗歌与散文格式，聚类结果按文学格式分离而非安全标签，无法预测越狱成功 | — | — | — |
| 10 | low | - | [Probing Persona-Dependent Preferences in Language Models](http://arxiv.org/abs/2605.13339v1) | 角色偏好探测 | 偏好表示跨角色大体共享，有益助手训练的探针可预测、操控偏好与助手反相关的邪恶角色的选择 | — | — | — |
| 11 | low | - | [Prompt-Activation Duality: Improving Activation Steering via Att...](http://arxiv.org/abs/2605.10664v1) | 激活引导优化 | 在多轮基准上平均连贯性漂移从-18.6改善至-1.9，第10轮特质表达从78.0提升至93.... | — | — | — |
| 12 | low | - | [ProteinJEPA: Latent prediction complements protein language mode...](http://arxiv.org/abs/2605.07554v1) | 蛋白质预训练 | 匹配预算下，所提方案在ESM2-35M获10胜3负3平，ESM2-150M获11胜2负3平，... | — | — | — |

## 方法族分布

- **激活引导优化**：1 篇
- **大模型路由决策**：1 篇
- **探针分析**：1 篇
- **机械可解释性**：1 篇
- **线性探针泛化**：1 篇
- **工具调用决策**：1 篇
- **计数失败机制**：1 篇
- **时序知识漂移**：1 篇
- **语义角色涌现**：1 篇
- **小样本适配**：1 篇
- **潜在规划定位**：1 篇
- **蛋白质预训练**：1 篇

## 常见基线方法

- **标准残差流激活引导**：1 篇
- **Always-RAG**：1 篇
- **Always-LC**：1 篇
- **Self-Route**：1 篇
- **原始激活训练的线性探针**：1 篇
- **仅提示（Prompt-only）方法**：1 篇
- **先推理后行动（Reason-then-Act）方法**：1 篇
- **token熵方法**：1 篇
- **语义熵方法**：1 篇
- **CCS**：1 篇

## 常用数据集

- **LaRA**：1 篇
- **LongBench-v2**：1 篇
- **奥赛罗棋盘游戏数据**：1 篇
- **顶夸克标记参考数据集**：1 篇
- **10个评估数据集**：1 篇
- **When2Tool基准**：1 篇
- **七个视觉识别基准**：1 篇
- **SCOPe-40**：1 篇
- **TAPE**：1 篇
- **Omni-MATH**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*