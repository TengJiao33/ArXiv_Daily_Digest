# 🧪 ArXiv AI 日报

📅 **2026-04-06 周一** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **38,542** (¥0.0130)

## 🔥 今日必读

---

### 1. The Compression Gap: Why Discrete Tokenization Limits Vision-Language-Action Model Scaling

🏷️ `cs.RO (机器人)` | 📄 [arXiv](http://arxiv.org/abs/2604.03191v1)

👤 Takuya Shiba


**中文标题**: 压缩缺口：为什么离散分词会限制视觉-语言-动作模型缩放

**背景与痛点**: 当前视觉-语言-动作（VLA）模型普遍默认升级上游高质量视觉编码器就能提升机器人下游操作性能，该规律在视觉语言预训练中已被验证，但现有研究从未系统分析不同动作表示对编码器升级收益的影响，实践中常出现编码器升级后性能不涨的异常。

**核心创新**: 本文从信息论角度提出「压缩缺口」核心原理：visuomotor流水线的最终性能由整条链路中最紧的信息瓶颈决定，离散动作分词引入的固定容量码本会成为绑定瓶颈，阻挡上游编码器升级的收益向下游传播，而连续动作表示不存在该硬瓶颈。

**技术细节**: 本文基于数据处理不等式推导理论结论，设计严格控制变量的对照实验：核心为三因子全因子实验，变量为动作表示（离散OAT/连续Diffusion Policy）、视觉编码器质量、模型大小；额外补充两类验证实验：多梯度编码器质量测试、离散码本容量消融，所有实验共享同一代码框架，排除架构差异干扰。

**实验结果**: 在LIBERO-10机器人操作基准上测试，升级编码器后连续Diffusion Policy成功率提升21-26个百分点，离散OAT仅提升3.6-10.4个百分点，扩大码本容量可部分恢复对编码器升级的敏感度，验证了压缩缺口假设。

---

### 2. Supply-Chain Poisoning Attacks Against LLM Coding Agent Skill Ecosystems

🏷️ `cs.CR (加密与安全)` | 📄 [arXiv](http://arxiv.org/abs/2604.03081v1)

👤 Yubin Qu, Yi Liu, Tongcheng Geng 等


**中文标题**: 《针对大语言模型编码智能体技能生态的供应链投毒攻击》

**背景与痛点**: 基于大语言模型的编码智能体普遍通过开放市场的第三方技能扩展能力，无强制安全审核，投毒后可直接获得系统级执行权限。此前研究仅涉及工具选择劫持或RAG文本污染，未验证投毒能否绕过现有对齐、架构防护，直接劫持智能体的系统级动作空间。

**核心创新**: 提出文档驱动隐式载荷执行（DDIPE）攻击方法，利用编码智能体将技能文档的代码示例、配置模板视为权威参考，会复现到生成代码中执行的特性，将恶意逻辑伪装成合法文档内容，无需显式恶意指令即可绕过防护，实现静默动作空间劫持，还支持规模化自动生成投毒技能。

**技术细节**: DDIPE采用两种恶意载荷嵌入方式：一是将恶意逻辑插入技能文档的合法代码块，二是将后门植入部署配置模板。搭配三类伪装：把数据盗窃包装成合规遥测、用异常捕获静默隐藏错误、将控制端地址伪装成内部服务地址。攻击生成采用LLM驱动的种子-变异-验证流水线，从81个手工种子扩展生成1070个恶意技能，覆盖15类MITRE ATT&CK攻击，通过逆权重抽样保证长尾攻击覆盖。

**实验结果**: 在4款主流编码智能体框架、5款主流大模型上测试，DDIPE绕过率达11.6%-33.5%，显式指令注入基线通过率为0%。静态分析仅能拦截90.7%的攻击，仍有2.5%可同时绕过静态检测和安全对齐，已向厂商确认4个真实漏洞，2个完成官方修复。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Detecting and Correcting Reference Hallucinations in Commercial LLMs and Deep Re...](http://arxiv.org/abs/2604.03173v1) `cs.CL (计算语言学)` | 针对大模型和深度研究Agent普遍存在的引用幻觉问题，首次系统测量了其引用可靠性，提出可行的检测修正方案，解决了科研Agent落地核心痛点 |
| 5 | [Co-Evolution of Policy and Internal Reward for Language Agents](http://arxiv.org/abs/2604.03098v1) `cs.LG (机器学习)` | 针对大语言模型Agent长时序训练中奖励稀疏延迟的核心瓶颈，提出策略与内在奖励共同演化的方案，为长任务Agent训练提供了新思路 |
| 6 | [Understanding the Role of Hallucination in Reinforcement Post-Training of Multim...](http://arxiv.org/abs/2604.03179v1) `cs.LG (机器学习)` | 首次系统分析多模态大模型RL后训练阶段幻觉的作用机制，纠正了业界对幻觉全负面的认知，为优化多模态推理训练提供了新方向 |
| 7 | [Automatic Textbook Formalization](http://arxiv.org/abs/2604.03071v1) `cs.AI (人工智能)` | 实现了超500页研究生级代数组合教材自动形式化到Lean定理证明器，是AI自动数学形式化的新里程碑，推进了AI辅助数学研究落地 |
| 8 | [Gradient Boosting within a Single Attention Layer](http://arxiv.org/abs/2604.03190v1) `cs.LG (机器学习)` | 针对Transformer注意力无法修正自身误差的固有缺陷，提出梯度提升注意力机制，将梯度提升思想融入单注意力层，为Transformer结构改进提供新方向 |
| 9 | [Can VLMs Truly Forget? Benchmarking Training-Free Visual Concept Unlearning](http://arxiv.org/abs/2604.03114v1) `cs.CV (计算机视觉)` | 针对多模态大模型视觉概念合规去学习的需求，构建首个免训练视觉概念去学习的评测基准，揭露了现有方法的结构缺陷，指导后续技术优化 |
| 10 | [Credential Leakage in LLM Agent Skills: A Large-Scale Empirical Study](http://arxiv.org/abs/2604.03070v1) `cs.CR (加密与安全)` | 完成首个针对LLM Agent第三方技能中凭证泄露风险的大规模实证研究，量化了该风险的普遍程度，为Agent技能安全开发审核提供重要依据 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-06
