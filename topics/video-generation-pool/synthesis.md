> 统计范围：原始75篇已标注论文。2026扩样新增120篇尚未做全文标注，未纳入本文矩阵、空格判断或15题邻居；“在本论文池内未见”仅限原75篇，不能延伸到195篇总池。

# 综合：任务结构与研究定位

[推断] 你的核心不是再加一种控制输入，而是建立一个可检验的“修改契约”：当前提/事件/观察改变时，推断必要改变集、应保持集和无法确定集，再由生成器执行，并验证两类约束都满足。它最自然落在编辑×训练信号，以及世界模型×记忆；数据与评测是实现该契约的必要支撑。

本池75篇全文均已取得并核对任务/方法/实验的相关片段（73篇HTML、2篇PDF），并非75篇逐行通读。事实字段给出正文/补充定位；归类、矩阵解释、差距及实验建议均为[推断]。三组GitHub配额和会议年份分层保持第一步不变。

计数：72篇主任务确定，3篇不确定；其他0/75＝0%，不确定3/75＝4%。64方法、6基准、4数据集、1分析、0综述。证据类型可重叠：74篇有定量评测（包含自建测试集，不全是独立公共benchmark）、67篇有消融、41篇有人类评价。人类评价包含生成偏好、指标校准与caption评价，不能直接相加参与者数或视为同一强度证据。

## 各任务定义、解法、证据与未解问题

### 文本或图像生成视频

[推断] 本文采用的标准定义：输入文本/初图，输出语义相符的视频；一般没有指定源视频的局部不变式。 本池落点：训练信号14/23，尤其蒸馏、偏好/RL和reward；架构3篇，评测/数据/推理各2篇。 证据主要是VBench等自动分数、reward/训练消融及人工偏好。 本池该任务23篇，定量23、消融18、人类评价19（可重叠，含自建评测集）。核心未解问题：高质量或高总分能否保证短暂必要事件和正确后果仍未解决；DOLLAR明确展示自动分数与人评错位，DenseDPO则诊断低运动偏好。 依据：[P024 · DOLLAR: Few-Step Video Generation via Distillation and Latent Reward Optimization](https://arxiv.org/html/2412.15689)；[P032 · Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/html/2604.19234)；[P072 · DenseDPO: Fine-Grained Temporal Preference Optimization for Video Diffusion Models](https://arxiv.org/html/2506.03517)。

### 条件控制生成

[推断] 本文采用的标准定义：给定可独立操控的姿态、相机、轨迹、音频、身份或事件时间等信号，输出符合约束的视频。 本池落点：条件注入8/14，表示2篇、训练信号2篇，架构和推理各1篇。 证据主要是控制误差、参考fidelity、通用画质、组件消融和人工偏好。 本池该任务14篇，定量14、消融14、人类评价9（可重叠，含自建评测集）。核心未解问题：信号足够、互相相容且能表达后果，常由用户先保证；控制到位不能证明必要后果正确或无关内容保持。 依据：[P005 · MotionCtrl: A Unified and Flexible Motion Controller for Video Generation](https://arxiv.org/html/2312.03641)；[P012 · MotionAgent: Fine-grained Controllable Video Generation via Motion Field Agent](https://arxiv.org/html/2502.03207)；[P056 · Mind the Time: Temporally-Controlled Multi-Event Video Generation](https://arxiv.org/html/2412.05263)。

### 编辑与修改

[推断] 本文采用的标准定义：给定源视频/已有世界与编辑请求，改变目标内容，同时保留任务规定的源信息；保持对象必须具体到身份、运动、背景或有效记忆。 本池落点：条件注入3/10、数据3/10；表示、架构、训练信号、记忆各1篇。 证据主要是编辑集上的遵循/相似性、运动/背景指标，消融及部分人工比较。 本池该任务10篇，定量9、消融10、人类评价5（可重叠，含自建评测集）。核心未解问题：“改哪些”多由mask、任务类型或已知编辑范围给出；P018已允许新接触改变原运动，P074已选择性更新记忆，因此剩余问题应收窄到影响范围未知、必要后果可组合且保持可验证。 依据：[P018 · TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/html/2603.29092)；[P059 · VideoCoF: Unified Video Editing with Temporal Reasoner](https://arxiv.org/html/2512.07469)；[P074 · PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449)。

### 长视频与多镜头叙事

[推断] 本文采用的标准定义：跨长时间或多镜头生成，要求后续prompt/镜头与历史实体、叙事连续；与短片AR和环境动作预测分开。 本池落点：3篇各落架构、记忆、评测；这个小样本不足以估计全领域主流。 证据主要是VBench-Long/InterVBench的长片统计、prompt对齐、实体judge与人工校准。 本池该任务3篇，定量3、消融2、人类评价2（可重叠，含自建评测集）。核心未解问题：身份保持和因果状态保持仍是不同目标；相似外观可能掩盖物品无因复原、信息提前泄露或旧事件被遗忘。 依据：[P053 · WorldAttention: An Efficient Attention Architecture for Interactive Video World Models](https://arxiv.org/pdf/2609.34606)；[P069 · LongLive: Real-time Interactive Long Video Generation](https://arxiv.org/html/2509.22622)；[P075 · EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](https://arxiv.org/html/2605.15199)。

### 动作条件的预测与交互世界模型

[推断] 本文采用的标准定义：输入视觉历史与动作，输出未来观察或交互rollout；若还训练agent，需区分视频预测误差与真实控制成功。 本池落点：架构5/16、训练信号5/16，表示/条件/记忆各2篇。 证据主要是动作控制误差、rollout保真、游戏/机器人回报、重访测试和受控消融。 本池该任务16篇，定量16、消融16、人类评价3（可重叠，含自建评测集）。核心未解问题：动作或外部观察改变后，哪些历史假设失效、哪些事实仍有效，尚缺统一协议；实时FPS也不能替代中断响应延迟。 依据：[P043 · AdaWorld: Learning Adaptable World Models with Latent Actions](https://arxiv.org/html/2503.18938)；[P048 · Training Agents Inside of Scalable World Models](https://arxiv.org/html/2509.24527)；[P049 · ActionSplice: In-Flight Action Editing for Interactive World Models](https://arxiv.org/html/2609.08230)；[P050 · Echo-Memory: A Controlled Study of Memory in Action World Models](https://arxiv.org/html/2606.09803)。

### 3D/4D 一致生成

[推断] 本文采用的标准定义：从有限观察生成相机控制的多视图/视频，共享几何世界并在重访时一致；输出不必为显式3D资产。 本池落点：记忆2/3、评测1/3；Gen3C的3D cache还列次表示。 证据主要是新视角重建与相机误差、循环轨迹和WorldScore；部分人类质量校准。 本池该任务3篇，定量3、消融2、人类评价1（可重叠，含自建评测集）。核心未解问题：VMem明确承认循环轨迹较简单，纹理相似指标不能充分证明真实多视图一致；动态结构变更后几何与外观记忆如何分开失效也未被这3篇覆盖。 依据：[P015 · GEN3C: 3D-Informed World-Consistent Video Generation with Precise Camera Control](https://arxiv.org/html/2503.03751)；[P062 · VMem: Consistent Interactive Video Scene Generation with Surfel-Indexed View Memory](https://arxiv.org/html/2506.18903)；[P063 · WorldScore: A Unified Evaluation Benchmark for World Generation](https://arxiv.org/html/2504.00983)。

### 视频作为推理或回答

[推断] 本文采用的标准定义：生成视频承担回答或解题过程，而不只是按描述呈现画面；正确性由问题语义、目标和合法中间状态决定。 本池落点：训练信号2/3、评测1/3，集中在可验证reward与问题型benchmark。 证据主要是受限规则任务成功率、OOD、reward/训练消融；开放用户意图依赖judge。 本池该任务3篇，定量3、消融2、人类评价0（可重叠，含自建评测集）。核心未解问题：可解析迷宫/棋盘验证难直接迁移到开放世界；外观逼真不等于回答正确，通用judge还需校准和对抗错误测试。 依据：[P030 · Respond Beyond Language: A Benchmark for Video Generation in Response to Realistic User Intents](https://arxiv.org/html/2506.01689)；[P034 · Wan-R1: Verifiable-Reinforcement Learning for Video Reasoning](https://arxiv.org/html/2603.27866)；[P036 · Video Models Can Reason with Verifiable Rewards](https://arxiv.org/html/2605.15458)。

### 其他（说明）

[推断] 本文采用的标准定义：保留给现有七类确实无法表示的输入输出契约，不用来收纳证据不足。 本池落点：本池0篇，无法判定主流贡献。 证据主要是无本池样本；没有可汇总证据。 本池该任务0篇，定量0、消融0、人类评价0（可重叠，含自建评测集）。核心未解问题：0篇并不说明任务空间已经完整：安全目标、评分模型产物和机构变化等仍暴露现有轴的限制。 依据：[P021 · SafeSora: Towards Safety Alignment of Text2Video Generation via a Human Preference Dataset](https://arxiv.org/html/2406.14477)；[P035 · CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/html/2605.11723)。

## 分类本身的检查

[推断] 这套分类可以组织阅读，但不是互斥的自然定律。VACE同时做控制和编辑；WorldDirector同时做动态世界编排与跨视角一致；WorldReasonBench同时是未来状态预测与过程推理评测。这3篇主任务保持不确定并在矩阵单列，不能用作者标题替代判定。

[推断] 建议将“生成范式”拆成两列：时间分解（整段/逐块/逐帧/混合）与采样预算（多步/少步及实际延迟）。当前15篇优先标少步/实时，其中多数还同时是AR；10篇因reward/benchmark或跨生成器而范式不确定。P066的24fps是生成视频播放帧率，不能据此称实时推理。

[推断] 建议拆开长视频延展与多镜头叙事；拆开identity consistency与state/causal consistency；将环境memory与KV计算cache分别记录；把编辑分成外观/空间运动/事件后果/历史或belief revision。无需立即合并世界模型与3D生成：两者分别强调动作状态转移与跨视角世界共享，但应允许副任务。

[推断] 贡献轴仍保留八类，但需要区分“新表示”与“新表示的条件注入”、“记忆语义更新”与“仅缓存加速”。主次贡献分开能减少假空格，不能消除边界主观性。控制信号中的“图像”目前兼容源视频和历史帧，建议后续拆开输入视频角色，并新增空间mask/边界框与是否由agent派生。

[推断] 新增“产物类型”（生成器/编辑器/世界模型/reward-verifier/数据/benchmark），比把reward工作塞进“其他”更有用。目标轴应补任务成功/答案正确、多样性、可修订性、安全/价值对齐；例如SafeSora的harmlessness不应被硬塞进画质或指令遵循。0个其他不说明目标轴完备。

[推断] 本池按来源目的抽样，Post-Training配额天然提高训练信号占比。24篇训练信号主贡献是池内分布，不是领域份额；3D、长叙事各只有3个确定样本，任何空格论证都应先扩池再下结论。

## 选择性修改需要怎样的评测

[推断] 对干预前后状态定义三集合：必须改变、必须保持、未确定。像素变化范围不等于因果影响范围：相机/遮挡/光照变化可能让未变对象的像素改变；同一外观也可能隐藏错误状态。对可控模拟场景，用同初始状态和共享外生随机源构造成组干预；在真实视频上用独立人工/规则审计补充，不能把模拟ground truth当真实世界识别保证。

[推断] 最小结果面板应同时报告：编辑请求成功率、必要后果召回、无关内容破坏率、已满足约束回退率、长程旧状态复发率，以及预算/响应延迟。先按未见事件组合、未见对象机制、未见相机/背景拆测试，再做总平均。verifier与训练reward应有独立验证，防止只学会高分。

已有强邻居必须作为基线：[P018 · TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/html/2603.29092)；[P049 · ActionSplice: In-Flight Action Editing for Interactive World Models](https://arxiv.org/html/2609.08230)；[P074 · PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449)。P018允许接触引起运动改变；P049明确不保证后续解码前缀完全相同；P074根据已知编辑类型更新记忆。因此不能将它们概括成“只做外观、完全不管后果”。

## 建议的研究收敛顺序

[推断] 先以题3为主线，选题7的机构变化或一个更简单的可模拟交互作任务实例；题4提供修复执行器，题11提供保持/后果验证。若你更想研究memory而非编辑训练，题6是另一条清晰主线。题1/9/10/15宜作为支撑模块，不宜一开始同时推进。

[推断] 题5、12、13、15单独表述与池内工作重叠很强，需要先写出比邻居更窄且可证伪的差异。题2更偏叙事与观察者知识，具有相邻但不同的任务契约。以下15题定位均是研究建议，不是已被论文验证的结果。

## 15个研究题的矩阵位置与最近邻

### 1. 少步蒸馏时，保护短暂但决定剧情的关键事件

[推断] 主格：**文本或图像生成视频 × 训练信号**。执行层：适合接在事件编辑系统后，先证明短暂事件确实被少步过程漏掉。

[推断] 任务契约：文本/教师视频、关键事件与采样预算 → 少步视频；保留事件发生、顺序和后果，允许非关键纹理变化。

- [P022 · T2V-Turbo: Breaking the Quality Bottleneck of Video Consistency Model with Mixed Reward Feedback](https://arxiv.org/html/2405.18750)：将mixed reward加入少步蒸馏；未定义短暂事件的重要性保持。
- [P024 · DOLLAR: Few-Step Video Generation via Distillation and Latent Reward Optimization](https://arxiv.org/html/2412.15689)：兼顾少步质量/多样性并揭示自动指标与人评错位；不提供关键事件不变式。
- [P072 · DenseDPO: Fine-Grained Temporal Preference Optimization for Video Diffusion Models](https://arxiv.org/html/2506.03517)：视频分段偏好能让短时间片段进入监督；并非蒸馏或剧情决定性识别。

[推断] 与已有工作的差异/风险：在本论文池内未见把“剧情必要事件召回”作为少步蒸馏的显式约束并独立验证其后果。DenseDPO使一般的“时间细粒度监督”不再足以构成差异。

[推断] 最小判别实验：同一教师样本固定噪声和预算，操控事件持续长度与因果必要性；报告事件召回、后果正确率、无事件对照和质量/延迟Pareto曲线。

### 2. 事件时间与信息揭示时间解耦的视频生成

[推断] 主格：**长视频与多镜头叙事 × 表示**。表示层：与主方向有关，但引入叙事/观察者语义，项目范围会扩大。

[推断] 任务契约：世界事件图、镜头/观察安排和揭示计划 → 多镜头视频；保持世界事件事实，仅改变观众何时看到证据。

- [P056 · Mind the Time: Temporally-Controlled Multi-Event Video Generation](https://arxiv.org/html/2412.05263)：显式绑定事件发生区间并支持scene cuts；没有独立的观众获知时钟。
- [P047 · The World is Your Canvas: Painting Promptable Events with Reference Images, Trajectories, and Text](https://arxiv.org/html/2512.16924)：控制事件时间、轨迹和可见性；可见性控制接近但不等于信息揭示语义。
- [P075 · EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](https://arxiv.org/html/2605.15199)：提供多镜头叙事和实体registry；评测实体一致，而非观众信念随镜头变化。

[推断] 与已有工作的差异/风险：在本论文池内未见明确分开world-event time与information-reveal time并评测两者的生成协议。需区分遮挡、倒叙、悬念与纯事件重排。

[推断] 最小判别实验：同一事件图生成两种揭示顺序；分别测真实事件顺序、每个镜头可见证据、各时刻观察者可回答的问题，防止只换镜头就宣称信息推理。

### 3. 面向事件编辑的视频生成：通过成组干预监督，学习后果传播与非相关内容保持

[推断] 主格：**编辑与修改 × 训练信号**。最贴近总体目标的主线；主格编辑×训练信号，数据和评测是必要的次落点。

[推断] 任务契约：源视频/世界状态、事件干预和保持约束 → 修改视频；改变被干预事件及其必要后果，保持非后代状态与已提交内容。

- [P018 · TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/html/2603.29092)：合成成对轨迹移动监督，且允许新接触改变运动；已覆盖局部后果变化的一部分。
- [P049 · ActionSplice: In-Flight Action Editing for Interactive World Models](https://arxiv.org/html/2609.08230)：matched rollback成组监督修正动作改变后的solver state；作用于未完成chunk。
- [P074 · PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449)：按编辑类型/区域使部分记忆失效并保持有效上下文；依赖已知编辑范围。

[推断] 与已有工作的差异/风险：不能仅以“配对干预＋保持”主张差异。更窄的候选是：在未知影响范围下，学习区分必要后果与应保持内容，并在跨事件组合上验证；在本论文池内未见这一完整契约的统一评测。

[推断] 最小判别实验：模拟器生成同场景同随机源的多分支干预组；设置必要改变集、应保持集及不确定集；同时测后果遗漏率、过度修改率、编辑成功率，并按未见机制/组合拆分。

### 4. 从结构化错误反馈学习视频局部修复，并保持已满足的约束

[推断] 主格：**编辑与修改 × 训练信号**。可收敛的执行子问题；不必先解决完整因果世界建模。

[推断] 任务契约：候选视频、错误位置/类型/理由、已满足约束集合 → 修复视频；改错且不回退已满足项。

- [P035 · CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/html/2605.11723)：输出异常时间窗、空间框和归因，并可作RL reward；没有逐轮约束保持的修复契约。
- [P059 · VideoCoF: Unified Video Editing with Temporal Reasoner](https://arxiv.org/html/2512.07469)：用reasoning frames定位编辑区域再生成；不是从错误反馈学习迭代修复。
- [P067 · Unified In-Context Video Editing](https://arxiv.org/html/2506.04216)：统一多种视频编辑接口；未显式跟踪已满足约束集合。

[推断] 与已有工作的差异/风险：在本论文池内未见把constraint regression作为主要训练与评测对象的通用结构化反馈修复。要区别于已有mask editing与异常reward微调。

[推断] 最小判别实验：人工可核验的错误注入与多轮修复；报告错误消除率、已满足约束破坏率、修复轮数，并在固定重采样预算下比整段重生成/普通mask编辑。

### 5. 可中断的交互视频生成

[推断] 主格：**动作条件的预测与交互世界模型 × 训练信号**。重要系统能力，但单独作为题目与P049高度接近；也可主归架构或推理，取决于最终机制。

[推断] 任务契约：已提交帧、活跃chunk/solver state、任意到达的新控制 → 低延迟续生成；明确哪些已展示帧不可撤回。

- [P049 · ActionSplice: In-Flight Action Editing for Interactive World Models](https://arxiv.org/html/2609.08230)：直接研究采样中断和动作改写，具有rollback与条件替换基线；最直接重叠。
- [P046 · Matrix-game 2.0: An open-source, real-time, and streaming interactive world model](https://arxiv.org/html/2508.13009)：实时动作控制与因果蒸馏；实时吞吐不保证当前chunk可中断。
- [P069 · LongLive: Real-time Interactive Long Video Generation](https://arxiv.org/html/2509.22622)：prompt切换时KV recache；通常在生成边界处理新条件。

[推断] 与已有工作的差异/风险：“可中断”本身在池内已有直接工作。候选差异需落到多次冲突指令、任意控制类型、严格解码前缀保持或新的延迟/质量保证，不能只复述ActionSplice。

[推断] 最小判别实验：在不同solver时刻随机到达更新；同时测从接收到首个正确视觉响应的时间、stale frames、已提交前缀差异与总重复NFE。

### 6. 当新增观测否定生成历史时，怎样修正视频模型的记忆和后续生成？

[推断] 主格：**动作条件的预测与交互世界模型 × 记忆与上下文**。与总体方向高度一致；主格世界模型×记忆，关联编辑×记忆的P074。

[推断] 任务契约：生成历史、记忆与新增外部观察 → 更新后的belief/memory及后续视频；保留仍有效事实，记录被撤销的推断。

- [P074 · PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449)：根据已知编辑更新RGB/深度记忆，避免旧语义重现；不自动判断观察真假。
- [P044 · WorldMem: Long-term Consistent World Simulation with Memory](https://arxiv.org/html/2504.12369)：长期记忆检索与时间条件支持重访；没有一般冲突证据裁决。
- [P050 · Echo-Memory: A Controlled Study of Memory in Action World Models](https://arxiv.org/html/2606.09803)：控制实验揭示容量、读取、压缩与重访表现不同；为记忆修改提供诊断基线。

[推断] 与已有工作的差异/风险：在本论文池内未见完整处理“外部观测冲突→可信度判断→依赖事实失效→后续一致续生成”的协议。已知编辑与观测纠错必须分开。

[推断] 最小判别实验：先让模型推断被遮挡内容，再给可靠/不可靠的矛盾观测；区分用户编辑和观测更新，测修正正确率、有效记忆保留率、旧错误复发率。

### 7. 对象结构或操作机制改变后，能否快速重新生成交互过程并保持其它不变

[推断] 主格：**编辑与修改 × 表示**。主方向的具体可验证场景；若输入仅初图+动作而非源交互，应移至世界模型×表示。

[推断] 任务契约：源交互、对象结构/机制修改和原操作意图 → 新交互视频；保留场景/身份和未受影响动作，重算接触与可行操作。

- [P018 · TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/html/2603.29092)：改变轨迹位置并重算合理接触；未普遍改变关节/操作机制。
- [P017 · Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/html/2602.09600)：手势驱动手物接触、开合等交互；未把机构改变作为受控干预。
- [P043 · AdaWorld: Learning Adaptable World Models with Latent Actions](https://arxiv.org/html/2503.18938)：用latent actions适配环境/动作；没有成对保持其它内容的重生成契约。

[推断] 与已有工作的差异/风险：在本论文池内未见以机构变化（如转轴、锁扣、滑轨）为干预变量、同时要求快速重生成和无关内容保持的系统评测。目标表示不能只用外观mask。

[推断] 最小判别实验：同一物体族控制一个关节/约束参数，其余场景与随机源固定；区分外观改动和机制改动，测运动合法性、任务完成、保持误差和重生成成本。

### 8. 面向视频模型的出题 agent：自动寻找“补哪些数据最值得”

[推断] 主格：**文本或图像生成视频 × 数据**。默认落一般生成×数据；服务事件编辑时改为编辑×数据，任务域必须先定。

[推断] 任务契约：模型错误、预算与候选数据生成器 → 下一批问题/数据；在固定成本下最大化held-out能力增益。

- [P073 · WorldReasonBench: Human-Aligned Stress Testing of Video Generators as Future World-State Predictors](https://arxiv.org/html/2605.10434)：对世界状态推理做分层stress testing，可提供难例空间；未验证按信息增益选择训练数据。
- [P035 · CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/html/2605.11723)：细粒度异常数据与诊断reward，可发现错误类型；不是主动采集价值策略。
- [P058 · FFP-300K: Scaling First-Frame Propagation for Generalizable Video Editing](https://arxiv.org/html/2601.01720)：可扩展成对编辑数据引擎及数据/模型消融；没有闭环最优补数agent。

[推断] 与已有工作的差异/风险：在本论文池内未见用实际后训练边际收益闭环验证的“数据价值出题agent”。发现低分样本并不代表这些样本最值得训练。

[推断] 最小判别实验：等标注/模拟预算比较随机、难度、diversity、不确定性与agent策略；每轮真实更新模型，测新任务泛化和遗忘，隔离训练reward与最终test。

### 9. Agent 能否根据生成任务的难点，获取最少但足够的控制信号，并让视频模型可靠执行？

[推断] 主格：**条件控制生成 × 推理时方法**。可作为主方向的前端；若训练query policy，主贡献可能改为训练信号。

[推断] 任务契约：任务和预算 → 选择/请求控制信号→生成并验证；保持用户已确认条件，最小化交互与测量成本。

- [P012 · MotionAgent: Fine-grained Controllable Video Generation via Motion Field Agent](https://arxiv.org/html/2502.03207)：agent把文本拆成对象/相机控制；未显式优化获取信号的成本。
- [P014 · Any2Caption:Interpreting Any Condition to Caption for Controllable Video Generation](https://arxiv.org/html/2503.24379)：把多类已有条件转成caption；解决解释而非主动选择最少条件。
- [P004 · SparseCtrl: Adding Sparse Controls to Text-to-Video Diffusion Models](https://arxiv.org/html/2311.16933)：稀疏条件可以有效控制；并非根据不确定性决定向用户/工具索取哪个信号。

[推断] 与已有工作的差异/风险：在本论文池内未见同时学习“最少信号获取”与“足够执行”的完整闭环。不可仅统计条件数量而忽略其精度、成本及不可观测性。

[推断] 最小判别实验：逐步给相机、单点、关键帧等信号；比较固定套餐与自适应查询，画成功率—获取成本曲线，并测试含噪/冲突控制。

### 10. 时空 credit assignment

[推断] 主格：**文本或图像生成视频 × 训练信号**。通用训练模块；用于选择性编辑时主格转编辑×训练信号。

[推断] 任务契约：生成轨迹、局部错误/reward及事件依赖 → 有针对性的训练更新；区分视频时间t、去噪步s、空间区域x。

- [P032 · Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/html/2604.19234)：对denoising timestep与reward objective分配credit；不等同视频时间/空间归因。
- [P072 · DenseDPO: Fine-Grained Temporal Preference Optimization for Video Diffusion Models](https://arxiv.org/html/2506.03517)：视频片段级偏好监督；提供video-time维度但不是像素空间credit。
- [P035 · CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/html/2605.11723)：异常时间窗与空间框能定位问题；定位证据不直接等于策略梯度credit。

[推断] 与已有工作的差异/风险：题目过宽且已有三种相邻机制。候选需明确是哪一轴、credit如何估计、是否因果，以及为何比全局reward有效。

[推断] 最小判别实验：使用已知局部故障和依赖链，比较t、s、x单轴及联合归因；控制计算量，测局部修复和非目标退化。

### 11. video-native verifier

[推断] 主格：**视频作为推理或回答 × 评测**。若核心是训练可用reward则落训练信号；这里按新评测协议/验证器基准先落视频推理×评测。

[推断] 任务契约：视频、任务契约与保持条件 → 可定位的违反项、证据及不确定性；不能只给单一质量分。

- [P036 · Video Models Can Reason with Verifiable Rewards](https://arxiv.org/html/2605.15458)：用可解析轨迹和规则验证视频解题；验证范围受任务规则限制。
- [P073 · WorldReasonBench: Human-Aligned Stress Testing of Video Generators as Future World-State Predictors](https://arxiv.org/html/2605.10434)：过程阶段问题与human calibration；近分样本仍有judge不稳定。
- [P035 · CaC: Advancing Video Reward Models via Hierarchical Spatiotemporal Concentrating](https://arxiv.org/html/2605.11723)：定位稀疏时空异常并给归因；物理/视觉异常检测不等于完整任务正确性。

[推断] 与已有工作的差异/风险：“视频验证器”在池内有多种实现，单凭video-native不足以定位差异。更具体的缺口是验证“必要改变＋不应改变”及状态依赖，而非逐帧caption后打分。

[推断] 最小判别实验：构造画质匹配但状态错误的对照、极短事件和遮挡后果；测漏检/误报、定位、校准及跨模型泛化，另做reward优化后的抗hacking测试。

### 12. 低成本的 online rollout

[推断] 主格：**动作条件的预测与交互世界模型 × 架构与生成范式**。基础设施方向；若不引入选择性状态重算，与用户总体目标联系较弱。

[推断] 任务契约：当前policy、世界模型与观测 → 低成本且有效的在线想象数据；保持动作分布一致和可用状态预测。

- [P068 · Horizon Imagination: Efficient On-Policy Rollout in Diffusion World Models](https://arxiv.org/html/2602.08032)：直接优化并行多未来步on-policy imagination与稳定动作采样。
- [P048 · Training Agents Inside of Scalable World Models](https://arxiv.org/html/2509.24527)：快速世界模型用于想象训练agent，shortcut forcing改善成本。
- [P042 · Diffusion for World Modeling: Visual Details Matter in Atari](https://arxiv.org/html/2405.12399)：少步diffusion世界模型支持Atari想象训练；场景和分辨率较受限。

[推断] 与已有工作的差异/风险：池内已有直接目标重叠。需要先区分训练时on-policy rollout、面向用户的实时渲染、以及真实环境在线交互，再选具体瓶颈。

[推断] 最小判别实验：固定总训练预算比较并行与顺序rollout，联合报告NFE、端到端时间、显存、回报/任务成功、action consistency和误差累积。

### 13. flow/diffusion 中 policy 与 exploration 的正确定义

[推断] 主格：**文本或图像生成视频 × 训练信号**。理论/训练基础方向，暂默认一般生成×训练信号；与事件编辑结合需另定任务。

[推断] 任务契约：给定生成器、噪声、solver与reward → 明确定义的随机policy及更新规则；说明探索发生于初始噪声、SDE转移还是环境动作。

- [P033 · Manifold-Aware Exploration for Reinforcement Learning in Video Generation](https://arxiv.org/html/2603.21872)：定义flow/SDE-GRPO下探索噪声、梯度平衡和trust region；直接邻近。
- [P028 · Improving Video Generation with Human Feedback](https://arxiv.org/html/2501.13918)：Flow-DPO、Flow-RWR与Noisy Reward Guidance提供不同优化对象。
- [P036 · Video Models Can Reason with Verifiable Rewards](https://arxiv.org/html/2605.15458)：SDE-GRPO用于规则验证任务，并分析早期去噪更新。

[推断] 与已有工作的差异/风险：不存在无需建模约定就唯一适用的policy定义；候选贡献是证明哪些随机化/估计器相容、何时有偏以及对视频任务的影响。不能把几种概念混成新算法名。

[推断] 最小判别实验：固定生成分布/预算，比较ODE初始噪声、SDE逐步噪声和离散solver policy；检验likelihood ratio、梯度偏差、KL和diversity，而非只报reward升高。

### 14. long horizon identity/causal consistency

[推断] 主格：**长视频与多镜头叙事 × 记忆与上下文**。可作为主方向的长程版本；动作环境中应转世界模型×记忆。

[推断] 任务契约：长视频历史、实体registry与事件/编辑记录 → 续生成；身份相同且状态按事件合法变化。

- [P075 · EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](https://arxiv.org/html/2605.15199)：跨镜头人物/物体/地点身份评测和entity memory；不等于状态因果正确。
- [P044 · WorldMem: Long-term Consistent World Simulation with Memory](https://arxiv.org/html/2504.12369)：场景重访与时间记忆；强调世界状态历史而非纯多镜头身份。
- [P074 · PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/html/2606.16449)：已知编辑后保留最新状态并使旧记忆失效；提供更新与保持的接口。

[推断] 与已有工作的差异/风险：必须拆成identity consistency和causal/state consistency：同一人可换衣服，已打碎物体不应无因复原。在本论文池内未见统一覆盖长叙事、干预后果及选择性保持的强协议。

[推断] 最小判别实验：长间隔离场重入，区分身份变化、合法状态变化、非法状态回退；分开报告ID、状态转移和记忆过时率，避免用图像相似度替代因果。

### 15. 多目标 reward 的稳定优化

[推断] 主格：**文本或图像生成视频 × 训练信号**。适合作为事件编辑/修复的训练支撑；通用多目标优化本身范围太广。

[推断] 任务契约：多个可能冲突的reward及约束 → 稳定更新的生成器；关键保持条件不应被平均分抵消。

- [P032 · Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/html/2604.19234)：阶段依赖的多目标credit融合是直接邻近。
- [P028 · Improving Video Generation with Human Feedback](https://arxiv.org/html/2501.13918)：多维VideoReward与flow对齐，提供组合reward和偏好建模。
- [P054 · WorldReward: Reward Modeling for Camera-Conditioned World Models](https://arxiv.org/html/2609.03952)：动作对齐、外观、运动共同构成世界模型reward，实验包含reward组件对照。

[推断] 与已有工作的差异/风险：静态加权与自适应融合已有池内工作。更贴合主方向的候选是把“不得破坏已满足约束”建模为约束优化，而非又一种reward权重调度。

[推断] 最小判别实验：构造可控冲突任务，报告各目标的Pareto front、最坏约束违反率、跨seed方差、训练崩溃/回退和抗reward hacking；与固定权重、动态融合比较。

## 阅读与复核限制

全文检索定位覆盖方法、实验、消融与相关补充；没有重新运行原论文实验，也没有替作者补填未报告的人数。user study中“每题若干评价者”“判断总数”“视频数”和“独立参与者数”分别记录。只有某篇明确的人数才能用于样本量判断；未核实的字段保留不确定。

本报告不作“没有人做过”的断言。空格只意味着这个按来源/年份抽样的池内没有对应主贡献样本；新颖性表述均限定在本论文池内。原始来源快照与全文保存在本地，公开页面仅提供自写中文摘要/分析、元数据、定位及原论文链接。
