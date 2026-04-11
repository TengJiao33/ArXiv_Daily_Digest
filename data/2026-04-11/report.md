# 🧪 ArXiv AI 日报

📅 **2026-04-11 周六** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **44,029** (¥0.0147)

## 🔥 今日必读

---

### 1. Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models

🏷️ `cs.CV (计算机视觉)` | 📄 [arXiv](http://arxiv.org/abs/2604.08545v1)

👤 Shilin Yan, Jintao Tong, Hongwei Xue 等


**中文标题**: 明智行动：在智能体多模态模型中培养元认知工具使用能力
**背景与痛点**: 当前工具增强的智能体多模态模型普遍存在元认知缺陷，无法合理权衡内部知识和外部工具，频繁出现盲目工具调用，哪怕问题可通过自身能力直接解决。现有方法将准确率与工具效率合并为单一标量奖励训练，陷入两难：惩罚过重抑制必要调用，惩罚过轻效率信号被准确率方差淹没，无法解决过度调用问题。
**核心创新**: 针对奖励耦合的固有缺陷，提出分层解耦策略优化框架HDPO，摒弃传统奖励标量化，将任务准确率和工具效率拆为两个独立正交的优化通道，自然形成“先掌握任务正确性、再优化调用效率”的隐式认知课程，训练出具备元认知决策能力的智能体Metis。
**技术细节**: 算法上，HDPO维护两个独立通道：准确率通道对单prompt的所有采样轨迹，基于答案正确性和格式合规性计算奖励，按标准GRPO计算优势；效率通道仅对正确轨迹计算奖励，奖励随工具调用次数增加递减，仅在正确轨迹集合内计算优势，最终总损失为两个通道损失的加权和。训练前还做了多阶段数据清洗，仅保留真正需要工具的高质量样本。
**实验结果**: 在V*Bench、HRBench、MathVista、CharXiv等十余个主流多模态基准测试中，Metis将冗余工具调用率从98%降至2%，同时大幅提升推理准确率，多项指标超过现有开源同参数量甚至更大参数量的智能体模型，验证了方法的有效性。

---

### 2. Verify Before You Commit: Towards Faithful Reasoning in LLM Agents via Self-Auditing

🏷️ `cs.AI (人工智能)` | 📄 [arXiv](http://arxiv.org/abs/2604.08401v1)

👤 Wenhao Yuan, Chenchen Lin, Jian Chen 等


**中文标题**: 提交前先验证：通过自审计实现大语言模型智能体的可信推理
**背景与痛点**: LLM智能体将中间推理轨迹作为内部信念存储，用于指导后续决策，但看似连贯的推理常违反逻辑或证据约束，错误信念会累积传播引发系统性行为漂移。现有方法依赖多数共识将一致性等同于可信性，无法规避结构相关的重复错误，也仅做表面文本改写不定位具体违规。
**核心创新**: 提出自审计验证推理框架SAVER，在智能体提交动作、更新内存前就对内部信念做显式验证修复，不靠最终任务正确率或外部共识保证推理可信性，通过内生的审计修复机制从根源阻止错误信念在长周期智能体中传播。
**技术细节**: 首先通过不同推理人格生成多个结构各异的候选信念，再用融合质量评分与结构相似度的核，通过k确定性点过程采样选出待审计子集；之后对抗审计定位推理违规，将违规分为缺失假设、循环推理等六类；最后按约束引导做最小局部修复，迭代审计修复直到满足验证标准，最终选出违规最少的高质量信念执行。
**实验结果**: 在涵盖多跳问答、证据敏感问答、局部推理的六个公开基准，三个不同尺寸基座模型上验证，SAVER相比主流基线，推理无违规轨迹率提升一倍以上，不可信步骤占比下降超五成，同时保持了竞争性的端任务性能。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [SUPERNOVA: Eliciting General Reasoning in LLMs with Reinforcement Learning on Na...](http://arxiv.org/abs/2604.08477v1) `cs.AI (人工智能)` | 现有RLVR仅能提升大模型在数学、代码等形式域的推理能力，该工作将RL适配到自然指令，激发大模型通用推理能力，推进通用大模型发展。 |
| 5 | [What Drives Representation Steering? A Mechanistic Case Study on Steering Refusa...](http://arxiv.org/abs/2604.08524v1) `cs.LG (机器学习)` | 方向向量 steering 是当前高效大模型对齐的主流方法，但缺乏对其工作机制的可解释性研究，该工作从机理层面解析原理，填补研究空白。 |
| 6 | [PSI: Shared State as the Missing Layer for Coherent AI-Generated Instruments in ...](http://arxiv.org/abs/2604.08529v1) `cs.HC` | 当前自然生成的个人AI工具普遍互相孤立，无法协同工作，该工作提出PSI共享状态架构，解决生成式AI工具碎片化问题，助力个人Agent落地。 |
| 7 | [PIArena: A Platform for Prompt Injection Evaluation](http://arxiv.org/abs/2604.08499v1) 💻 `cs.CR (加密与安全)` | 提示注入是大模型应用的核心安全风险，但领域内一直缺乏统一完善的评估平台，该工作提出PIArena统一评估基准，实用性强，填补领域空白。 |
| 8 | [Cram Less to Fit More: Training Data Pruning Improves Memorization of Facts](http://arxiv.org/abs/2604.08519v1) `cs.CL (计算语言学)` | 大模型普遍存在事实记忆不足引发幻觉的问题，该工作发现训练数据剪枝反而能提升模型事实记忆能力，结论反常识，兼具创新性和实用性。 |
| 9 | [Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models ...](http://arxiv.org/abs/2604.08476v1) `cs.CV (计算机视觉)` | 当前多模态大模型用GRPO训练后，常出现准确率提升但推理不忠实的问题，该工作提出约束策略优化改进GRPO，提升视觉推理可靠性。 |
| 10 | [KV Cache Offloading for Context-Intensive Tasks](http://arxiv.org/abs/2604.08426v1) `cs.LG (机器学习)` | 长上下文大模型应用中，KV缓存是内存和延迟的核心瓶颈，该工作优化KV缓存卸载方案，缓解长上下文任务的资源压力，工业落地价值高。 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-11
