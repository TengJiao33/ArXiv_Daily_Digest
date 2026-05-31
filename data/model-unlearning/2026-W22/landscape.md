# 📡 模型遗忘与反知识编辑 — 方法版图
> 2026-W22 (05/25-05/31) | 本周 25 篇 | 自动生成

📊 **3** 个方法族 | **25** 篇 high priority | **6** 篇附带代码

---

### 🔬 unlearning（18 篇）

- **基于顺序无关规则并集的方案无跨请求干扰，可抑制目标知识同时保留效用，对转述、跨语言查询鲁棒。** ⭐
  _[ICCU: In-Context Continual Unlearning via Pattern-Induced Refusal...](http://arxiv.org/abs/2605.27138v1)_

  - 评测信号：验证了方法的遗忘效果、原模型效用保留、顺序请求可扩展性，以及对转述跨语言查询的鲁棒性。
  - 失败模式：跨请求干扰、顺序请求下模型效用损失累积
  - Idea hook：可探索结合大模型上下文理解能力优化拒绝规则诱导，提升大规模顺序遗忘场景的性能。

- **自适应连通共享与解耦优化器状态可有效缓解遗忘保留梯度冲突，量化变体降内存且不损失性能** ⭐ 💻
  _[DualOptim+: Bridging Shared and Decoupled Optimizer States for Be...](http://arxiv.org/abs/2605.21539v1)_

  - 评测信号：在虚构遗忘、真实遗忘、安全对齐、多任务学习多类任务上，验证不同目标间的性能权衡与内存开销
  - 失败模式：遗忘与保留目标梯度方向冲突，导致二者性能权衡效果不佳
  - Idea hook：可探索该框架在更大参数规模大模型上的适配性，以及更低量化精度下的遗忘性能表现

- **CIFAR-10狄利克雷划分下，HF-KCU比重训快47.75倍，精度仅差0.60%，遗忘集成员推理成功率0.499与重训一致** ⭐
  _[Causal Unlearning in Collaborative Optimization: Exact and Approx...](http://arxiv.org/abs/2605.20341v1)_

  - 评测信号：评测了方法加速比、模型测试精度、遗忘集成员推理成功率，验证了效率、精度和隐私恢复效果
  - 失败模式：数据删除后重训开销过高，遗忘更新易串扰影响无关客户端
  - Idea hook：可拓展研究异质联邦场景下大规模大模型的高效因果遗忘，适配生产环境异步删除需求

- **符号感知避冲突聚合可抑制削弱过往遗忘效果的冲突更新，在多场景多指标下均优于现有基线** ⭐
  _[CATA: Continual Machine Unlearning via Conflict-Averse Task Arith...](http://arxiv.org/abs/2605.18610v1)_

  - 评测信号：在单次遗忘和持续遗忘两种设置下，评测遗忘有效性、模型保真度与遗忘持续性三项核心指标
  - 失败模式：顺序更新中冲突更新削弱过往遗忘效果，导致已移除知识重新出现
  - Idea hook：可探索该冲突规避任务算术框架，如何适配更大规模多模态大模型的持续机器遗忘场景

- **在标准基准和多种MDLM主干上，所提MDU相比现有大语言模型遗忘方法取得了更高的遗忘性能** ⭐ 💻
  _[Machine Unlearning for Masked Diffusion Language Models](http://arxiv.org/abs/2605.18253v1)_

  - 评测信号：在标准基准与多种MDLM主干模型上开展实验，验证了所提方法的遗忘性能与隐私效用权衡
  - 失败模式：掩码扩散语言模型领域缺乏专用的机器遗忘方案
  - Idea hook：可进一步探索该框架在隐私数据遗忘、安全内容清除等实际场景下的适配与性能优化

- **能量指数可准确高效量化知识存在性、分隔待遗忘与保留知识，所提EUA性能显著优于现有两类遗忘方法。** ⭐
  _[Distinguishable Deletion: Unifying Knowledge Erasure and Refusal ...](http://arxiv.org/abs/2605.16776v1)_

  - 评测信号：通过大量实验对比现有两类方法，验证所提EUA方法在大模型知识遗忘任务上性能优于已有方法。
  - 失败模式：知识删除易产生偏置删除，拒绝范式遗忘不彻底，存在有害知识复现问题
  - Idea hook：可探索该能量边界统一框架在顺序遗忘、大规模多类敏感知识遗忘场景下的泛化能力。

- **通过带闭式解的乘法参数更新实现表征正交，可高效完成目标遗忘，性能优于现有基线且保留模型通用效用。** ⭐ 💻
  _[ZeroUnlearn: Few-Shot Knowledge Unlearning in Large Language Mode...](http://arxiv.org/abs/2605.18879v2)_

  - 评测信号：评测方法的遗忘效果与模型通用效用的保留能力，验证所提方法性能优于现有各类基线方法。
  - 失败模式：现有遗忘方法计算成本高，遗忘完成后易出现模型整体通用效用下降的问题。
  - Idea hook：可探索将这种带闭式解的表征正交编辑思路，扩展到大规模多样本场景的大模型知识遗忘中。

- **在Qwen3-VL上，仅用少量留存监督数据，ASRU平均遗忘效果提升24.6%，生成质量提升5.8倍，同时保留模型效用。** ⭐
  _[ASRU: Activation Steering Meets Reinforcement Unlearning for Mult...](http://arxiv.org/abs/2605.15687v1)_

  - 评测信号：同时评测遗忘效果、遗忘后生成质量与模型原有效用，关注三者之间的平衡表现。
  - 失败模式：遗忘后生成质量下降，易产生幻觉或僵化响应，模型原有效用受损
  - Idea hook：可尝试将该激活引导结合强化优化的遗忘框架推广到不同架构的多模态大模型中验证通用性。

- **现有基线的单参数更新幅度比NF4量化区间宽度小47-828倍，4位量化会系统性逆转遗忘效果** ⭐
  _[Forgetting That Sticks: Quantization-Permanent Unlearning via Cir...](http://arxiv.org/abs/2605.15138v1)_

  - 评测信号：从有效遗忘、保留性能、量化后间隙、结构擦除四个维度评测，梯度基线压缩后准确率最高回升0.05
  - 失败模式：量化后遗忘效果反弹，现有方法无法兼顾遗忘有效性与量化稳定性
  - Idea hook：可探索不同量化位宽下永久遗忘的实现边界，拓展该方法到大参数模型的安全遗忘场景

- **通过概念分解实现细粒度知识操控，在域内域外遗忘设置下，目标遗忘和非目标保留效果均优于现有方法** ⭐
  _[ICED: Concept-level Machine Unlearning via Interpretable Concept ...](http://arxiv.org/abs/2605.14309v2)_

  - 评测信号：在域内和域外两种遗忘设置下，评测目标遗忘完整性、非目标知识保留效果与模型整体效用
  - 失败模式：实例级遗忘存在串扰，移除目标知识时会损伤同图内的非目标语义
  - Idea hook：可探索将概念级遗忘框架推广到开放域场景，解决开放世界VLM多混杂概念的选择性遗忘问题

- **注入扰动构造的不可学习样本会令LVLM过拟合噪声，无扰动推理时下游性能下降，三种威胁模型均有效防护** ⭐
  _[To See is Not to Learn: Protecting Multimodal Data from Unauthori...](http://arxiv.org/abs/2605.14291v1)_

  - 评测信号：在六个数据集、九个开源大视觉语言模型测试，验证方法在白灰黑三种威胁模型下均有效、隐秘且鲁棒
  - 失败模式：现有多模态数据防护均为事后方案，仅能在侵权发生后发挥作用，无法提前防护
  - Idea hook：可探索将该主动不可学习思路拓展到大规模多模态模型，优化跨模型防护的迁移效率与效果

- **针对危险知识和毒性两种反学习任务设计差异化目标，可在四款7-8B开源模型上取得优异效果** ⭐
  _[Model Unlearning Objectives Vary for Distinct Language Functions](http://arxiv.org/abs/2605.26454)_

  - 评测信号：在四款7B-8B开源大语言模型上验证方法，证明差异化反学习目标适配不同任务的有效性
  - 失败模式：统一反学习目标无法适配不同语言功能的反学习需求
  - Idea hook：可探索更多语言任务的差异化反学习目标设计，构建分类型的通用模型反学习体系

- **现有遗忘方法仅优化表征主导分量，重学习中主导分量修改易被反转，次要分量抗反转性更强** ⭐
  _[Robust LLM Unlearning Against Relearning Attacks: The Minor Compo...](http://arxiv.org/abs/2605.11685)_

  - 评测信号：重点评测方法抵御重学习攻击的鲁棒性，验证其性能显著优于现有最优遗忘方法
  - 失败模式：现有遗忘方法抗重学习攻击能力弱，被遗忘知识易快速恢复
  - Idea hook：可探索将次要分量优化思路推广到各类大模型遗忘场景，进一步提升遗忘鲁棒性

- **GUARD-IT是唯一可在所有测试设置下同时保留效用、抑制记忆、避免崩溃，量化场景下仍保持有效** ⭐
  _[Inference-Time Machine Unlearning via Gated Activation Redirectio...](http://arxiv.org/abs/2605.12765)_

  - 评测信号：评测方法的遗忘效果、模型效用保留能力、持续遗忘性能，以及量化部署场景下方法的鲁棒性
  - 失败模式：原有梯度参数编辑计算成本高、不可逆，量化后性能衰减，全局激活引导易致模型行为异常
  - Idea hook：可将推理时激活重定向思路拓展到多轮连续遗忘场景，探索极端量化下遗忘与效用的平衡

- **ReVa在两轮交互后的遗忘集问答任务中，拒绝率接近次优方法的两倍，同时还提升了保留集的诚实性。** ⭐
  _[Unlearners Can Lie: Evaluating and Improving Honesty in LLM Unlea...](http://arxiv.org/abs/2605.08765)_

  - 评测信号：从效用、保留集诚实性、遗忘有效性等多维度，在问答和多选设置下展开评测。
  - 失败模式：现有遗忘方法存在幻觉、生成异常、行为不一致等不诚实问题，遗忘诚实性不达标
  - Idea hook：可探索将遗忘诚实性要求拓展到隐私遗忘、多轮遗忘场景，验证改进方法的通用性。

- **HFRU在物体识别与人脸身份任务中，遗忘和保留性能均超98%，引入的物体幻觉可忽略，显著优于前人方法。** ⭐ 💻
  _[Object Hallucination-Free Reinforcement Unlearning for Vision-Lan...](http://arxiv.org/abs/2605.08031)_

  - 评测信号：评测遗忘性能、知识保留性能与物体幻觉副作用，验证所提方法性能优于现有方法。
  - 失败模式：遗忘不彻底，遗忘后引入额外物体幻觉
  - Idea hook：可拓展到多模态大模型遗忘任务，进一步探索不同奖励设计对幻觉抑制的作用。

- **INT4量化可恢复已通过BF16合规审计模型的遗忘内容，恢复程度最高达22倍，存在FA-RA-Q-INT4三难困境。** ⭐
  _[DurableUn: Quantization-Induced Recovery Attacks in Machine Unlea...](http://arxiv.org/abs/2605.02196)_

  - 评测信号：评测多种遗忘方法在不同精度下的遗忘效果、模型效用与量化鲁棒性，验证所提方法的多指标均衡能力。
  - 失败模式：低比特量化部署会恢复已遗忘内容，导致机器遗忘的合规性失效
  - Idea hook：可进一步研究破解FA-RA-Q-INT4三难困境，实现兼顾遗忘、效用与量化鲁棒性的鲁棒遗忘。

- **token级选择可提升梯度信噪比，在两个基准三种架构上，遗忘效果和效用保留均优于序列级基线** ⭐
  _[Unlearning What Matters: Token-Level Attribution for Precise Lang...](http://arxiv.org/abs/2605.00364)_

  - 评测信号：在TOFU、WMDP两个基准、三种模型架构上，评测方法的遗忘有效性与模型效用保留能力
  - 失败模式：遗忘不彻底，模型原有保留能力下降
  - Idea hook：可探索将token级归因思路拓展到真实场景大模型遗忘，进一步提升遗忘的精准度与效率


### 🔬 evaluation/benchmark（6 篇）

- **反事实训练存在两个隐藏缺陷：反事实语料不一致引发知识冲突干扰优化，拟合虚假目标导致幻觉溢出升高无关领域幻觉率。** ⭐
  _[On the Hidden Costs of Counterfactual Knowledge Training in LLM U...](http://arxiv.org/abs/2605.27083v1)_

  - 评测信号：提出带新型权衡指标和梯度诊断工具的扩展基准RWKU+，聚焦大语言模型遗忘的隐藏成本与副作用。
  - 失败模式：反事实训练存在知识冲突干扰优化，以及幻觉溢出推高无关领域幻觉率
  - Idea hook：针对反事实知识训练的两大缺陷，可探索缓解知识冲突与幻觉溢出的改进型大语言模型遗忘方案。

- **BEAP相较已有方法攻击成功率提升超60%，单次成功攻击平均仅需15个提示，生成提示可绕过安全过滤。** ⭐
  _[Erased but Exploitable: Black-box Embedding-Aware Prompting Again...](http://arxiv.org/abs/2605.26332v1)_

  - 评测信号：评测攻击成功率、对抗提示隐蔽性与生成图像质量，验证了BEAP相较现有方法的性能提升。
  - 失败模式：现有针对已遗忘模型的恢复攻击实用性差，生成的对抗提示易被安全过滤检测。
  - Idea hook：可基于该攻击思路设计更鲁棒的文生图概念遗忘方法，提升遗忘后模型的安全防御能力。

- **在8种方法的150个模型评估中，UDS的忠实度鲁棒性为20种指标最高，擦除深度因样本而异** ⭐ 💻
  _[Measuring the Depth of LLM Unlearning via Activation Patching](http://arxiv.org/abs/2605.24614v1)_

  - 评测信号：在横跨8种遗忘方法的150个模型上验证，UDS的忠实度与鲁棒性优于20种对比指标，开放了代码
  - 失败模式：遗忘不彻底，残留知识隐藏于内部表征，现有评估指标缺乏通用性无法有效检测
  - Idea hook：可将UDS扩展到不同架构LLM的遗忘审计，探索不同遗忘方法的擦除深度分布规律

- **微调模型ECE约0.04远低于预训练模型的ECE>0.5，遗忘后模型保留低校准但对相关性token依赖提升** ⭐
  _[Calibration vs Decision Making: Revisiting the Reliability Parado...](http://arxiv.org/abs/2605.20915v1)_

  - 评测信号：同时从概率校准误差和决策规则的虚假关联依赖两个层面，评估遗忘后语言模型的可靠性
  - 失败模式：仅用校准误差衡量遗忘后模型可靠性，无法识别依赖虚假关联的不可靠决策
  - Idea hook：能否设计同时覆盖概率校准与决策规则可靠性的机器遗忘评估指标，提升可靠性判断准确性

- **发现了仅存在于多语言机器遗忘场景中、单语言机器遗忘不具备的特有独特现象。** ⭐
  _[Knowledge Beyond Language: Bridging the Gap in Multilingual Machi...](http://arxiv.org/abs/2605.14404v1)_

  - 评测信号：评估多语言遗忘的整体质量，以及不同语言对间信息移除的一致性，捕捉信息的跨语言分布特征。
  - 失败模式：现有多语言机器遗忘评估无法捕捉信息的跨语言分布，评估不准确
  - Idea hook：可基于本文提出的评估指标，探索提升多语言机器遗忘跨语言一致性的新方法。

- **该基准结合合法合成数据与系统视觉变化，可真实鲁棒地评估大视觉语言模型版权遗忘的泛化能力。** ⭐
  _[Erase Persona, Forget Lore: Benchmarking Multimodal Copyright Unl...](http://arxiv.org/abs/2605.03547)_

  - 评测信号：同时评估版权方视角的遗忘有效性与部署方视角的模型通用效用保留，衡量二者的关键权衡。
  - 失败模式：现有版权遗忘评估缺乏鲁棒性，无法捕捉跨模态概念擦除的细微差异。
  - Idea hook：可基于该基准开发兼顾版权遗忘效果与模型通用能力保留的高效多模态遗忘方法。


### 🔬 survey（1 篇）

- **现有多数VLM机器遗忘方法易被三种攻击攻破，已遗忘的知识可通过提示或重训重新激活** ⭐ 💻
  _[On the Robustness of Machine Unlearning for Vision-Language Model...](http://arxiv.org/abs/2605.26992)_

  - 评测信号：在多类提示设置下统一评估现有方法，通过三种攻击范式检验VLM机器遗忘的实际鲁棒性
  - 失败模式：遗忘不彻底，仅隐藏目标知识，已遗忘的知识可被重新激活
  - Idea hook：可基于本文提出的攻击范式，设计能抵抗知识重激活的鲁棒多模态机器遗忘方法


---
*Knowledge Editing Direction Radar 自动生成 | 2026-05-31*