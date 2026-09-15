# Literature Review

更新：2026-09-15。157份按PDF内容去重的笔记；结果依据本地版本，未重跑实验。

<a id="index"></a>
## 索引

- [P001 · HG-DAgger: Interactive Imitation Learning with Human Experts](#p001)
- [P002 · Abductive Commonsense Reasoning](#p002)
- [P004 · WebGPT: Browser-assisted question-answering with human feedback](#p004)
- [P005 · There’s a Time and Place for Reasoning Beyond the Image](#p005)
- [P006 · Learning Iterative Reasoning through Energy Minimization](#p006)
- [P007 · The Abduction of Sherlock Holmes: A Dataset for Visual Abductive Reasoning](#p007)
- [P008 · Visual Abductive Reasoning](#p008)
- [P009 · Breaking Common Sense: WHOOPS! A Vision-and-Language Benchmark of Synthetic and Compositional Images](#p009)
- [P010 · Visual Writing Prompts: Character-Grounded Story Generation with Curated Image Sequences](#p010)
- [P011 · Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks](#p011)
- [P012 · Reflexion: Language Agents with Verbal Reinforcement Learning](#p012)
- [P013 · Sequential Modeling Enables Scalable Learning for Large Vision Models](#p013)
- [P014 · VOYAGER: An Open-Ended Embodied Agent with Large Language Models](#p014)
- [P015 · Inductive or Deductive? Rethinking the Fundamental Reasoning Abilities of LLMs](#p015)
- [P016 · DIVE: Towards Descriptive and Diverse Visual Commonsense Generation](#p016)
- [P017 · Exploring Defeasibility in Causal Reasoning](#p017)
- [P018 · Learning Iterative Reasoning through Energy Diffusion](#p018)
- [P019 · NL-EYE: Abductive NLI for Images](#p019)
- [P020 · ViCor: Bridging Visual Understanding and Commonsense Reasoning with Large Language Models](#p020)
- [P021 · Black Swan: Abductive and Defeasible Video Reasoning in Unpredictable Events](#p021)
- [P022 · Enabling Self-Improving Agents to Learn at Test Time With Human-In-The-Loop Guidance](#p022)
- [P023 · Generalizable Reasoning through Compositional Energy Minimization](#p023)
- [P024 · Nested Learning: The Illusion of Deep Learning Architecture](#p024)
- [P025 · Reasoning with Sampling: Your Base Model is Smarter Than You Think](#p025)
- [P026 · Training Large Language Models to Reason in a Continuous Latent Space](#p026)
- [P027 · VCD: A Dataset for Visual Commonsense Discovery in Images](#p027)
- [P028 · Video models are zero-shot learners and reasoners](#p028)
- [P029 · VideoDiff: Human-AI Video Co-Creation with Alternatives](#p029)
- [P030 · AbductiveMLLM: Boosting Visual Abductive Reasoning Within MLLMs](#p030)
- [P031 · Agentic Reasoning for Large Language Models](#p031)
- [P032 · Autoregressive, Yet Revisable: In Decoding Revision for Secure Code Generation](#p032)
- [P033 · Gen-Searcher: Reinforcing Agentic Search for Image Generation](#p033)
- [P034 · Lost in Transmission: When and Why LLMs Fail to Reason Globally](#p034)
- [P035 · Mind-Brush: Integrating Agentic Cognitive Search and Reasoning into Image Generation](#p035)
- [P036 · SimStep: Human-in-the-Loop Authoring of Interactive Educational Simulations Through Task-Level Abstractions](#p036)
- [P037 · SLM-MUX: Orchestrating Small Language Models for Reasoning](#p037)
- [P038 · “I’m Not Sure, But...”: Examining the Impact of Large Language Models’ Uncertainty Expression on User Reliance and Trust](#p038)
- [P039 · Make-a-Story: Visual Memory Conditioned Consistent Story Generation](#p039)
- [P040 · Collaposer: Transforming Photo Collections into Visual Assets for Storytelling with Collages](#p040)
- [P041 · Learning to Complement Humans](#p041)
- [P042 · LLMs Struggle to Balance Reasoning and World Knowledge in Causal Narrative Understanding](#p042)
- [P043 · LLMs Struggle to Perform Counterfactual Reasoning with Parametric Knowledge](#p043)
- [P044 · Orthogonal Causal Calibration](#p044)
- [P045 · Failure Modes of LLMs for Causal Reasoning on Narratives](#p045)
- [P046 · Explaining Concept Shift with Interpretable Feature Attribution](#p046)
- [P047 · Can LLMs Propose Instrumental Variables for Causal Reasoning?](#p047)
- [P048 · Utility-Directed Conformal Prediction: A Decision-Aware Framework for Actionable Uncertainty Quantification](#p048)
- [P049 · Decision-Focused Learning without Differentiable Optimization: Learning Locally Optimized Decision Losses](#p049)
- [P050 · Distributionally Robust Feature Selection](#p050)
- [P051 · Fostering the Ecosystem of AI for Social Impact Requires Expanding and Strengthening Evaluation Standards](#p051)
- [P052 · Valid Inference with Imperfect Synthetic Data](#p052)
- [P053 · Superhuman performance of a large language model on the reasoning tasks of a physician](#p053)
- [P054 · Melding the Data-Decisions Pipeline: Decision-Focused Learning for Combinatorial Optimization](#p054)
- [P055 · Principles of Mixed-Initiative User Interfaces](#p055)
- [P056 · Vibe Coding XR: Accelerating AI + XR Prototyping with XR Blocks and Gemini](#p056)
- [P057 · Thing2Reality: Enabling Spontaneous Creation of 3D Objects from 2D Content using Generative AI in XR Meetings](#p057)
- [P058 · How Well Can 3D Accessibility Guidelines Support XR Development? An Interview Study with XR Practitioners in Industry](#p058)
- [P059 · Sensible Agent: A Framework for Unobtrusive Interaction with Proactive AR Agents](#p059)
- [P060 · XR Blocks: Accelerating Human-centered AI + XR Innovation](#p060)
- [P061 · AgentHands: Generating Interactive Hand Gestures for Spatially Grounded Agent Conversations in XR](#p061)
- [P062 · InstructPipe: Generating Visual Blocks Pipelines with Human Instructions and LLMs](#p062)
- [P063 · Large Language Models and Causal Inference in Collaboration: A Comprehensive Survey](#p063)
- [P064 · Causality Model for Semantic Understanding on Videos](#p064)
- [P065 · Human-in-the-Loop through Chain-of-Thought](#p065)
- [P066 · Let’s Verify Step by Step](#p066)
- [P067 · τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains](#p067)
- [P068 · TPDiff: Temporal Pyramid Video Diffusion Model](#p068)
- [P069 · VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning](#p069)
- [P070 · Impossible Videos](#p070)
- [P071 · Counterfactual World Models via Digital Twin-conditioned Video Diffusion](#p071)
- [P072 · Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance](#p072)
- [P073 · The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity](#p073)
- [P074 · Beyond Single-Sentence Prompts: Upgrading Value Alignment Benchmarks with Dialogues and Stories](#p074)
- [P075 · Chain-of-Evidence Multimodal Reasoning for Few-shot Temporal Action Localization](#p075)
- [P076 · Interactive Reasoning: Visualizing and Controlling Chain-of-Thought Reasoning in Large Language Models](#p076)
- [P077 · Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens](#p077)
- [P078 · Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs](#p078)
- [P079 · Thinking in 360°: Humanoid Visual Search in the Wild](#p079)
- [P080 · Vis-CoT: A Human-in-the-Loop Framework for Interactive Visualization and Intervention in LLM Chain-of-Thought Reasoning](#p080)
- [P081 · Olaf-World: Orienting Latent Actions for Video World Modeling](#p081)
- [P083 · Causal-JEPA: Learning World Models through Object-Level Latent Masking](#p083)
- [P084 · CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models](#p084)
- [P085 · SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models](#p085)
- [P086 · See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs](#p086)
- [P087 · Don't Blink: Evidence Collapse during Multimodal Reasoning](#p087)
- [P088 · V-Retrver: Evidence-Driven Agentic Reasoning for Universal Multimodal Retrieval](#p088)
- [P089 · Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models](#p089)
- [P090 · From &lt;Answer&gt; to &lt;Think&gt;: Multi-Dimensional Supervision of Reasoning Process for LLM Optimization](#p090)
- [P091 · Improving Human Verification of LLM Reasoning through Interactive Explanation Interfaces](#p091)
- [P092 · Improving Visual Reasoning with Iterative Evidence Refinement](#p092)
- [P093 · Instruction-Evidence Contrastive Dual-Stream Decoding for Grounded Vision-Language Reasoning](#p093)
- [P094 · SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?](#p094)
- [P095 · TIR-Flow: Active Video Search and Reasoning with Frozen VLMs](#p095)
- [P096 · TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models](#p096)
- [P097 · Useful Memories Become Faulty When Continuously Updated by LLMs](#p097)
- [P098 · First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models](#p098)
- [P099 · VGS-Decoding: Visual Grounding Score Guided Decoding for Hallucination Mitigation in Medical VLMs](#p099)
- [P100 · When Thinking Drifts: Evidential Grounding for Robust Video Reasoning](#p100)
- [P101 · Computational Understanding of Narratives: A Survey](#p101)
- [P102 · Long-Context State-Space Video World Models](#p102)
- [P103 · Training Large Language Models to Reason in a Continuous Latent Space](#p103)
- [P104 · Reasoning with Language Model is Planning with World Model](#p104)
- [P105 · New Evaluation, Library, and Analysis of Step-by-Step Reasoning with Large Language Models](#p105)
- [P106 · Pandora: Towards General World Model with Natural Language Actions and Video States](#p106)
- [P107 · Offline Reinforcement Learning for LLM Multi-step Reasoning](#p107)
- [P108 · Flow of Reasoning: Training LLMs for Divergent Problem Solving with Minimal Examples](#p108)
- [P110 · Understanding the Sources of Uncertainty for Large Language and Multimodal Models](#p110)
- [P111 · CocoaBench: Evaluating Unified Digital Agents in the Wild](#p111)
- [P112 · Vision-G1: Towards General Reasoning Vision-Language Models via Reinforcement Learning](#p112)
- [P113 · Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought](#p113)
- [P114 · LLM Pretraining with Continuous Concepts](#p114)
- [P115 · ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings](#p115)
- [P116 · Reasoning by Superposition: A Theoretical Perspective on Chain of Continuous Thought](#p116)
- [P117 · Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective](#p117)
- [P118 · Calibrating Reasoning in Language Models with Internal Consistency](#p118)
- [P119 · Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification](#p119)
- [P120 · Imagine This! Scripts to Compositions to Videos](#p120)
- [P121 · World Models](#p121)
- [P122 · Phenaki: Variable Length Video Generation from Open Domain Textual Descriptions](#p122)
- [P123 · Genie: Generative Interactive Environments](#p123)
- [P124 · iVideoGPT: Interactive VideoGPTs are Scalable World Models](#p124)
- [P125 · Causally Steered Diffusion for Automated Video Counterfactual Generation](#p125)
- [P126 · Diffusion-Based Visual Art Creation: A Survey and New Perspectives](#p126)
- [P127 · MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences](#p127)
- [P128 · StoryMem: Multi-shot Long Video Storytelling with Memory](#p128)
- [P129 · StoryReasoning Dataset: Using Chain-of-Thought for Scene Understanding and Grounded Story Generation](#p129)
- [P130 · CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models](#p130)
- [P131 · Controllable Video Generation: A Survey](#p131)
- [P132 · Pre-trained Video Generative Models as World Simulators](#p132)
- [P133 · OneStory: Coherent Multi-Shot Video Generation with Adaptive Memory](#p133)
- [P134 · MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences](#p134)
- [P135 · WorldMem: Long-term Consistent World Simulation with Memory](#p135)
- [P136 · StoryBench: A Multifaceted Benchmark for Continuous Story Visualization](#p136)
- [P137 · Long-Context State-Space Video World Models](#p137)
- [P138 · StoryGAN: A Sequential Conditional GAN for Story Visualization](#p138)
- [P139 · Is Your World Simulator a Good Story Presenter? A Consecutive Events-Based Benchmark for Future Long Video Generation](#p139)
- [P140 · VideoAuteur: Towards Long Narrative Video Generation](#p140)
- [P141 · Watch-And-Help: A Challenge for Social Perception and Human-AI Collaboration](#p141)
- [P142 · Alchemy: A Benchmark and Analysis Toolkit for Meta-Reinforcement Learning Agents](#p142)
- [P143 · Interactive Visual Reasoning under Uncertainty](#p143)
- [P144 · Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation](#p144)
- [P145 · Generative Agent-Based Modeling with Actions Grounded in Physical, Social, or Digital Space Using Concordia](#p145)
- [P146 · ExpertAF: Expert Actionable Feedback from Video](#p146)
- [P147 · DreamGarden: A Designer Assistant for Growing Games from a Single Prompt](#p147)
- [P148 · Detecting Hallucinations in Large Language Models Using Semantic Entropy](#p148)
- [P149 · Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training](#p149)
- [P150 · WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment](#p150)
- [P151 · COMBO: Compositional World Models for Embodied Multi-Agent Cooperation](#p151)
- [P152 · DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents](#p152)
- [P153 · Internal Consistency and Self-Feedback in Large Language Models: A Survey](#p153)
- [P154 · Text2World: Benchmarking Large Language Models for Symbolic World Model Generation](#p154)
- [P155 · EgoPlan-Bench2: A Benchmark for Multimodal Large Language Model Planning in Real-World Scenarios](#p155)
- [P156 · PoE-World: Compositional World Modeling with Products of Programmatic Experts](#p156)
- [P157 · Exploring Exploration with Foundation Agents in Interactive Environments](#p157)
- [P158 · RULER-Bench: Probing Rule-based Reasoning Abilities of Next-level Video Generation Models for Vision Foundation Intelligence](#p158)
- [P159 · GPS: Graph-guided Proactive Information Seeking in Large Language Models](#p159)
- [P160 · Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review](#p160)

<a id="p001"></a>
## P001 · HG-DAgger: Interactive Imitation Learning with Human Experts

- **作者**：Michael Kelly; Chelsea Sidrane; Katherine Driggs-Campbell; Mykel J. Kochenderfer
- **时间**：本地版本：2019-03-11（arXiv:1810.02890v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICRA 2019（正式发表）；初稿 2018；本地 arXiv v2：2019-03-11。 [作者机构记录](https://experts.illinois.edu/en/publications/hg-dagger-interactive-imitation-learning-with-human-experts/)
- **论文链接**：[arXiv本地版本 1810.02890v2](https://arxiv.org/abs/1810.02890v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作
- **PDF版本**：7页；SHA-256：`5e3aefda8fa803c4bbd5c6760cc468a9ce926f0d2b38da24834069c3fdadbbd0`

### 中文摘要

让人类自主接管和交还控制权，改进真实系统中的交互式模仿学习，并从接管行为学习基于模型不确定性的风险阈值。

### 核心贡献

提出 Human-Gated DAgger，减少随机切换控制导致的人类标注失真；同时估计策略的可接受状态区域。

### 实现边界

实现于仿真与实车驾驶任务；人类负责判断何时接管，风险阈值是经验估计，未给出无碰撞保证。

### Method／方法

迭代执行新手策略；专家接管时独占控制并收集示范，数据聚合后重训网络集成；用集成输出分歧及接管前的不确定性学习阈值。

### Results／主要结果

实车在 5 组障碍配置上优于 DAgger/行为克隆；与人类转向分布的 Bhattacharyya 距离相较 DAgger 改善 21.1%。仿真中阈值内初始化的碰撞率约为阈值外的 1/12。

### Shortcomings／局限与可能不足

【作者】实车测试数据少，统计显著性有限；【解读】效果依赖专家及时接管，不确定性与真实危险之间并非严格等价。

### 证据定位

摘要 p1；方法 p2–3；实验 p4–6，表 I–II。

### Abstract

Imitation learning has proven to be useful for many real-world problems, but approaches such as behavioral cloning suffer from data mismatch and compounding error issues. One attempt to address these limitations is the DA GGER algorithm, which uses the state distribution induced by the novice to sample corrective actions from the expert. Such sampling schemes, however, require the expert to provide action labels without being fully in control of the system. This can decrease safety and, when using humans as experts, is likely to degrade the quality of the collected labels due to perceived actuator lag. In this work, we propose HG-DA GGER , a variant of DA GGER that is more suitable for interactive imitation learning from human experts in real-world systems. In addition to training a novice policy, HG-DA GGER also learns a safety threshold for a model-uncertainty-based risk metric that can be used to predict the performance of the fully trained novice in different regions of the state space. We evaluate our method on both a simulated and real-world autonomous driving task, and demonstrate improved performance over both DA GGER and behavioral cloning.

<a id="p002"></a>
## P002 · Abductive Commonsense Reasoning

- **作者**：Chandra Bhagavatula; Ronan Le Bras; Chaitanya Malaviya; Keisuke Sakaguchi; Ari Holtzman; Hannah Rashkin; Doug Downey; Scott Wen-tau Yih; Yejin Choi
- **时间**：本地版本：2020-02-14（arXiv:1908.05739v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICLR 2020（PDF 明示）；本地 arXiv v2：2020-02-14
- **论文链接**：[arXiv本地版本 1908.05739v2](https://arxiv.org/abs/1908.05739v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：[P003](#p003)与本文件SHA-256完全一致，共用此总结。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：18页；SHA-256：`c6d69ad1817d26ff208441dae37d9b638e82e6a0e85ce4eea2063adffbd1cdf7`

### 中文摘要

把溯因推理定义为根据前后观察寻找最合理解释，构建 ART 数据及解释选择、解释生成两类任务。

### 核心贡献

提供超过 2 万叙事情境和 20 万解释；提出 Abductive NLI/NLG，并分析预训练语言模型的推理缺口。

### 实现边界

英语短篇常识叙事中的候选解释选择/文本生成；合理解释不等于唯一、可验证的真实原因。

### Method／方法

众包构造观察及正负解释，使用对抗筛选降低捷径；比较 GPT/BERT 微调和不同观察依赖结构，进行人工与自动评价。

### Results／主要结果

ART 测试集最佳 BERT 68.9%±0.5%，人类多数投票 91.4%；5 个训练随机种子；生成任务仍有明显常识与因果连贯性问题。

### Shortcomings／局限与可能不足

【解读】故事和众包解释限定了常识分布；二选一准确率不能代表开放世界因果发现，生成评价受多解性影响。

### 证据定位

摘要 p1；任务/数据 §2–4；结果 §5，表1；分析 §6。

### Abstract

Abductive reasoning is inference to the most plausible explanation. For example, if Jenny finds her house in a mess when she returns from work, and remembers that she left a window open, she can hypothesize that a thief broke into her house and caused the mess, as the most plausible explanation. While abduction has long been considered to be at the core of how people interpret and read between the lines in natural language (Hobbs et al., 1988), there has been relatively little research in support of abductive natural language inference and generation. We present the first study that investigates the viability of language-based abductive reasoning. We introduce a challenge dataset, ART, that consists of over 20k commonsense narrative contexts and 200k explanations. Based on this dataset, we conceptualize two new tasks – (i) Abductive NLI: a multiple-choice question answering task for choosing the more likely explanation, and (ii) Abductive NLG: a conditional generation task for explaining given observations in natural language. On Abductive NLI, the best model achieves 68.9% accuracy, well below human performance of 91.4%. On Abductive NLG, the current best language generators struggle even more, as they lack reasoning capabilities that are trivial for humans. Our analysis leads to new insights into the types of reasoning that deep pre-trained language models fail to perform—despite their strong performance on the related but more narrowly defined task of entailment NLI—pointing to interesting avenues for future research.

<a id="p004"></a>
## P004 · WebGPT: Browser-assisted question-answering with human feedback

- **作者**：Reiichiro Nakano; Jacob Hilton; Suchir Balaji; Jeff Wu; Long Ouyang; Christina Kim; Christopher Hesse; Shantanu Jain; Vineet Kosaraju; William Saunders; Xu Jiang; Karl Cobbe; Tyna Eloundou; Gretchen Krueger; Kevin Button; Matthew Knight; Benjamin Chess; John Schulman
- **时间**：本地版本：2022-06-01（arXiv:2112.09332v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv 技术报告；初稿 2021；本地 v3：2022-06-01；PDF 未标正式会议/期刊
- **论文链接**：[arXiv本地版本 2112.09332v3](https://arxiv.org/abs/2112.09332v3)
- **项目／代码／数据**：[项目/演示页面](https://openaipublic.blob.core.windows.net/webgpt-answer-viewer/index.html)

- **主题**：XR与人机协作
- **PDF版本**：32页；SHA-256：`acad8d9fd55a30b94de9dfdae413e10b21e07bde54d767b2405b31341739cedb`

### 中文摘要

训练 GPT-3 操作文本浏览器、收集引用并回答长问题，以示范学习和人类偏好反馈提升答案质量。

### 核心贡献

把检索、浏览、引用和回答统一为可训练的交互轨迹，并利用带引用答案支持人类评价。

### 实现边界

文本浏览器和 ELI5 长问答；最强模型使用 175B、best-of-64，有引用不代表引用真实或推断正确。

### Method／方法

约 6,000 条人类示范做行为克隆，约 21,500 组偏好比较训练奖励模型；比较 PPO 与拒绝采样，主要最优配置采用行为克隆加奖励筛选。

### Results／主要结果

在 ELI5 上，最强模型相对人类示范答案的偏好率为 56%，相对 Reddit 高赞答案为 69%（平局计半）；这是偏好评价，不是事实准确率。

### Shortcomings／局限与可能不足

【作者】分布外问题仍困难，引用支持性不能替代真实性，存在偏见和奖励优化问题；【解读】多次浏览与采样成本高。

### 证据定位

摘要 p1；训练 §3；评价 §4–5；真实性和引用局限 §6。

### Abstract

We fine-tune GPT-3 to answer long-form questions using a text-based webbrowsing environment, which allows the model to search and navigate the web. By setting up the task so that it can be performed by humans, we are able to train models on the task using imitation learning, and then optimize answer quality with human feedback. To make human evaluation of factual accuracy easier, models must collect references while browsing in support of their answers. We train and evaluate our models on ELI5, a dataset of questions asked by Reddit users. Our best model is obtained by fine-tuning GPT-3 using behavior cloning, and then performing rejection sampling against a reward model trained to predict human preferences. This model’s answers are preferred by humans 56% of the time to those of our human demonstrators, and 69% of the time to the highest-voted answer from Reddit.

<a id="p005"></a>
## P005 · There’s a Time and Place for Reasoning Beyond the Image

- **作者**：Xingyu Fu; Ben Zhou; Ishaan Preetam Chandratreya; Carl Vondrick; Dan Roth
- **时间**：2022年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ACL 2022，Long Papers，1138–1149；会议 2022-05-22 至 05-27
- **项目／代码／数据**：[代码：zeyofu/TARA](https://github.com/zeyofu/TARA)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：12页；SHA-256：`aaf98fccea956b5824724ffc590c892f805b3814ef30ed5f8e096a11dd9987f1`

### 中文摘要

提出图像时空定位任务 TARA，要求综合画面线索与背景知识判断拍摄时间和地点。

### 核心贡献

构建约 16K 新闻图片和额外 61K WIT 弱监督样本，并提供基于局部图像线索的 CLIP 变体。

### 实现边界

主要为 NYT/Wikipedia 图片和给定标签集合的分类，不是无需候选的任意地点、精确日期识别。

### Method／方法

自动抽取新闻时空标签，众包验证可推理子集；比较 CLIP、微调、WIT 监督及 segment-wise 表征，使用 Accuracy 和层级 Example-F1。

### Results／主要结果

全测试集地点准确率 CLIP 11.11%、CLIP+Seg 16.46%。在人类对照子集，地点 23.33% vs 人类 86.21%，时间 3.33% vs 75.86%；不能把两个测试集合并比较。

### Shortcomings／局限与可能不足

【作者/设定】人类只测 test set of interest；【解读】新闻来源和标签分布有偏，图片可能不足以确定唯一时间，WIT 的分布差异限制收益。

### 证据定位

摘要 p1；数据 §3–4；方法 §5；表2、表3及 §6.3。

### Abstract

Images are often more significant than only the pixels to human eyes, as we can infer, associate, and reason with contextual information from other sources to establish a more complete picture. For example, in Figure 1, we can find a way to identify the news articles related to the picture through segment-wise understandings of the signs, the buildings, the crowds, and more. This reasoning could provide the time and place the image was taken, which will help us in subsequent tasks, such as automatic storyline construction, correction of image source in intended effect photographs, and upper-stream processing such as image clustering for certain location or time. In this work, we formulate this problem and introduce TARA: a dataset with 16k images with their associated news, time, and location, automatically extracted from New York Times1 (NYT), and an additional 61k examples as distant supervision from WIT (Srinivasan et al., 2021). On top of the extractions, we present a crowdsourced subset in which we believe it is possible to find the images’ spatiotemporal information for evaluation purpose. We show that there exists a 70% gap between a state-of-the-art joint model and human performance, which is slightly filled by our proposed model that uses segment-wise reasoning, motivating higher-level vision-language joint models that can conduct open-ended reasoning with world knowledge. The data and code are publicly available at https://github.com/zeyofu/TARA.

<a id="p006"></a>
## P006 · Learning Iterative Reasoning through Energy Minimization

- **作者**：Yilun Du; Shuang Li; Joshua Tenenbaum; Igor Mordatch
- **时间**：本地版本：2022-06-30（arXiv:2206.15448v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICML 2022（PDF 元数据与正文）；本地 arXiv v1：2022-06-30
- **论文链接**：[arXiv本地版本 2206.15448v1](https://arxiv.org/abs/2206.15448v1)
- **项目／代码／数据**：[项目/演示页面](https://energy-based-model.github.io/iterative-reasoning-as-energy-minimization/)

- **主题**：世界机制与演化
- **PDF版本**：14页；SHA-256：`2c44b73b49bf1fad468a2f7a4e03c2ddfd5eaef4447890c7a5d980bc1c8ceead`

### 中文摘要

把推理写成学习能量函数后的迭代优化，使测试时可以增加计算以处理更大或更难的问题。

### 核心贡献

IREM 用统一能量最小化处理图与连续算法任务，并演示嵌套组合求解。

### 实现边界

验证于合成图运算、加法、矩阵补全/求逆等；优化过程不保证任意实例达到全局最优。

### Method／方法

学习输入与候选输出之间的能量景观；通过迭代梯度更新寻找低能量解，以回放缓冲和末步截断反传控制训练开销。

### Results／主要结果

10 节点训练、15 节点测试的最短路元素 MSE 为 0.0464，循环网络 0.1083、前馈模型 1.4089；更难加法 MSE 为 0.0021，对比最佳列示基线 0.1577。

### Shortcomings／局限与可能不足

【解读】收益依赖能量函数及优化质量；增加推理时间有成本，合成任务的规模泛化不等于自然语言或开放世界推理。

### 证据定位

方法 §3；表1 p5；消融表2；§5 Conclusion and Limitations。

### Abstract

Deep learning has excelled on complex pattern recognition tasks such as image classification and object recognition. However, it struggles with tasks requiring nontrivial reasoning, such as algorithmic computation. Humans are able to solve such tasks through iterative reasoning – spending more time thinking about harder tasks. Most existing neural networks, however, exhibit a fixed computational budget controlled by the neural network architecture, preventing additional computational processing on harder tasks. In this work, we present a new framework for iterative reasoning with neural networks. We train a neural network to parameterize an energy landscape over all outputs, and implement each step of the iterative reasoning as an energy minimization step to find a minimal energy solution. By formulating reasoning as an energy minimization problem, for harder problems that lead to more complex energy landscapes, we may then adjust our underlying computational budget by running a more complex optimization procedure. We empirically illustrate that our iterative reasoning approach can solve more accurate and generalizable algorithmic reasoning tasks in both graph and continuous domains. Finally, we illustrate that our approach can recursively solve algorithmic problems requiring nested reasoning. Code and additional information is available at https://energy-based-model.github.io/iterative-reasoning-as-energy-minimization/.

<a id="p007"></a>
## P007 · The Abduction of Sherlock Holmes: A Dataset for Visual Abductive Reasoning

- **作者**：Jack Hessel; Jena D. Hwang; Jae Sung Park; Rowan Zellers; Chandra Bhagavatula; Anna Rohrbach; Kate Saenko; Yejin Choi
- **时间**：2022年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ECCV 2022（官方记录核验）。 [ECVA官方论文页](https://www.ecva.net/papers/eccv_2022/papers_ECCV/html/5263_ECCV_2022_paper.php)
- **项目／代码／数据**：[项目/演示页面](http://visualabduction.com/)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：18页；SHA-256：`6d3154700273e8716a1894925a16c6890426adc4cd9bb9d54a4fe1bde03c78ac`

### 中文摘要

构建 Sherlock，收集视觉线索和超出字面画面的合理推断，评估机器的视觉溯因能力。

### 核心贡献

103K 图片、363K 线索—推断对及约 19K 合理性判断，覆盖推断检索、证据定位和合理性比较。

### 实现边界

推断是人类认为合理的假设；主要评价检索/定位/比较，开放式生成评价仍待解决。

### Method／方法

自由观察式众包标注线索框和推断；训练图像、区域、文本兼容性评分器，比较 LXMERT、UNITER 和 CLIP，并加入多任务训练。

### Results／主要结果

CLIP-RN50x64 加多任务目标在三类评测中优于所列强基线，但与人类判断一致性仍有明显差距；文中同时报告定位及排序指标，不能统一当作准确率。

### Shortcomings／局限与可能不足

【作者】显著线索选择、合理推断的歧义及生成评价未解决；文字识别、动作识别等基础视觉错误也会传递到推断。

### 证据定位

摘要 p1；任务 §4；方法/结果 §5、表2；结论 §6。

### Abstract

Humans have remarkable capacity to reason abductively and hypothesize about what lies beyond the literal content of an image. By identifying concrete visual clues scattered throughout a scene, we almost can’t help but draw probable inferences beyond the literal scene based on our everyday experience and knowledge about the world. For example, if we see a “20 mph” sign alongside a road, we might assume the street sits in a residential area (rather than on a highway), even if no houses are pictured. Can machines perform similar visual reasoning? We present Sherlock, an annotated corpus of 103K images for testing machine capacity for abductive reasoning beyond literal image contents. We adopt a free-viewing paradigm: participants first observe and identify salient clues within images (e.g., objects, actions ) and then provide a plausible inference about the scene, given the clue. In total, we collect 363K (clue, inference) pairs, which form a first-of-its-kind abductive visual reasoning dataset. Using our corpus, we test three complementary axes of abductive reasoning. We evaluate the capacity of models to: i) retrieve relevant inferences from a large candidate corpus; ii) localize evidence for inferences via bounding boxes, and iii) compare plausible inferences to match human judgments on a newlycollected diagnostic corpus of 19K Likert-scale judgments. While we find that fine-tuning CLIP-RN50x64 with a multitask objective outperforms strong baselines, significant headroom exists between model performance and human agreement. Data, models, and leaderboard available at http://visualabduction.com/.

<a id="p008"></a>
## P008 · Visual Abductive Reasoning

- **作者**：Chen Liang; Wenguan Wang; Tianfei Zhou; Yi Yang
- **时间**：本地版本：2022-03-26（arXiv:2203.14040v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：CVPR 2022，pp.15565–15575（官方CVF记录核验）。 [CVF官方论文页](https://openaccess.thecvf.com/content/CVPR2022/html/Liang_Visual_Abductive_Reasoning_CVPR_2022_paper.html)
- **论文链接**：[arXiv本地版本 2203.14040v1](https://arxiv.org/abs/2203.14040v1)
- **项目／代码／数据**：[代码：leonnnop/VAR](https://github.com/leonnnop/VAR)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：16页；SHA-256：`90f39a03b4c4a282706963260126887bfd7658133b53f6b586bfe9e39cc5febe`

### 中文摘要

在事件片段被遮蔽的视频中描述已知事件并生成最可能的缺失事件解释，提出 VAR 数据集和 REASONER。

### 核心贡献

设计因果方向感知编码及置信度引导的级联解码，逐轮改进前提描述与假设。

### 实现边界

输入已有事件分段，缺失事件以黑帧遮蔽；实现的是语言解释生成，未识别或验证真实因果结构。

### Method／方法

使用预提取动作/外观特征，contextualized directional position embedding 区分关系；三个级联 Transformer 解码器通过句子置信度交换信息。

### Results／主要结果

消融中，普通 Transformer 的平均事件 CIDEr 30.04、BLEU-4 3.39；同时加入两个组件后为 36.13、4.66。完整模型领先比较的视频语言基线，但仍落后人类。

### Shortcomings／局限与可能不足

【解读】依赖事件分割和视觉特征；多种合理解释会使参考文本指标失真，因果位置编码并非干预意义上的因果保证。

### 证据定位

任务 §3；实现 §4.4；实验 §5、表8；附录失败案例。

### Abstract

Abductive reasoning seeks the likeliest possible explanation for partial observations. Although abduction is frequently employed in human daily reasoning, it is rarely explored in computer vision literature. In this paper, we propose a new task and dataset, Visual Abductive Reasoning (VAR), for examining abductive reasoning ability of machine intelligence in everyday visual situations. Given an incomplete set of visual events, AI systems are required to not only describe what is observed, but also infer the hypothesis that can best explain the visual premise. Based on our large-scale VAR dataset, we devise a strong baseline model, REASONER (causal-and-cascaded reasoning Transformer). First, to capture the causal structure of the observations, a contextualized directional position embedding strategy is adopted in the encoder, that yields discriminative representations for the premise and hypothesis. Then, multiple decoders are cascaded to generate and progressively refine the premise and hypothesis sentences. The prediction scores of the sentences are used to guide cross-sentence information flow in the cascaded reasoning procedure. Our VAR benchmarking results show that REASONER surpasses many famous video-language models, while still being far behind human performance. This work is expected to foster future efforts in the reasoning-beyond-observation paradigm.

<a id="p009"></a>
## P009 · Breaking Common Sense: WHOOPS! A Vision-and-Language Benchmark of Synthetic and Compositional Images

- **作者**：Nitzan Bitton-Guetta; Yonatan Bitton; Jack Hessel; Ludwig Schmidt; Yuval Elovici; Gabriel Stanovsky; Roy Schwartz
- **时间**：本地版本：2023-08-12（arXiv:2303.07274v4）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICCV 2023，2616–2627；本地 arXiv v4：2023-08-12。 [CVF官方论文页](https://openaccess.thecvf.com/content/ICCV2023/html/Bitton-Guetta_Breaking_Common_Sense_WHOOPS_A_Vision-and-Language_Benchmark_of_Synthetic_and_ICCV_2023_paper.html)
- **论文链接**：[arXiv本地版本 2303.07274v4](https://arxiv.org/abs/2303.07274v4)
- **项目／代码／数据**：[项目/演示页面](https://whoops-benchmark.github.io/)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：15页；SHA-256：`342485fdb71a2e2931d66cfd760bc87c9f78d58bd7edaf325cf0e921621629ab`

### 中文摘要

通过人为设计的反常识合成图像，评价模型是否能识别和解释图像中的异常，而不只描述物体。

### 核心贡献

提供视觉常识基准及解释异常任务，结合 captioning、匹配和 VQA；分析感知与推理各自的瓶颈。

### 实现边界

小规模、人工筛选的合成图像及四类任务；不能直接代表真实图像中的所有常识错误。

### Method／方法

设计师用文生图工具制作异常组合，众包标注解释；比较端到端 BLIP2 和图像描述→LLM 管线，并用人类及 GPT-4 评价解释。

### Results／主要结果

表1中，微调 BLIP2-XXL 异常识别 73%，人类 92%；解释的人类评分为 27%，oracle caption→GPT-3 为 68%，人类 95%。

### Shortcomings／局限与可能不足

【作者】数据规模小，仍可能含令人不适内容；【解读】生成工具、文化常识及 GPT 评价器带来偏差，oracle 描述结果不是实际端到端水平。

### 证据定位

摘要；数据 §2；表1；结果 §5.2；局限 §8。

### Abstract

Weird, unusual, and uncanny images pique the curiosity of observers because they challenge commonsense. For example, an image released during the 2022 world cup depicts the famous soccer stars Lionel Messi and Cristiano Ronaldo playing chess, which playfully violates our expectation that their competition should occur on the football field.1 Humans can easily recognize and interpret these unconventional images, but can AI models do the same? We introduce WHOOPS !, a new dataset and benchmark for visual commonsense. The dataset is comprised of purposefully commonsense-defying images created by designers using publicly-available image generation tools like Midjourney. We consider several tasks posed over the dataset. In addition to image captioning, cross-modal matching, and visual question answering, we introduce a difficult explanation generation task, where models must identify and explain why a given image is unusual. Our results show that state-of-the-art models such as GPT3 and BLIP2 still lag behind human performance on WHOOPS !. We hope our dataset will inspire the development of AI models with stronger visual commonsense reasoning abilities.

<a id="p010"></a>
## P010 · Visual Writing Prompts: Character-Grounded Story Generation with Curated Image Sequences

- **作者**：Xudong Hong; Asad Sayeed; Khushboo Mehra; Vera Demberg; Bernt Schiele
- **时间**：本地版本：2023-01-20（arXiv:2301.08571v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：TACL 2023，11:565–581；本地为 2023-01-20 预出版稿。 [ACL Anthology记录](https://aclanthology.org/2023.tacl-1.33/)
- **论文链接**：[arXiv本地版本 2301.08571v1](https://arxiv.org/abs/2301.08571v1)
- **项目／代码／数据**：[项目/演示页面](https://vwprompt.github.io/)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：15页；SHA-256：`33a8162c030e1f548ed7f94972bf7154d3efeb6b1ac91db896cf0d37217b1870`

### 中文摘要

用经过筛选的电影镜头序列和明确角色构建 VWP，以更好的输入与角色表示提升视觉故事的连贯性。

### 核心贡献

约 2K 个、每个 5–10 图的序列及约 12K 众包故事；提出角色感知的 CharGrid 基线。

### 实现边界

生成图像序列对应的文本故事；依赖电影镜头、角色框和筛选流程，不生成视频或验证事件真实发生。

### Method／方法

过滤低信息和重复镜头，提供角色名称/裁剪图引导写作；冻结 Swin 特征提取，结合角色特征与角色网格建模跨句连贯性。

### Results／主要结果

28 名众包者比较 50 对故事；本地稿表7中 CharGrid 相较 TAPM+char 的人类判断差值：连贯性 +8.41、视觉依据 +6.25、多样性 +11.06 个百分点。

### Shortcomings／局限与可能不足

【作者】叙事结构/narrativity 和写作者能力差异未充分建模；【解读】人工评价样本小，电影域与现实相册存在分布差异。

### 证据定位

摘要；构建 §3–5；模型 §6.1；人评 §6.3/表7；§7。

### Abstract

Current work on image-based story generation suffers from the fact that the existing image sequences collections do not have coherent plots behind them. We improve visual story generation by producing a new image-grounded dataset, Visual Writing Prompts (VWP). VWP contains almost 2K selected sequences of movie shots, each including 5-10 images. The image sequences are aligned with a total of 12K stories which were collected via crowdsourcing given the image sequences and a set of grounded characters from the corresponding image sequence. Our new image sequence collection and filtering process has allowed us to obtain stories that are more coherent and more diverse compared to previous work. We also propose a characterbased story generation model driven by coherence as a strong baseline. Evaluations show that our generated stories are more coherent, visually grounded, and more diverse than stories generated with the current stateof-the-art model.

<a id="p011"></a>
## P011 · Reasoning or Reciting? Exploring the Capabilities and Limitations of Language Models Through Counterfactual Tasks

- **作者**：Zhaofeng Wu; Linlu Qiu; Alexis Ross; Ekin Akyürek; Boyuan Chen; Bailin Wang; Najoung Kim; Jacob Andreas; Yoon Kim
- **时间**：本地版本：2024-03-28（arXiv:2307.02477v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：NAACL 2024，Long Papers，pp.1819–1862（官方ACL记录核验）；本地arXiv v3：2024-03-28。 [ACL Anthology记录](https://aclanthology.org/2024.naacl-long.102/)
- **论文链接**：[arXiv本地版本 2307.02477v3](https://arxiv.org/abs/2307.02477v3)
- **项目／代码／数据**：[代码：ZhaofengWu/counterfactual-evaluation](https://github.com/ZhaofengWu/counterfactual-evaluation)

- **主题**：世界机制与演化
- **PDF版本**：49页；SHA-256：`c7e3f360460c7a66c6d1329891aabebf7bff4e1ef4ee67896538d803d5dec75b`

### 中文摘要

用改变默认规则的反事实任务区分可迁移推理与对熟悉任务模式的依赖。

### 核心贡献

构造 11 类任务的默认/反事实配对评测，并加入反事实规则理解检查及不同提示条件。

### 实现边界

任务包括算术、代码、逻辑、空间、音乐和游戏；研究基于指定的 2023 版闭源模型，不是对全部 LLM 的不可推理证明。

### Method／方法

保持任务结构、改动进制/索引/坐标/游戏规则等条件，比较 GPT-4、GPT-3.5、Claude、PaLM-2，控制 CoT 与 few-shot 提示。

### Results／主要结果

11 项任务整体呈现反事实条件下显著且一致的性能下降；few-shot 能缩小但不能消除差距，理解规则也不保证正确执行。

### Shortcomings／局限与可能不足

【作者】默认与反事实任务难度不总能严格匹配，预训练内容未知，结果可能高估或低估能力；【解读】分布偏移与抽象推理失败不能完全分离。

### 证据定位

摘要；框架 §2；结果 §4；分析 §5；局限 §7。

### Abstract

The impressive performance of recent language models across a wide range of tasks suggests that they possess a degree of abstract reasoning skills. Are these skills general and transferable, or specialized to specific tasks seen during pretraining? To disentangle these effects, we propose an evaluation framework based on “counterfactual” task variants that deviate from the default assumptions underlying standard tasks. Across a suite of 11 tasks, we observe nontrivial performance on the counterfactual variants, but nevertheless find that performance substantially and consistently degrades compared to the default conditions. This suggests that while current LMs may possess abstract task-solving skills to an extent, they often also rely on narrow, non-transferable procedures for task-solving. These results motivate a more careful interpretation of language model performance that teases apart these aspects of behavior.

<a id="p012"></a>
## P012 · Reflexion: Language Agents with Verbal Reinforcement Learning

- **作者**：Noah Shinn; Federico Cassano; Ashwin Gopinath; Karthik Narasimhan; Shunyu Yao
- **时间**：2023年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2023（会议论文）
- **项目／代码／数据**：[代码（现地址）：noahshinn/reflexion](https://github.com/noahshinn/reflexion)；2026-09-16核验维护者仓库。原摘要中的旧地址作为历史文字保留。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：19页；SHA-256：`efba04cd48b779131fc4c3c58ae49e8523ded534f9225a7c57c7bdad0823803d`

### 中文摘要

让语言智能体把失败反馈总结成文字反思，并在后续尝试中利用记忆改进决策。

### 核心贡献

提出 actor—evaluator—self-reflection 框架，以语言记忆实现跨尝试改进。

### 实现边界

不更新模型参数；依赖可重复尝试、可获得反馈的环境，所谓 verbal RL 与梯度训练式 RL 不同。

### Method／方法

执行任务后由外部或内部评价器给出反馈，生成反思并写入有限情节记忆，下次提示时检索/拼接；在 ALFWorld、HotpotQA 和代码任务验证。

### Results／主要结果

论文报告 HumanEval 91% pass@1，相较引用的 GPT-4 80%；该数值来自允许反馈与迭代的完整协议，不能等同无反馈单次生成准确率。

### Shortcomings／局限与可能不足

【作者】可能停在局部最优，记忆窗口有限；生成的测试不足以可靠检验非确定性、外部 API 或并发程序。

### 证据定位

摘要；§3；§4.3；局限 §5。

### Abstract

Large language models (LLMs) have been increasingly used to interact with external environments (e.g., games, compilers, APIs) as goal-driven agents. However, it remains challenging for these language agents to quickly and efficiently learn from trial-and-error as traditional reinforcement learning methods require extensive training samples and expensive model fine-tuning. We propose Reflexion, a novel framework to reinforce language agents not by updating weights, but instead through linguistic feedback. Concretely, Reflexion agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion is flexible enough to incorporate various types (scalar values or free-form language) and sources (external or internally simulated) of feedback signals, and obtains significant improvements over a baseline agent across diverse tasks (sequential decision-making, coding, language reasoning). For example, Reflexion achieves a 91% pass@1 accuracy on the HumanEval coding benchmark, surpassing the previous state-of-the-art GPT-4 that achieves 80%. We also conduct ablation and analysis studies using different feedback signals, feedback incorporation methods, and agent types, and provide insights into how they affect performance. We release all code, demos, and datasets at `https://github.com/noahshinn024/reflexion`.

<a id="p013"></a>
## P013 · Sequential Modeling Enables Scalable Learning for Large Vision Models

- **作者**：Yutong Bai; Xinyang Geng; Karttikeya Mangalam; Amir Bar; Alan Yuille; Trevor Darrell; Jitendra Malik; Alexei A. Efros
- **时间**：本地版本：2023-12-01（arXiv:2312.00785v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：CVPR 2024，pp.22861–22872（官方CVF记录核验）；本地为2023-12-01预印版。 [CVF官方论文页](https://openaccess.thecvf.com/content/CVPR2024/html/Bai_Sequential_Modeling_Enables_Scalable_Learning_for_Large_Vision_Models_CVPR_2024_paper.html)
- **论文链接**：[arXiv本地版本 2312.00785v1](https://arxiv.org/abs/2312.00785v1)
- **项目／代码／数据**：[项目/演示页面](https://yutongbai.com/lvm.html)

- **主题**：世界机制与演化
- **PDF版本**：33页；SHA-256：`6e6272927d093a531405429818c6067df826310ba8983a8a2968bb8d117c390e`

### 中文摘要

把图像、视频和视觉标注统一为视觉句子，使用下一 token 预测训练无需语言输入的大视觉模型。

### 核心贡献

构建统一视觉序列表示并展示多任务视觉提示和模型/数据扩展趋势。

### 实现边界

任务由示例图像定义，输出为视觉 token；训练与评价不证明任意视觉任务均能零样本解决。

### Method／方法

VQGAN 将图像离散化，再用自回归 Transformer 学习跨图像序列；在 420B 视觉 token 上训练 300M、600M、1B、3B 模型。

### Results／主要结果

420B token 约对应 1.64B 图像；文中语义分割视觉序列困惑度随规模从 23.1（300M）降到 14.0（3B），并展示类比、视频预测等视觉提示结果。

### Shortcomings／局限与可能不足

【作者】视觉提示可能欠约束，tokenizer 与视频数据质量导致失败；算力限制了消融，对真正的涌现/泛化尚无定论。

### 证据定位

摘要；方法 §4；规模实验 §5.1/图3–4；局限 §6。

### Abstract

We introduce a novel sequential modeling approach which enables learning a Large Vision Model (LVM) without making use of any linguistic data. To do this, we define a common format, “visual sentences”, in which we can represent raw images and videos as well as annotated data sources such as semantic segmentations and depth reconstructions without needing any meta-knowledge beyond the pixels. Once this wide variety of visual data (comprising 420 billion tokens) is represented as sequences, the model can be trained to minimize a cross-entropy loss for next token prediction. By training across various scales of model architecture and data diversity, we provide empirical evidence that our models scale effectively. Many different vision tasks can be solved by designing suitable visual prompts at test time.

<a id="p014"></a>
## P014 · VOYAGER: An Open-Ended Embodied Agent with Large Language Models

- **作者**：Guanzhi Wang; Yuqi Xie; Yunfan Jiang; Ajay Mandlekar; Chaowei Xiao; Yuke Zhu; Linxi “Jim” Fan; Anima Anandkumar
- **时间**：本地版本：2023-10-19（arXiv:2305.16291v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：本地 arXiv v2：2023-10-19；正式平台待核验
- **论文链接**：[arXiv本地版本 2305.16291v2](https://arxiv.org/abs/2305.16291v2)
- **项目／代码／数据**：[项目/演示页面](https://voyager.minedojo.org)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：42页；SHA-256：`769a4e33ddeeb73870849232eece49afe882c2d146362e33917ccb432ba0efb8`

### 中文摘要

在 Minecraft 中用自动课程、可执行技能库和反馈驱动的代码修正实现持续探索与技能积累。

### 核心贡献

以代码技能外部记忆实现组合和迁移，配合自适应课程扩大探索范围。

### 实现边界

通过 Mineflayer JavaScript API 和结构化环境状态控制游戏；未训练模型权重，也未实现真实机器人上的终身学习。

### Method／方法

GPT-4 提议技能与代码，利用执行错误、环境反馈和自检反复修改；成功技能存入库，按任务检索重用。

### Results／主要结果

160 次提示迭代内发现 63 种物品，约为对照的 3.3 倍；探索距离 2.3 倍，关键科技里程碑最多快 15.3 倍；演示新地图任务迁移。

### Shortcomings／局限与可能不足

【作者】API 成本高，代码生成/自检失败和不可完成的幻觉任务仍存在；【解读】技能迁移限于同一游戏/API 体系。

### 证据定位

摘要；方法 §2；实验 §3.3；局限 §4。

### Abstract

We introduce VOYAGER, the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention. VOYAGER consists of three key components: 1) an automatic curriculum that maximizes exploration, 2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and 3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement. VOYAGER interacts with GPT-4 via blackbox queries, which bypasses the need for model parameter fine-tuning. The skills developed by VOYAGER are temporally extended, interpretable, and compositional, which compounds the agent’s abilities rapidly and alleviates catastrophic forgetting. Empirically, VOYAGER shows strong in-context lifelong learning capability and exhibits exceptional proficiency in playing Minecraft. It obtains 3.3× more unique items, travels 2.3× longer distances, and unlocks key tech tree milestones up to 15.3× faster than prior SOTA. VOYAGER is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch, while other techniques struggle to generalize.

<a id="p015"></a>
## P015 · Inductive or Deductive? Rethinking the Fundamental Reasoning Abilities of LLMs

- **作者**：Kewei Cheng; Jingfeng Yang; Haoming Jiang; Zhengyang Wang; Binxuan Huang; Ruirui Li; Shiyang Li; Zheng Li; Yifan Gao; Xian Li; Bing Yin; Yizhou Sun
- **时间**：本地版本：2024-08-07（arXiv:2408.00114v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2408.00114v2（本地版本）；正式会议/期刊未核实
- **论文链接**：[arXiv本地版本 2408.00114v2](https://arxiv.org/abs/2408.00114v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：18页；SHA-256：`565fc1b5b46f783169964078ab1dc9b1c1a075d382e428cb899ceac208044240`

### 中文摘要

用 SolverLearner 分离从样例归纳规则与执行规则，重新比较 LLM 的归纳和演绎能力。

### 核心贡献

让 LLM 生成映射程序，再交给外部解释器执行，降低执行错误对归纳能力评价的干扰。

### 实现边界

限于具有明确函数族和可执行规则的合成任务；程序执行由工具完成。

### Method／方法

比较直接输入输出提示、显式给规则、由样例生成 Python 规则三种设置，测试算术、空间等默认/反事实任务。

### Results／主要结果

GPT-4 在大部分受限归纳条件下接近或达到准确率 1；直接演绎特别是反事实执行较弱，GPT-3.5 并不普遍达到同等水平。

### Shortcomings／局限与可能不足

【作者】无搜索空间约束时归纳困难，结论依赖基础模型，主比较未纳入 CoT；【解读】不宜概括为所有归纳推理均强于演绎。

### 证据定位

§3 SolverLearner；§5；结论后的 Limitations。

### Abstract

Reasoning encompasses two typical types: deductive reasoning and inductive reasoning. Despite extensive research into the reasoning capabilities of Large Language Models (LLMs), moststudieshavefailedtorigorouslydifferentiate between inductive and deductive reasoning, leading to a blending of the two. This raises an essential question:In LLM reasoning, which poses a greater challenge - deductive or inductive reasoning?While the deductive reasoning capabilities of LLMs, (i.e. their capacity to follow instructions in reasoning tasks), have received considerable attention, their abilities intrueinductivereasoningremainlargelyunexplored. To investigate the true inductive reasoning capabilities of LLMs, we propose a novel framework, SolverLearner. This framework enables LLMs to learn the underlying function (i.e., y = fw (x)), that maps input data points (x) to their corresponding output values(y), using only in-context examples. By focusing on inductive reasoning and separating it from LLM-baseddeductivereasoning,wecanisolate and investigate inductive reasoning of LLMs in its pure form viaSolverLearner. Our observationsrevealthatLLMsdemonstrateremarkable inductive reasoning capabilities throughSolver- Learner, achieving near-perfect performance with ACC of 1 in most cases. Surprisingly, despite their strong inductive reasoning abilities, LLMs tend to relatively lack deductive reasoning capabilities, particularly in tasks involving “counterfactual” reasoning.

<a id="p016"></a>
## P016 · DIVE: Towards Descriptive and Diverse Visual Commonsense Generation

- **作者**：Jun-Hyung Park; Hyuntae Park; Youjin Kang; Eojin Jeon; SangKeun Lee
- **时间**：本地版本：2024-08-15（arXiv:2408.08021v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：EMNLP 2023，pp.9677–9695（官方ACL记录核验）；本地arXiv上传时间2024-08-15晚于会议。 [ACL Anthology记录](https://aclanthology.org/2023.emnlp-main.601/)
- **论文链接**：[arXiv本地版本 2408.08021v1](https://arxiv.org/abs/2408.08021v1)
- **项目／代码／数据**：[代码：Park-ing-lot/DIVE](https://github.com/Park-ing-lot/DIVE)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：19页；SHA-256：`e888c768a6d50a1c93040f51ec1e578f60acca8697a9dbe7af12f1d0fcdb7a06`

### 中文摘要

通过过滤泛泛的推断并改进训练目标，让视觉常识生成更具体、多样。

### 核心贡献

提出 generic inference filtering 与 contrastive retrieval learning。

### 实现边界

主要验证于 Visual Commonsense Graphs；“人类水平”限定于所测描述性/多样性指标。

### Method／方法

利用频次及图像语义集中度过滤通用推断，再用图结构构造对比检索监督；在原始、unique、novel 子集及人评中比较。

### Results／主要结果

在 VCG 的描述性和多样性指标上超过所列基线；450 条推断的人类成对评价支持改进，但并未证明常识正确性达到人类水平。

### Shortcomings／局限与可能不足

【作者】主要只测 VCG，仍会产生与上下文无关的推断；【解读】过滤通用答案可能改变覆盖率，多样性不等于真实性。

### 证据定位

§3–4，表1–3；§4.3 人评；结论后局限。

### Abstract

Towards human-level visual understanding, visual commonsense generation has been introduced to generate commonsense inferences beyond images. However, current research on visual commonsense generation has overlooked an important human cognitive ability: generating descriptive and diverse inferences. In this work, we propose a novel visual commonsense generation framework, called DIVE, which aims to improve the descriptiveness and diversity of generated inferences. DIVE involves two methods, generic inference filtering and contrastive retrieval learning, which address the limitations of existing visual commonsense resources and training objectives. Experimental results verify that DIVE outperforms state-ofthe-art models for visual commonsense generation in terms of both descriptiveness and diversity, while showing a superior quality in generating unique and novel inferences. Notably, DIVE achieves human-level descriptiveness and diversity on Visual Commonsense Graphs. Furthermore, human evaluations confirm that DIVE aligns closely with human judgments on descriptiveness and diversity.

<a id="p017"></a>
## P017 · Exploring Defeasibility in Causal Reasoning

- **作者**：Shaobo Cui; Lazar Milikic; Yiyang Feng; Mete Ismayilzada; Debjit Paul; Antoine Bosselut; Boi Faltings
- **时间**：本地版本：2024-06-27（arXiv:2401.03183v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Findings of ACL 2024，pp.6433–6452（官方记录核验）。 [ACL Anthology记录](https://aclanthology.org/2024.findings-acl.384/)
- **论文链接**：[arXiv本地版本 2401.03183v2](https://arxiv.org/abs/2401.03183v2)
- **项目／代码／数据**：[代码：cui-shaobo/defeasibility-in-causality](https://github.com/cui-shaobo/defeasibility-in-causality)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：20页；SHA-256：`86878994aeac20a87a1e4ff2d654bf615daf836681fdd1cf128fdaa7b2919652`

### 中文摘要

研究新信息如何增强或削弱常识因果关系，提出 δ-CAUSAL 与 CESAR 评分。

### 核心贡献

约 11K 事件、10 个领域的可撤销因果数据；测量加入 supporter/defeater 后因果强度变化。

### 实现边界

文本常识因果关系的相对变化评价，不是通过干预数据估计因果效应。

### Method／方法

构造原因—结果及支持/反驳论据；以 token 级因果关联和注意力构建 CESAR，另测论据生成。

### Results／主要结果

捕捉强度变化的指标从基线 47.2% 提高到 80.1%，相对提升 69.7%；GPT-3.5 生成支持/反驳论据的人评分别比人类低 4.5/10.7 点。

### Shortcomings／局限与可能不足

【作者】分数用于定量解释存在限制，领域覆盖待扩展；【解读】基于语言关联的强度并非已校准的因果概率。

### 证据定位

摘要；§5 CESAR；§6；Limitations。

### Abstract

Defeasibility in causal reasoning implies that the causal relationship between cause and effect can be strengthened or weakened. Namely, the causal strength between cause and effect should increase or decrease with the incorporation of strengthening arguments (supporters) or weakening arguments (defeaters), respectively. However, existing works ignore defeasibility in causal reasoning and fail to evaluate existing causal strength metrics in defeasible settings. In this work, we present δ-CAUSAL, the first benchmark dataset for studying defeasibility in causal reasoning. δ-CAUSAL includes around 11K events spanning ten domains, featuring defeasible causality pairs, namely, cause-effect pairs accompanied by supporters and defeaters. We further show that current causal strength metrics fail to reflect the change of causal strength with the incorporation of supporters or defeaters in δ-CAUSAL. To this end, we propose CESAR (Causal Embedding a Ssociation with Attention Rating), a metric that measures causal strength based on token-level causal relationships. CESAR achieves a significant 69.7% relative improvement over existing metrics, increasing from 47.2% to 80.1% in capturing the causal strength change brought by supporters and defeaters. We further demonstrate even Large Language Models (LLMs) like GPT-3.5 still lag 4.5 and 10.7 points behind humans in generating supporters and defeaters, emphasizing the challenge posed by δ-CAUSAL.

<a id="p018"></a>
## P018 · Learning Iterative Reasoning through Energy Diffusion

- **作者**：Yilun Du; Jiayuan Mao; Joshua Tenenbaum
- **时间**：本地版本：2024-06-17（arXiv:2406.11179v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICML 2024（PDF 明示）
- **论文链接**：[arXiv本地版本 2406.11179v1](https://arxiv.org/abs/2406.11179v1)
- **项目／代码／数据**：[项目/演示页面](https://energy-based-model.github.io/ired)

- **主题**：世界机制与演化
- **PDF版本**：13页；SHA-256：`c68d47bc3b18df31bf9e8dc7aff3a0ea46cf4a94f6a634102cbad1e7462c8771`

### 中文摘要

IRED 通过退火能量景观与扩散训练提升迭代推理，允许测试时增加优化计算。

### 核心贡献

结合分数匹配与能量监督，降低 IREM 训练不稳定和优化困难。

### 实现边界

连续算法、数独、图连通和离散规划；未扩展验证到通用语言推理。

### Method／方法

学习多噪声级能量函数，用对比监督塑造低能量正确解；推理时沿退火景观迭代梯度优化。

### Results／主要结果

数独同分布/更难测试准确率为 99.4%/62.1%，IREM 为 93.5%/24.6%，RRN 为 99.8%/28.6%；说明主要优势在更难分布，非所有设置最优。

### Shortcomings／局限与可能不足

【作者】仍需许多梯度步，对需要中间记忆的任务可能不足；【解读】测试时扩算与鲁棒全局求解不同。

### 证据定位

§3；§4.2 表格 p7；§5 Conclusion and Discussions。

### Abstract

We introduce iterative reasoning through energy diffusion (IRED), a novel framework for learning to reason for a variety of tasks by formulating reasoning and decision-making problems with energy-based optimization. IRED learns energy functions to represent the constraints between input conditions and desired outputs. After training, IRED adapts the number of optimization steps during inference based on problem difficulty, enabling it to solve problems outside its training distribution — such as more complex Sudoku puzzles, matrix completion with large value magnitudes, and path finding in larger graphs. Key to our method’s success is two novel techniques: learning a sequence of annealed energy landscapes for easier inference and a combination of score function and energy landscape supervision for faster and more stable training. Our experiments show that IRED outperforms existing methods in continuous-space reasoning, discrete-space reasoning, and planning tasks, particularly in more challenging scenarios. Code and visualizations are at https://energy-based-model.github.io/ired.

<a id="p019"></a>
## P019 · NL-EYE: Abductive NLI for Images

- **作者**：Mor Ventura; Michael Toker; Nitay Calderon; Zorik Gekhman; Yonatan Bitton; Roi Reichart
- **时间**：本地版本：2024-10-03（arXiv:2410.02613v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：本地稿标注 Under review；arXiv v1：2024-10-03；不据此认定已被某会议接收
- **论文链接**：[arXiv本地版本 2410.02613v1](https://arxiv.org/abs/2410.02613v1)
- **项目／代码／数据**：[项目/演示页面](https://venturamor.github.io/NLEye/)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：27页；SHA-256：`45dd19e417d1745940b12cc81023a0b7891e578e4bcfc24b69fe07fdc4032a67`

### 中文摘要

把溯因 NLI 扩展到多图输入，要求比较后果/原因图像的合理性并解释选择。

### 核心贡献

350 个三元组、1,050 张人工策划合成图，覆盖物理、功能、逻辑、情绪、文化和社会推理。

### 实现边界

受控合成图像比较任务；事故预防和生成视频验证是潜在应用，未作为系统实现验证。

### Method／方法

人工撰写场景并迭代文生图；比较 triplet/pair 设置、合理性预测及解释，分析纯视觉和文本替代条件。

### Results／主要结果

被测 VLM 在多项设置接近随机基线，人类在合理性和解释质量上明显更好；结果限于本地版本使用的模型与测试集。

### Shortcomings／局限与可能不足

【作者】常识标签存在文化/社会偏差，合成图仍可能含敏感内容；【解读】样本小、图像生成伪影与推理难度可能耦合。

### 证据定位

摘要；§2–4；结果 §5；失败分析 §6；Ethics。

### Abstract

Will a Visual Language Model (VLM)-based bot warn us about slipping if it detects a wet floor? Recent VLMs have demonstrated impressive capabilities, yet their ability to infer outcomes and causes remains underexplored. To address this, we introduce NL-E YE, a benchmark designed to assess VLMs’ visual abductive reasoning skills. NL-E YE adapts the abductive Natural Language Inference (NLI) task to the visual domain, requiring models to evaluate the plausibility of hypothesis images based on a premise image and explain their decisions. NL-E YE consists of 350 carefully curated triplet examples (1,050 images) spanning diverse reasoning categories: physical, functional, logical, emotional, cultural, and social. The data curation process involved two steps—writing textual descriptions and generating images using text-to-image models, both requiring substantial human involvement to ensure high-quality and challenging scenes. Our experiments show that VLMs struggle significantly on NL-E YE, often performing at random baseline levels, while humans excel in both plausibility prediction and explanation quality. This demonstrates a deficiency in the abductive reasoning capabilities of modern VLMs. NL-E YE represents a crucial step toward developing VLMs capable of robust multimodal reasoning for real-world applications, including accident-prevention bots and generated video verification.

<a id="p020"></a>
## P020 · ViCor: Bridging Visual Understanding and Commonsense Reasoning with Large Language Models

- **作者**：Kaiwen Zhou; Kwonjoon Lee; Teruhisa Misu; Xin Eric Wang
- **时间**：本地版本：2024-05-17（arXiv:2310.05872v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Findings of ACL 2024，pp.10783–10795（官方记录核验）；本地末位作者名Xin Eric Wang，ACL记录简写Xin Wang。 [ACL Anthology记录](https://aclanthology.org/2024.findings-acl.640/)
- **论文链接**：[arXiv本地版本 2310.05872v2](https://arxiv.org/abs/2310.05872v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：12页；SHA-256：`4503d215534a2016f3544189c73da3f8d25b8d674ba4dd04c05280d32364d827`

### 中文摘要

区分直接视觉理解与超出画面的常识推断，让 LLM 选择并指挥合适的视觉处理路线。

### 核心贡献

任务分类加主动视觉取证的 VLM/LLM 协作流程。

### 实现边界

VCR 和 A-OKVQA 四选一；不做域内微调，但依赖多个预训练模型及 in-context 示例。

### Method／方法

先从图像描述评估候选；不确定时由 LLM 分类为 VCU/VCI，调用 BLIP2 直接匹配或询问关键视觉因素，再重新推理。

### Results／主要结果

在论文所测无需域内微调的方法中表现最好；分析中 VCU 的 VLM/LLM+caption 平均准确率 63.6%/56.0%，VCI 为 50.5%/53.6%。

### Shortcomings／局限与可能不足

【作者】文本沟通丢失视觉细节、仍落后最佳监督模型；VCR 主方法比较仅 500 个样本，受 GPT-4 调用成本限制。

### 证据定位

§4；§5.1–5.2；§6；§8。

### Abstract

In our work, we explore the synergistic capabilities of pre-trained vision-and-language models (VLMs) and large language models (LLMs) on visual commonsense reasoning (VCR) problems. We find that VLMs and LLMs-based decision pipelines are good at different kinds of VCR problems. Pre-trained VLMs exhibit strong performance for problems involving understanding the literal visual content, which we noted as visual commonsense understanding (VCU). For problems where the goal is to infer conclusions beyond image content, which we noted as visual commonsense inference (VCI), VLMs face difficulties, while LLMs, given sufficient visual evidence, can use commonsense to infer the answer well. We empirically validate this by letting LLMs classify VCR problems into these two categories and show the significant difference between VLM and LLM with image caption decision pipelines on two subproblems. Moreover, we identify a challenge with VLMs’ passive perception, which may miss crucial context information, leading to incorrect reasoning by LLMs. Based on these, we suggest a collaborative approach, named ViCor, where pre-trained LLMs serve as problem classifiers to analyze the problem category, then either use VLMs to answer the question directly or actively instruct VLMs to concentrate on and gather relevant visual elements to support potential commonsense inferences. We evaluate our framework on two VCR benchmark datasets and outperform all other methods that do not require in-domain fine-tuning.

<a id="p021"></a>
## P021 · Black Swan: Abductive and Defeasible Video Reasoning in Unpredictable Events

- **作者**：Aditya Chinchure; Sahithya Ravi; Raymond Ng; Vered Shwartz; Boyang Li; Leonid Sigal
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CVPR 2025（PDF 元数据及官方记录）
- **项目／代码／数据**：[项目/演示页面](https://blackswan.cs.ubc.ca)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：10页；SHA-256：`91efca47ea0eadf531cb7523e3cf6f4016d01a79de26626f2b5748c87ecfc46d`

### 中文摘要

以反常视频事件检验模型能否解释隐藏事件，以及获得新证据后修正原先假设。

### 核心贡献

BlackSwanSuite 包含 1,655 个视频、超过 3,800 个选择题、4,900 个生成题和 6,700 个是非题。

### 实现边界

通过遮蔽或揭示视频片段构建 Forecaster/Detective/Reporter；是评测基准，未提出训练后消除缺陷的新模型。

### Method／方法

分阶段给出视觉证据，评估溯因和可撤销推理；使用选择题准确率、CLIP/LLM 生成指标及人类评价。

### Results／主要结果

表2 Detective MCQ：GPT-4o 65.1%、人类 90.0%，相差 24.9 个百分点；Reporter Y/N 为 60.1% vs 92.0%。注意本地表2图注与表头存在任务名称不一致，以上按表头及正文解释。

### Shortcomings／局限与可能不足

【解读】反常事件样本有选择偏差，感知失败与推理失败相互影响；开放式解释评价依赖参考与评价器。

### 证据定位

§3–5；表2和 §6.1；§7–8。

### Abstract

The commonsense reasoning capabilities of visionlanguage models (VLMs), especially in abductive reasoning and defeasible reasoning, remain poorly understood. Most benchmarks focus on typical visual scenarios [ 1, 23, 42], making it difficult to discern whether model performance stems from keen perception and reasoning skills, or reliance on pure statistical recall. We argue that by focusing on atypical events in videos, clearer insights can be gained on the core capabilities of VLMs. Explaining and understanding such out-of-distribution events requires models to extend beyond basic pattern recognition and regurgitation of their prior knowledge. To this end, we introduce Black- SwanSuite, a benchmark for evaluating VLMs’ ability to reason about unexpected events through abductive and defeasible tasks. Our tasks artificially limit the amount of visual information provided to models while questioning them about hidden unexpected events, or provide new visual information that could change an existing hypothesis about the event. We curate a comprehensive benchmark suite comprising over 3,800 MCQ, 4,900 generative and 6,700 yes/no questions, spanning 1,655 videos. After extensively evaluating various state-of-the-art VLMs, including GPT-4o and Gemini 1.5 Pro, as well as open-source VLMs such as LLaVA-Video, we find significant performance gaps of up to 32% from humans on these tasks. Our findings reveal key limitations in current VLMs, emphasizing the need for enhanced model architectures and training strategies. Our data and leaderboard is available at https://blackswan.cs.ubc.ca.

<a id="p022"></a>
## P022 · Enabling Self-Improving Agents to Learn at Test Time With Human-In-The-Loop Guidance

- **作者**：Yufei He; Ruoyu Li; Alex Chen; Yue Liu; Yulin Chen; Yuan Sui; Cheng Chen; Yi Zhu; Luca Luo; Frank Yang; Bryan Hooi
- **时间**：本地版本：2025-10-10（arXiv:2507.17131v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：EMNLP 2025 Industry Track，pp.1625–1653（官方记录核验）；正文结果按本地arXiv v2。 [ACL Anthology记录](https://aclanthology.org/2025.emnlp-industry.115/)
- **论文链接**：[arXiv本地版本 2507.17131v2](https://arxiv.org/abs/2507.17131v2)
- **项目／代码／数据**：[代码：yf-he/aria](https://github.com/yf-he/aria)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：30页；SHA-256：`9a42692cacd30f0379aaa6d69bbbc4370208f53e0c08516c6d8fe84cd268ce0b`

### 中文摘要

ARIA 识别知识缺口、向专家求助并维护带时间戳的知识库，以适应运行中变化的规则。

### 核心贡献

将主动询问、冲突消解和时效性知识更新结合，用于动态名称筛查与合同理解。

### 实现边界

更新主要是外部知识库；TikTok Pay 部署和用户覆盖是论文自述，不能将平台月活当作实验人数；公开 CUAD 实验用 LLM 模拟专家。

### Method／方法

自对话评估不确定性，在查询预算内请求解释/纠错；抽取知识、加时间戳，检测冲突并澄清后检索用于后续决策。

### Results／主要结果

真实序列测试为 11,846 例（156 阳性）；CUAD 在 B=2000 时 GPT-4o+ARIA 准确率 0.6358，静态模型 0.4872，RAG 0.5735。

### Shortcomings／局限与可能不足

【作者】依赖专家反馈质量和预算，运行开销未充分评测；【解读】模拟专家与人工长期使用存在差异。

### 证据定位

§4；表1；§6.1–6.2/表4；Limitations。

### Abstract

Large language model (LLM) agents often struggle in environments where rules and required domain knowledge frequently change, such as regulatory compliance and user risk screening. Current approaches—like offline fine-tuning and standard prompting—are insufficient because they cannot effectively adapt to new knowledge during actual operation. To address this limitation, we propose theAdaptive ReflectiveInteractiveAgent (ARIA) 1, an LLM agent framework designed specifically to continuously learn updated domain knowledge at test time. ARIA assesses its own uncertainty through structured self-dialogue, proactively identifying knowledge gaps and requesting targeted explanations or corrections from human experts. It then systematically updates an internal, timestamped knowledge repository with provided human guidance, detecting and resolving conflicting or outdated knowledge through comparisons and clarification queries. We evaluate ARIA on the realistic customer due diligence name screening task on TikTok Pay, alongside publicly available dynamic knowledge tasks. Results demonstrate significant improvements in adaptability and accuracy compared to baselines using standard offline fine-tuning and existing self-improving agents.ARIA is deployed within TikTok Pay serving over 150 million monthly active users, confirming its practicality and effectiveness for operational use in rapidly evolving environments.

<a id="p023"></a>
## P023 · Generalizable Reasoning through Compositional Energy Minimization

- **作者**：Alexandru Oarga; Yilun Du
- **时间**：本地版本：2025-10-23（arXiv:2510.20607v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：NeurIPS 2025 Main Conference Track（官方论文集核验）。 [NeurIPS官方论文集](https://proceedings.neurips.cc/paper_files/paper/2025/hash/7b22ed7325629fd4c041d47139410fd9-Abstract-Conference.html)
- **论文链接**：[arXiv本地版本 2510.20607v1](https://arxiv.org/abs/2510.20607v1)
- **项目／代码／数据**：[项目/演示页面](https://alexoarga.github.io/compositional_reasoning/)

- **主题**：世界机制与演化
- **PDF版本**：22页；SHA-256：`26f0122c9977bee78286c8587ae868a3fe2db86dc60f7dabe4a4710c6ac3f5f9`

### 中文摘要

先学习小子问题的能量函数，再在测试时组合约束求解更大、更复杂的问题。

### 核心贡献

组合能量景观与 Parallel Energy Minimization（PEM），支持增加约束和计算预算。

### 实现边界

N-Queens、3-SAT、图着色和填字；子问题分解由任务结构提供，不是自动发现任意问题分解。

### Method／方法

扩散与对比损失训练局部能量函数；求和形成全局目标，用多个并行候选进行能量最小化和筛选。

### Results／主要结果

只用一个 8 皇后训练实例时，P=1024 的方法在 100 次生成中得到 97 个有效解，表1最强比较设置为 41 个。

### Shortcomings／局限与可能不足

【作者】高斯初始化/增量限制，图着色仍未充分达到最优；【解读】并行采样成本显著，不能把 97% 视为单一低成本轨迹成功率。

### 证据定位

§3；表1 p6；§4；§5。

### Abstract

Generalization is a key challenge in machine learning, specifically in reasoning tasks, where models are expected to solve problems more complex than those encountered during training. Existing approaches typically train reasoning models in an end-to-end fashion, directly mapping input instances to solutions. While this allows models to learn useful heuristics from data, it often results in limited generalization beyond the training distribution. In this work, we propose a novel approach to reasoning generalization by learning energy landscapes over the solution spaces of smaller, more tractable subproblems. At test time, we construct a global energy landscape for a given problem by combining the energy functions of multiple subproblems. This compositional approach enables the incorporation of additional constraints during inference, allowing the construction of energy landscapes for problems of increasing difficulty. To improve the sample quality from this newly constructed energy landscape, we introduce Parallel Energy Minimization (PEM). We evaluate our approach on a wide set of reasoning problems. Our method outperforms existing state-of-the-art methods, demonstrating its ability to generalize to larger and more complex problems. Project website can be found at:https://alexoarga.github.io/compositional_reasoning/

<a id="p024"></a>
## P024 · Nested Learning: The Illusion of Deep Learning Architecture

- **作者**：Ali Behrouz; Meisam Razaviyayn; Peilin Zhong; Vahab Mirrokni
- **时间**：本地版本：2025-12-31（arXiv:2512.24695v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：NeurIPS 2025 Main Conference Track（官方论文集核验）；正式题名末词Architectures为复数，本地首页Architecture为单数。 [NeurIPS官方论文集](https://proceedings.neurips.cc/paper_files/paper/2025/hash/4309616aaed8e848009bc4a7ef73b493-Abstract-Conference.html)
- **论文链接**：[arXiv本地版本 2512.24695v1](https://arxiv.org/abs/2512.24695v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：52页；SHA-256：`e87a9ce82ff24e96f55b83fb9713a5d6fc9e4a1a232c12d42da49c10022ed891`

### 中文摘要

把网络、优化器和记忆统一为不同更新频率的嵌套优化过程，并据此设计连续记忆系统和 Hope。

### 核心贡献

提出 NL 视角、表达力更强的优化器、自修改学习模块和 Continuum Memory System。

### 实现边界

提供理论重述与具体原型实验；作者明确表示未普遍解决灾难性遗忘。标题按首页单数 Architecture，元数据为 Architectures。

### Method／方法

将梯度/上下文压缩解释为关联记忆；设计多个时间尺度更新的 MLP 记忆、M3 优化器，以及结合自指 Titans 的 Hope。

### Results／主要结果

在语言建模、知识更新、形式语言和长上下文任务中展示收益；如表1 16K UUID 检索 Hope 24.8%、Titans 21.2%、Transformer 40.8%，说明优势取决于任务，非全面领先。

### Shortcomings／局限与可能不足

【作者】有限容量的压缩仍带来遗忘；【解读】新概念的统一性不等于普适能力保证，需分别评价各组件、参数量和训练预算。

### 证据定位

§3–8；§9、表1–5；§10 的 Is Catastrophic Forgetting Solved?。

### Abstract

Over the last decades, developing more powerful neural architectures and simultaneously designing optimization algorithms to effectively train them have been the core of research efforts to enhance the capability of machine learning models. Despite the recent progresses, particularly in developing Language Models (LMs), there are fundamental challenges and unanswered questions about how such models cancontinually learn/memorize, self-improve, and find effective solutions. In this paper, we present a new learning paradigm, called Nested Learning (NL), that coherently represents a machine learning model with a set of nested, multi-level, and/or parallel optimization problems, each of which with its own “context flow”. Through the lenses of NL, existing deep learning methods learns from data throughcompressingtheir own context flow, andin-context learningnaturally emerges in large models. NL suggests a philosophy to design more expressive learning algorithms with more “levels”, resulting in higher-order in-context learning and potentially unlocking effective continual learning capabilities. In addition to its neuro-scientific motivation, we advocate for NL by presenting three core contributions: (1) Expressive Optimizers: We show that known gradient-based optimizers, such as Adam, SGD with Momentum, etc., are in fact associative memory modules that aim to compress the gradients’ information (by gradient descent). Building on this insight, we present other “more expressive" optimizers with deep memory and/or more powerful learning rules; (2) Self-Modifying Learning Module: Taking advantage of NL’s insights on learning algorithms, we present a sequence model that learns how to modify itself by learning its own update algorithm; and (3) Continuum Memory System: We present a new formulation for memory system that generalizes the traditional viewpoint of “long-term/short-term memory”. Combining our self-modifying sequence model with the continuum memory system, we present a continual learning module, calledHope, showing promising results in language modeling, knowledge incorporation, and few-shot generalization tasks, continual learning, and long-context reasoning tasks.

<a id="p025"></a>
## P025 · Reasoning with Sampling: Your Base Model is Smarter Than You Think

- **作者**：Aayush Karan; Yilun Du
- **时间**：本地版本：2025-10-16（arXiv:2510.14901v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2510.14901v1（本地版本）；正式会议/期刊未核实
- **论文链接**：[arXiv本地版本 2510.14901v1](https://arxiv.org/abs/2510.14901v1)
- **项目／代码／数据**：[项目/演示页面](https://aakaran.github.io/reasoning_with_sampling/)；[代码：aakaran/reasoning-with-sampling](https://github.com/aakaran/reasoning-with-sampling)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：20页；SHA-256：`8f029968f20292b320dda95d253911a187e34a18d33aa6cdc65883b9cc1a47d4`

### 中文摘要

不训练模型或使用验证器，而通过基础模型自身似然驱动的采样提升推理表现。

### 核心贡献

用自回归 MCMC 近似从幂分布采样，研究 RL 后训练之外的能力激发方式。

### 实现边界

需要访问模型似然和反复生成/打分；single-shot 指最终提交一条答案，不代表只进行一次采样计算。

### Method／方法

按块扩展序列，随机位置重采样后缀，用 Metropolis–Hastings 接受率逼近 p(x)^α；测试数学、代码、科学及一般帮助性。

### Results／主要结果

MATH500/GPQA 上部分设置接近 GRPO，HumanEval 和 AlpacaEval 部分设置更高；保持较好的多样性。收益需结合模型与采样预算看表1，不能统一为所有模型提升同一百分比。

### Shortcomings／局限与可能不足

【作者/设定】精确幂分布采样不可行，采用近似且计算昂贵；【解读】高似然并非正确性保证，省训练不等于省总算力。

### 证据定位

§4 算法1；§5.2 表1；计算分析及 §6。

### Abstract

Frontier reasoning models have exhibited incredible capabilities across a wide array of disciplines, driven by posttraining large language models (LLMs) with reinforcement learning (RL). However, despite the widespread success of this paradigm, much of the literature has been devoted to disentangling truly novel behaviors that emerge during RL but are not present in the base models. In our work, we approach this question from a different angle, instead asking whether comparable reasoning capabilites can be elicited from base models at inference time by pure sampling,without any additional training. Inspired by Markov chain Monte Carlo (MCMC) techniques for sampling from sharpened distributions, we propose a simple iterative sampling algorithm leveraging the base models’ own likelihoods. Over different base models, we show that our algorithm offers substantial boosts in reasoning that nearly match and even outperform those from RL on a wide variety of single-shot tasks, including MATH500, HumanEval, and GPQA. Moreover, our sampler avoids the collapse in diversity over multiple samples that is characteristic of RL-posttraining. Crucially, our method does not require training, curated datasets, or a verifier, suggesting broad applicability beyond easily verifiable domains.

<a id="p026"></a>
## P026 · Training Large Language Models to Reason in a Continuous Latent Space

- **作者**：本地稿匿名（Anonymous authors）；实名版本见 P103/P109
- **时间**：本地匿名稿未注明日期；ICLR 2025是投稿轮次，不作为正式发表时间
- **发表平台／版本状态**：Under review as a conference paper at ICLR 2025（匿名投稿版本，不能据此视作接收）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P103](#p103)/[P109](#p109)为同一COCONUT工作；本地15页匿名版与18页署名版分别记录，不能作为两项独立证据。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：15页；SHA-256：`4d75acf8306a57d2554cae06f6842f73ecde9b3c4176684508ed6be077b0958d`

### 中文摘要

COCONUT 把隐藏状态直接反馈为下一输入，实现不经文字解码的连续潜在推理。

### 核心贡献

连续 thought 的循环计算与逐阶段替换文本 CoT 的训练方案。

### 实现边界

基于 GPT-2，在 GSM8K、ProntoQA、ProsQA 验证；正文明确把每个连续 thought 计为一个计算 token。

### Method／方法

从语言 CoT 监督开始，逐步以隐藏向量取代早期推理步骤，保留可输出答案的语言阶段；用 ProsQA 分析潜在搜索分支。

### Results／主要结果

各任务优于 no-CoT，ProsQA 上超过文本 CoT，生成步数较少；不能据此称所有任务优于 CoT。具体实名版本数值见 P103，避免混用版本表格。

### Shortcomings／局限与可能不足

【解读】潜在状态不易审计，训练需推理轨迹与阶段设置；类似 BFS 的证据来自受控逻辑任务，不是任意问题的搜索保证。

### 证据定位

§3；§4/表1；§5 潜在搜索树；本地匿名封面。

### Abstract

Large language models are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thoughts (CoT) to solve a complex reasoning problem. However, we argue that language space may not be the optimal reasoning space. For example, most word tokens are primarily for textual coherence and not essential for reasoning, while some critical tokens require complex planning and pose huge challenges to LLMs. To explore the potential of LLM reasoning in an unrestricted latent space instead of using human language, we introduce a new paradigm C OCONUT (Chain of Continuous Thought). We utilize the last hidden state of the LLM as a representation of the reasoning state (termed “continuous thought”). Rather than decoding this into a word token, we feed it back to the LLM as the subsequent input embedding directly in the continuous space. Experiments show that C OCONUT can effectively augment the LLM on several reasoning tasks. It even outperforms CoT in certain logical reasoning tasks that require substantial planning, despite generating fewer tokens during inference. More interestingly, we observe an advanced reasoning patterns emerging from latent reasoning: the continuous thought can encode multiple potential next reasoning steps, allowing the model to perform a breadth-first search (BFS) to solve the problem, rather than prematurely committing to a single deterministic path like CoT. These findings demonstrate the promise of latent reasoning and offer valuable insights for future research on latent reasoning methods.

<a id="p027"></a>
## P027 · VCD: A Dataset for Visual Commonsense Discovery in Images

- **作者**：Xiangqing Shen; Fanfan Wang; Siwei Wu; Rui Xia
- **时间**：本地版本：2025-06-05（arXiv:2402.17213v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Findings of ACL 2025（官方记录核验）；本地arXiv:2402.17213v2。 [ACL Anthology记录](https://aclanthology.org/2025.findings-acl.290/)
- **论文链接**：[arXiv本地版本 2402.17213v2](https://arxiv.org/abs/2402.17213v2)
- **项目／代码／数据**：[代码：NUSTM/VCD](https://github.com/NUSTM/VCD)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：16页；SHA-256：`8fde486cc3f7096a777b415c3b45f71bd4d074255948644b0f7daf9eeea921da`

### 中文摘要

VCD 将物体框与可见、不可见常识三元组连接，支持图像中的常识发现。

### 核心贡献

超过 100K 图片、14M 物体—常识对，以及 Seen/Unseen、Property/Action/Space 层级分类；训练 VCM 基线。

### 实现边界

静态图片、区域级常识生成；尚未覆盖视频时序和动态因果。

### Method／方法

结合 Visual Genome 与 ConceptNet，映射/扩展三元组并进行质量控制，再用指令微调视觉语言模型生成常识。

### Results／主要结果

ImageNetVC 平均分由 OFA 80.7 到 VCM 83.5；Qwen-VL-7B 加常识后 OK-VQA 从 58.6 到 60.0。人评对 GPT-4o 的 Unseen 胜/平/负为 41%/29%/30%。

### Shortcomings／局限与可能不足

【作者】下游验证较简单、仅静态图像；【解读】大量自动构造常识可能保留知识库偏差，规模不代表每条均正确。

### 证据定位

§3；表3–5；Limitations。

### Abstract

Visual commonsense plays a vital role in understanding and reasoning about the visual world. While commonsense knowledge bases like ConceptNet provide structured collections of general facts, they lack visually grounded representations. Scene graph datasets like Visual Genome, though rich in object-level descriptions, primarily focus on directly observable information and lack systematic categorization of commonsense knowledge. We present Visual Commonsense Dataset ( VCD), a large-scale dataset containing over 100,000 images and 14 million object-commonsense pairs that bridges this gap. VCD introduces a novel three-level taxonomy for visual commonsense, integrating both Seen (directly observable) and Unseen (inferrable) commonsense across Property, Action, and Space aspects. Each commonsense is represented as a triple where the head entity is grounded to object bounding boxes in images, enabling scenedependent and object-specific visual commonsense representation. To demonstrate VCD’s utility, we develop VCM, a generative model that combines a vision-language model with instruction tuning to discover diverse visual commonsense from images. Extensive evaluations demonstrate both the high quality of VCD and its value as a resource for advancing visually grounded commonsense understanding and reasoning. Our dataset and code will be released on https://github.com/NUSTM/VCD.

<a id="p028"></a>
## P028 · Video models are zero-shot learners and reasoners

- **作者**：Thaddäus Wiedemer; Yuxuan Li; Paul Vicol; Shixiang Shane Gu; Nick Matarese; Kevin Swersky; Been Kim; Priyank Jaini; Robert Geirhos
- **时间**：本地版本：2025-09-29（arXiv:2509.20328v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Google DeepMind研究预印稿；首页2025-10-01；arXiv:2509.20328v2时间2025-09-29
- **论文链接**：[arXiv本地版本 2509.20328v2](https://arxiv.org/abs/2509.20328v2)
- **项目／代码／数据**：[项目/演示页面](https://video-zero-shot.github.io/)

- **主题**：世界机制与演化
- **PDF版本**：46页；SHA-256：`e4bb6ec0a03c7a08e7fedf5beb10e54fbdbb54f6de4569fbb87883ad8b498219`

### 中文摘要

探索 Veo 3 能否仅通过提示执行感知、操作和视觉推理任务，提出视频模型具备通用视觉能力的早期证据。

### 核心贡献

跨任务定性探索及 7 类任务定量评估，涵盖分割、边缘检测、编辑、迷宫、对称和类比。

### 实现边界

Veo API 连同 LLM prompt rewriter 作为黑盒；作者承认部分答案可能来自重写器。best-frame 和 pass@10 不是单次最终输出表现。

### Method／方法

输入图像及任务提示生成 8 秒视频，再按任务读取最好/最后一帧；比较 Veo 2、Veo 3 和图像/语言基线。

### Results／主要结果

Veo 3 在多任务中明显优于 Veo 2，增加尝试次数提升成功率；边缘检测在 BIPEDv2 的 50 张测试图评测，分割只测 50 张较容易的 LVIS 图。

### Shortcomings／局限与可能不足

【作者/设定】专用模型仍更强、成功不稳定，训练数据不可见；【解读】挑最好帧/多次尝试会高估实际可直接使用的可靠性。

### 证据定位

§2；§4 及图3–9；§5。

### Abstract

The remarkable zero-shot capabilities of Large Language Models (LLMs) have propelled natural language processing from task-specific models to unified, generalist foundation models. This transformation emerged from simple primitives: large, generative models trained on web-scale data. Curiously, the same primitives apply to today’s generative video models. Could video models be on a trajectory towards general-purposevisionunderstanding, much like LLMs developed general-purposelanguage understanding? We demonstrate that Veo 3 can solve a broad variety of tasks it wasn’t explicitly trained for: segmenting objects, detecting edges, editing images, understanding physical properties, recognizing object affordances, simulating tool use, and more. These abilities to perceive, model, and manipulate the visual world enable early forms of visual reasoning like maze and symmetry solving. Veo’s emergent zero-shot capabilities indicate that video models are on a path to becoming unified, generalist vision foundation models.

<a id="p029"></a>
## P029 · VideoDiff: Human-AI Video Co-Creation with Alternatives

- **作者**：Mina Huh; Ding Li; Kim Pimmel; Hijung Valentina Shin; Amy Pavel; Mira Dontcheva
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CHI 2025，2025-04-26 至 05-01；DOI 10.1145/3706598.3713417
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3706598.3713417)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全
- **PDF版本**：19页；SHA-256：`4387e6879b388b1371bad2857839323e56437fdc255065cc2245000586305adc`

### 中文摘要

用对齐时间轴、转录文本和差异高亮，帮助视频创作者比较、筛选和修改多种 AI 剪辑方案。

### 核心贡献

围绕 rough cut、B-roll 和文字效果的多方案共创交互。

### 实现边界

对用户已有素材提供编辑建议/组合，未训练新的通用视频生成模型。

### Method／方法

8 名专业创作者形成性研究；实现 React/D3/Remotion 界面，Whisper 转录与 GPT-4o 编辑建议；12 人被试内对照和 3 个真实素材案例。

### Results／主要结果

对“理解差异的有用性”评价均值为 4.92 vs 基线 2.25（p&lt;0.05）；参与者更易比较和定制，并报告更满意的创作结果。

### Shortcomings／局限与可能不足

【解读】小样本短期研究，比较的是特定基线；转录/语言主导流程可能遗漏视觉细节，偏好与专业成片质量不同。

### 证据定位

§3；§4.3；§5.1–5.3；§6–7。

### Abstract

To make an engaging video, people sequence interesting moments and add visuals such as B-rolls or text. While video editing requires time and effort, AI has recently shown strong potential to make editing easier through suggestions and automation. A key strength of generative models is their ability to quickly generate multiple variations, but when provided with many alternatives, creators struggle to compare them to find the best fit. We propose VideoDiff, an AI video editing tool designed for editing with alternatives. With VideoDiff, creators can generate and review multiple AI recommendations for each editing process: creating a rough cut, inserting B-rolls, and adding text effects. VideoDiff simplifies comparisons by aligning videos and highlighting differences through timelines, transcripts, and video previews. Creators have the flexibility to regenerate and refine AI suggestions as they compare alternatives. Our study participants (N=12) could easily compare and customize alternatives, creating more satisfying results.

<a id="p030"></a>
## P030 · AbductiveMLLM: Boosting Visual Abductive Reasoning Within MLLMs

- **作者**：Boyu Chang; Qi Wang; Xi Guo; Zhixiong Nan; Yazhou Yao; Tianfei Zhou
- **时间**：本地版本：2026-01-06（arXiv:2601.02771v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：AAAI 2026，40(4):2698–2706；正式上线2026-03-14，DOI 10.1609/aaai.v40i4.37258（AAAI官方核验）；本地为arXiv v1。 [AAAI官方论文页](https://ojs.aaai.org/index.php/AAAI/article/view/37258)
- **论文链接**：[arXiv本地版本 2601.02771v1](https://arxiv.org/abs/2601.02771v1)；[DOI正式记录](https://doi.org/10.1609/aaai.v40i4.37258)
- **项目／代码／数据**：[代码：ChangPtR/AbdMLLM](https://github.com/ChangPtR/AbdMLLM)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：9页；SHA-256：`2e9d58f9985c584aa48d97dbf51d1f7b98f81da5cc7bacd01997e66b8e388ea0`

### 中文摘要

结合语言假设筛选与图像想象，增强多模态模型对缺失视觉事件的溯因推理。

### 核心贡献

REASONER 与 IMAGINER 双模块联合学习：前者筛选假设，后者用扩散视觉表示辅助解释。

### 实现边界

标准 VAR 任务中的解释生成；想象画面属于条件生成，不能作为对真实隐藏事件的新观测证据。

### Method／方法

LLM 根据视频描述提出候选，经因果相关对比学习筛选；条件扩散模块通过适配器融合视频和推理表示，联合优化语言与图像分支。

### Results／主要结果

作者在标准 VAR 基准报告优于所列传统模型和 MLLM；消融显示去掉 IMAGINER 或其适配器会降低 CIDEr 等生成指标。

### Shortcomings／局限与可能不足

【解读】生成图像可能强化错误假设；依赖视频描述、候选覆盖和训练数据，自动文本指标不直接证明因果解释正确。

### 证据定位

摘要；REASONER/IMAGINER 方法；实验表格；表6及结论。

### Abstract

Visual abductive reasoning (V AR) is a challenging task that requires AI systems to infer the most likely explanation for incomplete visual observations. While recent MLLMs develop strong general-purpose multimodal reasoning capabilities, they fall short in abductive inference, as compared to human beings. To bridge this gap, we draw inspiration from the interplay between verbal and pictorial abduction in human cognition, and propose to strengthen abduction of MLLMs by mimicking such dual-mode behavior. Concretely, we introduceAbductiveMLLMcomprising of two synergistic components: REASONERand IMAGINER. The REASONERoperates in the verbal domain. It first explores a broad space of possible explanations using a blind LLM and then prunes visually incongruent hypotheses based on cross-modal causal alignment. The remaining hypotheses are introduced into the MLLM as targeted priors, steering its reasoning toward causally coherent explanations. The IMAGINER, on the other hand, further guides MLLMs by emulating human-like pictorial thinking. It conditions a text-to-image diffusion model on both the input video and the REASONER’s output embeddings to “imagine” plausible visual scenes that correspond to verbal explanation, thereby enriching MLLMs’ contextual grounding. The two components are trained jointly in an end-to-end manner. Experiments on standard V AR benchmarks show thatAbductiveMLLMachieves state-of-the-art performance, consistently outperforming traditional solutions and advanced MLLMs. Code— https://github.com/ChangPtR/AbdMLLM

<a id="p031"></a>
## P031 · Agentic Reasoning for Large Language Models

- **作者**：Tianxin Wei; Ting-Wei Li; Zhining Liu; Xuying Ning; Ze Yang; Jiaru Zou; Zhichen Zeng; Ruizhong Qiu; Xiao Lin; Dongqi Fu; Zihao Li; Mengting Ai; Duo Zhou; Wenxuan Bao; Yunzhe Li; Gaotang Li; Cheng Qian; Yu Wang; Xiangru Tang; Yin Xiao; Liri Fang; Hui Liu; Xianfeng Tang; Yuji Zhang; Chi Wang; Jiaxuan You; Heng Ji; Hanghang Tong; Jingrui He
- **时间**：本地版本：2026-01-18（arXiv:2601.12538v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2601.12538v1，2026-01-18（本地综述稿）
- **论文链接**：[arXiv本地版本 2601.12538v1](https://arxiv.org/abs/2601.12538v1)
- **项目／代码／数据**：[代码：weitianxin/Awesome-Agentic-Reasoning](https://github.com/weitianxin/Awesome-Agentic-Reasoning)

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：135页；SHA-256：`edc82b75fe0496cb13bf8288aac941e4437dc136a82b2dce4a7ab55d130db916`

### 中文摘要

系统梳理将推理与行动连接的语言智能体研究，覆盖基础能力、自我演化和多智能体协作。

### 核心贡献

按环境动态、优化方式与协作范围组织统一分类及应用/基准地图。

### 实现边界

135 页综述，正文说明汇总截至 2025 年的进展；没有训练或统一重测一个新模型。

### Method／方法

分别梳理规划/工具/搜索、反馈/记忆/适应、角色/分工/协作演化，区分上下文编排与 SFT/RL 后训练，并整理跨领域基准。

### Results／主要结果

产出研究分类、方法对照表和开放问题：个性化、长时交互、世界模型、潜在推理与协作治理；没有可归于本文新算法的单一准确率。

### Shortcomings／局限与可能不足

【解读】文献选择和分类含作者判断，跨论文成绩并非同条件比较，快速发展的领域需要持续更新。

### 证据定位

摘要；§2–5；应用 §6；基准 §7；开放问题 §8。

### Abstract

Reasoning is a fundamental cognitive process underlying inference, problem-solving, and decisionmaking. While large language models (LLMs) demonstrate strong reasoning capabilities in closed-world settings, exemplified by standard benchmarks in mathematics and code, they struggle in open-ended and dynamic environments. The emergence ofagentic reasoningmarks a paradigm shift, bridging thought and action by reframing LLMs as autonomous agents that plan, act, and learn through continual interaction. In this survey, we provide a systematic roadmap by organizing agentic reasoning along three complementary dimensions. First, we characterize environmental dynamics through three layers:foundational agentic reasoning establishes core single-agent capabilities, including planning, tool use, and search, that operate in stable environments;self-evolving agentic reasoningexamines how agents refine these capabilities through feedback, memory, and adaptation in evolving settings; andcollective multi-agent reasoningextends intelligence to collaborative scenarios where multiple agents coordinate roles, share knowledge, and pursue shared goals. Across all layers, we analyze system constraints and optimization settings by distinguishingin-context reasoning, which scales test-time interaction through structured orchestration and adaptive workflow design, fromposttraining reasoning, which optimizes behaviors through reinforcement learning and supervised fine-tuning. We further review and contextualize agentic reasoning frameworks in real-world applications and benchmarks spanning science, robotics, healthcare, autonomous research, and math, illustrating how different reasoning mechanisms are instantiated and evaluated across domains. This survey synthesizes agentic reasoning methods into a unified roadmap that bridges thoughts and actions, offering actionable guidance for agentic systems across environmental dynamics, optimization settings, and agent interaction settings. Finally, we outline open challenges and future directions, situating how agentic reasoning has developed while identifying what remains ahead: personalization, long-horizon interaction, world modeling, scalable multi-agent training, and governance frameworks for real-world deployment.

<a id="p032"></a>
## P032 · Autoregressive, Yet Revisable: In Decoding Revision for Secure Code Generation

- **作者**：Chengran Yang; Zichao Wei; Heminghao Deng; Jinfeng Jiang; Zhensu Sun; Ting Zhang; Tianyi Wu; Ming Wen; David Lo
- **时间**：本地版本：2026-05-06（arXiv:2602.01187v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint；稿面2026-05-07；arXiv:2602.01187v2时间2026-05-06
- **论文链接**：[arXiv本地版本 2602.01187v2](https://arxiv.org/abs/2602.01187v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全
- **PDF版本**：21页；SHA-256：`c9b7c702d280df7d23ac4f1133a46a1725bb3ccf82b0b77b70db469d9b05c775`

### 中文摘要

让自回归模型在生成过程中输出编辑指令，从而及时修改已经构造的代码。

### 核心贡献

Stream of Revision 以虚拟光标、编辑 token 和确定性渲染器把生成流转换为可修订程序。

### 实现边界

token 流仍单调自回归，改变的是渲染后的代码；主要在 C/C++ 安全对齐和 CSE2 检测器上评价。

### Method／方法

从真实 CVE 修复对构造训练数据，学习编辑动作及普通代码；用安全检查通过率、HumanEval 功能测试和 AST 解析率分别验证。

### Results／主要结果

相较多种修复/对齐基线改善 CSE2 安全通过率；叠加 ProSec 后文中报告 C +1.16、C++ +4.15 个百分点。

### Shortcomings／局限与可能不足

【解读】静态检查通过不等于无漏洞；需修改训练与渲染执行协议，仍可能生成语法/语义错误，跨语言效果有条件。

### 证据定位

§3；§4–6、表2；§7.3、表5；§9。

### Abstract

Large Language Model (LLM) based code generation is predominantly formulated as a strictly monotonic process, appending tokens linearly to an immutable prefix. This formulation contrasts to the cognitive process of programming, which is inherently interleaved with forward generation and on-the-fly revision. While prior works attempt to introduce revision via post-hoc agents or external static tools, they either suffer from high latency or fail to leverage the model’s intrinsic semantic reasoning. In this paper, we propose Stream of Revision, a paradigm shift that elevates code generation from a monotonic stream to a dynamic, self-correcting trajectory by leveraging model’s intrinsic capabilities. We introduce specific action tokens that enable the model to seamlessly backtrack and edit its own history within a single forward pass. By internalizing the revision loop, our framework Stream of Revision allows the model to activate its latent capabilities just-intime without external dependencies. Empirical results on secure code generation show that Stream of Revision significantly reduces vulnerabilities with minimal inference overhead.

<a id="p033"></a>
## P033 · Gen-Searcher: Reinforcing Agentic Search for Image Generation

- **作者**：Kaituo Feng; Manyuan Zhang; Shawn Chen; Yunlong Lin; Kaixuan Fan; Yilei Jiang; Hongyu Li; Dian Zheng; Chenyang Wang; Xiangyu Yue（首页为 Shawn Chen，PDF 元数据为 Shuang Chen）
- **时间**：本地版本：2026-05-02（arXiv:2603.28767v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2603.28767v2，2026-05-02（本地技术报告）
- **论文链接**：[arXiv本地版本 2603.28767v2](https://arxiv.org/abs/2603.28767v2)
- **项目／代码／数据**：[项目/演示页面](https://gen-searcher.vercel.app/)

- **主题**：创作与规则补全
- **PDF版本**：20页；SHA-256：`26f20d758c0536cd6839012347e0f7bccc94a0add0d978870236cd6d5ad3343a`

### 中文摘要

为知识密集的图像生成训练多步搜索智能体，先找文字知识与参考图，再调用生成器。

### 核心贡献

Gen-Searcher-SFT-10k/RL-6k 数据、KnowGen 基准和结合文字/图像反馈的 RL。

### 实现边界

搜索代理增强已有图像生成器；输出仍受搜索质量、网页时效和生成器能力限制。

### Method／方法

Qwen3-VL-8B 先 SFT 再 agentic RL；工具执行搜索/浏览，双奖励评价知识正确性与生成图的实际符合度。

### Results／主要结果

KnowGen、WISE 上相对所列生成器和代理基线获得提升，并展示跨生成器迁移；训练设置还需图像生成和网页摘要辅助模型，不能把代理 8B 视为全部计算规模。

### Shortcomings／局限与可能不足

【解读】外部来源可能错误，评价器及合成训练图可能带偏；多跳搜索和图像 rollout 的计算/服务成本高。

### 证据定位

§3 数据与训练；§4.1–4.4、表1–3；§5。

### Abstract

Recent image generation models have shown strong capabilities in generating high-fidelity and photorealistic images. However, they are fundamentally constrained by frozen internal knowledge, thus often failing on real-world scenarios that are knowledge-intensive or require up-to-date information. In this paper, we present Gen-Searcher, as the first attempt to train a search-augmented image generation agent, which performs multi-hop reasoning and search to collect the textual knowledge and reference images needed for grounded generation. To achieve this, we construct a tailored data pipeline and curate two high-quality datasets, Gen-Searcher-SFT-10k and Gen-Searcher-RL-6k, containing diverse search-intensive prompts and corresponding ground-truth synthesis images. We further introduce KnowGen, a comprehensive benchmark that explicitly requires search-grounded external knowledge for image generation and evaluates models from multiple dimensions. Based on these resources, we train Gen-Searcher with SFT followed by agentic reinforcement learning with dual reward feedback, which combines text-based and image-based rewards to provide more stable and informative learning signals for GRPO training. Experiments show that Gen-Searcher brings substantial gains, improving Qwen-Image by around 16 points on KnowGen and 15 points on WISE. We hope this work can serve as an open foundation for search agents in image generation, and we fully open-source our data, models, and code.

<a id="p034"></a>
## P034 · Lost in Transmission: When and Why LLMs Fail to Reason Globally

- **作者**：Tobias Schnabel; Kiran Tomlinson; Adith Swaminathan; Jennifer Neville
- **时间**：本地版本：2026-01-30（arXiv:2505.08140v5）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：NeurIPS 2025（PDF首页会议页脚）；本地arXiv:2505.08140v5更新2026-01-30
- **论文链接**：[arXiv本地版本 2505.08140v5](https://arxiv.org/abs/2505.08140v5)
- **项目／代码／数据**：[代码：microsoft/bapo](https://github.com/microsoft/bapo)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：39页；SHA-256：`9967dd46b0d1933065336b5d9d1ae994f04713da134b0099999ee7978a12e2d9`

### 中文摘要

用注意力通信带宽受限模型解释 LLM 在跨输入全局推理上的失败。

### 核心贡献

提出 Bounded Attention Prefix Oracle（BAPO），证明可达性等问题的带宽下界，并分析 CoT 如何缓解限制。

### 实现边界

理论结论对所定义 BAPO 模型成立；经验结果支持带宽假说，未证明真实 Transformer 只有同样的严格上限。

### Method／方法

用 prefix/attention oracle 抽象信息流，区分 BAPO-easy/hard；在受控和现实任务上比较模型与 CoT 条件。

### Results／主要结果

GPT-4o、Claude、Gemini 对 easy 任务较强、对小规模 hard 任务也会失败；适当分解的 CoT 在理论模型中可把 hard 计算转化为逐步 easy 计算。

### Shortcomings／局限与可能不足

【作者】真实有效带宽成因尚不清楚，部分下界较松；【解读】存在可用分解不保证模型会自动找到并可靠执行它。

### 证据定位

§2–3；§4；§6–7。

### Abstract

Despite their many successes, transformer-based large language models (LLMs) continue to struggle with tasks that require complex reasoning over large parts of their input. We argue that these failures arise due to capacity limits on the accurate flow of information within LLMs. To formalize this issue, we introduce the bounded attention prefix oracle (BAPO) model, a new computational framework that models bandwidth constraints on attention heads, the mechanism for internal communication in LLMs. We show that several important reasoning problems like graph reachability require high communication bandwidth for BAPOs to solve; we call these problems BAPO-hard. Our experiments corroborate our theoretical predictions: GPT-4o, Claude, and Gemini succeed on BAPO-easy tasks and fail even on relatively small BAPO-hard tasks. BAPOs also reveal another benefit of chain of thought (CoT): we prove that breaking down a task using CoT can turn any BAPO-hard problem into a BAPO-easy one. Our results offer principled explanations for key LLM failures and suggest directions for architectures and inference methods that mitigate bandwidth limits.

<a id="p035"></a>
## P035 · Mind-Brush: Integrating Agentic Cognitive Search and Reasoning into Image Generation

- **作者**：Jun He; Junyan Ye; Zilong Huang; Dongzhi Jiang; Chenjue Zhang; Leqi Zhu; Renrui Zhang; Xiang Zhang; Weijia Li
- **时间**：本地版本：2026-02-02（arXiv:2602.01756v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint；稿面2026-02-03；arXiv:2602.01756v1时间2026-02-02
- **论文链接**：[arXiv本地版本 2602.01756v1](https://arxiv.org/abs/2602.01756v1)
- **项目／代码／数据**：[代码：PicoTrex/Mind-Brush](https://github.com/PicoTrex/Mind-Brush)；[数据/模型：datasets/PicoTrex/Mind-Brush](https://huggingface.co/datasets/PicoTrex/Mind-Brush)

- **主题**：创作与规则补全
- **PDF版本**：36页；SHA-256：`7b438d417f55156c2f8657fb74afedd81786a23c05c2bdb5b5a99b9385794488`

### 中文摘要

以意图分析、主动搜索和显式推理补全图像生成所需的知识与隐含约束。

### 核心贡献

训练无需新增的 Mind-Brush 编排框架，以及含 500 个动态知识/推理样本的 Mind-Bench。

### 实现边界

调用既有搜索、推理与生成模型；输出符合事实的程度受检索资料和生成器制约。

### Method／方法

检测认知缺口，搜索多模态证据、补充约束后生成；用 checklist-based strict accuracy（全部清单项通过）和 WISE/RISEBench 评价。

### Results／主要结果

完整框架在 Mind-Bench 的消融中比仅 reasoning agent 高 0.17、比仅 search agent 高 0.06 的准确率；另在 WISE/RISE 上取得所报改进。

### Shortcomings／局限与可能不足

【解读】多模型调用成本高，清单覆盖和 MLLM 评价器可能漏检；“无需训练”只针对框架新增训练。

### 证据定位

§3；§4；§5.3–5.4；§6。

### Abstract

While text-to-image generation has achieved unprecedented fidelity, the vast majority of existing models function fundamentally as static text-topixel decoders. Consequently, they often fail to grasp implicit user intentions. Although emerging unified understanding-generation models have improved intent comprehension, they still struggle to accomplish tasks involving complex knowledge reasoning within a single model. Moreover, constrained by static internal priors, these models remain unable to adapt to the evolving dynamics of the real world. To bridge these gaps, we introduce Mind-Brush, a unified agentic framework that transforms generation into a dynamic, knowledgedriven workflow. Simulating a human-like ’thinkresearch-create’ paradigm, Mind-Brush actively retrieves multimodal evidence to ground out-ofdistribution concepts and employs reasoning tools to resolve implicit visual constraints. To rigorously evaluate these capabilities, we propose Mind-Bench, a comprehensive benchmark comprising 500 distinct samples spanning real-time news, emerging concepts, and domains such as mathematical and Geo-Reasoning. Extensive experiments demonstrate that Mind-Brush significantly enhances the capabilities of unified models, realizing a zero-to-one capability leap for the Qwen-Image baseline on Mind-Bench, while achieving superior results on established benchmarks like WISE and RISE.

<a id="p036"></a>
## P036 · SimStep: Human-in-the-Loop Authoring of Interactive Educational Simulations Through Task-Level Abstractions

- **作者**：Zoe Kaputa; Anika Rajaram; Vryan Feliciano; Zhuoyue Lyu; Maneesh Agrawala; Hariharan Subramonyam
- **时间**：2026年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CHI 2026，2026-04-13 至 04-17；DOI 10.1145/3772318.3791514
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3772318.3791514)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：34页；SHA-256：`3eca89598fa6497b0ecd0c6fd84398cfbacc158792df23ae34e5e85bdc3ed648`

### 中文摘要

通过可检查、可修改的任务级图表示，让教师逐步创作并调试互动教学模拟。

### 核心贡献

Chain-of-Abstractions 及 inverse correction，将概念、场景、学习目标、UI 与代码衔接。

### 实现边界

实现的是模拟创作与纠错工具；没有证明学生学习成绩改善或仿真物理绝对正确。

### Method／方法

教师在抽象图上验证和编辑，Claude 生成/修改代码；自动测试和图形回溯定位隐含假设；进行教师使用与抽象保真度研究。

### Results／主要结果

11 名教师体验研究的 1–6 分可用性均值 4.66（SD 0.36）；66 个模拟由 162 名 Prolific 参与者评价抽象保真度，概念图完整/连贯性 2.61/3。

### Shortcomings／局限与可能不足

【作者】Prolific 评价者学科/教龄等信息未收集；【解读】短期创作体验不等于课堂效果，自动修复仍需人工核查。

### 证据定位

§3–5；§6.2；§7/表5；§8.3。

### Abstract

Generative AI enables educators to create interactive learning content by describing goals in natural language. However, without programming affordances such as traceability, refinement, and debugging, teachers struggle to align simulations with learners’ needs, refine them step by step, or verify that they reflect intended learning concepts. We propose a task-level abstraction approach that structures authoring as a sequence of representations, mirroring how teachers plan lessons and providing checkpoints for specification, inspection, and refinement. We instantiate this approach in SimStep, an authoring environment that scaffolds simulation design with four abstractions, including Concept Graph, Scenario Graph, Learning Goal Graph, and UI Graph, and introduces an inverse correction process to revise hidden model assumptions without requiring code manipulation. A technical evaluation shows that these abstractions preserve fidelity across transformations, while a user study with educators demonstrates their effectiveness in authoring simulations. Our work reframes AI-assisted programming as human–AI co-authoring through structured, domain-aligned abstractions.

<a id="p037"></a>
## P037 · SLM-MUX: Orchestrating Small Language Models for Reasoning

- **作者**：Chenyu Wang; Zishen Wan; Hao Kang; Emma Chen; Zhiqiang Xie; Tushar Krishna; Vijay Janapa Reddi; Yilun Du
- **时间**：2026年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICLR 2026（PDF 明示 Published as a conference paper）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：27页；SHA-256：`a554693e80b40655b26e8479b00deb394efbb520aa37baba4cb6fac58fd96ad1`

### 中文摘要

让多个小模型独立作答，用一致性选择结果，并搜索互补模型组合。

### 核心贡献

SLM-MUX、模型子集搜索与配套测试时计算分配方案。

### 实现边界

使用固定模型组合及验证集；非模型间讨论，置信度主要以重复答案频次近似。

### Method／方法

每个模型多次采样，取自身众数并比较一致性；按 union accuracy 与冲突惩罚搜索组合，平局用验证准确率处理。

### Results／主要结果

论文报告相对既有编排方法最高提升 MATH 13.4、GPQA 8.8、GSM8K 7.0 个百分点；选定两个小模型的组合可在部分任务超过 Qwen2.5-72B。

### Shortcomings／局限与可能不足

【作者】穷举组合开销高且静态，一致性高也可能一致地错；【解读】需将多模型多次采样成本纳入比较。

### 证据定位

§3；§4；§5 Limitation and Future Work。

### Abstract

With the rapid development of language models, the number of small language models (SLMs) has grown significantly. Although they do not achieve state-of-theart accuracy, they are more efficient and often excel at specific tasks. This raises a natural question: can multiple SLMs be orchestrated into a system where each contributes effectively, achieving higher accuracy than any individual model? Existing orchestration methods have primarily targeted frontier models (e.g., GPT-4) and perform suboptimally when applied to SLMs. To address this gap, we propose a three-stage approach for orchestrating SLMs. First, we introduce SLM-MUX, a multi-model architecture that effectively coordinates multiple SLMs. Building on this, we develop two optimization strategies: (i) a model selection search that identifies the most complementary SLMs from a given pool, and (ii) test-time scaling tailored to SLM-MUX. Our approach delivers strong results: Compared to existing orchestration methods, our approach achieves up to 13.4% improvement on MATH, 8.8% on GPQA, and 7.0% on GSM8K. With just two SLMs, SLM-MUX outperforms Qwen 2.5 72B on GPQA and GSM8K, and matches its performance on MATH. We further provide theoretical analyses to substantiate the advantages of our method. Additional experiments show that the core principle of SLM-MUX extends to open-ended generation tasks (e.g., HumanEval) and benefits other model classes, including frontier LLMs and domain-specific fine-tuned SLMs. In summary, we demonstrate that SLMs can be effectively orchestrated into more accurate and efficient systems through the proposed approach.

<a id="p038"></a>
## P038 · “I’m Not Sure, But...”: Examining the Impact of Large Language Models’ Uncertainty Expression on User Reliance and Trust

- **作者**：Sunnie S. Y. Kim; Q. Vera Liao; Mihaela Vorvoreanu; Stephanie Ballard; Jennifer Wortman Vaughan
- **时间**：2024年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：FAccT 2024，2024-06-03 至 06-06；DOI 10.1145/3630106.3658941
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3630106.3658941)
- **项目／代码／数据**：[OSF研究材料](https://osf.io/mnrp9)

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：14页；SHA-256：`2fe292249e998fb7c0158f8f63a30b65b9d4f560407b0625bf728ff2f7dc5f30`

### 中文摘要

研究 LLM 用不同自然语言方式表达不确定性时，用户依赖、信任和任务表现如何变化。

### 核心贡献

预注册、N=404 的受控人类实验，区分第一人称、一般视角及无不确定性表达。

### 实现边界

虚构 AI 搜索系统中的医学事实是非题；操控表达，不训练或校准模型的真实不确定性。

### Method／方法

随机分组，对照有/无 AI 与不同措辞；用行为、答案正确性、信心和自报信任评价，并区分确认性/探索性分析。

### Results／主要结果

第一人称表达降低对系统信心与跟随率、提高用户准确率；一般视角效应较弱且未达显著。过度依赖仍存在，无 AI 组总体任务表现最好。

### Shortcomings／局限与可能不足

【解读】单一任务和短期实验限制外推；谨慎措辞不是校准概率，也可能降低对正确答案的依赖。

### 证据定位

§3 预注册设计；§4；§5.1；§6。

### Abstract

Widely deployed large language models (LLMs) can produce convincing yet incorrect outputs, potentially misleading users who may rely on them as if they were correct. To reduce such overreliance, there have been calls for LLMs to communicate their uncertainty to end users. However, there has been little empirical work examining how users perceive and act upon LLMs’ expressions of uncertainty. We explore this question through a large-scale, pre-registered, human-subject experiment (N=404) in which participants answer medical questions with or without access to responses from a fictional LLM-infused search engine. Using both behavioral and self-reported measures, we examine how different natural language expressions of uncertainty impact participants’ reliance, trust, and overall task performance. We find that firstperson expressions (e.g., “I’m not sure, but...”) decrease participants’ confidence in the system and tendency to agree with the system’s answers, while increasing participants’ accuracy. An exploratory analysis suggests that this increase can be attributed to reduced (but not fully eliminated) overreliance on incorrect answers. While we observe similar effects for uncertainty expressed from a general perspective (e.g., “It’s not clear, but...”), these effects are weaker and not statistically significant. Our findings suggest that using natural language expressions of uncertainty may be an effective approach for reducing overreliance on LLMs, but that the precise language used matters. This highlights the importance of user testing before deploying LLMs at scale.

<a id="p039"></a>
## P039 · Make-a-Story: Visual Memory Conditioned Consistent Story Generation

- **作者**：Tanzila Rahman; Hsin-Ying Lee; Jian Ren; Sergey Tulyakov; Shweta Mahajan; Leonid Sigal
- **时间**：2023年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CVPR 2023（正式会议 PDF）
- **项目／代码／数据**：[代码：ubc-vision/Make-A-Story](https://github.com/ubc-vision/Make-A-Story)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：10页；SHA-256：`f15cd145c1869ec4b7661371bea534f5649cc8fa07eb39f3613b91c555c971da`

### 中文摘要

以视觉记忆支持带指代的故事可视化，保持角色与背景跨图一致。

### 核心贡献

自回归 Story-LDM 及句子条件记忆注意力，并扩展 MUGEN/Flintstones 的指代设置。

### 实现边界

根据句子序列生成故事帧，主要是动画/游戏域；不是连续动作的长视频生成。

### Method／方法

潜在扩散逐帧生成，当前句子对过去图像和文本记忆做软注意力，以解析 he/she/they 等角色或背景指代。

### Results／主要结果

MUGEN、PororoSV、FlintstonesSV 上的图像质量、故事一致性和人评优于所列前作；同时演示保持一致与按情节改变背景。

### Shortcomings／局限与可能不足

【解读】角色集合和视觉域较有限，自回归错误可能累积；一致性指标不能完整衡量故事叙事质量。

### 证据定位

§3；§4–5；§6。

### Abstract

There has been a recent explosion of impressive generative models that can produce high quality images (or videos) conditioned on text descriptions. However, all such approaches rely on conditional sentences that contain unambiguous descriptions of scenes and main actors in them. Therefore employing such models for more complex task of story visualization, where naturally references and coreferences exist, and one requires to reason about when to maintain consistency of actors and backgrounds across frames/scenes, and when not to, based on story progression, remains a challenge. In this work, we address the aforementioned challenges and propose a novel autoregressive diffusion-based framework with a visual memory module that implicitly captures the actor and background context across the generated frames. Sentence-conditioned soft attention over the memories enables effective reference resolution and learns to maintain scene and actor consistency when needed. To validate the effectiveness of our approach, we extend the MUGEN dataset [19] and introduce additional characters, backgrounds and referencing in multisentence storylines. Our experiments for story generation on the MUGEN, the PororoSV [30] and the FlintstonesSV [16] dataset show that our method not only outperforms prior state-of-the-art in generating frames with high visual quality, which are consistent with the story, but also models appropriate correspondences between the characters and the background.

<a id="p040"></a>
## P040 · Collaposer: Transforming Photo Collections into Visual Assets for Storytelling with Collages

- **作者**：Jiayi Zhou; Liwenhan Xie; Jiaju Ma; Zheng Wei; Huamin Qu; Anyi Rao
- **时间**：本地版本：2026-01-26（arXiv:2601.18428v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：CHI 2026，2026-04-13 至 04-17（作者版明示正式记录）；DOI 10.1145/3772318.3791160
- **论文链接**：[arXiv本地版本 2601.18428v1](https://arxiv.org/abs/2601.18428v1)；[DOI正式记录](https://doi.org/10.1145/3772318.3791160)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全
- **PDF版本**：19页；SHA-256：`e579dd9e6132c26dbbbce515aba82204f8f109cd0a5f5c543472a6e717ae5c82`

### 中文摘要

Collaposer 根据故事描述从照片集合中提取和组织可用于拼贴的视觉素材。

### 核心贡献

把自动标注/检测/分割与故事驱动的语义选择、分层聚类展示结合。

### 实现边界

从输入照片提取切图并由用户构图；动画属于演示延伸，不是自主生成完整视频故事。

### Method／方法

6 名专家形成性访谈；流水线预处理照片，LLM 选择中心及相关标签，再按语义层次布局；12 人与两种消融基线被试内比较。

### Results／主要结果

12 人共创作 36 个静态拼贴故事、尝试 45 个提示；使用完整系统均一次获得可用素材集，故事匹配、多样性和可用性评价优于消融。

### Shortcomings／局限与可能不足

【作者】文字意图可能错配，选择依据透明性不足；【解读】小样本且基线为消融，不能推断相对全部专业工具的效率优势。

### 证据定位

§3；§4；§6–7；§9。

### Abstract

Digital collage is an artistic practice that combines image cutouts to tell stories. However, preparing cutouts from a set of photos remains a tedious and time-consuming task. A formative study identified three main challenges: 1) inefficient search for relevant photos, 2) manual image cutout, and 3) difficulty in organizing large sets of cutouts. To meet these challenges and facilitate asset preparation for collage, we propose Collaposer, a tool that transforms a collection of photos into organized, ready-to-use visual cutouts based on user-provided story descriptions. Collaposer tags, detects, and segments photos, and then uses an LLM to select central and related labels based on the user-provided story description. Collaposer presents the resulting visuals in varying sizes, clustered according to semantic hierarchy. Our evaluation shows that Collaposer effectively automates the preparation process to produce diverse sets of visual cutouts adhering to the storyline, allowing users to focus on collaging these assets for storytelling.

<a id="p041"></a>
## P041 · Learning to Complement Humans

- **作者**：Bryan Wilder; Eric Horvitz; Ece Kamar
- **时间**：本地版本：2020-05-01（arXiv:2005.00582v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：IJCAI 2020，pp.1526–1533（官方论文集核验）。 [IJCAI官方论文页](https://www.ijcai.org/proceedings/2020/212)
- **论文链接**：[arXiv本地版本 2005.00582v1](https://arxiv.org/abs/2005.00582v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作
- **PDF版本**：8页；SHA-256：`f2db8ece3b71eb3c52f40b5398ed32992f5d032a2a1a5bcf4ab054ff4cf68f9d`

### 中文摘要

联合训练预测模型和求助策略，以人机团队的整体效用而非机器独立准确率为目标。

### 核心贡献

提出判别式及决策论式的联合优化，显式利用人类与机器错误模式的互补。

### 实现边界

Galaxy Zoo 和 CAMELYON 的离线人类标注数据；交互主要为是否查询一个人类答案。

### Method／方法

建模标签、人类响应及条件预测；同时优化分类和查询决策，将求助成本/非对称错误代价纳入期望损失。

### Results／主要结果

表1中 Galaxy Zoo 一层 VOI 的平均损失改善 38.9%（跨查询成本），不同容量/任务收益差异很大，部分设置存在负改善。

### Shortcomings／局限与可能不足

【解读】需可靠的人类响应模型和代表性数据；未覆盖人类因 AI 建议而改变行为的长期双向协作。

### 证据定位

§2–3；§4/表1；§5。

### Abstract

A rising vision for AI in the open world centers on the development of systems that can complement humans for perceptual, diagnostic, and reasoning tasks. To date, systems aimed at complementing the skills of people have employed models trained to be as accurate as possible in isolation. We demonstrate how an end-to-end learning strategy can be harnessed to optimize the combined performance of human-machine teams by considering the distinct abilities of people and machines. The goal is to focus machine learning on problem instances that are difficult for humans, while recognizing instances that are difficult for the machine and seeking human input on them. We demonstrate in two real-world domains (scientific discovery and medical diagnosis) that human-machine teams built via these methods outperform the individual performance of machines and people. We then analyze conditions under which this complementarity is strongest, and which training methods amplify it. Taken together, our work provides the first systematic investigation of how machine learning systems can be trained to complement human reasoning.

<a id="p042"></a>
## P042 · LLMs Struggle to Balance Reasoning and World Knowledge in Causal Narrative Understanding

- **作者**：Khurram Yamin; Shantanu Gupta; Gaurav Ghosal; Zachary Lipton; Bryan Wilder
- **时间**：2026年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICLR 2026（PDF 明示）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P045](#p045)为同一工作不同题名/版本；本地[P042](#p042)明示ICLR 2026，[P045](#p045)为2025-06的较早预印稿。

- **主题**：世界机制与演化
- **PDF版本**：28页；SHA-256：`0264b3dec2f81a06f3272ce9328b2324bea065f9d9a77f4733091cb48ca9595d`

### 中文摘要

分析 LLM 在叙事因果理解中如何受事件顺序、已有知识和图结构复杂度影响。

### 核心贡献

受控的合成、半合成和真实叙事评测，定位常识捷径与顺序偏差。

### 实现边界

主要判断事件间因果关系和抽取图；未涵盖完整反事实或干预推理。

### Method／方法

从链、fork、collider 和 CauseNet 构造叙事，操控叙述顺序/知识一致性/长度；比较直接回答与先抽因果图。

### Results／主要结果

模型倾向按叙事顺序推断因果、以参数知识覆盖上下文；图更长/复杂时下降。先显式识别因果图可改善稳定性。

### Shortcomings／局限与可能不足

【作者】未覆盖其他因果任务；【解读】CauseNet 是文本声称的因果关系，受控叙事不等于真实科学因果发现。

### 证据定位

§3–4；§5；与 P045 封面、摘要比对。

### Abstract

The ability to robustly identify causal relationships is essential for autonomous decision-making and adaptation to novel scenarios. However, accurately inferring causal structure requires integrating both world knowledge and abstract logical reasoning. In this work, we investigate the interaction between these two capabilities through the representative task of causal reasoning over narratives. Through controlled synthetic, semi-synthetic and real-world experiments, we find that stateof-the-art large language models (LLMs) often rely on superficial heuristics—for example, inferring causality from event order or recalling memorized world knowledge without attending to context. Furthermore, we show that simple reformulations of the task can elicit more robust reasoning behavior. Our evaluation spans a range of causal structures, from linear chains to complex graphs involving colliders and forks. These findings uncover systematic patterns in how LLMs perform causal reasoning and lay the groundwork for developing methods that better align LLM behavior with principled causal inference.

<a id="p043"></a>
## P043 · LLMs Struggle to Perform Counterfactual Reasoning with Parametric Knowledge

- **作者**：Khurram Yamin, Gaurav Ghosal, Bryan Wilder
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：2025 年研究稿；ICML 2025 模板元数据；arXiv:2506.15732，主会/Workshop 身份不能只由模板判断。 [arXiv记录](https://arxiv.org/abs/2506.15732)
- **论文链接**：[arXiv论文记录](https://arxiv.org/abs/2506.15732)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：10页；SHA-256：`ba93aa93e6f55f736903bae8c7fb437ddf9783864e2d8fa6c9ecf4aa06c7d579`

### 中文摘要

测试模型能否将新反事实前提与已存知识结合，而不是继续沿用默认知识。

### 核心贡献

区分强化、添加、冲突与无关上下文的知识整合任务，并研究微调的副作用。

### 实现边界

受控知识图和短链因果查询；不是现实因果效应估计。

### Method／方法

在 GPT-4o/Llama3.1 与玩具模型上比较直接提示、CoT、160 条反事实示例微调及预训练干预。

### Results／主要结果

强化既有知识时 GPT-4o 直接提示约 85%、CoT 超过 95%；添加/冲突条件困难，简单微调可能仍依赖捷径或损害原有知识。

### Shortcomings／局限与可能不足

【作者】玩具前提多为单边编辑、两跳查询；【解读】少量训练与模型范围限制结论，不可说微调普遍无效。

### 证据定位

§3；§4；§5–6；附录训练细节。

### Abstract

Large Language Models have been shown to contain extensive world knowledge in their parameters, enabling impressive performance on many knowledge intensive tasks. However, when deployed in novel settings, LLMs often encounter situations where they must integrate parametric knowledge with new or unfamiliar information. In this work, we explore whether LLMs can combine knowledge in-context with their parametric knowledge through the lens of counterfactual reasoning. Through synthetic and real experiments in multi-hop reasoning problems, we show that LLMs generally struggle with counterfactual reasoning, often resorting to exclusively using their parametric knowledge. Moreover, we show that simple post-hoc finetuning can struggle to instill counterfactual reasoning ability – often leading to degradation in stored parametric knowledge. Ultimately, our work reveals important limitations of current LLM’s abilities to re-purpose parametric knowledge in novel settings.

<a id="p044"></a>
## P044 · Orthogonal Causal Calibration

- **作者**：Justin Whitehouse; Christopher Jung; Vasilis Syrgkanis; Bryan Wilder; Zhiwei Steven Wu
- **时间**：本地版本：2025-04-30（arXiv:2406.01933v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：COLT 2025 Extended Abstract，PMLR291:5712–5713（官方记录核验）；本地为完整研究稿，首页2025-05-02、arXiv v2为2025-04-30，两者篇幅不可混淆。 [PMLR官方记录](https://proceedings.mlr.press/v291/whitehouse25a.html)
- **论文链接**：[arXiv本地版本 2406.01933v2](https://arxiv.org/abs/2406.01933v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：49页；SHA-256：`b80516dff71d6e559774e8c2192764cc4d0f0108448bff43f2114cbf85526080`

### 中文摘要

用正交损失把异质性因果效应估计的校准转化为较标准的预测校准。

### 核心贡献

对 universal/conditional orthogonality 给出误差分解、样本切分和交叉校准算法及收敛保证。

### 实现边界

结论依赖识别条件、正交性、损失正则性和 nuisance 估计；重点是 L2 校准，不保证个体反事实准确或决策最优。

### Method／方法

构造广义伪结果或条件损失，在独立样本上校准；把误差分为 nuisance 估计误差与假想已知 nuisance 下的校准误差。

### Results／主要结果

401(k) 观察数据和合成条件分位数实验中降低校准误差，部分同时降低平均损失；理论提供高概率收敛及条件性的 do-no-harm 结果。

### Shortcomings／局限与可能不足

【作者】其他 Lp 校准及最终决策效用仍待研究；【解读】真实观察数据无法直接观测全部个体处理效应。

### 证据定位

摘要；§3–4；§5 图1–2；§6。

### Abstract

Estimates of heterogeneous treatment effects such as conditional average treatment effects (CATEs) and conditional quantile treatment effects (CQTEs) play an important role in real-world decision making. Given this importance, one should ensure these estimates are calibrated. While there is a rich literature on calibrating estimators of non-causal parameters, very few methods have been derived for calibrating estimators of causal parameters, or more generally estimators of quantities involving nuisance parameters. In this work, we develop general algorithms for reducing the task of causal calibration to that of calibrating a standard (non-causal) predictive model. Throughout, we study a notion of calibration defined with respect to an arbitrary, nuisance-dependent loss l, under which we say an estimator θ is calibrated if its predictions cannot be changed on any level set to decrease loss. For losses l satisfying a condition called universal orthogonality, we present a simple algorithm that transforms partially-observed data into generalized pseudo-outcomes and applies any off-the-shelf calibration procedure. For losses l satisfying a weaker assumption called conditional orthogonality, we provide a similar sample splitting algorithm the performs empirical risk minimization over an appropriately defined class of functions. Convergence of both algorithms follows from a generic, two term upper bound of the calibration error of any model: one term that measures the error in estimating unknown nuisance parameters and another that measures calibration error in a hypothetical world where the learned nuisances are true. We demonstrate the practical applicability of our results in experiments on both observational and synthetic data. Our results are exceedingly general, showing that essentially any existing calibration algorithm can be used in causal settings, with additional loss only arising from errors in nuisance estimation.

<a id="p045"></a>
## P045 · Failure Modes of LLMs for Causal Reasoning on Narratives

- **作者**：Khurram Yamin; Shantanu Gupta; Gaurav Ghosal; Zachary Lipton; Bryan Wilder
- **时间**：本地版本：2025-06-15（arXiv:2410.23884v5）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2410.23884v5，2025-06-15；后续改题的ICLR 2026版本见P042
- **论文链接**：[arXiv本地版本 2410.23884v5](https://arxiv.org/abs/2410.23884v5)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P042](#p042)为同一工作不同题名/版本；本条按较早的本地稿总结。

- **主题**：世界机制与演化
- **PDF版本**：23页；SHA-256：`49a0e206675337354ceff5c93faef9493f58048c70a0088fde01fd9b9c3647b0`

### 中文摘要

研究语言模型在叙事因果理解中的失效模式，是 P042 的早期版本。

### 核心贡献

明确事件顺序、参数知识一致性和叙事结构复杂度三类影响。

### 实现边界

因果关系识别/图抽取；本文明确把反事实案例留作未来工作。

### Method／方法

构造可控合成叙事并使用 CauseNet 的半合成/真实语句，比较多种模型和先抽图提示。

### Results／主要结果

事件拓扑顺序一致时较好，知识冲突及长链时较差；显式抽取因果图改善推理。本条按 v5 总结，不把后续 ICLR 附录结果回填为早期结果。

### Shortcomings／局限与可能不足

【作者】其他类型因果推理未测；【解读】叙事中识别给定因果并不等同从混杂观测中识别因果。

### 证据定位

§3–4；§5.1；与 P042 对照。

### Abstract

The ability to robustly identify causal relationships is essential for autonomous decision-making and adaptation to novel scenarios. However, accurately inferring causal structure requires integrating both world knowledge and abstract logical reasoning. In this work, we investigate the interaction between these two capabilities through the representative task of causal reasoning over narratives. Through controlled synthetic, semi-synthetic and real-world experiments, we find that stateof-the-art large language models (LLMs) often rely on superficial heuristics—for example, inferring causality from event order or recalling memorized world knowledge without attending to context. Furthermore, we show that simple reformulations of the task can elicit more robust reasoning behavior. Our evaluation spans a range of causal structures, from linear chains to complex graphs involving colliders and forks. These findings uncover systematic patterns in how LLMs perform causal reasoning and lay the groundwork for developing methods that better align LLM behavior with principled causal inference.

<a id="p046"></a>
## P046 · Explaining Concept Shift with Interpretable Feature Attribution

- **作者**：Ruiqi Lyu; Alistair Turcan; Bryan Wilder
- **时间**：本地版本：2025-05-27（arXiv:2505.20634v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint, Under review；arXiv:2505.20634v1，2025-05-27（本地版本）
- **论文链接**：[arXiv本地版本 2505.20634v1](https://arxiv.org/abs/2505.20634v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：25页；SHA-256：`b06c08edda94ada5d2c1566b92694110d440fab9c921c2fad4806ad9c010bcbc`

### 中文摘要

SGShift 将预测失效归因到条件标签分布发生变化的少数特征。

### 核心贡献

稀疏 GAM 归因、吸收模型误设项和 knockoff 错误发现控制扩展。

### 实现边界

表格数据的概念漂移，需源/目标域信息和标注；被选特征不是必然的干预因果变量。

### Method／方法

在原模型输出上拟合带 L1 惩罚的加性修正，结合两域共享误设项；用 knockoffs 筛选发生变化的特征。

### Results／主要结果

在糖尿病再入院、COVID 和 SUPPORT2 的半合成实验中，knockoff 变体多次获得 AUC&gt;0.9；召回率按 FPR=10% 评价，不能与任意阈值召回混用。

### Shortcomings／局限与可能不足

【作者】假设变化稀疏，密集变化难解释；【解读】GAM 加性结构和有限目标域标签限制复杂交互漂移识别。

### 证据定位

§4；§5–6/表2；§7。

### Abstract

Regardless the amount of data a machine learning (ML) model is trained on, there will inevitably be data that differs from their training set, lowering model performance. Concept shift occurs when the distribution of labels conditioned on the features changes, making even a well-tuned ML model to have learned a fundamentally incorrect representation. Identifying these shifted features provides unique insight into how one dataset differs from another, considering the difference may be across a scientifically relevant dimension, such as time, disease status, population, etc. In this paper, we propose SGShift, a model for detecting concept shift in tabular data and attributing reduced model performance to a sparse set of shifted features. SGShift models concept shift with a Generalized Additive Model (GAM) and performs subsequent feature selection to identify shifted features. We propose further extensions of SGShift by incorporating knockoffs to control false discoveries and an absorption term to account for models with poor fit to the data. We conduct extensive experiments in synthetic and real data across various ML models and find SGShift can identify shifted features with AUC &gt; 0.9 and recall &gt; 90%, often 2 or 3 times as high as baseline methods.

<a id="p047"></a>
## P047 · Can LLMs Propose Instrumental Variables for Causal Reasoning?

- **作者**：本地稿匿名；官方 CISPA 记录补充：Ivaxi Sheth; Zhijing Jin; Bryan Wilder; Dominik Janzing; Mario Fritz
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2025 Workshop（CISPA 记录日期 2025-12-06）；本地为匿名稿。 [CISPA机构记录](https://cispa.de/en/research/publications/104502-can-llms-propose-instrumental-variables-for-causal-reasoning-)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：18页；SHA-256：`c93595a135d3c4e837633d1fd4b30fe3f47805aa52e29411a4ef9dcbc6fa53c5`

### 中文摘要

用 LLM 提议并批判工具变量，探索观察数据中候选工具的发现。

### 核心贡献

IV Co-Scientist 多角色流程，以及无真值时的内部一致性比较。

### 实现边界

只能辅助提出候选；高 F 统计量只支持相关性，不能验证排除限制/独立性，内部一致也不等于因果有效。

### Method／方法

先测试恢复文献工具和拒绝已被推翻的工具；代理提议处理—结果—工具组合并批判假设，再比较第一阶段强度与估计一致性。

### Results／主要结果

5 个自动发现案例中多种候选表现出较强相关及高于随机代理的内部一致性；论文未建立所有新工具的真实有效性。

### Shortcomings／局限与可能不足

【解读】语义批评共享模型偏差；缺乏真值时一致性不足以排除共同混杂，候选须领域知识进一步审核。

### 证据定位

摘要；§2.1–2.2/表1；附录 C、H；CISPA 作者记录。

### Abstract

In the presence of confounding between an endogenous variable and the outcome, instrumental variables (IVs) are used to isolate causal effects. Identifying valid instruments requires interdisciplinary knowledge and contextual understanding, making it a difficult task. In this paper, we examine whether large language models (LLMs) can assist. We adopt a two-stage evaluation: first, testing whether LLMs recover established instruments from the literature, and second, assessing whether they avoid empirically or theoretically discredited ones. Building on these results, we introduce IV Co-Scientist, a multi-agent system that proposes, critiques, and refines IVs, along with a statistical test to contextualize consistency without ground truth. Our results show the potential of LLMs to identify valid IVs from large observational data.

<a id="p048"></a>
## P048 · Utility-Directed Conformal Prediction: A Decision-Aware Framework for Actionable Uncertainty Quantification

- **作者**：Santiago Cortes-Gomez; Carlos Patiño; Yewon Byun; Zhiwei Steven Wu; Eric Horvitz; Bryan Wilder
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICLR 2025（PDF 明示）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：20页；SHA-256：`014cd623273d23418cf34a7100f3f8741e56e4c4ca3ad9442505448e46e2df75`

### 中文摘要

把下游成本纳入保形预测，使具有覆盖保证的预测集合更适合实际决策。

### 核心贡献

针对可分/不可分效用构造 nonconformity score 与集合选择方法，并证明保留标准覆盖。

### 实现边界

标准覆盖依赖校准/测试交换性等条件，通常是边际保证；皮肤诊断为数据集示例，未做临床试验。

### Method／方法

利用标签或集合成本构造惩罚比率/保形分数，再做校准；在分类层级中偏好临床或语义更一致的集合。

### Results／主要结果

CIFAR-100、iNaturalist、ImageNet、Fitzpatrick 的所测效用成本均低于标准保形基线，并经验保持覆盖率。

### Shortcomings／局限与可能不足

【解读】需预先定义有意义的效用，分布变化影响保证；成本低不必然代表所有用户或群体都受益。PDF 代码链接仍写 [hidden]。

### 证据定位

§3；§4/图3及附录表4–6；§5、Reproducibility Statement。

### Abstract

Interest has been growing in decision-focused machine learning methods which train models to account for how their predictions are used in downstream optimization problems. Doing so can often improve performance on subsequent decision problems. However, current methods for uncertainty quantification do not incorporate any information about downstream decisions. We develop a methodology based on conformal prediction to identify prediction sets that account for a downstream cost function, making them more appropriate to inform high-stakes decision-making. Our approach harnesses the strengths of conformal methods—modularity, model-agnosticism, and statistical coverage guarantees—while incorporating downstream decisions and user-specified utility functions. We prove that our methods retain standard coverage guarantees. Empirical evaluation across a range of datasets and utility metrics demonstrates that our methods achieve significantly lower costs than standard conformal methods. We present a real-world use case in healthcare diagnosis, where our method effectively incorporates the hierarchical structure of dermatological diseases. The method successfully generates sets with coherent diagnostic meaning, potentially aiding triage for dermatology diagnosis and illustrating how our method can ground high-stakes decision-making employing domain knowledge.

<a id="p049"></a>
## P049 · Decision-Focused Learning without Differentiable Optimization: Learning Locally Optimized Decision Losses

- **作者**：Sanket Shah; Kai Wang; Bryan Wilder; Andrew Perrault; Milind Tambe
- **时间**：2022年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2022（正式会议 PDF）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：文件名写 without decision making，但首页实际标题是 without Differentiable Optimization。

- **主题**：XR与人机协作
- **PDF版本**：13页；SHA-256：`07b280867fab39304c2cddf0d2c056e09cce4810f27d2c1fa7395b6ecf454ccf`

### 中文摘要

通过学习局部决策损失，让预测训练适应下游优化而无需对求解器求导。

### 核心贡献

LODL 用黑盒优化器生成监督，学习可凸的任务相关损失。

### 实现边界

仍需大量调用黑盒求解器来拟合损失；“without differentiable optimization”并非完全不做优化。

### Method／方法

在真实标签附近扰动预测，用决策质量作为目标，拟合加权 MSE/方向二次型等局部损失，再用于训练预测网络。

### Results／主要结果

三个资源分配域均优于任务无关的两阶段训练，部分超过手工可微代理；样本增多通常提高表现，损失学习可并行/复用。

### Shortcomings／局限与可能不足

【作者】局部邻域/损失族选择影响泛化和成本；【解读】关于损失的凸性不使整个神经网络训练全局凸。

### 证据定位

§4；§5/表1–3；§6。

### Abstract

Decision-Focused Learning (DFL) is a paradigm for tailoring a predictive model to a downstream optimization task that uses its predictions in order to perform better on that specific task . The main technical challenge associated with DFL is that it requires being able to differentiate through the optimization problem, which is difficult due to discontinuous solutions and other challenges. Past work has largely gotten around this this issue by handcrafting task-specific surrogates to the original optimization problem that provide informative gradients when differentiated through. However, the need to handcraft surrogates for each new task limits the usability of DFL. In addition, there are often no guarantees about the convexity of the resulting surrogates and, as a result, training a predictive model using them can lead to inferior local optima. In this paper, we do away with surrogates altogether and instead learn loss functions that capture task-specific information. To the best of our knowledge, ours is the first approach that entirely replaces the optimization component of decision-focused learning with a loss that is automatically learned. Our approach (a) only requires access to a black-box oracle that can solve the optimization problem and is thus generalizable, and (b) can be convex by construction and so can be easily optimized over. We evaluate our approach on three resource allocation problems from the literature and find that our approach outperforms learning without taking into account task-structure in all three domains, and even hand-crafted surrogates from the literature.

<a id="p050"></a>
## P050 · Distributionally Robust Feature Selection

- **作者**：Maitreyi Swaroop; Tamar Krishnamurti; Bryan Wilder
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2025（会议论文）
- **项目／代码／数据**：[代码：maitreyiswaroop/dro-feature-selection](https://github.com/maitreyiswaroop/dro-feature-selection)

- **主题**：XR与人机协作
- **PDF版本**：30页；SHA-256：`cac9cafdc4deee05eb02c15751e5836ebb631d2b2dc2cfdc711c559e78b23cb1`

### 中文摘要

在观测特征预算下选择对多个子群体都有用的特征，以支持分别训练高质量模型。

### 核心贡献

噪声连续松弛和 Bayes 最优预测方差目标，避免反传穿过训练过程。

### 实现边界

选择共享特征，但下游允许各群体自己的模型；理论推导核心为 MSE，不能当作已证明所有损失适用。

### Method／方法

对特征加可控噪声，估计各组目标并最小化最差组损失，用重参数化和核估计做梯度优化。

### Results／主要结果

合成及 ACS/UCI 试验中优于所列 Lasso、XGBoost 和 DRO 改编基线；ACS 设置报告 MSE 数量级下降，UCI 分类也有经验收益。

### Shortcomings／局限与可能不足

【作者】插件估计在小群体可能偏，非 MSE 理论待扩展；【解读】依赖已知群体及代表性训练数据。

### 证据定位

§3；§4.3/图3；§5。

### Abstract

We study the problem of selecting limited features to observe such that models trained on them can perform well simultaneously across multiple subpopulations. This problem has applications in settings where collecting each feature is costly, e.g. requiring adding survey questions or physical sensors, and we must be able to use the selected features to create high-quality downstream models for different populations. Our method frames the problem as a continuous relaxation of traditional variable selection using a noising mechanism, without requiring backpropagation through model training processes. By optimizing over the variance of a Bayes-optimal predictor, we develop a model-agnostic framework that balances overall performance of downstream prediction across populations. We validate our approach through experiments on both synthetic datasets and real-world data.

<a id="p051"></a>
## P051 · Fostering the Ecosystem of AI for Social Impact Requires Expanding and Strengthening Evaluation Standards

- **作者**：Bryan Wilder; Angela Zhou
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2025，Position Paper Track；本地文件制作时间 2026 不应改为发表年
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：12页；SHA-256：`6b56fdf0a819fde5506ab115474a0b52b77b5cb85fb93651b35c2f8a3e26a794`

### 中文摘要

主张扩大社会影响贡献的认可范围，同时提高真实部署影响评价的严谨性。

### 核心贡献

区分方法创新、伙伴能力建设及部署贡献，讨论评审激励如何影响研究生态。

### 实现边界

立场论文，提出评价建议；没有新预测模型、受控干预结果或统一算法排行榜。

### Method／方法

分析既有评审标准和应用研究案例，分别讨论试点、随机与非随机部署、反方意见。

### Results／主要结果

建议作者明确影响机制、评审按贡献类型要求证据，并对部署研究采用更清晰和严格的效果评价。

### Shortcomings／局限与可能不足

【解读】观点依赖案例和规范性判断，尚无证据量化采用这些评审规则后的长期生态效果。

### 证据定位

§2–5；§6 Alternative views；§7。

### Abstract

There has been increasing research interest in AI/ML for social impact, and correspondingly more publication venues have refined review criteria for practice-driven AI/ML research. However, these review guidelines tend to most concretely recognize projects that simultaneously achieve deployment and novel ML methodological innovation. We argue that this introduces incentives for researchers that undermine the sustainability of a broader research ecosystem of social impact, which benefits from projects that make contributions on single front (applied or methodological) that may better meet project partner needs. Our position is that researchers and reviewers in machine learning for social impact must simultaneously adopt: 1) a more expansive conception of social impacts beyond deployment and 2) more rigorous evaluations of the impact of deployed systems.

<a id="p052"></a>
## P052 · Valid Inference with Imperfect Synthetic Data

- **作者**：Yewon Byun; Shantanu Gupta; Zachary C. Lipton; Rachel Leah Childers; Bryan Wilder
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2025（会议论文）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：40页；SHA-256：`f36995c8bce9d2c778ff92294498365045028b0df617164756664c6fa99ce9b8`

### 中文摘要

以广义矩估计整合真实、代理及完全合成数据，提高有限真实数据下的统计效率。

### 核心贡献

无需超参数的 GMM 估计器及一致性/渐近推断理论。

### 实现边界

仍需要真实数据与可识别的矩条件；理论有效性是渐近的，不能保证极少样本时精确覆盖。

### Method／方法

联合真实与合成矩残差，利用它们的预测相关性，估计权重和协方差构造参数与置信区间。

### Results／主要结果

8/8 个下游任务获得最低 MSE，7/8 的置信区间更窄；少标注设置多次 MSE 降幅超过 50%，并经验保持覆盖。

### Shortcomings／局限与可能不足

【作者】劣质合成数据可能无收益，极低数据量可欠覆盖；【解读】不能用模型模拟受试者完全替代真实样本。

### 证据定位

§4.5；§5.3/图1–2；§6 Limitations。

### Abstract

Predictions and generations from large language models are increasingly being explored as an aid in limited data regimes, such as in computational social science and human subjects research. While prior technical work has mainly explored the potential to use model-predicted labels for unlabeled data in a principled manner, there is increasing interest in using large language models to generate entirely new synthetic samples (e.g., synthetic simulations), such as in responses to surveys. However, it remains unclear by what means practitioners can combine such data with real data and yet produce statistically valid conclusions upon them. In this paper, we introduce a new estimator based on generalized method of moments, providing a hyperparameter-free solution with strong theoretical guarantees to address this challenge. Intriguingly, we find that interactions between the moment residuals of synthetic data and those of real data (i.e., when they are predictive of each other) can greatly improve estimates of the target parameter. We validate the finite-sample performance of our estimator across different tasks in computational social science applications, demonstrating large empirical gains.

<a id="p053"></a>
## P053 · Superhuman performance of a large language model on the reasoning tasks of a physician

- **作者**：Peter G. Brodeur; Thomas A. Buckley; Zahir Kanjee; Ethan Goh; Evelyn Bin Ling; Priyank Jain; Stephanie Cabral; Raja-Elie Abdulnour; Adrian D. Haimovich; Jason A. Freed; Andrew Olson; Daniel J. Morgan; Jason Hom; Robert Gallo; Liam G. McCoy; Haadi Mombini; Christopher Lucas; Misha Fotoohi; Matthew Gwiazdon; Daniele Restifo; Daniel Restrepo; Eric Horvitz; Jonathan Chen; Arjun K. Manrai; Adam Rodman
- **时间**：预印首发2024-12-14；本地摘要对应2025-06-02 arXiv v3；正式Science论文2026-04-30上线
- **发表平台／版本状态**：Science 392(6797):524–527，2026-04-30，DOI 10.1126/science.adz4433；正式题名为Performance of a large language model on the reasoning tasks of a physician（删除Superhuman）。本条英文摘要与结果仍按本地预印稿。 [PubMed正式发表记录](https://pubmed.ncbi.nlm.nih.gov/42060751/)；[arXiv记录](https://arxiv.org/abs/2412.10849)
- **论文链接**：[DOI正式记录](https://doi.org/10.1126/science.adz4433)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：Science正式版修改了题名与摘要措辞；本地PDF是较早的Superhuman题名版本，不将其摘要或具体数值直接标为正式版原文。

- **主题**：XR与人机协作
- **PDF版本**：25页；SHA-256：`4e1cb616b98899043525e3ff7dc712029af55202ad46371e676e7f2d52ac471f`

### 中文摘要

用医生评分的复杂病例、诊断/管理任务及急诊第二意见场景评价 OpenAI o1 系列。

### 核心贡献

把评价扩展到临床推理过程和真实病历，而不局限选择题考试。

### 实现边界

主要为离线病例及预定义时间点第二意见；未证明真实部署改善患者结局，也未实证人机团队优于医生。

### Method／方法

五类病例推理实验加急诊研究，专家使用 Bond/R-IDEA 等量表评分，与历史和医生基线比较；分别考察 o1-preview 与 o1。

### Results／主要结果

143 个 NEJM 病例中鉴别列表含正确诊断 78.3%（95%CI 70.7–84.8），首位诊断正确 52%；80 份 Healer 回答中 78 份 R-IDEA 满分；“不可漏诊”覆盖未显著优于对照。

### Shortcomings／局限与可能不足

【作者】领域/病例有限，需前瞻试验及协作研究；【解读】量表满分和候选列表命中不是独立临床胜任，历史对照与数据泄漏风险需保留。

### 证据定位

摘要 PDF p2；结果 p3–5；讨论 p5–6；方法 p6 起。

### Abstract

A seminal paper published by Ledley and Lusted in 1959 introduced complex clinical diagnostic reasoning cases as the gold standard for the evaluation of expert medical computing systems, a standard that has held ever since. Here, we report the results of a physician evaluation of a large language model (LLM) on challenging clinical cases against a baseline of hundreds of physicians. We conduct five experiments to measure clinical reasoning across differential diagnosis generation, display of diagnostic reasoning, triage differential diagnosis, probabilistic reasoning, and management reasoning, all adjudicated by physician experts with validated psychometrics. We then report a real-world study comparing human expert and AI second opinions in randomly-selected patients in the emergency room of a major tertiary academic medical center in Boston, MA. We compared LLMs and board-certified physicians at three predefined diagnostic touchpoints: triage in the emergency room, initial evaluation by a physician, and admission to the hospital or intensive care unit. In all experiments—both vignettes and emergency room second opinions—the LLM displayed superhuman diagnostic and reasoning abilities, as well as continued improvement from prior generations of AI clinical decision support. Our study suggests that LLMs have achieved superhuman performance on general medical diagnostic and management reasoning, fulfilling the vision put forth by Ledley and Lusted, and motivating the urgent need for prospective trials.

<a id="p054"></a>
## P054 · Melding the Data-Decisions Pipeline: Decision-Focused Learning for Combinatorial Optimization

- **作者**：Bryan Wilder, Bistra Dilkina, Milind Tambe
- **时间**：2019年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：AAAI 2019（首页明示 AAAI-19），1658 起
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：严重错名：文件名为 25_Creating General User Models from Computer Use.pdf，实际内容为 2019 年 Melding the Data-Decisions Pipeline；目录未据此包含那篇用户建模论文。

- **主题**：XR与人机协作
- **PDF版本**：9页；SHA-256：`a7997e4591c5b639447f6fed81bd226792d743fe767781af22f9ce39b112a3fc`

### 中文摘要

把预测与组合优化端到端连接，直接按最终决策质量训练预测器。

### 核心贡献

为线性规划和子模最大化提供可反传的连续松弛框架。

### 实现边界

适用所分析的优化结构和松弛条件；不是用户建模或计算机使用日志研究。

### Method／方法

将离散优化连续化，计算决策目标对预测参数的梯度；以优化效用训练模型并与两阶段 MSE 训练比较。

### Results／主要结果

多种决策问题上提高最终效用，即使预测 MSE 更差；示例中决策训练模型的通道总权重与真值相关 r²=0.94，解释了正确排序的重要性。

### Shortcomings／局限与可能不足

【解读】松弛与整数决策存在差距，依赖优化器和任务结构；牺牲预测校准后的输出不宜直接当真实量。

### 证据定位

首页/元数据；技术框架及实验；图2讨论，PDF p7–8。

### Abstract

Creating impact in real-world settings requires artificial intelligence techniques to span the full pipeline from data, to predictive models, to decisions. These components are typically approached separately: a machine learning model is first trained via a measure of predictive accuracy, and then its predictions are used as input into an optimization algorithm which produces a decision. However, the loss function used to train the model may easily be misaligned with the end goal, which is to make the best decisions possible. Hand-tuning the loss function to align with optimization is a difficult and error-prone process (which is often skipped entirely). We focus on combinatorial optimization problems and introduce a general framework for decision-focused learning, where the machine learning model is directly trained in conjunction with the optimization algorithm to produce highquality decisions. Technically, our contribution is a means of integrating common classes of discrete optimization problems into deep learning or other predictive models, which are typically trained via gradient descent. The main idea is to use a continuous relaxation of the discrete problem to propagate gradients through the optimization procedure. We instantiate this framework for two broad classes of combinatorial problems: linear programs and submodular maximization. Experimental results across a variety of domains show that decisionfocused learning often leads to improved optimization performance compared to traditional methods. We find that standard measures of accuracy are not a reliable proxy for a predictive model’s utility in optimization, and our method’s ability to specify the true goal as the model’s training objective yields substantial dividends across a range of decision problems.

<a id="p055"></a>
## P055 · Principles of Mixed-Initiative User Interfaces

- **作者**：Eric Horvitz
- **时间**：1999年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CHI 1999，1999-05-15—20，pp.159–166（PDF首页）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：8页；SHA-256：`d242048fb0ad4247cd2b0f4a1872c94f319ae8b311fa18df6195fb5361331348`

### 中文摘要

讨论如何将直接操作与自动化代理结合，提出处理用户意图不确定性、打扰成本和人机共同修正结果的设计原则，以Lookout邮件日程助手说明。

### 核心贡献

归纳12条混合主动权界面原则，并将不确定性与动作效用引入“等待／询问／主动执行”的选择。

### 实现边界

实现是叠加在Outlook上的邮件时间解析和日程建议原型；不是通用任务代理，也不是对12条原则的全面因果验证。

### Method／方法

SVM文本分类并校准意图概率；按收益、误操作及打扰成本设置决策阈值；结合阅读停留时间选择介入时机；允许手动调用、取消、降级到日历范围及编辑建议。

### Results／主要结果

展示Lookout自动提取会议日期、创建待确认预约、低置信度询问和时机建模；文中主要证据是系统与概率/效用曲线，未提供现代意义的大样本随机对照效率提升结果。

### Shortcomings／局限与可能不足

【解读】依赖领域解析规则、意图概率与主观成本模型；意图识别错误和不适当打断仍可能发生，原则能否跨任务成立需另行评估。

### 证据定位

PDF pp.1–2：12条原则；pp.2–7：Lookout实现、概率/效用及注意力模型；pp.7–8：总结。

### Abstract

Recent debate has centered on the relative promise of focusing user-interface research on developing new metaphors and tools that enhance users’ abilities to directly manipulate objects versus directing effort toward developing interface agents that provide automation. In this paper, we review principles that show promise for allowing engineers to enhance human-computer interaction through an elegant coupling of automated services with direct manipulation. Key ideas will be highlighted in terms of the Lookout system for scheduling and meeting management.

<a id="p056"></a>
## P056 · Vibe Coding XR: Accelerating AI + XR Prototyping with XR Blocks and Gemini

- **作者**：Ruofei Du; Benjamin Hersh; David Li; Nels Numan; Xun Qian; Yanhe Chen; Zhongyi Zhou; Jiahao Ren; Xingyue Chen; Robert Timothy Bettridge; Faraz Faruqi; Xiang ‘Anthony’ Chen; Steve Toh; David Kim
- **时间**：本地PDF未明确；未按文件名或PDF制作时间推断。
- **发表平台／版本状态**：2026年预印本；首页标注arXiv，ACM DOI/ISBN为占位符，不能据此认定正式ACM发表
- **项目／代码／数据**：[项目/演示页面](https://xrblocks.github.io/gem)；[代码：google/xrblocks](https://github.com/google/xrblocks)

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：10页；SHA-256：`eeb4f0c125281216f66235077762dabb3a17831374fc227303153c7d33c50ed3`

### 中文摘要

通过XR Blocks的高层空间交互API与Gemini，将自然语言需求生成可运行WebXR原型，并提供60条提示的初步技术评测。

### 核心贡献

整合提示、代码生成、人工检查与即时XR运行的工作流；发布XR Blocks及VCXR60试点任务。

### 实现边界

60提示来自20人四次工作坊；pass@1仅指桌面模拟器无运行错误，不衡量视觉质量、需求满足或真机交互正确性。“一分钟内”不是所有配置的结果。

### Method／方法

Reality Model封装用户、物理场景、感知/交互组件；Gemini生成脚本；XR Blocks v0.11.0通过Playwright无头Chromium监控错误，四种配置各运行5轮。

### Results／主要结果

表1：Gemini3.1Pro高思考pass@1=95.5%，时间中位86.02秒；低思考94.1%/33.39秒；3Flash高87.8%/22.26秒、低87.4%/17.30秒。每条提示5次中至少一次无错误。

### Shortcomings／局限与可能不足

【作者】Web性能与云延迟、模型幻觉API及复杂空间逻辑错误；【解读】开发时基于该试点反复修复框架，独立留出集与任务语义/真机评测不足。

### 证据定位

PDF pp.3–5：框架、表1及§4–5。

### Abstract

While large language models have accelerated software development through “vibe coding”, prototyping intelligent Extended Reality (XR) experiences remains inaccessible due to the friction of complex game engines and low-level sensor integration. To bridge this gap, we contribute XR Blocks, an open-source, modular WebXR framework that abstracts spatial computing complexities into high-level, human-centered primitives. Building upon this foundation, we present Vibe Coding XR, an end-to-end rapid prototyping workflow that leverages LLMs to translate natural language intent directly into functional XR software. Using a web-based interface, creators can transform high-level prompts (e.g., “create a dandelion that reacts to hand” ) into interactive WebXR applications in under a minute. We provide a preliminary technical evaluation on a pilot dataset (VCXR60) alongside diverse application scenarios highlighting mixed-reality realism, multi-modal interaction, and generative AI integrations. By democratizing spatial software creation, this work empowers practitioners to bypass lowlevel hurdles and rapidly move from “idea to reality. ” Code and live demos are available at https://github.com/google/xrblocks and http://xrblocks.github.io/gem.

<a id="p057"></a>
## P057 · Thing2Reality: Enabling Spontaneous Creation of 3D Objects from 2D Content using Generative AI in XR Meetings

- **作者**：Erzhen Hu, Mingyi Li, Jungtaek Hong, Xun Qian, Alex Olwal, David Kim, Seongkook Heo, and Ruofei Du
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：UIST 2025，2025-09-28—10-01；DOI 10.1145/3746059.3747621
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3746059.3747621)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作
- **PDF版本**：16页；SHA-256：`76717358341146a96d67837248e800d3852cdff07b304ccea212e53a425ff561`

### 中文摘要

在远程XR会议中把物理物体、网页图片转成可共同操作的3D表示，并在3D对象与2D白板快照间切换，支持即时讨论。

### 核心贡献

实现Thing2Reality的物体级2D→3D→2D交互链，研究多种表示在协作不同阶段的互补用途。

### 实现边界

生成的是条件多视图/3D Gaussian近似表示，不保证精确几何、尺寸或不可见表面；研究为探索性原型评估，未设置2D屏幕共享基线。

### Method／方法

用户圈选对象→MobileSAM分割→条件多视图扩散与LGM Gaussian重建→Unity多人XR；支持缩放、移动、正交视图和白板投影。

### Results／主要结果

单人研究N=12均完成任务，工作流评分4.9/5、参与感5/5；双人研究18人/9对观察到2D组织叙事、3D空间解释及混合/顺序使用策略；7/9对准备演示时主动生成多个2D快照。

### Shortcomings／局限与可能不足

【作者】小样本、单次实验，缺少基线和长期使用；专业精度不足，抽象概念难以实体化；生成误差、尺寸理解与格式切换认知负担。

### 证据定位

PDF pp.4–7：实现、研究1；pp.8–12：研究2；§8.3。

### Abstract

During remote communication, participants often share both digital and physical content, such as product designs, digital assets, and environments, to enhance mutual understanding. Recent advances in augmented communication have facilitated users to swiftly create and share digital 2D copies of physical objects from video feeds into a shared space. However, conventional 2D representations of digital objects limits spatial referencing in immersive environments. To address this, we propose Thing2Reality, an Extended Reality (XR) meeting platform that facilitates spontaneous discussions of both digital and physical items during remote sessions. With Thing2Reality, users can quickly materialize ideas or objects in immersive environments and share them as conditioned multiview renderings or 3D Gaussians. Thing2Reality enables users to interact with remote objects or discuss concepts in a collaborative manner. Our user studies revealed that the ability to interact with and manipulate 3D representations of objects significantly enhances the efficiency of discussions, with the potential to augment discussion of 2D artifacts.

<a id="p058"></a>
## P058 · How Well Can 3D Accessibility Guidelines Support XR Development? An Interview Study with XR Practitioners in Industry

- **作者**：Daniel Killough; Tiger F. Ji; Kexin Zhang; Yaxin Hu; Yu Huang; Ruofei Du; Yuhang Zhao
- **时间**：2026年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CHI 2026，2026-04-13—17；DOI 10.1145/3772318.3790520
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3772318.3790520)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：15页；SHA-256：`f35c8a8c027b4841c09d5f2ae8da50f5844ff810285a9c4c4eef92710867daf9`

### 中文摘要

访谈25位XR行业从业者，检查六套资源中的20项3D无障碍指南能否支持XR开发，分析指南含糊、场景不匹配和落实责任问题。

### 核心贡献

给出跨视觉、运动、认知、言语、听觉的指南适用性分析与开发责任/实施建议；强调指南应提供可操作示例。

### 实现边界

评估对象是从业者对指南的解释和可行性判断；没有实现并测量全套辅助功能，也没有证明残障用户效果改善。

### Method／方法

半结构访谈、指南排序/讨论、主题分析，将优先级、开发阶段和责任组织成矩阵。

### Results／主要结果

25人均提出可结合其项目的实现思路；12人报告沉浸与无障碍的张力，20人希望补充具体案例/实现；发现即时安全、平台依赖、需情境调整等不同优先级。

### Shortcomings／局限与可能不足

【作者/解读】样本规模和行业背景限制概括性，25人中23男2女；自述意愿不等于真实落地，残障最终用户的直接验证仍不足。

### 证据定位

PDF §3–4、表2–3、§5.3；pp.3–11。

### Abstract

While accessibility (a11y) guidelines exist for 3D games and virtual worlds, their applicability to extended reality (XR)’s unique interaction paradigms (e.g.,spatial tracking, kinesthetic interactions) remains unexplored. XR practitioners need practical guidance to successfully implement a11y guidelines under real-world constraints. We present the first evaluation of existing 3D a11y guidelines applied to XR development through semi-structured interviews with 25 XR practitioners across diverse organization contexts. We assessed 20 commonly-agreed a11y guidelines from six major resources across visual, motor, cognitive, speech, and hearing domains, comparing practitioners’ development practices against guideline applicability to XR. Our investigation reveals that guidelines can be highly effective when designed as transformation catalysts rather than compliance checklists, but fundamental mismatches exist between existing 3D guidelines and XR requirements, creating both implementation barriers and design gaps. This work provides foundational insights towards developing a11y guidelines and support tools that address XR’s distinct characteristics.

<a id="p059"></a>
## P059 · Sensible Agent: A Framework for Unobtrusive Interaction with Proactive AR Agents

- **作者**：Geonsun Lee; Min Xia; Nels Numan; Xun Qian; David Li; Yanhe Chen; Achin Kulshrestha; Ishan Chatterjee; Yinda Zhang; Dinesh Manocha; David Kim; Ruofei Du
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：UIST 2025；DOI 10.1145/3746059.3747748
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3746059.3747748)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作
- **PDF版本**：22页；SHA-256：`f5caf04876cd2886402ba5aaff888b582997be5298e87724d8a715a334b73344`

### 中文摘要

结合多模态情境感知决定主动AR助手提供什么帮助，以及用语音、视觉、头/手/注视等何种方式交互，从而降低打扰和主观操作负担。

### 核心贡献

将建议内容和交互模态联合适配；专家工作坊N=12、标注研究N=40及XR原型研究N=10支撑设计。

### 实现边界

当前没有长期用户偏好建模，也未求解精确的介入时机；测试为有限AR和360°视频场景。

### Method／方法

第一视角相机/传感器与LMM推断活动和约束，选择图标、二选一或多选建议及可用输入模态；与语音提问基线做被试内比较。

### Results／主要结果

N=10：Raw-TLX均值20.55对43.27，主观负担降低；偏好6.00对3.80/7；但交互更慢，28.54秒对16.43秒（p&lt;.001）。SUS81.33对76.67，差异不显著（p=.11）。

### Shortcomings／局限与可能不足

【作者】小样本、探索统计未校正多重比较，缺少常显多选界面对照；无长期个性化/时机模型。【解读】不能由较低主观负担推断客观效率提高。

### 证据定位

PDF pp.14–16，§7.4、图8、§9。

### Abstract

Proactive AR agents promise context-aware assistance, but their interactions often rely on explicit voice prompts or responses, which can be disruptive or socially awkward. We introduce Sensible Agent, a framework designed for unobtrusive interaction with these proactive agents. Sensible Agent dynamically adapts both “what” assistance to offer and, crucially, “how” to deliver it, based on real-time multimodal context sensing. Informed by an expert workshop (n=12) and a data annotation study (n=40), the framework leverages egocentric cameras, multimodal sensing, and Large Multimodal Models (LMMs) to infer context and suggest appropriate actions delivered via minimally intrusive interaction modes. We demonstrate our prototype on an XR headset through a user study (n=10) in both AR and VR scenarios. Results indicate that Sensible Agent significantly reduces perceived interaction effort compared to voice-prompted baseline, while maintaining high usability and achieving higher preference.

<a id="p060"></a>
## P060 · XR Blocks: Accelerating Human-centered AI + XR Innovation

- **作者**：David Li; Nels Numan; Xun Qian; Yanhe Chen; Zhongyi Zhou; Evgenii Alekseev; Geonsun Lee; Alex Cooper; Min Xia; Scott Chung; Jeremy Nelson; Xiuxiu Yuan; Jolica Dias; Tim Bettridge; Benjamin Hersh; Michelle Huynh; Konrad Piascik; Ricardo Cabello; David Kim; Ruofei Du
- **时间**：本地版本：2025-09-29（arXiv:2509.25504v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preliminary White Paper，2025-09；arXiv:2509.25504v1
- **论文链接**：[arXiv本地版本 2509.25504v1](https://arxiv.org/abs/2509.25504v1)
- **项目／代码／数据**：[项目/演示页面](https://xrblocks.github.io)；[代码：google/xrblocks](https://github.com/google/xrblocks)
- **版本关系**：[P056](#p056)在该框架上进一步加入Gemini工作流和初步技术评测；本稿是较早白皮书。

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：9页；SHA-256：`e55cf9cd2a2e2651019cb9926d88c8c242fdda9c1df4e3e29b8c1bf375ec6f08`

### 中文摘要

提出跨桌面模拟器与XR设备的模块化Web框架，统一感知、渲染、交互和AI服务，以减少AI+XR原型开发的集成工作。

### 核心贡献

Reality Model与可插拔Core引擎，提供用户、世界、交互及AI模板和演示。

### 实现边界

作者明确说agents、peers、context等概念原语仅初步实现；不是完整通用多代理/持久记忆/跨设备协作平台。

### Method／方法

WebXR、three.js、TensorFlow及Gemini之上封装相机/深度/音频、物理、手势与智能模块，同一高层脚本在模拟器和设备运行。

### Results／主要结果

展示遮挡/重照明、虚实物理交互、手势控制和情境助手等开源样例；本白皮书未报告受控开发效率实验或通用基准提升数值。

### Shortcomings／局限与可能不足

【作者】设计愿景尚未全部实现，Web性能低于原生引擎、云延迟、复杂用户与情境模型待完善。

### 证据定位

PDF §4–6，尤其§6.2 pp.6–7。

### Abstract

We are on the cusp where Artificial Intelligence (AI) and Extended Reality (XR) are converging to unlock new paradigms of interactive computing. However, a significant gap exists between the ecosystems of these two fields: while AI research and development is accelerated by mature frameworks like JAX and benchmarks like LMArena, prototyping novel AI-driven XR interactions remains a high-friction process, often requiring practitioners to manually integrate disparate, low-level systems for perception, rendering, and interaction. To bridge this gap, we present XR Blocks, a crossplatform framework designed to accelerate human-centered AI + XR innovation. XR Blocks strives to provide a modular architecture with plug-and-play components for core abstraction in AI + XR: user, world, peers; interface, context, and agents. Crucially, it is designed with the mission of “reducing frictions from idea to reality”, thus accelerating rapid prototyping of AI + XR apps. Built upon accessible technologies (WebXR, three.js, TensorFlow, Gemini), our toolkit lowers the barrier to entry for XR creators. We demonstrate its utility through a set of open-source templates, samples, and advanced demos, empowering the community to quickly move from concept to interactive XR prototype.

<a id="p061"></a>
## P061 · AgentHands: Generating Interactive Hand Gestures for Spatially Grounded Agent Conversations in XR

- **作者**：Ziyi Liu; David Li; Zhongyi Zhou; David Kim; Ruofei Du; Xun Qian
- **时间**：2026年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CHI 2026；DOI 10.1145/3772318.3790938
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3772318.3790938)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作
- **PDF版本**：24页；SHA-256：`4e70cdb316ca2322b9d9f88e65c0f61e7650371854027fe51de20c96b656225c`

### 中文摘要

让XR会话助手以与语音同步、指向真实场景的虚拟手势解释对象、动作和位置，缩小语言指令与空间理解之间的差距。

### 核心贡献

形成手势设计分类并实现带GestureEvents的语言生成、解析和动画流水线。

### 实现边界

依赖轻量预扫描对象注册表，主要适合静态场景；手势实例来自人工编写的有限集合，并非任意动作生成或物理机器人操作。

### Method／方法

N=10形成性研究→LLM生成按词对齐的手势类型/参数→解析为时间戳姿态→Unity/OpenXR渲染；Galaxy XR、Gemini2.5Flash与语音识别/合成。

### Results／主要结果

N=12被试内研究，定位对象评分6.50对4.58/7，参与感6.08对4.58，理解困难1.83对3.58；数值信息理解差异不显著。主要指标是体验问卷，未证明长期记忆或实际任务正确率提升。

### Shortcomings／局限与可能不足

【作者】预注册静态场景、有限手势库、细粒度操作精度、文化和个性化适配不足；【解读】小样本短时语音基线比较，不能分离所有视觉/同步因素。

### 证据定位

PDF §4.5、§6、图8 p.13、§7 pp.14–15。

### Abstract

Communicating spatial tasks via text or speech creates “a mental mapping gap” that limits an agent’s expressiveness. Inspired by co-speech gestures in face-to-face conversation, we proposeAgentHands, an LLM-powered XR system that equips agents with hands to render responses clearer and more engaging. Guided by a design taxonomy distilled from a formative study (N=10), we implement a novel pipeline to generate and render a hand agent that augments conversational responses with synchronized, space-aware, and interactive hand gestures: using a meta-instruction,AgentHands generates verbal responses embedded withGestureEvents aligned to specific words; each event specifies gesture type and parameters. At runtime, a parser converts events into time-stamped poses and motions, driving an animation system that renders expressive hands synchronized with speech. In a within-subjects study (N=12), AgentHands increased engagement and made spatially grounded conversations easier to follow compared to a speech-only baseline.

<a id="p062"></a>
## P062 · InstructPipe: Generating Visual Blocks Pipelines with Human Instructions and LLMs

- **作者**：Zhongyi Zhou; Jing Jin; Vrushank Phadnis; Xiuxiu Yuan; Jun Jiang; Xun Qian; Kristen Wright; Mark Sherwood; Jason Mayes; Jingtao Zhou; Yiyi Huang; Zheng Xu; Yinda Zhang; Johnny Lee; Alex Olwal; David Kim; Ram Iyengar; Na Li; Ruofei Du
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CHI 2025，2025-04-26—05-01；DOI 10.1145/3706598.3713905
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3706598.3713905)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：22页；SHA-256：`1c79bb8d2488e8d95ccebbb3496de4af2ac61c9a35d52e479d9b7237d307b410`

### 中文摘要

用自然语言生成Visual Blocks的ML可视化流水线，再由用户检查和编辑节点图，减少从空白画布寻找和连接节点的工作。

### 核心贡献

节点选择器、伪代码生成器与纠错编译器的模块化助手，结合技术评测及N=16用户研究。

### 实现边界

生成范围受已支持节点/API和解释器约束；不保证流水线语义完全正确，用户仍需理解和调试。

### Method／方法

LLM按指令选择节点→依据节点文档生成伪代码→解释器修复并编译JSON节点图→Visual Blocks交互修改。

### Results／主要结果

用户研究表2：完成时间中位203.5秒对304.5秒；交互次数中位5对16，均p&lt;.001；NASA-TLX六项中五项改善，心理需求未显著下降。论文“5倍”交互缩减来自其他评测条件，不能代替该用户研究的3.2倍。

### Shortcomings／局限与可能不足

【作者】生成结果的理解与调试、精确提示编写会增加心理负担；语言与视觉思考切换有成本；有限节点及用户任务限制外推。

### 证据定位

PDF §3–5、§6.5、表2 p.9、§7–8。

### Abstract

Visual programming has the potential of providing novice programmers with a low-code experience to build customized processing pipelines. Existing systems typically require users to build pipelines from scratch, implying that novice users are expected to set up and link appropriate nodes from a blank workspace. In this paper, we introduce InstructPipe, an AI assistant for prototyping machine learning (ML) pipelines with text instructions. We contribute two large language model (LLM) modules and a code interpreter as part of our framework. The LLM modules generate pseudocode for a target pipeline, and the interpreter renders the pipeline in the node-graph editor for further human-AI collaboration. Both technical and user evaluation (N=16) shows that InstructPipe empowers users to streamline their ML pipeline workflow, reduce their learning curve, and leverage open-ended commands to spark innovative ideas.

<a id="p063"></a>
## P063 · Large Language Models and Causal Inference in Collaboration: A Comprehensive Survey

- **作者**：Xiaoyu Liu; Paiheng Xu; Junda Wu; Jiaxin Yuan; Yifan Yang; Yuhang Zhou; Fuxiao Liu; Tianrui Guan; Haoliang Wang; Tong Yu; Julian McAuley; Wei Ai; Furong Huang
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：Findings of ACL: NAACL 2025，2025-04-29—05-04，pp.7683–7699
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：17页；SHA-256：`c65902b8d31e407e95a5902d022c21236bf54757c131aea82c03d264e43e73ee`

### 中文摘要

从双向关系综述因果推断与LLM：因果方法帮助推理、公平安全、可解释性和多模态建模；LLM知识与生成能力帮助因果发现和效应估计。

### 核心贡献

提供双向任务分类与方法梳理，组织因果视角下的LLM评测、干预和知识辅助推断。

### 实现边界

综述，没有提出统一因果求解器或新实验排行榜；文献中的因果保证依赖各自识别假设。

### Method／方法

按“因果推断→LLM”和“LLM→因果推断”组织研究，人工筛选相关论文/预印本并归纳挑战。

### Results／主要结果

主要产出为分类、研究对照和开放问题：因果知识、可识别性、模型偏差和评估可靠性仍需结合；无统一效应量可报告。

### Shortcomings／局限与可能不足

【作者】领域快速发展，侧重关键工作覆盖而非穷尽检索，预印本质量由人工判断；【解读】不同因果任务与数据假设之间的结果不可直接横比。

### 证据定位

PDF §2–5、p.9 Limitations。

### Abstract

Causal inference has demonstrated significant potential to enhance Natural Language Processing (NLP) models in areas such as predictive accuracy, fairness, robustness, and explainability by capturing causal relationships among variables. The rise of generative Large Language Models (LLMs) has greatly impacted various language processing tasks. This survey focuses on research that evaluates or improves LLMs from a causal view in the following areas: reasoning capacity, fairness and safety issues, explainability, and handling multimodality. Meanwhile, LLMs can assist in causal inference tasks, such as causal relationship discovery and causal effect estimation, by leveraging their generation ability and knowledge learned during pre-training. This review explores the interplay between causal inference frameworks and LLMs from both perspectives, emphasizing their collective potential to further the development of more advanced and robust artificial intelligence systems.

<a id="p064"></a>
## P064 · Causality Model for Semantic Understanding on Videos

- **作者**：Yicong Li（李逸聪；学位作者）；导师Tat-Seng Chua
- **时间**：本地版本：2025-03-16（arXiv:2503.12447v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：National University of Singapore博士学位论文，封面2023；arXiv:2503.12447v1，2025-03-16上传；各章对应ACM MM/CVPR/ICCV等独立论文
- **论文链接**：[arXiv本地版本 2503.12447v1](https://arxiv.org/abs/2503.12447v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：封面学位年份与arXiv上传年份不同；摘要中STR“question-irrelevant…as causal patterns”与方法描述矛盾，按正文应理解为选择问题相关证据，保留原文不擅改。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：139页；SHA-256：`f9114bfd9eae7a7dc8539edb63337135da99bd93a5bc3319fd7cf0c0e06ad626`

### 中文摘要

围绕视频关系检测与视频问答中的长尾、背景混淆和复杂时空结构，依次提出IVRD、IGV、EIGV和STR/TranSTR，研究因果建模与视觉证据选择。

### 核心贡献

四部分：关系原型与干预去偏；问题关键场景的不变定位；结合等变性的可解释定位；复杂长视频中关键帧和对象的时空选择。

### 实现边界

针对具体监督视频理解任务的结构建模与正则化；没有证实任意现实因果发现。作者明确缺少人类因果场景定位标注，主要由QA准确率间接验证定位质量。

### Method／方法

IVRD以对象轨迹和关系原型降低对象—关系偏置；IGV置换环境保持答案不变；EIGV再要求因果场景/问题语义变化引发答案等变；TranSTR可微选择时刻/对象并改进候选答案解码。

### Results／主要结果

表3.2 ImageNet-VidVRD：mAP22.97对基线21.24，零样本mAP1.47对0.60；表4.2 IGV NExT-QA51.34对HGA50.01；表5.2 EIGV跨骨干/数据集提升1.3–5.2个百分点；表6.3 TranSTR NExT-QA61.5、MSVD47.1、MSRVTT43.1，表6.4 Causal-VidQA62.2对VGT55.4。不同章的骨干/设置不同，不能视为单一连续受控消融。

### Shortcomings／局限与可能不足

【作者】缺乏直接视觉因果定位评估、迁移到大型VLM计算开销高、3D与现实复杂场景待探索；【解读】背景置换和因果图是建模假设，QA改进本身不证明识别真实因果机制。

### 证据定位

摘要PDF pp.9–11；表3.2 p.46、表4.2–3 p.71、表5.2 p.91、表6.3–4 p.114；结论pp.120–123。

### Abstract

After a decade of prosperity, the development of video understanding has reached a critical juncture, where the sole reliance on massive data and complex architectures is no longer a one-size-fits-all solution to all situations. The presence of ubiquitous data imbalance hampers DNNs from effectively learning the underlying causal mechanisms, leading to significant performance drops when encountering distribution shifts, such as long-tail imbalances and perturbed imbalances. This realization has prompted researchers to seek alternative methodologies to capture causal patterns in video data. To tackle these challenges and increase the robustness of DNNs, causal modeling emerged as a principle to discover the true causal patterns behind the observed correlations. This thesis focuses on the domain of semantic video understanding and explores the potential of causal modeling to advance two fundamental tasks: Video Relation Detection (VidVRD) and Video Question Answering (VideoQA). In summary, the major contributions of this thesis are as follows: • We propose an interventional video relation detection method , named IVRD, to address the long-tail imbalance of relation in VidVRD, where tail relations, despite being informative, are difficult to predict due to their scarcity in the dataset. Specifically, we form a set of relation prototypes in a hierarchical manner, which forces the relation reasoning module to focus on the visual content of dynamic interactions between entities rather than relying on spurious correlations between objects and relation labels. By incorporating causal reasoning, IVRD offers a promising direction for improving video understanding in the presence of long-tail imbalances, enabling models to better generalize to real-world scenarios where rare or infrequent relations may play a crucial role in the overall understanding of the scene. • We introduce the invariant grounding for VideoQA , dubbed as IGV, a model-agnostic learning framework that addresses the negative effect induced by the spurious correlations in the answer-environment. In essence, IGV discovers the causal reasoning pattern by grounding the questioncritical (causal) scene. Specifically, it leverages the fact that the relations between causal scenes and answers are invariant regardless of changes in the environment, and the removal of causal scenes should cause failure in answering the question. By grounding these critical scenes, IGV compels the VideoQA models to focus on the essential visual content for accurate reasoning, while shielding them from the negative influence of the environment, thus significantly improving the reasoning ability of the backbone models. • We introduce the equivariant grounding for VideoQA , EIGV, to further advance the robustness and visual explainability in a model-agnostic manner. Built on top of IGV, EIGV additionally incorporates equivariance, which encourages the answering process to be sensitive to the semantic changes in the causal scene and question. In comparison, invariant grounding enforces the answering to be insensitive to changes in the environmental scene. As a result, these two regularizations work collaboratively to distinguish the causal scene from the environment while providing more transparency by presenting the visual-linguistic alignment. By combining the strengths of both invariant and equivariant grounding, EIGV creates a more robust and explainable framework for VideoQA. • We discover spatio-Temporal rationales for VideoQA, which solve the low accuracy on samples with long video and multiple objects ( i.e.complex VideoQA). Since current VideoQA practices (including pretrained models, e.g.SeVila [158]) are mostly trained with short video clips ( ∼15s) with few entities (∼2), they tend to suffer from poor transferability to complex video (over 80s and 5 objects). The reason behind is that long videos inevitably introduce vast redundancy and spurious correlations due to the presence of numerous question-irrelevant environmental objects. Confronting this challenge, we first highlight the importance of modeling question-critical temporal moments and spatial objects, and then introduce Spatio-Temporal Rationalization (STR), which utilizes a differentiable selection module to adaptively gather question-critical moments and objects through cross-modal interaction. Coupled with a more reasonable candidate answer decoding strategy, STR effectively identifies question-irrelevant frames and objects as causal patterns, leading to improved predictions, especially in complex scenarios. A limitation of this thesis pertains to the evaluation of the identified causal scenes. Throughout the research, we have relied on the overall Question Answering (QA) performance as an indirect indicator of the discovered causal scene’s quality, which is based on the rationale that a more accurate localization of the causal scene can potentially yield richer question-relation visual cues, subsequently enhancing QA performance. However, it is essential to acknowledge that a direct quantitative measure rooted in the causal scene would offer more compelling insights. Regrettably, due to the absence of human-level grounding annotations, such a measurement remains absent in the current work. Therefore, future endeavors will focus on establishing an evaluation benchmark specifically tailored to the causal scene, involving human annotations on the visual elements that underpin the answering process. This initiative will contribute to a more comprehensive and rigorous assessment of causal scene discovery. In summary, our contributions extend the frontiers of causal modeling in semantic video understanding, empowering AI systems to grasp causal patterns and improve performance on challenging video understanding tasks.

<a id="p065"></a>
## P065 · Human-in-the-Loop through Chain-of-Thought

- **作者**：Zefan Cai; Baobao Chang; Wenjuan Han
- **时间**：本地版本：2023-06-23（arXiv:2306.07932v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2306.07932，首发2023-06-10；本地稿未标明正式会议。 [arXiv记录](https://arxiv.org/abs/2306.07932)
- **论文链接**：[arXiv本地版本 2306.07932v2](https://arxiv.org/abs/2306.07932v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：20页；SHA-256：`0a48c6cfe64884bc4292a0b31e6fd639697b72ad6161f55fcdbc5369721205f6`

### 中文摘要

通过人类局部修改LLM推理链提升多步推理，并用成本—效用模型分析人工纠错投入的取舍。

### 核心贡献

Manual Correction System（MCS）与CAMLOP成本效用模型，将中间逻辑修正和人工成本一起评估。

### 实现边界

使用text-davinci-002及12个推理数据集；改善包含额外人工信息，不能等同模型自主推理提升；经济模型最优性仅相对其成本/效用假设。

### Method／方法

人工检查并修正推理子步骤，继续生成；可结合self-consistency；以Cobb–Douglas式效用与预算分析纠错策略。

### Results／主要结果

8个算术数据集MCS比CoT平均+4.68个百分点，结合self-consistency平均+6.39；GSM8K56.48→61.56→62.92（5次运行中位）；还评估常识/符号任务。

### Shortcomings／局限与可能不足

【解读】人工知识、纠错质量及时间计价会影响结论；旧单一骨干和有限任务限制对现今模型与真实人机协作的外推。

### 证据定位

PDF §3–4、表2–3、§5–6。

### Abstract

While the emergence of powerful language models along with Chain-of-thought prompting has made automation more and more omnipresent, it sometimes demonstrates its weakness in long-term or multi-step logical reasoning. For example, users don’t always get desirable answers for complex mathematical problems without human involvement. Against this background, we present the Manual Correction System (MCS) — a human-in-the-loop system enhanced by Chainof-Thought prompting, which explores how manual correction of sub-logics in rationales can improve LLM’s reasoning performance. Moving one step forward, considering a system with human-in-the-loop involves more than having humans improve performance but also controlling the cost. Therefore, we post a Costutility Analysis Model for Human-in-the-Loop systems (CAMLOP) based on classical economics theory to analyze, quantify and balance the utility and the corresponding cost. We conduct experiments of MCS and CAMLOP with twelve datasets. A significant advantage w.r.t cost and utility proves its superiority over strong baselines.

<a id="p066"></a>
## P066 · Let’s Verify Step by Step

- **作者**：Hunter Lightman; Vineet Kosaraju; Yura Burda; Harri Edwards; Bowen Baker; Teddy Lee; Jan Leike; John Schulman; Ilya Sutskever; Karl Cobbe
- **时间**：预印稿2023年；正式发表于ICLR 2024，本地版本具体修订日未明示
- **发表平台／版本状态**：ICLR 2024（官方论文集核验）；本地为2023年较早预印稿。 [ICLR官方记录](https://proceedings.iclr.cc/paper_files/paper/2024/file/aca97732e30bcf1303bc22ac3924fd16-Paper-Conference.pdf)
- **项目／代码／数据**：[代码：openai/prm800k](https://github.com/openai/prm800k)

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：29页；SHA-256：`af32cabec7d40ca2d5b6bfc8ea28d6b5fdcf987eabb0843ca9a5a6f2371fdfaf`

### 中文摘要

比较对每一步推理给反馈的过程监督与只标记最终答案的结果监督，在数学推理中过程奖励模型更适合挑选可靠解答，并发布PRM800K人工标注。

### 核心贡献

系统对比PRM/ORM、主动学习收集步骤标注及约80万条反馈数据集。

### 实现边界

主要训练奖励/排序模型，固定生成器进行best-of-N选择；作者明确没有用奖励模型对生成器做RL。78%是在代表性MATH测试子集、较大采样预算下的结果。

### Method／方法

人类逐步判断正确/错误/中性，训练步骤奖励模型；与自动最终答案标签训练的ORM和多数投票比较；主动选择高价值错误样本。

### Results／主要结果

最佳过程监督系统在所评MATH子集解出约78%；PRM随N增加优于ORM和多数投票；主动学习带来约2.6倍数据效率提升。

### Shortcomings／局限与可能不足

【作者/解读】数学域和可检查答案限制泛化；大规模PRM/ORM训练数据并非完全可比，小规模实验补充控制；人工步骤标注昂贵，多样本排序增加推理成本。

### 证据定位

PDF §2、§3–5、图3、§8；方法边界p.3。

### Abstract

In recent years, large language models have greatly improved in their ability to perform complex multi-step reasoning. However, even stateof-the-art models still regularly produce logical mistakes. To train more reliable models, we can turn either to outcome supervision, which provides feedback for a final result, or process supervision, which provides feedback for each intermediate reasoning step. Given the importance of training reliable models, and given the high cost of human feedback, it is important to carefully compare the both methods. Recent work has already begun this comparison, but many questions still remain. We conduct our own investigation, finding that process supervision significantly outperforms outcome supervision for training models to solve problems from the challenging MATH dataset. Our process-supervised model solves 78% of problems from a representative subset of the MATH test set. Additionally, we show that active learning significantly improves the efficacy of process supervision. To support related research, we also release PRM800K, the complete dataset of 800,000 step-level human feedback labels used to train our best reward model.

<a id="p067"></a>
## P067 · τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- **作者**：Shunyu Yao; Noah Shinn; Pedram Razavi; Karthik Narasimhan
- **时间**：本地版本：2024-06-17（arXiv:2406.12045v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：2024年arXiv预印本（本地版本）
- **论文链接**：[arXiv本地版本 2406.12045v1](https://arxiv.org/abs/2406.12045v1)
- **项目／代码／数据**：[代码：sierra-research/tau-bench](https://github.com/sierra-research/tau-bench)

- **主题**：XR与人机协作
- **PDF版本**：50页；SHA-256：`0ce66a1763d698c61bb311c3c874bf593d1e9a5bfff11bb35f6f72b981f6da56`

### 中文摘要

用模拟用户、领域规则和API数据库交互评估语言代理，检查最终数据库是否达成目标，并衡量多次执行都成功的可靠性。

### 核心贡献

零售/航空服务任务及pass^k一致性指标，补充静态工具调用基准。

### 实现边界

用户由LLM模拟，后端为受控数据库；pass^k指k次都成功，和至少一次成功的pass@k相反；数据库结果匹配无法穷尽所有对话品质/规则违规。

### Method／方法

给代理政策与工具、模拟用户给需求，通过交互完成状态改变；匹配最终状态并重复运行估计一致成功率。

### Results／主要结果

表2 GPT-4o pass^1零售61.2%、航空35.2%，按领域平均48.2%；零售pass^8低于25%。因此摘要“&lt;50%”是跨领域平均，不是每个域都低于50%。

### Shortcomings／局限与可能不足

【解读】两域、模拟用户和有限任务影响外部效度；成功依赖模型版本/提示/工具实现，最终状态评估也可能漏掉过程中错误。

### 证据定位

PDF §2–5、表2、图4。

### Abstract

Existing benchmarks do not test language agents on their interaction with human users or ability to follow domain-specific rules, both of which are vital for deploying them in real world applications. We propose τ-bench, a benchmark emulating dynamic conversations between a user (simulated by language models) and a language agent provided with domain-specific API tools and policy guidelines. We employ an efficient and faithful evaluation process that compares the database state at the end of a conversation with the annotated goal state. We also propose a new metric (pass^k) to evaluate the reliability of agent behavior over multiple trials. Our experiments show that even state-of-the-art function calling agents (like gpt-4o) succeed on &lt; 50% of the tasks, and are quite inconsistent (pass^8 &lt; 25% in retail). Our findings point to the need for methods that can improve the ability of agents to act consistently and follow rules reliably.

<a id="p068"></a>
## P068 · TPDiff: Temporal Pyramid Video Diffusion Model

- **作者**：Lingmin Ran; Mike Zheng Shou
- **时间**：本地版本：2025-03-12（arXiv:2503.09566v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2503.09566v1，2025-03（本地预印本）
- **论文链接**：[arXiv本地版本 2503.09566v1](https://arxiv.org/abs/2503.09566v1)
- **项目／代码／数据**：[项目/演示页面](https://showlab.github.io/TPDiff/)

- **主题**：世界机制与演化
- **PDF版本**：11页；SHA-256：`6b838eac12b8bc1270dcdc00e5c80b63d18971a73a7554cd9d0f9f90206ced06`

### 中文摘要

利用扩散前期高噪声下的帧冗余，以低帧率起步并逐阶段增加帧率，配合分阶段扩散训练降低视频生成成本。

### 核心贡献

时间金字塔扩散与stage-wise训练，统一减少训练和采样计算。

### 实现边界

需要相应训练/适配；验证以MiniFlux-vid、AnimateDiff等配置为主，不是任意预训练视频模型的无损即插即用加速。

### Method／方法

沿去噪过程分段求解概率流ODE，阶段间时序插值并对齐数据/噪声，仅末段使用完整帧率。

### Results／主要结果

30步采样：MiniFlux-vid20.79→12.18秒（1.71倍），AnimateDiff6.01→4.04秒（1.49倍）；训练速度约2/2.13倍，所评VBench多数指标保持或改善。

### Shortcomings／局限与可能不足

【解读】速度依赖帧数/架构/硬件；早期低时间分辨率可能丢失快速运动信息，长视频/高动态真实需求的普遍质量保证未建立。

### 证据定位

PDF §3–4、表1–2、图5 pp.6–8。

### Abstract

The development of video diffusion models unveils a significant challenge: the substantial computational demands. To mitigate this challenge, we note that the reverse process of diffusion exhibits an inherent entropy-reducing nature. Given the inter-frame redundancy in video modality, maintaining full frame rates in high-entropy stages is unnecessary. Based on this insight, we propose TPDiff, a unified framework to enhance training and inference efficiency. By dividing diffusion into several stages, our framework progressively increases frame rate along the diffusion process with only the last stage operating on full frame rate, thereby optimizing computational efficiency. To train the multi-stage diffusion model, we introduce a dedicated training framework: stage-wise diffusion. By solving the partitioned probability flow ordinary differential equations (ODE) of diffusion under aligned data and noise, our training strategy is applicable to various diffusion forms and further enhances training efficiency. Comprehensive experimental evaluations validate the generality of our method, demonstrating 50% reduction in training cost and 1.5x improvement in inference efficiency. Our project page is: https://showlab.github.io/TPDiff/

<a id="p069"></a>
## P069 · VideoMind: A Chain-of-LoRA Agent for Temporal-Grounded Video Reasoning

- **作者**：Ye Liu; Kevin Qinghong Lin; Chang Wen Chen; Mike Zheng Shou
- **时间**：本地版本：2026-02-21（arXiv:2503.13444v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICLR 2026（PDF页眉）；arXiv:2503.13444v3
- **论文链接**：[arXiv本地版本 2503.13444v3](https://arxiv.org/abs/2503.13444v3)
- **项目／代码／数据**：[项目/演示页面](https://videomind.github.io/)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：26页；SHA-256：`7e5ba7dcd966c8bd72980a005b98027b8f67c0a05fb6f778f241a2a0bf09e666`

### 中文摘要

用规划、时刻定位、验证、回答四个角色进行带时间证据的视频问答，以共享骨干上的多个LoRA切换角色。

### 核心贡献

角色化视频推理与Chain-of-LoRA，兼顾专门训练能力与显存效率，评估15个基准。

### 实现边界

各角色有专门训练数据/优化，并非零训练工具链；定位证据不代表严格因果解释，尚未结合音频。

### Method／方法

planner决定需要何种角色，grounder提出时间段，verifier筛选，answerer基于片段回答；同一Qwen2-VL骨干动态加载角色LoRA。

### Results／主要结果

表7（2B）Chain-of-LoRA峰值显存4.2GB，对独立四模型16.6GB，性能相同；Video-MME总分55.4对基础53.0，长视频46.3对43.1；NExT-GQA准确率71.4对69.6、mIoU28.6。

### Shortcomings／局限与可能不足

【作者】角色与数据需精细优化，联合优化/音频待研究；【解读】多步定位验证仍增加延迟，收益跨基准不均匀。

### 证据定位

PDF §3–4、表7 p.9、结论局限。

### Abstract

Videos, with their unique temporal dimension, demand precise grounded understanding, where answers are directly linked to visual, interpretable evidence. Despite significant breakthroughs in text-based reasoning with large language models, multi-modal reasoning – especially for videos – remains limited. In this work, we fill this gap by introducingVideoMind, a novel video-language agent for temporal-grounded video reasoning. Our method involves two key innovations: (1) We identify four essential capabilities for grounded video reasoning and propose a role-based agentic workflow, comprising aplannerto coordinate roles, a grounderfor temporal event localization, averifierto assess event candidates, and ananswererfor question answering. (2) To efficiently integrate these roles during inference, we propose a novelChain-of-LoRAmechanism, where a unified base model with multiple LoRA adapters is leveraged to enable seamless role switching, balancing efficiency and flexibility. Extensive experiments on 15 benchmarks across Grounded VideoQA, Video Temporal Grounding, and General VideoQA tasks demonstrate the effectiveness of the proposed scheme in advancing video agent, test-time scaling, and long-form video reasoning. Code, models, datasets, and demos are available athttps://videomind.github.io/.

<a id="p070"></a>
## P070 · Impossible Videos

- **作者**：Zechen Bai; Hai Ci; Mike Zheng Shou
- **时间**：本地版本：2025-03-18（arXiv:2503.14378v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2503.14378v1，2025-03（本地版本）
- **论文链接**：[arXiv本地版本 2503.14378v1](https://arxiv.org/abs/2503.14378v1)
- **项目／代码／数据**：[项目/演示页面](https://showlab.github.io/Impossible-Videos/)

- **主题**：世界机制与演化
- **PDF版本**：26页；SHA-256：`5b6d3239d06f838dbbfd470e42f62eeea8a74a38479c99979b2fc1a3edf6918e`

### 中文摘要

构建违背物理、生物、地理或社会常识的视频生成/理解基准，检查模型能否遵循不可能情景提示并识别视频异常。

### 核心贡献

IPV-Bench分类体系（4域14类）、IPV-TXT生成提示与IPV-VID理解数据及综合生成指标。

### 实现边界

目标是按提示生成反现实内容，不能把高分解读为更准确模拟物理；“不可能”包括语境化社会/地理常识，非全是严格物理定律。

### Method／方法

按分类设计提示、收集筛选生成视频，对生成质量/提示跟随及Video-LLM异常理解做评测。

### Results／主要结果

所测生成模型最佳Mochi1仅37.3%情形生成高质量不可能视频；高视觉质量与异常提示跟随常不一致；视频理解模型仍难联合时间动态和世界知识识别异常。

### Shortcomings／局限与可能不足

【解读】人工分类、生成器分布和评判者影响结果；反现实题材不覆盖普通现实视频能力，模型排名仅对应本地版本评测。

### 证据定位

PDF §3–5，表2、§4.1 p.8。

### Abstract

Synthetic videos nowadays is widely used to complement data scarcity and diversity of realworld videos. Current synthetic datasets primarily replicate real-world scenarios, leaving impossible, counterfactual and anti-reality video concepts underexplored. This work aims to answer two questions: 1) Can today’s video generation models effectively follow prompts to create impossible video content? 2) Are today’s video understanding models good enough for understanding impossible videos? To this end, we introduce IPV-B ENCH , a novel benchmark designed to evaluate and foster progress in video understanding and generation. IPV-B ENCH is underpinned by a comprehensive taxonomy, encompassing 4 domains, 14 categories. It features diverse scenes that defy physical, biological, geographical, or social laws. Based on the taxonomy, a prompt suite is constructed to evaluate video generation models, challenging their prompt following and creativity capabilities. In addition, a video benchmark is curated to assess Video-LLMs on their ability of understanding impossible videos, which particularly requires reasoning on temporal dynamics and world knowledge. Comprehensive evaluations reveal limitations and insights for future directions of video models, paving the way for next-generation video models.

<a id="p071"></a>
## P071 · Counterfactual World Models via Digital Twin-conditioned Video Diffusion

- **作者**：Yiqing Shen; Aiza Maksutova; Chenjia Li; Mathias Unberath
- **时间**：本地版本：2025-11-21（arXiv:2511.17481v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2511.17481v1，2025-11（本地版本）；保留文件名中的CVPR未获本次充分核验，不作为正式发表记录。
- **论文链接**：[arXiv本地版本 2511.17481v1](https://arxiv.org/abs/2511.17481v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：14页；SHA-256：`7f7d56e5b755149cc609ad0acdf0b5e58ccdf160a388465ebd8c1f1b9d83044e`

### 中文摘要

把视频转为显式对象与关系的数字孪生描述，LLM修改干预后的时间演化，再条件生成反事实视频。

### 核心贡献

CWMDT将感知、干预传播和视频合成分开，提供可编辑结构条件。

### 实现边界

数字孪生为结构化文本/轨迹描述，不是经过物理验证的仿真器；LLM预测的反事实合理性不等于识别真实因果效应。

### Method／方法

提取场景摘要、对象帧描述、深度/面积/质心轨迹→LLM生成干预后的表示→视频扩散条件合成；每个干预采样3条孪生轨迹。

### Results／主要结果

在RVEBench及另一反事实视频基准报告优于比较方法；补充CausalVQA debug评估中Qwen2.5VL+CWMDT反事实准确率70.0%，比基础模型+17.5个百分点，anticipation62.5%、hypothetical72.5%。这些是小型debug集结果。

### Shortcomings／局限与可能不足

【解读】感知、结构化与LLM推断错误可逐级传播；小规模反事实QA不能证明真实部署或物理约束严格满足；生成成本和多候选选择影响效果。

### 证据定位

PDF §3–4 pp.3–8；附录A表4 p.10。

### Abstract

World models learn to predict the temporal evolution of visual observations given a control signal, potentially enabling agents to reason about environments through forward simulation. Because of the focus on forward simulation, current world models generate predictions based on factual observations. For many emerging applications, such as comprehensive evaluations of physical AI behavior under varying conditions, the ability of world models to answer counterfactual queries – such as “what would happen if this object was removed?” – is of increasing importance. We formalize counterfactual world models that additionally take interventions as explicit inputs, predicting temporal sequences under hypothetical modifications to observed scene properties. Traditional world models operate directly on entangled pixel-space representations where object properties and relationships cannot be selectively modified. This modeling choice prevents targeted interventions on specific scene properties. We introduce CWMDT, a framework to overcome those limitations, turning standard video diffusion models into effective counterfactual world models. First, CWMDT constructs digital twins of observed scenes to explicitly encode objects and their relationships, represented as structured text. Second, CWMDT applies large language models to reason over these representations and predict how a counterfactual intervention propagates through time to alter the observed scene. Third, CWMDT conditions a video diffusion model with the modified representation to generate counterfactual visual sequences. Evaluations on two benchmarks show that the CWMDT approach achieves state-of-the-art performance, suggesting that alternative representations of videos, such as the digital twins considered here, offer powerful control signals for video forward simulation-based world models.

<a id="p072"></a>
## P072 · Wan-Move: Motion-controllable Video Generation via Latent Trajectory Guidance

- **作者**：Ruihang Chu; Yefei He; Zhekai Chen; Shiwei Zhang; Xiaogang Xu; Bin Xia; Dingdong Wang; Hongwei Yi; Xihui Liu; Hengshuang Zhao; Yu Liu; Yingya Zhang; Yujiu Yang
- **时间**：本地版本：2025-12-09（arXiv:2512.08765v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2512.08765v1，2025-12（本地版本）
- **论文链接**：[arXiv本地版本 2512.08765v1](https://arxiv.org/abs/2512.08765v1)
- **项目／代码／数据**：[代码：ali-vilab/Wan-Move](https://github.com/ali-vilab/Wan-Move)

- **主题**：世界机制与演化
- **PDF版本**：22页；SHA-256：`d9a58b9d2755593daeac68fd1ff16c24e6acf21b605077b53c9a007c14d384d3`

### 中文摘要

用密集点轨迹移动首帧潜特征，直接作为图生视频条件，实现无需额外运动编码器的精细运动控制，并提出MoveBench。

### 核心贡献

latent trajectory guidance与运动控制评测集，保持Wan-I2V架构并进行规模化训练。

### 实现边界

无架构变化不等于无需训练；需要首帧及运动轨迹，主要展示5秒480p生成，不保证长期遮挡下的可控性。

### Method／方法

将点轨迹投影到VAE潜空间，沿轨迹复制首帧特征，形成时空条件图，对基础I2V模型微调。

### Results／主要结果

MoveBench/DAVIS上取得较低轨迹EPE和较高PSNR/SSIM；192个多物体样例继续评估；用户研究认为运动控制可与Kling1.5Pro Motion Brush相比，比较限定于所评设置。

### Shortcomings／局限与可能不足

【作者】长时间遮挡、轨迹缺失可使控制丢失；【解读】质量和控制受基础模型、轨迹准确性及训练分布限制，用户偏好不等同所有指标领先。

### 证据定位

PDF §3、§5表1–2、§6 p.10。

### Abstract

We present Wan-Move, a simple and scalable framework that brings motion control to video generative models. Existing motion-controllable methods typically suffer from coarse control granularity and limited scalability, leaving their outputs insufficient for practical use. We narrow this gap by achieving precise and high-quality motion control. Our core idea is to directly make the original condition features motion-aware for guiding video synthesis. To this end, we first represent object motions with dense point trajectories, allowing fine-grained control over the scene. We then project these trajectories into latent space and propagate the first frame’s features along each trajectory, producing an aligned spatiotemporal feature map that tells how each scene element should move. This feature map serves as the updated latent condition, which is naturally integrated into the off-the-shelf image-to-video model,e.g., Wan-I2V-14B, as motion guidance without any architecture change. It removes the need for auxiliary motion encoders and makes fine-tuning base models easily scalable. Through scaled training, Wan-Move generates 5-second, 480p videos whose motion controllability rivals Kling 1.5 Pro’s commercial Motion Brush, as indicated by user studies. To support comprehensive evaluation, we further design MoveBench, a rigorously curated benchmark featuring diverse content categories and hybrid-verified annotations. It is distinguished by larger data volume, longer video durations, and high-quality motion annotations. Extensive experiments on MoveBench and the public dataset consistently show Wan-Move’s superior motion quality. Code, models, and benchmark data are made available.

<a id="p073"></a>
## P073 · The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity

- **作者**：Parshin Shojaee; Iman Mirzadeh; Keivan Alizadeh; Maxwell Horton; Samy Bengio; Mehrdad Farajtabar
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：本地30页早期稿；2025-06发布，Apple官方项目页另标NeurIPS；后续版本不与本地结果混合。 [Apple研究页面](https://machinelearning.apple.com/research/illusion-of-thinking)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：30页；SHA-256：`cb4c72f922d3eb75d5fa10c371818027374bf8b592453fc569003a0dfff12a0d`

### 中文摘要

在可调复杂度的谜题中比较推理模型与普通LLM，分析准确率与思考token随复杂度变化的规律。

### 核心贡献

使用汉诺塔、棋子交换、过河及积木等可模拟验证任务，识别低、中、高复杂度的不同表现区间并检查推理轨迹。

### 实现边界

测量有限模型在给定提示、完整动作序列输出和预算下的谜题表现；不能据此证明模型完全没有推理能力，或所有未来架构存在同一不可逾越上限。

### Method／方法

调节任务规模、以模拟器验证逐步动作，每实例25次采样；匹配推理预算比较pass@k，分析解答出现位置及token使用。

### Results／主要结果

低复杂度普通模型常较有效，中复杂度推理模型占优，高复杂度二者可降至0；临界复杂度附近思考token反而下降，即使仍有预算；给出算法也未稳定解决精确执行。

### Shortcomings／局限与可能不足

【作者】谜题领域窄、主要黑箱API、确定性逐步验证难推广；【解读】输出长度、任务可解性/表示和执行协议均影响阈值，不能把经验失败解释为普遍理论结论。

### 证据定位

PDF §4、图4–8、§5及Limitations p.11。

### Abstract

Recent generations of frontier language models have introduced Large Reasoning Models (LRMs) that generate detailed thinking processes before providing answers. While these models demonstrate improved performance on reasoning benchmarks, their fundamental capabilities, scaling properties, and limitations remain insufficiently understood. Current evaluations primarily focus on established mathematical and coding benchmarks, emphasizing final answer accuracy. However, this evaluation paradigm often suffers from data contamination and does not provide insights into the reasoning traces’ structure and quality. In this work, we systematically investigate these gaps with the help of controllable puzzle environments that allow precise manipulation of compositional complexity while maintaining consistent logical structures. This setup enables the analysis of not only final answers but also the internal reasoning traces, offering insights into how LRMs “think”. Through extensive experimentation across diverse puzzles, we show that frontier LRMs face a complete accuracy collapse beyond certain complexities. Moreover, they exhibit a counterintuitive scaling limit: their reasoning effort increases with problem complexity up to a point, then declines despite having an adequate token budget. By comparing LRMs with their standard LLM counterparts under equivalent inference compute, we identify three performance regimes: (1) lowcomplexity tasks where standard models surprisingly outperform LRMs, (2) medium-complexity tasks where additional thinking in LRMs demonstrates advantage, and (3) high-complexity tasks where both models experience complete collapse. We found that LRMs have limitations in exact computation: they fail to use explicit algorithms and reason inconsistently across puzzles. We also investigate the reasoning traces in more depth, studying the patterns of explored solutions and analyzing the models’ computational behavior, shedding light on their strengths, limitations, and ultimately raising crucial questions about their true reasoning capabilities.

<a id="p074"></a>
## P074 · Beyond Single-Sentence Prompts: Upgrading Value Alignment Benchmarks with Dialogues and Stories

- **作者**：Yazhou Zhang; Qimeng Liu; Qiuchi Li; Peng Zhang; Jing Qin
- **时间**：本地版本：2025-03-28（arXiv:2503.22115v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint, Under review；arXiv:2503.22115，2025-03-28。 [arXiv记录](https://arxiv.org/abs/2503.22115)
- **论文链接**：[arXiv本地版本 2503.22115v1](https://arxiv.org/abs/2503.22115v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：24页；SHA-256：`f87a1db46bf43589966d1bf5fd3334cc597bee27afaab611b70859c0073e3b08`

### 中文摘要

把单句中文价值观评测改写成多轮对话与伦理故事，检验更复杂上下文中的价值对齐与责任判断。

### 核心贡献

基于CVALUES构建C-Plus Values/CVALUES PLUS数据及分层评估框架，暴露单轮直接问题不易发现的失误。

### 实现边界

中文语境和定义的伦理评分；分数并非客观普世道德质量，也不等于已改善模型安全性。

### Method／方法

自动/人工清洗原始问题，生成对话陷阱与故事，组合人工和自动评分，比较不同模型在对话/叙事场景的表现。

### Results／主要结果

本地报告Claude3.5对话得分83.7、故事65.3；许多模型在故事任务下降，但各模型并非一致，Llama3.1-405B对话49.4、故事55.2。

### Shortcomings／局限与可能不足

【作者】文化和场景覆盖有限，评分主观，复杂伦理标准难统一；【解读】合成改写及自动评判可能引入系统偏差。

### 证据定位

PDF §2–5，§5.2–3 p.13、Limitations p.15。

### Abstract

Evaluating the value alignment of large language models (LLMs) has traditionally relied on single-sentence adversarial prompts, which directly probe models with ethically sensitive or controversial questions. However, with the rapid advancements in AI safety techniques, models have become increasingly adept at circumventing these straightforward tests, limiting their effectiveness in revealing underlying biases and ethical stances. To address this limitation, we propose an upgraded value alignment benchmark that moves beyond single-sentence prompts by incorporating multi-turn dialogues and narrative-based scenarios. This approach enhances the stealth and adversarial nature of the evaluation, making it more robust against superficial safeguards implemented in modern LLMs. We design and implement a dataset that includes conversational traps and ethically ambiguous storytelling, systematically assessing LLMs’ responses in more nuanced and context-rich settings. Experimental results demonstrate that this enhanced methodology can effectively expose latent biases that remain undetected in traditional single-shot evaluations. Our findings highlight the necessity of contextual and dynamic testing for value alignment in LLMs, paving the way for more sophisticated and realistic assessments of AI ethics and safety.

<a id="p075"></a>
## P075 · Chain-of-Evidence Multimodal Reasoning for Few-shot Temporal Action Localization

- **作者**：Mengshi Qi; Hongwei Ji; Wulian Yun; Xianlin Zhang; Huadong Ma
- **时间**：本地版本：2025-12-25（arXiv:2504.13460v5）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：IEEE Transactions on Image Processing（PDF页眉）；arXiv:2504.13460v5，具体卷期/正式出版日未在本地明确
- **论文链接**：[arXiv本地版本 2504.13460v5](https://arxiv.org/abs/2504.13460v5)
- **项目／代码／数据**：[代码：MICLAB-BUPT/VAL-VLM](https://github.com/MICLAB-BUPT/VAL-VLM)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：22页；SHA-256：`b7cc35891863b534350013194741c2b2bdb2484992030b98ef52a200fee69b5c`

### 中文摘要

将视频与由VLM/LLM生成的Chain-of-Evidence文本结合，在少样本条件下定位未见动作类别的时间范围。

### 核心贡献

层次文本—视觉对齐、逐阶段证据链生成和Human-related Anomaly Localization（HAL）数据集。

### 实现边界

few-shot针对新动作类别，基础VLM/LLM和特征器已有预训练；文本生成后有自动过滤、一致性校验、迭代及人工审核，不是无需人工的通用因果定位。

### Method／方法

从视频产生事件证据描述，逐层精化时间/动作关系；对齐query/support视觉及语义特征，联合建模动作共同性与差异。

### Results／主要结果

ActivityNet1.3单实例1-shot mAP@0.5=71.5，多实例5-shot=58.7；在THUMOS14多实例设置改善，但单实例1-shot下降，作者归因于短且不完整动作片段妨碍完整CoE生成。

### Shortcomings／局限与可能不足

【作者/解读】依赖生成文本质量、验证成本和完整动作语境；HAL及少样本划分的提升不能直接外推到开放世界长视频；证据链提及因果关系并不构成因果识别。

### 证据定位

PDF §III–IV、表I/III、图6 pp.6–8。

### Abstract

Traditional temporal action localization (TAL) methods rely on large amounts of detailed annotated data, whereas few-shot TAL reduces this dependence by using only a few training samples to identify unseen action categories. However, existing few-shot TAL methods typically focus solely on video-level information, neglecting textual information, which can provide valuable semantic support for the action localization task. To address these issues, in this work, we propose a new few-shot temporal action localization method by Chain-of-Evidence multimodal reasoning to improve localization performance. Specifically, we design a novel few-shot learning framework to capture action commonalities and variations, which includes a semantic-aware text-visual alignment module designed to align the query and support videos at different levels. Meanwhile, to better express the temporal dependencies and causal relationships between actions at the textual level, we design a Chain-of-Evidence (CoE) reasoning method that progressively guides the Vision Language Model (VLM) and Large Language Model (LLM) to generate CoE text descriptions for videos. The generated texts can capture more variance of action than visual features. We conduct extensive experiments on the publicly available ActivityNet1.3, THUMOS14 and our newly collected Human-related Anomaly Localization Dataset . The experimental results demonstrate that our proposed method significantly outperforms existing methods in single-instance and multi-instance scenarios. Our source code and data are available at https://github.com/MICLAB-BUPT/VAL-VLM.

<a id="p076"></a>
## P076 · Interactive Reasoning: Visualizing and Controlling Chain-of-Thought Reasoning in Large Language Models

- **作者**：Rock Yuren Pang; K. J. Kevin Feng; Shangbin Feng; Chu Li; Weijia Shi; Yulia Tsvetkov; Jeffrey Heer; Katharina Reinecke
- **时间**：本地版本：2025-06-30（arXiv:2506.23678v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2506.23678v1，2025-06-30（本地版本）
- **论文链接**：[arXiv本地版本 2506.23678v1](https://arxiv.org/abs/2506.23678v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：15页；SHA-256：`f659a7c8bfc4836d0491888233347daea905380b2a73283dc5f7305cfd0ce316`

### 中文摘要

Hippo将长推理文本组织成可交互的主题树，允许用户删除、添加、修改假设并重新生成，支持有权衡的日常决策。

### 核心贡献

提出Interactive Reasoning界面与原型，展示在输出最终答案前介入推理内容的人机协作。

### 实现边界

可视化的是生成的CoT及其整理结果，不是模型真实内部计算图；作者明确没有声称反馈使推理或答案更准确/更个性化。

### Method／方法

DeepSeek-R1生成推理，GPT-4o负责整理树、澄清和连接节点；反馈节点/直接编辑后续写；16人被试内比较。

### Results／主要结果

感知控制评分Hippo5.75对基线4.19，p=.003；用户报告更易理解结构和察觉假设，观察到更有针对性的反馈；没有客观准确率提升结论。

### Shortcomings／局限与可能不足

【作者】N=16且较熟悉LLM，两项日常两难任务；没有系统验证反馈后的模型行为或CoT忠实性，知识密集任务需外部证据。

### 证据定位

PDF §4.3、§5.3、§8 p.11。

### Abstract

The output quality of large language models (LLMs) can be improved via “reasoning”: generating segments of chain-of-thought (CoT) content to further condition the model prior to producing user-facing output. While these chains contain valuable information, they are verbose and lack explicit organization, making them tedious to review. Moreover, they lack opportunities for user feedback, such as to remove unwanted considerations, add desired ones, or clarify unclear assumptions. We introduce Interactive Reasoning, an interaction design that visualizes chain-of-thought outputs as a hierarchy of topics and enables user review and modification. We implement interactive reasoning in Hippo, a prototype for AIassisted decision making in the face of uncertain trade-offs. In a user study with 16 participants, we find that interactive reasoning in Hippo allows users to quickly identify and interrupt erroneous generations, efficiently steer the model towards customized responses, and better understand both model reasoning and model outputs. Our work contributes to a new paradigm that incorporates user oversight into LLM reasoning processes.

<a id="p077"></a>
## P077 · Is Chain-of-Thought Reasoning of LLMs a Mirage? A Data Distribution Lens

- **作者**：Chengshuai Zhao; Zhen Tan; Pingchuan Ma; Dawei Li; Bohan Jiang; Yancheng Wang; Yingzhen Yang; Huan Liu
- **时间**：本地版本：2026-05-08（arXiv:2508.01191v6）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2508.01191v6（本地版本）
- **论文链接**：[arXiv本地版本 2508.01191v6](https://arxiv.org/abs/2508.01191v6)
- **项目／代码／数据**：[代码：ChengshuaiZhao0/DataAlchemy](https://github.com/ChengshuaiZhao0/DataAlchemy)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：38页；SHA-256：`a039bae82027a21ab7d38f00228c4d1e549f5b543ad1ad172b9b6c656cf05c6f`

### 中文摘要

以可控合成环境研究CoT在训练与测试分布的任务、长度和格式差异下何时失败，解释推理链与最终答案可能不一致。

### 核心贡献

DataAlchemy精确控制分布偏移，分离推理过程、答案与完整链正确性，检验由训练分布形成的归纳偏置。

### 实现边界

合成符号转化任务中的受控证据，不是证明所有自然语言推理仅为记忆；大模型训练语料不透明。

### Method／方法

控制训练变换组合、链长度和表达格式，训练/微调多架构规模模型并对比ID、组合迁移和OOD；分别评估链与答案exact match。

### Results／主要结果

指定变换实验中完整链ID100%，CMP0.01%、POOD/OOD0%；可出现推理100%但答案0.01%，或推理0%但答案100%的分离。数值只适用于该受控任务。

### Shortcomings／局限与可能不足

【作者】合成环境无法覆盖自然语言丰富性，真实预训练分布难度量；【解读】特定分布外失败支持脆弱性，不能直接推出不存在任何系统泛化能力。

### 证据定位

PDF §3–8、表1–2 p.7、Limitations p.11。

### Abstract

Chain-of-Thought (CoT) prompting has been shown to be effective in eliciting structured reasoning (i.e., CoT reasoning) from large language models (LLMs). Regardless of its popularity, recent studies expose its failures in some reasoning tasks, raising fundamental questions about the nature of CoT reasoning. In this work, we propose a data distribution lens to understand when and why CoT reasoning succeeds or fails. We hypothesize that CoT reasoning reflects a structured inductive bias learned from in-distribution data, enabling models to conditionally generate reasoning trajectories that approximate those observed during training. As such, the effectiveness of CoT reasoning is fundamentally governed by the nature and degree of distribution discrepancy between training data and test queries. Guided by this lens, we dissect CoT reasoning via three dimensions:task,length, andformat. To test the hypothesis, we introduceDataAlchemy, an abstract and fully controllable environment that trains LLMs from scratch and systematically probes them under various distribution conditions. Through rigorous controlled experiments, we reveal that CoT reasoning is a brittle mirage when it is pushed beyond training distributions, emphasizing the ongoing challenge of achieving genuine and generalizable reasoning. Our code is available at GitHub: https://github.com/ChengshuaiZhao0/DataAlchemy.

<a id="p078"></a>
## P078 · Seeing but Not Believing: Probing the Disconnect Between Visual Attention and Answer Correctness in VLMs

- **作者**：Zhining Liu; Ziyi Chen; Hui Liu; Chen Luo; Xianfeng Tang; Suhang Wang; Joy Zeng; Zhenwei Dai; Zhan Shi; Tianxin Wei; Benoit Dumoulin; Hanghang Tong
- **时间**：本地版本：2025-10-20（arXiv:2510.17771v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint, Under Review；arXiv:2510.17771v1
- **论文链接**：[arXiv本地版本 2510.17771v1](https://arxiv.org/abs/2510.17771v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：21页；SHA-256：`b8bec5569aa162e20a84ec3ff8ad4d9f9b33d37157fed6b7feadd35bd121ea22`

### 中文摘要

分析视觉注意力与答对之间的分离，发现模型错误回答时也可能关注正确证据，提出测试时视觉证据增强VEA。

### 核心贡献

层间注意力诊断与按深层注意力选择/突出证据区域的无需训练干预。

### 实现边界

“看到”用注意力定位代理衡量，不等于模型完整理解或证据对答案有因果作用；需要开放权重/注意力访问。

### Method／方法

定位视觉grounding层，提取证据分数，选择性遮罩/突出图像区域后重推理；跨4个系列8个VLM比较。

### Results／主要结果

表1平均Exact Match+5.67个百分点（最高11.1），Token F1+6.83（最高17.3）；跨LLaVA、Qwen、Gemma、InternVL收益较一致，小模型收益更大。

### Shortcomings／局限与可能不足

【解读】关注区域也可能错误，遮罩会丢失上下文；额外推理成本及架构依赖，本文定位为诊断与干预研究而非部署完备系统。

### 证据定位

PDF §3–4、表1–2、§6。

### Abstract

Vision-Language Models (VLMs) achieve strong results on multimodal tasks such as visual question answering, yet they can still fail even when the correct visual evidence is present. In this work, we systematically investigate whether these failures arise from notperceivingthe evidence or from notleveragingit effectively. By examining layer-wise attention dynamics, we find that shallow layers focus primarily on text, while deeper layers sparsely but reliably attend to localized evidence regions. Surprisingly, VLMs often perceive the visual evidence when outputting incorrect answers, a phenomenon we term“seeing but not believing” that widely exists in major VLM families. Building on this, we introduce an inference-time intervention that highlights deep-layer evidence regions through selective attention-based masking. It requires no training and consistently improves accuracy across multiple families, including LLaV A, Qwen, Gemma, and InternVL. These results show that VLMs encode reliable evidence internally but underutilize it, making such signals explicit can bridge the gap between perception and reasoning, advancing the diagnostic understanding and reliability of VLMs.

<a id="p079"></a>
## P079 · Thinking in 360°: Humanoid Visual Search in the Wild

- **作者**：Heyang Yu; Yinan Han; Xiangyu Zhang; Baiqiao Yin; Bowen Chang; Xiangyu Han; Xinhao Liu; Jing Zhang; Marco Pavone; Chen Feng; Saining Xie; Yiming Li
- **时间**：本地版本：2025-11-26（arXiv:2511.20351v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2511.20351v2（本地版本）
- **论文链接**：[arXiv本地版本 2511.20351v2](https://arxiv.org/abs/2511.20351v2)
- **项目／代码／数据**：[项目/演示页面](https://humanoid-vstar.github.io)

- **主题**：XR与人机协作
- **PDF版本**：23页；SHA-256：`864de2cd0e517e00859e476929d6b7381cda259798222181b6e00f4b44c92e02`

### 中文摘要

在360°全景中通过头部转动主动寻找目标物体或路径，构建公共复杂环境H*Bench并训练视觉搜索代理。

### 核心贡献

对象搜索HOS/路径搜索HPS任务、全景感知—动作闭环与SFT+RL训练。

### 实现边界

环境由单张全景表示，主要动作是头部视角旋转/对准；没有真实行走、避障、动态环境或完整机器人部署验证。

### Method／方法

从全景渲染当前视角，根据图像/历史选择头部动作；Qwen2.5-VL-3B全参数SFT后RL优化搜索成功。

### Results／主要结果

对象搜索14.83%→47.38%，路径6.44%→24.94%；Gemini2.5Pro基线HOS31.96%、HPS33.00%，故训练模型并非在路径上超过最佳闭源模型。

### Shortcomings／局限与可能不足

【作者/解读】物理/社会空间常识和视觉—动作转化困难；静态全景不含真实移动、视差和传感误差，路径任务仍远未解决。

### 证据定位

PDF §3–4、表1与训练结果、图5。

### Abstract

Humans rely on the synergistic control of head (cephalomotor) and eye (oculomotor) to efficiently search for visual information in 360°. However, prior approaches to visual search are limited to a static image, neglecting the physical embodiment and its interaction with the 3D world. How can we develop embodied visual search agents as efficient as humans while bypassing the constraints imposed by realworld hardware? To this end, we proposehumanoid visual searchwhere a humanoid agent actively rotates its head to search forobjectsorpathsin an immersive world represented by a 360° panoramic image. To study visual search in visually-crowded real-world scenarios, we build H∗Bench, a new benchmark that moves beyond household scenes to challenging in-the-wild scenes that necessitate advanced visual-spatial reasoning capabilities, such as transportation hubs, large-scale retail spaces, urban streets, and public institutions. Our experiments first reveal that even top-tier proprietary models falter, achieving only∼30% success in object and path search. We then use post-training techniques to enhance the open-source Qwen2.5-VL, increasing its success rate by overthreefoldfor both object search (14.83%→47.38%) and path search (6.44%→ 24.94%). Notably, the lower ceiling of path search reveals its inherent difficulty, which we attribute to the demand for sophisticated spatial commonsense. Our results not only show a promising path forward but also quantify the immense challenge that remains in building MLLM agents that can be seamlessly integrated into everyday human life.

<a id="p080"></a>
## P080 · Vis-CoT: A Human-in-the-Loop Framework for Interactive Visualization and Intervention in LLM Chain-of-Thought Reasoning

- **作者**：Kaviraj Pather; Elena Hadjigeorgiou; Arben Krasniqi; Claire Schmit; Irina Rusu; Marc Pons; Kabir Khan
- **时间**：本地版本：2025-12-29（arXiv:2509.01412v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2509.01412v2（本地预印本）
- **论文链接**：[arXiv本地版本 2509.01412v2](https://arxiv.org/abs/2509.01412v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：10页；SHA-256：`7ac33fd5fafb7173409dd79467e23080aeebc87bb5f9a9874e66c02df4d9ec78`

### 中文摘要

将线性CoT转换成交互图，由用户标记、剪除错误分支并补充前提，再继续生成，报告人机协作正确率和体验提升。

### 核心贡献

Vis-CoT图结构、pruning/grafting干预流程与用户研究。

### 实现边界

结果包含用户新增知识和纠错，不是Llama2-70B独立解题能力；图是CoT的结构化展示，不保证忠实反映内部推理。

### Method／方法

Llama2-70B-Chat、React/D3界面与FastAPI，24名相关专业参与者；GSM8K/StrategyQA及100项自建规划任务，人工评价部分任务的答案与有效推理链。

### Results／主要结果

作者报告CoT→Vis-CoT：GSM8K74.8→91.7%，StrategyQA79.5→94.1%，规划68→92%；平均时间410.5→285.2秒，2.1次干预/题；SUS65.5→88.2。

### Shortcomings／局限与可能不足

【解读】正文对全测试集评测与24人用户实验的样本分配、统计不确定性及复现材料交代有限，数值应作作者报告；参与者有专业背景，需独立复现及更广泛人群验证。

### 证据定位

PDF pp.6–8，算法1、实验设置、表I–III。

### Abstract

Large Language Models (LLMs) have demonstrated remarkable reasoning capabilities through Chain-of-Thought (CoT) prompting. However, the underlying reasoning process remains an opaque ”black box,” making it difficult to verify, debug, or control, which limits trust and reliability in highstakes applications. To address this critical gap, we introduce Vis-CoT, a novel human-in-the-loop framework that transforms the linear CoT text into a structured, interactive reasoning graph. Our system allows users to visualize the logical flow of the model’s reasoning, identify flawed steps, and directly intervene by pruning incorrect paths and grafting new, user-defined premises. This transforms the interaction from a passive observation to an active collaboration, enabling users to steer the model toward more accurate and trustworthy conclusions. Through comprehensive experiments on diverse reasoning benchmarks, including GSM8K and StrategyQA, we demonstrate that Vis- CoT significantly improves final answer accuracy by up to 24 percentage points over non-interactive baselines. Furthermore, our user study reveals a substantial increase in perceived usability and user trust, underscoring the value of transparency and control. Our work presents a promising paradigm for creating more reliable, understandable, and collaborative reasoning systems by synergizing the computational power of LLMs with human critical oversight.

<a id="p081"></a>
## P081 · Olaf-World: Orienting Latent Actions for Video World Modeling

- **作者**：Yuxin Jiang; Yuchao Gu; Ivor W. Tsang; Mike Zheng Shou
- **时间**：本地版本：2026-05-26（arXiv:2602.10104v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICML 2026，PMLR306（PDF首页）；arXiv:2602.10104v2
- **论文链接**：[arXiv本地版本 2602.10104v2](https://arxiv.org/abs/2602.10104v2)
- **项目／代码／数据**：[项目/演示页面](https://showlab.github.io/Olaf-World)
- **版本关系**：[P082](#p082)与本文件SHA-256完全一致，共用此总结。

- **主题**：世界机制与演化
- **PDF版本**：18页；SHA-256：`f108f25fdbcf882621692aef27c19b0b06a75a4405abffef226cbe130019e983`

### 中文摘要

针对无标签视频中潜动作与场景纠缠的问题，用冻结视频表征的时间变化为潜动作提供跨场景共享语义参考，训练可迁移世界模型。

### 核心贡献

SeqΔ-REPA序列控制效果对齐与Olaf-World预训练/控制适配流水线。

### 实现边界

潜动作是从视频变化学习的控制表示，非保证唯一可识别真实动作；“1分钟”是特定新控制空间的少量标注适配，不是完整机器人任务训练时间。

### Method／方法

β-VAE逆/前向动力学学习潜动作；累计动作表征对齐冻结自监督视频编码器特征差；训练潜动作条件视频生成并适配新控制接口。

### Results／主要结果

第一/第三人称跨域动作线性探测和动作原型一致性优于AdaWorld；展示零样本动作转移、新场景生成及少标注适配收益。

### Shortcomings／局限与可能不足

【作者/解读】依赖视频编码器捕捉动作效果，视角/外观变化仍可混入；跨人到机器人等具身迁移列为未来工作，未建立普遍因果可识别性。

### 证据定位

PDF §3–4、图4–5、§5及附录E。

### Abstract

Scaling action-controllable world models is limited by the scarcity of action labels. While latent action learning promises to extract control interfaces from unlabeled video, learned latents often fail to transfer across contexts: they entangle scene-specific cues and lack a shared coordinate system. This occurs because standard objectives operate onlywithineach clip, providing no mechanism to align action semantics across contexts. Our key insight is that although actions are unobserved, theirsemantic effectsare observable and can serve as a shared reference. We introduceSeq ∆-REPA, a sequence-level controleffect alignment objective that anchors integrated latent action to temporal feature differences from a frozen, self-supervised video encoder. Building on this, we presentOlaf-World, a pipeline that pretrains action-conditioned video world models from large-scale passive video. Extensive experiments demonstrate that our method learns a more structured latent action space, leading to stronger zero-shot action transfer and more data-efficient adaptation to new control interfaces than state-ofthe-art baselines.

<a id="p083"></a>
## P083 · Causal-JEPA: Learning World Models through Object-Level Latent Masking

- **作者**：Heejeong Nam; Quentin Le Lidec; Lucas Maes; Yann LeCun; Randall Balestriero
- **时间**：本地版本：2026-05-28（arXiv:2602.11389v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2602.11389v2（本地版本）
- **论文链接**：[arXiv本地版本 2602.11389v2](https://arxiv.org/abs/2602.11389v2)
- **项目／代码／数据**：[代码：galilai-group/cjepa](https://github.com/galilai-group/cjepa)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：25页；SHA-256：`956e136d92c4c944a53e3c2d9cd826aebc96b06af542cd767a0a213e47fb609b`

### 中文摘要

将JEPA掩码预测从图像patch移到对象潜变量，通过遮住部分对象迫使模型利用交互关系，改善反事实问答与规划效率。

### 核心贡献

C-JEPA对象级潜掩码学习目标与可观测性理论分析，区分仅对象表示和对象掩码的作用。

### 实现边界

object masking是“counterfactual-like”预测，不直接等同do干预；没有用显式时间因果图验证影响邻域。

### Method／方法

对象编码器产生slots，预测被遮对象的历史/未来潜状态，避免像素重建；基于紧凑潜模型规划控制。

### Results／主要结果

表2 SAVi骨干反事实按问题准确率60.19%，无对象掩码OC-JEPA41.10%（+19.09个百分点），总体83.88对77.28%；控制任务用约patch模型1%的潜输入特征达到可比结果。

### Shortcomings／局限与可能不足

【作者】对象编码器质量限制上限、过度掩码会丢失有效依赖、缺乏真实因果图验证；【解读】简化对象环境和所评控制任务限制现实外推。

### 证据定位

PDF §4–6、表2 p.6、§7 p.9。

### Abstract

World models require robust relational understanding to support prediction, reasoning, and control. While object-centric representations provide a useful abstraction, they are not sufficient to capture interaction-dependent dynamics. We therefore propose C-JEPA, a simple and flexible objectcentric world model that extends masked joint embedding prediction from image patches to objectcentric representations. By masking object-level latents and requiring each masked object state to be inferred from the surrounding context, C- JEPA imposes structured partial observability during training, creating counterfactual-like prediction queries that discourage shortcut solutions and make interaction-dependent prediction necessary under the learning objective. Empirically, C-JEPA leads to consistent gains in visual question answering, with an absolute improvement of about 20% in counterfactual reasoning over the same architecture without object-level masking. On agent control tasks, C-JEPA enables substantially more efficient planning by using only 1% of the total latent input features required by patch-based world models, while achieving comparable performance. Finally, we provide a formal analysis demonstrating that object-level masking induces useful inductive bias by controlling observability. Our code is available at https://github.com/galilai-group/cjepa.

<a id="p084"></a>
## P084 · CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models

- **作者**：León Begiristain; Olaf Dünkel; Adam Kortylewski
- **时间**：本地版本：2026-05-22（arXiv:2605.23699v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2605.23699v1，2026-05（本地版本）
- **论文链接**：[arXiv本地版本 2605.23699v1](https://arxiv.org/abs/2605.23699v1)
- **项目／代码／数据**：[项目/演示页面](https://genintel.github.io/CRONOS/)

- **主题**：世界机制与演化
- **PDF版本**：27页；SHA-256：`c2a65989b5dce1061ecdafc430424d43a388220cfd38a6c9f5721e5ab8678137`

### 中文摘要

在Unreal Engine中保持物理事件类别并系统改变视角、场景、对象类别和外观，测量视频世界模型预测是否稳定符合物理。

### 核心贡献

可匹配干预的CRONOS基准与经人评校验的物体稳定/物理合理性指标。

### 实现边界

主要衡量视觉条件变化下的物理一致性，非现实因果效应估计；I2V首帧无法唯一确定未来，采用best-of-three缓解而未完全解决。

### Method／方法

生成碰撞、跌落、遮挡等受控视频；比较Cosmos2.5、CogVideoX1.5、MAGI1、Wan2.2；部分支持5帧V2V；结合规则、视觉模型和VLM评判。

### Results／主要结果

所评最强模型成功率仍仅22%；视角变化尤其破坏结果；报告的多种得分从3次采样中按参考运动相似度挑选，不能作单次成功率理解。

### Shortcomings／局限与可能不足

【作者】合成—真实域差、单参考未来、仅开放模型；【解读】评判模型误差和选优协议影响绝对分数。

### 证据定位

PDF §3–4、§4.1 p.6、§5 p.9。

### Abstract

Video prediction is increasingly viewed as a path toward generalizable world models, yet it remains unclear whether these systems learn underlying causal structure or merely exploit superficial visual correlations for future prediction. We introduce CRONOS, an intervention-based benchmark designed to evaluate counterfactual physical consistency: whether a model’s predictions of physical events respond appropriately to controlled changes in the visual input, such as variations of scene context, viewpoint, object appearance, and object category. Built in a photorealistic Unreal Engine environment, CRONOS enables controlled, high-fidelity generation of videos across diverse scenes and dynamics. In contrast to previous benchmarks, CRONOS systematically intervenes on four key factors — viewpoint, scene, object category, and object appearance — while keeping the underlying physical event type, such as a collision, occlusion, or fall, fixed. Our evaluation of recent open-source video generators reveals substantial failures in counterfactual physical consistency: prediction quality for the same physical event type is affected by appearance, environment, and, particularly by viewpoint changes. CRONOS provides a controlled and reproducible testbed for diagnosing how the quality of generated videos changes for different interventions, establishing a concrete target for developing models that perform consistently across changes of multiple conditions. The dataset and code are available at: https://genintel.github.io/CRONOS/.

<a id="p085"></a>
## P085 · SolarWM: Open Data and Scalable Training for Long-Horizon Video World Models

- **作者**：Junchao Huang; Guian Fang; Shengju Qian; Xianghao Kong; Zhuoran Zhao; Wei Huang; Yihua Du; Zixin Zhang; Justin Cui; Yuchao Gu; Yukang Chen; Xinting Hu; Tianyu He; Shaoshuai Shi; Zhuotao Tian; Xin Wang; Mike Zheng Shou; Li Jiang
- **时间**：本地版本：2026-09-02（arXiv:2609.02886v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：2026-09技术报告；arXiv:2609.02886v1
- **论文链接**：[arXiv本地版本 2609.02886v1](https://arxiv.org/abs/2609.02886v1)
- **项目／代码／数据**：[项目/演示页面](https://junchao-cs.github.io/SolarWM-Web/)；[代码：Junchao-cs/SolarWM/tree/main](https://github.com/Junchao-cs/SolarWM/tree/main)；[数据/模型：datasets/junchaoh-cs/SolarWM-Data](https://huggingface.co/datasets/junchaoh-cs/SolarWM-Data)

- **主题**：世界机制与演化
- **PDF版本**：26页；SHA-256：`b11f376c90bdd340cfe8f64953858ffa142ddee989d8b5bfc237400650418115`

### 中文摘要

统一多源视频、相机几何、字幕和质量记录，跨视频骨干实施三阶段训练，支持相机可控的长时自回归视频生成。

### 核心贡献

10数据源143万canonical clips的数据引擎、可重配筛选与混合配方、四种5B–33B标称骨干的统一适配/蒸馏框架。

### 实现边界

长时展示主要为5B-fast学生；固定场景文本、预定相机轨迹是控制条件，不是任意任务代理或经过验证的物理仿真；发布矩阵含作者承诺，未逐项验证下载。

### Method／方法

对齐帧、度量相机几何、字幕和来源；双向适配→teacher-forced自回归初始化/AnyFlow→分布匹配蒸馏；保留各骨干原生表征。

### Results／主要结果

报告16fps、4步采样，5秒片段训练后连续生成分钟/60分钟序列；§7主要以图6–11定性展示跨域、相机跟随和长时外观保持，缺少统一量化长时物理/记忆基准，不能将小时端点示例解读为所有帧一致性保证。

### Shortcomings／局限与可能不足

【解读】长时证据为抽样可视化和有限轨迹；相机控制不同于对象交互，训练数据清洗/几何误差及来源分布可影响泛化；实时性依赖硬件和模型配置。

### 证据定位

PDF §4–6、表1/4/5；§7 pp.15–20、图10–11。

### Abstract

We introduce SolarWM, a fully open foundation for building interactive video world models from data preparation through long-horizon inference. Training across heterogeneous data sources and video backbones is challenging: datasets differ in temporal scale, camera geometry, visual quality, motion, and captioning styles, while video generators use distinct representations and architectures. Naive data mixing and model-specific implementations therefore produce inconsistent supervision and make results difficult to reproduce and compare. SolarWM addresses this coupling with a reconfigurable multi-source data engine and a backbone-native adaptation framework. The engine converts 1.43 million canonical clips from 10 datasets into a unified, frame-aligned contract covering visual observations, metric camera geometry, captions, quality metadata, selection decisions, and provenance, while decoupling source processing from mixture construction. Under shared camera-conditioning, training, and inference interfaces, we instantiate four 5B–33B models based on Wan2.2, LTX-2.5, and MiniMax-H3 while preserving their native representations and objectives. A unified three-stage recipe combines bidirectional adaptation, teacherforced autoregressive initialization, and distribution matching distillation. The resulting causal models enable real-time interaction over rollouts ranging from minutes to hours after being trained on only 5s sequences. By releasing the resulting data, pipeline, recipes, weights, and framework, SolarWM provides a reproducible and extensible foundation for interactive world-model research. Website (Dataset &amp; Code &amp; Model):https://junchao-cs.github.io/SolarWM-Web/

<a id="p086"></a>
## P086 · See It, Say It, Sorted: An Iterative Training-Free Framework for Visually-Grounded Multimodal Reasoning in LVLMs

- **作者**：Yongchang Zhang; Oliver Ma; Tianyi Liu; Guangquan Zhou; Yang Chen
- **时间**：本地版本：2026-03-07（arXiv:2602.21497v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2602.21497v2（本地版本）
- **论文链接**：[arXiv本地版本 2602.21497v2](https://arxiv.org/abs/2602.21497v2)
- **项目／代码／数据**：[代码：uuuuZYC/See-It-Say-It-Sorted](https://github.com/uuuuZYC/See-It-Say-It-Sorted)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：10页；SHA-256：`f0cf8bcf783bce9a16ed1d4e2b2f7637ef9fb33b402e6646d2012dee7de1f46c`

### 中文摘要

ECRD在推理过程中维护文字视觉证据池，将基础生成概率与证据引导分布结合，不足时再次观察图片补充证据。

### 核心贡献

无需训练的证据条件解码与动态visual decider，尝试抑制推理中视觉幻觉传播。

### 实现边界

需要访问token概率并多次视觉查询；证据池来自模型描述，不是已验证真值，“每个token有视觉依据”是设计目标而非形式保证。

### Method／方法

改进VDGD的候选词和KL证据偏好，融合基础置信度，按当前上下文决定是否追加图像证据并继续解码。

### Results／主要结果

TreeBench Qwen2.5VL-7B总体37.0→47.9（+10.9个百分点，约29.5%相对提升）；32B42.5→48.6、72B42.2→49.9。摘要16.5–29.5%不应全部写成百分点；RH-Bench另报告RH-AUC收益。

### Shortcomings／局限与可能不足

【解读】证据生成错误仍可能循环强化；推理延迟、超参数和决策器可靠性影响实际收益，部分子项不变。

### 证据定位

PDF §2–3、表1 p.4、§4。

### Abstract

Recent large vision-language models (LVLMs) have demonstrated impressive reasoning ability by generating long chain-of-thought (CoT) responses. However, CoT reasoning in multimodal contexts is highly vulnerable to visual hallucination propagation: once an intermediate reasoning step becomes inconsistent with the visual evidence, subsequent steps—even if logically valid—can still lead to incorrect final answers. Existing solutions attempt to mitigate this issue by training models to “think with images” via reinforcement learning (RL). While effective, these methods are costly, model-specific, and difficult to generalize across architectures. Differently, we present a lightweight method that bypasses RL training and provides an iterative, training-free, plug-and-play framework for visuallygrounded multimodal reasoning. Our key idea is to supervise each reasoning step at test time with visual evidence, ensuring that every decoded token is justified by corresponding visual cues. Concretely, we construct a textual visual-evidence pool that guides the model’s reasoning generation. When existing evidence is insufficient, a visual decider module dynamically extracts additional relevant evidence from the image based on the ongoing reasoning context, expanding the pool until the model achieves sufficient visual certainty to terminate reasoning and produce the final answer. Extensive experiments on multiple LVLM backbones and benchmarks demonstrate the effectiveness of our approach. Our method achieves 16.5%–29.5% improvements on TreeBench and 13.7% RH-AUC gains on RH- Bench, substantially reducing hallucination rates while improving reasoning accuracy without additional training.

<a id="p087"></a>
## P087 · Don't Blink: Evidence Collapse during Multimodal Reasoning

- **作者**：Suresh Raghu; Satwik Pandey
- **时间**：本地版本：2026-04-05（arXiv:2604.04207v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint, Under Review；arXiv:2604.04207v1
- **论文链接**：[arXiv本地版本 2604.04207v1](https://arxiv.org/abs/2604.04207v1)
- **项目／代码／数据**：[代码：R-Suresh07/Dont-Blink](https://github.com/R-Suresh07/Dont-Blink)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：18页；SHA-256：`d4c05386de217c426af7adda5962f890cb31635e3ba957b26c4a18e7442825f9`

### 中文摘要

发现推理过程中视觉证据注意力下降，但其与出错的关系取决于任务；结合熵和视觉信号进行选择性拒答风险控制。

### 核心贡献

证据衰减诊断、熵—视觉交互模型及任务条件的vision veto。

### 实现边界

3个2B–8B模型、2模型家族、每数据集约300题；注意力是相关性信号，不能证明证据衰减导致错误。

### Method／方法

用标注证据区域选视觉grounding层，分析推理前后注意力、输出熵和正确性，拟合跨任务交互并在固定覆盖率筛除高风险回答。

### Results／主要结果

视觉证据注意力常下降超过一半；持续视觉参考任务中的低熵/低视觉关注更危险，符号任务未必；针对性veto在90%覆盖率下最多降低1.9个百分点选择性风险，全局线性融合可能恶化迁移。

### Shortcomings／局限与可能不足

【作者】模型/数据规模有限、极端象限每格仅2–8样本；分析假定任务类型已知，真实部署还需自动分类；待做激活干预检验因果性。

### 证据定位

PDF §3–5、Limitations p.8、附录B。

### Abstract

Reasoning VLMs can become more accurate while progressively losing visual grounding as they think. This creates task-conditional danger zones where low-entropy predictions are confident but ungrounded, a failure mode text-only monitoring cannot detect. Evaluating three reasoning VLMs on MathVista, HallusionBench, and MMMU_Pro, we find a pervasive evidence-collapse phenomenon: attention to annotated evidence regions drops substantially, often losing over half of evidence mass, as reasoning unfolds. Full-response entropy is the most reliable text-only uncertainty signal under cross-dataset transfer, yet adding vision features with a single global linear rule is brittle and often degrades transfer. An entropy-vision interaction model reveals a task-conditional regime: lowentropy, visually disengaged predictions are hazardous on sustained visual-reference tasks but benign on symbolic tasks. Using this structure, a targeted vision veto reduces selective risk by up to 1.9 percentage points at 90% coverage, while avoiding degradations where disengagement is expected. The results support task-aware multimodal monitoring for safe deployment under distribution shift. All code is publicly available at https:// github.com/R-Suresh07/Dont-Blink.

<a id="p088"></a>
## P088 · V-Retrver: Evidence-Driven Agentic Reasoning for Universal Multimodal Retrieval

- **作者**：Dongyang Chen; Chaoyang Wang; Dezhao Su; Xi Xiao; Zeyu Zhang; Jing Xiong; Qing Li; Yuzhang Shang; Shichao Kan
- **时间**：本地版本：2026-02-25（arXiv:2602.06034v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2602.06034v2（本地版本）
- **论文链接**：[arXiv本地版本 2602.06034v2](https://arxiv.org/abs/2602.06034v2)
- **项目／代码／数据**：[代码：chendy25/V-Retrver](https://github.com/chendy25/V-Retrver)；[数据/模型：V-Retrver](https://huggingface.co/V-Retrver)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：26页；SHA-256：`5ad4ffde63f37dc3ccae679a3335edcf4126775661e934ae8201ab65dfcb18b5`

### 中文摘要

在多模态检索候选重排时主动调用视觉工具查看细节，以交替假设与验证代替只依赖固定图像编码的文字推理。

### 核心贡献

V-Retrver代理式视觉检索推理及三阶段课程训练。

### 实现边界

在给定候选池上检索/重排，依赖初始召回及视觉工具；不是无成本全库端到端搜索。

### Method／方法

监督激活推理→拒绝采样精炼→证据对齐RL，学习针对模糊候选进行选择性图像检查。

### Results／主要结果

M-BEIR平均Recall69.7%，U-MARVEL-7B64.8%（+4.9个百分点）；FIQ51.2对38.2、CIRR73.5对63.2。各子任务Recall@K的K不同；摘要“平均23%”不能替代这里的同表绝对差。

### Shortcomings／局限与可能不足

【解读】多轮工具调用与候选数量增加成本，局部检查错误可传入重排，外部检索分布变化及规模化延迟仍需验证。

### 证据定位

PDF §3–4、表2 pp.6–7。

### Abstract

Multimodal Large Language Models (MLLMs) have recently been applied to universal multimodal retrieval, where Chain-of-Thought (CoT) reasoning improves candidate reranking. However, existing approaches remain largely languagedriven, relying on static visual encodings and lacking the ability to actively verify fine-grained visual evidence, which often leads to speculative reasoning in visually ambiguous cases. We propose V-Retrver, an evidence-driven retrieval framework that reformulates multimodal retrieval as an agentic reasoning process grounded in visual inspection. V-Retrver enables an MLLM to selectively acquire visual evidence during reasoning via external visual tools, performing a multimodal interleaved reasoning process that alternates between hypothesis generation and targeted visual verification. To train such an evidence-gathering retrieval agent, we adopt a curriculum-based learning strategy combining supervised reasoning activation, rejection-based refinement, and reinforcement learning with an evidence-aligned objective. Experiments across multiple multimodal retrieval benchmarks demonstrate consistent improvements in retrieval accuracy (with 23.0% improvements on average), perception-driven reasoning reliability, and generalization.

<a id="p089"></a>
## P089 · Fill the GAP: A Granular Alignment Paradigm for Visual Reasoning in Multimodal Large Language Models

- **作者**：Yanting Miao; Yutao Sun; Dexin Wang; Mengyu Zhou; Pascal Poupart; Lei Lv; Li Xu; Qi Zhao; Li Wang; Hao Li; Xiaoxi Jiang; Guanjun Jiang
- **时间**：本地版本：2026-05-25（arXiv:2605.12374v4）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2605.12374v4（本地版本）
- **论文链接**：[arXiv本地版本 2605.12374v4](https://arxiv.org/abs/2605.12374v4)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：PDF作者metadata缺Li Xu，已按首页完整作者名单补齐。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：23页；SHA-256：`4c3611e580ebef4d36d768a4b052d534b7185aab603c5bdce7e121eed47cd053`

### 中文摘要

诊断连续视觉潜推理将decoder隐状态直接反馈到输入时的特征尺度失配，提出特征、数据/上下文及难度分配的多粒度对齐。

### 核心贡献

GAP的PCA对齐latent head、可检查辅助图像监督与按难度选择潜token训练。

### 实现边界

在Qwen2.5VL-7B等所评设置微调；辅助图像用于监督构造，不是推理时外部图像生成；前作系统对比训练配方不同，不能全部归因为架构。

### Method／方法

构造49,309个图像—问题—辅助图像样本，学习映射回视觉输入子空间，选择基础模型困难题应用潜监督，并控制latent token预算。

### Results／主要结果

相对Monet，平均感知+1.74、平均推理+5.98个百分点；相对LVR+0.57/+6.31；基础Qwen Avg-R52.62，而前两者47.99/47.66，说明潜推理也可能退化。

### Shortcomings／局限与可能不足

【作者/解读】结果主要是均值点估计，潜目标质量/子空间和难度阈值影响收益；更多潜token不必然更好，泛化到其他架构仍需验证。

### 证据定位

PDF §3–5、表2–5、§6；作者p.1。

### Abstract

Visual latent reasoning lets a multimodal large language model (MLLM) create intermediate visual evidence as continuous tokens, avoiding external tools or image generators. However, existing methods usually follow an output-as-input latent paradigm and yield unstable gains. We identify evidence for a feature-space mismatch that can contribute to this instability: dominant visual-latent models build on pre-norm MLLMs and reuse decoder hidden states as predicted latent inputs, even though these states occupy a substantially different norm regime from the input embeddings the model was trained to consume (Xie et al., 2025; Li et al., 2026; Team et al., 2026). This mismatch can make direct latent feedback unreliable. Motivated by this diagnosis, we propose GAP, a Granular Alignment Paradigm for visual latent modeling. GAP aligns visual latent reasoning at three levels: feature-level alignment maps decoder outputs into input-compatible visual latents through a lightweight PCA-aligned latent head; context-level alignment grounds latent targets with inspectable auxiliary visual supervision; and capacityguided alignment assigns latent supervision selectively to examples where the base MLLM struggles. On Qwen2.5-VL 7B, the resulting model achieves the best mean aggregate perception and reasoning performance among our supervised variants. Inference-time intervention probing further suggests that generated latents provide task-relevant visual signal beyond merely adding token slots.

<a id="p090"></a>
## P090 · From &lt;Answer&gt; to &lt;Think&gt;: Multi-Dimensional Supervision of Reasoning Process for LLM Optimization

- **作者**：Anonymous authors（本地双盲稿未署名）
- **时间**：本地匿名稿未注明日期；ICLR 2026是投稿轮次，不作为正式发表时间
- **发表平台／版本状态**：Under review as a conference paper at ICLR 2026；此状态不表示已录用，日期未明确
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：33页；SHA-256：`ffe9f19fb7c2282d7818de1e63fbceaacdcd600c34e4b357d03e839a8c20605a`

### 中文摘要

用置信度、相关性与连贯性三个维度评价完整推理过程，作为无需逐步切分或标准答案的奖励，支持偏好优化和RL。

### 核心贡献

Dimension-level Reward Model（DRM）及DPO/GRPO训练应用，补充仅最终正确性或逐步PRM监督。

### 实现边界

评分不要求答案真值，但仍借助预训练相关性/奖励模型及训练数据；不等于没有任何监督或能保证逻辑正确。

### Method／方法

置信度校准、Qwen3-8B-Reranker语义相关性及Nemotron70B奖励模型连贯性组成分数，构造偏好对或在线奖励，可与可验证答案奖励组合。

### Results／主要结果

在Llama3.1-8B、R1-Distill-Llama8B及Qwen3-8B上报告数学、QA、代码执行与谜题的ID/OOD收益；DRM能区分答案均对或均错的样本，DRM@ANY在表4优于对应只看答案的偏好构造。

### Shortcomings／局限与可能不足

【解读】高置信/相关/流畅不保证事实与逻辑正确，存在奖励投机；外部评判模型较大，评分和优化成本不可忽略；匿名稿元数据与公开复现状态未确认。

### 证据定位

PDF §2–3、表4–5、§6；首页匿名状态。

### Abstract

Large language models (LLMs) can develop strong reasoning ability when trained appropriately. Existing approaches are broadly categorized into outcome-level answer supervision and process-level reasoning supervision. However, the former provides only sparse binary feedback and overlooks intermediate step quality, while the latter scores individual steps but requires task-specific segmentation. To this end, we propose a novel framework that assesses the quality of reasoning process along three dimensions:Confidencefor uncertainty calibration,Relevancefor semantic alignment andCoherencefor logical consistency. Together, these dimensions capture aspects beyond final answer correctness and enable interpretable assessment without requiring ground truth answers. Our framework serves as aDimension-levelRewardModel (DRM) that assigns scores to reasoning processes and provides supervision signals for both off-policy (e.g., DPO) and on-policy (e.g., GRPO) optimization. Experimental results show that DRM provides effective supervision signals, guides the optimization of LLMs and enhances their reasoning ability. In particular, DRM-supervised training achieves consistent gains on both in-distribution and out-of-distribution open-domain tasks, including mathematics, question answering, code execution and puzzles. Our findings demonstrate that multidimensional supervision of reasoning process can improve the generalized reasoning ability of LLMs beyond the training distribution.

<a id="p091"></a>
## P091 · Improving Human Verification of LLM Reasoning through Interactive Explanation Interfaces

- **作者**：Runtao Zhou; Giang Nguyen; Nikita Kharya; Anh Nguyen; Chirag Agarwal
- **时间**：2026年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：IUI 2026，2026-03-23—26；DOI 10.1145/3742413.3789134
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3742413.3789134)
- **项目／代码／数据**：[代码：Runtaozhou/Interactive-CoT](https://github.com/Runtaozhou/Interactive-CoT)

- **主题**：创作与规则补全、XR与人机协作
- **PDF版本**：18页；SHA-256：`9ec925e6e875d9130a70e08ff8777481680bd097aad8d78aacbca46319149bf2`

### 中文摘要

比较传统CoT与可交互文本、程序和图形解释，研究用户能否更准确核查数学解答及定位推理错误。

### 核心贡献

iCoT、iPoT、iGraph三种格式转换界面及125人验证实验。

### 实现边界

优化的是人类核查模型解释的表现，不是LLM自主解题；10道实验题中正确/错误解释比例1:9，结果受错误高基率影响。

### Method／方法

保持解释底层内容，改变结构、渐进展示、变量高亮和依赖关系；被试组间比较正确性核验、错误定位、时间及体验。

### Results／主要结果

核验准确率iGraph85.6%、iPoT82.5%、iCoT80.6%、普通CoT73.5%；平均响应时间57.9、约60、约60、64.7秒。

### Shortcomings／局限与可能不足

【作者】1:9不平衡是为覆盖9类错误并控制疲劳；图复杂度、代码语法和顺序文本各有成本；【解读】有限数学任务不能代表长期学习提升或真实低错误率审核。

### 证据定位

PDF §3–5、图5–7、§7 p.10。

### Abstract

The reasoning capabilities of Large Language Models (LLMs) have led to their increasing employment in several critical applications, particularly education, where they support problem-solving, tutoring, and personalized study. While there are a plethora of works showing the effectiveness of LLMs in generating step-by-step solutions through chain-of-thought (CoT) reasoning on reasoning benchmarks, little is understood about whether the generated CoT is helpful for end-users in improving their ability to comprehend mathematical reasoning problems and detect errors/hallucinations in LLM-generated solutions. To address this gap and contribute to understanding how reasoning can improve human-AI interaction, we present three new interactive reasoning interfaces: interactive CoT (iCoT), interactive Program-of-Thought (iPoT), and interactive Graph (iGraph), and a novel framework that generates the LLM’s reasoning from traditional CoT to alternative, interactive formats. Across 125 participants, we found that interactive interfaces significantly improved performance. Specifically, the iGraph interface yielded the highest clarity and error detection rate (85.6%), followed by iPoT (82.5%), iCoT (80.6%), all outperforming standard CoT (73.5%). Interactive interfaces also led to faster response times, where participants using iGraph were fastest (57.9 secs), compared to iCoT and iPoT (60 secs), and the standard CoT baseline (64.7 secs). Furthermore, participants preferred the iGraph reasoning interface, citing its superior ability to enable users to follow the LLM’s reasoning process. We discuss the implications of these results and provide recommendations for the future design of reasoning models. The code and interfaces for this project can be found here: https://github.com/Runtaozhou/Interactive-CoT

<a id="p092"></a>
## P092 · Improving Visual Reasoning with Iterative Evidence Refinement

- **作者**：Zeru Shi; Kai Mei; Yihao Quan; Dimitris N. Metaxas; Ruixiang Tang
- **时间**：本地版本：2026-03-14（arXiv:2603.14117v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2603.14117v1，2026-03（本地版本）
- **论文链接**：[arXiv本地版本 2603.14117v1](https://arxiv.org/abs/2603.14117v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：21页；SHA-256：`90f64b8dd352647c94fd531a6da25b2f0ddbc909fd3c6c949eb59f10a351edb2`

### 中文摘要

SIEVE通过模型内部显著图像区域的embedding重复访问证据，以RL学习何时以及取哪些区域，避免外部裁剪与重新编码。

### 核心贡献

内生视觉重访和证据嵌入插入推理链的训练框架。

### 实现边界

需要RL训练和隐状态访问，不是training-free；复用已有视觉编码不能恢复首次编码完全丢失的细节。

### Method／方法

依据文本锚点和视觉显著性抽取区域表示，在生成中触发重访并注入embedding，按回答奖励学习调用策略。

### Results／主要结果

表1 Qwen3VL-4B V*78.01→85.86%（+7.85个百分点/约10.06%相对），HR4K77.75→81.25、HR8K72.38→76.13；但ZoomEye的4B V*为90.05，高于SIEVE，正文“所有基线均胜出”的概括不完全符合表格。

### Shortcomings／局限与可能不足

【解读】既有表征、显著性定位错误和RL奖励限制证据质量；不同工具方法速度/输入预算需一起比较，不能只看平均得分。

### 证据定位

PDF §3–4、表1 pp.7–8；正文与表格例外已注明。

### Abstract

Vision–language models (VLMs) are increasingly capable of reasoning over images, but robust visual reasoning often requires re-grounding intermediate steps in the underlying visual evidence. Recent approaches typically rely on external image operations such as zooming or cropping to re-access fine-grained details during inference, which requires additional image re-encoding and can disrupt the reasoning trajectory. We argue that VLMs already provide strong internal signals for identifying and reusing visual evidence, and that these signals can be directly leveraged to support image-grounded reasoning. Motivated by this insight, we propose an end-to-end self-revisit framework,SIEVE, that trains models to re-engage image evidence through internal representations. SIEVEautomatically extracts embeddings of salient image regions and injects them into the reasoning chain when additional grounding is needed, enabling later steps to condition on relevant visual cues without external tool calls or re-encoding. We use reinforcement learning to teach the model when to trigger visual revisiting and which region embeddings to retrieve and insert during the reasoning process. Experiments on multiple visual reasoning benchmarks, together with perception, reasoning, and hallucination evaluations, show that SIEVEyields consistent gains, improving performance by 8% on average across several benchmarks.

<a id="p093"></a>
## P093 · Instruction-Evidence Contrastive Dual-Stream Decoding for Grounded Vision-Language Reasoning

- **作者**：Yashwant Pravinrao Bangde; Debaditya Roy
- **时间**：本地版本：2026-05-08（arXiv:2604.25809v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2604.25809v2（本地版本）
- **论文链接**：[arXiv本地版本 2604.25809v2](https://arxiv.org/abs/2604.25809v2)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：14页；SHA-256：`68ff3ed3e82e6fec964e338c9348812bd24878ec360a421ddff61a154b9fab90`

### 中文摘要

分别以任务指令和严格视觉证据提示计算两条token分布，用分歧自适应门控融合，降低语言先验驱动的幻觉。

### 核心贡献

Instruction-Evidence Contrastive Dual-Stream Decoding（IECD²）的双流及对称KL门控。

### 实现边界

推理时双流概率，依赖开放模型logits和证据提示；两流均来自模型，证据流不是真实标签。

### Method／方法

每步计算instruction/evidence两分布；一致时保留表达性，分歧大时抑制仅语言流偏好的token；跨caption/VQA/对象幻觉评估。

### Results／主要结果

在LLaVA1.5和InstructBLIP的POPE、AMBER、VQAv2、MME及COCO报告改善，尤其POPE adversarial；各指标与骨干详见表1及生成评测表，不能把所有子项概括为同一提升幅度。

### Shortcomings／局限与可能不足

【作者】视觉证据不足时收益受限、提示分离与KL门控超参数跨任务/架构变化；【解读】双流增加推理成本，一致但错误仍难检测。

### 证据定位

PDF §3–4、表1、§5 p.10。

### Abstract

Vision-Language Models (VLMs) exhibit strong performance in instruction following and open-ended vision-language reasoning, yet they frequently generate fluent outputs that are weakly grounded in visual evidence. Prior works have shown that instruction prompting further worsens this issue by amplifying language priors, especially when the visual signal is uncertain or ambiguous. To address this challenge, we propose a decoding framework that explicitly balances linguistic informativeness and visual faithfulness during generation. Our method, Instruction-Evidence Contrastive Dual-Stream Decoding (IECD2), maintains two parallel probability distribution of tokens at each decoding step: an instruction-driven stream that promotes expressive and informative responses, and an evidence-driven stream that enforces strict grounding in the image. These two streams are adaptively fused using a symmetric KL-based contrastive gate, which suppresses tokens favored by language priors but unsupported by visual evidence, while preserving them when both distributions agree. We evaluate IECD2 on multiple datasets spanning various generative vision-language reasoning tasks such as captioning and visual question answering on multiple datasets such as, POPE, MME, VQAv2, AMBER, and MSCOCO. IECD 2 demonstrates consistent improvements in task accuracy and reasoning performance with substantial reduction in hallucination compared to state-of-the-art decoding approaches.

<a id="p094"></a>
## P094 · SaaS-Bench: Can Computer-Use Agents Leverage Real-World SaaS to Solve Professional Workflows?

- **作者**：Kean Shi; Zihang Li; Tianyi Ma; Zengji Tu; Jialong Wu; Wendong Xu; Xinbo Xu; Qingyao Yang; Ruoyu Wu; Weichu Xie; Ming Wu; Jason Zeng; Michael Heinrich; Elvis Zhang; Liang Chen; Kuan Li; Baobao Chang
- **时间**：本地版本：2026-05-24（arXiv:2605.15777v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：技术报告，首页2026-05-26；arXiv:2605.15777v2
- **论文链接**：[arXiv本地版本 2605.15777v2](https://arxiv.org/abs/2605.15777v2)
- **项目／代码／数据**：[代码：UniPat-AI/SaaS-Bench](https://github.com/UniPat-AI/SaaS-Bench)；[项目/演示页面 2](https://unipat.ai/blog/SaaS-Bench)
- **版本关系**：PDF作者metadata遗漏Wendong Xu，已按首页补齐。

- **主题**：XR与人机协作
- **PDF版本**：24页；SHA-256：`99ec0f81715a715fb4709c1810e1537ba5cad294c9a1878bd63531abdfc9a8ed`

### 中文摘要

在23个可部署SaaS系统、6个职业领域中设置106个跨应用长流程任务，以加权检查点衡量部分进度和完整完成。

### 核心贡献

可部署真实软件环境及长流程多模态评测，区分checkpoint score与resolved rate。

### 实现边界

是受控部署的SaaS工作流评测，成绩依赖给定工具/步数/模型版本；部分纯文本模型只评文本域，分母不同。

### Method／方法

提供任务、应用入口和凭据，代理操作浏览器/GUI；检查各中间状态和最终目标，分析阶段衰减与错误类型。

### Results／主要结果

表2最高总体检查点分43.9%，最高全流程完成率3.8%；GPT5.5High等头部检查点约43–44%，不代表完成同等比例任务；模型在后续阶段持续衰减。

### Shortcomings／局限与可能不足

【解读】有限任务及应用配置不能穷尽专业工作，检查点权重和预算影响排名；多次尝试提升部分表现但未解决完整流程可靠性。

### 证据定位

PDF §3–4、表2 pp.7–9、§6。

### Abstract

Computer-Using Agents (CUAs) are rapidly extending large language models (LLMs) beyond text-based reasoning toward action execution in more complex environments, such as web browsers and graphical user interfaces (GUIs). However, existing web and GUI agent benchmarks often rely on simplified settings, isolated tasks, or short-horizon interactions, making it difficult to assess capabilities of agents in realistic professional workflows. Software-as-a-Service (SaaS) environments are a natural choice for CUA evaluation, as they host a large share of modern digital work and naturally involve dynamic system states, cross-application coordination, domainspecific knowledge, and long-horizon dependencies. To this end, we introduce SAAS-BENCH, a benchmark built on 23 deployable SaaS systems across six professional domains, containing 106 tasks grounded in realistic work scenarios. These tasks require long-horizon execution, cover both text-only and multimodal settings, and are evaluated with weighted verification checkpoints that measure strict task completion and partial progress. Experiments show that representative LLM-based agents struggle on SAAS-BENCH, with even the strongest model completing fewer than 4% of tasks end-to-end, exposing limitations in planning, state tracking, cross-application context maintenance, and error recovery. Code are available at UniPat-AI/SaaS-Bench for reproduction. HOMEPAGE:https://unipat.ai/blog/SaaS-Bench

<a id="p095"></a>
## P095 · TIR-Flow: Active Video Search and Reasoning with Frozen VLMs

- **作者**：Hongbo Jin; Siyi Xie; Jiayu Ding; Kuanwei Lin; Ge Li
- **时间**：本地版本：2026-01-07（arXiv:2601.06176v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2601.06176v1，2026-01（本地版本）
- **论文链接**：[arXiv本地版本 2601.06176v1](https://arxiv.org/abs/2601.06176v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作
- **PDF版本**：14页；SHA-256：`55c6f57cdd9fd2a838d7f75df0e26eee001942e0b8bebe7806c901f85b182dc2`

### 中文摘要

冻结视频VLM，通过分解问题、主动局部观察与持久证据工作区迭代进行视频搜索和推理。

### 核心贡献

HDD任务分解、HAP高保真主动感知、EBA证据仲裁组成TIR-Flow。

### 实现边界

不更新模型参数，但使用多轮推理/视频片段访问；所谓“严格逻辑一致”无形式证明，受基础模型规划能力限制。

### Method／方法

把问题拆成可验证子任务，针对假设搜索/放大视频证据，累积修订线索再回答。

### Results／主要结果

7个基准报告平均约5.9个百分点收益；Qwen2.5VL-7B EgoSchema69.2%，较基线+10.5个百分点；推理类子集平均约6.7，两个平均不能混用。

### Shortcomings／局限与可能不足

【作者】仅重点评估7B级LLaVA-Video/Qwen2.5VL，错误初始分解可传播，多轮主动感知降低速度。

### 证据定位

PDF §3–4、表1、Limitations p.9。

### Abstract

While Large Video-Language Models (Video- LLMs) have achieved remarkable progress in perception, their reasoning capabilities remain a bottleneck. Existing solutions typically resort to a heavy "data engineering" paradigm—synthesizing large-scale Chain-of- Thought (CoT) datasets followed by Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). This pipeline primarily optimizes probability sampling efficiency and aligns output distributions, but fails to activate the intrinsic intelligence required for dynamic visual exploration. In this work, we proposeTIR-Flow, a novel framework that shifts the paradigm from passive processing to active video searching and reasoning without additional data or parameter updating. Concretely, our framework operates through three synergistic modules:HDDdecomposes complex queries into a set of verifiable sub-tasks; HAPactively directs visual attention to gather high-resolution evidence for hypothesis validation;EBAmaintains a persistent workspace to accumulate and update the discovered clues for logical reasoning. Extensive experiments on seven benchmarks demonstrate that TIR- Flow significantly outperforms recent strong baselines, delivering an average performance boost of5.9%, with gains reaching10.5%on Egoschema. Our analysis confirms that empowering frozen VLMs with System-2-like active perception is a scalable path toward solving long-horizon video reasoning.

<a id="p096"></a>
## P096 · TSRBench: A Comprehensive Multi-task Multi-modal Time Series Reasoning Benchmark for Generalist Models

- **作者**：Fangxu Yu; Xingang Guo; Lingzhi Yuan; Haoqiang Kang; Hongyu Zhao; Lianhui Qin; Furong Huang; Bin Hu; Tianyi Zhou
- **时间**：本地版本：2026-05-07（arXiv:2601.18744v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICML 2026，PMLR306（PDF首页）；arXiv:2601.18744v2
- **论文链接**：[arXiv本地版本 2601.18744v2](https://arxiv.org/abs/2601.18744v2)
- **项目／代码／数据**：[项目/演示页面](https://tsrbench.github.io/)

- **主题**：世界机制与演化
- **PDF版本**：32页；SHA-256：`25dea52cdcb7c8a0a3177586f33d7cd35d7ea00f89222942859987d2928ea700`

### 中文摘要

用文本、图形时间序列评估通用模型在感知、推理、预测与决策上的能力，并分析规模和模态组合效应。

### 核心贡献

14领域、4,125题、15任务的TSRBench及30余种LLM/VLM/TSLLM比较。

### 实现边界

基准得分衡量所构造任务，不能直接代表真实预测收益、临床/金融决策质量；“scaling规律失效”是该样本上的经验现象。

### Method／方法

统一时间序列多模态输入和任务定义，比较文本/视觉/合并输入、模型规模及子任务关联。

### Results／主要结果

GPT5文本+视觉总体55.6%；开放LLM Qwen2.5-72B42.4%，开放VLM Qwen3VL-32B44.9%。推理/感知随规模改善，预测关联较弱或负；多模态互补未被稳定利用。

### Shortcomings／局限与可能不足

【解读】文本序列编码、绘图格式和答案评分均影响结果，有限领域题库与模型快照不能建立普遍规模定律。

### 证据定位

PDF §3–4、表2、图3–4、§5。

### Abstract

Time series are ubiquitous in real-world scenarios and crucial for applications ranging from energy management to traffic control. Consequently, the ability to reason over time series is a fundamental skill for generalist models to solve complex problems. However, current benchmarks for generalist models largely overlook this dimension. To bridge this gap, we introduce TSRBENCH, a comprehensive multi-modal benchmark designed to stress-test the full spectrum of time series reasoning capabilities. TSRBENCH features: i) a diverse set of 4125 problems from 14 domains, and is categorized into 4 major dimensions: Perception, Reasoning, Prediction, and Decision-Making. ii) 15 tasks from the 4 dimensions evaluating essential reasoning capabilities (e.g., numerical reasoning). Through extensive experiments, we evaluate over 30 leading proprietary and open-source LLMs, VLMs, and TSLLMs within TSRBENCH. Our findings reveal that: i) scaling laws hold for perception and reasoning but break down for prediction; ii) strong reasoning does not guarantee accurate context-aware forecasting, indicating a decoupling between semantic understanding and numerical prediction; and iii) despite the complementary nature of textual and visual forms of time series as inputs, current multimodal models fail to effectively fuse them for reciprocal performance gains. TSRBENCH provides a standardized evaluation platform that not only highlights existing challenges but also offers valuable insights to advance generalist models. Our code and dataset are available at https://tsrbench.github.io/.

<a id="p097"></a>
## P097 · Useful Memories Become Faulty When Continuously Updated by LLMs

- **作者**：Dylan Zhang; Yanshan Lin; Zhengkun Wu; Yihang Sun; Bingxuan Li; Dianqi Li; Hao Peng
- **时间**：本地版本：2026-05-13（arXiv:2605.12978v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2605.12978v1，2026-05（本地版本）
- **论文链接**：[arXiv本地版本 2605.12978v1](https://arxiv.org/abs/2605.12978v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：重要数值冲突：摘要说GPT5.4在已解ARC题中“fails on 54%”；正文p.2说失败46%，§4说准确率降到54%。汇总依正文写54%准确率，并保留摘要原句供核对。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：69页；SHA-256：`16613d73b3dfe8de8dd73d42c4fb7b2e803b84a78d7ecf748c9e23a7e3b4aa92`

### 中文摘要

持续把经验压缩改写成文字记忆可能先有帮助再逐渐损坏，即使输入是有用轨迹或标准答案，抽象/合并过程仍会积累失真。

### 核心贡献

多代理基准的连续记忆退化诊断，控制更新顺序/分组及原始情节保留，并构建ARC-AGI Stream记忆动作环境。

### 实现边界

研究自然语言外部记忆及当前LLM整理器，不涉及权重更新或所有结构化记忆；不能推出记忆本身必然有害。

### Method／方法

固定经验池比较Static-All、Static-Group、Stream与只保留episodic轨迹；允许Retain/Delete/Consolidate；分析错分组、过度概括和窄分布过拟合。

### Results／主要结果

WebShop AWM随经验从8增至128，成功率0.64→0.20（无记忆0.20）；19题已被GPT5.4无记忆全部解出的ARC切片，在带真值合并后正文报告准确率降至约54%；原始轨迹对照仍有竞争力。

### Shortcomings／局限与可能不足

【作者】文本代理/受控ARC环境、少数模型家族，重复次数少且未报正式误差条；真实具身、多模态及其他记忆格式待验证。

### 证据定位

PDF pp.1–3、§4–6、图1–2/4、§8 p.11；摘要与正文数值冲突。

### Abstract

Learning from past experience benefits from two complementary forms of memory: episodic traces—raw trajectories of what happened—and consolidated abstractions distilled across many episodes into reusable, schema-like lessons. Recent agentic-memory systems pursue the consolidated form: an LLM rewrites past trajectories into a textual memory bank that it continuously updates with new interactions, promising selfimproving agents without parameter updates. Yet we find that such consolidated memories produced by today’s LLMs are often faulty even when derived from useful experiences. As consolidation proceeds, memory utility first rises, then degrades, and can fall below the no-memory baseline. More surprisingly, even when consolidating from ground-truth solutions, GPT-5.4 fails on 54% of a set of ARC-AGI problems it had previously solved without memory. We trace the regression to the consolidation step rather than the underlying experience: the same trajectories yield qualitatively different memories under different update schedules, and an episodiconly control that simply retains those trajectories remains competitive with the consolidators we test. In a controlled ARC-AGI Stream environment that exposes Retain, Delete, and Consolidate actions, agents preserve raw episodes by default and double the accuracy of their forced-consolidation counterparts; disabling consolidation entirely (episodic management only) matches this auto regime. Practically, robust agent memory should treat raw episodes as first-class evidence and gate consolidation explicitly rather than firing it after every interaction. Looking forward, reliable agentic memory will require LLMs that can consolidate without overwriting the evidence they depend on.

<a id="p098"></a>
## P098 · First Logit Boosting: Visual Grounding Method to Mitigate Object Hallucination in Large Vision-Language Models

- **作者**：Jiwoo Ha; Jongwoo Baek; Jinhyun So
- **时间**：本地版本：2026-04-01（arXiv:2604.00455v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2604.00455v1，2026-04（本地版本）
- **论文链接**：[arXiv本地版本 2604.00455v1](https://arxiv.org/abs/2604.00455v1)
- **项目／代码／数据**：[代码：jiwooha20/FLB](https://github.com/jiwooha20/FLB)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：19页；SHA-256：`ab4f4c867fb503cf82a5beed05b964b90cb445abb3ee0729e0fdc4b4857665d3`

### 中文摘要

保存首次生成时的整条词表logit向量，并在后续解码中加权补回，缓解长文本生成时视觉约束减弱造成的对象幻觉。

### 核心贡献

First Logit Boosting（FLB）轻量解码方法，并分析初始视觉信号与“The”等词的间接稳定作用。

### 实现边界

复用的是第一步完整logits，不是重复第一个词；不增加额外模型或双路逐token推理，但不能动态重新读取新证据。

### Method／方法

缓存l₀，在每一步对当前logits加入加权初始分布后采样；跨对象幻觉任务、模型及基准比较。

### Results／主要结果

报告在多LVLM和幻觉基准上减少虚构对象，且推理开销接近基线；改进来自静态早期信号补偿，并非消除位置编码导致的长期衰减。

### Shortcomings／局限与可能不足

【作者】无法充分处理上下文变化的视觉语义，未根治RoPE衰减；【解读】首步不可靠或任务需新证据时，静态强化也可能引入偏差。

### 证据定位

PDF §4–6、§7及Limitations p.8。

### Abstract

Recent Large Vision-Language Models (LVLMs) have demonstrated remarkable performance across various multimodal tasks that require understanding both visual and linguistic inputs. However, object hallucination — the generation of nonexistent objects in answers — remains a persistent challenge. Although several approaches such as retraining and external grounding methods have been proposed to mitigate this issue, they still suffer from high data costs or structural complexity. Training-free methods such as Contrastive Decoding (CD) are more costeffective, avoiding additional training or external models, but still suffer from long-term decay, where visual grounding weakens and language priors dominate as the generation progresses. In this paper, we propose First Logit Boosting (FLB), a simple yet effective training-free technique designed to alleviate long-term decay in LVLMs. FLB stores the logit of the first generated token and adds it to subsequent token predictions, effectively mitigating longterm decay of visual information. We observe that FLB (1) sustains the visual information embedded in the first token throughout generation, and (2) suppresses hallucinated words through the stabilizing effect of the “The” token. Experimental results show that FLB significantly reduces object hallucination across various tasks, benchmarks, and backbone models. Notably, it causes negligible inference overhead, making it highly applicable to real-time multimodal systems. Code is available athttps://github.com/jiwooha20/FLB

<a id="p099"></a>
## P099 · VGS-Decoding: Visual Grounding Score Guided Decoding for Hallucination Mitigation in Medical VLMs

- **作者**：Govinda Kolli; Adinath Madhavrao Dukre; Behzad Bozorgtabar; Dwarikanath Mahapatra; Imran Razzak
- **时间**：本地版本：2026-03-19（arXiv:2603.20314v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2603.20314v1，2026-03（本地预印本）；模板不能证明已正式录用
- **论文链接**：[arXiv本地版本 2603.20314v1](https://arxiv.org/abs/2603.20314v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：11页；SHA-256：`cbffff846249c3568249b13ebeb8e15d339fece08618710efe4eaecd716e4206`

### 中文摘要

通过原图与加噪图条件下词概率的差异估计视觉依赖，按token自适应调整医疗VLM解码以减少幻觉。

### 核心贡献

Visual Grounding Score与VGS-Decoding，区别于固定权重对比解码。

### 实现边界

医疗影像问答离线评测，不是临床验证；视觉依赖分数不保证医学正确性；代码在稿中仅承诺录用后发布。

### Method／方法

向原图加Gaussian/Poisson噪声，双路得到token分布，以视觉退化后的概率变化定义VGS并重加权候选。

### Results／主要结果

LLaVA-Med、CheXagent、MedGemma在VQA-RAD和MIMIC-Diff-VQA六组合均报告改善；MedGemma总体分别+8.16/+9.12个百分点，CheXagent在MIMIC仅+0.12；约2倍推理开销。

### Shortcomings／局限与可能不足

【解读】加噪反应未必等同病灶依据，可能损伤细微信号；仅两个数据集，缺乏临床安全/外部验证，摘要“适合临床部署”超出实验已证实范围。

### 证据定位

PDF §2–3、表1–2、§4 p.9。

### Abstract

Medical Vision-Language Models (VLMs) often hallucinate by generating responses based on language priors rather than visual evidence, posing risks in clinical applications. We propose Visual Grounding Score Guided Decoding (VGS-Decoding), a training-free method to mitigate hallucinations during inference. Our key insight is that hallucinated tokens maintain or increase their probability when visual information is degraded, while visually grounded tokens decrease in probability. We introduce the Visual Grounding Score (VGS), which measures each token’s visualdependencybycomparingdistributionsfromoriginalanddistorted images. During decoding, we reweight probabilities by amplifying visually grounded tokens while suppressing hallucinations. Unlike fixedweight contrastive methods, VGS-Decoding provides per-token adaptive control. Experiments on MIMIC-Diff-VQA and VQA-RAD across LLaVA-Med, CheXagent, and MedGemma demonstrate consistent improvements, with up to+9.12%overall gain and+8.98%in open-ended recall, while introducing only2×inference overhead and no additional training, making it practical for clinical deployment. Upon acceptance, code will be released publicly to facilitate reproducibility.

<a id="p100"></a>
## P100 · When Thinking Drifts: Evidential Grounding for Robust Video Reasoning

- **作者**：Mi Luo; Zihui Xue; Alex Dimakis; Kristen Grauman
- **时间**：首发2025-10-07；本地PDF具体版本时间未明示
- **发表平台／版本状态**：arXiv:2510.06077，首发2025-10-07（官方arXiv核验）；本地版本日期未从首页确定，文件名26不是发表证据。 [arXiv记录](https://arxiv.org/abs/2510.06077)
- **论文链接**：[arXiv论文记录](https://arxiv.org/abs/2510.06077)
- **项目／代码／数据**：[项目/演示页面](https://vision.cs.utexas.edu/projects/video-ver/)

- **主题**：世界机制与演化、XR与人机协作
- **PDF版本**：32页；SHA-256：`2ae02aa04e836398b722dd92b870b3c1937e7f102f2a6a84be28ff44e7e04e26`

### 中文摘要

分析视频CoT可能因语言先验而偏离视觉内容，提出Visual Evidence Reward，用RL促使推理过程保持可验证的视频证据。

### 核心贡献

Visual Thinking Drift诊断及Video-VER证据奖励训练。

### 实现边界

主要在选择题等封闭答案任务构造规则奖励；开放式QA明确列为未来工作；Bayesian解释不构成所有漂移的因果证明。

### Method／方法

将答案正确、视觉证据、格式和长度奖励结合GRPO（证据权重0.3），训练模型产生与问题相关视频内容一致的推理。

### Results／主要结果

10基准中所比较开放模型9项排名第一，VSI-Bench由Video-R1更强；TempCompass74.0%、TVBench52.8%。多基础模型直接CoT会下降，证据训练后较稳定。

### Shortcomings／局限与可能不足

【作者】开放式推理证据奖励待扩展；【解读】受奖励验证器、封闭答案及基础视频感知限制，长而有格式的推理仍可能不忠实。

### 证据定位

PDF §3–5、表1、§6 p.10。

### Abstract

Video reasoning, the task of enabling machines to infer from dynamic visual content through multi-step logic, is crucial for advanced AI. While the Chain-of-Thought (CoT) mechanism has enhanced reasoning in text-based tasks, its application to video understanding remains underexplored. This paper presents a systematic analysis revealing that CoT often degrades performance in video reasoning, generating verbose but misleading internal monologues, and leading to hallucinated visual details and overridden correct intuitions—a phenomenon we term "visual thinking drift." We explain this drift through a Bayesian lens, positing that CoT traces often diverge from actual visual evidence, instead amplifying internal biases or language priors, causing models to storytell rather than engage in grounded reasoning. To counteract this, we introduce Visual Evidence Reward (VER), a reinforcement learning framework that explicitly rewards the generation of reasoning traces that are verifiably grounded in visual evidence. Comprehensive evaluation across 10 diverse video understanding benchmarks demonstrates that our Video-VER consistently achieves top performance. Our work sheds light on the distinct challenges of video-centric reasoning and encourages the development of AI that robustly grounds its inferences in visual evidence—for large multimodal models that not only “think before answering", but also “see while thinking".1

<a id="p101"></a>
## P101 · Computational Understanding of Narratives: A Survey

- **作者**：Priyanka Ranade; Sanorita Dey; Anupam Joshi; Tim Finin
- **时间**：2022年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：IEEE Access，Vol.10，2022；收到2022-07-18、接受09-01、发表09-08、当前版09-30；DOI 10.1109/ACCESS.2022.3205314
- **论文链接**：[DOI正式记录](https://doi.org/10.1109/ACCESS.2022.3205314)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：20页；SHA-256：`976245eb5b4ee27353330a79987c9c069803301b597c0adbedf36e2ae4e9318c`

### 中文摘要

综述叙事的计算理解，特别是在线多源碎片化叙事的构建、抽取、演化、生成、表示与评估。

### 核心贡献

整理叙事结构组成、语义/时间关系和研究任务层次，汇集资源与开放挑战。

### 实现边界

综述及概念整理，不是统一实现系统；涵盖到2022年前后的技术，不能作为后续LLM叙事研究全景。

### Method／方法

围绕实体/事件、主题、意图和关系组织IR/NLU工作，比较自包含故事与跨来源演化叙事。

### Results／主要结果

产出研究分类图、语义关系示例和代表项目/挑战表，强调跨源连接、时间演化、意图/修辞及一致评估不足；无新模型准确率结果。

### Shortcomings／局限与可能不足

【解读】叙事定义与粒度跨学科不统一，在线数据偏差/噪声和标准真值缺乏使方法难公平比较；综述选取本身非穷尽。

### 证据定位

PDF §§II–V、图2、表1/3、§VI p.16。

### Abstract

Storytelling, and the delivery of societal narratives, enable human beings to communicate, connect, and understand one another and the world around them. Narratives can be defined as spoken, visual, or written accounts of interconnected events and actors, generally evolving through some notion of time. Today, information is typically conveyed over online communication mediums, such as social media and blogging websites. Consequently, the act of narrative delivery itself has shifted from simply imparting information through self-contained structures such as books, to more fragmented structures, such as social media websites, where evolving story events are constructed over multiple online sources. Ubiquitous online conversation can manifest into sophisticated narratives that have the potential to influence wide-spread user interpretations of cultural sentiments, attitudes, values, as well as geopolitical events and facts. As a result, narratives are actively being used as strategic tools for shaping local events, promoting collective opinions, and asserting ideologies and propaganda, making them sources of interest for identifying themes, intentions, and goals across multiple communities and potential adversaries. Identifying fragmented narratives, extracting thematic and temporal components that constitute evolving narratives, and locating signs of active rhetoric framing tactics, are difficult to detect and analyze without large-scale automation. This problem can be addressed through the use of natural language understanding technologies. Our goal is to document and discuss methods to efficiently construct, extract, and detect evolving online narratives. The novel contribution of this paper is the formal collation and documentation of such technologies and research areas, as well as extensive discussion on open research challenges and goals in the definition, identification, construction, generation, and representation of online narratives. To our knowledge, there is currently no existing formal documentation that organizes and provides extended discussion on narrative understanding research areas and open challenges.

<a id="p102"></a>
## P102 · Long-Context State-Space Video World Models

- **作者**：Ryan Po; Yotam Nitzan; Richard Zhang; Berlin Chen; Tri Dao; Eli Shechtman; Gordon Wetzstein; Xun Huang
- **时间**：本地版本：2025-05-26（arXiv:2505.20171v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：本地arXiv:2505.20171v1，2025-05-26；对应ICCV 2025正式版见P137
- **论文链接**：[arXiv本地版本 2505.20171v1](https://arxiv.org/abs/2505.20171v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P137](#p137)为同一工作；本条是15页arXiv版本，[P137](#p137)为12页ICCV 2025论文版。

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：15页；SHA-256：`3ae3aef450f64712291ea605ecc1bb56f27130519a13e9b64d17289ce71553ce`

### 中文摘要

以状态空间模型扩展动作条件视频生成的时间记忆，用块级扫描加局部注意力降低长上下文成本。

### 核心贡献

面向因果视频的SSM扫描架构、训练策略及长时空间回访/推理评测。

### 实现边界

低分辨率合成Memory Maze/Minecraft；每帧成本恒定不等于达到实时交互，作者明确当前尚未达到交互帧率，记忆不能有效超出训练上下文。

### Method／方法

空间块级Mamba/SSM扫描处理长历史，局部稠密注意力保持邻帧一致，递归状态支持固定每帧推理成本。

### Results／主要结果

576帧上下文后的224帧推理任务：SSIM0.855、LPIPS0.099、PSNR28.2；192帧上下文因果模型0.839/0.125/27.1；全上下文Transformer0.860/0.089/28.8，仍略好但成本更高。

### Shortcomings／局限与可能不足

【作者】速度未实时、训练上下文外记忆泛化不足、仅合成低分辨率；【解读】固定状态容量可能压缩/遗忘长时细节。

### 证据定位

PDF §4–5、表3 p.6、§6 p.8。

### Abstract

Video diffusion models have recently shown promise for world modeling through autoregressive frame prediction conditioned on actions. However, they struggle to maintain long-term memory due to the high computational cost associated with processing extended sequences in attention layers. To overcome this limitation, we propose a novel architecture leveraging state-space models (SSMs) to extend temporal memory without compromising computational efficiency. Unlike previous approaches that retrofit SSMs for non-causal vision tasks, our method fully exploits the inherent advantages of SSMs in causal sequence modeling. Central to our design is a block-wise SSM scanning scheme, which strategically trades off spatial consistency for extended temporal memory, combined with dense local attention to ensure coherence between consecutive frames. We evaluate the long-term memory capabilities of our model through spatial retrieval and reasoning tasks over extended horizons. Experiments on Memory Maze and Minecraft datasets demonstrate that our approach surpasses baselines in preserving long-range memory, while maintaining practical inference speeds suitable for interactive applications.

<a id="p103"></a>
## P103 · Training Large Language Models to Reason in a Continuous Latent Space

- **作者**：Shibo Hao; Sainbayar Sukhbaatar; DiJia Su; Xian Li; Zhiting Hu; Jason Weston; Yuandong Tian
- **时间**：本地版本：2025-11-03（arXiv:2412.06769v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2412.06769v3（本地署名版）；正式平台另待核验
- **论文链接**：[arXiv本地版本 2412.06769v3](https://arxiv.org/abs/2412.06769v3)
- **项目／代码／数据**：[代码：facebookresearch/coconut](https://github.com/facebookresearch/coconut)
- **版本关系**：[P109](#p109)与本文件SHA-256完全一致；[P026](#p026)为同一工作的较早匿名版，独立保留版本差异。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：18页；SHA-256：`6eb32c71eaa571b727ee95bce20396243fd70dc1ee8a37f91a7de717790d5b46`

### 中文摘要

Coconut把LLM最后隐状态直接作为下一个输入embedding，在连续潜空间进行中间推理，以课程训练逐步取代文本CoT。

### 核心贡献

Chain of Continuous Thought架构及课程，展示某些任务中潜状态可同时容纳备选路径的行为。

### 实现边界

以小模型和合成逻辑/数学任务验证，潜状态类似BFS的观察不等于通用、严格或无限宽搜索；数学表现仍低于文本CoT。

### Method／方法

逐阶段用连续thought替代更多文本步骤，回馈隐状态，再生成文字答案；比较无CoT、iCoT、pause token等。

### Results／主要结果

表1 GSM8K34.1±1.5%对CoT42.9±0.2%，但高于无CoT16.5%；ProsQA97.0对CoT77.5，仍低于iCoT98.2；GSM8K平均生成位置8.2对25.0（包含潜步骤的效率定义须遵循论文）。

### Shortcomings／局限与可能不足

【作者/解读】课程与已有CoT监督重要、规模和任务有限，难解释/检查潜过程；减少显式token不自动等于同比例实际速度提升。

### 证据定位

PDF §3–5、表1 p.9、§5.3–6。

### Abstract

Large language models (LLMs) are restricted to reason in the “language space”, where they typically express the reasoning process with a chain-of-thought (CoT) to solve a complex reasoning problem. However, we argue that language space may not always be optimal for reasoning. For example, most word tokens primarily ensure textual coherence and are not essential for reasoning, while some critical tokens require complex planning and pose huge challenges to LLMs. To explore the potential of LLM reasoning in an unrestricted latent space instead of using natural language, we introduce a new paradigm Coconut (Chain of Continuous Thought). We utilize the last hidden state of the LLM as a representation of the reasoning state (termed “continuous thought”). Rather than decoding this into a word token, we feed it back to the LLM as the subsequent input embedding directly in the continuous space. This latent reasoning paradigm leads to the emergence of an advanced reasoning pattern: the continuous thought can encode multiple alternative next reasoning steps, allowing the model to perform a breadth-first search (BFS) to solve the problem, rather than prematurely committing to a single deterministic path like CoT. Coconut outperforms CoT on certain logical reasoning tasks that require substantial search during planning, and shows a better trade-off between accuracy and efficiency.

<a id="p104"></a>
## P104 · Reasoning with Language Model is Planning with World Model

- **作者**：Shibo Hao; Yi Gu; Haodi Ma; Joshua Jiahua Hong; Zhen Wang; Daisy Zhe Wang; Zhiting Hu
- **时间**：2023年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：EMNLP 2023，2023-12-06—10，pp.8154–8173
- **项目／代码／数据**：[代码（现地址）：maitrix-org/llm-reasoners](https://github.com/maitrix-org/llm-reasoners)；2026-09-16核验现仓库，README列有本论文及其Reasoning-via-Planning实现。

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：20页；SHA-256：`f67d075c889d885db80355f6d398fb2aa6830406340c365140e234af05056dc3`

### 中文摘要

RAP让LLM分别提出推理动作和预测状态变化，再用蒙特卡洛树搜索规划较高价值的推理路径。

### 核心贡献

统一推理为规划，将LLM世界模型和MCTS用于积木规划、数学及逻辑任务。

### 实现边界

世界模型是语言预测状态，不是真实环境模拟器；搜索增加多次模型调用，效果受转移/奖励错误限制。

### Method／方法

定义状态、动作和奖励，MCTS选择/扩展/回传，LLM模拟后果并评估中间收益，输出一个选定计划。

### Results／主要结果

Blocksworld RAP20在2/4/6步任务成功率1.00/0.88/0.42，GPT4-CoT0.50/0.63/0.40；6步优势很小，33%相对提升是特定汇总口径，不代表每项。

### Shortcomings／局限与可能不足

【作者】冻结模型受预训练能力限制；【解读】搜索预算、任务特定提示/奖励及不可靠状态预测影响扩展到开放现实问题。

### 证据定位

PDF §2–4、表1、Limitations p.10。

### Abstract

Large language models (LLMs) have shown remarkable reasoning capabilities, particularly with chain-of-thought (CoT) prompting. However, LLMs sometimes still struggle with problems that are easy for humans, such as generating action plans to achieve given goals in an environment, or performing complex math or logical reasoning. The deficiency stems from the key fact that LLMs lack an internal world model to predict the world state (e.g., environment status, intermediate variable values) and simulate long-term outcomes of actions. This prevents LLMs from performing deliberate planning akin to human brains, which involves exploring alternative reasoning paths, anticipating future states and rewards, and iteratively refining existing reasoning steps. To overcome the limitations, we propose a new LLM reasoning framework, Reasoning vi a Planning (RAP). RAP repurposes the LLM as both a world model and a reasoning agent, and incorporates a principled planning algorithm based on Monte Carlo Tree Search for strategic exploration in the vast reasoning space. During reasoning, the LLM (as agent) incrementally builds a reasoning tree under the guidance of the LLM (as world model) and rewards, and efficiently obtains a high-reward reasoning path with a proper balance between exploration vs. exploitation. We apply RAP to various challenging reasoning problems including plan generation, math reasoning, and logical inference, and demonstrate its superiority over strong baselines. RAP with LLaMA-33B even surpasses CoT with GPT-4, achieving 33% relative improvement in a plan generation setting.1

<a id="p105"></a>
## P105 · New Evaluation, Library, and Analysis of Step-by-Step Reasoning with Large Language Models

- **作者**：Shibo Hao; Yi Gu; Haotian Luo; Tianyang Liu; Xiyan Shao; Xinyuan Wang; Shuhua Xie; Haodi Ma; Adithya Samavedhi; Qiyue Gao; Zhen Wang; Zhiting Hu
- **时间**：本地版本：2024-08-11（arXiv:2404.05221v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：COLM 2024（PDF首页）
- **论文链接**：[arXiv本地版本 2404.05221v2](https://arxiv.org/abs/2404.05221v2)
- **项目／代码／数据**：[项目/演示页面](https://www.llm-reasoners.net/)

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：24页；SHA-256：`e76d095d0dd17d3c7c502650e2f93035e3bc9f9a914df1c72075b73cd9a35f32`

### 中文摘要

提出自动生成任务特定评价标准的AutoRace与统一搜索、奖励、世界模型组件的LLM Reasoners库，系统比较多步推理策略。

### 核心贡献

推理链自动评测、模块化库与搜索因素实验分析。

### 实现边界

AutoRace以GPT4为评判者，自动不等于无误；评判是否符合标准，不保证推理链忠实反映内部过程。

### Method／方法

自动归纳任务错误/规则形成rubric，再评估链；将CoT、ToT、RAP统一为搜索/奖励/转移，研究宽度、深度和提示。

### Results／主要结果

6任务推理链评判平均准确率0.86，SocREval0.82、直接整链判断0.56；搜索奖励可减少“答案对但推理错”，部分任务广度优于深度。

### Shortcomings／局限与可能不足

【解读】评判依赖GPT4及自动rubric质量，搜索比较受预算与提示影响；结论依任务，不能证明所有场景BFS或RAP最优。

### 证据定位

PDF §3–5、表1 p.5、§5.2 p.10。

### Abstract

Generating accurate step-by-step reasoning is essential for Large Language Models (LLMs) to address complex problems and enhance robustness and interpretability. Despite the flux of research on developing advanced reasoning approaches, systematically analyzing the diverse LLMs and reasoning strategies in generating reasoning chains remains a significant challenge. The difficulties stem from the lack of two key elements: (1) an automatic method for evaluating the generated reasoning chains on different tasks, and (2) a unified formalism and implementation of the diverse reasoning approaches for systematic comparison. This paper aims to close the gap: (1) We introduceAutoRace for fully automated reasoning chain evaluation. Existing metrics rely on expensive human annotations or pre-defined LLM prompts not adaptable to different tasks. In contrast, AutoRace automatically creates detailed evaluation criteria tailored for each task, and uses GPT-4 for accurate evaluation following the criteria. (2) We developLLM Reasoners, a library for standardized modular implementation of existing and new reasoning algorithms, under a unified formulation of the search, reward and world model components. With the new evaluation and library, (3) we conduct extensive study of different reasoning approaches (e.g., CoT, ToT, RAP). The analysis reveals interesting findings about different factors contributing to reasoning, including the reward-guidance, breadth-vs-depth in search, world model, and prompt formats, etc.

<a id="p106"></a>
## P106 · Pandora: Towards General World Model with Natural Language Actions and Video States

- **作者**：Jiannan Xiang; Guangyi Liu; Yi Gu; Qiyue Gao; Yuting Ning; Yuheng Zha; Zeyu Feng; Tianhua Tao; Shibo Hao; Yemin Shi; Zhengzhong Liu; Eric P. Xing; Zhiting Hu
- **时间**：本地PDF未明确；未按文件名或PDF制作时间推断。
- **发表平台／版本状态**：2024年研究预印稿；本地未明确正式发表平台
- **项目／代码／数据**：[项目/演示页面](https://world-model.ai)

- **主题**：世界机制与演化
- **PDF版本**：21页；SHA-256：`11a16778bc562baf9abab2aa90a8b8b32c0827fa034d9510da76779a515c401d`

### 中文摘要

把语言自回归模型与视频扩散生成器结合，按自由文本动作连续生成下一段世界状态视频。

### 核心贡献

混合自回归—扩散架构与复用预训练模型的分阶段对齐/指令微调。

### 实现边界

世界状态为视频片段，动作跟随和物理一致性可能失败；通用世界模型是目标，“实时控制”不等于每帧物理实时仿真。

### Method／方法

Vicuna7B接收历史视觉状态与动作，输出条件embedding供DynamiCrafter生成下一段，额外使用上一段末4帧维持连续性。

### Results／主要结果

展示室内外、人类/机器人、2D/3D等跨域可控生成；扩大训练规模后动作跟随改善；§3.4明确展示语义、运动、常识和时序一致性失败。

### Shortcomings／局限与可能不足

【作者】公共视频字幕噪声影响控制，高质量仿真数据域更容易；【解读】主要视觉演示不能证明长程决策可靠性，后续大模型扩展仍为设想。

### 证据定位

PDF §2、§3示例与§3.4 p.14、§5。

### Abstract

World models simulate future states of the world in response to different actions. They facilitate interactive content creation and provides a foundation for grounded, long-horizon reasoning. Current foundation models do not fully meet the capabilities of general world models: large language models (LLMs) are constrained by their reliance on language modality and their limited understanding of the physical world, while video models lack interactive action control over the world simulations. This paper makes a step towards building a general world model by introducing Pandora , a hybrid autoregressive-diffusion model that simulates world states by generating videos and allows real-time control with free-text actions. Pandora achieves domain generality, video consistency, and controllability through large-scale pretraining and instruction tuning. Crucially, Pandora bypasses the cost of training-from-scratch by integrating a pretrained LLM (7B) and a pretrained video model, requiring only additional lightweight finetuning. We illustrate extensive outputs by Pandora across diverse domains (indoor/outdoor, natural/urban, human/robot, 2D/3D, etc.). The results indicate great potential of building stronger general world models with larger-scale training.

<a id="p107"></a>
## P107 · Offline Reinforcement Learning for LLM Multi-step Reasoning

- **作者**：Huaijie Wang; Shibo Hao; Hanze Dong; Shenao Zhang; Yilin Bao; Ziran Yang; Yi Wu
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：Findings of ACL 2025，2025-07-27—08-01，pp.8881–8893
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：13页；SHA-256：`54bc06c0e9082ca1d952447839dd3ba3a39d109632f75bd5f0e1b4818d9458b2`

### 中文摘要

OREO用离线轨迹联合学习策略与价值函数，以soft Bellman方程进行细粒度信用分配，减少对成对偏好数据的依赖。

### 核心贡献

离线推理优化目标，可复用学到的价值函数指导测试时树搜索。

### 实现边界

不需要偏好对不等于不需要带奖励数据；价值模型可直接复用不代表搜索没有额外算力成本。

### Method／方法

最大熵RL下优化策略/价值的Bellman一致性，支持token或响应层次目标、迭代数据更新和价值引导搜索。

### Results／主要结果

Qwen1.5B GSM8K77.3%、MATH52.5%，SFT73.5/47.5；DeepSeekMath7B85.9/49.2；ALFWorld unseen79.1%、seen80.7%，SFT67.2/62.9。

### Shortcomings／局限与可能不足

【作者】部分消融/搜索仅1.5B，任务主要数学与ALFWorld，代码/浏览待验证；【解读】离线分布覆盖与价值误差会限制策略改进。

### 证据定位

PDF §3–5、表1–2 p.7、§7 p.9。

### Abstract

Improving the multi-step reasoning ability of large language models (LLMs) with offline reinforcement learning (RL) is essential for quickly adapting them to complex tasks. While Direct Preference Optimization (DPO) has shown promise in aligning LLMs with human preferences, it is less suitable for multi-step reasoning tasks because (1) DPO relies on paired preference data, which is not readily available for multi-step reasoning tasks, and (2) it treats all tokens uniformly, making it ineffective for credit assignment in multi-step reasoning tasks, which often come with sparse reward. In this work, we propose OREO (Offline REasoning Optimization), an offline RL method for enhancing LLM multi-step reasoning. Building on insights from previous works of maximum entropy reinforcement learning, it jointly learns a policy model and value function by optimizing the soft Bellman Equation. We show in principle that it reduces the need to collect pairwise data and enables better credit assignment. Empirically, OREO surpasses existing offline learning methods on multi-step reasoning benchmarks, including mathematical reasoning tasks (GSM8K, MATH), and embodied agent control (ALFWorld). The approach can be extended to a multi-iteration framework when additional resources are available. Furthermore, the learned value function can be leveraged to guide the tree search for free, which can further boost the performance during test time.

<a id="p108"></a>
## P108 · Flow of Reasoning: Training LLMs for Divergent Problem Solving with Minimal Examples

- **作者**：Anonymous authors（本地双盲稿）
- **时间**：本地匿名稿未注明日期；ICLR 2025是投稿轮次，不作为正式发表时间
- **发表平台／版本状态**：Under review as a conference paper at ICLR 2025；不能据此视为已录用；具体日期不详
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：32页；SHA-256：`938263956875f85c04bb18094173c51bb5da27b8f308b3a4ccec5dc96e60e47b`

### 中文摘要

用GFlowNet式训练让LLM按奖励比例采样不同有效推理路径，在少量问题示例下同时提高正确性和解法多样性。

### 核心贡献

Flow of Reasoning（FOR）把多步推理表示为DAG上的概率流，优化多样高奖励轨迹。

### 实现边界

“15示例”是部分任务的问题数，不代表只有15次训练交互；依赖任务奖励/模拟器，创造性是任务定义的解法多样性指标。

### Method／方法

以Markov推理状态与路径奖励构造流匹配/轨迹训练，从有限问题反复探索高质量路径并微调LLM。

### Results／主要结果

五类谜题评测；Rubik四步183题、15训练示例时FOR准确率10.87±1.18%，SFT1.82%，XoT4.92%；FOR多样性1.29、创造性82.61%。Game24仍落后GPT4o/o1-mini等更强基础模型。

### Shortcomings／局限与可能不足

【解读】奖励设计和有限可验证环境限制一般开放创意任务；魔方绝对成功率仍低，更多样不等同更正确或更有实际创新价值。

### 证据定位

PDF §3–4、表1–3、§4.4 p.8。

### Abstract

The ability to generate diverse solutions to a given problem is a hallmark of human creativity. This divergent reasoning is also crucial for machines, enhancing their robustness and enabling them to assist humans in many applications such as scientific discovery. However, existing approaches to multi-step reasoning with large language models (LLMs) have mostly focused only on reasoning accuracy, without further discovering more diverse valid solutions. For example, supervised fine-tuning can improve LLM reasoning quality, but requires extensive supervised data to capture the full range of possible solutions. Reinforcement learning aims to find limited highest-reward solutions while neglecting the solution diversity. To fill this gap, we propose Flow of Reasoning (FOR), an efficient diversity-seeking LLM finetuning method aimed at improving reasoning quality and diversity with minimal data. FOR formulates multi-step LLM reasoning as a Markovian flow on a DAG-structured reasoning graph. This formulation allows us to incorporate and adapt principled GFlowNet approaches, for finetuning LLMs to sample diverse reasoning paths with probabilities proportional to the (unnormalized) reward of target problems. Extensive experiments show that, with limited training examples (e.g., 15 examples), FOR enables the discovery of diverse, creative, high-quality solutions, greatly outperforming a wide range of existing inference and training methods across five challenging puzzle-solving tasks, including BlocksWorld (embodied reasoning), Game24 (math puzzle solving), Rubik’s Cube (spatial reasoning), 1D-ARC (abstraction reasoning), and PrOntoQA (logical reasoning).

<a id="p110"></a>
## P110 · Understanding the Sources of Uncertainty for Large Language and Multimodal Models

- **作者**：Ziran Yang; Shibo Hao; Hao Sun; Lai Jiang; Qiyue Gao; Yian Ma; Zhiting Hu
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICLR 2025 Workshop：Quantify Uncertainty and Hallucination in Foundation Models: The Next Frontier in Reliable AI（首页）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：20页；SHA-256：`2cd60cc497dacba53d97c7c56ccb153e879d408445af64b57ed24429940e268c`

### 中文摘要

将模型输出不确定性按提示措辞、上下文和视觉预处理等因素分解，识别与错误率更相关的分量以用于幻觉检测和自训练筛选。

### 核心贡献

超出传统epistemic/aleatoric二分的信息论分解框架及effective calibrator概念。

### 实现边界

分量含义依赖选定扰动因素与采样分布；与错误相关不意味着识别真正因果来源，也不保证概率校准。

### Method／方法

用条件熵与互信息逐层分解总熵，对提示/输入变体采样，比较分量与错误关联；用于VQA及SVAMP自训练。

### Results／主要结果

部分分量比总不确定性更能指示幻觉；在视觉QA和数学推理展示检测/筛选收益；SVAMP采用Gemma2-9B、6种实体改写和6种CoT模板，结论受该扰动空间约束。

### Shortcomings／局限与可能不足

【解读】需多次查询和语义等价改写，改写错误可污染分解；有效分量跨域/模型是否稳定尚无通用保证。

### 证据定位

PDF §2、表1、§3–4 pp.6–9。

### Abstract

Understanding and quantifying uncertainty in large model predictions is critical for their safe and trustworthy deployment. However, existing methods that estimate the overall prediction uncertainty often fail due to miscalibration like model overconfidence. Uncertainty decomposition provides a way to focus on some specific parts in total uncertainty, removing those unrelated components. Traditional uncertainty decomposition into epistemic (model-related) and aleatoric (data-related) components is insufficient for current model usage, as additional factors like prompt phrasing and context significantly influence the model’s predictions and add the source of uncertainty. We introduce a unified uncertainty decomposition framework that systematically separates uncertainty contributed by various factors such as prompting, context, and preprocessing of multimodal inputs. By quantifying each component’s uncertainty, our approach identifies which uncertainty terms are well-correlated with the model’s hallucination rates, thereby enhancing hallucination detection and model improvement. We validate our framework through applications in visual question answering and math reasoning, demonstrating that effective uncertainty components can serve as metrics for hallucination detection and improve model performance through self-training. Grounded in information theory and highly extensible, our framework provides a novel perspective on uncertainty decomposition in large language and multimodal models, offering valuable insights for future research.

<a id="p111"></a>
## P111 · CocoaBench: Evaluating Unified Digital Agents in the Wild

- **作者**：CocoaBench Team; Shibo Hao; Zhining Zhang; Zhiqi Liang; Tianyang Liu; Yuheng Zha; Qiyue Gao; Jixuan Chen; Zilong Wang; Zhoujun Cheng; Haoxiang Zhang; Junli Wang; Hexi Jin; Boyuan Zheng; Kun Zhou; Yu Wang; Feng Yao; Licheng Liu; Yijiang Li; Zhifei Li; Zhengtao Han; Pracha Promthaw; Tommaso Cerruti; Xiaohan Fu; Ziqiao Ma; Jingbo Shang; Lianhui Qin; Julian McAuley; Eric P. Xing; Zhengzhong Liu; Rupesh Kumar Srivastava; Zhiting Hu
- **时间**：本地版本：2026-04-14（arXiv:2604.11201v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：Preprint, Under review；arXiv:2604.11201v2
- **论文链接**：[arXiv本地版本 2604.11201v2](https://arxiv.org/abs/2604.11201v2)
- **项目／代码／数据**：[项目/演示页面](https://cocoabench.github.io/)

- **主题**：XR与人机协作
- **PDF版本**：26页；SHA-256：`2832e5b0a617129a2f6de538b03da95a3b71e29e4f4d9fdce9996040d7423fe4`

### 中文摘要

用同时需要视觉、搜索和编程的长流程任务评估统一数字代理，以最终输出自动评测，并提供轻量共享Cocoa-Agent框架。

### 核心贡献

CocoaBench跨能力组合任务及控制模型骨干差异的统一实验支架。

### 实现边界

完整代理系统和共享框架的成绩不可混为纯模型能力；“in the wild”仍是人工设计、有自动验证器的任务样本。

### Method／方法

只给任务说明，以最终产物函数判定成功；分别测完整系统和相同Cocoa-Agent下的模型，分析规划/执行/视觉错误。

### Results／主要结果

GPT5.4在Codex/OpenClaw中45.1%，共享Cocoa-Agent36.6%；ClaudeSonnet4.6在OpenClaw34.0%、ClaudeCode25.5%、Cocoa-Agent15.7%，显示框架影响显著。

### Shortcomings／局限与可能不足

【解读】评估函数覆盖范围、基础设施与外部环境变化影响可复现性，成功率不能代替所有产物质量；所测任务离可靠全能代理仍有差距。

### 证据定位

PDF §3–5、图4、§6。

### Abstract

LLM agents now perform strongly in software engineering, deep research, GUI automation, and various other applications, while recent agent scaffolds and models are increasingly integrating these capabilities into unified systems. Yet, most evaluations still test these capabilities in isolation, which leaves a gap for more diverse use cases that require agents to combine different capabilities. We introduce COCOABENCH, a benchmark for unified digital agents built from human-designed, long-horizon tasks that require flexible composition ofvision,search, andcoding. Tasks are specified only by an instruction and an automatic evaluation function over the final output, enabling reliable and scalable evaluation across diverse agent infrastructures. We also present COCOA-AGENT, a lightweight shared scaffold for controlled comparison across model backbones. Experiments show that current agents remain far from reliable on COCOABENCH, with the best evaluated system achieving only 45.1% success rate. Our analysis further points to substantial room for improvement in reasoning and planning, tool use and execution, and visual grounding.1

<a id="p112"></a>
## P112 · Vision-G1: Towards General Reasoning Vision-Language Models via Reinforcement Learning

- **作者**：Yuheng Zha, Kun Zhou, Yujia Wu, Yushu Wang, Jie Feng, Zhi Xu, Shibo Hao, Zhengzhong Liu, Eric P. Xing, Zhiting Hu
- **时间**：2026-03-14正式上线（AAAI期刊式论文集记录）
- **发表平台／版本状态**：AAAI 2026，40(33):28131–28139；正式上线2026-03-14，DOI 10.1609/aaai.v40i33.40039（AAAI官方核验）。 [AAAI官方论文页](https://ojs.aaai.org/index.php/AAAI/article/view/40039)
- **论文链接**：[DOI正式记录](https://doi.org/10.1609/aaai.v40i33.40039)
- **项目／代码／数据**：[代码：yuh-zha/Vision-G1](https://github.com/yuh-zha/Vision-G1)

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：9页；SHA-256：`244c5846a1bf20d1a4a57c0c793e431a075dbeaa5279de26c5b3664d63cb9753`

### 中文摘要

汇集多域视觉推理可验证奖励数据，结合影响函数筛选与难度课程，多轮RL训练通用视觉推理模型。

### 核心贡献

46数据集、5域13维度的RL-ready数据及Vision-G1-7B训练方案。

### 实现边界

“general”限于涵盖的图像任务；视频和3D是未来方向；正文对评测数量有9/18/17三种表述，按具体表格任务阅读。

### Method／方法

统一题目/奖励格式，影响函数过滤低价值样本，再按中等难度及类别平衡进行多轮GRPO。

### Results／主要结果

数学表2平均42.1%，基础Qwen2.5VL-7B39.0，但Vision-R1-7B42.5%、GPT4o45.7%更高；因此不能将摘要领先描述套到每个数学指标。跨综合/专业任务另有收益。

### Shortcomings／局限与可能不足

【作者/解读】数据/奖励质量、任务均衡及影响近似影响结果；数据混合收益不等于全面推理泛化，需防跨基准数据重叠。

### 证据定位

PDF Approach、Main Results、表1–3、Conclusion p.7；指标例外见表2。

### Abstract

Recent vision-language models (VLMs) show strong reasoning capabilities through training with reinforcement learning from verifiable rewards (RLVR). Despite their impressive capabilities, current VLMs focus on a limited range of reasoning tasks, such as mathematical and logical reasoning, due to the lack of readily available verifiable reward data in broader domains. As a result, these models struggle to generalize their reasoning abilities to the wide variety of challenges encountered in real-world environments. To address this limitation, we collect and assemble a comprehensive RL-ready visual reasoning training dataset encompassing 46 datasets across 13 dimensions of 5 domains, covering a wide range of realistic scenarios such as infographic reasoning, mathematical reasoning, spatial reasoning, and general science reasoning. Based on this dataset, we propose an influence function-based data filtering strategy and a multi-round data curriculum method to iteratively strengthen general visual reasoning abilities. Using this approach, we train a general reasoning VLM, namely Vision-G1. Our 7B model achieves state-of-the-art performance across nine visual reasoning benchmarks, surpassing similar-sized VLMs and even GPT-4o and Gemini-1.5 Flash. Code — https://github.com/yuh-zha/Vision-G1

<a id="p113"></a>
## P113 · Emergence of Superposition: Unveiling the Training Dynamics of Chain of Continuous Thought

- **作者**：Hanlin Zhu; Shibo Hao; Zhiting Hu; Jiantao Jiao; Stuart Russell; Yuandong Tian
- **时间**：本地版本：2026-03-01（arXiv:2509.23365v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICLR 2026（PDF首页）；arXiv:2509.23365v3
- **论文链接**：[arXiv本地版本 2509.23365v3](https://arxiv.org/abs/2509.23365v3)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：32页；SHA-256：`0618e8beba581d69a8b8483fc36d8930855935373137d66090116eebb07bb01e`

### 中文摘要

分析连续CoT隐式并行搜索如何在训练中形成，针对简化两层Transformer的有向图可达任务刻画关键注意力logit动态。

### 核心贡献

在思考生成和答案预测两阶段分析index-matching logit先增长再有界，从而保留多个可能前沿的理论机制。

### 实现边界

定理依赖简化两层模型、任务结构与对称等假设，不适用于任意大模型训练；superposition是向量多路径编码，不是量子计算。

### Method／方法

推导梯度训练下局部搜索logit变化，用课程训练跟踪注意力及潜状态，检验理论预测。

### Results／主要结果

受控图任务测试准确率96.2%，训练logit轨迹与有界假设一致；部分候选提升通路随设置/随机种子改变，并不总经同一&lt;R&gt; token。

### Shortcomings／局限与可能不足

【解读】简化参数化和合成图数据限制一般性，多层大模型、预训练/不同优化器的机制仍需检验。

### 证据定位

PDF §3–5、§5训练细节p.9、§6及附录E。

### Abstract

Previous work shows that the chain of continuous thought (continuous CoT) improves the reasoning capability of large language models (LLMs) by enabling implicit parallel thinking, and a subsequent work provided theoretical insight by showing that a two-layer transformer equipped with continuous CoT can efficiently solve directed graph reachability by maintaining a superposition of multiple reasoning traces in the continuous thought. However, it remains unclear how the superposition mechanism is naturally learned from gradient-based training methods. To fill this gap, we theoretically analyze the training dynamics of a simplified two-layer transformer on the directed graph reachability problem to unveil how the superposition mechanism emerges during training in two training stages – (i) athought-generationstage that autoregressively expands the continuous thought, and (ii) apredictionstage that converts the thought into the final answer. Our analysis reveals that during training using continuous thought, the index-matching logit, an important quantity which reflects the strength of the model’s local search ability, will first increase and then remain bounded under mild assumptions. The bounded index-matching logit effectively balances exploration and exploitation during the reasoning process: the model will exploit local problem structures to identify plausible search traces, and assign comparable weights to multiple such traces to explore when it is uncertain about which solution is correct, which results in superposition. Our experimental results tracking the growth of logits further validate our theory.

<a id="p114"></a>
## P114 · LLM Pretraining with Continuous Concepts

- **作者**：Jihoon Tack; Jack Lanchantin; Jane Yu; Andrew Cohen; Ilia Kulikov; Janice Lan; Shibo Hao; Yuandong Tian; Jason Weston; Xian Li
- **时间**：本地版本：2025-02-12（arXiv:2502.08524v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICLR 2026（官方会议论文列表核验）；本地为2025-02-13稿面日期的早期预印版，arXiv v1为2025-02-12。 [ICLR官方记录](https://iclr.cc/virtual/2026/papers.html)；[OpenReview稿件](https://openreview.net/pdf?id=P7RwEIiCyh)
- **论文链接**：[arXiv本地版本 2502.08524v1](https://arxiv.org/abs/2502.08524v1)
- **项目／代码／数据**：[代码：facebookresearch/RAM/tree/main/projects/cocomix](https://github.com/facebookresearch/RAM/tree/main/projects/cocomix)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：17页；SHA-256：`02442c5e0d6a0156893b45222b6d2ce4089a8eb5414986bac6760a7f82781f59`

### 中文摘要

CoCoMix在下一token预训练之外预测来自稀疏自编码器的连续概念，并与token表示交错输入，以提高样本效率及一定程度的可控性。

### 核心贡献

连续概念预测+混合的端到端预训练方案，比较NTP、蒸馏和pause tokens。

### 实现边界

需要预训练模型/SAE提供概念目标；概念可解释性依赖SAE，不能保证全模型透明；主要模型规模69M–1.38B。

### Method／方法

从教师隐状态经SAE提取稀疏概念，学生同时预测token和概念，将压缩概念向量插入隐状态流。

### Results／主要结果

200B token实验中1.38B模型平均下游准确率49.7对NTP48.7、KD49.1%；报告达到NTP同等性能所需token减少21.5%；124M概念教师也可帮助更大模型。

### Shortcomings／局限与可能不足

【解读】总体提升温和且不保证逐任务领先；教师概念提取有额外成本，token节省不直接等于总训练算力同比下降。

### 证据定位

PDF §2–3、表1 p.6、§5；首页日期。

### Abstract

Next token prediction has been the standard training objective used in large language model pretraining. Representations are learned as a result of optimizing for token-level perplexity. We propose Continuous Concept Mixing (CoCoMix), a novel pretraining framework that combines discrete next token prediction with continuous concepts. Specifically, CoCoMix predicts “continuous concepts” learned from a pretrained sparse autoencoder and mixes them into the model’s hidden state by interleaving with token hidden representations. Through experiments on multiple benchmarks, including language modeling and downstream reasoning tasks, we show that CoCoMix is more sample efficient and consistently outperforms standard next token prediction, knowledge distillation and inserting pause tokens. We find that combining both concept learning and interleaving in an end-to-end framework is critical to performance gains. Furthermore, CoCoMix enhances interpretability and steerability by allowing direct inspection and modification of the predicted concept, offering a transparent way to guide the model’s internal reasoning process.

<a id="p115"></a>
## P115 · ToolkenGPT: Augmenting Frozen Language Models with Massive Tools via Tool Embeddings

- **作者**：Shibo Hao; Tianyang Liu; Zhen Wang; Zhiting Hu
- **时间**：2023年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2023（论文版）
- **项目／代码／数据**：[代码：Ber666/ToolkenGPT](https://github.com/Ber666/ToolkenGPT)

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：25页；SHA-256：`052e79422c205ba6f4155a8f06c22ad1766da376e8077be3a75cf45c7efe88e3`

### 中文摘要

把工具当作词表里的特殊token，仅学习工具embedding，使冻结LLM能选择大量工具，再通过提示生成参数并执行。

### 核心贡献

toolken表示及低参数工具学习，支持扩展工具集合并利用示范数据。

### 实现边界

冻结骨干不等于无训练；每个新工具仍需embedding学习/示范，参数生成及执行错误未被消除。

### Method／方法

把工具embedding矩阵拼到输出词表，联合选择文字/工具；触发工具后切参数提示，执行结果回填上下文。

### Results／主要结果

GSM8K-XL（568题）ToolkenGPT33%对ReAct32%；FuncQA13工具单跳73%对57%，多跳15%对6%，多跳绝对成功率仍低；另有知识库与具身规划实验。

### Shortcomings／局限与可能不足

【解读】工具数量扩展的选择质量依赖演示分布，复杂组合与参数泛化困难；不是任意未知工具零样本使用保证。

### 证据定位

PDF §3–4、表2 p.6、§5。

### Abstract

Augmenting large language models (LLMs) with external tools has emerged as a promising approach to solving complex problems. However, traditional methods, which fine-tune LLMs with tool demonstration data, can be both costly and restricted to a predefined set of tools. Recent in-context learning paradigm alleviates these issues, but the limited context length only allows for a few shots of demonstrations, leading to suboptimal understandings of the tools. Moreover, when there are numerous tools to choose from, in-context learning could completely fail to work. In this paper, we propose an alternative approach, ToolkenGPT, which combines the benefits of both sides. Our approach represents each tool as a token (“toolken”) and learns an embedding for it, enabling tool calls in the same way as generating a regular word token. Once a toolken is triggered, the LLM is prompted to complete arguments for the tool to execute. ToolkenGPT offers the flexibility to plug in an arbitrary number of tools by expanding the set of toolkens on the fly. In addition, it improves tool use by allowing extensive demonstration data for learning the toolken embeddings. In diverse domains, including numerical reasoning, knowledge-based question answering, and embodied plan generation, our approach effectively augments LLMs with tools and substantially outperforms various latest baselines. ToolkenGPT demonstrates the promising ability to use relevant tools from a large tool set in complex scenarios.1

<a id="p116"></a>
## P116 · Reasoning by Superposition: A Theoretical Perspective on Chain of Continuous Thought

- **作者**：Hanlin Zhu; Shibo Hao; Zhiting Hu; Jiantao Jiao; Stuart Russell; Yuandong Tian
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2025（论文版）
- **项目／代码／数据**：[代码：Ber666/reasoning-by-superposition](https://github.com/Ber666/reasoning-by-superposition)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：33页；SHA-256：`d40150700bdbfbb721e65bc728c473fc266d716cba5479f5e1387d5a88870849`

### 中文摘要

构造两层Transformer在连续CoT中并行编码多个搜索前沿，以图直径D步解决有向图可达，并用训练实验观察相似潜表示。

### 核心贡献

连续thought并行BFS的表达能力构造及经验对应分析。

### 实现边界

与离散CoT的O(n²)是对比已有最好构造，不是已证明离散CoT必需Ω(n²)；严格分离的下界明确留作未来。

### Method／方法

在连续向量中叠加搜索前沿，用两层注意力迭代扩展；ProsQA合成子集上课程训练与潜态/注意力分析。

### Results／主要结果

2层Coconut在所评ProsQA接近满分，CoT/无CoT约75%，12层CoT约83%；理论需D个连续步骤，条件和数值精度按构造。

### Shortcomings／局限与可能不足

【作者/解读】离散CoT下界未建立，结论局限图可达和构造假设；训练动力学与更广任务的充分解释仍需研究（P113进一步分析）。

### 证据定位

PDF 定理及§3–4、§5图4、§6 p.10。

### Abstract

Large Language Models (LLMs) have demonstrated remarkable performance in many applications, including challenging reasoning problems via chain-ofthought (CoT) techniques that generate “thinking tokens” before answering the questions. While existing theoretical works demonstrate that CoT with discrete tokens boosts the capability of LLMs, recent work on continuous CoT lacks a theoretical understanding of why it outperforms discrete counterparts in various reasoning tasks, such as directed graph reachability, a fundamental graph reasoning problem that includes many practical domain applications as special cases. In this paper, we prove that a two-layer transformer with D steps of continuous CoT can solve the directed graph reachability problem, whereD is the diameter of the graph, while the best known result of constant-depth transformers with discrete CoT requires O(n2) decoding steps where n is the number of vertices (D &lt; n). In our construction, each continuous thought vector is a superposition state that encodes multiple search frontiers simultaneously (i.e., parallel breadth-first search (BFS)), while discrete CoT must choose a single path sampled from the superposition state, which leads to a sequential search that requires many more steps and may be trapped in local solutions. We also performed extensive experiments to verify that our theoretical construction aligns well with the empirical solution obtained via training dynamics. Notably, encoding of multiple search frontiers as a superposition state automatically emerges in training continuous CoT, without explicit supervision to guide the model to explore multiple paths simultaneously. Our code is available at https://github.com/Ber666/reasoning-by-superposition .

<a id="p117"></a>
## P117 · Revisiting Reinforcement Learning for LLM Reasoning from A Cross-Domain Perspective

- **作者**：Zhoujun Cheng; Shibo Hao; Tianyang Liu; Fan Zhou; Yutao Xie; Feng Yao; Yuexin Bian; Yonghao Zhuang; Nilabjo Dey; Yuheng Zha; Yi Gu; Kun Zhou; Yuqi Wang; Yuan Li; Richard Fan; Jianshu She; Chengqian Gao; Abulhair Saparov; Haonan Li; Taylor W. Killian; Mikhail Yurochkin; Zhengzhong Liu; Eric P. Xing; Zhiting Hu
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2025 Datasets and Benchmarks Track（论文版）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：摘要/§4.2称32B比ORZ提升7.8，但表3为52.68−46.95=5.73个百分点；7.80对应SimpleRL32B44.88。以表格为准。

- **主题**：世界机制与演化、XR与人机协作、AI方法与评测
- **PDF版本**：21页；SHA-256：`47973c5ee52be94e5c210f58fa1f1df7f9a775538d9752decff760f7ba8d31e5`

### 中文摘要

构建92K条六域可验证推理数据GURU，研究RL跨域迁移及难度影响，并训练7B/32B多域推理模型。

### 核心贡献

数学、代码、科学、逻辑、仿真、表格数据与验证器，跨域训练分析和17任务评估套件。

### 实现边界

只覆盖可构造验证奖励的领域；混合训练并非每项都优于专用模型，难源域还可能负迁移到简单任务。

### Method／方法

来源清洗去重、领域/难度过滤，Qwen2.5-Base上GRPO训练，控制域混合和难度研究迁移。

### Results／主要结果

表3平均GURU7B41.17对ORZ7B33.90（+7.27）；32B52.68对ORZ46.95（+5.73）。32B AIME24为32.29，低于ORZ47.50，说明总体更均衡不等于数学全面领先。

### Shortcomings／局限与可能不足

【解读】任务平均权重、验证器可靠性和混合比例影响结论，数据规模/在线混合未充分研究；摘要提升数值存在口径冲突。

### 证据定位

PDF §2–4、表3 p.8、§6。

### Abstract

Reinforcement learning (RL) has shown promise in enhancing large language model (LLM) reasoning, yet progress towards broader capabilities is limited by the availability of high-quality, multi-domain datasets. This work introduces GURU, a 92K RL-for-reasoning dataset designed to address this gap, covering six reasoning domains: Math, Code, Science, Logic, Simulation, and Tabular, each with corresponding verifiers. We build GURU via a careful data-curation pipeline, including sourcing, deduplication, reward design, and domain-specific and difficulty-based filtering. With GURU, we present a systematic investigation of cross-domain RL generalization, and reveal several key aspects affecting crossdomain transferability. We further train two models GURU-7B and GURU-32B purely with RL on our curated data and observe largely improved performance over leading open RL reasoning model baselines, with gains of 7.3% and 7.8% respectively on an extensive 17-task, six-domain evaluation suite. We are releasing our dataset, code, and evaluation suite to the community, aiming to support further research and development of more general RL-enhanced reasoning models.

<a id="p118"></a>
## P118 · Calibrating Reasoning in Language Models with Internal Consistency

- **作者**：Zhihui Xie; Jizhou Guo; Tong Yu; Shuai Li
- **时间**：本地版本：2024-12-05（arXiv:2405.18711v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：NeurIPS 2024 Main Conference Track（官方论文集核验）；本地arXiv v2为2024-12-05。 [NeurIPS官方论文集](https://proceedings.neurips.cc/paper_files/paper/2024/hash/d037fd021c9aace128b8ce25001cdb6c-Abstract-Conference.html)
- **论文链接**：[arXiv本地版本 2405.18711v2](https://arxiv.org/abs/2405.18711v2)
- **项目／代码／数据**：[代码：zhxieml/internal-consistency](https://github.com/zhxieml/internal-consistency)

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：23页；SHA-256：`ab6abe3fc5cdc39c45c1f877d6426ca7303d79f918e3f8d84f9ca2e84d783661`

### 中文摘要

解码中间层对答案的潜在预测，以层间一致性衡量置信度，并优先选择内部更一致的推理路径。

### 核心贡献

Internal consistency无需训练置信信号、推理路径加权与attention/FFN跨层分析。

### 实现边界

需要隐状态访问和可定义答案的任务；内部一致不保证正确，也不是标准概率意义的普遍校准保证。

### Method／方法

用中间层潜预测与末层比较，计算一致性；对多条CoT/L2M路径加权，提高更可信答案的权重。

### Results／主要结果

跨模型/数据发现错误CoT常有更低内部一致性，加权后推理表现改善；实验使用二分类50/50平衡的calibrated accuracy，不能当作原始类别比例下准确率。

### Shortcomings／局限与可能不足

【作者】主要decoder-only、基础CoT，其他架构/推理方式待扩展；【解读】需要多路径采样，任务格式及层选择影响可靠性。

### 证据定位

PDF §3–4、§4.1–3、§6 p.10。

### Abstract

Large language models (LLMs) have demonstrated impressive capabilities in various reasoning tasks, aided by techniques like chain-of-thought prompting that elicits verbalized reasoning. However, LLMs often generate text with obvious mistakes and contradictions, raising doubts about their ability to robustly process and utilize generated rationales. In this work, we investigate reasoning in LLMs through the lens of internal representations, focusing on how these representations are influenced by generated rationales. Our preliminary analysis reveals that while generated rationales improve answer accuracy, inconsistencies emerge between the model’s internal representations in middle layers and those in final layers, potentially undermining the reliability of their reasoning processes. To address this, we propose internal consistency as a measure of the model’s confidence by examining the agreement of latent predictions decoded from intermediate layers. Extensive empirical studies across different models and datasets demonstrate that internal consistency effectively distinguishes between correct and incorrect reasoning paths. Motivated by this, we propose a new approach to calibrate reasoning by up-weighting reasoning paths with high internal consistency, resulting in a significant boost in reasoning performance. Further analysis uncovers distinct patterns in attention and feed-forward modules across layers, providing insights into the emergence of internal inconsistency. In summary, our results demonstrate the potential of using internal representations for self-evaluation of LLMs. Our code is available at github.com/zhxieml/internal-consistency.

<a id="p119"></a>
## P119 · Reasoning Models Know When They’re Right: Probing Hidden States for Self-Verification

- **作者**：Anqi Zhang; Yulin Chen; Jane Pan; Chen Zhao; Aurojit Panda; Jinyang Li; He He
- **时间**：本地版本：2025-04-07（arXiv:2504.05419v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：COLM 2025正式论文已核实；本地仍为2025-04-07的arXiv v1，首页Preprint, Under review反映当时状态。以下实验数字按本地稿保留。[COLM正式论文](https://openreview.net/forum?id=O6I0Av7683)
- **论文链接**：[arXiv本地版本 2504.05419v1](https://arxiv.org/abs/2504.05419v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：18页；SHA-256：`c32a216f1eb0d49db8a1c6873e465b0a52e3c67fb15dc3961361cc6edf700504`

### 中文摘要

训练隐状态探针识别中间答案正确性，发现答案形成前已有可预测信号，并用高置信提前结束降低过度推理。

### 核心贡献

中间/未来答案正确性探测、校准分析和动态早退出。

### 实现边界

需要带正确性标签训练探针、访问隐状态；标题“知道”指可解码统计信号，并非意识或无监督自证。

### Method／方法

收集中间答案隐状态与标签，训练MLP探针，验证集调参/校准，推理中达到阈值时退出并输出答案。

### Results／主要结果

阈值0.85约节省24%token，准确率88.2对不退出88.6%，是近似保持并非完全相等；0.9阈值节省19%，准确率同为88.6%；同预算胜固定退出约5个百分点。

### Shortcomings／局限与可能不足

【解读】探针迁移/校准可能随模型任务改变；阈值越低越可能提前接受错误，token减少不必然线性缩短端到端延迟。

### 证据定位

PDF §3–5、§5.2 p.8、图5。

### Abstract

Reasoning models have achieved remarkable performance on tasks like math and logical reasoning thanks to their ability to search during reasoning. However, they still suffer from overthinking, often performing unnecessary reasoning steps even after reaching the correct answer. This raises the question: can models evaluate the correctness of their intermediate answers during reasoning? In this work, we study whether reasoning models encode information about answer correctness through probing the model’s hidden states. The resulting probe can verify intermediate answers with high accuracy and produces highly calibrated scores. Additionally, we find models’ hidden states encode correctness of future answers, enabling early prediction of the correctness before the intermediate answer is fully formulated. We then use the probe as a verifier to decide whether to exit reasoning at intermediate answers during inference, reducing the number of inference tokens by 24% without compromising performance. These findings confirm that reasoning models do encode a notion of correctness yet fail to exploit it, revealing substantial untapped potential to enhance their efficiency.

<a id="p120"></a>
## P120 · Imagine This! Scripts to Compositions to Videos

- **作者**：Tanmay Gupta; Dustin Schwenk; Ali Farhadi; Derek Hoiem; Aniruddha Kembhavi
- **时间**：本地版本：2018-04-10（arXiv:1804.03608v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ECCV 2018，pp.598–613（官方ECVA核验）；文件名中的cvpr有误。 [ECVA官方论文页](https://www.ecva.net/papers/eccv_2018/papers_ECCV/html/Tanmay_Gupta_Imagine_This_Scripts_ECCV_2018_paper.php)
- **论文链接**：[arXiv本地版本 1804.03608v1](https://arxiv.org/abs/1804.03608v1)
- **项目／代码／数据**：[作者演示视频](https://youtu.be/688Vv86n0z8)
- **版本关系**：发表会议以ECCV为准，不采用文件名CVPR。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：22页；SHA-256：`aeae85082dd70d12d6744a5045231e6a74fa98947a26e4fc29249b04339f83e9`

### 中文摘要

CRAFT先从文本预测实体的时空布局，再检索视频实体片段并合成视频，利用组合式表示提高语义匹配和视觉一致性。

### 核心贡献

Composition/Retrieval/Fusion网络、布局与外观联合建模及超过25,000视频的Flintstones标注数据。

### 实现边界

主要动画域和已有视频片段重组，不能任意合成库中不存在的对象/运动；不同模块评测有使用前序真值布局/外观的条件。

### Method／方法

逐实体布局预测、联合文本/场景/位置检索，triplet与辅助分类学习检索空间，融合时空片段。

### Results／主要结果

在语义名词/形容词/动词召回、布局与人评视觉质量上优于直接像素生成基线；可组合未见描述并转移到无字幕视频库。

### Shortcomings／局限与可能不足

【解读】依赖精细实体标注与候选片段覆盖，检索组合易产生接缝/动态不一致；动画证据不能外推写实长视频。

### 证据定位

PDF §3–5、表1–3与§5.3；ECVA用于会议信息。

### Abstract

Imagining a scene described in natural language with realistic layout and appearance of entities is the ultimate test of spatial, visual, and semantic world knowledge. Towards this goal, we present the Composition, Retrieval and Fusion Network (Craft), a model capable of learning this knowledge from video-caption data and applying it while generating videos from novel captions. Craft explicitly predicts a temporal-layout of mentioned entities (characters and objects), retrieves spatio-temporal entity segments from a video database and fuses them to generate scene videos. Our contributions include sequential training of components of Craft while jointly modeling layout and appearances, and losses that encourage learning compositional representations for retrieval. We evaluate Craft on semantic fidelity to caption, composition consistency, and visual quality . Craft outperforms direct pixel generation approaches and generalizes well to unseen captions and to unseen video databases with no text annotations. We demonstrate Craft on Flintstones, a new richly annotated video-caption dataset with over 25000 videos. For a glimpse of videos generated by Craft, see https://youtu.be/688Vv86n0z8.

<a id="p121"></a>
## P121 · World Models

- **作者**：David Ha, Jürgen Schmidhuber
- **时间**：本地版本：2018-05-09（arXiv:1803.10122v4）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：2018年World Models研究稿及互动论文网站；不与后续改题版本混合
- **论文链接**：[arXiv本地版本 1803.10122v4](https://arxiv.org/abs/1803.10122v4)
- **项目／代码／数据**：[项目/演示页面](https://worldmodels.github.io)

- **主题**：世界机制与演化
- **PDF版本**：21页；SHA-256：`b0c1e30aab53efd28ddf61d661f680150918d4d03b77bae62bc52d62dbd76cce`

### 中文摘要

用生成式模型压缩视觉并预测时间动态，训练小控制器，展示在学到的梦境中学习策略后迁移回真实游戏环境。

### 核心贡献

VAE视觉模型、MDN-RNN记忆模型和简洁控制器的模块化世界模型，区分表征学习与控制优化。

### 实现边界

CarRacing和VizDoom等游戏；CarRacing控制器并非全部仅在梦中训练，梦中转移主要由Doom实验展示；不能保证学到完整物理因果结构。

### Method／方法

无监督学习V和M，控制器用z及RNN隐状态选动作，由进化策略优化；在随机梦境模型中训练并调温防利用模型缺陷。

### Results／主要结果

CarRacing100随机试验906±21，视觉表示单独632±251、加隐藏层788±141；展示Doom梦境训练后的真实环境迁移。

### Shortcomings／局限与可能不足

【作者/解读】代理可利用世界模型错误，温度和数据覆盖影响转移；简单低分辨率游戏与独立模块训练不代表普遍开放环境控制。

### 证据定位

PDF §3表1、§4梦境实验及讨论。

### Abstract

We explore building generative neural network models of popular reinforcement learning environments. Our world model can be trained quickly in an unsupervised manner to learn a compressed spatial and temporal representation of the environment. By using features extracted from the world model as inputs to an agent, we can train a very compact and simple policy that can solve the required task. We can even train our agent entirely inside of its own hallucinated dream generated by its world model, and transfer this policy back into the actual environment. An interactive version of this paper is available at https://worldmodels.github.io

<a id="p122"></a>
## P122 · Phenaki: Variable Length Video Generation from Open Domain Textual Descriptions

- **作者**：Ruben Villegas; Mohammad Babaeizadeh; Pieter-Jan Kindermans; Hernan Moraldo; Han Zhang; Mohammad Taghi Saffar; Santiago Castro; Julius Kunze; Dumitru Erhan
- **时间**：2023年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICLR 2023（PDF首页）
- **项目／代码／数据**：[项目/演示页面](https://phenaki.github.io/)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：14页；SHA-256：`176243b1066c4db80df9b1f3de4de6fb8d6f9631fd65726c3e19015eaff5e4e2`

### 中文摘要

通过因果视频tokenizer与文本条件掩码Transformer，从随时间改变的文字提示生成可延续的视频。

### 核心贡献

C-ViViT变长视频离散表示、图文与视频文本联合训练、随故事提示自回归延续。

### 实现边界

“任意长”是可反复延长的机制，不保证任意时长保持质量/角色记忆；训练短片与展示长片之间没有无限泛化保证。

### Method／方法

因果时间注意力压缩视频token，T5文本条件下迭代补全被掩token，解码后以已有帧/新提示生成后续片段。

### Results／主要结果

相较逐帧编码减少约40%或更多视频token并改善时空重建一致性；训练1.4秒、8fps片段后展示分钟级变提示生成；图文联合数据帮助覆盖视频训练中未见概念组合。

### Shortcomings／局限与可能不足

【解读】长期误差积累、低分辨率/细节和精确动作控制限制；token效率和视觉演示不能等同电影级叙事/物理可靠性。

### 证据定位

PDF §2–4、tokenizer及生成实验、附录；首页摘要。

### Abstract

We present Phenaki, a model capable of realistic video synthesis, given a sequence of textual prompts. Generating videos from text is particularly challenging due to the computational cost, limited quantities of high quality text-video data and variable length of videos. To address these issues, we introduce a new model for learning video representation which compresses the video to a small representation of discrete tokens. This tokenizer uses causal attention in time, which allows it to work with variable-length videos. To generate video tokens from text we are using a bidirectional masked transformer conditioned on pre-computed text tokens. The generated video tokens are subsequently de-tokenized to create the actual video. To address data issues, we demonstrate how joint training on a large corpus of image-text pairs as well as a smaller number of video-text examples can result in generalization beyond what is available in the video datasets. Compared to the previous video generation methods, Phenaki can generate arbitrary long videos conditioned on a sequence of prompts (i.e. time variable text or a story) in open domain. To the best of our knowledge, this is the first time a paper studies generating videos from open domain time variable prompts. In addition, compared to the per-frame baselines, the proposed video encoder-decoder computes fewer tokens per video but results in better spatio-temporal consistency.

<a id="p123"></a>
## P123 · Genie: Generative Interactive Environments

- **作者**：Jake Bruce; Michael Dennis; Ashley Edwards; Jack Parker-Holder; Yuge (Jimmy) Shi; Edward Hughes; Matthew Lai; Aditi Mavalankar; Richie Steigerwald; Chris Apps; Yusuf Aytar; Sarah Bechtle; Feryal Behbahani; Stephanie Chan; Nicolas Heess; Lucy Gonzalez; Simon Osindero; Sherjil Ozair; Scott Reed; Jingwei Zhang; Konrad Zolna; Jeff Clune; Nando de Freitas; Satinder Singh; Tim Rocktäschel
- **时间**：本地版本：2024-02-23（arXiv:2402.15391v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：本地Google DeepMind稿首页2024-02-26；页边arXiv:2402.15391v1标2024-02-23，区分稿面日期与版本时间
- **论文链接**：[arXiv本地版本 2402.15391v1](https://arxiv.org/abs/2402.15391v1)
- **项目／代码／数据**：[项目/演示页面](https://sites.google.com/view/genie-2024/home)

- **主题**：世界机制与演化
- **PDF版本**：27页；SHA-256：`94c63a5ced89355326706c88236591c2972ced12f3dece4f8982f020110c81f3`

### 中文摘要

从无动作标签的互联网视频学习潜动作和动态，用图像、照片或草图初始化可逐帧控制的生成式环境。

### 核心贡献

11B生成式交互环境，时空tokenizer、潜动作模型与自回归动态模型联合支持视频到可控世界。

### 实现边界

文字提示经图像生成可间接初始化，模型本体主要图像提示/潜动作控制；主要平台游戏等域，非任意真实世界高保真模拟。

### Method／方法

潜动作模型从相邻帧推断离散控制，ST-transformer编码视频token，动态模型根据历史与动作预测下一帧；不需真实动作标签训练。

### Results／主要结果

展示未见图片/手绘初始化、潜动作可控性和从视频模仿策略；模型约1fps、记忆仅16帧，作者明确长时一致与交互速度待提升。

### Shortcomings／局限与可能不足

【作者】可幻觉不合理未来、上下文短、速度低；【解读】无监督动作语义在所有情境并不保证一致，视觉可玩不等于任务可用。

### 证据定位

PDF §2–4、§5 p.11。

### Abstract

We introduce Genie, the first generative interactive environment trained in an unsupervised manner from unlabelled Internet videos. The model can be prompted to generate an endless variety of actioncontrollable virtual worlds described through text, synthetic images, photographs, and even sketches. At 11B parameters, Genie can be considered a foundation world model. It is comprised of a spatiotemporal video tokenizer, an autoregressive dynamics model, and a simple and scalable latent action model. Genie enables users to act in the generated environments on a frame-by-frame basis despite training without any ground-truth action labels or other domain-specific requirements typically found in the world model literature. Further the resulting learned latent action space facilitates training agents to imitate behaviors from unseen videos, opening the path for training generalist agents of the future.

<a id="p124"></a>
## P124 · iVideoGPT: Interactive VideoGPTs are Scalable World Models

- **作者**：Jialong Wu; Shaofeng Yin; Ningya Feng; Xu He; Dong Li; Jianye Hao; Mingsheng Long
- **时间**：本地版本：2024-05-24（arXiv:2405.15223v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：NeurIPS 2024 Main Conference Track（官方论文集核验）。 [NeurIPS官方论文集](https://proceedings.neurips.cc/paper_files/paper/2024/hash/7dbb5bfab324e3b86af9bd0df15498dd-Abstract-Conference.html)
- **论文链接**：[arXiv本地版本 2405.15223v1](https://arxiv.org/abs/2405.15223v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：25页；SHA-256：`1e2d26119085edcf56158c4a199484aba285e21059fae3de0815d87574ff80e6`

### 中文摘要

把视觉、动作与奖励统一为token序列，使用压缩视频tokenizer及自回归Transformer预训练，适配预测、规划与模型式RL。

### 核心贡献

交互VideoGPT框架、上下文条件压缩tokenization及大规模人类/机器人轨迹预训练。

### 实现边界

主要机器人操作/视觉控制任务；未经适配在新机器人上会生成旧机器人外观，少样本tokenizer适配仍重要。

### Method／方法

用上下文帧帮助大幅压缩后续帧token，将动作奖励交错建模；下游微调模型/编码器，并以模型生成经验供策略学习。

### Results／主要结果

在所评连续控制上改善相对无模型方法的样本效率，与DreamerV3相当或更高；100/1000轨迹时预训练优势更明显，全量数据时较小；压缩方案按自回归forward次数计约16倍降低。

### Shortcomings／局限与可能不足

【解读】16倍是token/调用计数，不是端到端硬件实测速比；预训练机器人多样性不足，模型误差与合成轨迹偏差仍影响策略。

### 证据定位

PDF §3–4，图6–8、§4.4 p.8。

### Abstract

World models empower model-based agents to interactively explore, reason, and plan within imagined environments for real-world decision-making. However, the high demand for interactivity poses challenges in harnessing recent advancements in video generative models for developing world models at scale. This work introduces Interactive VideoGPT (iVideoGPT), a scalable autoregressive transformer framework that integrates multimodal signals—visual observations, actions, and rewards—into a sequence of tokens, facilitating an interactive experience of agents via next-token prediction. iVideoGPT features a novel compressive tokenization technique that efficiently discretizes high-dimensional visual observations. Leveraging its scalable architecture, we are able to pre-train iVideoGPT on millions of human and robotic manipulation trajectories, establishing a versatile foundation that is adaptable to serve as interactive world models for a wide range of downstream tasks. These include action-conditioned video prediction, visual planning, and model-based reinforcement learning, where iVideoGPT achieves competitive performance compared with state-of-the-art methods. Our work advances the development of interactive general world models, bridging the gap between generative video models and practical model-based reinforcement learning applications.

<a id="p125"></a>
## P125 · Causally Steered Diffusion for Automated Video Counterfactual Generation

- **作者**：Nikos Spyrou; Athanasios Vlontzos; Paraskevas Pegios; Thomas Melistas; Nefeli Gkouti; Yannis Panagakis; Giorgos Papanastasiou; Sotirios A. Tsaftaris
- **时间**：本地版本：2025-08-05（arXiv:2506.14404v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2506.14404v2（本地版本）
- **论文链接**：[arXiv本地版本 2506.14404v2](https://arxiv.org/abs/2506.14404v2)
- **项目／代码／数据**：[代码：nysp78/counterfactual-video-generation](https://github.com/nysp78/counterfactual-video-generation)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：23页；SHA-256：`6d89932cdf6a8eceef98e749d795c15861c7334d7a30d7bc4f32914e6c72bd67`

### 中文摘要

给定属性因果图，把干预及其应保留/改变的关系写入提示，用VLM文字反馈反复优化视频编辑以生成更符合指定因果关系的反事实。

### 核心贡献

黑箱可接入的CSVC提示级因果引导，评估有效性、最小性和时序质量。

### 实现边界

依赖先验因果图，主要真实人脸年龄/性别/胡须/秃发等属性编辑；不是从视频发现因果结构，基于外观标签的假设不等于生物学因果真值。

### Method／方法

因果目标/解耦提示→TokenFlow/FLATTEN/Tune-A-Video等编辑器→VLM评估损失→语言提示迭代，核心框架不需改编辑器内部。

### Results／主要结果

表1中CSVC通常提高各编辑后端的目标属性有效性，加入因果解耦提示效果更佳；通过LPIPS、VLM、DOVER、FVD及帧间CLIP检查最小性/质量。

### Shortcomings／局限与可能不足

【解读】评估和优化共享VLM语义偏差，有限属性图与人脸域限制因果解释；基础编辑器若需one-shot适配，整体并非完全无训练。

### 证据定位

PDF §3–5、表1、§6。

### Abstract

Adapting text-to-image (T2I) latent diffusion models (LDMs) to video editing has shown strong visual fidelity and controllability, but challenges remain in maintaining causal relationships inherent to the video data generating process. Edits affecting causally dependent attributes often generate unrealistic or misleading outcomes if these relationships are ignored. In this work, we introduce a causally faithful framework for counterfactual video generation, formulated as an Out-of-Distribution (OOD) prediction problem. We embed prior causal knowledge by encoding the relationships specified in a causal graph into text prompts and guide the generation process by optimizing these prompts using a vision-language model (VLM)-based textual loss. This loss encourages the latent space of the LDMs to capture OOD variations in the form of counterfactuals, effectively steering generation toward causally meaningful alternatives. The proposed framework, dubbed CSVC, is agnostic to the underlying video editing system and does not require access to its internal mechanisms or fine-tuning. We evaluate our approach using standard video quality metrics and counterfactual-specific criteria, such as causal effectiveness and minimality. Experimental results show that CSVC generates causally faithful video counterfactuals within the LDM distribution via prompt-based causal steering, achieving state-of-the-art causal effectiveness without compromising temporal consistency or visual quality on real-world facial videos. Due to its compatibility with any black-box video editing system, our framework has significant potential to generate realistic ’what if’ hypothetical video scenarios in diverse areas such as digital media and healthcare. Code: https://github.com/nysp78/counterfactual-video-generation.

<a id="p126"></a>
## P126 · Diffusion-Based Visual Art Creation: A Survey and New Perspectives

- **作者**：Bingyuan Wang; Qifeng Chen; Zeyu Wang
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ACM Computing Surveys 57(10), Article268；2025-05-07上线，2025-10卷期；2025-04-01接受；DOI10.1145/3728459
- **论文链接**：[DOI正式记录](https://doi.org/10.1145/3728459)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：创作与规则补全
- **PDF版本**：38页；SHA-256：`18c343dc471df6180c288a6b3bc1c30e4075f42475deec95b9f059a3c5981f6e`

### 中文摘要

从艺术需求和技术方法共同审视扩散视觉艺术创作，系统编码相关论文，建立应用、理解和生成的分析框架及人机协作展望。

### 核心贡献

四阶段文献筛选、七维编码和场景—模态—任务—方法框架，连接艺术要求与计算问题。

### 实现边界

综述，不是新的图像/视频生成模型；PDF封面的2026-01-31为下载日期，不是发表日。

### Method／方法

明确研究问题和纳入条件，结构/时间分析论文编码，归纳技术与人机协作趋势。

### Results／主要结果

识别视觉艺术的风格控制、内容编辑、跨模态与多场景生成热点，提出技术能力与艺术家参与方式共同演化的研究方向；无统一新实验排名。

### Shortcomings／局限与可能不足

【解读】文献筛选/编码有解释性，领域更新快；创作质量和创造性没有跨艺术门类统一客观标准。

### 证据定位

PDF封面元数据；§4–6、图4、§7–8（正文到PDF p.30）。

### Abstract

The integration of generative AI in visual art has revolutionized not only how visual content is created but also how AI interacts with and reflects the underlying domain knowledge. This survey explores the emerging realm of diffusion-based visual art creation, examining its development from both artistic and technical perspectives. We structure the survey into three phases: data feature and framework identification, detailed analyses using a structured coding process, and open-ended prospective outlooks. Our findings reveal how artistic requirements are transformed into technical challenges and highlight the design and application of diffusion-based methods within visual art creation. We also provide insights into future directions from technical and synergistic perspectives, suggesting that the confluence of generative AI and art has shifted the creative paradigm and opened up new possibilities. By summarizing the development and trends of this emerging interdisciplinary area, we aim to shed light on the mechanisms through which AI systems emulate and, possibly, enhance human capacities in artistic perception and creativity.

<a id="p127"></a>
## P127 · MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences

- **作者**：Canyu Zhao; Mingyu Liu; Wen Wang; Weihua Chen; Fan Wang; Hao Chen; Bo Zhang; Chunhua Shen
- **时间**：本地版本：2025-11-25（arXiv:2407.16655v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：ICLR 2025（PDF首页）；arXiv:2407.16655v3
- **论文链接**：[arXiv本地版本 2407.16655v3](https://arxiv.org/abs/2407.16655v3)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P134](#p134)同一论文不同文件；本稿首页3位作者标共同一作，[P134](#p134)首页只对前2位标星，作者顺序相同。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：31页；SHA-256：`19dcbd7282b7ec5eab617b7d97a0aaaa42d43b765a7c7d57a866b1f88d22f93a`

### 中文摘要

用自回归模型规划长序列关键帧token，再以扩散渲染图像和视频，以多模态剧本和人脸身份条件维持跨场景角色一致。

### 核心贡献

叙事/渲染分层框架、包含角色及风格的剧本和身份保持渲染。

### 实现边界

“叙事一致”主要由脚本对齐和角色视觉指标代理；关键帧及短片段组装不保证每项事件真实发生或长时物理因果一致。

### Method／方法

扩散自动编码器产生紧凑关键帧token，自回归预测下一个keyframe，文本/FaceID条件解码，再生成帧间视频。

### Results／主要结果

表1无参考Ours长期一致LT0.814对StoryDiffusion0.596，FID2.043对4.643；审美6.093略低于6.134，非逐项最佳；有参考Ours-ref LT0.893但使用额外条件。

### Shortcomings／局限与可能不足

【解读】人脸身份覆盖、长时错误累积和剧本粒度影响结果；参考/无参考条件需分开比较，电影域指标不等于人类叙事理解。

### 证据定位

PDF §3–4、表1–2 p.9、§5。

### Abstract

Recent advancements in video generation have primarily leveraged diffusion models for short-duration content. However, these approaches often fall short in modeling complex narratives and maintaining character consistency over extended periods, which is essential for long-form video production like movies. We propose MovieDreamer, a novel hierarchical framework that integrates the strengths of autoregressive models with diffusion-based rendering to pioneer long-duration video generation with intricate plot progressions and high visual fidelity. Our approach utilizes autoregressive models for global narrative coherence, predicting sequences of visual tokens that are subsequently transformed into high-quality video frames through diffusion rendering. This method is akin to traditional movie production processes, where complex stories are factorized down into manageable scene capturing. Further, we employ a multimodal script that enriches scene descriptions with detailed character information and visual style, enhancing continuity and character identity across scenes. We present extensive experiments across various movie genres, demonstrating that our approach not only achieves superior visual and narrative quality but also effectively extends the duration of generated content significantly beyond current capabilities.

<a id="p128"></a>
## P128 · StoryMem: Multi-shot Long Video Storytelling with Memory

- **作者**：Kaiwen Zhang; Liming Jiang; Angtian Wang; Jacob Zhiyuan Fang; Tiancheng Zhi; Qing Yan; Hao Kang; Xin Lu; Xingang Pan
- **时间**：本地版本：2025-12-22（arXiv:2512.19539v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：首页2025-12-23；arXiv:2512.19539v1
- **论文链接**：[arXiv本地版本 2512.19539v1](https://arxiv.org/abs/2512.19539v1)
- **项目／代码／数据**：[项目/演示页面](https://kevin-thu.github.io/StoryMem)

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：20页；SHA-256：`893eb41d0811d6480248c118b3146657400c5b93dfc5ae1c4ff1a62b75d116af`

### 中文摘要

用动态历史关键帧记忆把单镜头视频扩散改造成逐镜头长叙事生成，并通过语义/审美选择维持紧凑记忆。

### 核心贡献

Memory-to-Video（M2V）、负RoPE位置与latent拼接、LoRA训练及ST-Bench。

### 实现边界

需微调单镜头骨干；分钟级逐镜头生成不是无限记忆，纯视觉记忆可能混淆多角色；平滑过渡和提示跟随有取舍。

### Method／方法

历史镜头选相关美观关键帧写入记忆，潜空间拼接注入模型；MI2V/MR2V支持过渡和定制。

### Results／主要结果

ST-Bench总体跨镜头一致性0.5065，报告比基础模型相对提高28.7%、比HoloCine提高9.4%；用户成对偏好更高；单镜头提示跟随略下降。

### Shortcomings／局限与可能不足

【作者】复杂多角色和大运动差异过渡困难；【解读】视觉一致性/审美不证明事件链完成，记忆选择会过滤重要但不美观的状态。

### 证据定位

PDF §3–4、表1–2、图7、§5。

### Abstract

Visual storytelling requires generating multi-shot videos with cinematic quality and long-range consistency. Inspired by human memory, we proposeStoryMem, a paradigm that reformulates long-form video storytelling as iterative shot synthesis conditioned on explicit visual memory, transforming pre-trained single-shot video diffusion models into multi-shot storytellers. This is achieved by a novelMemory-to-Video (M2V)design, which maintains a compact and dynamically updated memory bank of keyframes from historical generated shots. The stored memory is then injected into single-shot video diffusion models via latent concatenation and negative RoPE shifts with only LoRA fine-tuning. A semantic keyframe selection strategy, together with aesthetic preference filtering, further ensures informative and stable memory throughout generation. Moreover, the proposed framework naturally accommodates smooth shot transitions and customized story generation application. To facilitate evaluation, we introduce ST-Bench, a diverse benchmark for multi-shot video storytelling. Extensive experiments demonstrate thatStoryMemachieves superior cross-shot consistency over previous methods while preserving high aesthetic quality and prompt adherence, marking a significant step toward coherent minute-long video storytelling.

<a id="p129"></a>
## P129 · StoryReasoning Dataset: Using Chain-of-Thought for Scene Understanding and Grounded Story Generation

- **作者**：Daniel A. P. Oliveira; David Martins de Matos
- **时间**：本地版本：2025-08-30（arXiv:2505.10292v2）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2505.10292v2（本地版本）
- **论文链接**：[arXiv本地版本 2505.10292v2](https://arxiv.org/abs/2505.10292v2)
- **项目／代码／数据**：[数据/模型：datasets/daniel3303/StoryReasoning](https://huggingface.co/datasets/daniel3303/StoryReasoning)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：31页；SHA-256：`ba6b37f97eb4e938f932a69fc2e4f6572cdd454f72329fffc733ac3dedb43ca1`

### 中文摘要

为电影图像序列生成带跨帧实体链接的场景分析和故事，建立StoryReasoning并微调Qwen Storyteller，减少人物/物体指代幻觉。

### 核心贡献

4,178故事、52,016图像的结构化分析/grounded叙事数据，跨帧重识别和基线模型。

### 实现边界

输出以多图到文字故事为主，不是生成视频；创造性/幻觉主要由LLM评判，不能等同人类创意评估。

### Method／方法

视觉相似性与人脸识别匹配对象，表格组织跨帧场景，CoT生成并将词语链接到实体，微调Qwen2.5VL7B。

### Results／主要结果

平均每故事幻觉4.06→3.56（相对−12.3%）；创造性评分2.58→3.38/5（+31%）；描述准确评分2.69→2.76，收益较小。

### Shortcomings／局限与可能不足

【作者】外观相似实体如双胞胎可混淆、电影构图偏差、对话第一人称难grounding；LLM评判偏差和文本相似指标可能惩罚合理创作。

### 证据定位

PDF §3–5、表1–2 p.8、§6。

### Abstract

Visual storytelling systems struggle to maintain character identity across frames and link actions to appropriate subjects, frequently leading to referential hallucinations. These issues can be addressed through grounding of characters, objects, and other entities on the visual elements. We propose StoryReasoning, a dataset containing 4,178 stories derived from 52,016 movie images, with both structured scene analyses and grounded stories. Each story maintains character and object consistency across frames while explicitly modeling multi-frame relationships through structured tabular representations. Our approach features cross-frame object re-identification using visual similarity and face recognition, chain-of-thought reasoning for explicit narrative modeling, and a grounding scheme that links textual elements to visual entities across multiple frames. We establish baseline performance by fine-tuning Qwen2.5-VL 7B, creating Qwen Storyteller, which performs end-to-end object detection, re-identification, and landmark detection while maintaining consistent object references throughout the story. Evaluation demonstrates a reduction from 4.06 to 3.56 (-12.3%) hallucinations on average per story and an improvement in creativity from 2.58 to 3.38 (+31.0%) when compared to a non-fine-tuned model.

<a id="p130"></a>
## P130 · CounterVid: Counterfactual Video Generation for Mitigating Action and Temporal Hallucinations in Video-Language Models

- **作者**：Tobia Poppi; Burak Uzkent; Amanmeet Garg; Lucas Porto; Garin Kessler; Yezhou Yang; Marcella Cornia; Lorenzo Baraldi; Rita Cucchiara; Florian Schiffers
- **时间**：本地版本：2026-01-08（arXiv:2601.04778v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2601.04778v1（本地版本）；代码/模型在稿中为待公开承诺
- **论文链接**：[arXiv本地版本 2601.04778v1](https://arxiv.org/abs/2601.04778v1)
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：16页；SHA-256：`473d1665bbd2a82bfbf319b6598336ea9023c21145d6fc9bf9d750622bb9b610`

### 中文摘要

生成保留场景但改变短时动作/顺序的反事实视频硬负例，以文字和视觉偏好联合DPO减少视频VLM动作与时间幻觉。

### 核心贡献

约26K偏好对CounterVid与MixDPO，面向语言先验导致的时间/动作错误。

### 实现边界

反事实主要是&lt;2秒动作的语义替换，不是严格结构因果模型干预；生成数据质量不完美，评估中只有68%标为good。

### Method／方法

多模态LLM提出替代动作/编辑指导，图像与视频扩散合成负例，过滤并构造文字/视觉偏好，冻结视觉编码器进行参数高效优化。

### Results／主要结果

留出集Qwen2.5VL7B平均57.8→66.2%；顺序列表16.5→43.8%；3B平均36.9→45.2%。样本审核7%视觉质量差，部分任务有约17%歧义。

### Shortcomings／局限与可能不足

【作者】过滤和生成质量、短动作限制、冻结视觉编码器；【解读】合成负例收益需关注跨真实域迁移而非只看内部留出集。

### 证据定位

PDF §3–4、表1–2 p.6、Limitations p.9。

### Abstract

Video-language models (VLMs) achieve strong multimodal understanding but remain prone to hallucinations, especially when reasoning about actions and temporal order. Existing mitigation strategies, such as textual filtering or random video perturbations, often fail to address the root cause: over-reliance on language priors rather than fine-grained visual dynamics. We propose a scalable framework forcounterfactual video generationthat synthesizes videos differing only in actions or temporal structure while preserving scene context. Our pipeline combines multimodal LLMs for action proposal and editing guidance with diffusion-based image and video models to generate semantic hard negatives at scale. Using this framework, we build CounterVid, a synthetic dataset of ∼26k preference pairs targeting action recognition and temporal reasoning. We further introduce MixDPO, a unified Direct Preference Optimization approach that jointly leverages textual and visual preferences. Finetuning Qwen2.5-VL with MixDPO yields consistent improvements, notably in temporal ordering, and transfers effectively to standard video hallucination benchmarks. Code and models will be made publicly available.

<a id="p131"></a>
## P131 · Controllable Video Generation: A Survey

- **作者**：Yue Ma; Kunyu Feng; Zhongyuan Hu; Xinyu Wang; Yucheng Wang; Mingzhe Zheng; Bingyuan Wang; Qinghe Wang; Xuanhua He; Hongfa Wang; Chenyang Zhu; Hongyu Liu; Yingqing He; Zeyu Wang; Zhifeng Li; Xiu Li; Sirui Han; Yike Guo; Wei Liu; Dan Xu; Linfeng Zhang; Qifeng Chen
- **时间**：本地版本：2026-01-19（arXiv:2507.16869v3）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2507.16869v3（本地版本）；检索方法主要覆盖2020–2025，文件名26不等于内容只属2026
- **论文链接**：[arXiv本地版本 2507.16869v3](https://arxiv.org/abs/2507.16869v3)
- **项目／代码／数据**：[代码：mayuelala/Awesome-Controllable-Video-Generation](https://github.com/mayuelala/Awesome-Controllable-Video-Generation)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：41页；SHA-256：`a14847ae33974419f181f58ca0c4df227f2c1fdafdeb7b9910470cd15a236f86`

### 中文摘要

系统梳理文本之外的姿态、深度、轨迹、相机、音频、身份等视频生成控制，比较单条件、多条件和通用控制机制。

### 核心贡献

控制信号/注入方式分类、基础视频模型及文献资源汇集。

### 实现边界

综述，列出的生成分辨率、速度和代码状态属于原文时点/原实验配置；不是同硬件复现实验排行榜。

### Method／方法

PRISMA式四阶段筛选，按基础模型、条件类型、去噪注入方式和应用分析研究。

### Results／主要结果

形成控制分类与模型对照，指出多条件协调、精确局部控制、时序一致、通用接口和评估标准的挑战；无新模型统一提升数值。

### Shortcomings／局限与可能不足

【解读】快速更新导致覆盖时点有限，各论文预算/数据/控制难度不同，列表不可直接作为质量排名。

### 证据定位

PDF §3检索流程、§4–7、§8 p.26。

### Abstract

With the rapid development of AI-generated content (AIGC), video generation has emerged as one of its most dynamic and impactful subfields. In particular, the advancement of video generation foundation models has led to growing demand for controllable video generation methods that can more accurately reflect user intent. Most existing foundation models are designed for text-to-video generation, where text prompts alone are often insufficient to express complex, multi-modal, and fine-grained user requirements. This limitation makes it challenging for users to generate videos with precise control using current models. To address this issue, recent research has explored the integration of additional non-textual conditions—such as camera motion, depth maps, and human pose—to extend pretrained video generation models and enable more controllable video synthesis. These approaches aim to enhance the flexibility and practical applicability of AIGC-driven video generation systems. In this survey, we provide a systematic review of controllable video generation, covering both theoretical foundations and recent advances in the field. We begin by introducing the key concepts and commonly used open-source video generation models. We then focus on control mechanisms in video diffusion models, analyzing how different types of conditions can be incorporated into the denoising process to guide generation. Finally, we categorize existing methods based on the types of control signals they leverage, including single-condition generation, multi-condition generation, and universal controllable generation. For a complete list of the literature on controllable video generation reviewed, please visit our curated repository at https://github.com/mayuelala/Awesome-Controllable-Video-Generation.

<a id="p132"></a>
## P132 · Pre-trained Video Generative Models as World Simulators

- **作者**：Haoran He; Yang Zhang; Liang Lin; Zhongwen Xu; Ling Pan
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICLR 2025（PDF首页）；文件名77无可靠年份含义
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。

- **主题**：世界机制与演化
- **PDF版本**：17页；SHA-256：`dce93f666b6f970e5163c61fe1c0ead37843cbe44eaebd66be8bedc4d76dee43`

### 中文摘要

DWS在预训练视频生成器上添加动作条件模块和运动强化损失，获得可按动作轨迹生成的动态模型，再通过优先想象改进模型式RL。

### 核心贡献

适配扩散/自回归骨干的动作接口、动态转移训练与prioritized imagination。

### 实现边界

需要任务动作数据和微调；“任何模型通用”仅在所测架构证实，主要游戏/机器人域，非现实通用仿真。

### Method／方法

轻量动作模块对齐动作与视觉变化，以运动损失强化动态；按价值选想象轨迹供PPO/离线策略训练。

### Results／主要结果

Procgen/Atari展示较PPO及部分模型式RL的样本效率收益；Breakout报告约7倍分数提升，限定具体预算/基线；另用合成经验增强离线策略。

### Shortcomings／局限与可能不足

【解读】模型动态误差、动作覆盖和想象优先级可造成偏差；Procgen策略训练中世界模型仍需继续微调，不能当作一次预训练后通吃。

### 证据定位

PDF §3–5、§5.2图6–7、§5.3。

### Abstract

Video generative models pre-trained on large-scale internet datasets have achieved remarkable success, excelling at producing realistic synthetic videos. However, they often generate clips based on static prompts (e.g., text or images), limiting their ability to model interactive and dynamic scenarios. In this paper, we propose Dynamic World Simulation (DWS), a novel approach to transform pre-trained video generative models into controllable world simulators capable of executing specified action trajectories. To achieve precise alignment between conditioned actions and generated visual changes, we introduce a lightweight, universal actionconditioned module that seamlessly integrates into any existing model. Instead of focusing on complex visual details, we demonstrate that consistent dynamic transition modeling is the key to building powerful world simulators. Building upon this insight, we further introduce a motion-reinforced loss that enhances action controllability by compelling the model to capture dynamic changes more effectively. Experiments demonstrate that DWS can be versatilely applied to both diffusion and autoregressive transformer models, achieving significant improvements in generating action-controllable, dynamically consistent videos across games and robotics domains. Moreover, to facilitate the applications of the learned world simulator in downstream tasks such as model-based reinforcement learning, we propose prioritized imagination to improve sample efficiency, demonstrating competitive performance compared with state-of-the-art methods.

<a id="p133"></a>
## P133 · OneStory: Coherent Multi-Shot Video Generation with Adaptive Memory

- **作者**：Zhaochong An; Menglin Jia; Haonan Qiu; Zijian Zhou; Xiaoke Huang; Zhiheng Liu; Weiming Ren; Kumara Kahatapitiya; Ding Liu; Sen He; Chenyang Zhang; Tao Xiang; Fanny Yang; Serge Belongie; Tian Xie
- **时间**：本地版本：2025-12-08（arXiv:2512.07802v1）；正式发表时间如已核实，见下一项。
- **发表平台／版本状态**：arXiv:2512.07802v1（本地版本）
- **论文链接**：[arXiv本地版本 2512.07802v1](https://arxiv.org/abs/2512.07802v1)
- **项目／代码／数据**：[项目/演示页面](https://zhaochongan.github.io/projects/OneStory)

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：17页；SHA-256：`31338f0d7ecd2fa06661eb61cdcf6e0c6af71ad9266062b66478796afd0ce453`

### 中文摘要

OneStory把多镜头生成视为下一镜头预测，从全局历史挑选相关帧并自适应压缩为紧凑条件，保持角色/环境一致。

### 核心贡献

Frame Selection、Adaptive Conditioner、带指代字幕的多镜头数据及shot inflation/解耦条件训练。

### 实现边界

历史经选择压缩，不能保留所有事件状态；依赖预训练I2V模型和相应训练，并非无需训练的记忆外挂。

### Method／方法

按当前镜头字幕检索历史信息帧，重要性引导patchification压缩上下文，直接条件注入下一镜头视频生成器。

### Results／主要结果

表2无AC/FS时角色/环境一致0.5153/0.5112，完整0.5874/0.5752；语义对齐0.1814→0.2389。增加至3帧等价上下文后角色/环境0.5926/0.5863，说明预算仍有影响。

### Shortcomings／局限与可能不足

【解读】历史选择失误、对象混淆和累积漂移仍可能发生；指标主要衡量视觉/语义一致，不能保证复杂故事事件因果完整。

### 证据定位

PDF §3–5、表2 p.8、§6。

### Abstract

Storytelling in real-world videos often unfolds through multiple shots—discontinuous yet semantically connected clips that together convey a coherent narrative. However, existing multi-shot video generation (MSV) methods struggle to effectively model long-range cross-shot context, as they rely on limited temporal windows or single keyframe conditioning, leading to degraded performance under complex narratives. In this work, we propose OneStory, enabling global yet compact cross-shot context modeling for consistent and scalable narrative generation. OneStory reformulates MSV as a next-shot generation task, enabling autoregressive shot synthesis while leveraging pretrained image-to-video (I2V) models for strong visual conditioning. We introduce two key modules: a Frame Selection module that constructs a semantically-relevant global memory based on informative frames from prior shots, and an Adaptive Conditioner that performs importance-guided patchification to generate compact context for direct conditioning. We further curate a high-quality multi-shot dataset with referential captions to mirror real-world storytelling patterns, and design effective training strategies under the next-shot paradigm. Finetuned from a pretrained I2V model on our curated 60K dataset, OneStory achieves state-of-the-art narrative coherence across diverse and complex scenes in both text- and image-conditioned settings, enabling controllable and immersive long-form video storytelling.

<a id="p134"></a>
## P134 · MovieDreamer: Hierarchical Generation for Coherent Long Visual Sequences

- **作者**：Canyu Zhao; Mingyu Liu; Wen Wang; Weihua Chen; Fan Wang; Hao Chen; Bo Zhang; Chunhua Shen
- **时间**：本地PDF未明确；未按文件名或PDF制作时间推断。
- **发表平台／版本状态**：ICLR 2025正式论文版（PDF首页）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P127](#p127)同一工作，31页但SHA不同；本稿前2位作者标星，[P127](#p127)前3位标星；下述主要表格结果一致，版本不计为独立证据。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：31页；SHA-256：`1b087586ac8870db8a1387f8b29b51504d15a408053d5e9e4a226976dc9d8bb0`

### 中文摘要

以多模态剧本、自回归关键帧及扩散视频渲染组合实现长叙事视觉序列，强调角色与风格跨镜头保持。

### 核心贡献

分层生成与身份保持渲染，支持有/无参考故事生成。

### 实现边界

主要验证脚本对齐和视觉角色一致；不保证长序列每项事件完成/真实因果正确，有参考条件不能和纯文本输入直接比较。

### Method／方法

预测紧凑关键帧token，使用FaceID及文字渲染，再以关键帧条件生成视频片段。

### Results／主要结果

表1无参考LT0.814、ST0.646、FID2.043；有参考LT0.893/ST0.701/FID1.912。表2视频CLIP19.520、Inception8.642、Aesthetic6.049、CLIP-sim0.704；各指标口径限该测试集。

### Shortcomings／局限与可能不足

【解读】叙事与角色指标不等同完整事件序列正确，长时误差和身份覆盖仍有限；不同条件与不同版本须保留标识。

### 证据定位

PDF §3–4、表1–2 p.9。

### Abstract

Recent advancements in video generation have primarily leveraged diffusion models for short-duration content. However, these approaches often fall short in modeling complex narratives and maintaining character consistency over extended periods, which is essential for long-form video production like movies. We propose MovieDreamer, a novel hierarchical framework that integrates the strengths of autoregressive models with diffusion-based rendering to pioneer long-duration video generation with intricate plot progressions and high visual fidelity. Our approach utilizes autoregressive models for global narrative coherence, predicting sequences of visual tokens that are subsequently transformed into high-quality video frames through diffusion rendering. This method is akin to traditional movie production processes, where complex stories are factorized down into manageable scene capturing. Further, we employ a multimodal script that enriches scene descriptions with detailed character information and visual style, enhancing continuity and character identity across scenes. We present extensive experiments across various movie genres, demonstrating that our approach not only achieves superior visual and narrative quality but also effectively extends the duration of generated content significantly beyond current capabilities.

<a id="p135"></a>
## P135 · WorldMem: Long-term Consistent World Simulation with Memory

- **作者**：Zeqi Xiao; Yushi Lan; Yifan Zhou; Wenqi Ouyang; Shuai Yang; Yanhong Zeng; Xingang Pan
- **时间**：2025-04-16首发预印本；2025年NeurIPS发表；本地版本日期未明示
- **发表平台／版本状态**：NeurIPS 2025 Main Conference Track（官方论文集核验）；arXiv:2504.12369首发2025-04-16；本地文件未明确具体版本日。 [NeurIPS官方论文集](https://papers.neurips.cc/paper_files/paper/2025/hash/470629a47e2d65ce0606c40055df5d26-Abstract-Conference.html)；[arXiv记录](https://arxiv.org/abs/2504.12369)
- **论文链接**：[arXiv论文记录](https://arxiv.org/abs/2504.12369)
- **项目／代码／数据**：[项目/演示页面](https://xizaoqu.github.io/worldmem/)

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：14页；SHA-256：`f1c77acf725e4d4c657bb11fa04abd75c418854abb04e6d8a7b2477c6c0ead78`

### 中文摘要

以过去帧、位姿和时间戳组成记忆库，通过状态相关的memory attention重建之前去过的地方并表达世界随时间演化。

### 核心贡献

显式状态帧记忆与检索式世界生成，扩展有限上下文的视频模拟。

### 实现边界

Minecraft主要实验使用模拟器提供的真值位姿；现实只给动作时位姿需预测，误差条件不同；记忆增强并不证明完整3D世界模型。

### Method／方法

为帧存姿态/时间，按当前目标状态检索并注意历史视图；扩散模型结合当前上下文与记忆生成。

### Results／主要结果

超上下文Minecraft PSNR25.32对DiffusionForcing18.04，LPIPS0.1429对0.4376；RealEstate10K回访PSNR20.19对DFoT8.396。主要是回到已见视角的重建任务。

### Shortcomings／局限与可能不足

【解读】真值位姿和已访问参考带来条件优势，未知位姿、动态遮挡和记忆容量扩张仍有风险；回访重建好不等于开放新场景因果预测准确。

### 证据定位

PDF §3–4、§4.1 pp.6–7、表1–2。

### Abstract

World simulation has gained increasing popularity due to its ability to model virtual environments and predict the consequences of actions. However, the limited temporal context window often leads to failures in maintaining longterm consistency, particularly in preserving 3D spatial consistency. In this work, we present WorldMem, a framework that enhances scene generation with a memory bank consisting of memory units that store memory frames and states (e.g., poses and timestamps). By employing a memory attention mechanism that effectively extracts relevant information from these memory frames based on their states, our method is capable of accurately reconstructing previously observed scenes, even under significant viewpoint or temporal gaps. Furthermore, by incorporating timestamps into the states, our framework not only models a static world but also captures its dynamic evolution over time, enabling both perception and interaction within the simulated world. Extensive experiments in both virtual and real scenarios validate the effectiveness of our approach.

<a id="p136"></a>
## P136 · StoryBench: A Multifaceted Benchmark for Continuous Story Visualization

- **作者**：Emanuele Bugliarello; Hernan Moraldo; Ruben Villegas; Mohammad Babaeizadeh; Mohammad Taghi Saffar; Han Zhang; Dumitru Erhan; Vittorio Ferrari; Pieter-Jan Kindermans; Paul Voigtlaender
- **时间**：2023年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：NeurIPS 2023 Datasets and Benchmarks Track（PDF首页）
- **项目／代码／数据**：[代码：google/storybench](https://github.com/google/storybench)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：31页；SHA-256：`1d7fde670c781d256bb4a41b4ad1375c75af97ae3941b4fa447725078a20c2f5`

### 中文摘要

在三个既有视频数据集上增加带时间戳的多句故事标注，评估动作执行、故事续写和纯文本故事视频生成。

### 核心贡献

Oops/UVO/DiDeMo的连续故事基准、不同训练设置及视频人评指南。

### 实现边界

多数为较短、单镜头用户视频，不能代表长电影多镜头；虽为“continuous story”不意味着无限时长评测。

### Method／方法

人工标注时间段/动作及诊断标签；用小型Phenaki基线进行零样本、单任务、多任务微调；比较自动指标与人类评价。

### Results／主要结果

续写专门微调改善动作与上下文一致；Oops动作执行FVD：GEN-ZS416、CONT-ST350；但自动分数与人评存在偏离，作者强调仍需人工核查。

### Shortcomings／局限与可能不足

【作者】视频不长、以单镜头非专业内容为主、自动指标不足；【解读】少数小基线不能穷尽所有生成模型能力。

### 证据定位

PDF §3–6、表4–7、§7–8。

### Abstract

Generating video stories from text prompts is a complex task. In addition to having high visual quality, videos need to realistically adhere to a sequence of text prompts whilst being consistent throughout the frames. Creating a benchmark for video generation requires data annotated over time, which contrasts with the single caption used often in video datasets. To fill this gap, we collect comprehensive human annotations on three existing datasets, and introduce StoryBench: a new, challenging multi-task benchmark to reliably evaluate forthcoming text-to-video models. Our benchmark includes three video generation tasks of increasing difficulty: action execution, where the next action must be generated starting from a conditioning video; story continuation, where a sequence of actions must be executed starting from a conditioning video; and story generation, where a video must be generated from only text prompts. We evaluate small yet strong text-to-video baselines, and show the benefits of training on story-like data algorithmically generated from existing video captions. Finally, we establish guidelines for human evaluation of video stories, and reaffirm the need of better automatic metrics for video generation. StoryBench aims at encouraging future research efforts in this exciting new area.

<a id="p137"></a>
## P137 · Long-Context State-Space Video World Models

- **作者**：Ryan Po; Yotam Nitzan; Richard Zhang; Berlin Chen; Tri Dao; Eli Shechtman; Gordon Wetzstein; Xun Huang
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICCV 2025，正文页码8733起（PDF论文版）
- **项目／代码／数据**：本地PDF未检出明确属于本文的项目链接；不代表作者没有发布资源。
- **版本关系**：与[P102](#p102)为同一工作；本条是12页ICCV 2025论文版，[P102](#p102)为15页arXiv版本。

- **主题**：创作与规则补全、世界机制与演化、XR与人机协作
- **PDF版本**：12页；SHA-256：`fe20255bf4824c5ed9d408c9963ac7efce53b1f043971ba20e541fd658969a2c`

### 中文摘要

以块级SSM扫描存储较长视频历史，结合局部注意力维持局部连贯，降低动作条件世界模型长上下文计算。

### 核心贡献

因果视频SSM架构、训练策略及长时空间记忆测试。

### 实现边界

每帧推理成本不随历史增长，但作者明确尚不支持交互帧率，无法有效超训练长度记忆；仅低分辨率合成环境。

### Method／方法

Mamba状态压缩长历史，block-wise扫描与frame-local attention结合，逐帧扩散生成。

### Results／主要结果

576历史帧/224预测帧任务PSNR28.2、LPIPS0.099、SSIM0.855；接近全历史Transformer28.8/0.089/0.860并优于较低复杂度比较方法。

### Shortcomings／局限与可能不足

【作者】速度、长度外推和高分辨率真实视频扩展待解决；【解读】压缩状态对长期精细记忆仍有容量约束。

### 证据定位

PDF §4–5、表3 p.6、§6 p.8。

### Abstract

Video diffusion models have recently shown promise for world modeling through autoregressive frame prediction conditioned on actions. However , they struggle to maintain long-term memory due to the high computational cost associated with processing extended sequences in attention layers. To overcome this limitation, we propose a novel architecture leveraging state-space models (SSMs) to extend temporal memory without compromising computational efficiency. Unlike previous approaches that retrofit SSMs for non-causal vision tasks, our method fully exploits the inherent advantages of SSMs in causal sequence modeling. Central to our design is a block-wise SSM scanning scheme, which strategically trades off spatial consistency for extended temporal memory, combined with dense local attention to ensure coherence between consecutive frames. We evaluate the long-term memory capabilities of our model through spatial retrieval and reasoning tasks over extended horizons. Experiments on Memory Maze and Minecraft datasets demonstrate that our approach surpasses baselines in preserving long-range memory, while maintaining practical inference speeds suitable for interactive applications.

<a id="p138"></a>
## P138 · StoryGAN: A Sequential Conditional GAN for Story Visualization

- **作者**：Yitong Li, Zhe Gan, Yelong Shen, Jingjing Liu, Yu Cheng, Yuexin Wu, Lawrence Carin, David Carlson, Jianfeng Gao
- **时间**：2019年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CVPR 2019（论文版）
- **项目／代码／数据**：[代码：yitong91/StoryGAN](https://github.com/yitong91/StoryGAN)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：10页；SHA-256：`f81df8beff3dd5f58ca33af45475b7e70b19fff4e47d9c08a4b3016e5e2f32bc`

### 中文摘要

每句话生成一张图，把故事可视化为有角色和场景一致性的图片序列。

### 核心贡献

StoryGAN顺序条件GAN、动态Context Encoder/Text2Gist、图像级与故事级判别器，以及CLEVR-SV/Pororo-SV数据。

### 实现边界

是句子到图片序列，不是连续视频生成；重点为全局一致而非帧间运动平滑；主要合成/动画小域。

### Method／方法

故事编码初始化状态，Text2Gist融合当前句与历史，逐图生成；两级对抗损失约束单图和全序列。

### Results／主要结果

CLEVR-SV SSIM0.672，ImageGAN0.596、SVC0.641、SVFN0.654；用户排序平均名次1.94优于ImageGAN2.91（越低越好）。

### Shortcomings／局限与可能不足

【解读】低分辨率、数据域窄，角色细节和长故事能力有限；SSIM仅在该合成布局约束下具可比性，非通用故事质量指标。

### 证据定位

PDF §3–4、表1 p.6、表3–4 p.8。

### Abstract

In this work, we propose a new task called Story Visualization. Given a multi-sentence paragraph, the story is visualized by generating a sequence of images, one for each sentence. In contrast to video generation, story visualization focuses less on the continuity in generated images (frames), but more on the global consistency across dynamic scenes and characters – a challenge that has not been addressed by any single-image or video generation methods. Therefore, we propose a new story-to-image-sequence generation model, StoryGAN, based on the sequential conditional GAN framework. Our model is unique in that it consists of a deep Context Encoder that dynamically tracks the story flow, and two discriminators at the story and image levels, to enhance the image quality and the consistency of the generated sequences. To evaluate the model, we modified existing datasets to create the CLEVR-SV and Pororo- SV datasets. Empirically, StoryGAN outperformed stateof-the-art models in image quality, contextual consistency metrics, and human evaluation.

<a id="p139"></a>
## P139 · Is Your World Simulator a Good Story Presenter? A Consecutive Events-Based Benchmark for Future Long Video Generation

- **作者**：Yiping Wang; Xuehai He; Kuan Wang; Luyao Ma; Jianwei Yang; Shuohang Wang; Simon Shaolei Du; Yelong Shen
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：CVPR 2025（论文版）
- **项目／代码／数据**：[项目/演示页面](https://ypwang61.github.io/project/StoryEval)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：10页；SHA-256：`cba490f9ce2d4f8ebd0372826b3fcca803dbd37770ce22a2f3df199f55bac24b`

### 中文摘要

用2–4个连续事件的短故事提示测量视频模型是否完成所要求事件，补充审美与时空一致性等细节指标。

### 核心贡献

StoryEval423提示、7类场景，逐事件自动核验与一致投票。

### 实现边界

completion rate是已完成事件比例，不是全故事全对比例；视频时长有限，不能直接代表分钟级长叙事表现。

### Method／方法

检索真实视频/人工构思提示，VLM如GPT4o和LLaVAOV72B核验每一事件并投票，与人工评价检查一致性。

### Results／主要结果

11模型无一平均事件完成率超过50%，hard类无一超过20%；Kling1.5总体40.1%，Pika1.5为19.4%；高传统时间一致性分数仍可伴随低事件完成。

### Shortcomings／局限与可能不足

【解读】VLM评分存在误判，一致投票也可能共同偏差；可生成时长/动作复杂度、提示类别和模型版本影响排名。

### 证据定位

PDF §2–3、表1–2、§3.1 pp.7–8。

### Abstract

The current state-of-the-art video generative models can produce commercial-grade videos with highly realistic details. However, they still struggle to coherently present multiple sequential events in the stories specified by the prompts, which is foreseeable an essential capability for future long video generation scenarios. For example, top T2V generative models still fail to generate a video of the short simple story ”how to put an elephant into a refrigerator. ” While existing detail-oriented benchmarks primarily focus on fine-grained metrics like aesthetic quality and spatial-temporal consistency, they fall short of evaluating models’ abilities to handle event-level story presentation. To address this gap, we introduce StoryEval, a story-oriented benchmark specifically designed to assess text-to-video (T2V) models’ story-completion capabilities. StoryEval features 423 prompts spanning 7 classes, each representing short stories composed of 2–4 consecutive events. We employ Vision-Language Models, such as GPT-4o and LLaVA-OV-Chat-72B, to verify the completion of each event in the generated videos, applying a unanimous voting method to enhance reliability. Our methods ensure high alignment with human evaluations, and the evaluation of 11 models reveals its challenge, with none exceeding an average story-completion rate of 50%. StoryEval provides a new benchmark for advancing T2V models and highlights the challenges and opportunities in developing next-generation solutions for coherent storydriven video generation. Project website is available at https://ypwang61.github.io/project/StoryEval.

<a id="p140"></a>
## P140 · VideoAuteur: Towards Long Narrative Video Generation

- **作者**：Junfei Xiao; Feng Cheng; Lu Qi; Liangke Gui; Yang Zhao; Shanchuan Lin; Jiepeng Cen; Zhibei Ma; Alan Yuille; Lu Jiang
- **时间**：2025年；具体日期、卷期及稿件状态见下一项。本地独立修订日期未明确。
- **发表平台／版本状态**：ICCV 2025（论文版）
- **项目／代码／数据**：[项目/演示页面](https://videoauteur.github.io)

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：11页；SHA-256：`e4087daed3ec8e414c07c7654a84cad474d99d436bbe67eaa7f5e1ae5f857671`

### 中文摘要

面向烹饪长叙事视频构建数据和分层生成流程，交错语言/视觉导演规划步骤，滚动关键帧渲染再生成视频。

### 核心贡献

烹饪数据整理、Long Narrative Video Director、滚动历史条件渲染及视觉embedding对齐。

### 实现边界

实证集中烹饪域；自动VLM检查和人评不保证食谱正确/操作安全；不是任意电影场景通用导演。

### Method／方法

导演交替生成语言状态与视觉embedding，以滚动参考图条件DiT渲染关键帧，正则化视觉embedding驱动视频模型。

### Results／主要结果

表3 YouCook2 CLIP-T25.9→26.4、FVD557.7→512.6；HowTo100M26.6→27.3、541.1→520.7；去掉embedding正则反而更差，说明对齐是必要因素。

### Shortcomings／局限与可能不足

【解读】域特定数据、阶段间误差累积、角色/步骤的长程一致仍受基础生成器限制，需更广题材和事件完成验证。

### 证据定位

PDF §3–5、表3 pp.6–7、§6。

### Abstract

Recent video generation models have shown promising results in producing high-quality video clips lasting several seconds. However, these models face challenges in generating long sequences that convey clear and informative events, limiting their ability to support coherent narrations. In this paper, we present a large-scale cooking video dataset designed to advance long-form narrative generation in the cooking domain. We validate the quality of our proposed dataset in terms of visual fidelity and textual caption accuracy using state-of-the-art Vision-Language Models (VLMs) and video generation models, respectively. We further introduce a Long Narrative Video Director to enhance both visual and semantic coherence in generated videos and emphasize the role of aligning visual embeddings to achieve improved overall video quality. Our method demonstrates substantial improvements in generating visually detailed and semantically aligned keyframes, supported by finetuning techniques that integrate text and image embeddings within the video generation process.

<a id="p141"></a>
## P141 · Watch-And-Help: A Challenge for Social Perception and Human-AI Collaboration

- **作者**：Xavier Puig; Tianmin Shu; Shuang Li; Zilin Wang; Yuan-Hong Liao; Joshua B. Tenenbaum; Sanja Fidler; Antonio Torralba
- **时间**：初稿2020；本地arXiv:2010.09890v2，2021-05-03。
- **发表平台／版本状态**：ICLR 2021；本地PDF首页明确标注正式会议。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2010.09890v2)
- **项目／代码／数据**：[Watch-And-Help代码](https://github.com/xavierpuigf/watch_and_help) · [VirtualHome模拟器代码](https://github.com/xavierpuigf/virtualhome)；原项目页在2026-09-16核验时存在证书域名不匹配，网页入口改用维护者代码仓库。

- **主题**：XR与人机协作
- **PDF版本**：23页；SHA-256：`35fd46183bb785e6f8eb0303083ca59036322f09fc4b20bea243bfc52d84486f`

### 中文摘要

提出先观察、后协助的两阶段家庭任务：助手从另一智能体的一次示范中推断目标，再在不同房间配置中协助完成同一目标。VirtualHome-Social支持多智能体互动，并以规划、学习基线和真人实验评估社会感知与协作效率。

### 核心贡献

将目标推断与跨场景协作联合纳入可复现基准；提供多智能体家庭仿真、任务划分、成功率/加速比指标，并检验仿真人类与真实参与者配合时的结论是否一致。

### 实现边界

Watch阶段学习目标，Help阶段执行；本文基线使用视野内物体的真值符号状态，并非端到端像素感知。目标以预设谓词组合表示，低层动作受模拟器限制；未实现在线澄清对话、XR头显取证或持续更新目标推断。

### Method／方法

Transformer编码示范中的物体状态，再经LSTM与时间聚合预测目标谓词；对比层次规划HP、层次RL及学习高层策略与规划低层动作的Hybrid。规划器考虑Alice的未来计划，降低重复劳动与动作冲突。训练1,011个任务；两个测试集各100个任务，保留未见公寓及谓词组合，单轮最多250步。

### Results／主要结果

Test-1目标识别precision/recall为0.85/0.96；仅看最终观察为0.79/0.75；输入Alice动作则为0.99/0.99，说明结果明显依赖输入条件。Test-2组合任务降至0.68/0.64。HP和Hybrid能提供帮助，随机目标HP在40%的回合产生目标冲突。真人单人实验6人，协作实验12人、90次试验：三种助手的总体排序与仿真评估一致。

### Shortcomings／局限与可能不足

作者指出在线目标推断和智能体通信仍是后续方向；错误目标可能使强规划器帮倒忙。研究判断：符号真值感知、较小真人样本和有限家庭谓词空间限制向真实XR迁移，成功率不能直接代表人类注意力成本或请求行动的可接受性。

### 证据定位

PDF pp.3–5：任务、输入条件与基线；pp.6–7：目标识别和协作结果；pp.8–9及附录D：真人实验与边界。

### Abstract

In this paper, we introduce Watch-And-Help (WAH), a challenge for testing social intelligence in agents. In WAH, an AI agent needs to help a human-like agent perform a complex household task efficiently. To succeed, the AI agent needs to i) understand the underlying goal of the task by watching a single demonstration of the human-like agent performing the same task (social perception), and ii) coordinate with the human-like agent to solve the task in an unseen environment as fast as possible (human-AI collaboration). For this challenge, we build VirtualHomeSocial, a multi-agent household environment, and provide a benchmark including both planning and learning based baselines. We evaluate the performance of AI agents with the human-like agent as well as with real humans using objective metrics and subjective user ratings. Experimental results demonstrate that the proposed challenge and virtual environment enable a systematic evaluation on the important aspects of machine social intelligence at scale.

<a id="p142"></a>
## P142 · Alchemy: A Benchmark and Analysis Toolkit for Meta-Reinforcement Learning Agents

- **作者**：Jane X. Wang; Michael King; Nicolas Porcel; Zeb Kurth-Nelson; Tina Zhu; Charlie Deck; Peter Choy; Mary Cassin; Malcolm Reynolds; Francis Song; Gavin Buttimore; David P. Reichert; Neil Rabinowitz; Loic Matthey; Demis Hassabis; Alexander Lerchner; Matthew Botvinick（Wang与King共同一作）
- **时间**：初稿2021；本地arXiv:2102.02926v3，2021-10-20。
- **发表平台／版本状态**：NeurIPS 2021 Datasets and Benchmarks Track；本地首页有会议标注。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2102.02926v3)
- **项目／代码／数据**：[资源 1](https://github.com/deepmind/dm_alchemy)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：24页；SHA-256：`af6e9cd02d6a8d10c3a76e30b09c56e39b10fc4f265338f8e3b7142a15dedf9d`

### 中文摘要

提出具有可分析潜在因果结构的元强化学习环境Alchemy。智能体通过试用药水、改变石头属性来发现每个episode的化学规则，并利用跨trial知识提高收益；同时提供符号版本、理想观察者和行为诊断工具，定位强化学习未能学会哪些抽象规律。

### 核心贡献

兼顾组合任务丰富度和机制透明性，使环境机制、belief与参考策略可计算；把总体分数拆解为结构发现、信息利用和动作执行的能力诊断。

### 实现边界

每个episode包含10个trial；机制在episode内固定，跨episode重新采样，共167,424种预设化学配置。它研究已有真值机制的发现，不是创作者尚未定义规则的开放补全。理想观察者仅对当前trial做精确前瞻，并非对整个10-trial episode进行全局最优规划。

### Method／方法

Unity第一人称3D环境与共享机制的符号环境；药水在三维属性立方体上改变石头状态，目标是提高投入坩埚的石头价值。训练IMPALA/LSTM与VMPO/Transformer-XL基线，另实现维护可能机制集合并搜索动作的理想观察者。通过额外提供真值机制或Bayesian belief、增加预测辅助损失，诊断感知与推断瓶颈。

### Results／主要结果

表1在1,000个测试episode上报告均值±标准误：IMPALA 140.2±1.5，VMPO 156.2±1.6，符号VMPO 155.4±1.6，随机启发式145.7±1.5，理想观察者284.4±1.6，oracle 288.5±1.5。基线虽训练2×10^10步仍远低于参考策略；提供显式belief/机制显著改善表现，说明困难不只来自视觉控制。

### Shortcomings／局限与可能不足

机制族人为设计，主要强调深入诊断而非跨领域覆盖；理想观察者的搜索复杂度限制更大环境。基线使用特权信息的增强实验仅用于诊断，不算解决原任务；也未证明对自然科学开放发现或用户改写规则的泛化。

### 证据定位

PDF pp.4–5：任务机制、规模与表1；p.5脚注6：理想观察者的trial内边界；pp.6–10：训练、诊断和讨论。

### Abstract

There has been rapidly growing interest in meta-learning as a method for increasing the flexibility and sample efficiency of reinforcement learning. One problem in this area of research, however, has been a scarcity of adequate benchmark tasks. In general, the structure underlying past benchmarks has either been too simple to be inherently interesting, or too ill-defined to support principled analysis. In the present work, we introduce a new benchmark for meta-RL research, emphasizing transparency and potential for in-depth analysis as well as structural richness. Alchemy is a 3D video game, implemented in Unity, which involves a latent causal structure that is resampled procedurally from episode to episode, affording structure learning, online inference, hypothesis testing and action sequencing based on abstract domain knowledge. We evaluate a pair of powerful RL agents on Alchemy and present an in-depth analysis of one of these agents. Results clearly indicate a frank and specific failure of meta-learning, providing validation for Alchemy as a challenging benchmark for meta-RL. Concurrent with this report, we are releasing Alchemy as public resource, together with a suite of analysis tools and sample agent trajectories.

<a id="p143"></a>
## P143 · Interactive Visual Reasoning under Uncertainty

- **作者**：Manjie Xu; Guangyuan Jiang; Wei Liang; Chi Zhang; Yixin Zhu（Xu与Jiang共同一作）
- **时间**：初稿2022；本地arXiv:2206.09203v2，2023-10-29。文件名的22对应初稿，不是正式会议年。
- **发表平台／版本状态**：NeurIPS 2023 Datasets and Benchmarks Track；本地首页明确标注。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2206.09203v2)
- **项目／代码／数据**：[资源 1](https://sites.google.com/view/ivre)

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：24页；SHA-256：`033de0d7f6d538c695e793bd8cf3786452225117d3899019655999dc8a7ea5cc`

### 中文摘要

IVRE把Blicket检测变成主动视觉推理任务：仅凭初始场景不能知道所有物体是否会使机器激活，智能体必须提出新实验、根据结果更新belief，并在有限次数内解除不确定性。对符号、像素、LLM和人类基线的比较显示，实验选择和证据整合均构成明显瓶颈。

### 核心贡献

提供可干预、可反馈的视觉推理环境，联合评估假设更新与实验效率；用共享底层机制的符号/像素版本区分推理难度与感知难度。

### 实现边界

9个物体、其中1–4个Blicket，4个初始context面板，总时步上限T=10；机制为至少一个Blicket出现即激活的OR规则，且告知Blicket总数。行动简化为选取物体集合，不含机器人运动控制、用户代执行、空间提示或注意力中断。

### Method／方法

智能体同时输出下一实验的物体选择与各物体Blicketness belief；观测为二进制向量或160×120合成图。奖励联合全体识别成功、每步成本及与搜索oracle belief的Jensen–Shannon距离。对比随机/Bayes/逐个测试/NOTEARS/搜索组合、actor-critic RL与GPT-3.5/4。

### Results／主要结果

PDF表2的episode全物体识别准确率：人类98.15%，Search-Naive 83.80%，符号DDPG-Re 46.03%，GPT-4 26%，GPT-3.5 11%；像素DDPG与TD3仅0.72%/0.31%。机器基线通常评估10,000个随机episode，LLM评估100个，不能把这些值视作等样本量对照；人类为单独实验。

### Shortcomings／局限与可能不足

作者明确指出合成场景和简单因果结构的限制；最佳启发式依赖OR机制先验及逐个实验策略。研究判断：该基准已经覆盖主动取证，XR研究需进一步处理行动由用户执行、观察受到提示影响与任务成本，不能只把同一任务搬进头显。

### 证据定位

PDF pp.4–5：环境及奖励；pp.6–7：基线和人类设置；p.8表2：结果；pp.9–10：分析与明确局限。

### Abstract

One of the fundamental cognitive abilities of humans is to quickly resolve uncertainty by generating hypotheses and testing them via active trials. Encountering a novel phenomenon accompanied by ambiguous cause-effect relationships, humans make hypotheses against data, conduct inferences from observation, test their theory via experimentation, and correct the proposition if inconsistency arises. These iterative processes persist until the underlying mechanism becomes clear. In this work, we devise the IVRE (pronounced as ivory) environment for evaluating artificial agents’ reasoning ability under uncertainty. IVRE is an interactive environment featuring rich scenarios centered around Blicket detection. Agents in IVRE are placed into environments with various ambiguous action-effect pairs and asked to determine each object’s role. They are encouraged to propose effective and efficient experiments to validate their hypotheses based on observations and actively gather new information. The game ends when all uncertainties are resolved or the maximum number of trials is consumed. By evaluating modern artificial agents in IVRE, we notice a clear failure of today’s learning methods compared to humans. Such inefficacy in interactive reasoning ability under uncertainty calls for future research in building human-like intelligence.

<a id="p144"></a>
## P144 · Semantic Uncertainty: Linguistic Invariances for Uncertainty Estimation in Natural Language Generation

- **作者**：Lorenz Kuhn; Yarin Gal; Sebastian Farquhar
- **时间**：本地arXiv:2302.09664v3，2023-04-15。
- **发表平台／版本状态**：ICLR 2023；本地首页明确标注。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2302.09664v3)
- **项目／代码／数据**：[资源 1](https://github.com/lorenzkuhn/semantic_uncertainty)
- **版本关系**：与P148为前后续工作，内容不同，均保留。

- **主题**：AI方法与评测
- **PDF版本**：19页；SHA-256：`0cc1c0b189dbe6ccdf12deb2f11761ff183ee4813a04f7add8b28ec35375f330`

### 中文摘要

针对同一含义可有多种语言表达的问题，将LLM输出不确定性从token序列层提升到语义层：采样多个答案，将语义等价答案聚类，再对含义的概率分布计算熵。无需重新训练被测生成模型，在自由回答QA上更有效预测答案是否可靠。

### 核心贡献

提出semantic entropy及基于双向蕴含的语义聚类；分析采样温度、表达长度、样本数如何影响语言不确定性估计，避免把措辞差异误当作事实分歧。

### 实现边界

实验以OPT 2.7B–30B、CoQA开放书QA和TriviaQA闭卷QA为主；需要多次生成、序列概率以及用于双向蕴含判断的DeBERTa模型。无监督指无需该任务的正确性标签训练不确定性估计器，不表示系统完全没有经过监督训练的组件。

### Method／方法

对同一问题采样M个答案；将问题与答案一起输入NLI模型，在两个方向均为entailment时聚为同一含义；聚合簇内序列概率并估计语义熵。对照普通/长度归一化预测熵、词面相似度和p(True)，用错误检测AUROC评价。

### Results／主要结果

表2中30B设置：CoQA语义熵AUROC 0.77，单纯不同含义数量为0.66；TriviaQA分别0.83/0.79。人工核对聚类等价判断准确率为CoQA 95.5%、TriviaQA 92.7%。更多样本和合适的中间温度通常有利，文中主要采样温度0.5；AUROC衡量排序辨别能力，不能当作答案正确率。

### Shortcomings／局限与可能不足

语义聚类会出错，最坏情况下需要O(M²)对比较；多次生成增加推理成本。作者指出不防止模型欺骗，长篇摘要等任务还需更强语义等价判断。研究判断：稳定重复的错误可能低熵；创作中多个均合规则的答案也可能高熵，不能直接等同于需要纠错。

### 证据定位

PDF pp.4–6：语义熵与双向蕴含；p.7：模型、数据及评价；p.8表2及p.9：结果、采样敏感性与讨论。

### Abstract

We introduce a method to measure uncertainty in large language models. For tasks like question answering, it is essential to know when we can trust the natural language outputs of foundation models. We show that measuring uncertainty in natural language is challenging because of ‘semantic equivalence’—different sentences can mean the same thing. To overcome these challenges we introduce semantic entropy—an entropy which incorporates linguistic invariances created by shared meanings. Our method is unsupervised, uses only a single model, and requires no modifications to ‘off-the-shelf’ language models. In comprehensive ablation studies we show that the semantic entropy is more predictive of model accuracy on question answering data sets than comparable baselines.

<a id="p145"></a>
## P145 · Generative Agent-Based Modeling with Actions Grounded in Physical, Social, or Digital Space Using Concordia

- **作者**：Alexander Sasha Vezhnevets; John P. Agapiou; Avia Aharon; Ron Ziv; Jayd Matyas; Edgar A. Duéñez-Guzmán; William A. Cunningham; Simon Osindero; Danny Karmon; Joel Z. Leibo
- **时间**：本地arXiv:2312.03664v2，2023-12-13；封面标注December 2023。
- **发表平台／版本状态**：Google DeepMind/Google Research技术报告、arXiv预印本；本地版本未标明正式会议或期刊。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2312.03664v2)
- **项目／代码／数据**：[资源 1](https://github.com/google-deepmind/concordia)

- **主题**：世界机制与演化
- **PDF版本**：32页；SHA-256：`ac0a23ef187ebef1820b8aebc19d2610035b1f234527b9f854151cb77ad966fb`

### 中文摘要

Concordia是构建生成式多智能体模拟的框架。智能体以组件和关联记忆组织行为，由Game Master维护环境并将自然语言动作转为情境后果或结构化/API操作，从而连接社会互动、模拟物理状态和数字服务。论文讨论应用场景及验证模拟可信度的方法。

### 核心贡献

以可组合组件统一LLM调用、记忆检索、角色行为和Game Master环境更新；支持将自然语言社会行为接到明确的外部状态变量与数字操作，提供开放实现与建模讨论。

### 实现边界

自然语言GM对物理合理性的判断属于语言模型模拟；只有明确接入程序/状态变量的部分拥有相应执行语义。论文包含已实现案例与潜在应用设想，不能把法律/规范涌现、真实用户预测、所有外部应用接入都视为已验证功能。

### Method／方法

每个智能体用长期关联记忆与工作记忆组件回答身份、情境、适当行动等问题；GM解析尝试动作、更新状态并向不同角色发送其可见观察。数字案例通过嵌套PhoneGameMaster和PhoneUniverse选择app、函数和参数，再更新应用状态及通知。

### Results／主要结果

主要结果为框架与定性案例：展示多智能体叙事、数字手机/日历操作的调用流程，以及可接入确定性状态更新的模拟方式。本地报告未提供统一任务集上的成功率、基线消融或真实人类行为预测误差，不能据此声称社会模拟已达真实预测精度。

### Shortcomings／局限与可能不足

作者强调必须针对具体研究问题检验泛化和algorithmic fidelity，LLM可能呈现刻板印象；用同一模型生成并解释模拟亦不能替代外部验证。研究判断：语言层一致性不保证长期因果正确性或改规则后的局部更新，开放动作解析也可能产生累积状态错误。

### 证据定位

PDF pp.5–10：组件、GM及实验设计；pp.10–11：模拟验证边界；pp.16–19：数字服务实例与明确标为潜在的应用；后续章节：讨论。

### Abstract

Agent-based modeling has been around for decades, and applied widely across the social and natural sciences. The scope of this research method is now poised to grow dramatically as it absorbs the new affordances provided by Large Language Models (LLM)s. Generative Agent-Based Models (GABM) are not just classic Agent-Based Models (ABM)s where the agents talk to one another. Rather, GABMs are constructed using an LLM to apply common sense to situations, act “reasonably”, recall common semantic knowledge, produce API calls to control digital technologies like apps, and communicate both within the simulation and to researchers viewing it from the outside. Here we present Concordia, a library to facilitate constructing and working with GABMs. Concordia makes it easy to construct language-mediated simulations of physically- or digitally-grounded environments. Concordia agents produce their behavior using a flexible component system which mediates between two fundamental operations: LLM calls and associative memory retrieval. A special agent called the Game Master (GM), which was inspired by tabletop role-playing games, is responsible for simulating the environment where the agents interact. Agents take actions by describing what they want to do in natural language. The GM then translates their actions into appropriate implementations. In a simulated physical world, the GM checks the physical plausibility of agent actions and describes their effects. In digital environments simulating technologies such as apps and services, the GM may handle API calls to integrate with external tools such as general AI assistants (e.g., Bard, ChatGPT), and digital apps (e.g., Calendar, Email, Search, etc.). Concordia was designed to support a wide array of applications both in scientific research and for evaluating performance of real digital services by simulating users and/or generating synthetic data.

<a id="p146"></a>
## P146 · ExpertAF: Expert Actionable Feedback from Video

- **作者**：Kumar Ashutosh; Tushar Nagarajan; Georgios Pavlakos; Kris Kitani; Kristen Grauman
- **时间**：初稿2024；本地arXiv:2408.00672v3，2025-04-11。
- **发表平台／版本状态**：CVPR 2025；以CVF正式论文入口核实。
- **论文链接**：[论文/发表记录 1](https://openaccess.thecvf.com/content/CVPR2025/papers/Ashutosh_ExpertAF_Expert_Actionable_Feedback_from_Video_CVPR_2025_paper.pdf) · [论文/发表记录 2](https://arxiv.org/abs/2408.00672v3)
- **项目／代码／数据**：[资源 1](https://vision.cs.utexas.edu/projects/ExpertAF/)

- **主题**：XR与人机协作
- **PDF版本**：18页；SHA-256：`cf0af650338c144587b2147b95007535684c74908d1499a87c87f67266954b56`

### 中文摘要

从学习者执行体育动作的视频和3D姿态生成可操作的指导，包括指出优缺点的专家式文字反馈、检索正确示范，以及生成修正后的3D姿态。利用Ego-Exo4D专家评论构建弱监督错误—正确动作配对，训练统一视频、姿态与文本模型。

### 核心贡献

将技能评价从单一分数推进到具体纠正建议与示范；贡献弱监督配对数据和支持三类输出的多模态自回归模型。

### 实现边界

实际评估篮球、足球、攀岩三类身体技能；主设置输入包含ego/exo视频与3D姿态，假定一个主要动作执行者。输出视频是检索已有示范，生成的是姿态序列；新专家视频生成留作未来。没有进行长期训练者技能提升或实时XR闭环试验。

### Method／方法

Llama3-70B压缩专家评论并标注身体部位/正确性；按技能等级匹配错误与正确演示，用PA-MPJPE对齐时间并过滤。InternVideo2视频特征、姿态codebook和文本映射至Llama3-8B，联合学习评论、示范检索与姿态token生成。训练25,505个tuple，人工核验测试1,272个。

### Results／主要结果

表1：ExpertAF的BLEU-4/METEOR/ROUGE-L为44.9/49.6/54.6；示范检索recall@50为19.1%、median rank 158，优于LLaVA-FT w/pose的18.0%/172；姿态误差PA-MPJPE由该基线150mm降至135mm。每场景5名评价者的1–4分质量评分也优于基线。带正确示范等特权输入的full-sup行不可与主设置混用。

### Shortcomings／局限与可能不足

作者指出对疲劳等不可直接见到的状态较弱，自动提取姿态有噪声；配对真值只覆盖可能错误中的一部分。研究判断：质量偏好与姿态距离未证明建议能在实际交互中改善技能，也未评估提示导致的注意分配或后续观察变化。

### 证据定位

PDF pp.3–6：任务、配对数据、编码器及训练；p.7表1：三类输出结果及特权输入说明；p.8：人评和失败案例。

### Abstract

Feedback is essential for learning a new skill or improving one’s current skill-level. However, current methods for skill-assessment from video only provide scores or compare demonstrations, leaving the burden of knowing what to do differently on the user. We introduce a novel method to generate actionable feedback (AF) from video of a person doing a physical activity, such as basketball or soccer. Our method takes a video demonstration and its accompanying 3D body pose and generates (1) free-form expert commentary describing what the person is doing well and what they could improve, and (2) a visual expert demonstration that incorporates the required corrections. We show how to leverage Ego-Exo4D’s [29] videos of skilled activity and expert commentary together with a strong language model to create a weakly-supervised training dataset for this task, and we devise a multimodal video-language model to infer coaching feedback. Our method is able to reason across multi-modal input combinations to output fullspectrum, actionable coaching—expert commentary, expert video retrieval, and expert pose generation—outperforming strong vision-language models on both established metrics and human preference studies.

<a id="p147"></a>
## P147 · DreamGarden: A Designer Assistant for Growing Games from a Single Prompt

- **作者**：Sam Earle; Samyak Parajuli; Andrzej Banburski-Fahey
- **时间**：初稿2024；正式会议2025-04；本地arXiv:2410.01791v2，2025-11-22。文件名24_CHI不能用作正式发表年份。
- **发表平台／版本状态**：CHI 2025，获Best Paper Award（微软作者机构记录）。本地30页arXiv版本仍含占位DOI/ISBN，不把这些占位符当成正式标识。
- **论文链接**：[论文/发表记录 1](https://www.microsoft.com/en-us/research/publication/dreamgarden-a-designer-assistant-for-growing-games-from-a-single-prompt/?lang=ko-kr) · [论文/发表记录 2](https://arxiv.org/abs/2410.01791v2)
- **项目／代码／数据**：[资源 1](https://www.microsoft.com/en-us/research/project/speaking-the-world-into-existence/publications/)；作者机构的相关项目入口；不据此声称全部代码已开源。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：30页；SHA-256：`e1a2ce4f52bc1ddbb0c9a63c70c4e9fd95901acae67ae9ffe86f4ae447e0e8a6`

### 中文摘要

从一个开放的梦境、场景或游戏构想出发，LLM规划器逐层分解任务，调用代码和素材子模块在Unreal Engine内构建环境。用户通过可视化计划树扩展、剪枝、查看中间产物及编辑反馈，与自主生成过程协作。

### 核心贡献

将分层计划、可编辑游戏引擎资产、编译/运行/视觉反馈和节点界面整合为创作助手，研究用户在主动编辑与旁观生成之间切换的交互方式。

### 实现边界

实现C++ Actor、场景布局、素材生成/检索与UE内运行；实验主要限制为无需玩家的0-player模拟。修改节点会撤回相关实现及顺序上后续任务，并重新执行；不是精确因果依赖分析，也没有证明任意规则编辑后的最小后果更新。视觉自动评估只看启动后前6秒的6张截图。

### Method／方法

GPT-4o将seed prompt递归展开为计划树，叶节点分派给代码/素材模块；代码经历编译、布局加载、运行、截图评价的反复修正。GUI允许变更叶节点状态、直接改代码或反馈，再继续生成。N=10、每次最多45分钟的形成性可用性研究记录访谈、操作与系统日志。

### Results／主要结果

研究参与者认可规划和原型用途，部分人认为计划树本身就有价值；观察到剪枝、扩展与自定义反馈能够改变后续产物。但对复杂游戏机制的能力仍持保留态度。默认超参数下完整流程约1小时，情绪体验有正负两面。论文以定性系统观察和小样本可用性研究为主，没有受控比较的规则正确率或开发效率增益。

### Shortcomings／局限与可能不足

作者报告过度分解、请求超出模块能力的任务、代码/素材失败、等待长以及中间结果难以消化等问题；骨骼动画不在当前能力范围。研究判断：这已覆盖创作计划补全、可视化与人工修改，后续AI贡献需要独立评测约束满足、改动传播或有用多样性。

### 证据定位

PDF pp.6–10：模块、代码循环、剪枝与实验设计；p.8：6秒视觉评价边界；pp.11–15：系统结果、用户主题与耗时；pp.15–16：讨论。

### Abstract

Coding assistants are increasingly leveraged in game design, both generating code and making high-level plans. To what degree can these tools align with developer workflows, and what new modes of human-computer interaction can emerge from their use? We present DreamGarden, an AI system capable of assisting with the development of diverse game environments in Unreal Engine. At the core of our method is an LLM-driven planner, capable of breaking down a single, high-level prompt—a dream, memory, or imagined scenario provided by a human user—into a hierarchical action plan, which is then distributed across specialized submodules facilitating concrete implementation. This system is presented to the user as a garden of plans and actions, both growing independently and responding to user intervention via seed prompts, pruning, and feedback. Through a user study, we explore design implications of this system, charting courses for future work in semi-autonomous assistants and open-ended simulation design.

<a id="p148"></a>
## P148 · Detecting Hallucinations in Large Language Models Using Semantic Entropy

- **作者**：Sebastian Farquhar; Jannik Kossen; Lorenz Kuhn; Yarin Gal（前三位共同贡献）
- **时间**：2024-06-19在线发表；Nature卷期日期2024-06-20；本地为期刊排版版本。
- **发表平台／版本状态**：Nature 630, 625–630 (2024)，DOI:10.1038/s41586-024-07421-0。
- **论文链接**：[论文/发表记录 1](https://doi.org/10.1038/s41586-024-07421-0)
- **项目／代码／数据**：[资源 1](https://github.com/jlko/semantic_uncertainty) · [资源 2](https://github.com/jlko/long_hallucinations) · [资源 3](https://doi.org/10.5281/zenodo.10964366)
- **版本关系**：P144的语义熵方向后续工作；增加离散估计和长篇事实检测等实验，非重复文件。

- **主题**：AI方法与评测
- **PDF版本**：12页；SHA-256：`52e7ad2740b25cc7697b69e12d69ca0dde844eca9f79dfa304a79be5b0e99c1a`

### 中文摘要

研究幻觉中的一种特定机制：同一提示下随机产生不同且错误的事实性回答。通过聚合同义表达后的语义熵识别这种confabulation，并设计不依赖输出概率的离散版本和长段落事实拆分流程，支持跨任务判断何时不宜直接信任回答。

### 核心贡献

明确区分随机编造与稳定的系统性错误；将语义不确定性扩展到不同模型、QA/数学任务及GPT-4传记段落，并支持只有文本输出的黑箱接口。

### 实现边界

定位的是随采样变化的confabulations，不能保证事实正确，也不处理所有训练错误、欺骗或系统性推理失误。方法为生成后的检测/选择性回答；没有自动获取新环境证据或学习交互式取证策略。

### Method／方法

对同一问题多次采样，用双向蕴含判断将回答按含义聚类；有概率时聚合语义概率，无概率时用簇的样本频率估计离散语义熵。长文本先拆分事实陈述，再围绕陈述生成问题、重采样回答并汇总不确定性；以AUROC和拒答—准确率曲线等评估。

### Results／主要结果

30个模型×任务组合的平均AUROC：语义熵0.790，naive entropy 0.691，P(True) 0.698，embedding regression 0.687。离散版本总体接近有概率版本；GPT-4长篇传记实验的错误检测AUROC/AURAC也优于比较基线，但拒绝20%以上高风险回答后，P(True)在剩余回答准确率上略占优。上述指标不是模型本身的QA准确率。

### Shortcomings／局限与可能不足

作者明确不保证系统性错误的事实性；需要多次采样与语义判定，有推理成本及判定误差。研究判断：对于架空创作，多个合法结局的语义分歧应作为设计多样性，不应直接标记为幻觉；需区分规则违反和合法分支。

### 证据定位

PDF p.1：confabulation定义、发表日期与边界；pp.2–5：实验、30组合均值及长文本结果；pp.7–10：方法细节；p.11：代码地址。

### Abstract

Large language model (LLM) systems, such as ChatGPT1 or Gemini2, can show impressive reasoning and question-answering capabilities but often ‘hallucinate’ false outputs and unsubstantiated answers3,4. Answering unreliably or without the necessary information prevents adoption in diverse fields, with problems including fabrication of legal precedents5 or untrue facts in news articles6 and even posing a risk to human life in medical domains such as radiology7. Encouraging truthfulness through supervision or reinforcement has been only partially successful8. Researchers need a general method for detecting hallucinations in LLMs that works even with new and unseen questions to which humans might not know the answer. Here we develop new methods grounded in statistics, proposing entropy-based uncertainty estimators for LLMs to detect a subset of hallucinations—confabulations—which are arbitrary and incorrect generations. Our method addresses the fact that one idea can be expressed in many ways by computing uncertainty at the level of meaning rather than specific sequences of words. Our method works across datasets and tasks without a priori knowledge of the task, requires no task-specific data and robustly generalizes to new tasks not seen before. By detecting when a prompt is likely to produce a confabulation, our method helps users understand when they must take extra care with LLMs and opens up new possibilities for using LLMs that are otherwise prevented by their unreliability.

<a id="p149"></a>
## P149 · Learning to Clarify: Multi-turn Conversations with Action-Based Contrastive Self-Training

- **作者**：Maximillian Chen; Ruoxi Sun; Tomas Pfister; Sercan Ö. Arık（按本地v2顺序）
- **时间**：初稿2024-05-31；本地arXiv:2406.00222v2，2025-07-27。
- **发表平台／版本状态**：ICLR 2025；OpenReview正式会议版本及Google Research记录核实。
- **论文链接**：[论文/发表记录 1](https://openreview.net/forum?id=SIE6VFps9x) · [论文/发表记录 2](https://research.google/pubs/learning-to-clarify-multi-turn-conversations-with-action-based-contrastive-self-training/) · [论文/发表记录 3](https://arxiv.org/abs/2406.00222v2)
- **项目／代码／数据**：[资源 1](https://github.com/google-research/google-research/tree/master/learning_to_clarify)

- **主题**：XR与人机协作、AI方法与评测
- **PDF版本**：45页；SHA-256：`22efec0f1c73fc160254b68a9119b9cbfeee39649e6ed035f38fc7530a10da82`

### 中文摘要

针对LLM在歧义请求中直接猜测或含糊回答的问题，提出ACT，用询问澄清与直接回答等不同对话动作构造偏好对，再结合当前策略采样和多轮用户模拟训练，使少量对话数据也能教会模型何时澄清及如何完成任务。

### 核心贡献

把偏好学习从回答表面质量推进到动作选择及多轮任务后果；提出quasi-online DPO训练流程和AmbigSQL歧义SQL任务，并评估缺少人工动作标签的设置。

### 实现边界

实验为PACIFIC表格QA、Abg-CoQA阅读QA、AmbigSQL；澄清依赖文本用户模拟器、动作分类器和任务结果判据。无动作标签版本仍使用伪标签及任务数据，不是无需监督。用户回答主要提供信息，不涉及执行物理动作以生成新证据。

### Method／方法

先根据正确/错误对话动作产生winning/losing响应；训练中从当前模型采样，识别动作是否正确。对正确动作继续模拟用户和助手对话，按最终语义/SQL执行结果更新偏好对，再进行DPO式优化。主模型Zephyr-7B，比较50/100/250条对话下的SFT、IRPO及提示基线。

### Results／主要结果

PACIFIC 50对话、相同Zephyr模型：动作Macro-F1从SFT 69.0升至ACT 82.2，澄清后F1从43.5升至57.2，trajectory F1从61.3升至61.9。AmbigSQL相同50对话设置，execution match由21.9升至43.6，澄清后由13.9升至38.1；但50对话的动作准确率仍低于IRPO（80.8 vs 91.0）。消融支持on-policy采样与多轮模拟的作用，不能概括为所有指标全面最佳。

### Shortcomings／局限与可能不足

研究判断：效果依赖模拟用户、动作伪标签及任务启发式的质量；对话数据效率不能等同于总体训练计算效率。未验证真实用户多轮体验、错误/拒答用户、行动代价与后续感知反馈；跨任务泛化应进一步检验。

### 证据定位

PDF pp.4–7：设定和ACT算法；p.8表1：PACIFIC；p.10表3：AmbigSQL；pp.11–12表4/5：无标签设置与消融；附录：模拟器和提示。

### Abstract

Large language models (LLMs), optimized through human feedback, have rapidly emerged as a leading paradigm for developing intelligent conversational assistants. However, despite their strong performance across many benchmarks, LLM-based agents might still lack conversational skills such as disambiguation – when they are faced with ambiguity, they often overhedge or implicitly guess users’ true intents rather than asking clarification questions. Under task-specific settings, high-quality conversation samples are often limited, constituting a bottleneck for LLMs’ ability to learn optimal dialogue action policies. We propose Action-Based Contrastive Self-Training (ACT), a quasi-online preference optimization algorithm based on Direct Preference Optimization (DPO), that enables data-efficient dialogue policy learning in multi-turn conversation modeling. We demonstrate ACT’s efficacy under in data-efficient tuning scenarios, even when there is no action label available, using multiple real-world conversational tasks: tabular-grounded question-answering, machine reading comprehension, and AmbigSQL, a novel task for disambiguating information-seeking requests for complex SQL generation towards data analysis agents. Additionally, we propose evaluating LLMs’ ability to function as conversational agents by examining whether they can implicitly recognize and reason about ambiguity in conversation. ACT demonstrates substantial conversation modeling improvements over standard tuning approaches like supervised fine-tuning and DPO.

<a id="p150"></a>
## P150 · WorldCoder, a Model-Based LLM Agent: Building World Models by Writing Code and Interacting with the Environment

- **作者**：Hao Tang; Darren Key; Kevin Ellis
- **时间**：初稿2024-02；本地arXiv:2402.12275v3，2024-09-20。
- **发表平台／版本状态**：NeurIPS 2024 Main Conference Track；正式proceedings核实。
- **论文链接**：[论文/发表记录 1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/820c61a0cd419163ccbd2c33b268816e-Abstract-Conference.html) · [论文/发表记录 2](https://arxiv.org/abs/2402.12275v3)
- **项目／代码／数据**：[资源 1](https://github.com/haotang1995/WorldCoder)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：65页；SHA-256：`55c47b1df146967ecab1933518783059885b693460d3ebbc7554aaec0eeb101f`

### 中文摘要

让LLM根据与环境的少量交互，编写可执行Python转移与奖励函数作为世界模型，再由规划器选择行动。模型既要解释已有经历，也应允许找到正收益计划；新证据揭示错误时修改代码，支持环境和目标迁移。

### 核心贡献

将环境知识显式表示成程序；把optimism under uncertainty写为程序与规划器之间的逻辑约束，以引导探索和修正奖励理解；展示可编辑程序模型的样本效率与迁移优势。

### 实现边界

确定性、符号离散状态；Sokoban/MiniGrid及转成符号MDP的ALFWorld。是从既有环境的观测学习模型，不是从任意创作者规则生成完整世界；代码可编辑不意味着已经评测规则编辑的局部保持、合法多样性或全部反事实后果。

### Method／方法

分离Python转移函数与目标条件奖励函数。模型需满足对所有已收集transition的拟合约束，以及存在可达正奖励轨迹的乐观约束。GPT-4根据不一致样本修补代码，REx决定优先改哪个候选；配合有限深度值迭代/MCTS规划、经验回放和少量随机探索。

### Results／主要结果

Sokoban约前50个动作即可建立基本世界模型；ReAct在基础关卡仅15%±8%成功。示例模型前置约40万LLM token后可用程序规划继续行动；预训练知识贡献被作者明确承认。加入传送门规则后仍能学习阻塞行为；MiniGrid迁移及稀疏奖励任务受益于乐观约束。ALFWorld可合成250余行模型，代表任务通常首个episode约20步探索后获得奖励（3 seeds），不是完整ALFWorld榜单成功率。

### Shortcomings／局限与可能不足

作者明确限制为确定性、符号离散环境；长程困难还受规划器限制（例如更难的5箱以上Sokoban）。程序合成和前置LLM计算成本较高，依赖预训练程序/游戏先验；拟合已见数据只验证样本覆盖部分，不能保证全状态正确。

### 证据定位

PDF pp.2–5：表示、约束与算法；pp.6–8图3–5：Sokoban、MiniGrid、ALFWorld结果；pp.9–10：局限；附录D/E：生成代码。

### Abstract

We give a model-based agent that builds a Python program representing its knowledge of the world based on its interactions with the environment. The world model tries to explain its interactions, while also being optimistic about what reward it can achieve. We define this optimism as a logical constraint between a program and a planner. We study our agent on gridworlds, and on task planning, finding our approach is more sample-efficient compared to deep RL, more compute-efficient compared to ReAct-style agents, and that it can transfer its knowledge across environments by editing its code.

<a id="p151"></a>
## P151 · COMBO: Compositional World Models for Embodied Multi-Agent Cooperation

- **作者**：Hongxin Zhang; Zeyuan Wang; Qiushi Lyu; Zheyuan Zhang; Sunli Chen; Tianmin Shu; Behzad Dariush; Kwonjoon Lee; Yilun Du; Chuang Gan（前三位共同一作）
- **时间**：初稿2024；本地arXiv:2404.10775v3，2025-04-16。文件名24_iclr与正式会议年不一致。
- **发表平台／版本状态**：ICLR 2025；本地PDF首页明确标注。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2404.10775v3)
- **项目／代码／数据**：[资源 1](https://umass-embodied-agi.github.io/COMBO/)

- **主题**：XR与人机协作、世界机制与演化
- **PDF版本**：24页；SHA-256：`3fb20948b81c1acfd733970019c5bd101909824fd9d24193dbfd96ec4c2209bc`

### 中文摘要

在各智能体只有第一人称局部观察的条件下，通过可组合视频世界模型预测联合动作后果，并配合他者意图估计与树搜索实现协作。先补全全局俯视状态，再将多智能体动作条件组合起来模拟未来，支持不同合作伙伴和人数。

### 核心贡献

组合式联合动作建模、针对智能体可达区域的损失加权，以及世界状态补全—意图预测—搜索规划的模块化系统；包含仿真基准和小规模真实人机协作。

### 实现边界

主要评估2–4个智能体的桌面拼图、食物组合、按钮取物任务；输入RGBD和相机矩阵，动作采用环境定义的操作。所谓任意人数的实验支持是4-agent训练向2/3-agent迁移，不是无限人数保证。真实机器人实验另用真实数据微调世界模型，仅5次试验。

### Method／方法

融合历次局部RGBD为俯视点云投影并用扩散补全；通过组合各智能体动作条件的扩散预测，并按其可达区域加权学习。VLM负责动作提议、意图跟踪和结果评分，再用树搜索选择计划。对异常高预测收益设置阈值以抑制利用世界模型幻觉。

### Results／主要结果

表1在每设置20个episode上，COMBO于TDW-Game两合作伙伴成功率均1.00，TDW-Cook为0.90/1.00；移除意图跟踪后分别0.65/0.60及0.80/0.80。2D-FetchQ的60次replay评价成功率81.3%，Co-GAIL为53.3%。真实人类—XArm拼图成功4/5，成功trial平均8.4步。表4预算扩大可改善表现，但该消融样本更小。

### Shortcomings／局限与可能不足

作者指出多次大模型推理使响应慢；状态补全、动作误解和视觉生成错误会影响规划。研究判断：共享真实空间的人机案例存在，但尚未检验头显视角、用户拒绝/延迟执行、提示改变证据分布或取证与主任务的注意力竞争。

### 证据定位

PDF pp.4–7：组合模型、区域损失及规划；pp.8–10表1–5：仿真结果与计算预算；pp.23–24附录D/表8：真实人机实验。

### Abstract

In this paper, we investigate the problem of embodied multi-agent cooperation, where decentralized agents must cooperate given only egocentric views of the world. To effectively plan in this setting, in contrast to learning world dynamics in a single-agent scenario, we must simulate world dynamics conditioned on an arbitrary number of agents’ actions given only partial egocentric visual observations of the world. To address this issue of partial observability, we first train generative models to estimate the overall world state given partial egocentric observations. To enable accurate simulation of multiple sets of actions on this world state, we then propose to learn a compositional world model for multiagent cooperation by factorizing the naturally composable joint actions of multiple agents and compositionally generating the video conditioned on the world state. By leveraging this compositional world model, in combination with Vision Language Models to infer the actions of other agents, we can use a tree search procedure to integrate these modules and facilitate online cooperative planning. We evaluate our methods on three challenging benchmarks with 24 agents. The results show our compositional world model is effective and the framework enables the embodied agents to cooperate efficiently with different agents across various tasks and an arbitrary number of agents, showing the promising future of our proposed methods. More videos can be found at https://umass-embodied-agi.github.io/COMBO/.

<a id="p152"></a>
## P152 · DiscoveryWorld: A Virtual Environment for Developing and Evaluating Automated Scientific Discovery Agents

- **作者**：Peter Jansen; Marc-Alexandre Côté; Tushar Khot; Erin Bransom; Bhavana Dalvi Mishra; Bodhisattwa Prasad Majumder; Oyvind Tafjord; Peter Clark
- **时间**：初稿2024-06；本地arXiv:2406.06769v2，2024-10-07。
- **发表平台／版本状态**：NeurIPS 2024 Datasets and Benchmarks Track；正式proceedings核实。
- **论文链接**：[论文/发表记录 1](https://proceedings.neurips.cc/paper_files/paper/2024/hash/13836f251823945316ae067350a5c366-Abstract-Datasets_and_Benchmarks_Track.html) · [论文/发表记录 2](https://arxiv.org/abs/2406.06769v2)
- **项目／代码／数据**：[资源 1](https://github.com/allenai/discoveryworld)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：29页；SHA-256：`28793ae05bbb22ed6e02fbdceb697a2b9ea8ebff6932c4dd8fb5b70bba5dde91`

### 中文摘要

提出低成本虚拟科学发现环境，要求智能体完整经历提出假设、设计与执行实验、分析结果、得出解释并完成任务。涵盖蛋白质组、化学、考古、反应堆、植物营养、太空疾病、火箭科学和语言发现，用任务完成、过程与解释知识三类指标区分会操作和真正形成发现。

### 核心贡献

为端到端科学发现提供可复现、可控参数的互动基准；加入组件级unit tasks和人类科学家参照，避免只用最终成功掩盖不完整推理过程。

### 实现边界

8主题×3难度×5参数seed=120个发现任务实例（24个主题—难度组合），另有10类基础unit tasks。环境为抽象文本/2D模拟而非真实实验；任务机制已定义但对agent未知，适合机制发现研究，不替代创作者规则补全任务。

### Method／方法

提供物体、仪器、移动/读写/操作等动作及结构化记分卡；GPT-4o实现ReAct、Plan+Execute、维护实验假设与测量记录的Hypothesizer。简单任务最多100步，普通/挑战任务1,000步；知识按预设解释要求评价。另招募11名自然科学硕士/博士背景参与者。

### Results／主要结果

表4：ReAct的简单/挑战任务平均完成率38%/18%；Hypothesizer对应解释知识得分34%/8%。机器在基础unit tasks可达到60%左右完成率，仍难完成发现全流程。人类所测16个普通/挑战组合平均完成率66%、知识得分55%；人类评测的任务与seed配置不同，不能与120实例机器均值无条件直接比较。

### Shortcomings／局限与可能不足

作者强调低保真模拟不保证真实发现迁移；完整120任务的API实验成本约3,000–10,000美元，为论文实验时期成本。空间操作、长上下文和知识评分均可能混入其他能力；研究判断：需分离找出机制、执行实验和最终动作成功，且解释评分不能当作形式化因果证明。

### 证据定位

PDF pp.4–6：环境、规模与指标；p.7表4/5：机器；pp.8–9表6：人类与分析；p.15附录B/C：局限、成本和动作空间。

### Abstract

Automated scientific discovery promises to accelerate progress across scientific domains. However, developing and evaluating an AI agent’s capacity for endto-end scientific reasoning is challenging as running real-world experiments is often prohibitively expensive or infeasible. In this work we introduce DISCOVERYWORLD , the first virtual environment for developing and benchmarking an agent’s ability to perform complete cycles of novel scientific discovery. DISCOVERYWORLD contains a variety of different challenges, covering topics as diverse as radioisotope dating, rocket science, and proteomics, to encourage development of general discovery skills rather than task-specific solutions. DISCOVERYWORLD itself is an inexpensive, simulated, text-based environment (with optional 2D visual overlay). It includes 120 different challenge tasks, spanning eight topics each with three levels of difficulty and several parametric variations. Each task requires an agent to form hypotheses, design and run experiments, analyze results, and act on conclusions. DISCOVERYWORLD further provides three automatic metrics for evaluating performance, based on (a) task completion, (b) task-relevant actions taken, and (c) the discovered explanatory knowledge. We find that strong baseline agents, that perform well in prior published environments, struggle on most DISCOVERYWORLD tasks, suggesting that DISCOVERYWORLD captures some of the novel challenges of discovery, and thus that DISCOVERYWORLD may help accelerate near-term development and assessment of scientific discovery competency in agents. Code available at github.com/allenai/discoveryworld.

<a id="p153"></a>
## P153 · Internal Consistency and Self-Feedback in Large Language Models: A Survey

- **作者**：Xun Liang; Shichao Song; Zifan Zheng; Hanyu Wang; Qingchen Yu; Xunkai Li; Rong-Hua Li; Yi Wang; Zhonghao Wang; Feiyu Xiong; Zhiyu Li
- **时间**：初稿2024-07-19；本地arXiv:2407.14507v3，2024-09-18。
- **发表平台／版本状态**：arXiv综述预印本；尚未核实正式发表平台。页眉的JOURNAL OF LATEX CLASS FILES及AUGUST 2021为模板，不能作为期刊和发表日期。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2407.14507v3)
- **项目／代码／数据**：[资源 1](https://github.com/IAAR-Shanghai/ICSFSurvey)

- **主题**：AI方法与评测
- **PDF版本**：20页；SHA-256：`41fc06755fbf77dde907801588d81aa96e0c54191ce4afe3af6e277e0be6decd`

### 中文摘要

从模型内部一致性出发，统一整理置信度估计、幻觉检测、推理、自我修正与自训练等工作。将一致性分成文本响应、token解码和潜在张量三个层次，并用自我评价—反馈—自我更新框架解释现有方法之间的关系与争议。

### 核心贡献

给出跨响应、解码和潜在表示的一致性分类，以及Self-Evaluate→反馈信号→Self-Update的统一组织框架；把推理时的回答修改与训练时的参数/学生模型更新放在同一研究地图中。

### 实现边界

属于综述和概念框架，没有提出并统一验证一个新的通用自我修正算法。文中的‘Consistency Is (Almost) Correctness’是有前提的假设，不是模型答案正确性的定理；当稳定错误来自训练知识或共享偏差时，多次一致仍可能出错。

### Method／方法

按黑箱/灰箱/白箱访问条件，梳理不确定性、置信度、幻觉、语言批评及对比等反馈；归纳推理拓扑、迭代修改、多智能体、偏好学习、蒸馏和数据增广。以Llama3-8B-Instruct的标点计数展示三个一致性层次的区别，并讨论hourglass假说。

### Results／主要结果

主要结果是文献分类与相互矛盾发现的综合解释。p.5的示例中，同一标点计数问题5次文本回答为{5,3,3,3,3}，多数一致但错误；不同解码策略输出为{4,4,3,4,4}。这是小型说明性实验，不能外推为总体性能提升或正式基准结果。

### Shortcomings／局限与可能不足

【作者】讨论内在反馈能否可靠纠错的争议及一致性假设的适用条件。【解读】没有统一控制模型、任务、采样预算的定量元分析；潜表示例不足以建立一般规律。架空世界的规则若与训练语料中的常识冲突，‘训练知识多数正确’这一推理前提尤其需要重新检验。

### 证据定位

PDF pp.4–7：分类、标点示例与统一框架；pp.8–14：方法组织；pp.15–16：争议与一致性假设。

### Abstract

Large language models (LLMs) often exhibit deficient reasoning or generate hallucinations. To address these, studies prefixed with “Self-” such as Self-Consistency, Self-Improve, and Self-Refine have been initiated. They share a commonality: involving LLMs evaluating and updating themselves. Nonetheless, these efforts lack a unified perspective on summarization, as existing surveys predominantly focus on categorization. In this paper, we use a unified perspective of internal consistency, offering explanations for reasoning deficiencies and hallucinations. Internal consistency refers to the consistency in expressions among LLMs’ latent, decoding, or response layers based on sampling methodologies. Then, we introduce an effective theoretical framework capable of mining internal consistency, named Self-Feedback. This framework consists of two modules: Self-Evaluation and Self-Update. The former captures internal consistency signals, while the latter leverages the signals to enhance either the model’s response or the model itself. This framework has been employed in numerous studies. We systematically classify these studies by tasks and lines of work; summarize relevant evaluation methods and benchmarks; and delve into the concern, “Does Self-Feedback Really Work?” We also propose several critical viewpoints, including the “Hourglass Evolution of Internal Consistency”, “Consistency Is (Almost) Correctness” hypothesis, and “The Paradox of Latent and Explicit Reasoning”. The relevant resources are open-sourced at https://github.com/IAAR-Shanghai/ICSFSurvey.

<a id="p154"></a>
## P154 · Text2World: Benchmarking Large Language Models for Symbolic World Model Generation

- **作者**：Mengkang Hu; Tianxing Chen; Yude Zou; Yuheng Lei; Qiguang Chen; Ming Li; Yao Mu; Hongyuan Zhang; Wenqi Shao; Ping Luo（前三位共同贡献）
- **时间**：2025-07，Findings of ACL 2025；本地为正式论文集版本，pp.26043–26066。
- **发表平台／版本状态**：Findings of the Association for Computational Linguistics: ACL 2025；DOI:10.18653/v1/2025.findings-acl.1337。
- **论文链接**：[论文/发表记录 1](https://aclanthology.org/2025.findings-acl.1337/)
- **项目／代码／数据**：[资源 1](https://text-to-world.github.io/)

- **主题**：创作与规则补全、世界机制与演化、AI方法与评测
- **PDF版本**：24页；SHA-256：`516fd70c100750ff006a62c75aa772ac08bcf91cf4de4e3cbc41ff00c405e319`

### 中文摘要

研究模型能否将自然语言世界描述转成可供符号规划器使用的PDDL世界模型。通过多阶段数据筛选、人工核验及解析执行和结构指标，评价16个LLM，并比较报错修正、上下文示例、合成数据微调及智能体训练对建模能力的作用。

### 核心贡献

建立自然语言→符号状态/动作规则的基准和评测流程；将谓词、参数、前置条件与动作效果分开测量，暴露仅生成可解析代码与正确建模之间的差距。

### 实现边界

输入已提供谓词/动作名称、类型或签名和高层描述；主设置刻意省略明确前置条件和效果，让模型补足。初始1,801个域经筛选剩264个，人工终检得到103个，分为2个训练示例和101个测试域；不能把中间264个当成最终测试数。EXEC主要检查解析/验证器可执行性，SIM和F1基于参考PDDL结构，不是所有轨迹的行为等价证明。

### Method／方法

从已有PDDL域构造自然语言描述，多阶段自动过滤后由6位计算机背景标注者及2位复核者做质量控制。评价9个系列的16个LLM；比较零样本CoT、不做修正EC0与最多3次解析报错反馈EC3、两样本提示、601个合成域上的SFT及智能体轨迹训练。

### Results／主要结果

Table 1中DeepSeek-R1从EC0到EC3：EXEC 72.3→89.1，谓词F1 71.7→86.7、参数F1 64.0→76.3、前置条件F1 57.6→65.0、效果F1 58.8→67.3；结构SIM反而84.3→84.0。两样本提示能明显改善部分模型，但gpt-4o-mini部分指标退步。合成数据SFT使原本EXEC为0的Llama3.1模型获得可解析建模能力；不同干预没有一致改善所有指标。

### Shortcomings／局限与可能不足

【解读】有限域规模及对单一参考实现的结构匹配，无法覆盖所有同样有效的建模选择；高层描述本身可能不完整，不能将创作补全一概判为与唯一参考不一致。没有评测交互式规则修改、影响范围内的最小更新，或同一规则下多种合理演化的覆盖度。

### 证据定位

PDF pp.2–5：任务、指标、数据过滤与103/101计数；pp.6–9：错误类型、Table 1主结果及Table 2示例实验。

### Abstract

Recently, there has been growing interest in leveraging large language models (LLMs) to generate symbolic world models from textual descriptions. Although LLMs have been extensively explored in the context of world modeling, prior studies encountered several challenges, including evaluation randomness, dependence on indirect metrics, and a limited domain scope. To address these limitations, we introduce a novel benchmark, TEXT2WORLD , based on planning domain definition language (PDDL), featuring hundreds of diverse domains and employing multi-criteria, execution-based metrics for a more robust evaluation. We benchmark current LLMs using TEXT2WORLD and find that reasoning models trained with largescale reinforcement learning outperform others. However, even the best-performing model still demonstrates limited capabilities in world modeling. Building on these insights, we examine several promising strategies to enhance the world modeling capabilities of LLMs, including test-time scaling, agent training, and more. We hope that TEXT2WORLD can serve as a crucial resource, laying the groundwork for future research in leveraging LLMs as world models.

<a id="p155"></a>
## P155 · EgoPlan-Bench2: A Benchmark for Multimodal Large Language Model Planning in Real-World Scenarios

- **作者**：Lu Qiu; Yi Chen; Yuying Ge; Yixiao Ge; Ying Shan; Xihui Liu（前两位共同贡献；按本地v2署名顺序）
- **时间**：初稿2024-12-05；本地arXiv:2412.04447v2，2025-04-11；正式期刊在线发表2026-04-08。
- **发表平台／版本状态**：International Journal of Computer Vision 134, article 222 (2026)，DOI:10.1007/s11263-026-02826-y。正式论文扩展为25个模型；以下摘要及数字仍按本地v2的21个模型记录。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2412.04447v2) · [论文/发表记录 2](https://link.springer.com/article/10.1007/s11263-026-02826-y)
- **项目／代码／数据**：[资源 1](https://qiulu66.github.io/egoplanbench2/)

- **主题**：XR与人机协作
- **PDF版本**：18页；SHA-256：`86d13b4d204df0eee1eec14c5a5dde9f3cdc465b7e5b96009d4d8b7f4c48f353`

### 中文摘要

以真实第一人称活动视频考查多模态LLM能否结合当前视觉状态、此前任务进度与目标选择下一步行动。构建涵盖4个领域、24种场景的1,321个问题，并用多模态CoT和自一致性改善模型的历史理解、对象定位与下一步决策。

### 核心贡献

从1,113段Ego4D视频建立依赖视觉信息和活动进度的规划问答，刻意剔除仅靠文字即可回答、或当前帧已经泄露下一动作的问题；分析模型对时间、对象和目标的联合理解错误。

### 实现边界

任务是离线四选一下一动作预测，不是执行计划的闭环智能体成功率。输入包含任务目标、历史视频与当前帧；视频时长为数秒至5分钟。筛选条件要求相关对象可见，未评测用户按请求主动改变视角来补充证据。

### Method／方法

GPT-4辅助清理动作叙述、推断目标及生成问答；InternVL1.5与GPT-4帮助自适应选择时间点，再做循环评测与人工核查。训练自由的增强流程结合动作历史摘要、GroundingDINO对象边界框、CoT及自一致性投票。

### Results／主要结果

本地Table I中GPT-4V最高准确率32.63%，随机为25%，多数模型约23–27%。Table II是另一提示实验：基线32.80%，加入多模态CoT和自一致性达到43.04%，提升10.24个百分点；不能把这个增量加到Table I的32.63%。使用真实标注动作历史可到51.67%，属于特权输入条件。

### Shortcomings／局限与可能不足

【作者/实验分析】动作进度、当前环境、领域知识与空间定位仍会混淆。【解读】四选一正确不等于可执行规划；模型参与筛选可能带来分布偏差，抽帧可错过短暂事件。没有测量用户注意力、取证动作代价、计划执行失败后的恢复或XR提示改变后续观察的问题。

### 证据定位

PDF pp.5–7：数据构建与Table I；pp.7–12：错误分析；p.14 Table II：提示与特权输入条件；正式期刊信息见Springer页面。

### Abstract

The advent of Multimodal Large Language Models (MLLMs), leveraging the power of Large Language Models, has recently demonstrated superior multimodal understanding and reasoning abilities, heralding a new era for artificial general intelligence (AGI). However, achieving AGI necessitates more than just comprehension and reasoning. A crucial capability required is effective planning in diverse scenarios, which involves making reasonable decisions based on complex environments to solve real-world problems. Despite its importance, the planning abilities of current MLLMs in varied scenarios remain underexplored, leaving a significant gap in our understanding of their full potential. In this paper, we introduce EgoPlan-Bench2, a rigorous and comprehensive benchmark designed to assess the planning capabilities of MLLMs across a wide range of real-world scenarios. EgoPlan-Bench2 encompasses everyday tasks spanning 4 major domains and 24 detailed scenarios, closely aligned with human daily life. EgoPlan-Bench2 is constructed through a semiautomatic process utilizing egocentric videos, complemented by manual verification. Grounded in a first-person perspective, it mirrors the way humans approach problem-solving in everyday life. We evaluate 21 competitive MLLMs and provide an in-depth analysis of their limitations, revealing that they face significant challenges in real-world planning. To further improve the planning proficiency of current MLLMs, we propose a training-free approach using multimodal Chain-of-Thought (CoT) prompting through investigating the effectiveness of various multimodal prompts in complex planning. Our approach enhances the performance of GPT-4V by 10.24% on EgoPlan-Bench2 without additional training. Our work not only sheds light on the current limitations of MLLMs in planning, but also provides insights for future enhancements in this critical area. We have made data and code available at https://qiulu66.github.io/egoplanbench2/.

<a id="p156"></a>
## P156 · PoE-World: Compositional World Modeling with Products of Programmatic Experts

- **作者**：Wasu Top Piriyakulkij; Yichao Liang; Hao Tang; Adrian Weller; Marta Kryven; Kevin Ellis
- **时间**：初稿2025-05；本地arXiv:2505.10819v4，2025-11-19；正式会议NeurIPS 2025。
- **发表平台／版本状态**：Advances in Neural Information Processing Systems 38（NeurIPS 2025，主会）。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2505.10819v4) · [论文/发表记录 2](https://proceedings.neurips.cc/paper_files/paper/2025/hash/262dd62fd1bbb30d6a6b4d578f5e65ff-Abstract-Conference.html)
- **项目／代码／数据**：[资源 1](https://topwasu.github.io/poe-world) · [资源 2](https://github.com/topwasu/poe-world)

- **主题**：世界机制与演化、AI方法与评测
- **PDF版本**：30页；SHA-256：`71cf49e51a7705bb24fc0812ec7f33871ae4dfd5871021b5c954d720ad440814`

### 中文摘要

将环境动力学表示为多个小型程序专家组成的加权乘积模型，支持随机性、部分可观测性和较复杂的对象交互。LLM从少量轨迹编写与修订专家程序，优化其权重后形成可规划或用于训练策略的世界模型。

### 核心贡献

用可组合的概率程序专家替代单一庞大确定性模拟器；把局部机制知识、轨迹拟合与在线修订结合起来，并在原版和修改后的Atari环境中考查少样本适应。

### 实现边界

使用OCAtari提取的结构化对象/属性，作者还按游戏修补对象检测，非从原始像素端到端学得全部机制。模型以完整历史为条件，并假设下一状态对象属性条件独立以便归一化。实验集中在Pong、Montezuma’s Revenge及其改版；没有解决通用探索、奖励学习或任意创作者世界。

### Method／方法

LLM合成短Python程序，其确定性属性预测转换为带噪专家分布，未规定属性采用均匀分布；按加权乘积组合。L-BFGS最大似然拟合权重并删去弱专家，新轨迹触发补充/修正。使用对象接触关系的高层图和低层动作搜索做分层规划，也用世界模型训练RL策略。

### Results／主要结果

少于1,000帧初始示范加最多3,000步额外交互条件下，Table 1的PoE-World+planner在原版/改版Montezuma均得100±0，WorldCoder和100k步PPO均为0；此处100分对应拿到钥匙，非通关。原版/改版Pong分别为−12.33±0.88、−13.67±0.67，虽优于相应少样本基线但仍是负分；20M步PPO在原版Pong为17±0.58，不能笼统声称超越长期训练的RL。

### Shortcomings／局限与可能不足

【作者】未学习像素感知，也没有通用解决探索及奖励学习。【解读】条件独立、人工对象接口与两类游戏限制外推；交互样本节省不等于LLM合成及规划计算成本低。没有独立评测规则编辑后的因果影响定位、无关内容保持或多种合法世界的覆盖。

### 证据定位

PDF pp.3–6：专家分布、权重学习、规划和对象输入；p.7 Table 1：交互预算与游戏结果；pp.8–10：预测实验和局限。

### Abstract

Learning how the world works is central to building AI agents that can adapt to complex environments. Traditional world models based on deep learning demand vast amounts of training data, and do not flexibly update their knowledge from sparse observations. Recent advances in program synthesis using Large Language Models (LLMs) give an alternate approach which learns world models represented as source code, supporting strong generalization from little data. To date, application of program-structured world models remains limited to natural language and grid-world domains. We introduce a novel program synthesis method for effectively modeling complex, non-gridworld domains by representing a world model as an exponentially-weighted product of programmatic experts (PoE-World) synthesized by LLMs. We show that this approach can learn complex, stochastic world models from just a few observations. We evaluate the learned world models by embedding them in a model-based planning agent, demonstrating efficient performance and generalization to unseen levels on Atari’s Pong and Montezuma’s Revenge. We release our code and display the learned world models and videos of the agent’s gameplay at https://topwasu.github.io/poe-world.

<a id="p157"></a>
## P157 · Exploring Exploration with Foundation Agents in Interactive Environments

- **作者**：Daniel P. Sawyer; Nan Rosemary Ke; Hubert Soyer; Martin Engelcke; David P. Reichert; Drew A. Hudson; John Reid; Alexander Lerchner; Danilo Jimenez Rezende; Timothy P. Lillicrap; Michael Mozer; Jane X. Wang
- **时间**：初稿2024-12-09；本地arXiv:2412.06438v2，2025-10-07。
- **发表平台／版本状态**：Google DeepMind研究预印本；尚未核实正式会议/期刊。arXiv页面亦可用旧题名Can foundation models actively gather information in interactive environments to test hypotheses?检索；本条保留本地PDF题名。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2412.06438v2)
- **项目／代码／数据**：本地PDF及本次核查未检出明确属于本文的项目/代码入口；不代表作者没有发布资源。
- **版本关系**：基于P142 Alchemy构造部分实验；是环境/能力评测的后续工作，非相同PDF。

- **主题**：XR与人机协作、世界机制与演化、AI方法与评测
- **PDF版本**：30页；SHA-256：`18991b9ca070b5bc1ca4355db21012d97ce34c4715cf6d16d738eab85b96125c`

### 中文摘要

考查基础模型能否在交互环境中主动收集信息、检验假设并适应隐藏机制。以文本/三维Feature World和更复杂的Alchemy实验，分析模型、先验说明及周期总结对探索质量、跨试次学习和机制突变后适应的作用。

### 核心贡献

区分探索动作是否提供足够信息与模型是否正确利用信息；从简单特征发现扩展到跨试次隐藏动力学学习，并测试不预告的规则改变。包含模型从视频读取状态、提出行动指令、由人类执行的三维概念验证。

### 实现边界

无需微调的模型能力研究，非新训练算法。三维试验用Gemini 1.5 Pro，由人类执行移动/放置指令；这一设置已经覆盖‘新证据需要请求人类行动’的基本形态。每个三维条件15个episode，任务结构简单，未优化人类注意力、行动可接受性或XR空间提示。

### Method／方法

Feature World中寻找产生奖励的颜色/形状属性或属性组合，比较模型探索与随机及理想策略；将Gemini扩展到三维视频输入和人类执行。TextAlchemy比较GPT-4o、o4-mini、Claude 3.7与Gemini 2.5 Pro，控制是否给结构先验、是否每轮自总结，并在后续试次静默更换环境机制。

### Results／主要结果

三维Gemini行动条件的15个episode有8个出现视觉错误；保留这些错误时，奖励属性识别相对随机行动者的提升不显著（p=0.13），去除视觉错误后才显示优势。Alchemy在无先验且不总结时，没有模型显示显著的跨试次提升；增加总结后，除o4-mini外模型在无先验设置也能改善。机制改变后，Gemini 2.5 Pro和Claude 3.7在相应增强条件下能恢复表现，GPT-4o/o4-mini适应较弱。

### Shortcomings／局限与可能不足

【解读】固定合成环境族及Alchemy每条件10次随机重复限制统计与开放世界结论；人类承担底层动作控制，掩盖真实部署的行动落地问题。论文没有处理取证与用户当前任务的注意力冲突、请求被拒绝、提示污染观察及人机私有信息差异。作者关于能力上限的推测不应当作无内在障碍的证明。

### 证据定位

PDF pp.5–7：Feature World与三维人类执行，p.7 Figure 3及视觉错误；pp.8–11：Alchemy、总结/先验和机制突变；p.12：局限。

### Abstract

Foundation models excel at single-turn reasoning, but many real-world challenges, from scientific research to technology development, require multi-turn exploration in dynamic interactive environments. Crucial components of learning from experience in these settings, such as efficiently gathering information to test hypotheses, meta-learning a model of the world’s dynamics, and adapting to unexpected changes, remain largely unexplored for these models. We first evaluate foundation models in Feature World, a setting that primarily tests information gathering about a static hidden reward function. In this initial setting, we show that state-of-the-art foundation models come close to optimal efficiency in selecting maximally informative actions in tasks with simple reward functions. As a proof of concept, we also show a model can gather information efficiently in a 3D embodied version of this task, though errors in vision limit some aspects of performance. In order to test exploration across multiple dependent turns and trials, we implement a custom, text-based version of the Alchemy environment, a benchmark designed for meta-learning. Here, agents must deduce a latent causal structure by integrating information across multiple state-dependent trials. In this more complex setting, we find that recent foundation models struggle to meta-learn strategies that enable improved performance over time. However, prompting the models to summarize their observations at regular intervals enables an emergent meta-learning process, allowing them to improve across trials. Notably, in some models, summarization also enabled adaptive re-learning of this information when the environment’s rules change unexpectedly. While most models performed reasonably well on simple Feature World tasks, evaluations in Alchemy reveal stark differences in robustness among the models, with Gemini 2.5 performing best, followed by Claude 3.7, and ChatGPT-4o and o4-mini struggling the most. These results underscore Alchemy’s value as a benchmark for meta-learning and strategy adaptation in foundation models. By moving beyond simple discovery to complex, stateful environments, we demonstrate that the most significant challenge for foundation agents is not selecting informative actions in the moment, but rather seeking and integrating knowledge through adaptive strategies over time. Intriguingly, we find there is likely no intrinsic barrier to future generations of foundation agents more fully mastering these abilities.

<a id="p158"></a>
## P158 · RULER-Bench: Probing Rule-based Reasoning Abilities of Next-level Video Generation Models for Vision Foundation Intelligence

- **作者**：Xuming He; Zehao Fan; Hengjia Li; Fan Zhuo; Hankun Xu; Senlin Cheng; Di Weng; Haifeng Liu; Can Ye; Boxi Wu（前三位共同贡献）
- **时间**：本地arXiv:2512.02622v1，2025-12-02。
- **发表平台／版本状态**：arXiv预印本；项目页亦采用预印本引用，尚未核实正式会议录用。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2512.02622v1)
- **项目／代码／数据**：[资源 1](https://hexmseeu.github.io/RULER-Bench-proj/)

- **主题**：世界机制与演化
- **PDF版本**：30页；SHA-256：`fab16d768eec43e7f891e6e6993e0bd77ca4f4fdffd675d5e978c408dcd9e90b`

### 中文摘要

为视频生成模型建立规则推理基准，要求生成的过程在科学、视觉、假设、游戏、语义与人文任务中体现隐含规则。通过人工核验的规则解释和逐项问题，将指令遵循、视觉一致性、视觉保真度与规则连贯性分开评价。

### 核心贡献

提供622个样本、40种任务、6个大类和约6,500条核查问题，分别测试文本到视频及图像到视频模型；揭示视觉质量较高仍可能缺少正确规则后果的现象。

### 实现边界

评价短视频生成是否符合给定场景/隐含规则，包含假设性世界条件，但没有交互式创作者规则编辑或同一规则下多条演化的覆盖实验。o3按good/medium/bad映射100/50/0做问题级评分，RC是归一化评分，不是整段视频严格满足规则的比例。

### Method／方法

人工与GPT-5构造任务、隐含解释和核查表并复核；评测10个视频模型（6闭源、4开源），由o3逐项评分。另比较加入规则/预期结果解释的增强提示，并以80个视频、813个问题的人类标注核对自动评审。

### Results／主要结果

Table 2中Veo 3.1的RC为48.87、IF 68.70、VC 76.68、VF 86.72；Sora 2的RC为41.23，体现画面质量与规则得分的差距。游戏类Sora 2为19.97、Veo 3.1为17.70；正文‘全部低于15’与表格不一致，本条依表格记录。o3与人工判断一致率85.12%，Spearman 0.8011。增强提示下Veo假设类RC由46.79到58.12；该提示包含额外规则/结果信息。

### Shortcomings／局限与可能不足

【解读】自动评审仍会误判，逐条平均分不能证明长时间轨迹的逻辑有效性；感知与渲染质量可能混入推理指标。提供预期后果的提示不能单独证明模型本身学会了推导。另Table 4科学类50.97→62.62的实际增量为11.65，表内印成+9.65；记录数据时需复算。

### 证据定位

PDF p.3：分类；p.5：指标与问题构建；p.6 Tables 2–3：主结果；p.7 Table 4：提示实验；p.8：人工一致性研究。

### Abstract

Recent advances in video generation have enabled the synthesis of videos with strong temporal consistency and impressive visual quality, marking a crucial step toward vision foundation models. To evaluate these video generation models, existing benchmarks primarily focus on factors related to visual perception and understanding, like visual aesthetics, instruction adherence, and temporal coherence. However, the rule-based reasoning capabilities of video generation models remain largely unexplored. Although recent studies have carried out preliminary explorations into whether video models can serve as zero-shot learners, they still lack a fine-grained decomposition of reasoning capabilities and a comprehensive evaluation protocol. To address this gap, we introduce RULER-Bench, a benchmark designed to evaluate the reasoning ability of video generation models from the perspective of cognitive rules. Built upon two fundamental paradigms: text-to-video and image-to-video, RULER-Bench covers 40 representative tasks spanning six rule categories with 622 high-quality annotated instances. For the evaluation of each generated video, we construct a checklist covering four metrics and leverage GPT-o3 to assign scores to each question, achieving 85% alignment with human judgements. Extensive experiments show that the state-of-the-art model achieves only 48.87% on the rule coherence metric, highlighting significant room for improvement in the reasoning capability of next-level video models. We expect that the insight obtained from RULER-Bench will facilitate further development of reasoning-aware video generation, advancing video generation models toward vision foundation intelligence.

<a id="p159"></a>
## P159 · GPS: Graph-guided Proactive Information Seeking in Large Language Models

- **作者**：Ruiqing Li; Yifeng Xu; Xinke Jiang; Zhibang Yang; Xinyu Ma; Yue Fang; Junfeng Zhao; Yasha Wang; Xu Chu
- **时间**：2026；本地标注Published as a conference paper at ICLR 2026，未检出独立的精确版本日期。
- **发表平台／版本状态**：International Conference on Learning Representations（ICLR 2026），正式论文集已核实。
- **论文链接**：[论文/发表记录 1](https://proceedings.iclr.cc/paper_files/paper/2026/hash/1f49b7fbd7c7afc52c1db0d4ed1a338d-Abstract-Conference.html)
- **项目／代码／数据**：[资源 1](https://github.com/lrq111/GPS)

- **主题**：XR与人机协作、创作与规则补全、AI方法与评测
- **PDF版本**：25页；SHA-256：`59c114d720cc8d31d8c53fede1b4298921279d14a9bc5a59d93dfdd3b0f4c314`

### 中文摘要

面向检索增强问答中缺少用户条件的问题，将文档中的条件规则组织为有向无环图，沿图主动澄清缺失变量，并根据回答裁剪无关分支。通过条件路径合成训练数据和面向澄清结果的强化学习，同时改善回答正确性和提问效率。

### 核心贡献

把条件逻辑表示、主动澄清与训练目标结合：DAG为提问提供结构，动态遍历降低冗余，混合奖励共同考虑最终正确性、交互轮数和图质量。

### 实现边界

理论的逻辑完备性针对有限取值函数可被DAG表示，不保证LLM会从真实文档正确抽取全部规则。实验的用户模拟器回答已有条件事实；没有通过物理行动创造新证据。世界规则已给定，未知的是用户条件，并非从观察发现未知环境机制。

### Method／方法

Reasoner输出条件变量、值分支与答案叶节点；Clarifier按可达路径代价选择问题，收到回答后剪枝。用ConditionalQA中的欠明确样本及DeepSeek-R1合成条件路径，筛选完整输入可答而缺失输入不可答的数据。GRPO训练Reasoner，结合正确性、轮数惩罚与结构质量奖励；在Qwen2.5-7B和Llama3-8B骨干上验证。

### Results／主要结果

Table 1中Qwen-GPS在Synthetic/ConditionalQA/ShARC的成功率为60.2/73.4/79.3%，WCT为4.59/2.91/2.41；对应Clarify-DPO成功率59.2/72.0/78.5%，WCT 4.67/3.52/2.93。WCT把失败样本按最大10轮计罚，不等于原始平均提问次数；另列F1衡量是否需要澄清，不是答案F1。Llama-GPS在ShARC为75.8%，低于Clarify-DPO的82.7%，并非所有设置均最佳。Qwen在ConditionalQA移除RL后成功率73.4→67.7%。

### Shortcomings／局限与可能不足

【解读】有限离散条件、相对固定规则库及模拟用户限制复杂开放场景；图抽取错误可系统性排除正确路径。LLM判分和模拟用户偏差仍在；轮数成本没有表达用户动作风险、注意力中断及不同取证行动对后续观察的影响。

### 证据定位

PDF pp.3–7：DAG、算法、数据合成与奖励；p.8：SR/WCT/澄清需要F1定义；pp.9–10 Tables 1–2：主结果和消融；附录A/B：理论。

### Abstract

Equipping Large Language Models (LLMs) with the ability to proactively ask clarifying questions is essential to mitigate ambiguity when faced with underspecified user queries in retrieval-augmented generation (RAG) systems. However, existing methods often neglect the rule-based reasoning structures embedded in the retrieved knowledge that are central to ambiguity, making it challenging to learn an effective and efficient question-asking strategy. To address these issues, we introduce GPS, a two-stage framework for enhancing proactive information seeking abilities of LLMs in RAG systems. In the reasoning stage, we propose a Directed Acyclic Graph (DAG) reasoning structure with theoretical guarantees of logical completeness, which facilitates capturing all conditional logic in the retrieved knowledge and supports effective clarification. In the clarification stage, we design a traversal-based algorithm that dynamically prunes the DAG based on user responses, enabling efficient clarification. To further enhance DAG construction, we first propose a conditional paths guided data synthesis method to address data scarcity challenge, then we apply a clarification-oriented reinforcement learning method with a hybrid reward that jointly considers effectiveness and efficiency to optimize the LLM. Experiments on three benchmarks demonstrate that GPS outperforms baseline methods in both success rate and clarification efficiency.

<a id="p160"></a>
## P160 · Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review

- **作者**：Jingbo Chen; He Wang; Wei Yuan; Yuqiao Lai; Zhenyan Lu
- **时间**：本地arXiv:2607.09403v1，2026-07-10。首页所写August 2026为未核实模板信息，不采用为正式发表日期。
- **发表平台／版本状态**：arXiv预印本。PDF含JAIR期刊模板及占位DOI 10.1613/jair.1.xxxxx；未查到足以确认JAIR正式发表的记录，不能按已发表JAIR论文引用。
- **论文链接**：[论文/发表记录 1](https://arxiv.org/abs/2607.09403v1)
- **项目／代码／数据**：本地PDF及本次核查未检出明确属于本文的项目/代码入口；不代表作者没有发布资源。

- **主题**：创作与规则补全、世界机制与演化
- **PDF版本**：36页；SHA-256：`e116379992778595245b5564198d216a171c7b88850d71d691789788ed2f450b`

### 中文摘要

AutoWorldBuilder从一两句世界设定生成地理、社会、资源与文化等概念。系统以多智能体分工、任务依赖调度、分层上下文预算和迭代审核控制规模与内部一致性；在20个设定任务、两种LLM后端上报告运行及内部评审结果。

### 核心贡献

整合概念存储、DAG与语义分组调度、FAISS检索和四层上下文、专门Auditor与可配置角色。是架空世界概念扩展系统的直接前作，但其提出的数据结构与实际启用功能必须区分。

### 实现边界

作者在§6.4明确：16种概念关系只完成定义，关系解析模块未实现，实验关系类型覆盖率为0%；不能称已验证完整知识图谱推理。输出是概念设定集合，未实现可执行世界演化、因果干预或规则修改后的依赖更新；接受/拒绝设定等实时人机协作列为未来工作。质量来自系统内部LLM评审，无独立外部正确性基准。

### Method／方法

将输入拆成有依赖的任务，拓扑排序后按语义与批大小分组；从已完成批次检索相关概念，按Essential/Relevant/Summary/Collaboration四层分配上下文。21种专门角色按技能配置加载，8种Auditor参与评分、修订和筛选；主要测试中文输入。20个案例覆盖5类世界，每种后端各运行20次，共40次。

### Results／主要结果

Table 8中GPT-OSS 120B和DeepSeek v3.2均19/20次完成（95%）；成功世界平均56.2/103.4个概念，平均18/31分钟，内部最终通过率85.5/99.2%。作者称初轮42%经审核到85%以上，但Table 14中DeepSeek平均评分从8.40降至8.21。所谓89.9/90.7%压缩对应平均304.3/278.4 token相对3,000-token预算的未用比例，不能当作相对未压缩完整上下文的受控节省率。Auditor全部通过只说明未检出问题，不代表零冲突。

### Shortcomings／局限与可能不足

【作者】关系解析未启用、Auditor零检出值得怀疑、缺外部标准化评估、任务分解会产生环或解析错误、主要支持中文。§5.4明确模块分析是理论预期而非受控消融，因此+10–15百分点审核收益及50–70%时间缩减等预测不能记为实验测得。表2预算比例与各层token数亦不一致。【解读】两后端批大小下限略有不同，且内部判分、少量任务、无创作者研究限制关于一致性和效率的强结论。

### 证据定位

PDF pp.12–20：概念/调度/压缩/审核；pp.21–25 Tables 6–14：20×2实验及压缩分母；pp.27–28 §5.4：非受控消融声明；p.30 §6.4：关系模块未实现及质量评估局限；p.31：人机协作列为未来工作。

### Abstract

Worldbuilding, the construction of coherent fictional worlds, is a foundational task in game design and literary creation. Large Language Models (LLMs) offer new possibilities for automated content generation, but their application to worldbuilding faces three challenges: context explosion that grows linearly with the building process, the tension between creative diversity and content consistency, and the absence of automated quality assurance. This paper presents AutoWorldBuilder, a multi-agent collaborative system that addresses these challenges through five integrated components: a structured concept network with conflict detection; a DAG-based hybrid batch scheduler that groups tasks by semantic locality; a four-layer context compression mechanism achieving approximately 90% token reduction; an iterative review system with specialized Auditor agents that improves proposal pass rates from 42% to over 85%; and a skill-driven agent architecture supporting zero-code extension with differentiated temperature configuration. Two experiments across 20 diverse worldbuilding tasks, using GPT-OSS 120B and DeepSeek v3.2 as LLM backends, demonstrate a 95.0% success rate. The system generated 56–103 self-consistent concepts per world in 18–31 minutes, with no conflicts detected by the review pipeline. The architectural patterns validated here, including layer-as-budget compression, semantic-locality scheduling, and separation of generation and review, may transfer to the broader class of knowledge-intensive, multi-agent LLM applications.

<a id="p003"></a>
历史别名：[P002](#p002)

<a id="p082"></a>
历史别名：[P081](#p081)

<a id="p109"></a>
历史别名：[P103](#p103)
