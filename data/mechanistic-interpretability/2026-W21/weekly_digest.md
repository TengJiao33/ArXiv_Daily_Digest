# mechanistic-interpretability — 2026-W21 (05/18-05/24)

本周新增 **18** 篇论文，**2** 篇附带代码。优先级：high 0 / medium 0 / low 18。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Event-Grounded Sparse Autoencoders for Vision-Language-Action Po...](http://arxiv.org/abs/2605.17204v1) | VLA可解释性 | 在两种仿真架构和一项真实机器人研究中，事件接地排序对OpenVLA因果效应最强，可迁移至π_... | — | — | ✅ |
| 2 | low | - | [SegCompass: Exploring Interpretable Alignment with Sparse Autoen...](http://arxiv.org/abs/2605.22658v1) | 可解释推理分割 | 学习到的稀疏概念质量与最终分割掩码准确率呈强相关，SegCompass通过增强可检查对齐获得... | — | — | ✅ |
| 3 | low | - | [A Distributional View for Visual Mechanistic Interpretability: K...](http://arxiv.org/abs/2605.17504v1) | 视觉机制可解释性 | 发现现有视觉机制可解释性范式要么偏离自然图像分布难被人解读，要么无法激活模型特征缺乏机械忠实... | — | — | — |
| 4 | low | - | [A Sharper Picture of Generalization in Transformers](http://arxiv.org/abs/2605.20988v1) | Transformer泛化 | 稀疏度不超过上下文长度的任意布尔函数都存在平坦极小值，应用PAC-Bayes可得到非空的Tr... | — | — | — |
| 5 | low | - | [Aligned Training: A Parameter-Free Method to Improve Feature Qua...](http://arxiv.org/abs/2605.18629v1) | 稀疏自编码器改进 | 现有所有现代架构的SAE中，由编解码器方向内积定义的对齐得分呈现双峰分布 | — | — | — |
| 6 | low | - | [Are Sparse Autoencoder Benchmarks Reliable?](http://arxiv.org/abs/2605.18229v1) | 基准可靠性验证 | TPP和SCR在规范设置下未通过测试不应使用，最优的sae-probes也难区分同架构SAE... | — | — | — |
| 7 | low | - | [Babel: Jailbreaking Safety Attention via Obfuscation Distributio...](http://arxiv.org/abs/2605.17971v1) | 大模型越狱攻击 | 大模型安全对齐依赖少量稀疏分布注意力头，多数表征空间弱监控，GPT-4o上成功率从41.33... | — | — | — |
| 8 | low | - | [Beyond Linear Superposition: Discovering Climate Features in AI ...](http://arxiv.org/abs/2605.17493v1) | 模型可解释性 | KAN-SAE获得975个有效特征，较线性基线提升72%，特征冗余降低20%，可发现线性基线... | — | — | — |
| 9 | low | - | [Conceptualizing Embeddings: Sparse Disentanglement for Vision-La...](http://arxiv.org/abs/2605.22679v1) | 嵌入稀疏解耦 | 视觉语言表示中的明显纠缠可通过合适的基变换解决，不需要进行过完备的维度扩展 | — | — | — |
| 10 | low | - | [From Circuit Evidence to Mechanistic Theory: An Inductive Logic ...](http://arxiv.org/abs/2605.21303v1) | 机制可解释性 | CFS发现不同任务有不同计算策略：注意力介导复制、MLP介导绑定，ILP签名结构分离效果优于... | — | — | — |
| 11 | low | - | [From Correlation to Cause: A Five-Stage Methodology for Feature ...](http://arxiv.org/abs/2605.22462v1) | 因果特征分析 | 在IOI任务中，15个选择性特征仅解释31%激活方差，选择性比率与因果力负相关r=-0.56 | — | — | — |
| 12 | low | - | [Geometry-Adaptive Explainer for Faithful Dictionary-Based Interp...](http://arxiv.org/abs/2605.21849v1) | 机制可解释性 | 分布偏移会旋转模型主动使用的子空间，忠实性间隙的大小控制了分布外可解释忠实性的退化程度 | — | — | — |

## 方法族分布

- **机制可解释性**：2 篇
- **稀疏自编码器改进**：1 篇
- **基准可靠性验证**：1 篇
- **大模型越狱攻击**：1 篇
- **视觉机制可解释性**：1 篇
- **模型可解释性**：1 篇
- **VLA可解释性**：1 篇
- **可解释神经编码**：1 篇
- **稀疏特征审计**：1 篇
- **嵌入稀疏解耦**：1 篇
- **可解释推理分割**：1 篇
- **因果特征分析**：1 篇

## 代码资源

- [SegCompass: Exploring Interpretable Alignment with Sparse Autoencoders for Enhan...](https://github.com/ZhenyuLU-Heliodore/SegCompass.) · 6 stars
- [Event-Grounded Sparse Autoencoders for Vision-Language-Action Policies](https://github.com/xc-j/Event-SAE)

## 常见基线方法

- **基于Rademacher复杂度推导泛化界**：2 篇
- **普通稀疏自编码器**：1 篇
- **现有SAE改进变体**：1 篇
- **目标探针扰动TPP**：1 篇
- **伪相关去除SCR**：1 篇
- **k稀疏探测**：1 篇
- **top-K激活检索方法**：1 篇
- **带正则化的优化方法**：1 篇
- **线性基线稀疏自编码器**：1 篇
- **随机对照**：1 篇

## 常用数据集

- **摘要未提及**：2 篇
- **SAEBench**：1 篇
- **300条IOI任务提示语料**：1 篇
- **Bloom(2024)层8残差流SAE特征集**：1 篇
- **五个挑战性基准**：1 篇
- **IOI任务数据集**：1 篇
- **VUA数据集**：1 篇
- **LARDv2**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*