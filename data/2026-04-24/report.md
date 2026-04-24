# 🧪 ArXiv AI 日报

📅 **2026-04-24 周五** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **40,492** (¥0.0136)

## 🔥 今日必读

---

### 1. Tool Attention Is All You Need: Dynamic Tool Gating and Lazy Schema Loading for Eliminating the MCP/Tools Tax in Scalable Agentic Workflows

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.21816v1)

👤 Anuj Sadani, Deepak Kumar


**中文标题**: 工具注意力即一切：动态工具门控与懒Schema加载消除可扩展智能体工作流中的MCP/工具税

**背景与痛点**: 模型上下文协议（MCP）是当前大模型智能体对接外部工具的通用标准，但它要求每轮对话都注入全量工具的JSON Schema，带来每轮1万至6万token的额外开销即“工具税”，挤占有效上下文导致推理退化，还大幅提升运营成本，现有方案要么损失灵活性，要么需要重度重构，缺乏即插即用的解决方案。

**核心创新**: 将Transformer自注意力的动态选择思想从token层面拓展到工具层面，提出了中间件层的工具注意力（Tool Attention）机制，兼容现有MCP协议无需底层改造，通过动态语义匹配选工具加懒加载，既消除了工具税，还天然缩小了工具投毒攻击的暴露面，是模型无关的即插即用方案。

**技术细节**: 预计算所有工具的精简自然语言摘要和句嵌入，每轮对话计算当前查询嵌入与各工具摘要的余弦语义重叠分数；通过状态感知门控过滤不满足权限、前置状态要求的工具，选出分数最高的TopK工具；采用两阶段懒加载：所有工具精简摘要常驻上下文（可全局缓存），仅将选中TopK的完整JSON Schema注入上下文，额外增加后验幻觉门控，拒绝调用不在激活集的工具。

**实验结果**: 在基于真实部署数据校准的120工具六服务器模拟基准测试中，工具注意力实现了95%的每轮工具token削减，有效上下文利用率从24%提升至91%，投影得到任务成功率提升22个百分点，延迟降低52%，成本降低86%。

---

### 2. Thinking with Reasoning Skills: Fewer Tokens, More Accuracy

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.21764v1)

👤 Guangxiang Zhao, Qilong Shi, Xusen Xiao 等


**中文标题**: 带着推理技能思考：更少Token，更高准确率
**背景与痛点**: 当前主流推理大模型依靠生成长中间推理轨迹（如思维链）提升准确率，但冗余的试错探索会生成数千个思考Token，大幅推高推理成本与延迟。现有压缩方法仅强制缩短推理长度，仍要求模型从头推理，容易牺牲准确率，陷入效率-准确率两难。
**核心创新**: 提出从大量过往推理探索中蒸馏可复用推理技能，将昂贵的一次性探索和高效的在线推理解耦，在线推理时通过检索相关技能引导模型走正确求解路径，靠经验复用而非强制压缩减少冗余，打破效率-准确率 trade-off，且无需训练、兼容黑箱大模型API。
**技术细节**: 整体分两步实现：离线阶段，对源问题生成完整长推理轨迹，根据结果对错，用更强的总结模型蒸馏结构化技能卡——成功轨迹提炼通用求解模式，错误轨迹提炼避坑修正方法，每张卡包含触发、步骤、避坑、检查四个模块，提取关键词后存入索引；在线阶段，对新问题检索top-k相关技能注入prompt，要求模型仅用相关技能，限制单卡长度避免prompt膨胀。
**实验结果**: 在DeepMath数学数据集、NEMOTRON竞技编程数据集测试，对比各类高效推理基线，TRS可减少15%-59%的推理Token，降低最高53.8%的单请求成本，同时准确率维持或提升0-2.4个百分点，问题难度越高收益越显著，支持跨模型技能迁移。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [When Prompts Override Vision: Prompt-Induced Hallucinations in LVLMs](http://arxiv.org/abs/2604.21911v1) `cs.CV (计算机视觉)` | 揭示了大视觉语言模型中提示覆盖视觉输入、诱发幻觉的新问题，填补了LVLM幻觉来源研究的空白，对多模态安全很有意义 |
| 5 | [Transient Turn Injection: Exposing Stateless Multi-Turn Vulnerabilities in Large...](http://arxiv.org/abs/2604.21860v1) `cs.CR (加密与安全)` | 发现了无状态多轮LLM系统中一类未被关注的新对抗漏洞，提出瞬态轮注入攻击方法，对大模型安全防护有重要参考价值 |
| 6 | [Alignment has a Fantasia Problem](http://arxiv.org/abs/2604.21827v1) `cs.AI (人工智能)` | 指出现代大模型对齐存在的“幻想问题”：默认用户总能清晰表达需求，结合行为科学开辟了对齐领域新方向，启发性很强 |
| 7 | [MathDuels: Evaluating LLMs as Problem Posers and Solvers](http://arxiv.org/abs/2604.21916v1) `cs.CL (计算语言学)` | 针对前沿大模型在静态数学基准上接近天花板、无法区分能力的痛点，提出LLM同时当出题者与解题者的新评估框架，创新性很强 |
| 8 | [From Research Question to Scientific Workflow: Leveraging Agentic AI for Science...](http://arxiv.org/abs/2604.21910v1) `cs.AI (人工智能)` | 解决了现有科学工作流需要人工转译研究问题为可执行语义的痛点，提出用智能Agent实现全流程科学自动化，推进了AI for Science落地 |
| 9 | [Evaluation of Automatic Speech Recognition Using Generative Large Language Model...](http://arxiv.org/abs/2604.21928v1) `cs.CL (计算语言学)` | 解决了传统ASR评估指标WER对语义不敏感的痛点，提出用生成式大语言模型做ASR评估，和人类判断相关性更高，实用性很强 |
| 10 | [Why are all LLMs Obsessed with Japanese Culture? On the Hidden Cultural and Regi...](http://arxiv.org/abs/2604.21751v1) `cs.CL (计算语言学)` | 揭示了大模型中未被关注的隐藏文化偏见，发现现有LLM普遍存在过度偏向日本文化的偏差，对大模型文化对齐研究很有价值 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-24
