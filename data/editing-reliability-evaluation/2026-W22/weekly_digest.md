# 编辑可靠性与行为控制 — 2026-W22 (05/25-05/31)

本周新增 **30** 篇论文，**6** 篇附带代码。优先级：high 27 / medium 3 / low 0。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Distributed Multi-Layer Editing for Rule-Level Knowledge in Larg...](http://arxiv.org/abs/2604.08284v1) | locate-then-edit | Transformer中公式和描述集中在较早层，实例与中间层关联更强，DMLE比最强基线平均... | 在GPT-J-6B等四个主流大模型上评测，验证方法在实例可迁移性、规则理解上的性... | 单一层/连续块干预编辑，无法可靠编辑跨多形式的规则层知识 | ✅ |
| 2 | high | - | [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editin...](http://arxiv.org/abs/2604.12559v1) | framework/tooling | 将离散事实锚定在Transformer浅层、仅最小更新深层，可兼顾整体编辑性能与细粒度事实访... | 推出带细粒度问答对与事实级指标的诊断基准UnFine，评测方法的细粒度问答与整体... | 现有非结构化模型编辑后缺乏可靠的细粒度事实访问能力 | ✅ |
| 3 | high | - | [From Fact Overwriting to Knowledge Evolution: Causal Editing via...](http://arxiv.org/abs/2605.28303v1) | other | 原静态知识覆盖范式自我反驳率达95.6%，本文CODE方法可将其降至1.8%，多跳准确率可达... | 在LLaMA-3.1和Qwen-2.5两个大模型上评测了自我反驳率与多跳推理准确... | 静态事实覆盖破坏模型知识拓扑，引发认知失调，导致模型出现高自我反... | ✅ |
| 4 | high | - | [HoReN: Normalized Hopfield Retrieval for Large-Scale Sequential ...](http://arxiv.org/abs/2605.08143v2) | memory-based editor | HoReN可在ZsRE上支撑5万次顺序编辑，仍保持整体性能高于0.93，现有方法在1万次编辑... | 在标准、结构化、非结构化三类基准评测编辑性能，重点验证大规模顺序编辑下的性能稳定... | 顺序编辑累积性能退化，万级编辑前发生性能崩溃，复述输入泛化能力差 | ✅ |
| 5 | high | - | [Modality-Decoupled Online Recursive Editing](http://arxiv.org/abs/2605.20273v1) | 在线编辑方法 | 模态解耦可避免视觉主导的更新偏差，正交低秩子空间可缓解长程编辑干扰，单编辑开销恒定。 | 在多个多模态大模型骨干与在线编辑基准上，评测了方法的可靠性、通用性、局部性与效率... | 现有方法应用于多模态在线编辑存在跨模态冲突与长程编辑间干扰 | ✅ |
| 6 | high | - | [The Model Agreed, But Didn't Learn: Diagnosing Surface Complianc...](http://arxiv.org/abs/2604.05995v1) | evaluation/benchmark | 当前知识编辑普遍存在表面合规，仅模仿目标输出未修改内部信念，递归修改会累积残留降低记忆可逆性 | 关注大语言模型知识编辑是否完成真正的结构性记忆修改，检测表面合规问题与递归编辑的... | 知识编辑仅表面合规未真修改内部信念，递归编辑累积残留引发认知不稳... | ✅ |
| 7 | high | - | [Automatically Finding and Validating Unexpected Side-Effects of ...](http://arxiv.org/abs/2605.05090v1) | framework/tooling | 合成设置中可可靠恢复注入的已知行为变化，真实场景能区分大小干预，无效应时不产生幻觉差异 | 验证该方法能可靠识别干预的预期与意外副作用，无效应时不幻觉差异，可区分不同程度的... | 难以自动化发现干预的意外副作用，易幻觉出不存在的行为差异 | — |
| 8 | high | - | [Benchmarking Safety Risks of Knowledge-Intensive Reasoning under...](http://arxiv.org/abs/2605.10146v1) | evaluation/benchmark | 恶意知识编辑可稳定诱导错误不安全推理，还能保留大模型通用能力，风险难检测，受三类关键因素影响 | 从攻击有效性、推理正确性、副作用三个维度，评测恶意知识编辑对知识密集推理的安全风... | 现有基准缺乏对恶意知识编辑安全风险的系统评估，恶意编辑引发的风险... | — |
| 9 | high | - | [BetaEdit: Null-Space Constrained Sequential Model Editing](http://arxiv.org/abs/2605.09285v1) | framework/tooling | 现有零空间编辑方法因依赖近似零空间固有存在知识泄露，历史感知更新可有效缓解长程顺序编辑的性能... | 在两个标准基准的三个大语言模型上开展实验，验证所提方法在大规模顺序编辑中的性能优... | 知识泄露、大规模顺序编辑过程中的性能严重衰退 | — |
| 10 | high | - | [Beyond Binary Edits Robust Multimodal Knowledge Editing with Adv...](http://arxiv.org/abs/2605.23780v1) | steering | 将语义等价多模态输入归为知识单元，结合对抗生成与低秩对齐可有效提升多模态知识编辑的泛化鲁棒性 | 重点评测所提方法提升多模态知识编辑的鲁棒性，以及跨语义等价多模态变体的泛化能力 | 现有多模态知识编辑无法将编辑传播到语义等价的多模态变体，泛化性不... | — |
| 11 | high | - | [Beyond the Covariance Trap: Unlocking Generalization in Same-Sub...](http://arxiv.org/abs/2603.15518) | locate-then-edit | 同一主体知识编辑泛化崩溃的几何根源是提示变化引发的激活漂移超出编辑后模型的泛化容差，标准协方... | 重点评测方法提升同一主体知识编辑后，模型在不同用户指令下召回更新知识的泛化鲁棒性 | 同一主体知识编辑后，提示变化引发激活漂移导致泛化崩溃，无法召回更... | — |
| 12 | high | - | [Closed-Form Concept Erasure via Double Projections](http://arxiv.org/abs/2604.10032v1) | unlearning | 仅需两步闭式投影且无需训练，耗时仅数秒，在多个生成模型上效果超SOTA，更忠实保留非目标概念 | 在多个不同生成模型上评测了概念擦除性能、非目标概念保留效果以及方法运行效率 | 现有概念擦除方法易扭曲无关非目标概念，依赖迭代优化导致运行效率低... | — |

## A 会 / Venue 标签

- **ICML 2026**：1 篇

## 方法族分布

- **locate-then-edit**：8 篇
- **evaluation/benchmark**：7 篇
- **framework/tooling**：6 篇
- **other**：3 篇
- **steering**：1 篇
- **在线编辑方法**：1 篇
- **memory-based editor**：1 篇
- **meta-learning editor**：1 篇
- **unlearning**：1 篇
- **结构隔离编辑**：1 篇

## 失败模式与风险信号

- 因果错位导致编辑泛化不足，特征纠缠引发无关信息意外编辑
- 任务向量投影到SAE特征子空间形成信息瓶颈，丢弃大量修改能量导致编辑无效
- 静态事实覆盖破坏模型知识拓扑，引发认知失调，导致模型出现高自我反驳率。
- 现有多模态知识编辑无法将编辑传播到语义等价的多模态变体，泛化性不足
- 现有方法应用于多模态在线编辑存在跨模态冲突与长程编辑间干扰
- 知识注入后模型发生灾难性遗忘，原有预训练能力大幅下降
- 多语言编辑之间相互串扰
- 顺序长期编辑灾难性遗忘、模型性能崩溃
- 现有基准缺乏对恶意知识编辑安全风险的系统评估，恶意编辑引发的风险难以检出
- 知识泄露、大规模顺序编辑过程中的性能严重衰退

## 评测信号

- 在多个基准和不同MLLM上评测，验证方法向相关上下文传播编辑同时保持高局部性的性能。
- 在Minerva Math基准7个数学推理科目评测，5个科目显著提升，无显著下降，方法无额外推理成本
- 在LLaMA-3.1和Qwen-2.5两个大模型上评测了自我反驳率与多跳推理准确率，验证方法效果。
- 重点评测所提方法提升多模态知识编辑的鲁棒性，以及跨语义等价多模态变体的泛化能力
- 在多个多模态大模型骨干与在线编辑基准上，评测了方法的可靠性、通用性、局部性与效率。
- 评测不同模型规模下，知识注入后新记忆获取与原有预训练能力保留的权衡表现
- 在大规模批量编辑场景下，评测不同向量合并方法的性能、抗干扰能力及超参数对性能的影响
- 评测长时序顺序编辑下模型的稳定性与编辑性能，验证所提理论正确性与方法的竞争力
- 从攻击有效性、推理正确性、副作用三个维度，评测恶意知识编辑对知识密集推理的安全风险
- 在两个标准基准的三个大语言模型上开展实验，验证所提方法在大规模顺序编辑中的性能优势。

## 代码资源

- [Distributed Multi-Layer Editing for Rule-Level Knowledge in Large Language Model...](https://github.com/Pepper66/DMLE.) · 4 stars
- [Modality-Decoupled Online Recursive Editing](https://github.com/lab-klc/M-ORE.) · 1 stars
- [HoReN: Normalized Hopfield Retrieval for Large-Scale Sequential Model Editing](https://github.com/ha11ucin8/HoReN.) · 1 stars
- [The Model Agreed, But Didn't Learn: Diagnosing Surface Compliance in Large Langu...](https://github.com/XiaojieGu/SA-MCQ.) · 1 stars
- [From Fact Overwriting to Knowledge Evolution: Causal Editing via On-Policy Self-...](https://github.com/CrashBugger/CODE.)
- [FABLE: Fine-grained Fact Anchoring for Unstructured Model Editing](https://github.com/caskcsg/FABLE.)

## 常见基线方法

- **基于SAE特征子空间投影的SAE引导模型编辑方法**：1 篇
- **监督微调(SFT)**：1 篇
- **在线策略自蒸馏**：1 篇
- **无共享协方差简单求和**：1 篇
- **单语定位后编辑方法**：1 篇
- **现有零空间类模型编辑方法**：1 篇
- **现有历史感知编辑方法**：1 篇
- **五种现有大语言模型编辑系统**：1 篇
- **现有终身知识编辑方法**：1 篇
- **LoRA**：1 篇

## 常用数据集

- **Minerva Math基准**：1 篇
- **自建合成语料**：1 篇
- **开放域事实问答基准**：1 篇
- **知识编辑基准**：1 篇
- **MzsRE**：1 篇
- **标准模型编辑基准1**：1 篇
- **标准模型编辑基准2**：1 篇
- **EC-Bench**：1 篇
- **EditPropBench**：1 篇
- **ZsRE**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*