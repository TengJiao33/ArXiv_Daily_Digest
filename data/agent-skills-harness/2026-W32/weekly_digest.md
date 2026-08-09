# Agent Skills 与 Harness — 2026-W32 (08/03-08/09)

本周新增 **139** 篇论文，**13** 篇附带代码。优先级：high 108 / medium 23 / low 8。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | - | [Agentic Reinforcement Learning with Self-Distilled Reward Shapin...](http://arxiv.org/abs/2608.03223v1) | reward learning | ADRS在不同RL骨干、少数据、未见任务、扩展训练等设置下，都能稳定提升长周期交互任务的性能... | 通过自蒸馏获得token级监督信号，结合收益关联的TVA门控校准信号，整合进强化... | 未披露具体基准名称与详细消融结果，未验证该方法在真实工业场景的落... | ✅ |
| 2 | high | - | [Cooperative Coevolution for Resource-Constrained Agentic LLM Pos...](http://arxiv.org/abs/2608.02391v1) | policy optimization | 相同GPU小时预算下，CoPES恢复了GRPO 92%的验证精度增益，内存需求不到全参数GR... | 通过协同分解参数子空间的进化策略，降低资源约束下智能体后训练的内存与时间消耗，提... | 仅在4B参数模型与两类任务上验证，未测试更大模型与更多真实场景，... | ✅ |
| 3 | high | - | [EnvACE: Internalizing Environment Dynamics via World Rehearsal f...](http://arxiv.org/abs/2608.06197v1) | policy optimization | 世界预演可在不同模型规模下稳定提升策略学习，测试阶段中等预演预算无需额外外部交互即可提升性能... | 通过世界预演让策略内化环境动力学，训练替代外部环境交互，测试可预演后执行，优化决... | 仅在标准学术基准验证，未测试真实工业场景的泛化能力，落地效果待验... | ✅ |
| 4 | high | - | [GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks](http://arxiv.org/abs/2608.03764v1) | evaluation/benchmark | 自进化可将留出测试集准确率最高提升16.44个百分点，但最优性能仍远低于91.6%的全信息O... | 通过设计可归因、抗数据污染的评测基准，为智能体自进化能力评估提供反馈，明确能力缺... | 当前智能体自进化性能远未达标，仅覆盖规则类企业工作流，泛化性待验... | ✅ |
| 5 | high | - | [PAST-Bench: Benchmarking the Foundations of Recursive Self-Impro...](http://arxiv.org/abs/2608.04003v1) | evaluation/benchmark | 保留经验确实能提升智能体性能，但提升不均衡，相同整体增益的智能体，其提升路径符合预期设计的程... | 基于评测发现的问题，对原有Hermes框架在智能体循环各阶段添加针对性干预，提升... | 改进效果依赖具体能力类型与基础模型，通用性不足，尚未在更大规模场... | ✅ |
| 6 | high | - | [PosterMELD: Multi-Agent Paper-to-Poster Generation for Controlla...](http://arxiv.org/abs/2608.02218v1) | multi-agent coordination | PosterMELD打印就绪率达81.3%，为P2P的3.4倍，单请求平均成本仅为Codex... | 依托容量感知槽引导生成过程，通过确定性门限与VLM审查将失败路由至限定范围修复，... | 仅在科学论文转海报场景验证，跨任务跨场景通用性未得到充分验证 | ✅ |
| 7 | high | - | [RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Re...](http://arxiv.org/abs/2607.29241v1) | agent harness | 分离方向选择与假设生成，配合多臂老虎机路由，有限预算下更稳定，在线测试ADVV提升2.084... | 通过RecHarness分离修改方向选择与方案生成，用多臂老虎机依验证反馈控制a... | 仅针对推荐模型优化场景验证，跨场景通用性未验证，暂无其他明显落地... | ✅ |
| 8 | high | - | [SearchMaster: Grounded and Regulated Self-Play for Search Agents](http://arxiv.org/abs/2608.01822v1) | agent harness | 加入三项控制的自对弈训练，可将Qwen3.5-9B搜索准确率提升13.33个百分点，Brow... | 通过证据链锚定任务生成、搜索深度奖励校准难度、过度打开惩罚规制工具使用，结合GR... | 摘要未对比现有SOTA方法，也未验证方法在开放真实搜索场景的泛化... | ✅ |
| 9 | high | - | [Self-Evolving Coding Agents](http://arxiv.org/abs/2608.03392v1) | survey | 软件工程特有的可执行反馈、仓库级上下文与编码轨迹，是智能体自进化天然优势但也带来诸多新挑战。 | 系统梳理自进化编码智能体的各类演化路径，厘清领域概念边界，为设计可控自适应编码智... | 自进化编码智能体存在反馈不可靠、基准过拟合、成本高、安全性不足等... | ✅ |
| 10 | high | - | [SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Aug...](http://arxiv.org/abs/2608.05573v1) | evaluation/benchmark | 经误判案例精炼的JudgeSkill使同一款智能体评判器准确率提升14.8个百分点，离线选轨... | 将验证知识外部化为可复用JudgeSkill，引导智能体评判器做针对性检查，通过... | 仅在自建基准上验证，尚未在真实工业场景任务中测试，泛化能力未得到... | ✅ |
| 11 | high | - | [Test-time reasoning effort and unauthorized tool use in language...](http://arxiv.org/abs/2608.03169v1) | tool-use control | 本研究840条实验轨迹中未出现任何未授权工具调用，高低推理算力下违规率95%上限分别低于3.... | 依托预设的工具访问控制策略约束调用权限，调整推理算力参数，检验参数对违规调用的影... | 仅在单个模型的有限测试场景实验，结论向其他模型和真实场景的推广性... | ✅ |
| 12 | high | - | [Tool Specifications Matter: Uncovering and Mitigating Safety Ris...](http://arxiv.org/abs/2607.29254v1) | tool-use control | Schema格式工具规范会削弱模型拒绝信号，是智能体安全退化的主因，SafeKeep可将有害... | 提出推理阶段防护方案SafeKeep，通过分离安全判断与工具执行的规范形式，提升... | 仅在有限学术基准完成测试，未在真实复杂工业场景验证方法的鲁棒性与... | ✅ |

## 方法族分布

- **agent harness**：46 篇
- **evaluation/benchmark**：38 篇
- **tool-use control**：12 篇
- **skill generation**：11 篇
- **policy optimization**：7 篇
- **other**：5 篇
- **unlearning/safety**：5 篇
- **multi-agent coordination**：5 篇
- **survey**：4 篇
- **online distillation**：2 篇
- **reward learning**：2 篇
- **model steering**：1 篇

## 失败模式与风险信号

- 长文档抽取时记录列表截断，高准确率智能体推理成本过高
- 自动化偏见、工程师去技能化、浅层参与、责任扩散
- 验证计算不精确，数学验证建模与底层实现过早耦合
- 自对弈训练缺乏持久状态，失败经验无法塑造未来训练，技能记忆固定不演化
- 现有验证仅评估孤立组件，无法捕捉智能体多步轨迹在动态环境中的多维度失效。
- 工具规范格式不当引发不安全工具执行
- 低质量稀缺训练数据导致小模型工具调用性能大幅落后于大模型
- LLM同时选方向生成假设导致有限预算下搜索不稳定，局部优化容易停滞
- 工具返回绑定错误引发的误授权放行
- 单轮标注的幻觉与时序混淆错误

## 评测信号

- 评测不同类型智能体在长短文档上的抽取、溯源性能与成本，验证LlamaExtract的综合性能最优
- 本文未开展实证评测，仅基于已有公开研究完成概念整合与培养框架的构建。
- 在DeepSeek、GPT、Gemini共七种模型配置下测试，最高较最强基线提升准确率8.3个百分点，中高复杂度样本增益更大。
- SESA在多个骨干模型上相对SSP平均准确率提升1.2-3.2个点，相对SkillRL提升0.9个点，提升效果稳定
- 现有智能体验证研究覆盖不均衡，行为验证充分，时序、合规等多个关键方向验证覆盖存在明显缺口。
- 肿瘤分割Dice系数相对提升22.4%，边界错误降低超39%，70%合成病例可支持与真实影像一致的临床决策。
- 在专家标注的BrainArena基准上性能显著优于现有最优智能体基线，实际研究产出了可验证的神经科学新发现。
- 有害请求拒绝率从23.8%提升至70.6%，观测级提示注入攻击成功率从25.6%降至2.5%，同时保留任务处理能力。
- 经Turnstile数据微调的小模型工具调用性能较原生base模型提升数倍，部分场景性能超越规模大十余倍的大模型。
- 有限实验预算下搜索比纯LLM推理更稳定，在线A/B测试显示ADVV提升2.084%，收入提升0.534%

## 控制机制 / Harness 信号

- 通过构建标准化评测基准，量化衡量不同企业文档抽取智能体的多维度性能，提供评测反馈
- 通过构建系统化教育框架，培养工程师对智能体系统的管控判断能力，规范人机协作过程。
- 通过中断-执行-恢复的数学工具流接口解耦验证建模与执行，分工完成验证，支撑答案判定与修正。
- 通过任务生成与技能记忆的双向共演化循环，将有效失败提炼为可复用技能，动态调整智能体行为与训练分布
- 构建五维度分类框架梳理智能体验证研究现状，暴露领域缺口，为可信智能体落地提供方向指引。
- 本文为医学影像合成研究，不涉及模型或智能体行为的控制与改进相关内容。
- 通过从公开论文代码对提取的代码化分析技能构建技能库，结合分层规划约束智能体生成规范的分析流程。
- 提出推理阶段防护方案SafeKeep，通过分离安全判断与工具执行的规范形式，提升智能体工具调用的安全性。
- 通过将多轮交互分解为约束分步生成，搭配验证与错误反馈循环，细粒度控制生成数据的质量与多样性。
- 通过RecHarness分离修改方向选择与方案生成，用多臂老虎机依验证反馈控制agent搜索方向，辅以跳盆机制

## 可靠性 / 落地风险

- 仅覆盖已有标注的企业文档场景，未验证未知场景泛化性，部分高性能模型成本偏高
- 属于工程教育研究，未产出可落地的agent技术方案，对本方向工业落地无直接支撑。
- 未公开具体数据集与基线细节，未说明算力开销，可复现性存在潜在风险。
- 仅在问答基准任务完成验证，未在复杂真实开放环境测试，泛化能力有待验证
- 缺乏成熟的全生命周期验证方法，难以保障安全关键工业场景下智能体部署的可靠性。
- 仅在小规模样本完成验证，缺乏大规模多中心临床验证，临床落地仍需进一步研究。
- 仅适用于神经科学领域，技能覆盖依赖已有公开论文代码，通用性不足，未明确说明算力开销。
- 仅在有限学术基准完成测试，未在真实复杂工业场景验证方法的鲁棒性与适配性。
- 仅在公开基准测试验证，未提及合成数据在真实工业场景的泛化稳定性
- 仅针对推荐模型优化场景验证，跨场景通用性未验证，暂无其他明显落地风险

## 代码资源

- [GDPevo: Evaluating Agent Self-Evolution on Real Business Tasks](https://github.com/Prism-Shadow/GDPevo.) · 41 stars
- [EnvACE: Internalizing Environment Dynamics via World Rehearsal for Agentic Reinf...](https://github.com/Within-yao/EnvACE.) · 9 stars
- [SkillTV-Bench: Benchmarking How Well Judges Perform on Skill-Augmented Agentic E...](https://github.com/HanZhi306/SkillTV-Bench) · 3 stars
- [PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Person...](https://github.com/Gen-Verse/PAST-Bench) · 2 stars
- [Tool Specifications Matter: Uncovering and Mitigating Safety Risks in AI Agents](https://github.com/snowcatsmoking/SafeKeep) · 1 stars
- [PosterMELD: Multi-Agent Paper-to-Poster Generation for Controllable Design Diver...](https://github.com/Shannon4Science/PosterMELD.) · 1 stars
- [Agentic Reinforcement Learning with Self-Distilled Reward Shaping](https://github.com/gitrxh/ADRS-arxiv) · 1 stars
- [RecHarness: A Bandit-Routed Agentic Harness for Self-Evolving Recommender System...](https://github.com/6lyc/RecHarness.)
- [Cooperative Coevolution for Resource-Constrained Agentic LLM Post-Training](https://github.com/MetaronWang/CoPES)
- [SearchMaster: Grounded and Regulated Self-Play for Search Agents](https://github.com/WentaoTan/SearchMaster.)

## 常见基线方法

- **未提及具体基线方法**：2 篇
- **商用视觉大模型**：1 篇
- **编码智能体**：1 篇
- **基于自然语言反思的修正方法**：1 篇
- **直接生成验证程序的验证方法**：1 篇
- **SSP**：1 篇
- **SkillRL**：1 篇
- **预对比度基线**：1 篇
- **现有最优合成模型**：1 篇
- **其他生成模型基线**：1 篇

## 常用数据集

- **ALFWorld**：5 篇
- **摘要未提及**：4 篇
- **BrowseComp**：3 篇
- **OSWorld 2.0**：2 篇
- **SkillsBench**：2 篇
- **WebShop**：2 篇
- **BrowseComp-Plus**：2 篇
- **SWE-Bench Pro**：2 篇
- **Terminal-Bench 2**：2 篇
- **ExtractBench**：1 篇

---
*自动生成于 2026-08-09 | ArXiv_Daily_Digest*