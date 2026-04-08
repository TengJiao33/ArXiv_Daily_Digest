# 🧪 ArXiv AI 日报

📅 **2026-04-08 周三** | 🤖 扫描/精选: **50/9**

> 📊 Tokens: **56,905** (¥0.0186)

## 🔥 今日必读

---

### 1. Gym-Anything: Turn any Software into an Agent Environment

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.06126v1)

👤 Pranjal Aggarwal, Graham Neubig, Sean Welleck


**中文标题**: Gym-Anything：将任意软件转化为智能体环境
**背景与痛点**: 当前计算机使用智能体（CUA）研究多集中在短视野、低经济价值的消费级软件任务，核心痛点是为复杂专业软件构建可交互环境需要大量专家人力，无法规模化，导致现有基准评估脱离实际，也缺乏足够多样的长视野训练数据，限制了真实场景CUA技术发展。
**核心创新**: 将环境构建本身转化为多智能体任务，通过AI自动完成任意软件的环境搭建、配置与验证，突破了手动构建环境的规模化瓶颈，基于GDP数据构建了覆盖所有22个主要职业大类的大规模真实基准CUA-World，填补了高经济价值长视野任务的基准空白。
**技术细节**: 首先基于GDP数据分层筛选，从万余个候选中选出200个覆盖全职业、可沙箱运行的高经济价值软件；框架将每个环境标准化为三段安装配置脚本加声明式配置文件，核心采用创建-审核多智能体循环：创建智能体编写脚本、下载真实领域数据、生成运行证据，独立审核智能体按质量清单验证，共享记忆积累经验加速后续构建；任务采用种子放大生成，结合特权 ground truth 的VLM检查表完成自动验证。
**实验结果**: 基于CUA-World训练轨迹蒸馏的2B参数视觉语言模型，性能超过两倍大小的原生4B模型，性能随训练数据规模对数线性提升，对未见过的软件具备泛化能力；长视野子集CUA-World-Long极具挑战，最强前沿模型仅27.5%通过率，测试时审核可将Gemini 3 Flash通过率从11.5%提升至14%。

---

### 2. In-Place Test-Time Training

🏷️ `cs.LG (机器学习)` | 📄 [arXiv](http://arxiv.org/abs/2604.06169v1)

👤 Guhao Feng, Shengjie Luo, Kai Hua 等


**中文标题**: 原位测试时训练（In-Place TTT）
**背景与痛点**: 当前大模型普遍采用训练后固定权重部署的静态范式，无法在推理时动态适配流式输入的新上下文信息。测试时训练（TTT）虽提出通过推理时更新快权重解决该问题，但现有方法存在架构不兼容预训练模型、计算效率低、优化目标不匹配自回归语言建模的核心痛点。
**核心创新**: 本文提出In-Place TTT框架，核心思路是复用Transformer中已有MLP模块作为快权重载体，而非新增专用模块，实现了对现有预训练大模型的即插即用增强；同时设计了对齐下一词预测任务的优化目标，支持大分块并行计算，兼顾性能与部署效率。
**技术细节**: 具体实现上，将门控MLP的输入投影、门控权重保留为预训练慢权重，仅将MLP最终输出投影矩阵作为推理时可动态更新的快权重；序列分块处理，每块先使用当前快权重输出，再更新快权重供后续块使用。优化目标改用一维卷积提取未来token信息做监督，理论证明该目标能明确提升正确下一词的输出概率，还可通过前缀和实现原生上下文并行。
**实验结果**: 在RULER长上下文基准、Pile等多数据集验证，对Qwen3、LLaMA3.1等预训练模型增强后，64k以上长上下文性能稳定提升，128k上下文准确率提升超2个点；从头预训练也优于现有同类TTT和高效注意力方法，额外计算开销可忽略。


---

## 📋 同样值得关注

| # | 论文 | 推荐理由 |
|:-:|---|---|
| 4 | [Claw-Eval: Toward Trustworthy Evaluation of Autonomous Agents](http://arxiv.org/abs/2604.06132v1) `cs.AI (人工智能)` | 针对现有自主Agent评测存在的三大核心缺陷，推出Claw-Eval可信评测框架，提升Agent评测可靠性，推动自主Agent领域规范化发展 |
| 5 | [HaloProbe: Bayesian Detection and Mitigation of Object Hallucinations in Vision-...](http://arxiv.org/abs/2604.06165v1) `cs.CV (计算机视觉)` | 针对大视觉语言模型的物体幻觉问题，提出贝叶斯检测与缓解方案，弥补现有方法依赖模型自输出的缺陷，大幅提升多模态生成可靠性 |
| 6 | [PoM: A Linear-Time Replacement for Attention with the Polynomial Mixer](http://arxiv.org/abs/2604.06129v1) 💻 `cs.CV (计算机视觉)` | 提出线性复杂度的多项式混合器PoM，可作为自注意力的开箱即用替换方案，降低大模型训练推理成本，效率优化方向有重要创新 |
| 7 | [Paper Circle: An Open-source Multi-agent Research Discovery and Analysis Framewo...](http://arxiv.org/abs/2604.06170v1) 💻 `cs.CL (计算语言学)` | 针对科研文献爆炸增长、研究者难高效发现分析文献的痛点，推出开源多Agent科研辅助框架，帮助研究者高效梳理领域工作，实用性强 |
| 8 | [Exclusive Unlearning](http://arxiv.org/abs/2604.06154v1) `cs.CL (计算语言学)` | 针对工业LLM落地中合规性遗忘有害内容的需求，提出专属遗忘方案，解决现有机器删除方法适配性差的问题，工业落地价值高 |
| 9 | [How LLMs Follow Instructions: Skillful Coordination, Not a Universal Mechanism](http://arxiv.org/abs/2604.06015v1) `cs.AI (人工智能)` | 针对LLM指令遵循机制不清晰的核心问题，研究发现指令遵循是技能协调而非通用机制，深化了对指令调谐的基础认知，启发后续研究 |
| 10 | [Flowr -- Scaling Up Retail Supply Chain Operations Through Agentic AI in Large S...](http://arxiv.org/abs/2604.05987v1) `cs.AI (人工智能)` | 针对大型连锁超市零售供应链大量人工流程低效的痛点，推出基于智能体AI的Flowr方案，落地实际运营场景降本增效，工业应用价值高 |

---

🧪 ArXiv Daily Digest | 扫描 cs.CL / cs.AI / cs.LG | 2026-04-08
