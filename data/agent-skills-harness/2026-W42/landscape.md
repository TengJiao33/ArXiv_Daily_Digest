# 📡 Agent Skills 与 Harness — 方法版图
> 2026-W42 (10/12-10/18) | 本周 210 篇 | 自动生成

📊 **2** 个方法族 | **1** 篇 high priority | **20** 篇附带代码

---

### 🔬 tool-use control（1 篇）

- **现有主流代码Agent跨会话技能组合攻击成功率达46.7%-77.4%，所提防御可将其降至10.9%。** ⭐
  _[Understanding and Mitigating Cross-Session Attacks via Persistent...](http://arxiv.org/abs/2610.13227v1)_

  - 评测信号：所提防御将整体攻击成功率从69.5%降至10.9%，同时将合法任务完成率从79.6%提升至87.5%。
  - 控制机制：通过恢复工件来源上下文，增加预执行审查环节，保留agent最终执行决策权，防御跨会话攻击。
  - 评测环境：SkillRelayBench，指标为攻击成功率、攻击链成功率、合法任务完成率
  - 失败模式：跨会话持久工件导致恶意效应跨技能执行传播，引发各类安全后果
  - 可靠性风险：未防护的跨会话持久工件引入隐蔽攻击面，恶意攻击可影响智能体后续正常执行，带来安全隐患。


### 🔬 未分类（209 篇）

- **提取失败**
  _[X-AgentRed: Red-Teaming Personal Agents in Evolving Multi-Service...](http://arxiv.org/abs/2610.13886v1)_


- **提取失败**
  _[A Baseline Assessment for the Agentic Web Technology Stack](http://arxiv.org/abs/2610.13703v1)_


- **提取失败**
  _[A-SAW: The Agentic Software Architecture Workflow](http://arxiv.org/abs/2610.13647v1)_


- **提取失败**
  _[MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynami...](http://arxiv.org/abs/2610.13534v1)_


- **提取失败**
  _[Humanize MLE Agents: Multi-Agent Session Alternation Beyond Singl...](http://arxiv.org/abs/2610.13494v1)_


- **提取失败** 💻
  _[Proactive Agentic Orchestration](http://arxiv.org/abs/2610.13485v1)_


- **提取失败** 💻
  _[Rollout-Time Intervention: Unlocking Agentic Reinforcement Learni...](http://arxiv.org/abs/2610.13438v1)_


- **提取失败**
  _[ProgramGym: Scaling Training Environments for Long-Horizon Progra...](http://arxiv.org/abs/2610.13395v1)_


- **提取失败**
  _[AgentSWE: Can Coding Agents Build the Agent You Actually Want?](http://arxiv.org/abs/2610.13361v1)_


- **提取失败** 💻
  _[AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents](http://arxiv.org/abs/2610.13335v1)_


- **提取失败**
  _[Masked Diffusion Language Agents for Tool-Integrated Chemical Rea...](http://arxiv.org/abs/2610.13330v1)_


- **提取失败**
  _[JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolvin...](http://arxiv.org/abs/2610.13194v1)_


- **提取失败**
  _[RoleWorld: Knowledge Transfer in World Modeling with Functional R...](http://arxiv.org/abs/2610.13172v1)_


- **提取失败**
  _[Scaling Agentic Data for Long-Horizon Terminal Intelligence](http://arxiv.org/abs/2610.13166v1)_


- **提取失败**
  _[SOAR: Source-Aware Reinforcement Learning with Precise Credit Ass...](http://arxiv.org/abs/2610.13157v1)_


- **提取失败**
  _[Quality, Not Just Outcome: A Structural Scoring Framework for Sel...](http://arxiv.org/abs/2610.13152v1)_


- **提取失败** 💻
  _[DRYLAB-Bench: Benchmarking the Biosecurity Risk of Agentic LLM Mu...](http://arxiv.org/abs/2610.13116v1)_


- **提取失败**
  _[When Faster Decisions Do Not Make Better Agents: An Empirical Stu...](http://arxiv.org/abs/2610.13092v1)_


- **提取失败**
  _[LongHarness: Advancing Agentic Reasoning over 100M-Token Corpora ...](http://arxiv.org/abs/2610.13075v1)_


- **提取失败**
  _[CB-Orchestrator: Adaptive Workflow Optimization for LLM Agents vi...](http://arxiv.org/abs/2610.13064v1)_


- **提取失败**
  _[Evo$^2$: Evolving the Evolver through Weight-Harness Co-Evolution](http://arxiv.org/abs/2610.13025v1)_


- **提取失败**
  _[Don't Guess, Just Ask: Evaluating Interactive Requirement Clarifi...](http://arxiv.org/abs/2610.13022v1)_


- **提取失败**
  _[EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving ...](http://arxiv.org/abs/2610.13021v1)_


- **提取失败**
  _[Scaling Empowered Agents](http://arxiv.org/abs/2610.13002v1)_


- **提取失败** 💻
  _[Work2Skill: Capturing Human GUI Experience for Reusable Agent Ski...](http://arxiv.org/abs/2610.12984v1)_


- **提取失败**
  _[JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learni...](http://arxiv.org/abs/2610.12957v1)_


- **提取失败**
  _[TreeHCA: Hindsight-Guided Exploration and Credit Assignment for M...](http://arxiv.org/abs/2610.12828v1)_


- **提取失败**
  _[AgentPersonaBench: Benchmarking Persona-Driven User Simulation](http://arxiv.org/abs/2610.04379)_


- **提取失败**
  _[MedImageOSWorld: Benchmarking GUI Agents for Medical Image Consol...](http://arxiv.org/abs/2610.04800)_


- **提取失败**
  _[When to Compile a Computer-Use Agent? Measuring Payback and Makin...](http://arxiv.org/abs/2610.02932)_


- **提取失败**
  _[Co-Modifying Application Code and Deployment Infrastructure: A Ca...](http://arxiv.org/abs/2610.12849)_


- **提取失败**
  _[SCCGBench: Executability-Oriented Evaluation for Real-World Web S...](http://arxiv.org/abs/2610.12920)_


- **提取失败**
  _[TestSuiteBench: Coding Agents Struggle to Generate Strong Test Su...](http://arxiv.org/abs/2610.13065)_


- **提取失败**
  _[Evaluating LLM Creativity through Long-Tail Performance](http://arxiv.org/abs/2610.12998)_


- **提取失败**
  _[Travel Back To Move Forward: Retrospective Exploration and Evolvi...](http://arxiv.org/abs/2610.13058)_


- **提取失败**
  _[Beyond Binary Verifiable Rewards: Behavioral Self-Rewarding for S...](http://arxiv.org/abs/2610.12598)_


- **提取失败**
  _[BDD-Bench: A Behavior-Driven Benchmark for Coding Agents across t...](https://www.semanticscholar.org/paper/ce9fc8c3c10f819c881e2e7a7b9b1594f78f7279)_


- **提取失败**
  _[Whose Oracle Is It? The Authority Problem in Deployed Agentic Pro...](https://www.semanticscholar.org/paper/2ccce93d6f9144e0a4826e53482c41e893d98d28)_


- **提取失败**
  _[Toward Trace-Guided Automated Program Repair](https://www.semanticscholar.org/paper/b2ce02a1485d07fe828f932b9f4e6782ab358ac3)_


- **提取失败**
  _[Ranking Is Not Authority: Executable Context-Routing Contracts fo...](https://www.semanticscholar.org/paper/65f6b51496727d5a8f3dc676ddae60a9a9977d49)_


- **提取失败**
  _[Before the First Model Call: Factorizing Token Alignment and Cue ...](https://www.semanticscholar.org/paper/7cb085ed519905ba6ba43fd7dd08d17b586212c6)_


- **提取失败**
  _[From Statistical Code Generation to Correct-by-Construction AI Pr...](https://www.semanticscholar.org/paper/e8094ac42279ccf6a2111a896e5222a7c390ea06)_


- **提取失败**
  _[Evaluating Symbolic Feedback Granularity for LLM-Based Program Re...](https://www.semanticscholar.org/paper/44b78199912126b3397d8fa663fda10326b87a51)_


- **提取失败**
  _[Evaluating Low-Shot Procedural Skill Transfer in Language-Agent D...](https://www.semanticscholar.org/paper/2a5494ba978069f0749d524939aada8064e9fc7f)_


- **提取失败**
  _[LLM Agents as Resilience Engineers for Scientific Applications](http://arxiv.org/abs/2610.11260)_


- **提取失败**
  _[BrickBench: Evaluating Agentic Brick Design](http://arxiv.org/abs/2610.12452)_


- **提取失败**
  _[Autonomous Code Migration for Quantum Programming Languages: A Ca...](http://arxiv.org/abs/2610.12187)_


- **提取失败**
  _[Evaluating Local Language Model Agents for Reproducible Data Engi...](http://arxiv.org/abs/2610.11482)_


- **提取失败**
  _[PolyCodeEval: Benchmarking Multilingual Code Generation from Func...](http://arxiv.org/abs/2610.11618)_


- **提取失败**
  _[Which Skill to Distill? SGUID: Selecting a Compact Skill Bank for...](http://arxiv.org/abs/2610.12367)_


- **提取失败**
  _[Leakage-Resistant Evaluation of AI-Generated Database Specificati...](http://arxiv.org/abs/2610.12778)_


- **提取失败**
  _[SWE-Duel: Towards a Self-Scaling Arena for Coding Agents](http://arxiv.org/abs/2610.12569)_


- **提取失败**
  _[Recurrent Harness for Agentic Continual Learning](http://arxiv.org/abs/2610.12668)_


- **提取失败**
  _[MADS: Multi-Agent Dialog Simulation for Robust Conversational Age...](http://arxiv.org/abs/2610.12757)_


- **提取失败**
  _[Listen-to-Reason: Listen with Experts, Retrieve over a Graph, Rea...](http://arxiv.org/abs/2610.10749)_


- **提取失败**
  _[Semantic Behavioral Watermarking: Paraphrase-Robust and Forgery-R...](http://arxiv.org/abs/2610.08668)_


- **提取失败**
  _[The Model Plants the Trigger: Answer-Side Backdoor Attacks in Mul...](http://arxiv.org/abs/2610.07723)_


- **提取失败** 💻
  _[Not Every Call Needs a Frontier Model: Per-Call-Site Evaluation o...](http://arxiv.org/abs/2610.09021)_


- **提取失败**
  _[Turnslide: Scalable Multi-Turn Data Synthesis by Walking a Finite...](http://arxiv.org/abs/2610.07070)_


- **提取失败**
  _[Tev: Scaling Long-Horizon Agentic Environments with Dense Progres...](http://arxiv.org/abs/2610.18868v1)_


- **提取失败**
  _[The Last Remote Sensing Model Built by Humans? Casting Any Earth ...](http://arxiv.org/abs/2610.18845v1)_


- **提取失败** 💻
  _[Self-Evolving Agent Harness](http://arxiv.org/abs/2610.18813v1)_


- **提取失败** 💻
  _[SkillScaffold: Scaffolding Agentic Reinforcement Learning with Po...](http://arxiv.org/abs/2610.18807v1)_


- **提取失败**
  _[SEAR: Self-Evolving Agentic Robotics](http://arxiv.org/abs/2610.18792v1)_


- **提取失败**
  _[BLADE: Auditing Information Use for Failure Attribution in LLM Mu...](http://arxiv.org/abs/2610.18780v1)_


- **提取失败**
  _[Knowledge Graphs as Files: An Agent Harness Where Tool Creation a...](http://arxiv.org/abs/2610.18616v1)_


- **提取失败**
  _[Legal-R1: Agentic Retrieval for Evidence-Based Legal Reasoning](http://arxiv.org/abs/2610.18611v1)_


- **提取失败**
  _[Reading Right, Acting Wrong: Diagnosing Decision Failures of Syst...](http://arxiv.org/abs/2610.18579v1)_


- **提取失败**
  _[Lost in Implicit Routing: How LLM Agents Fail to Load Relevant Sk...](http://arxiv.org/abs/2610.18522v1)_


- **提取失败**
  _[Towards Safe Autonomy for Computer Use](http://arxiv.org/abs/2610.18508v1)_


- **提取失败**
  _[The Last Mile of Coding Agents for Long-Document Tasks: An Empiri...](http://arxiv.org/abs/2610.18507v1)_


- **提取失败**
  _[Delegating Earth science model calibration to knowledge-guided LL...](http://arxiv.org/abs/2610.18378v1)_


- **提取失败**
  _[Urbex: Agentic Spatial Grounding for City-Scale 3D Scenes](http://arxiv.org/abs/2610.18356v1)_


- **提取失败**
  _[Let the Mind Conceive, Let the Hand Achieve: Following Multimodal...](http://arxiv.org/abs/2610.18352v1)_


- **提取失败**
  _[Jev-Guard: Fast Routing and Auditing Agent Actions over Editable ...](http://arxiv.org/abs/2610.18326v1)_


- **提取失败**
  _[Encrypted Skills Can Become New Security Exploits If AI Agents Kn...](http://arxiv.org/abs/2610.18262v1)_


- **提取失败**
  _[Holding Agents Accountable with Verifiable Agent Insurance](http://arxiv.org/abs/2610.18230v1)_


- **提取失败**
  _[APT: Feedback-Driven Agentic Post-Training for Text-to-Image Gene...](http://arxiv.org/abs/2610.18097v1)_


- **提取失败**
  _[LifeSearch: Benchmarking Deep Research Agents for Real-World Life...](http://arxiv.org/abs/2610.18092v1)_


- **提取失败** 💻
  _[AM-Bench: Understanding Agents under Task Underspecification acro...](http://arxiv.org/abs/2610.18090v1)_


- **提取失败**
  _[ResearchFlow-Eval: Tracing the Execution Gap in End-to-End Multi-...](http://arxiv.org/abs/2610.18088v1)_


- **提取失败**
  _[AReaL-RSI: Adaptive Scaling and Coordination of Recursive Self-Im...](http://arxiv.org/abs/2610.18083v1)_


- **提取失败**
  _[From Agents to Edges: Paired Optimization for Multi-Agent Collabo...](http://arxiv.org/abs/2610.18069v1)_


- **提取失败**
  _[WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursi...](http://arxiv.org/abs/2610.18067v1)_


- **提取失败**
  _[LADDER: A Long-Horizon Robot Manipulation Benchmark](http://arxiv.org/abs/2610.18053v1)_


- **提取失败**
  _[FRACTION: Fraud Explanation Generation via Agentic Graph Context ...](http://arxiv.org/abs/2610.18023v1)_


- **提取失败** 💻
  _[Agent-Reflex: Teaching Language Agents to Act Reflectively](http://arxiv.org/abs/2610.17953v1)_


- **提取失败**
  _[State-Aware Generation of Deployable Websites from Visual Prototy...](http://arxiv.org/abs/2610.17861v1)_


- **提取失败**
  _[SchemaFill: Efficient LLM Tool Calling via Slot-Parallel Speculat...](http://arxiv.org/abs/2610.07086)_


- **提取失败**
  _[PhySGA: A Physics-Space Grounded Agentic Framework for Generaliza...](http://arxiv.org/abs/2610.20560v1)_


- **提取失败**
  _[AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents](http://arxiv.org/abs/2610.20474v1)_


- **提取失败**
  _[Same Claim, Different Interpretations: How LLM Agents Resolve Amb...](http://arxiv.org/abs/2610.20457v1)_


- **提取失败**
  _[Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineerin...](http://arxiv.org/abs/2610.20344v1)_


- **提取失败**
  _[TreeFlex: Agents Navigating Their Own Search Trees](http://arxiv.org/abs/2610.20334v1)_


- **提取失败**
  _[Reflect After Failure: Brain-Inspired Self-Evolving Agents for Em...](http://arxiv.org/abs/2610.20312v1)_


- **提取失败**
  _[Harness Policy Distillation: Aligning Agent Policies with Runtime...](http://arxiv.org/abs/2610.20261v1)_


- **提取失败**
  _[Long-Horizon RL Needs Muon](http://arxiv.org/abs/2610.20256v1)_


- **提取失败**
  _[P2Patch: Exploit-Guided Vulnerability Repair](http://arxiv.org/abs/2610.20245v1)_


- **提取失败**
  _[Task-State Governance: A Virtual Machine for Verifiable and Recov...](http://arxiv.org/abs/2610.20100v1)_


- **提取失败**
  _[CoRedSkill: Stealthy Skill Composition Attacks via AST-Guided Inj...](http://arxiv.org/abs/2610.20049v1)_


- **提取失败**
  _[Memorizing Who, Knowing How: Benchmarking Personal and Procedural...](http://arxiv.org/abs/2610.20022v1)_


- **提取失败**
  _[What Coding Agents Leave Unsaid: Measuring Task-State Gaps Betwee...](http://arxiv.org/abs/2610.20003v1)_


- **提取失败**
  _[A Strong Harness Narrows the Model Gap: A Comparative Evaluation ...](http://arxiv.org/abs/2610.19999v1)_


- **提取失败**
  _[AtomSearch: Evidence-Grounded Tree Search for Agent Skill Optimiz...](http://arxiv.org/abs/2610.19951v1)_


- **提取失败**
  _[When Non-Adversarial Noise Hurts Learning: Benchmarking Skill Sel...](http://arxiv.org/abs/2610.19910v1)_


- **提取失败**
  _[How GUI Agents Fail: GraceBench for Execution Stability Diagnosis](http://arxiv.org/abs/2610.19900v1)_


- **提取失败**
  _[LAGO: Language Agents with Reusable Growing Options](http://arxiv.org/abs/2610.19843v1)_


- **提取失败**
  _[EGCForest: Structured Agent Memory Organization for Enterprise Gr...](http://arxiv.org/abs/2610.19836v1)_


- **提取失败**
  _[Teaching Agents in their Own Style: Blackbox Teacher Distillation...](http://arxiv.org/abs/2610.19834v1)_


- **提取失败**
  _[ActionOPD: Distilling Decisions, Not Tokens](http://arxiv.org/abs/2610.19820v1)_


- **提取失败**
  _[One Monitor Does Not Fit All: Formalism-Agnostic Runtime Verifica...](http://arxiv.org/abs/2610.19818v1)_


- **提取失败**
  _[Calibration and Risk-Budgeted Decisions with System One Models](http://arxiv.org/abs/2610.19811v1)_


- **提取失败**
  _[ReproBAIT: Can coding agents build their own biological AI tools?](http://arxiv.org/abs/2610.19810v1)_


- **提取失败**
  _[Evolve Together, Fall into Place: How Social Scaffolding Shapes S...](http://arxiv.org/abs/2610.19799v1)_


- **提取失败**
  _[PRISMATIC : Prescription Risk Inspection System for Multi-Agent T...](http://arxiv.org/abs/2610.19762v1)_


- **提取失败**
  _[J-tau: A Fully Localized Japanese Benchmark for Tool-Agent-User I...](http://arxiv.org/abs/2610.19638v1)_


- **提取失败**
  _[JevCoder: When Does Decision Delegation Pay Off in Code Repair?](http://arxiv.org/abs/2610.19596v1)_


- **提取失败**
  _[L3M: A Verifiable Harness and Runtime for Self-Extending and Self...](http://arxiv.org/abs/2610.19591v1)_


- **提取失败**
  _[LLMA-UML: Extending the UML for Modeling LLM-Agent Systems](https://www.semanticscholar.org/paper/05ee1b684494b03d7e517d0b0f6bbf925cf98f91)_


- **提取失败**
  _[LIBERO-PeRM: Benchmarking Personalized Robotic Manipulation](http://arxiv.org/abs/2610.22372v1)_


- **提取失败**
  _[FDE-Gym: The Last Mile of AI Delivery](http://arxiv.org/abs/2610.22350v1)_


- **提取失败**
  _[MLExpert: Towards a Generalist Agentic Model for Autonomous Machi...](http://arxiv.org/abs/2610.22344v1)_


- **提取失败**
  _[3DCodeVerse: Exploring 3D Worlds as Code](http://arxiv.org/abs/2610.22341v1)_


- **提取失败**
  _[A team of Gemini 4 Argon agents beats Minecraft](http://arxiv.org/abs/2610.22319v1)_


- **提取失败**
  _[Learning to Steer LLM Agents and Multi-Agent Systems](http://arxiv.org/abs/2610.22316v1)_


- **提取失败**
  _[Improving Environment-Agnostic Coding Agents: The Role of Scaffol...](http://arxiv.org/abs/2610.22289v1)_


- **提取失败**
  _[Librarian Agents: Training LLMs to Curate Long-Context Workspaces...](http://arxiv.org/abs/2610.22273v1)_


- **提取失败**
  _[Shortcut Sensitivity in Agent-Safety Evaluations](http://arxiv.org/abs/2610.22243v1)_


- **提取失败**
  _[OS-Helix: Unifying GUI Interaction and Code Execution in Native C...](http://arxiv.org/abs/2610.22234v1)_


- **提取失败**
  _[Architecting for Hardware Diversity: Meta's End-to-End Co-Design ...](http://arxiv.org/abs/2610.22230v1)_


- **提取失败**
  _[HTN-Orchestrate: A Hierarchical Task Network Framework for Multi-...](http://arxiv.org/abs/2610.22195v1)_


- **提取失败**
  _[PROBE: Learning to Audit Policy Compliance in Tool-Using LLM Agen...](http://arxiv.org/abs/2610.22124v1)_


- **提取失败**
  _[FAOPs: Normal Forms and an Algebra for AI Agent Workflows](http://arxiv.org/abs/2610.22061v1)_


- **提取失败**
  _[Priming Base Models for Agentic Post-Training: An Open Midtrainin...](http://arxiv.org/abs/2610.22019v1)_


- **提取失败**
  _[CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving ...](http://arxiv.org/abs/2610.21910v1)_


- **提取失败** 💻
  _[RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Met...](http://arxiv.org/abs/2610.21791v1)_


- **提取失败**
  _[DeciCAD: Harness-Grounded Learning of Action Policies for CAD Age...](http://arxiv.org/abs/2610.21755v1)_


- **提取失败**
  _[The Self-Improvement Problem](http://arxiv.org/abs/2610.21646v1)_


- **提取失败**
  _[Rethinking the Role of Tool Graph Memory in Multi-Turn Tool Use](http://arxiv.org/abs/2610.21571v1)_


- **提取失败**
  _[DialFork: Going Beyond Factuality to Evaluate Procedural Hallucin...](http://arxiv.org/abs/2610.21561v1)_


- **提取失败**
  _[Agent Status Protocol (ASP): A Lightweight Specification for Stat...](http://arxiv.org/abs/2610.21538v1)_


- **提取失败**
  _[ISW-Agent: Integrating LLM-Driven Dialogue with n8n Workflow for ...](http://arxiv.org/abs/2610.21502v1)_


- **提取失败**
  _[MetaExp: Learning to Self-Improve through Experience via Verifiab...](http://arxiv.org/abs/2610.21492v1)_


- **提取失败**
  _[Incentivizing Tool-Use Reinforcement Learning for Post-Arrival Em...](http://arxiv.org/abs/2610.21449v1)_


- **提取失败**
  _[Do Agents Need a New Kind of Paper? SPRA: Structured Paper Repres...](http://arxiv.org/abs/2610.21424v1)_


- **提取失败** 💻
  _[JevAgentHarness: Benchmarking, Deploying and Training Decision Mo...](http://arxiv.org/abs/2610.21412v1)_


- **提取失败**
  _[Jev-LiteMAS: Separating Decisions from Generation in Multi-Agent ...](http://arxiv.org/abs/2610.21411v1)_


- **提取失败**
  _[FedSkillGit: Federated Skill Evolution via Version Control](http://arxiv.org/abs/2610.21348v1)_


- **提取失败**
  _[DocPilot: Interactive Agent Orchestration and Training for Long V...](http://arxiv.org/abs/2610.21327v1)_


- **提取失败**
  _[Harness-Search: Guiding Long-Horizon Search through Multi-Agent C...](http://arxiv.org/abs/2610.05382)_


- **提取失败**
  _[Rethinking Tool Design for Agentic RCA: A Controlled Empirical St...](http://arxiv.org/abs/2610.05009)_


- **提取失败**
  _[Bidirectional Preference Synthesis: Learning Prompt-Conditioned P...](http://arxiv.org/abs/2610.04328)_


- **提取失败**
  _[Understanding and Mitigating Hallucination Escape in Tool-Using L...](http://arxiv.org/abs/2610.04409)_


- **提取失败** 💻
  _[MASBench: Benchmarking LLM-based Multi-Agent Collaboration under ...](http://arxiv.org/abs/2610.04672)_


- **提取失败** 💻
  _[APEX: Active Protection at Execution Boundaries for LLM Agents](http://arxiv.org/abs/2610.06966)_


- **提取失败**
  _[OverAct: Measuring and Mitigating Proactive Over-Authorization in...](http://arxiv.org/abs/2610.01508)_


- **提取失败**
  _[Datura: Progressive Red Teaming Testing for Tool Invocation Chain...](https://www.semanticscholar.org/paper/6f61a10b8a901d2899d15e26e647d841b7fc365c)_


- **提取失败**
  _[SWE-PDB: Teaching LLMs to Leverage Debugging Tools via Agentic Tr...](https://www.semanticscholar.org/paper/c29ded7cc9bf3ea32570d92ad526d41661237efe)_


- **提取失败**
  _[Keyword Harnesses Fail Open: A Cheap Diagnostic Ladder for Tool-U...](http://arxiv.org/abs/2610.02142)_


- **提取失败**
  _[Choosing Before Acting: Comparative Value Estimation for Long-Hor...](http://arxiv.org/abs/2610.02330)_


- **提取失败**
  _[AgentChaosBench: Benchmarking External Fault Detection and Locali...](https://www.semanticscholar.org/paper/f08da96e010556c2269e7031682c4856a66df84a)_


- **提取失败**
  _[MIMESIS: Learning User Simulators as Training Environments for In...](http://arxiv.org/abs/2610.09484)_


- **提取失败** 💻
  _[RELY-SE: A Dashboard for Measuring Operational Reliability of AI ...](https://www.semanticscholar.org/paper/0bb0a8026da0074bfa8838a5aab0e5b3b3e24616)_


- **提取失败**
  _[From Evidence to Action: How Tool-Using Agents Fail](http://arxiv.org/abs/2610.07753)_


- **提取失败**
  _[ST-Bench: A Spatial-Temporal Benchmark for Multi-Agent System Gen...](http://arxiv.org/abs/2610.07763)_


- **提取失败** 💻
  _[BACAM: Behavior-Aware Continual Agent Merging for Multi-Turn Inte...](http://arxiv.org/abs/2610.04966)_


- **提取失败**
  _[AECG: Asymmetric Experience Consolidation and Governance In Multi...](http://arxiv.org/abs/2610.05176)_


- **提取失败**
  _[Sibyl: An Efficient Small-large Model Collaboration Framework for...](http://arxiv.org/abs/2610.05383)_


- **提取失败**
  _[DUET: Co-Evolving Solver and Grader Agents](http://arxiv.org/abs/2610.04087)_


- **提取失败**
  _[Text2Dashboard: A Governed Agent Architecture for Natural-Languag...](http://arxiv.org/abs/2610.06914)_


- **提取失败**
  _[AgentInspect: Diagnosing Behavioral Failures in Artificial Intell...](https://www.semanticscholar.org/paper/e2c1e91570b5503c47080f0a3d295284404a59bd)_


- **提取失败**
  _[Finding the Right Fit: Model-Harness Interactions across Agent Ta...](http://arxiv.org/abs/2610.00917)_


- **提取失败**
  _[RISED: RubrIcs for agentic multi-environment Selection and sElf-D...](http://arxiv.org/abs/2610.00979)_


- **提取失败**
  _[Revision-Aware Independent Agent Graphs for Dynamic Reasoning](http://arxiv.org/abs/2610.01249)_


- **提取失败**
  _[ReCast: Attribution-Oriented Step Representation Learning for LLM...](http://arxiv.org/abs/2610.11334)_


- **提取失败**
  _[GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Productio...](http://arxiv.org/abs/2610.09112)_


- **提取失败**
  _[MiniCorp: The Last Mile of the AI Agent Firm](http://arxiv.org/abs/2610.05912)_


- **提取失败**
  _[SCAD: Structured Credit Assignment and Distillation for Long-Hori...](http://arxiv.org/abs/2610.03372)_


- **提取失败**
  _[InvestigationWorlds: An Agentic Environment for Legal Investigati...](http://arxiv.org/abs/2610.04129)_


- **提取失败**
  _[Dynamic Harness Search: Building Multi-Agent Systems Per-Query vi...](http://arxiv.org/abs/2610.04137)_


- **提取失败** 💻
  _[OpenGameEval: Benchmarking Agentic Programming and Exploration in...](http://arxiv.org/abs/2610.02563)_


- **提取失败**
  _[DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents](http://arxiv.org/abs/2610.02351)_


- **提取失败**
  _[Agent Evaluation Reliability: More Tasks Won't (Always) Fix An Ag...](http://arxiv.org/abs/2610.00651)_


- **提取失败**
  _[Staying on Task: Testing the Foundations of Long-Horizon Agent Re...](http://arxiv.org/abs/2609.38712)_


- **提取失败**
  _[LIBERO-Agent: Evaluating General-Purpose Agents for Direct Embodi...](http://arxiv.org/abs/2609.39507)_


- **提取失败**
  _[Beyond the Shadows of Plato's Cave: Evaluating False Memory in Au...](http://arxiv.org/abs/2609.39473)_


- **提取失败**
  _[Legal Research Bench: Measuring End-to-End Reliability in Long-Ho...](http://arxiv.org/abs/2610.00609)_


- **提取失败**
  _[AREX-2: Advancing Self-Improving Agents through Long-Horizon Refl...](http://arxiv.org/abs/2609.38288)_


- **提取失败** 💻
  _[Inducing Process Supervision from Outcome-Only Reinforcement Lear...](http://arxiv.org/abs/2609.36641)_


- **提取失败**
  _[AgBench: Agentic AI Benchmarks for Personal AI Devices](http://arxiv.org/abs/2609.38652)_


- **提取失败**
  _[AX is the New AEO](http://arxiv.org/abs/2609.34951)_


- **提取失败**
  _[LiteEvo: Automated, Cost-Efficient Harness Evolution for Generali...](http://arxiv.org/abs/2609.33146)_


- **提取失败**
  _[DynGraphAgentBench: A Benchmark for Agentic Lifecycle Control in ...](http://arxiv.org/abs/2609.33980)_


- **提取失败**
  _[Why Do Agent Teams Fail Across Boundaries? A Failure Taxonomy for...](http://arxiv.org/abs/2610.19342)_


- **提取失败**
  _[Interlock: From Local Correctness to Task Completion in Long-Hori...](http://arxiv.org/abs/2610.19686)_


- **提取失败**
  _[StateCraft: Augmenting Video World Models with Abstract-State Rea...](http://arxiv.org/abs/2610.19795)_


- **提取失败**
  _[ChemArgus: Automated Scientific Diagnostics for Lab-Grade Multimo...](http://arxiv.org/abs/2610.20012)_


- **提取失败**
  _[BizBench: Unveiling Hidden Challenges in Deploying Long-Horizon A...](http://arxiv.org/abs/2610.20424)_


- **提取失败**
  _[STP-GUI: Spatially-Aware Token Pruning for Efficient Web-GUI Agen...](http://arxiv.org/abs/2610.20390)_


- **提取失败**
  _[The World Won't Wait: Evaluating and Teaching Agents Under a Live...](http://arxiv.org/abs/2610.20665)_


- **提取失败**
  _[Failure Recovery via Belief Updates and World Modeling for Long-H...](http://arxiv.org/abs/2610.18082)_


- **提取失败**
  _[AgentStripes: An Evidence-Graded Maturity Model for AI Agents](http://arxiv.org/abs/2610.18603)_


- **提取失败**
  _[Learning How to Remember: Memory Modality Selection for GUI Agent...](http://arxiv.org/abs/2610.17928)_


- **提取失败**
  _[Adaptive-Group Process Rewards for GUI Agents](http://arxiv.org/abs/2610.17710)_


- **提取失败** 💻
  _[LatentRiskBench: Measuring State-Dependent Risks in Enterprise Ag...](http://arxiv.org/abs/2610.17685)_


- **提取失败**
  _[Learn from Move: the Next Step for GUI Agents](http://arxiv.org/abs/2610.16720)_


- **提取失败**
  _[EvoWeb: A Benchmark for Coding Agents on Evolving Web Application...](http://arxiv.org/abs/2610.16402)_


- **提取失败**
  _[Why Agentic Workflows Fail: A Taxonomy Derived from Literature an...](http://arxiv.org/abs/2610.17418)_


- **提取失败** 💻
  _[Davinci-Tool: Scaling Agentic Tool-Use Supervision with Verifiabl...](http://arxiv.org/abs/2610.16867)_



---
*ArXiv_Daily_Digest 自动生成 | 2026-10-18*