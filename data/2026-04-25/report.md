# 🧪 ArXiv AI 日报

📅 **2026-04-25 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **40,246** (¥0.0135)

## 🔥 今日必读

---

### 1. Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.21816v1) | 💻 [GitHub](https://github.com/asadani/tool-attention) ⭐1

👤 Anuj Sadani, Deepak Kumar


**中文标题**: 工具注意力即一切：面向可扩展智能体工作流消除MCP/工具税的动态工具门控与懒Schema加载

**背景与痛点**: MCP是当前LLM智能体对接外部工具的通用标准，但其要求每轮对话全量注入所有工具的完整JSON Schema，产生了单轮最高数万token的「工具税」，既挤占有效推理上下文、降低推理质量，又推高成本、扩大工具投毒攻击面，现有方案要么牺牲灵活性要么需要大规模重构。

**核心创新**: 将Transformer自注意力动态选择相关信息的思路推广到工具层，提出了中间件层的工具注意力机制，仅为每轮对话动态加载匹配当前用户意图的少量工具完整Schema，原生兼容现有MCP协议，无需改动底层模型或协议，兼顾效率、灵活性与安全性。

**技术细节**: 具体实现分为三步：1 预生成所有工具的精简短摘要，用公开 sentence 编码器生成嵌入；2 每轮计算用户查询与工具摘要的余弦相似度（即意图-Schema重叠得分），再通过状态感知门控过滤不满足权限、流程前置条件的工具，选出得分最高的Top K候选；3 采用两阶段懒加载：所有工具短摘要常驻上下文（可全量缓存），仅将Top K的完整Schema注入当前prompt，额外增加后置门控拦截模型对非激活工具的错误调用。

**实验结果**: 在匹配真实生产部署的120工具、六服务器模拟基准测试中，直接测得工具token每轮降低95%（从47.3k降至2.4k），有效上下文利用率从24%提升至91%，结合公开部署数据推算，任务成功率提升22个百分点，延迟降低52%，成本降低86%。

---

### 2. Thinking with Reasoning Skills: Fewer Tokens, More Accuracy

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.21764v1)

👤 Guangxiang Zhao, Qilong Shi, Xusen Xiao 等


**中文标题**: 《用推理技能思考：更少Token，更高准确率》

**背景与痛点**: 当前主流推理大模型依靠长中间思考链提升复杂推理准确率，导致推理Token量极大，推高了推理成本与延迟。现有高效推理方法多通过硬约束压缩推理长度，强迫模型缩短思考过程，容易跳过关键步骤，在复杂问题上陷入效率-准确率此消彼长的矛盾，无法兼顾两者。

**核心创新**: 提出TRS框架，将推理范式从「每次从零开始推理」改为「复用蒸馏好的通用推理技能」，把昂贵的探索过程一次性离线完成，在线推理靠检索经验减少冗余试错，打破了效率和准确率的固有trade-off，且无需训练、兼容黑盒大模型API，部署灵活。

**技术细节**: 分为离线建库和在线推理两步：离线阶段，先让推理模型对源问题生成完整推理轨迹，再用更强的摘要模型把长轨迹蒸馏为结构化技能卡，成功轨迹提取可复用的解题模式，失败轨迹提取错误模式和避错方案，每个技能卡带触发关键词构建检索索引。在线阶段，对新问题检索top-k相关技能卡注入prompt，提示模型只使用相关技能，限制技能卡总长度避免prompt膨胀，数学默认用BM25检索，代码默认用混合检索。

**实验结果**: 在DeepMath数学推理、Nemotron编程竞赛基准测试，对比标准CoT、CoD、TALE等基线，TRS可降低15%-59%的推理Token与成本，同时准确率持平或提升0.2-4.1个百分点，问题难度越高收益越显著，蒸馏的技能可跨模型迁移适配不同场景。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](http://arxiv.org/abs/2604.21911v1) `cs.CV (计算机视觉)` | 揭示了大视觉语言模型中prompt覆盖视觉输入引发的新型幻觉问题，深化了对多模态大模型幻觉成因的理解，对LVLM对齐有重要参考价值。 |
| 5 | [Low-Rank Adaptation Redux for Large Models](http://arxiv.org/abs/2604.21905v1) `cs.LG (机器学习)` | 对当前大模型参数高效微调的标准方案LoRA重新梳理优化，针对现有LoRA的不足提出改进，对工业界大模型微调实践有很高实用价值。 |
| 6 | [Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large...](http://arxiv.org/abs/2604.21860v1) `cs.CR (加密与安全)` | 发现了大语言模型无状态多轮对话场景下的新型安全漏洞瞬态轮注入，揭示了未被关注的安全风险，对LLM安全防御研究有重要意义。 |
| 7 | [Alignment has a Fantasia Problem](http://arxiv.org/abs/2604.21827v1) `cs.AI (人工智能)` | 指出现代对齐的核心隐含缺陷：默认用户能清晰表达目标，提出对齐存在「幻想问题」，开辟了对齐研究的新方向，洞见非常深刻。 |
| 8 | [MathDuels: Evaluating LLMs as Problem Posers and Solvers](http://arxiv.org/abs/2604.21916v1) `cs.CL (计算语言学)` | 解决了当前前沿大模型在静态数学基准接近天花板、无法区分能力的问题，提出LLM同时作为出题者和解题者的全新评估范式。 |
| 9 | [From Research Question to Scientific Workflow: Leveraging Agentic AI for Science...](http://arxiv.org/abs/2604.21910v1) `cs.AI (人工智能)` | 解决了科学工作流生成中需要手动将研究问题转换为语义流程的痛点，用智能体AI实现全流程自动化，推动AI for Science落地。 |
| 10 | [Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regi...](http://arxiv.org/abs/2604.21751v1) `cs.CL (计算语言学)` | 发现现有大语言模型普遍存在隐藏文化偏差：过度偏向日本文化，补充了LLM文化偏见研究的新发现，对大模型公平对齐有重要价值。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-25
