# representation-engineering — 2026-W17 (04/20-04/26)

本周新增 **62** 篇论文，**4** 篇附带代码。优先级：high 0 / medium 0 / low 62。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [Learning Uncertainty from Sequential Internal Dispersion in Larg...](http://arxiv.org/abs/2604.15741) | 大模型幻觉检测 | 大语言模型层间内部表示的离散程度可反映不确定性，SIVR性能稳定优于现有多个强基线方法 | — | — | ✅ |
| 2 | low | - | [Purging the Gray Zone: Latent-Geometric Denoising for Precise Kn...](http://arxiv.org/abs/2604.14324v1) | 未分类 | — | — | — | ✅ |
| 3 | low | - | [SinkTrack: Attention Sink based Context Anchoring for Large Lang...](http://arxiv.org/abs/2604.10027) | 大模型幻觉缓解 | SinkTrack在SQuAD2.0提升21.6%，在M3CoT提升22.8%，训练免费且推... | — | — | ✅ |
| 4 | low | - | [Trust-SSL: Additive-Residual Selective Invariance for Robust Aer...](http://arxiv.org/abs/2604.21349v1) | 未分类 | — | — | — | ✅ |
| 5 | low | - | [ART: Attention Replacement Technique to Improve Factuality in LL...](http://arxiv.org/abs/2604.06393) | 幻觉缓解 | 发现大语言模型的浅层主要依赖均匀注意力模式，该模式会因无法聚焦相关信息引发幻觉 | — | — | — |
| 6 | low | - | [ATLAS: Constitution-Conditioned Latent Geometry and Redistributi...](http://arxiv.org/abs/2604.17663) | 隐几何探测 | 宪法诱导隐几何可跨模型与基质复现，未适配Phi模型AUC达0.984，ALM8数据平均AUC... | — | — | — |
| 7 | low | - | [Activation Steering for Aligned Open-ended Generation without Sa...](http://arxiv.org/abs/2604.08169) | 激活引导对齐 | 三种激活引导方法均可恢复目标性状保留连贯性，StTP和StMP更能保持通用能力、减少多轮重复 | — | — | — |
| 8 | low | - | [Aligning Recommendations with User Popularity Preferences](http://arxiv.org/abs/2604.01036) | 流行度偏差校正 | SPREE可针对不同用户调整流行度引导的方向与幅度，多数据集验证其提升对齐性且保留推荐质量。 | — | — | — |
| 9 | low | - | [Arbitration Failure, Not Perceptual Blindness: How Vision-Langua...](http://arxiv.org/abs/2604.09364) | VLM可解释性 | 对错样本编码视觉证据强度相近，最终层logit间隙预测接地结果相关系数ρ=0.847，图像t... | — | — | — |
| 10 | low | - | [Are LLM Uncertainty and Correctness Encoded by the Same Features...](http://arxiv.org/abs/2604.19974) | 大模型可解释性 | 不确定性与正确性分属三类特征，抑制混杂特征提准1.1%降熵75%，3个特征预测正确性AURO... | — | — | — |
| 11 | low | - | [Attention at Rest Stays at Rest: Breaking Visual Inertia for Cog...](http://arxiv.org/abs/2604.01989) | 认知幻觉缓解 | MLLM解码早期确定的视觉注意力会保持惯性静态，无法动态支持关系推理，是认知幻觉的关键诱因 | — | — | — |
| 12 | low | - | [Auditing Support Strategies in LLMs through Grounded Multi-Turn ...](http://arxiv.org/abs/2604.17079v1) | 未分类 | — | — | — | — |

## 方法族分布

- **未分类**：20 篇
- **大模型幻觉缓解**：3 篇
- **大模型幻觉检测**：3 篇
- **大模型可解释性**：2 篇
- **大模型安全对齐**：2 篇
- **隐私保护个性化**：1 篇
- **大模型谄媚机制**：1 篇
- **接地推理**：1 篇
- **可控性漂移检测**：1 篇
- **引用幻觉定位**：1 篇
- **有害意图检测**：1 篇
- **隐几何探测**：1 篇

## 代码资源

- [SinkTrack: Attention Sink based Context Anchoring for Large Language Models](https://github.com/67L1/SinkTrack.) · 10 stars
- [Purging the Gray Zone: Latent-Geometric Denoising for Precise Knowledge Boundary...](https://github.com/Notbesidemoon/GeoDe.) · 1 stars
- [Trust-SSL: Additive-Residual Selective Invariance for Robust Aerial Self-Supervi...](https://github.com/WadiiBoulila/trust-ssl.)
- [Learning Uncertainty from Sequential Internal Dispersion in Large Language Model...](https://github.com/ponhvoan/internal-variance.)

## 常见基线方法

- **SimCLR**：1 篇
- **VICReg**：1 篇
- **通用转向（US）**：1 篇
- **表示工程（RepE）**：1 篇
- **现有激活引导方法**：1 篇
- **仅参数化方法**：1 篇
- **随机基线**：1 篇
- **标准自回归AR**：1 篇
- **提示式自校正**：1 篇
- **Best-of-16**：1 篇

## 常用数据集

- **MATH-500**：2 篇
- **TriviaQA**：2 篇
- **TruthfulQA**：2 篇
- **EuroSAT**：1 篇
- **AID**：1 篇
- **NWPU-RESISC45**：1 篇
- **BDD100K**：1 篇
- **整理后的有害查询集合**：1 篇
- **美国大陆2017-2023年1210万地球观测样本**：1 篇
- **120组分三个复杂度层级的环境查询样本**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*