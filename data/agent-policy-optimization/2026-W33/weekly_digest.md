# Agent 策略优化与在线蒸馏 — 2026-W33 (08/10-08/16)

本周新增 **68** 篇论文，**6** 篇附带代码。优先级：high 29 / medium 30 / low 9。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](http://arxiv.org/abs/2608.09836v1) | online distillation | 发现同策略蒸馏存在退化一致失败模式，强错配下TIDE将Avg@8从6.9%提升至20.3%，... | 通过token级的师生缺余错配校正改进同策略蒸馏，抑制退化回答，提升蒸馏过程中教... | 仅在数学推理场景验证，未在实际agent任务测试，方法通用性有待... | ✅ |
| 2 | high | - | [Beyond Solvability: Task Learnability as a Static Prior for LLM ...](http://arxiv.org/abs/2608.09217v1) | policy optimization | 任务可学习性跨独立训练上下文可复现，能预测下游效用，TrajVal可提升RL后训练数据效率，... | 将任务可学习性作为静态先验优化RL后训练的任务采样调度，提升训练过程的数据利用效... | 仅在推理类任务验证，未测试更多任务类型，估计性能依赖探测运行的质... | — |
| 3 | high | - | [Bidirectional Context Self-Distillation for Reinforcement Learni...](http://arxiv.org/abs/2608.09555v1) | online distillation | 融合增广和约简两个互补上下文视图的自蒸馏信号，可在所有测试模型规模下提升基于技能的LLM智能... | 通过双向上下文自蒸馏，从增广和约简两个互补视图获取token级监督信号，重缩放R... | 仅在两个标准学术基准测试，未在复杂真实场景验证，方法通用性有待进... | — |
| 4 | high | - | [Consilience for Verifier-Free Test-Time Scaling](http://arxiv.org/abs/2608.09898v1) | model steering | 现有基于置信度的无验证器测试时缩放方法中，均匀高置信度通常代表探索不足，更易产出置信度高的错... | 通过Consilience框架评估推理置信度的时间不对称性，惩罚高初始置信度，筛... | 仅在数学与代码两类任务验证，方法通用性未充分验证，对黑盒模型的适... | — |
| 5 | high | - | [Control-Diverse Reinforcement Fine-Tuning: Decoupling the Shared...](http://arxiv.org/abs/2608.08224v1) | policy optimization | 高共享激活可与任务特异性控制共存，激活-控制间隙越小意味着控制坍缩到共享方向丢失特异性，CD... | 通过在RL后训练损失中加入共享控制瓶颈正则项，鼓励控制多样性，解耦控制瓶颈，提升... | 方法依赖二阶梯度的一阶近似，其机制结论在更大规模模型上的通用性未... | — |
| 6 | high | - | [Dual-Loop Self-Evolution via Verifiable Emotion Feedback for Mul...](http://arxiv.org/abs/2608.10626v1) | policy optimization | 该框架不增加回滚预算，将Qwen3-8B整体得分提升25.37点，比基线均匀情感奖励RL高出... | 基于可验证情感反馈设计双环训练框架，内圈优化对话策略，外圈自适应调整训练经验分布 | 依赖固定的用户模拟器与验证器，二者的误差会传递，影响最终策略的训... | — |
| 7 | high | - | [Fisher-R1: Training LLM Agents for Reliable Hypothesis Testing](http://arxiv.org/abs/2608.07437v1) | policy optimization | 当前LLM智能体缺乏可靠的假设检验统计推理，Fisher-R1相对DeepSeekV4-Pr... | 基于验证后的统计正确性设计奖励信号，使用强化学习训练LLM智能体，优化其假设检验... | 仅在自建基准P-Bench完成评测，方法在真实复杂科研场景下的泛... | — |
| 8 | high | - | [GCPO: Diagnosing and Constraining Subspace Geometry in Rollout R...](http://arxiv.org/abs/2608.11674v1) | policy optimization | 更新与预训练权重主导奇异子空间的瞬时重叠峰值通常预示性能退化，GCPO最高较最强基线提升2.... | 通过对参数更新施加双边正交投影，将更新约束在预训练权重的互补子空间，稳定策略训练... | 仅在两个中尺寸大模型上验证，未在更大参数规模模型测试，方法通用性... | — |
| 9 | high | - | [Gated-BEPO: Confidence-Gated Bellman Credit Assignment for Large...](http://arxiv.org/abs/2608.06861) | policy optimization | 选择性引入步级贝尔曼信用比均匀引入效果更好，自适应门控融合显著优于传统固定权重融合方式 | 通过改进信用分配机制优化大语言模型智能体的策略训练，自适应融合不同粒度信用信号提... | 依赖经验回滚图构造，对轨迹数据量要求较高，大规模应用可能存在较高... | — |
| 10 | high | - | [IB-RL: Isolated Bilateral Reinforcement Learning for Strategic D...](http://arxiv.org/abs/2608.06735v1) | policy optimization | 固定对手训练会引发静态对手不匹配，IB-RL在Vehicle TeleSales达89.6%... | 采用双边共训练搭配各智能体策略隔离优化机制，避免策略过拟合固定对手，提升泛化能力... | 仅在两个特定策略对话任务验证，方法通用性未得到充分验证，评测场景... | — |
| 11 | high | - | [Idea Search: Guiding Tree Search with Ideas to Explore Diverse S...](http://arxiv.org/abs/2608.08958v1) | policy optimization | 思想库增强仅对老虎机采样有益，偏好新思想的探索提示能发掘稀有高性能解，增加采样级探索反而会降... | 通过引入动态更新的思想库引导树搜索分支探索，改进大语言模型测试阶段的搜索行为，提... | 仅在单个生物信息学任务上验证，方法的泛化能力未得到验证，通用性有... | — |
| 12 | high | - | [Improving Generalization Robustness of Multimodal RLVR](http://arxiv.org/abs/2608.08802v1) | reward learning | 标准RLVR在提示扰动下准确率下降约3%，提出的PIRL下降不超过1%，分离奖励格式语义可有... | 通过设计分离格式与语义的动态三元奖励，添加一致性正则约束，提升RLVR对扰动提示... | 仅在公开基准测试验证，未在真实高风险医疗场景落地测试，实际部署可... | — |

## 方法族分布

- **policy optimization**：30 篇
- **reward learning**：7 篇
- **online distillation**：7 篇
- **evaluation/benchmark**：7 篇
- **model steering**：3 篇
- **other**：3 篇
- **agent harness**：3 篇
- **unlearning/safety**：2 篇
- **skill generation**：2 篇
- **survey**：1 篇
- **multi-agent coordination**：1 篇
- **consistency detection**：1 篇

## 失败模式与风险信号

- 大模型后训练输出创造性与多样性下降
- LLM智能体做假设检验时，即便分析执行正确，也常出现细微推断错误，最终得出错误结论。
- 临床诊断过早闭合，漏检危险信号，序列临床决策能力不足
- 纯大语言模型控制器无法满足严格实时的工业安全关键控制需求
- 大标签空间类别不平衡，序列生成目标缺乏对预测集合的直接监督
- 固定对手训练导致策略过拟合对手特有规律，泛化到未知对手性能下降
- DPO蒸馏仅模仿教师离线选择，未直接优化目标，原有方案依赖第三方带来隐私暴露
- 现有自动评分器未观测到决定性状态就给出判断，导致奖励信号不准确
- 现有置信基无验证器测试时缩放方法在复杂任务上灾难性失效，易产出高置信错误结果
- 同策略蒸馏的退化一致：学生靠循环达成高token一致，但生成全局有缺陷的退化回答

## 评测信号

- 不牺牲生成质量的前提下提升创造性多样性，RL应用中取得明确的性能增益，有具体数值支撑
- 在P-Bench基准上，Fisher-R1-14B相比DeepSeekV4-Pro平均相对提升21%单试成功率，最难任务提升达26%，性能优于多个开源闭源强基线。
- 对抗条件下诊断准确率提升7%，漏检率降31%，87.6%临床专家偏好该模型，多个未知基准性能均优于基线。
- 基于现有已发表文献证据做定性分析，未给出具体的量化评测指标与结果
- 该方法在四个CTI基准取得最佳平均F1，子技术级F1提升7.4个百分点，8B模型推理速度比基线快28倍。
- 未知独立留出对手上的泛化成功率，IB-RL相比最优单边基线，两个任务成功率分别提升5%和12%。
- 该方案隐私-效用权衡优于DPO基线，相比前沿大模型可去除更多隐私，推理成本仅为GPT-4o的1%
- 在WebGen-Bench上8B参数策略功能成功率达52.01%，超出基线7.88个百分点，在WG-core-250上超越480B参数Qwen3-Coder。
- 实验验证所提Consilience方法在研究生数学推理、自由形式代码生成任务上，效果均优于现有无验证器测试时缩放基线方法。
- 在多组Qwen3师生对的数学推理测试中，TIDE性能稳定优于基线，强师生错配场景下提升尤为显著

## 控制机制 / Harness 信号

- 通过注入特殊[StartCreativity]标记偏置生成方向，在指令调优中平衡生成质量与创造性
- 基于验证后的统计正确性设计奖励信号，使用强化学习训练LLM智能体，优化其假设检验推理能力，提升结论可靠性。
- 通过强化学习框架，利用对齐诊断、安全等多目标的结构化奖励信号，在模拟对抗交互中优化智能体临床决策策略。
- 明确LLM在MARL中的四类接入点，分层划分功能模块，梳理定位两类方法各自的适用场景
- 通过带可验证分解奖励的强化学习，直接对预测技术集合的精确率、召回率与输出格式进行监督。
- 采用双边共训练搭配各智能体策略隔离优化机制，避免策略过拟合固定对手，提升泛化能力。
- 通过组相对策略优化在线强化模型，基于自生成的隐私与效用双目标奖励优化行为，防范奖励黑客
- 通过设计自进化程序化验证评分器，提供准确的强化学习奖励信号，引导大模型策略优化，提升网页生成功能正确性。
- 通过Consilience框架评估推理置信度的时间不对称性，惩罚高初始置信度，筛选满足最终高置信要求的推理结果，改进输出质量。
- 通过token级的师生缺余错配校正改进同策略蒸馏，抑制退化回答，提升蒸馏过程中教师知识的传递效果

## 可靠性 / 落地风险

- 摘要未披露明确局限性，缺乏大规模工业场景验证，存在潜在落地适配风险
- 仅在自建基准P-Bench完成评测，方法在真实复杂科研场景下的泛化可靠性未得到验证。
- 仅在模拟环境完成验证，未经过真实临床检验，落地临床存在安全性与有效性不确定性。
- 纯LLM控制方案的实时性与安全性缺乏足够实证支持，工业落地存在较高不确定性
- 仅在CTI提取特定任务验证，方法的泛化能力未在更多场景得到验证。
- 仅在两个特定策略对话任务验证，方法通用性未得到充分验证，评测场景有限。
- 评测依赖LLM法官，缺少大规模真实场景下隐私保护与文本效用的实证验证
- 需要在真实浏览器实例化项目收集轨迹证据，验证技能构建流程复杂，落地资源成本较高。
- 仅在数学与代码两类任务验证，方法通用性未充分验证，对黑盒模型的适配性尚不明确。
- 仅在数学推理场景验证，未在实际agent任务测试，方法通用性有待进一步验证

## 代码资源

- [Test-Time Augmentation for LLMs: When Input Diversity Beats Output Diversity at ...](https://github.com/aws-samples/sample-genai-reflection-for-bedrock.) · 12 stars
- [Mismatch Matters: On-Policy Distillation Beyond Token Agreement](https://github.com/yzc-666/TIDE) · 1 stars
- [Efficient Test-Time Scaling for LLM-based Time Series Forecasting](https://github.com/xuanmay2701/SCALER.) · 1 stars
- [CARE: Confidence-Aware Reasoning for Reliable Medical VQA](https://github.com/anotherbricki/CARE.) · 1 stars
- [JustLLMGRPO: Radiographic Control for Chest X-Ray Generation](https://github.com/pxcai/JustLLMGRPO.)
- [Finding the Signal in the Spam: Jointly Learning Rewards and Worker Reliability ...](https://github.com/KaustubhShejole/BoRa_EM.)

## 常见基线方法

- **GRPO**：4 篇
- **自一致性**：2 篇
- **监督微调（SFT）**：2 篇
- **多模型基线**：1 篇
- **多模型输出蒸馏变体**：1 篇
- **骨干模型**：1 篇
- **GPT-5.4**：1 篇
- **DeepSeekV4-Pro**：1 篇
- **基础大语言模型**：1 篇
- **传统多智能体强化学习**：1 篇

## 常用数据集

- **摘要未提及**：9 篇
- **数学推理任务**：5 篇
- **代码生成任务**：4 篇
- **ALFWorld**：3 篇
- **WebShop**：2 篇
- **数学推理基准**：2 篇
- **逻辑推理任务**：2 篇
- **叙事生成任务**：1 篇
- **AMC**：1 篇
- **MATH**：1 篇

---
*自动生成于 2026-08-16 | ArXiv_Daily_Digest*