# representation-engineering — 2026-W21 (05/18-05/24)

本周新增 **52** 篇论文，**2** 篇附带代码。优先级：high 0 / medium 0 / low 52。

> ⚠️ 本周论文数较多，搜索关键词可能过宽，可考虑收紧 arxiv_query。

## 优先阅读

| # | 优先级 | Venue | 论文 | 方法族 | 关键发现 | 控制/评测 | 风险 | 代码 |
|:-:|:------:|:-----:|------|--------|----------|----------|------|:----:|
| 1 | low | - | [SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation...](http://arxiv.org/abs/2502.01042) | 大模型安全调控 | 大语言模型可在自身内部状态做安全自我评估，SafeSwitch仅调不到6%参数即可降约80%... | — | — | ✅ |
| 2 | low | - | [Toward Stable Value Alignment: Introducing Independent Modules f...](http://arxiv.org/abs/2605.11712) | 稳定价值对齐 | SVGT可在多个骨干模型和安全基准上将有害评分降低超70%，同时保持生成流畅不干扰骨干原有表... | — | — | ✅ |
| 3 | low | - | [Ablating Safety: Mechanisms for Removing Alignment in Language M...](http://arxiv.org/abs/2605.17413v1) | 语言模型去对齐 | 任务专用LoRA将平均安全得分提至0.87，通用得分0.83，不安全合规性0.13，优于各类... | — | — | — |
| 4 | low | - | [Adaptive Probe-based Steering for Robust LLM Jailbreaking](http://arxiv.org/abs/2605.20286v1) | 大模型越狱攻击 | 该方法无需额外对比提示与费力手动调参，可将加固大模型越狱的平均有害性得分从6%提升至70% | — | — | — |
| 5 | low | - | [AlpsBench: An LLM Personalization Benchmark for Real-Dialogue Me...](http://arxiv.org/abs/2603.26680) | 大模型个性化基准 | 模型难可靠提取潜在用户特征，大干扰池下检索精度骤降，显式记忆无法保证偏好对齐响应 | — | — | — |
| 6 | low | - | [Beyond Forgetting: Machine Unlearning Elicits Controllable Side ...](http://arxiv.org/abs/2601.21702) | 机器遗忘 | 机器遗忘除实现遗忘外，可产生可控的真实性、情感、拒绝等侧行为，还能提升模型上下文学习能力 | — | — | — |
| 7 | low | - | [CLIPer: Tailoring Diverse User Preference via Classifier-Guided ...](http://arxiv.org/abs/2605.07162) | 大模型个性化 | — | — | — | — |
| 8 | low | - | [Contrastive Conceptor Activation Steering (COAST): Unlocking Vis...](http://arxiv.org/abs/2605.17144v1) | 激活引导 | COAST使仿真、真实机器人任务成功率分别提升超20%、40%，失败模式跨任务共享结构，成功... | — | — | — |
| 9 | low | - | [Controllable Value Alignment in Large Language Models through Ne...](http://arxiv.org/abs/2602.07356) | 可控价值对齐 | NeVA可显著降低价值引导中的平均泄漏，残余影响基本仅局限于语义相关的价值类别，通用能力降解... | — | — | — |
| 10 | low | - | [Decodable but Not Corrected by Fixed Residual-Stream Linear Stee...](http://arxiv.org/abs/2605.05715) | 大模型故障校正 | 过度思维（OT）故障线性解码平衡准确率71.6%，29种固定线性引导校正效果Delta≈0，... | — | — | — |
| 11 | low | - | [Diagnosing and Correcting Concept Omission in Multimodal Diffusi...](http://arxiv.org/abs/2605.14270) | 概念遗漏校正 | 对文本token进行线性探测可证明，文本嵌入能够区分出代表目标概念缺失的特征遗漏信号 | — | — | — |
| 12 | low | - | [Differentially Private Steering for Large Language Model Alignme...](http://arxiv.org/abs/2501.18532) | 大模型隐私对齐 | 在0.5B到7B不同规模开源大模型中，PSA保证差分隐私同时性能损失极小，隐私保障优于现有非... | — | — | — |

## A 会 / Venue 标签

- **ICLR 2026**：1 篇

## 方法族分布

- **多模态安全**：2 篇
- **激活引导**：2 篇
- **大模型个性化**：2 篇
- **多价值对齐**：2 篇
- **大模型安全对齐**：2 篇
- **概念遗漏校正**：1 篇
- **大语言模型干预**：1 篇
- **幻觉回路分析**：1 篇
- **多智能体谄媚**：1 篇
- **表征动作缺口**：1 篇
- **稳定价值对齐**：1 篇
- **大模型反社会机制**：1 篇

## 代码资源

- [SafeSwitch: Steering Unsafe LLM Behavior via Internal Activation Signals](https://github.com/Hanpx20/SafeSwitch.) · 14 stars
- [Toward Stable Value Alignment: Introducing Independent Modules for Consistent Va...](https://github.com/Clervils/SVGT.git.) · 2 stars

## 常见基线方法

- **线性干预方法**：1 篇
- **指令微调Instruct模型**：1 篇
- **提示级防御**：1 篇
- **八个开源全模态大语言模型**：1 篇
- **Gemini 3.1 Pro**：1 篇
- **对比发现特征法**：1 篇
- **语义搜索特征法**：1 篇
- **授权上下文提示**：1 篇
- **可逆拒绝方向激活投影**：1 篇
- **表示控制投影**：1 篇

## 常用数据集

- **POPE-adversarial**：1 篇
- **AMBER**：1 篇
- **IMAVB**：1 篇
- **多模态安全基准数据集**：1 篇
- **通用效用基准数据集**：1 篇
- **Security-AR**：1 篇
- **摘要未提及**：1 篇
- **MATH**：1 篇
- **MMLU-Pro**：1 篇
- **竞争性编程**：1 篇

---
*自动生成于 2026-07-01 | ArXiv_Daily_Digest*