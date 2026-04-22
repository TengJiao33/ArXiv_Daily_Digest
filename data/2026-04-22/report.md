# 🧪 ArXiv AI 日报

📅 **2026-04-22 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **60,465** (¥0.0196)

## 🔥 今日必读

---

### 1. UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling

🏷️ `cs.RO (机器人)` | 📄 [arXiv](http://arxiv.org/abs/2604.19734v1)

👤 Boyu Chen, Yi Chen, Lu Qiu 等


**中文标题**: UniT：面向人到仿人机器人策略学习与世界建模的统一物理语言
**背景与痛点**: 仿人机器人规模化训练受限于高质量机器人数据稀缺，海量低成本人类运动数据可作为补充，但体态结构差异带来的运动学错配形成跨体态鸿沟。现有方法依赖难扩展的手工动作重定向，纯动作/纯视觉表征存在分布偏移或外观噪声干扰，多模态方案也未实现真正的跨体态表征对齐。
**核心创新**: 基于「不同体态的相同物理意图会产生一致视觉结果」的核心洞察，提出基于视觉锚定的统一动作分词器UniT，将人类和仿人机器人的异构动作投影到体态无关的共享离散隐空间，作为统一接口同时支持策略学习与世界建模，可规模化复用海量人类知识。
**技术细节**: 设计视觉、动作、融合三个并行编码分支，采用共享残差量化码本将所有特征编码到统一离散空间。核心约束为双向交叉重构：所有分支的输出分词都需要同时重构未来视觉特征和原始动作块，强制异构动作按物理结果对齐到同一隐流形。下游适配出两类方案：VLA-UniT让视觉语言大模型预测统一token，再加轻量流匹配头生成本体动作；WM-UniT用UniT特征作为通用条件实现动作条件世界建模。
**实验结果**: 在RoboCasa仿真基准、DROID数据集和小鹏IRON真实仿人机器人上测试，全数据设置下VLA-UniT整体成功率比次优SOTA高11.7个百分点，10%小样本下性能接近全数据基线，验证了零样本跨任务迁移能力，世界建模任务中跨体态可控性也得到显著提升。

---

### 2. VLA Foundry: A Unified Framework for Training Vision-Language-Action Models

🏷️ `cs.RO (机器人)` | 📄 [arXiv](http://arxiv.org/abs/2604.19728v1) | 💻 [GitHub](https://github.com/TRI-ML/vla_foundry) ⭐149

👤 Jean Mercat, Sedrick Keh, Kushal Arora 等


**中文标题**: VLA Foundry：统一的视觉-语言-动作模型训练框架

**背景与痛点**: 现有开源视觉-语言-动作（VLA）机器人框架大多仅专注于下游动作训练阶段，上游LLM、VLM预训练与下游动作微调分散在互不兼容的代码栈中，耦合度高、灵活性差，无法支撑研究者系统探索上游数据配方、骨干架构对下游策略性能的影响。

**核心创新**: 核心贡献是推出了端到端统一的开源VLA训练框架，将LLM预训练、VLM预训练、VLA策略微调整合到共享数据抽象、训练逻辑的单代码库中，同时支持从零全流程训练和直接加载Hugging Face预训练骨干，模块化设计允许灵活替换任意组件，同步开放全套预训练权重与规范评估工具。

**技术细节**: 框架采用可嵌套继承的YAML配置+冻结数据类系统，基于注册机制实现模型、数据集的即插即用，支持加权混合多模态数据集，分布式训练基于FSDP2原生支持多节点多GPU，兼容云原生部署。针对机器人数据做了专项优化，支持多种归一化方案、SE(3)空间下绝对/相对动作表示、可配置时序动作窗口；VLA采用流匹配动作头，以VLM输出的观测token隐状态为条件生成动作序列。

**实验结果**: 在开源LBM Eval桌面双机械手操作仿真基准测试，完全从零训练的Foundry-VLA-1.7B多任务模型，性能与作者团队之前的闭源SOTA基线相当；基于预训练Qwen3-VL骨干的模型，成功率超出基线23个百分点，验证了更强VLM骨干可直接提升VLA策略能力。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Discovering a Shared Logical Subspace: Steering LLM Logical Reasoning via Alignm...](http://arxiv.org/abs/2604.19716v1) `cs.CL (计算语言学)` | 针对LLM多步逻辑推理能力不足的痛点，提出对齐自然语言与符号视图学习共享逻辑子空间，融合两类方法优势，为提升推理能力提供新思路 |
| 5 | [A Self-Evolving Framework for Efficient Terminal Agents via Observational Contex...](http://arxiv.org/abs/2604.19572v1) `cs.CL (计算语言学)` | 针对长视界多轮终端Agent上下文冗余的痛点，提出基于观测压缩的自进化框架，降低计算开销，适配长任务Agent落地需求，创新性解决Agent核心痛点 |
| 6 | [Micro Language Models Enable Instant Responses](http://arxiv.org/abs/2604.19642v1) `cs.CL (计算语言学)` | 针对可穿戴端侧设备算力功耗不足，无法持续运行现有小LLM的痛点，提出微语言模型方案实现边缘即时响应，解决端侧LLM部署的实际难题，实用性极强 |
| 7 | [Pause or Fabricate? Training Language Models for Grounded Reasoning](http://arxiv.org/abs/2604.19656v1) `cs.CL (计算语言学)` | 针对LLM输入不完整时容易编造虚假信息的问题，训练模型学会在信息不足时暂停输出而非虚构，从训练层面缓解幻觉风险，提升输出可靠性 |
| 8 | [An AI Agent Execution Environment to Safeguard User Data](http://arxiv.org/abs/2604.19657v1) `cs.CR (加密与安全)` | 针对AI Agent需要访问用户隐私数据带来的安全风险，提出专用的Agent执行环境来保障用户数据安全，解决Agent落地的核心安全痛点 |
| 9 | [SafetyALFRED: Evaluating Safety-Conscious Planning of Multimodal Large Language ...](http://arxiv.org/abs/2604.19638v1) 💻 `cs.AI (人工智能)` | 当前多模态大模型Agent缺乏安全规划能力的标准化评估基准，该工作推出SafetyALFRED基准填补空白，推动安全智能Agent领域研究 |
| 10 | [FASTER: Value-Guided Sampling for Fast RL](http://arxiv.org/abs/2604.19730v1) 💻 `cs.LG (机器学习)` | 针对现有高性能强化学习算法测试时采样多个动作候选成本过高的痛点，提出值引导采样方法加速RL推理，大幅降低部署成本，实用性强 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-22
