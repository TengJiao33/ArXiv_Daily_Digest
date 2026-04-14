# 🧪 ArXiv AI 日报

📅 **2026-04-14 周二** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **62,567** (¥0.0203)

## 🔥 今日必读

---

### 1. ClawGuard: A Runtime Security Framework for Tool-Augmented LLM Agents Against Indirect Prompt Injection

🏷️ `cs.CR (加密与安全)` | 📄 [arXiv](http://arxiv.org/abs/2604.11790v1)

👤 Wei Zhao, Zhe Li, Peixin Zhang 等


**中文标题**: ClawGuard：面向工具增强大语言模型Agent的间接提示注入运行时安全框架

**背景与痛点**: 工具增强LLM Agent可自动化多步复杂真实任务，但存在三类间接提示注入风险：网页本地内容注入、MCP服务器注入、公开技能文件注入。现有三类防御都有缺陷：模型级对齐需微调仍可被绕过，协议级隔离需跨厂商协调，架构级防御要么限制灵活性要么需专家手动写规则，无法覆盖三类注入场景。

**核心创新**: 提出在工具调用边界做确定性权限管控的防御思路，通过在每一次工具调用执行前拦截检查，把依赖模型安全对齐的概率性防御转化为可审计的确定性防御。无需修改模型或现有Agent基础设施，可自动从用户任务目标推导访问约束，无需手动写规则，能覆盖三类主流注入渠道。

**技术细节**: 分为两个核心流程：1.预会话规则生成：在首次工具调用前，用Agent自身LLM从用户任务目标自动推导网络、文件、工具调用三类维度的任务规则，结合不可修改的系统级基线安全规则，经用户确认后激活生效。2.逐调用检查：每个待执行工具调用依次经过敏感数据打码、黑白名单权限校验、新技能首次风险核验、模糊结果人工审批四步，所有操作记入审计日志。

**实验结果**: 在AgentDojo、SkillInject、MCPSafeBench三个基准、五个主流大模型上测试，ClawGuard在AgentDojo实现100%防御成功率，将SkillInject和MCPSafeBench的攻击成功率降低50%-84%，同时几乎不影响合法任务的完成率，防御效果显著优于原生 baseline。

---

### 2. Agentic Aggregation for Parallel Scaling of Long-Horizon Agentic Tasks

🏷️ `cs.CL (计算语言学)` | 📄 [arXiv](http://arxiv.org/abs/2604.11753v1)

👤 Yoonsang Lee, Howard Yen, Xi Ye 等


**中文标题**: 面向长周期智能体任务并行缩放的智能聚合方法

**背景与痛点**: 长周期智能体任务（如深度搜索、深度研究）可通过并行生成多条独立轨迹提升性能，核心难点是如何高效聚合多条轨迹结果。现有方法要么仅聚合最终答案丢弃轨迹内中间证据，要么压缩轨迹产生不可逆信息损失，全量加载又会超出模型上下文窗口，成本也很高。

**核心创新**: 提出AggAgent智能聚合框架，将聚合任务本身建模为智能体交互任务，把已生成的多条并行轨迹当作可交互环境，通过轻量工具按需检索轨迹信息，既保留了轨迹的完整信息保真度，又解决了上下文溢出问题，实现了性能和成本的帕累托最优。

**技术细节**: AggAgent初始仅输入原始问题和各轨迹的元数据（步数、token数、工具统计），完整轨迹预存在环境中不预加载进上下文。它配备三个轻量内存工具：get_solution可获取指定或全部轨迹的最终答案，search_trajectory按关键词搜索指定轨迹的匹配步骤，get_segment读取指定范围的轨迹步骤。遵循从粗到细的工作流：先概览所有方案找到分歧点，再按需检索验证证据，最后合成输出结果，聚合总成本始终不超过单次智能体rollout。

**实验结果**: 在涵盖智能搜索、深度研究两类任务的6个基准测试3个主流模型，AggAgent相比最强基线平均绝对性能提升最高5.3%，深度研究任务提升达10.3%，仅增加5.7%的额外开销，远低于传统摘要聚合的41%。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [A Mechanistic Analysis of Looped Reasoning Language Models](http://arxiv.org/abs/2604.11791v1) `cs.LG (机器学习)` | 针对当下热门的隐层循环提升LLM推理性能的方案，完成了系统性机制分析，厘清了循环推理的工作逻辑，为后续推理优化提供核心支撑。 |
| 5 | [SWE-AGILE: A Software Agent Framework for Efficiently Managing Dynamic Reasoning...](http://arxiv.org/abs/2604.11716v1) 💻 `cs.AI (人工智能)` | 针对现有软件工程Agent缺乏深度系统2推理、难以处理复杂边缘场景的问题，提出了动态推理上下文管理框架，提升了代码Agent处理复杂任务的能力。 |
| 6 | [ClawGUI: A Unified Framework for Training, Evaluating, and Deploying GUI Agents](http://arxiv.org/abs/2604.11784v1) `cs.LG (机器学习)` | 针对当前GUI Agent领域训练、评估、部署流程碎片化的痛点，提出了统一的全流程框架，大幅降低了GUI Agent的开发落地门槛，实用性很高。 |
| 7 | [Why Do Large Language Models Generate Harmful Content?](http://arxiv.org/abs/2604.11663v1) `cs.AI (人工智能)` | 针对大语言模型生成有害内容的底层成因研究不充分的问题，提出基于因果中介分析的研究路径，为LLM安全对齐工作提供了更坚实的理论依据。 |
| 8 | [General365: Benchmarking General Reasoning in Large Language Models Across Diver...](http://arxiv.org/abs/2604.11778v1) `cs.CL (计算语言学)` | 针对现有LLM推理基准多偏向特定领域的不足，构建了覆盖多样化挑战性任务的通用推理基准，能更准确评估LLM的真实通用能力。 |
| 9 | [StarVLA-$α$: Reducing Complexity in Vision-Language-Action Systems](http://arxiv.org/abs/2604.11757v1) 💻 `cs.RO (机器人)` | 针对现有视觉语言动作（VLA）机器人系统复杂度高、生态碎片化的问题，提出了复杂度精简方案，推动了通用机器人Agent的轻量化落地。 |
| 10 | [C-ReD: A Comprehensive Chinese Benchmark for AI-Generated Text Detection Derived...](http://arxiv.org/abs/2604.11796v1) 💻 `cs.CL (计算语言学)` | 针对现有AI生成文本检测缺乏中文真实场景基准的空白，构建了源自真实Prompt的全面中文检测基准，适配中文场景AIGC风险管控需求，实用性强。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-14
