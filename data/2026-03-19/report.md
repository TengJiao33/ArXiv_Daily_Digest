# 🧪 ArXiv AI 日报

📅 **2026-03-19 周四** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **30,006** (¥0.0106)

## 🔥 今日必读

---

### 1. AgentFactory: A Self-Evolving Framework Through Executable Subagent Accumulation and Reuse

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2603.18000v1) | 💻 [GitHub](https://github.com/zzatpku/AgentFactory) ⭐6

👤 Zhang Zhang, Shuqi Lu, Hongjin Qian 等


**中文标题**: AgentFactory：通过可执行子智能体积累与复用实现自进化的框架
**背景与痛点**: 当前基于大语言模型的自进化智能体多将成功经验存储为文本提示、反思或推理轨迹，无法在复杂场景下保证任务重执行的可靠性；现有代码级自进化方法仅面向高度专业化的科学任务，不支持通用日常任务的能力积累。
**核心创新**: 提出Install→Self-Evolve→Deploy三阶段自进化范式，核心是将成功任务解决方案存储为可执行的标准化Python子智能体而非文本经验，支持持续自主优化与跨系统导出复用，兼顾通用性和复用效率。
**技术细节**: 架构分为三部分：元智能体编排器负责任务分解与子智能体生命周期管理；三级技能系统包含固定元编排技能、内置基础工具技能、动态进化的子智能体技能；工作区管理器提供隔离执行环境，避免修改失败破坏共享库。三阶段分别完成从零构建存储子智能体、基于执行反馈迭代优化子智能体代码、导出带标准化文档的独立可复用模块。
**实验结果**: 在两批共30个覆盖网页检索、自动化、数据处理等领域的真实任务上测试，对比ReAct从零解决、文本经验自进化两种基线，AgentFactory复用累积子智能体后，编排任务的平均输出token消耗比基线降低40%~60%，强能力大模型在初始任务阶段即可获得明显的复用收益。

---

### 2. TDAD: Test-Driven Agentic Development - Reducing Code Regressions in AI Coding Agents via Graph-Based Impact Analysis

🏷️ `cs.SE (软件工程)` | 📄 [arXiv](http://arxiv.org/abs/2603.17973v1) | 💻 [GitHub](https://github.com/pepealonso95/TDAD.) ⭐0

👤 Pepe Alonso


**中文标题**: TDAD：测试驱动智能体开发——基于图影响力分析降低AI编码智能体的代码回归
**背景与痛点**: 当前AI编码智能体的评估和优化几乎只关注问题解决率，严重忽略代码回归（原本通过的测试被补丁破坏）问题；现有方案要么全量跑测试成本太高无法规模化，要么仅匹配邻近文件会漏间接依赖，纯TDD流程提示反而会让中小模型产生更多回归，带回归的补丁实际中几乎都会被拒绝合入。
**核心创新**: 将经典软件工程的测试影响力分析适配AI编码智能体场景，核心洞察是给智能体提供上下文（哪些测试可能受影响），远好于给它详细的流程指令（如何做TDD）；推出了开源零依赖工具，呼吁社区将回归率作为和解决率同等重要的第一类评估指标。
**技术细节**: 分两阶段 pipeline，第一阶段索引：基于Python标准AST解析代码库，构建含文件/函数/类/测试四类节点的代码-测试依赖图，通过命名匹配、前缀匹配、目录邻近度三级策略建立测试到被测代码的关联；第二阶段对直接关联、传递调用、文件依赖、导入关联四种路径加权打分，筛选最高风险的至多50个测试，导出为可grep的静态测试表，技能提示仅20行，pip安装零额外依赖。
**实验结果**: 在SWE-bench Verified基准测试，100个实例上Qwen3-Coder 30B将测试级回归率从6.08%降至1.82%，降幅达70%；集成到OpenCode Agent搭配Qwen3.5-35B后，问题解决率从24%提升至32%，验证了「上下文优于流程」的核心结论。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [CARE: Covariance-Aware and Rank-Enhanced Decomposition for Enabling Multi-Head L...](http://arxiv.org/abs/2603.17946v1) `cs.LG (机器学习)` | 针对大模型KV缓存开销大的痛点，提出协方差感知秩增强分解，可将预训练GQA转换为MLA，不增加KV缓存成本同时提升模型表达能力。 |
| 5 | [Efficient Training-Free Multi-Token Prediction via Embedding-Space Probing](http://arxiv.org/abs/2603.17942v1) `cs.CL (计算语言学)` | 挖掘LLM本身隐含的多token预测能力，提出简单无训练的多token预测方案，无需改动模型就能提升推理速度，落地成本极低。 |
| 6 | [Loc3R-VLM: Language-based Localization and 3D Reasoning with Vision-Language Mod...](http://arxiv.org/abs/2603.18002v1) `cs.CV (计算机视觉)` | 针对现有多模态大模型空间理解、视点感知推理能力不足的问题，提出面向语言驱动定位和3D推理的VLM，推动3D多模态落地。 |
| 7 | [Mitigating LLM Hallucinations through Domain-Grounded Tiered Retrieval](http://arxiv.org/abs/2603.17872v1) `cs.CL (计算语言学)` | 针对大语言模型领域场景幻觉问题，提出基于领域锚定的分层检索方案，有效缓解幻觉，提升RAG系统落地效果，实用性强。 |
| 8 | [Process Supervision for Chain-of-Thought Reasoning via Monte Carlo Net Informati...](http://arxiv.org/abs/2603.17815v1) `cs.CL (计算语言学)` | 针对思维链推理中中间错误传播的问题，提出基于蒙特卡洛网络信息增益的过程监督方法，有效提升大模型多步推理的准确率。 |
| 9 | [RAMP: Reinforcement Adaptive Mixed Precision Quantization for Efficient On Devic...](http://arxiv.org/abs/2603.17891v1) `cs.LG (机器学习)` | 针对端侧LLM量化现有方法统一比特宽效果差的痛点，提出强化学习自适应混合精度量化，提升端侧大模型推理精度与效率，落地价值高。 |
| 10 | [VideoAtlas: Navigating Long-Form Video in Logarithmic Compute](http://arxiv.org/abs/2603.17948v1) `cs.CV (计算机视觉)` | 针对长视频输入多模态模型计算复杂度高、表示损失大的问题，提出对数复杂度的长视频处理方案，大幅提升长视频LLM的处理效率。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-03-19
