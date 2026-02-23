# 🧪 ArXiv AI 日报

📅 **2026-02-23 周一** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **44,347** (¥0.0152)

## 🔥 今日必读

---

### 1. The Geometry of Noise: Why Diffusion Models Don't Need Noise Conditioning

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2602.18428v1)

👤 Mojtaba Sahraee-Ardakan, Mauricio Delbracio, Peyman Milanfar


**中文标题**: 噪声的几何：为什么扩散模型不需要噪声条件化

**背景与痛点**: 现有主流扩散生成模型都依赖显式的噪声水平（时间步）条件输入，近年新兴的噪声无关自治生成模型，仅用一个与时间无关的静态向量场就能生成高质量样本，但该范式一直存在核心悖论：为什么有界的静态网络能在梯度本应发散的数据流形附近保持稳定？现有工作未从根本上解决该疑问，也无法解释不同盲扩散模型的性能差异。

**核心创新**: 本文从几何角度对噪声无关自治扩散给出了严谨的统一理论框架，将其隐式优化目标定义为对所有噪声水平积分得到的边际能量，证明自治生成本质是边际能量上的黎曼梯度流，揭示静态向量场会隐式引入局部共形度量抵消梯度奇异性，同时推导了自治采样的结构稳定性条件。

**技术细节**: 首先推导得最优噪声无关向量场，是所有噪声水平下最优条件场按噪声后验概率加权得到的期望，再将其分解为天然梯度、传输校正、线性漂移三个可解释的几何分量。在高维全局、近数据流形局部两种场景下，噪声后验都会坍缩，传输校正项消失，有效增益会以恰好抵消梯度发散的速度趋近于零，保证向量场有界，最终推导得到不同参数化的稳定性条件。

**实验结果**: 在CIFAR-10、SVHN、Fashion MNIST以及可控高维玩具数据集上验证，结果完全符合理论预测：去掉噪声条件的DDPM噪声预测模型生成充满噪声的无效样本；去掉噪声条件的速度参数化模型生成质量与带显式条件的基线相当，CIFAR-10上FID可低至2.23。

---

### 2. Thinking by Subtraction: Confidence-Driven Contrastive Decoding for LLM Reasoning

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2602.18232v1)

👤 Lexiang Tang, Weihao Gao, Bingchen Zhao 等


**中文标题**: 减法式思考：面向大语言模型推理的置信度驱动对比解码

**背景与痛点**: 现有大模型推理的测试时扩展方法大多均匀增加全解码过程的计算量，要么生成多条推理轨迹，要么全局应用对比解码，普遍算力开销大、冗余推理多。推理不确定性实际高度局部化，仅少数低置信度token会引发绝大多数错误，全局修正会稀释干预效果，也造成计算浪费。

**核心创新**: 本文提出置信度驱动对比解码（CCD），核心是只在推理过程中识别出的低置信度关键位置做针对性修正，不对高置信度的稳定推理步骤做多余干预，无需额外训练、也不需要生成多条推理轨迹，仅引入极小的KV缓存开销，是传统全局测试时缩放方案的高效替代。

**技术细节**: 解码时首先在线计算每个生成token的预测置信度，通过滑动窗口统计最近置信度分布，用分位数阈值动态划分低置信度待干预token和高置信度语义锚点；维护双KV缓存，主缓存保存正常上下文，对比缓存将高置信度锚点替换为无语义占位符，构造故意混淆的参考分布；仅在低置信度位置触发对比修正，最终预测logits为原分布加权后减去混淆参考分布加权，放大正确token概率优势。

**实验结果**: 在AIME2024/2025、BRUMO2025、HMMT2025四个高难度数学推理基准测试，覆盖1.5B到32B不同规模的稠密、MoE大模型，相比原生解码，CCD稳定提升3-5个百分点的准确率，同时能压缩冗余推理，输出更简洁，超参数鲁棒性好。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [SPQ: An Ensemble Technique for Large Language Model Compression](http://arxiv.org/abs/2602.18420v1) 💻 `cs.CL (计算语言学)` | 提出结合保留方差SVD、剪枝、量化的集成LLM压缩方法SPQ，兼顾压缩率和模型性能，有效降低大模型部署成本，工业实用价值高。 |
| 5 | [RVR: Retrieve-Verify-Retrieve for Comprehensive Question Answering](http://arxiv.org/abs/2602.18425v1) `cs.CL (计算语言学)` | 针对开放域问答需要覆盖多维度答案信息的痛点，提出多轮检索框架RVR，通过检索-验证-再检索提升召回全面性，改进RAG问答效果。 |
| 6 | [Analyzing and Improving Chain-of-Thought Monitorability Through Information Theo...](http://arxiv.org/abs/2602.18297v1) `cs.LG (机器学习)` | 针对CoT推理难以监控异常输出（如代码生成测试黑客行为）的问题，基于信息论分析并改进CoT可监控性，提升LLM输出可靠性。 |
| 7 | [Decoding as Optimisation on the Probability Simplex: From Top-K to Top-P (Nucleu...](http://arxiv.org/abs/2602.18292v1) `cs.LG (机器学习)` | 针对当前LLM解码被当作启发式调参的现状，提出将解码统一为概率单纯形上的优化框架，统一了主流采样方法，有基础理论价值。 |
| 8 | [On the Adversarial Robustness of Discrete Image Tokenizers](http://arxiv.org/abs/2602.18252v1) `cs.CV (计算机视觉)` | 离散图像分词器是当前多模态大模型核心组件，本文系统分析其对抗鲁棒性，填补领域研究空白，对多模态系统安全设计有指导意义。 |
| 9 | [A Probabilistic Framework for LLM-Based Model Discovery](http://arxiv.org/abs/2602.18266v1) `cs.LG (机器学习)` | 提出基于LLM的自动化科学模型发现概率框架，结合Agent范式从观测数据挖掘可解释机械模型，有望加速科学发现，前沿性突出。 |
| 10 | [PRISM-FCP: Byzantine-Resilient Federated Conformal Prediction via Partial Sharin...](http://arxiv.org/abs/2602.18396v1) `cs.LG (机器学习)` | 针对联邦学习中拜占庭攻击导致 conformal预测校准失效的痛点，提出基于部分共享的鲁棒框架，提升分布式预测的可靠性与安全性。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-02-23
