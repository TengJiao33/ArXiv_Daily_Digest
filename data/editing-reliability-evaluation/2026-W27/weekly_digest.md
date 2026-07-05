# 编辑可靠性与行为控制 — 2026-W27 (06/29-07/05)

本周新增 **48** 篇论文，**5** 篇附带代码。优先级：high 19 / medium 23 / low 6。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | high | ICML 2026 | [Dismantling Pathological Shortcuts: A Causal Framework for Faith...](http://arxiv.org/abs/2606.27596v1) | model steering | LVLM幻觉源于决策关键步骤中，特定风险注意力头脱离视觉证据锁定语言先验形成病理捷径，该方法... | 在推理阶段无监督定位引发幻觉的风险注意力中介，通过因果干预切断病理捷径，引导模型... | 仅验证了大视觉语言模型幻觉问题，该机制在其他大模型可靠性问题上的... | ✅ |
| 2 | high | - | [SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict...](http://arxiv.org/abs/2606.27786) | model steering | 仅训练不到0.01%参数的轻量门控模块，就能有效缓解RAG知识冲突，效果优于现有神经元修改类... | 添加轻量可学习门控模块，冻结主干模型，生成阶段自适应调制模型内部激活，平衡两类知... | 未量化评估该方法对模型通用能力的实际影响，缺乏大规模真实场景的可... | ✅ |
| 3 | high | ICML 2026 | [Search for Truth from Reasoning: A Dynamic Representation Editin...](http://arxiv.org/abs/2606.28589v1) | model steering | 真相在句子级编码且与推理模式纠缠，有效干预需定位早期高熵分支，朴素引导向量易损害正确轨迹 | 通过动态表示编辑解耦推理流形、提纯真值投影，监控前瞻熵，对推理轨迹做选择性引导与... | 仅在封闭域数学和编码任务验证，未探究开放域场景下的副作用与泛化可... | ✅ |
| 4 | high | - | [A Mechanistic View of Authority Hierarchy in LLM Sycophancy](http://arxiv.org/abs/2607.00415v1) | unlearning/safety | 权威诱导谄媚定位于模型晚期关键层，正确表征按权威等级被擦除，均值向量干预无效，仅能被思维链部... | 通过机制分析定位偏差发生位置，测试了均值向量干预、思维链推理对该偏差的逆转控制效... | 仅在三个中小开源模型上验证，结论在大模型上的泛化性有待验证 | — |
| 5 | high | - | [Auditing Forgetting in Limited Memory Language Models](http://arxiv.org/abs/2607.00605v1) | unlearning/safety | LMLM参数泄漏几乎为零，删除后残留事实占比0.7%~13.6%，主要来自近邻检索伪影，遗忘... | 通过因果审计框架定位删除式遗忘后残留事实的来源，提升遗忘效果评测的准确性与可靠性... | 遗忘边界依赖外部数据库管理，若数据库存在缺陷，删除后仍会残留敏感... | — |
| 6 | high | - | [Closing the Activation-Cone Blind Spot: Response-Time Probing an...](http://arxiv.org/abs/2606.29441v1) | model steering | 基于单层激活对齐的防御对预填充攻击存在结构盲区，响应时间探测在所有模型上AUROC可达0.9... | 对模型首个生成token的隐藏状态做线性探测，结合AlphaSteer的零空间引... | 结论仅适用于特定预填充模板族，对未知类型攻击的泛化能力未验证，落... | — |
| 7 | high | - | [Conditional Co-Ablation: Recovering Self-Repair Backups in Trans...](http://arxiv.org/abs/2607.01940v1) | other | 在GPT-2-small IOI电路中，CoAx将备份头恢复的ROC-AUC从0.33提升至... | 通过条件共消融干预识别Transformer电路中的自修复备份组件，提升组件归因... | 方法需要多轮顺序消融，计算开销较高，仅验证到7B规模模型，更大模... | — |
| 8 | high | - | [CreativityNeuro: Steering Language Model Weights to Improve Dive...](http://arxiv.org/abs/2607.01433v1) | model steering | 权重空间引导可泛化到未见过的开放任务，在DAT上最多提升14个人类百分位，激活引导不具备跨任... | 采用无数据的对比权重空间引导调整模型，无需重训练或梯度微调，实现提升发散思维、减... | 未评测该方法对模型原有通用能力的副作用，仅在创造力任务验证，跨领... | — |
| 9 | high | - | [EgoSafetyBench: A Diagnostic Egocentric Video Benchmark for Eval...](http://arxiv.org/abs/2607.00218v1) | evaluation/benchmark | 现有VLM易漏特定危险时刻，误导性场景标识可让最多三分之一危害被漏检，表观鲁棒性多为无差别报... | 通过构建诊断性评测基准暴露VLM安全防护缺陷，为改进运行时安全防护能力提供基准反... | 现有VLM安全防护易漏检真实危害也易过度干预，可靠性不足，难以满... | — |
| 10 | high | - | [Epistemic Goggles: A Pretrained Module that Induces an Epistemic...](http://arxiv.org/abs/2607.01690v1) | model steering | 添加预训练Goggles后，模型识别虚构内容正确率从9%升至91%，生成的认知框架可抵抗持续... | 通过预训练Goggles模块，在监督微调过程中编辑LoRA接收的梯度，为模型赋予... | 模块需针对基模型、框架、LoRA配置单独训练，适配成本高，跨配置... | — |
| 11 | high | - | [EvalSafetyGap: A Hybrid Survey and Conceptual Framework for LLM ...](http://arxiv.org/abs/2606.30219v1) | survey | 10个样本模型中，能力与持续对抗鲁棒性关联统计不显著（r=0.232，p=0.520），公开... | 通过构建统一的EvalSafetyGap概念框架，规范安全评估测量，提升对齐实践... | 现有安全评测依赖代理指标，无法反映真实安全属性，评测结果不可靠会... | — |
| 12 | high | - | [HARC: Coupling Harmfulness and Refusal Directions for Robust Saf...](http://arxiv.org/abs/2607.00572v1) | unlearning/safety | 越狱攻击会在prompt编码阶段提前抑制拒绝或有害性方向，不同攻击类在有害性-拒绝平面占据可... | 通过微调耦合prompt与响应位置残差流中的两个安全方向，仅干预目标子空间实现安... | 未披露具体评测基准，仅在有限模型上验证，大规模真实场景有效性待验... | — |

## A 会 / Venue 标签

- **ICML 2026**：4 篇

## 方法族分布

- **model steering**：18 篇
- **evaluation/benchmark**：12 篇
- **unlearning/safety**：5 篇
- **other**：5 篇
- **policy optimization**：2 篇
- **factuality benchmark**：1 篇
- **multi-agent coordination**：1 篇
- **survey**：1 篇
- **skill generation**：1 篇
- **tool-use control**：1 篇
- **agent harness**：1 篇

## 失败模式与风险信号

- 原有统计披露控制基于的事实上匿名假设已失效，出行数据隐私保护不足
- 强化学习后训练引发生成模型感知质量退化、速度范数膨胀
- 现有VLA基准对深度语言接地、组合指令理解的测试压力不足
- 大视觉语言模型生成物体幻觉，脱离视觉证据依赖语言先验生成内容。
- 现有研究碎片化，未联合建模多模态与时间社交交互信号，无法开展公平对比
- 推理复杂度提升后可靠性下降，表格与先验冲突时依赖预训练知识
- 现有方法灵活性不足，易引发灾难性遗忘，依赖历史旧知识访问，预处理成本高
- 参数知识与多源外部知识存在不一致冲突，现有方法只能偏向单一来源无法主动解决冲突。
- 大模型多跳推理幻觉、逻辑链断裂，过度结构复杂度导致推理性能退化
- 新旧事实同存于模型参数时，模型受原有参数影响输出过时错误答案

## 评测信号

- 可重识别目标中重识别成功率72%，总体案例成功率41.9%，单目标仅需数分钟数美元的攻击成本
- 所提方法可在完全保留原有奖励的前提下，稳定提升图像质量与真实感，在少步推理设置下增益更明显。
- 剪枝一半VLA的LLM模块可提升OpenVLA-OFT在LIBERO的任务成功率，仅保留两个语言块也能恢复基线性能。
- 该方法在抑制LVLM物体幻觉上达到SOTA，性能较基线SID提升29.1%，同时保留了模型原有的语言丰富度。
- 采用统一标准化评测协议，对比不同设置下的预测性能，分析各类因素对预测效果的影响。
- 通过对比模型在原始真实表和反事实修改表上的准确率差距，揭示模型依赖预训练先验而非给定表格的现象。
- 验证所提方法相比现有方法在终身知识编辑任务上的准确率优势，最高可实现14%的平均准确率提升。
- 实验结果表明所提MACR框架性能显著优于现有SOTA基线，显式冲突解决的输出结果具备可解释性。
- SCM-GRPO在两个基准数据集上准确率优于强基线，生成的多跳推理结构相比基线更具可追溯性。
- TAS可解决29%-57%的参数时间冲突，保留85%-99%非冲突准确率，四个评测模型中三个性能优于ITI基线

## 控制机制 / Harness 信号

- 本文仅验证智能体驱动的重识别威胁可行性，未提出模型或智能体的行为控制方案
- 在训练阶段向基础损失添加铰链惩罚，约束模型输出速度范数不超过参考范数，抑制质量退化同时保留奖励。
- 通过可控移除Transformer模块的干预方式，结合敏感度指标排序，再微调恢复，以此评估各模块的必要性。
- 在推理阶段无监督定位引发幻觉的风险注意力中介，通过因果干预切断病理捷径，引导模型生成更忠实的输出。
- 本文不涉及模型或Agent行为的控制改进，仅构建流行度预测基准与对应预测模型。
- 构建配对原始-反事实关系数据库基准，通过对比两类库的准确率差距度量模型回答的忠实度。
- 通过动态层选择结合零空间投影约束梯度更新方向，无需访问历史旧知识，实现更灵活的终身知识更新。
- 通过改进语义熵做知识置信度评估，再用分工多智能体推理显式检测并解决多源知识冲突。
- 通过结构因果建模锚定推理依赖，结合GRPO强化学习动态平衡推理结构深度与简洁性，提升推理可靠性。
- 推理测试阶段无需重训练，通过检测冲突、定位关键层，引导模型隐状态朝向新事实表示，选择性覆盖过时知识

## 可靠性 / 落地风险

- 现有出行数据隐私保护机制未覆盖智能体AI带来的新型重识别威胁，缺乏成熟应对方案
- 实验仅在图像生成流模型上验证，未在其他任务场景测试，方法泛化性尚未验证。
- 现有VLA过度分配容量给语言模块，带来不必要的计算成本，现有基准无法有效评测深度语言理解能力。
- 仅验证了大视觉语言模型幻觉问题，该机制在其他大模型可靠性问题上的通用性未知。
- 研究主题与LLM/Agent可靠性控制方向不匹配，无法为当前方向提供直接参考。
- 现有表格问答仅评测准确率未测忠实度，无法发现模型依赖先验的问题，下游应用结果不可靠。
- 未评测该方法在长期顺序编辑下的副作用，未验证极端场景下的编辑可靠性，存在潜在风险。
- 依赖多轮多智能体推理推理成本较高，未验证复杂真实场景下的方法泛化能力。
- 仅在两个封闭数据集完成验证，未测试开放场景，方法的泛化可靠性未得到充分验证。
- 仅在8B及以下参数模型验证，方法对更大规模模型及其他冲突类型的泛化性未知

## 代码资源

- [SHIFT: Gate-Modulated Activation Steering for Knowledge Conflict Mitigation in R...](https://github.com/OpenBMB/SHIFT.) · 8 stars
- [Dismantling Pathological Shortcuts: A Causal Framework for Faithful LVLM Decodin...](https://github.com/Cc2021start/Fox.) · 1 stars
- [Search for Truth from Reasoning: A Dynamic Representation Editing Framework for ...](https://github.com/tianlwang/DynaSteer.) · 1 stars
- [Surrogate Fidelity: When Can Open LLMs Explain Closed Ones?](https://github.com/facebookresearch/surrogate.) · 1 stars
- [Towards Robustness against Typographic Attack with Training-free Concept Localiz...](https://github.com/Liu-524/SamplingTAR.)

## 常见基线方法

- **NFT**：1 篇
- **AWM**：1 篇
- **DPO**：1 篇
- **推理时间速度重归一化校正**：1 篇
- **OpenVLA-OFT**：1 篇
- **未剪枝原VLA模型**：1 篇
- **SID**：1 篇
- **代表性现有流行度预测方法**：1 篇
- **现有终身知识编辑方法**：1 篇
- **传统二选一知识冲突处理方法**：1 篇

## 常用数据集

- **摘要未提及**：4 篇
- **锚定真实地址的模拟时空位置数据集**：1 篇
- **LIBERO**：1 篇
- **机器人操作基准**：1 篇
- **真实工业机器人场景**：1 篇
- **Bluesky平台数据集**：1 篇
- **Reddit平台数据集**：1 篇
- **ContraTable**：1 篇
- **多个知识冲突相关基准**：1 篇
- **HoVer**：1 篇

---
*自动生成于 2026-07-05 | ArXiv_Daily_Digest*