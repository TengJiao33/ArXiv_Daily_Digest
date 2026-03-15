# 🧪 ArXiv AI 日报

📅 **2026-03-15 周日** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **43,174** (¥0.0145)

## 🔥 今日必读

---

### 1. IsoCompute Playbook: Optimally Scaling Sampling Compute for LLM RL

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.12151v1)

👤 Zhoujun Cheng, Yutao Xie, Yuxiao Qu 等


**中文标题**: IsoCompute手册：大语言模型RL训练的采样计算最优缩放

**背景与痛点**: 当前预训练已有成熟的缩放定律指导计算分配，但大语言模型的RL后训练领域，从业者拿到固定计算预算后，缺乏明确的分配规则指导：不知道该把计算分配给更多每问题并行采样、更多每批问题还是更多训练迭代，现有研究仅关注单维度缩放，未给出实用的最优分配处方。

**核心创新**: 该研究首次在固定总计算预算下，对三个核心采样维度（每问题并行采样数、每批问题数、训练更新步数）系统开展最优分配实验，基于累计12万小时H200的大规模实验，提炼出可落地的实践调参规则，填补了LLM RL领域计算最优缩放的研究空白。

**技术细节**: 研究将总采样计算表示为三个维度的乘积，先构建适配任务难度的稳定训练配方：简单任务启用KL和熵正则避免训练早停，难任务禁用正则避免训练发散，学习率按总批量大小的平方根缩放。通过网格搜索提取不同预算下的性能最优前沿，发现最优每问题并行采样数随总计算增加上升后饱和，增大并行采样可缓解多问题间的梯度干扰，简单任务中增益来自输出鲁棒性提升，难任务中增益来自正确解覆盖范围扩大。

**实验结果**: 在Guru-Math数学推理数据集上划分难易子集验证，规律在Qwen、Llama系列三个主流基座模型，GRPO、PPO等多种RL算法，分布内和分布外任务上均一致成立，提炼的分配规则可直接指导实际RL调参。

---

### 2. Security Considerations for Artificial Intelligence Agents

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2603.12230v1)

👤 Ninghui Li, Kaiyuan Zhang, Kyle Polley 等


**中文标题**: 人工智能代理的安全考量

**背景与痛点**: 当前大语言模型驱动的通用AI代理已进入规模化商用阶段，但这类架构天生模糊了代码与数据边界，支持动态生成工作流，原有面向确定性软件的传统安全机制存在根本性适配缺陷，行业缺乏针对AI代理尤其是多代理系统的系统性安全梳理和标准化指引。

**核心创新**: 本文结合Perplexity运营千万级用户通用代理系统的一线经验，系统性梳理了AI代理区别于传统软件的独特安全属性，拆解了全栈攻击面，提出适配AI代理特性的纵深防御架构，明确了当前研究缺口和标准化方向，填补了行业系统性安全梳理的空白。

**技术细节**: 首先点明AI代理的三大核心安全差异：彻底模糊代码与数据边界，不可控第三方数据可直接决定代理控制流；支持动态生成非确定性工作流，权限范围广且行为难审计；原有安全机制的人工决策假设失效。本文拆解了工具调用、多代理协调、部署托管全链路攻击面，点明间接提示注入、多代理困惑副署、长工作流级联失效三大核心风险，提出输入检测-模型加固-系统沙箱+确定性权限控制的三层纵深防御架构，明确要求必须保留确定性强制防护层作为最后防线。

**实验结果**: 本文为面向NIST标准制定的行业经验梳理，无公开专项测试实验，核心结论来自千万级用户生产运营实践：当前输入检测误报率高、模型层防护不可靠，生产环境最可靠的是确定性工具白名单和权限边界控制，亟需行业统一标准和适配代理的新型安全研究。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [TopoBench: Benchmarking LLMs on Hard Topological Reasoning](http://arxiv.org/abs/2603.12133v1) `cs.AI (人工智能)` | 拓扑网格推理需要全局空间不变性推理，当前最强LLM也难以很好解决，本文推出全新的难拓扑推理评测基准，推动LLM复杂推理能力研究。 |
| 5 | [SciMDR: Benchmarking and Advancing Scientific Multimodal Document Reasoning](http://arxiv.org/abs/2603.12249v1) `cs.CL (计算语言学)` | 科学多模态文档推理数据集构建长期存在规模、真实性、 realism的三角权衡，本文推出新基准SciMDR，推动科学多模态大模型技术发展。 |
| 6 | [Cross-Context Review: Improving LLM Output Quality by Separating Production and ...](http://arxiv.org/abs/2603.12123v1) `cs.CL (计算语言学)` | LLM在同生成会话中很难自我检查输出错误，本文提出简单有效的跨上下文审查方案，无需额外训练就能提升输出质量，工业落地成本极低。 |
| 7 | [EndoCoT: Scaling Endogenous Chain-of-Thought Reasoning in Diffusion Models](http://arxiv.org/abs/2603.12252v1) `cs.CV (计算机视觉)` | 当前扩散模型大多仅把MLLM作为外部文本编码器，本文提出将思维链推理内生化到扩散模型中，可扩展复杂空间推理能力，创新思路清晰。 |
| 8 | [IndexCache: Accelerating Sparse Attention via Cross-Layer Index Reuse](http://arxiv.org/abs/2603.12201v1) `cs.CL (计算语言学)` | 长上下文Agent工作流对注意力效率要求很高，本文提出通过跨层索引复用加速稀疏注意力，能有效降低推理成本，助力长上下文Agent落地。 |
| 9 | [Neural Thickets: Diverse Task Experts Are Dense Around Pretrained Weights](http://arxiv.org/abs/2603.12228v1) `cs.LG (机器学习)` | 本文提出新观点：预训练权重周围密集分布着适配不同任务的专家子网络，为低成本高效微调预训练模型提供了全新研究思路。 |
| 10 | [LifeSim: Long-Horizon User Life Simulator for Personalized Assistant Evaluation](http://arxiv.org/abs/2603.12152v1) `cs.CL (计算语言学)` | 当前个性化AI助手的评测基准普遍不贴合真实长周期场景，本文推出长范围用户生活模拟器，解决了评测错位痛点，推动助手技术发展。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-15
