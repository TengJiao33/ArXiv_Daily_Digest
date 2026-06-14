# Agent 策略优化与在线蒸馏 — 2026-W24 (06/08-06/14)

本周新增 **86** 篇论文，**7** 篇附带代码。优先级：high 37 / medium 33 / low 16。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 控制/评测 | 风险 | Idea Hook | 代码 |
|:-:|:------:|:-----:|------|--------|----------|------|-----------|:----:|
| 1 | high | - | [3SPO: State-Score-Supervised Policy Optimization for LLM Agents](http://arxiv.org/abs/2606.09961v1) | policy optimization | 通过每步基于历史成功率生成的状态分数做监督，实现步级策略优化，改进信用分配，提升... | 仅在两个中小规模基准验证，未验证大规模复杂长周期任务的泛化效果。 | 能否将这种步级状态分数监督思路引入在线策略蒸馏，提升稀疏奖励场景下智能体后训练效率？ | ✅ |
| 2 | high | - | [Pushing the Limits of LLM Tool Calling via Experiential Knowledg...](http://arxiv.org/abs/2606.10875v1) | tool-use control | 通过整合经验知识，推理阶段并行采样扩展推理宽度激活知识，训练阶段用知识增强数据做... | 仅在两个公开基准验证效果，未验证真实场景泛化性，摘要未披露详细消... | 探索将本文经验知识整合激活思路结合到Agent在线策略蒸馏中，优化工具调用场景的策略性能。 | ✅ |
| 3 | high | - | [Trajectory-Refined Distillation](http://arxiv.org/abs/2606.08432v1) | online distillation | 通过教师引导在蒸馏前修正学生模型生成的错误前缀，从轨迹层面干预，缓解原有蒸馏的梯... | 未在具体下游agent任务验证，方法通用性有待验证，未披露详细的... | 可将该轨迹修正蒸馏思路迁移到agent在线策略蒸馏中，解决agent rollout过程的前... | ✅ |
| 4 | high | - | [APPO: Agentic Procedural Policy Optimization](http://arxiv.org/abs/2606.12384v1) | policy optimization | 通过将分支与信用分配转移到细粒度决策点，设计分支分数筛选有效分支点，结合程序级优... | 未披露具体基准细节与工程实现细节，结果的可复现性存在一定不确定性... | 能否将APPO的细粒度信用分配思路结合在线蒸馏，优化大语言模型智能体的后训练效果？ | — |
| 5 | high | - | [AliyunConsoleAgent: Training Web Agents in Real-World Cloud Envi...](http://arxiv.org/abs/2606.09447v1) | policy optimization | 通过前沿模型轨迹蒸馏做监督微调，结合GRPO强化学习与双通道奖励模型，优化智能体... | 仅在阿里云内部场景验证，方法在其他厂商异构云环境的泛化能力未得到... | 能否借鉴这种蒸馏结合GRPO的方案，在通用场景中低成本训练性能达标的专用Web Agent？ | — |
| 6 | high | - | [Beyond Absolute Imitation: Anchored Residual Guidance for Privil...](http://arxiv.org/abs/2606.10385v1) | online distillation | 通过锚定残差解耦特权监督，实现可控同策略蒸馏，减少模型后见偏差，规范推理生成行为... | 未披露具体公开基准，未在真实落地Agent场景验证，方法的泛化能... | 可借鉴锚定残差解耦思路，改进现有Agent在线策略蒸馏方案，缓解长轨迹推理的后见泄漏问题。 | — |
| 7 | high | - | [Beyond Uniform Token-Level Trust Region in LLM Reinforcement Lea...](http://arxiv.org/abs/2606.10968v1) | policy optimization | 通过位置加权阈值与累积前缀预算调整信任域约束，优化RLVR框架下的策略更新过程。 | 未在具体下游任务基准验证，方法泛化性与实际落地效果未明确说明。 | 将累积前缀偏差约束思路引入agent在线策略优化，能否缓解agent推理的早期错误累积问题？ | — |
| 8 | high | - | [Bittensor Agent Arenas as a Trajectory Primitive: Distilling a S...](http://arxiv.org/abs/2606.10064v1) | online distillation | 通过激励对齐的Agent竞技场生成合格轨迹，经过滤后结合SFT与教师引导的Dr.... | 数据依赖特定Bittensor子网产出，脱离该生态可复用性较低，... | 探索如何利用激励对齐的开放Agent竞技场生成低成本高质量轨迹，解决小模型Agent后训练的... | — |
| 9 | high | - | [Breaking Entropy Bounds: Accelerating RL Training via MTP with R...](http://arxiv.org/abs/2606.12370v1) | policy optimization | 通过分析熵波动对MTP接受率的约束，引入概率拒绝采样，设计端到端TV损失优化接受... | 仅在Qwen系列底座模型上验证，未验证其他架构底座的泛化效果，跨... | 在Agent在线策略蒸馏的rollout阶段引入该MTP方案，能否有效降低蒸馏过程的算力成本... | — |
| 10 | high | - | [Breaking the Tokenizer Barrier: On-Policy Distillation across Mo...](http://arxiv.org/abs/2606.09456v1) | online distillation | 通过设计精确的分词映射算法，实现跨模型族、跨分词器场景下高保真的在线策略知识蒸馏... | 未在下游实际任务尤其是agent场景验证效果，跨大模型族蒸馏的效... | 能否将该跨模型族在线蒸馏方法，用于不同开源模型的agent策略在线蒸馏，优化学生agent的... | — |
| 11 | high | - | [Capability-Aligned Hierarchical Learning for Tool-Augmented LLMs](http://arxiv.org/abs/2606.09371v1) | policy optimization | 通过RLVR对分层工具学习框架的高层规划与低层执行策略做联合优化，对齐二者能力，... | 仅在有限公开基准验证，未验证方法在大规模真实工业场景中的泛化性与... | 能否将该分层能力对齐思路结合在线蒸馏，优化工具增强agent后训练阶段的策略性能？ | — |
| 12 | high | - | [Co-Evolving Skill Generation and Policy Optimization](http://arxiv.org/abs/2606.08755v1) | policy optimization | 通过预存储验证估计候选技能边际效用，基于奖励间隙过滤劣质技能，用效用信号训练技能... | 未经过大规模实际任务验证，边际效用估计偏差可能误滤有用技能，影响... | 如何在在线迭代的agent技能库中，低成本验证新技能边际效用，提升长周期运行agent的可靠... | — |

## 方法族分布

- **policy optimization**：43 篇
- **reward learning**：12 篇
- **online distillation**：8 篇
- **evaluation/benchmark**：5 篇
- **other**：5 篇
- **unlearning/safety**：3 篇
- **survey**：3 篇
- **agent harness**：2 篇
- **model steering**：2 篇
- **tool-use control**：1 篇
- **multi-agent coordination**：1 篇
- **evaluation/benchmark, reward learning**：1 篇

## 失败模式与风险信号

- 稀疏延迟奖励下信用分配难，训练不稳定，易出现分布偏移导致智能体性能下降
- 现有前缀评估仅依赖局部正确性，在大搜索空间、稀疏奖励场景下评估偏差大
- 工具决策次优、多步交互错误累积、决策过度自信错误
- 现有流GRPO训练与模型能力脱钩，提示选择盲目、优势估计偏差，训练不稳定
- 单步一次性奖励对多轮SQL修正引导不足，无法适配多轮SQL优化过程
- 调度器无法适配可变集群规模，规模变化需重训，注意力特征分布偏移导致新规模性能下降。
- 将多元分歧偏好扁平化为统一偏好模型，导致奖励模型无法匹配用户真实需求。
- 稀疏奖励场景下强化学习收敛慢、探索效率低、泛化性能差
- 跨语言事实不一致
- 硬掩码直接丢弃越界有害token的梯度，造成优化信息损失，导致训练稳定性不足

## 评测信号

- Q-Evolve在三个基准任务上的样本效率、鲁棒性与整体任务性能均优于对比的强基线方法
- 验证不同场景下前缀监督信号的效果，发现在大候选池、高搜索预算、稀疏奖励场景下性能更优。
- 通过参数空间诊断与控制实验，验证同策略蒸馏独特更新几何与子空间锁定的功能特性。
- 在多个工具任务上验证方法能提升决策质量与智能体整体性能，同时保持更可靠的决策不确定性估计。
- 仅明确提到模型性能提升与训练稳定性提升，未公布具体的评测指标与数值结果。
- 在BIRD、Spider及Spider鲁棒性变体上，所提方法在主任务性能和鲁棒性评测均取得一致的提升。
- 16节点训练直接测试32、48节点，N=48时相较无SRR同架构降低平均响应时间8.9%。
- 指出当前偏好对齐方法无法捕捉真实多元需求，投入充足的大模型仍然存在较高的幻觉率问题。
- 相对无引导、未校准、标准RL三类基线，ULPS实现超9%执行准确率提升，减少环境交互，提升奖励AUC
- GRPO相较于轻量持续预训练和监督微调，在跨语言一致性与未见语言泛化上都获得了更优结果。

## 控制机制 / Harness 信号

- 通过分布内强化学习框架，结合隐式Q学习生成过程奖励信号，依托行为近端策略优化实现智能体策略迭代自改进。
- 通过基于前缀增益学习的前缀效用模型PUM，为推理过程提供更贴合最终结果的监督奖励信号。
- 通过参数空间诊断刻画同策略蒸馏的更新轨迹，对照基线方法分析其参数更新的独特规律。
- 将不确定性量化引入奖励设计，加入排斥力维持不确定性分隔，结合轻量标注后训练优化智能体工具决策。
- 通过能力感知的自适应提示选择与全局-组内优势融合，改进GRPO策略优化过程，稳定训练并提升性能。
- 通过设计融合结构、词法信息的渐进式多类奖励，为多轮SQL修正提供更密集有效的优化引导。
- 通过结构化表示正则化SRR约束注意力特征分布，稳定不同输入规模的特征统计，提升规模泛化能力。
- 通过分析人类真实多元偏好，揭露现有奖励对齐方法的缺陷，为AI对齐改进提供方向依据。
- 通过不确定性调制的LLM行为引导，结合熵基混合机制自适应平衡LLM先验与PPO学习得到的agent策略
- 采用一致性驱动的GRPO强化学习优化模型，通过重组多语言路由、减少语言专业化提升跨语言事实一致性。

## 可靠性 / 落地风险

- 仅在学术基准验证，未测试真实复杂环境，自迭代过程存在潜在分布偏移累积风险
- 仅在数学推理任务验证，未在更多任务及真实Agent场景测试，通用性有待验证。
- 仅做理论特性分析，未在下游实际任务验证，结论对实际方法优化的实用价值尚不明确。
- 未披露具体评测基准细节，方法泛化性未充分验证，缺乏各模块作用的详细分析披露。
- 仅在文本到图像流模型GRPO场景验证，方法泛化到其他场景的有效性未验证。
- 依赖Oracle构建诊断树获取结构信息，脱离标注Oracle的开放场景适用性会受限。
- 未在真实工业集群的多样工作负载上验证，实际落地的泛化效果尚不明确。
- 现有对齐方法错误假设人类偏好统一性，训练出的AI无法匹配真实需求，对齐可靠性不足。
- 仅在小规模网格基准验证，方法复杂度较高，复杂开放场景下的泛化性尚未验证
- 实验仅在人工构建数据集开展，未在真实跨语言应用场景验证，泛化可靠性待验证。

## 可延展 Idea Hook

- 可将该自进化分布内优化思路结合在线蒸馏，进一步提升agent策略迭代的样本效率
- 可将这种基于增益的前缀评估思路引入Agent推理的奖励学习，缓解Agent策略优化中的奖励稀疏问题。
- 能否基于本文发现的子空间锁定特性，设计低算力开销的Agent策略在线蒸馏优化方案？
- 可探索在在线策略蒸馏中引入不确定性对齐机制，提升师生框架下智能体工具调用决策的可靠性。
- 可尝试将本文能力感知自适应提示选择思路，迁移到大语言模型Agent的GRPO策略优化中。
- 可以将渐进式奖励设计思路引入多轮agent决策，解决多步任务中稀疏奖励引导不足的问题。
- 能否将本文针对规模泛化的正则化思路迁移到LLM agent测试时扩展场景，提升泛化性能？
- 针对人类偏好多元性，研究可适配偏好分歧的奖励建模方法，提升大语言模型对齐的实际可靠性。
- 可探究将这种不确定性感知的LLM引导策略引入agent在线蒸馏，改善稀疏奖励场景下的agent训练效率
- 能否将这种一致性驱动强化学习思路，迁移到多语言智能体的事实一致性优化任务中？
- 可将该平滑散度正则方法引入agent在线策略蒸馏，优化离策略更新的稳定性，提升蒸馏效率。
- 可研究经RLHF对齐的Agent是否也存在浅对齐问题，隐藏的违规行为结构是否可被用户提示绕过激活。

## 下次可问导师的问题

- 这种基于分布内学习的自进化框架结合在线蒸馏能否提升长程任务agent的训练效率？
- 我们能否把这种前缀增益评估思路用到在线策略蒸馏的学生模型中间步骤奖励设计中？
- 我们是否可以利用子空间锁定的结论，来降低当前Agent在线蒸馏工作的算力成本？
- 我们做在线策略蒸馏优化agent工具决策时，是否需要引入不确定性对齐机制来提升性能？
- 我们做Agent GRPO策略优化时，是否值得引入这种能力感知机制来提升训练稳定性？
- 这种针对多轮修正的渐进式奖励设计思路，能否迁移到通用多轮agent决策任务中？
- 这种面向调度的规模泛化正则化方法是否适合迁移到通用agent的测试时扩展优化？
- 我们是否需要在当前的奖励学习研究中，加入对人类偏好多元性建模的探索？
- 我们能否基于这一思路改进现有在线蒸馏框架，解决稀疏奖励下agent训练效率低的问题？
- 我们当前Agent可靠性研究，是否需要关注跨语言场景下事实一致性的优化需求？
- 我们是否可以将这种散度正则的思路整合到当前的agent在线策略蒸馏框架中做改进？
- 我们做Agent对齐研究，是否需要关注RLHF带来的浅对齐问题以及隐含的可绕过安全风险？

## 代码资源

- [Claw-R1: A Step-Level Data Middleware System for Agentic Reinforcement Learning](https://github.com/AgentR1/Claw-R1) · 183 stars
- [3SPO: State-Score-Supervised Policy Optimization for LLM Agents](https://github.com/genalyu/3SPO.) · 15 stars
- [Trajectory-Refined Distillation](https://github.com/louieworth/trd) · 3 stars
- [Pushing the Limits of LLM Tool Calling via Experiential Knowledge Integration an...](https://github.com/hypasd-art/KATE.) · 1 stars
- [Artificial Intelligence for Mathematical Reasoning: An Integrated Survey of Lang...](https://github.com/Starscream-11813/awesome-AI4Math.)
- [GIFT: LLM-Guided State-Reward Interface for Financial Reinforcement Learning](https://github.com/KAG778/GIFT)
- [Topical Phase Transitions in Artificial Intelligence Research: Large-Scale Evide...](https://github.com/KurbanIntelligenceLab/ai-phase-transitions.)

## 常见基线方法

- **GRPO**：5 篇
- **未提及具体基线**：2 篇
- **监督微调(SFT)**：2 篇
- **PPO**：2 篇
- **基于局部正确性的过程奖励模型**：1 篇
- **基于规则的奖励方法**：1 篇
- **可验证奖励强化学习(RLVR)**：1 篇
- **Flow-GRPO**：1 篇
- **DanceGRPO**：1 篇
- **Flow-CPS**：1 篇

## 常用数据集

- **数学推理基准**：6 篇
- **摘要未提及**：5 篇
- **数学推理任务**：3 篇
- **WebShop**：2 篇
- **竞赛数学基准**：2 篇
- **五个数学推理基准**：2 篇
- **GSM8K**：2 篇
- **AppWorld**：2 篇
- **ALFWorld**：2 篇
- **AlfWorld**：1 篇

---
*自动生成于 2026-06-14 | ArXiv_Daily_Digest*