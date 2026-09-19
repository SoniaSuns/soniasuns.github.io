"""Build the source-linked RQ atlas from the local PDF inventory and curated relations.

Run from the research workspace: python website/_tools/rq-map/build.py
Only a PDF in the inventory counts as collected. Downloads are managed separately.
"""
import collections
import html
import json
import pathlib
import re

SITE = pathlib.Path(__file__).resolve().parents[2]
ROOT = SITE.parent
DATE = "2026-09-19"
catalog_path = SITE / "_data/literature_review/catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8")) if catalog_path.exists() else {}
aliases = catalog.get("historical_aliases", {"P003":"P002", "P082":"P081", "P109":"P103"})

def canonical(identifier):
    return aliases.get(identifier, identifier)

routes = [
    dict(id="world", label="世界机制与演化", root="W0", question="在规则不完整、会变化或违背常识时，如何建立可执行、可检验、可修订的世界机制，并让长期演化与干预后果持续遵循这些机制？", explanation="核心对象是状态、规则和状态转移。先区分机制发现、给定规则的执行、创作者指定规则，以及仅生成视觉上连贯的内容。", anchors=["P150", "P156", "P154", "P157", "P071", "P158", "P147"], metrics="转移预测与规划成功；规则满足率；干预影响与不受影响部分的保持；长程状态一致性；有效演化的多样性。"),
    dict(id="xr", label="XR 与人机协作", root="X0", question="在部分可观测、人的注意力和行动能力受限的情境中，智能体如何与人建立并修正共享理解，选择观察、提问、提示或交还控制，以低交互成本实现可靠协作？", explanation="核心对象是人与智能体的协作过程。重点不只是识别当前场景，而是表达假设、共同取证、选择介入方式，并允许人纠正错误推断。", anchors=["P055", "P059", "P061", "P041", "P143", "P157", "P159"], metrics="团队任务成功；证据获取收益；提问、身体行动与打扰成本；错误假设修复；恰当依赖；认知负荷与可访问性。"),
]

parents = [
    ("W1", "world", "获得机制", "世界规则从哪里来，应该用什么表示才能学习、执行和迁移？", "P121 P150 P154 P156 P157"),
    ("W2", "world", "改变条件", "当前提、规则或证据变化时，哪些结论和演化必须改变，哪些必须保持？", "P011 P017 P021 P071 P084 P158"),
    ("W3", "world", "持续演化", "时间、镜头、参与者和编辑次数增加后，如何保持状态与机制一致？", "P135 P128 P145 L163 P147 P160"),
    ("W4", "world", "推理与验证", "如何把机制用于多步推理，并判别正确机制、可靠证据与表面连贯？", "P104 P103 P078 P087 P044"),
    ("X1", "xr", "共享情境", "人与智能体怎样知道彼此指什么、想做什么，以及还缺什么证据？", "P061 P141 P155 P143 P157"),
    ("X2", "xr", "分配主动权", "何时应该询问、等待、建议、自主行动或请求人接管？", "P055 P059 P149 P159 P041 P001"),
    ("X3", "xr", "校准与修复", "怎样让人恰当地依赖、检查和纠正智能体，并检验协作是否真的有效？", "P038 P148 P065 P091 P067"),
    ("X4", "xr", "创作与可访问性", "怎样让人能构建、修改和使用这些协作机制，而不过度依赖开发专家？", "P060 P062 P036 P058"),
]
parents = [dict(id=i, route=r, label=l, question=q, anchors=a.split()) for i, r, l, q, a in parents]

branches = []
def branch(i, parent, label, question, before, after, gap, core, support="", anchors=""):
    branches.append(dict(id=i, parent=parent, route="world" if i.startswith("W") else "xr", label=label, question=question, before=before, after=after, gap=gap, core=core.split(), support=support.split(), anchors=(anchors or core).split()[:5], rq_origin="跨论文综合归纳；不是作者逐字给出的统一 RQ"))

branch("W1a", "W1", "从描述到规则", "自然语言设定怎样变成可被规划器执行的前置条件与效果？", "世界作为一段描述", "世界作为有类型、谓词和动作语义的模型", "可解析、与参考结构相似，仍不等于所有轨迹行为等价。", "P154", "P160 P062", "P154 P160")
branch("W1b", "W1", "从经验到程序", "能否用少量交互学习、调试并组合世界转移程序？", "神经网络动力学，或一次性完整程序", "可修改的 Python 模型 → 多个带权程序专家；加入随机性与部分可观测性", "WorldCoder 的确定性符号环境与 PoE-World 的对象输入，不能直接外推到任意原始视觉环境。", "P150 P156", "S06 S04", "S06 P150 P156")
branch("W1c", "W1", "从视频到可控动力学", "视频表征怎样支持动作条件预测，并把动作语义迁移到新场景？", "被动预测未来画面，或有动作标签的控制数据", "潜空间想象、视频 token、无标签潜动作、跨场景动作对齐", "潜动作和逼真视频不自动带来可识别的因果机制；加速与几何控制是实现条件。", "P121 P123 P124 P132 P106 P081 P083 S01 S02 S03 S04 S05", "P013 P068 L162 L164", "P121 P123 P124 P081")
branch("W1d", "W1", "主动发现隐藏机制", "当规则未知时，怎样选实验、整合跨轮证据，并适应机制突变？", "观察与答案预先给定，环境规则固定", "主动干预、跨试次记忆、未知因果结构与规则突变", "P157 已有模型请求人执行 3D 动作的原型；机会在复杂机制与人的成本联合优化。", "P142 P143 P152 P157 P014 S12", "P012", "P142 S12 P143 P152 P157")
branch("W2a", "W2", "抵抗默认常识", "明确给出反常识前提后，模型能否按新规则推理而非复述旧知识？", "默认规则和常识一致", "坐标/任务规则置换、反事实知识、反常事件和不可能视频", "指令中的反事实规则、因果叙事和要求生成不可能情境，是不同实验问题。", "P011 P015 P043 P042 P045 P009 P070", "P077", "P011 P015 P043 P042")
branch("W2b", "W2", "溯因与撤销假设", "如何从不完整观察形成解释，并在新证据到来后增强、削弱或撤销解释？", "静态文本的最合理解释", "图像/视频线索、隐藏事件、多假设及可撤销推断", "合理解释不是被识别的真实原因；生成的想象图像也不是新观测。", "P002 P005 P007 P008 P016 P017 P019 P020 P021 P027 P030 S13", "", "P002 P008 S13 P017 P021")
branch("W2c", "W2", "干预与反事实", "怎样显式指定改变的变量，同时保持其余机制，并产生可核验的后果？", "事实视频外推，或只改变提示词", "结构化对象/关系、给定因果图、数字孪生条件与反事实负例", "P125 依赖给定图；P071 的孪生并非经验证的物理引擎；P130 是动作语义替换。", "P071 P125 P130", "P064 P063 P047 P044", "P071 P125 P130 P063")
branch("W2d", "W2", "规则一致性的评测", "怎样区分画质、指令遵循、事件完成与真正的规则一致性？", "看起来合理的单段生成", "保持事件、改变外观/视角；逐规则核验；要求反常识规则", "CRONOS 主要测外观条件变化下的物理稳定性；RULER 的归一化评分不是整条轨迹全对率。", "P158 P084 P028 P139", "P073", "P158 P084 P139")
branch("W3a", "W3", "长程世界记忆", "离开再返回、时间推进或反复更新记忆后，怎样保留正确状态？", "局部时间窗口", "帧—位姿—时间记忆、状态空间长上下文、持续记忆更新", "视觉重现、动态状态更新与记忆不失真需分开验证；训练外的无限记忆未被证明。", "P085 P102 P137 P135 P097", "P024", "P135 P102 P097")
branch("W3b", "W3", "事件与跨镜头叙事", "怎样把多事件故事展开成长期序列，并保持实体、动作和事件完成？", "逐句图像与短片续接", "显式布局/关键帧、分层导演、跨镜头记忆与事件级评估", "角色一致、布局一致和故事偏好不能代替因果机制或物理正确性。", "P010 P039 P120 P122 P127 P128 P129 P133 P134 P136 P138 P139 P140 P161 S27", "P101 P131", "P138 P039 P136 P128 P161")
branch("W3c", "W3", "多主体与开放演化", "怎样使局部规则产生可解释的群体行为、协作或持续新颖演化？", "单一智能体、固定目标", "Game Master 维护共同世界、联合动作预测；搜索模拟参数和新颖行为", "Concordia 的社会模拟、COMBO 的协作预测、ASAL 的人工生命搜索是三个侧面，不能互相当作验证。", "P145 P151 L163 S07 S08 S09", "P074", "S09 P145 P151 S07 L163")
branch("W3d", "W3", "创作者修改世界", "人修改规则或任务节点后，如何更新相关后果并保留无关内容？", "一次性设定/生成", "计划树、任务图、分层设定与迭代审核", "DreamGarden 是较粗的撤销重做；AutoWorldBuilder 尚未实现关系解析。精确依赖更新仍是待验证机会。", "P036 P147 P160", "L164 P072", "P147 P036 P160")
branch("W4a", "W4", "组合与搜索（方法支撑）", "当推理深度与分支增加时，什么表示与搜索机制支持全局约束？", "单条文字 CoT 或固定计算预算", "显式状态规划、树搜索、连续潜推理、能量组合与训练/采样策略", "这些论文多用数学/合成任务；支持推理组件，不等于已实现可编辑物理世界。", "P104 P105 S10 S11 S22", "P006 P018 P023 P025 P026 P103 P108 P113 P114 P116 P034 P037 P073 P077 P107 P112 P117 P115 P031", "S10 P104 P103 P023 P034")
branch("W4b", "W4", "推理是否仍有视觉依据", "长推理过程中怎样发现证据丢失、重新观察并约束输出？", "一次视觉编码后继续语言推理", "时间定位、证据池、双流解码、特征重访和过程监督", "注意力、熵与视觉依赖是代理指标；‘关注了’不等于因果使用或答对。", "P069 P075 P078 P086 P087 P088 P089 P092 P093 P098 P099 P100", "P090", "P078 P087 P086 P092 P100")
branch("W4c", "W4", "校准、漂移与有效推断", "模型或数据机制变化后，怎样判断结论仍可靠且对决策有用？", "静态准确率和合成数据拟合", "概念漂移归因、因果校准、真实/合成数据推断及多任务时间序列评价", "统计识别、交换性和数据条件需明确；这组是验证方法支撑，不是世界生成系统。", "", "P046 P044 P047 P051 P052 P063 P096", "P046 P044 P052 P096")
branch("W4d", "W4", "生成过程作为推理", "视频生成过程能否执行规则与计算视觉答案，训练或测试时外援分别贡献了什么？", "用 VLM 先求解，再把结果交给视频生成器", "区分无外援生成、外部教师监督、测试时优化，以及生成预训练到感知的迁移", "视觉轨迹像推理步骤不代表步骤忠实；需要任务规则、未见组合、过程约束和外部依赖消融。", "P158", "", "P158")
branch("X1a", "X1", "空间指涉与表达", "怎样让‘这个/那里/这样做’成为双方共享、可消歧的空间信息？", "屏幕上的语音+指向；用户输入端消歧", "可穿戴注视/指向/历史；对象锚定；智能体输出同步手势", "AgentHands 依赖预扫描对象与有限手势；不能视为开放世界的任意动作理解。", "P061 P057 S17 S18 S24", "", "S18 S17 S24 P061")
branch("X1b", "X1", "目标与任务状态", "怎样从示范、第一人称历史或动作表现推断用户目标与下一步需求？", "显式目标或单张当前画面", "观察后协助、历史进度、他者意图、动作技能反馈与 BDI 用户模型", "离线下一动作选择不等于闭环执行；专家式反馈不等于已证明长期技能提升。", "P141 P155 P151 P146 S23", "", "P141 P155 P151 S23")
branch("X1c", "X1", "通过行动获得证据", "不知道发生了什么时，应该看哪里、问谁，或请求人执行什么辨别动作？", "固定观察与文本澄清", "主动转头/视频搜索、物理实验、由人执行的取证动作", "要区分澄清已有事实和创造新证据；P143/P157 已覆盖实验式取证，尚不足以验证自然 XR 中的负担权衡。", "P143 P157 P079 P095 S12", "P005 P007 P009 P020 P021 P027 P030 P069 P075 P088", "P143 P157 P079 P095")
branch("X2a", "X2", "何时与怎样澄清", "怎样识别缺失条件，并用尽量少的问题获得正确决策所需信息？", "直接猜测或给出所有可能回答", "对话动作偏好学习；按条件 DAG 提问并裁剪分支", "ACT/GPS 的用户主要提供已知信息；未学习通过身体行动产生新证据的策略。", "P149 P159 S21", "S19", "P149 S21 P159")
branch("X2b", "X2", "主动介入与打扰成本", "如何共同决定提供什么帮助、是否介入，以及何时用何种通道交互？", "用户发起请求，或只预测潜在需求", "将需求、通道可用性、社会情境和打扰成本一起考虑", "小规模原型研究支持具体交互收益；尚不能推出长期部署中最优介入策略。", "P055 P059 S15 S16 S23 S25", "", "P055 S15 S16 S23 P059")
branch("X2c", "X2", "控制权与团队效用", "何时交给人、让机器做，或更新知识，才能最大化团队净收益？", "机器单独准确率，算法决定采样/接管", "人自主接管、联合优化求助策略、将错误与获取信息的成本纳入决策", "驾驶、离线分类、合约问答与 XR 各有边界；迁移需要真实的人的能力/成本模型。", "P001 P041 P022 S14 S20", "P048 P049 P050 P054", "S14 P001 P041 P048")
branch("X3a", "X3", "不确定性与恰当依赖", "什么不确定性可信，怎样表达才帮助用户正确决定是否依赖？", "token 概率或一句‘不确定’", "语义簇、层间一致性、隐状态探针、来源分解与用户依赖实验", "检测器、概率校准、表达方式和人的信任是四个不同环节；一致错误不会被语义熵自动发现。", "P038 P110 P118 P119 P144 P148 P153 S26", "", "P144 P148 P038 P110")
branch("X3b", "X3", "核查、反馈与修复", "怎样让用户检查和修改关键假设，并让修正有效进入后续行为？", "线性解释与最终答案反馈", "局部 CoT 编辑、图/程序解释、过程监督、反思和知识更新", "可见 CoT 不一定忠实反映内部计算；人提供的新知识须计入协作成本与收益。", "P065 P066 P076 P080 P091 P012 P022", "P090 P097 S19", "P065 P080 P076 P091")
branch("X3c", "X3", "协作评测与真实效用", "如何测持续协作可靠性，而不只测模型某次答对？", "单轮静态问答与独立模型排行榜", "用户—工具—规则交互、重复成功、跨应用产物验证和部署效用", "模拟用户或离线医疗评分不等于真实人机团队或真实部署获益。", "P067 P094 P111", "P053 P051 P004 S20", "P067 P094 P111 P051")
branch("X4a", "X4", "可检查的协作创作工具", "怎样用自然语言和可编辑中间表示降低原型/内容创作成本？", "手写代码、黑盒生成与单个建议", "Visual Blocks/XR 模块、任务图、备选方案比较及人在环修改", "原型速度与创作偏好不证明底层机制正确；通用图像/视频创作论文作为相关界面设计参照。", "P056 P060 P062 P036 P147 P029", "P032 P035 P033 P040 P126", "P062 P060 P036 P147")
branch("X4b", "X4", "可访问性与设计规范", "通用指南在具体 XR 场景里能否被开发者执行，并覆盖不同能力的用户？", "抽象设计原则或事后修补", "开发工作流中的可操作指南；按用户通道与能力适配", "行业访谈暴露执行障碍，不是对全部残障群体体验的效果验证。", "P058 S19", "P055 S15", "P058 S19 S15")

# External records are reference-verified additions, not locally collected PDFs.
external_rows = [
    ("S01", "PILCO: A Model-Based and Data-Efficient Approach to Policy Search", "PILCO", "2011", "Deisenroth & Rasmussen", "https://spiral.imperial.ac.uk/entities/publication/5d3d92ac-439a-47c4-beb8-311c3c7122cc", "用概率动力学与不确定性传播减少控制学习所需的真实交互。", "概率模型与近似推断条件下的控制；不是通用视频模拟。", "P121", 1, "P121 PDF pp.9、11、16；作者机构库摘要"),
    ("S02", "On Learning to Think: Algorithmic Information Theory for Novel Combinations of Reinforcement Learning Controllers and Recurrent Neural World Models", "On Learning to Think", "2015", "Jürgen Schmidhuber", "https://arxiv.org/abs/1511.09249", "讨论控制器如何利用循环世界模型进行预测与求解。", "理论框架与历史脉络，不是后来视频世界模型的统一实证基线。", "P121", 1, "P121 PDF p.2、p.20；arXiv 原始记录"),
    ("S03", "Dream to Control: Learning Behaviors by Latent Imagination", "Dreamer", "2020 / 2019", "Hafner et al.", "https://arxiv.org/abs/1912.01603", "在紧凑潜空间想象轨迹，并通过价值梯度学习长程行为。", "依赖学习的动力学；没有可编辑符号规则或物理正确性保证。", "P123", 1, "P123 PDF p.15；Dreamer §1、§4–5"),
    ("S04", "Mastering Diverse Domains through World Models", "DreamerV3", "2023（预印本）", "Hafner et al.", "https://arxiv.org/abs/2301.04104", "通过稳定化训练使世界模型控制器在多领域使用同一配置。", "学得任务控制能力，不代表任意规则的因果识别。此处对应被引用的 2023 预印本题名。", "P156", 1, "P156 PDF p.1、参考文献[1] p.11；arXiv v2"),
    ("S05", "Learning Latent Dynamics for Planning from Pixels", "PlaNet", "2019 / 2018", "Hafner et al.", "https://arxiv.org/abs/1811.04551", "从图像学潜在状态动力学，在潜空间中在线规划。", "与 Dreamer 的策略/价值学习不同，主要用在线规划。", "S03", 2, "Dreamer §4 Reconstruction、§5 Control with latent dynamics；arXiv 原文"),
    ("S06", "Human-Level Reinforcement Learning through Theory-Based Modeling, Exploration, and Planning", "Theory-based RL", "2021", "Tsividis et al.", "https://arxiv.org/abs/2107.12544", "用可组合的游戏理论、实验式探索和规划提高样本效率。", "预设表示与游戏环境；WorldCoder 后续改用通用 Python 和 LLM 先验。", "P150", 1, "P150 PDF p.2、参考文献[67] p.14；arXiv 摘要"),
    ("S07", "Lenia — Biology of Artificial Life", "Lenia", "2019 / 2018", "Bert Wang-Chak Chan", "https://arxiv.org/abs/1812.05433", "研究连续细胞自动机中的自组织生命形态及其参数空间。", "人工生命基底，不等于已实现真实生物进化。", "L163", 1, "ASAL PDF pp.1–2、参考文献 p.14；Lenia 摘要"),
    ("S08", "Abandoning Objectives: Evolution Through the Search for Novelty Alone", "Novelty Search", "2011", "Lehman & Stanley", "https://doi.org/10.1162/EVCO_a_00025", "以行为新颖性驱动搜索，减少预定义目标的欺骗性。", "新颖性不自动等于有用性或无限开放演化。", "L163", 1, "ASAL PDF p.16 参考文献；原论文 PDF 镜像 https://gwern.net/doc/reinforcement-learning/exploration/2011-lehman.pdf"),
    ("S09", "Generative Agents: Interactive Simulacra of Human Behavior", "Generative Agents", "2023", "Park et al.", "https://arxiv.org/abs/2304.03442", "以记忆、反思与规划支持可信的社会行为模拟。", "行为可信度和涌现示例不等于真实社会预测有效性。", "P145", 1, "P145 PDF p.8 明确复用 Park 等的关联记忆；arXiv 摘要"),
    ("S10", "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models", "Chain of Thought", "2022", "Wei et al.", "https://arxiv.org/abs/2201.11903", "通过中间文字步骤的示例提示改善多步任务表现。", "输出推理文本不保证忠实或正确。", "P104", 1, "P104 PDF pp.1–2 明确对照；原论文摘要"),
    ("S11", "Tree of Thoughts: Deliberate Problem Solving with Large Language Models", "Tree of Thoughts", "2023", "Yao et al.", "https://arxiv.org/abs/2305.10601", "把单条推理扩展成可评估、回溯的候选思维搜索树。", "RAP 将其列为并行相关工作，不能说 RAP 由它单向演化而来。", "P104", 1, "P104 PDF p.2 使用 concurrently；ToT 摘要"),
    ("S12", "ACRE: Abstract Causal REasoning Beyond Covariation", "ACRE", "2021", "Zhang et al.", "https://openaccess.thecvf.com/content/CVPR2021/html/Zhang_ACRE_Abstract_Causal_REasoning_Beyond_Covariation_CVPR_2021_paper.html", "通过对象与 Blicket 机器观察测试超越共现的抽象因果归纳。", "给定观察的推断；IVRE 才进一步让智能体主动操作并更新信念。", "P143", 1, "P143 PDF pp.2–4 明确继承 ACRE 设置；CVPR 官方页面"),
    ("S13", "Thinking Like a Skeptic: Defeasible Inference in Natural Language", "Defeasible NLI", "2020", "Rudinger et al.", "https://aclanthology.org/2020.findings-emnlp.418/", "新信息如何增强或削弱原本合理的自然语言推断？", "一般可撤销推断不一定涉及因果关系。", "P017", 1, "P017 PDF p.3 区分 δ-NLI 与 δ-CAUSAL，p.11 引用；P021 p.10 [31]"),
    ("S14", "A Reduction of Imitation Learning and Structured Prediction to No-Regret Online Learning", "DAgger", "2011", "Ross, Gordon & Bagnell", "https://proceedings.mlr.press/v15/ross11a.html", "聚合当前策略遇到的状态与专家标签，缓解行为克隆的分布偏移。", "原始采样/控制机制对实时人类专家的负担，促成 HG-DAgger 的人控接管。", "P001", 1, "P001 PDF pp.1–2；AISTATS 官方论文页"),
    ("S15", "Human I/O: Towards a Unified Approach to Detecting Situational Impairments", "Human I/O", "2024", "Liu et al.", "https://arxiv.org/abs/2403.04008", "用第一人称感知估计眼、耳、手和发声通道的可用性。", "主要检测情境障碍；没有联合解决主动帮助内容选择。", "P059", 1, "P059 PDF p.2、p.18 [41]；作者 arXiv 摘要"),
    ("S16", "OmniActions: Predicting Digital Actions in Response to Real-World Multimodal Sensory Inputs with LLMs", "OmniActions", "2024", "Li et al.", "https://arxiv.org/abs/2405.03901", "由现实图像/音频与情境预测用户希望进行的数字后续动作。", "动作意图预测不等于情境中的时机与通道协调。", "P059", 1, "P059 PDF pp.2–3、p.18 [34]；作者 arXiv 摘要"),
    ("S17", "GazePointAR: A Context-Aware Multimodal Voice Assistant for Pronoun Disambiguation in Wearable Augmented Reality", "GazePointAR", "2024", "Lee et al.", "https://makeabilitylab.cs.washington.edu/project/gazepointar/", "联合语音、注视、指向和会话历史消解可穿戴 AR 中的代词指涉。", "侧重理解用户指向；AgentHands 转向智能体如何通过手势向人表达。", "P061", 1, "P061 PDF p.3、p.16 [38]；作者实验室论文全文"),
    ("S18", "“Put-That-There”: Voice and Gesture at the Graphics Interface", "Put-That-There", "1980", "Richard A. Bolt", "https://doi.org/10.1145/800250.807503", "结合语音和指向，使用户能用指示代词操纵图形对象。", "基于 GazePointAR 正文对该工作的描述和原始参考条目核验；本轮 ACM 全文未能访问。", "S17", 2, "GazePointAR PDF pp.2–3、p.14 [9]"),
    ("S19", "Guidelines for Human-AI Interaction", "Human–AI Guidelines", "2019", "Amershi et al.", "https://www.microsoft.com/en-us/research/wp-content/uploads/2019/01/Guidelines-for-Human-AI-Interaction-camera-ready.pdf", "整理初次使用、日常交互、错误与长期使用中的人机交互规范。", "设计指南不是对任意应用协作收益的实验保证。", "P149", 1, "P149 PDF p.1、p.13 参考文献；Microsoft Research 原论文"),
    ("S20", "Beyond Accuracy: The Role of Mental Models in Human-AI Team Performance", "Beyond Accuracy", "2019", "Bansal et al.", "https://ojs.aaai.org/index.php/HCOMP/article/view/5285", "研究人对模型错误边界的认识如何影响团队表现。", "提高机器准确率并不必然提高团队效用；不能直接推出 XR 的效果。", "P041", 1, "P041 PDF p.7 参考文献；HCOMP 官方论文页"),
    ("S21", "ConditionalQA: A Complex Reading Comprehension Dataset with Conditional Answers", "ConditionalQA", "2022", "Sun, Cohen & Salakhutdinov", "https://aclanthology.org/2022.acl-long.253/", "要求同时回答问题及列出答案成立的条件。", "条件化阅读理解为 GPS 的主动询问提供任务基础；本身不是物理实验。", "P159", 1, "P159 PDF p.7、p.14 参考文献；ACL 官方论文页"),
    ("S22", "ReAct: Synergizing Reasoning and Acting in Language Models", "ReAct", "2023 / 2022", "Yao et al.", "https://arxiv.org/abs/2210.03629", "交替生成推理与环境动作，让外部观察反馈进入后续推理。", "与学习可执行转移程序不同，推理/行动仍主要由 LLM 在线产生。", "P150", 1, "P150 PDF pp.1–2 明确比较；原论文摘要"),
    ("S23", "Satori: Towards Proactive AR Assistant with Belief-Desire-Intention User Modeling", "Satori", "2025 / 2024", "Li et al.", "https://arxiv.org/abs/2410.16668", "用信念—欲望—意图用户模型组织主动 AR 帮助的推断。", "显式 BDI 不等于已校准的多假设推断或可纠正机制。", "P059", 1, "P059 PDF p.18 [33]；CHI DOI 10.1145/3706598.3714188；亦见本地 XR 草稿"),
    ("S24", "Augmented Object Intelligence with XR-Objects", "XR-Objects", "2024", "Dogan et al.", "https://arxiv.org/abs/2404.13274", "让现实对象成为带情境菜单、查询与数字操作的交互入口。", "对象语义和动作入口不等于已辨明隐藏原因。", "P061", 1, "P061 PDF p.3 引用 Dogan 等[12]；Google Research 论文页；亦见 XR 草稿"),
    ("S25", "AiGet: Transforming Everyday Moments into Hidden Knowledge Discovery with AI Assistance on Smart Glasses", "AiGet", "2025", "Cai et al.", "https://arxiv.org/abs/2501.16240", "通过智能眼镜在日常低负荷时刻主动呈现与环境有关的知识。", "Sensible Agent 将其与时间紧迫、社会约束强的辅助场景区分。", "P059", 1, "P059 §1 对照 AiGet；arXiv 作者摘要；亦见 XR 草稿"),
    ("S26", "Bubbleu: Exploring Augmented Reality Game Design with Uncertain AI-based Interaction", "Bubbleu", "2023", "Kim et al.", "https://doi.org/10.1145/3544548.3581270", "对象检测会出错时，模糊性、透明性与可控性怎样改变 AR 游戏体验？", "手机 AR 游戏中的感知错误设计，不等于 LLM 语义置信度校准。", "abductive/conclusion.md", 1, "本地阅读笔记提出线索，ACM 正式论文摘要及作者 PDF 另行核验"),
    ("S27", "NUWA-XL: Diffusion over Diffusion for eXtremely Long Video Generation", "NUWA-XL", "2023", "Yin et al.", "https://aclanthology.org/2023.acl-long.73/", "以全局关键帧和局部递归扩散降低长视频训练/推理差距。", "长视频渲染与全局连贯不自动构成动作条件世界机制。", "P127", 1, "P127 PDF p.14 参考文献；ACL 官方论文页；亦见本地 VideoGeneration 报告"),
]

def local_links(text):
    return [dict(label=html.unescape(label), url=url) for label, url in re.findall(r"\[([^\]]+)\]\((https?://[^)]+)\)", text)]

records = []
for file in sorted((SITE / "_data/literature_review").glob("papers_*.json")):
    records.extend(json.loads(file.read_text(encoding="utf-8")))
manifest = json.loads((ROOT / "literature-corpus/manifest.json").read_text(encoding="utf-8"))
docs = {d["paper_id"]: d for d in manifest["documents"] if d["paper_id"]}
papers = []
for r in records:
    d = docs[r["id"]]
    papers.append(dict(id=r["id"], title=html.unescape(r["title"]), short=html.unescape(r["title"].split(":")[0]), year=r["year"], authors=r["authors"], collected=True, note=r["id"].lower(), scope="本地全文笔记", summary=html.unescape(r["abstract_zh"]), boundary=html.unescape(r["boundary"]), evidence=r["evidence"], sources=[s.replace("\\", "/") for s in d["sources"]], sha256=d["sha256"], pages=d["pages"], links=local_links(r.get("paper_links", "")), verified=r.get("verified", ""), mappings=[]))

annotation_path = SITE / "_data/literature_annotations.json"
annotations = json.loads(annotation_path.read_text(encoding="utf-8")) if annotation_path.exists() else {"papers": []}
annotations_by_id = {p["id"]: p for p in annotations["papers"]}

extra = [
    ("L162", "2411.19108", "Timestep Embedding Tells: It’s Time to Cache for Video Diffusion Model", "TeaCache", "2024 / 2025", "Liu et al.", "根据时间步输入变化估计模型输出变化，选择缓存复用以降低视频扩散推理成本。", "无需训练的加速方法；不解决长期状态记忆或因果规则。", "PDF pp.1–3：摘要、引言与缓存方法"),
    ("L163", "2412.17799", "Automating the Search for Artificial Life with Foundation Models", "ASAL", "2024 / 2025", "Kumar et al.", "以视觉语言模型评价模拟结果，搜索目标现象、持续新颖性和多样模拟，覆盖 Lenia、Boids、细胞自动机等基底。", "优化的是基础模型定义的指标与有限模拟；新颖性不等于无限开放演化或真实生命。", "PDF pp.1–2：目标；pp.4–9：搜索与基底；pp.14–17：参考文献"),
    ("L164", "2501.03847", "Diffusion as Shader: 3D-aware Video Diffusion for Versatile Video Generation Control", "Diffusion as Shader", "2025", "Gu et al.", "用 3D 跟踪视频作为统一控制条件，支持相机控制、运动迁移和对象操作。", "几何控制不等于学习或识别因果规律。", "PDF pp.1–4：摘要、问题和方法"),
]
for i, arxiv, title, short, year, authors, summary, boundary, evidence in extra:
    d = next(d for d in manifest["documents"] if any(arxiv in s for s in d["sources"]))
    if d["paper_id"] and any(p["id"] == d["paper_id"] for p in papers):
        aliases[i] = d["paper_id"]
        next(p for p in papers if p["id"] == d["paper_id"])["short"] = short
        continue
    papers.append(dict(id=i, title=title, short=short, year=year, authors=authors, collected=True, note=None, scope="本地已收集 · 本次补入脉络，尚无独立全文笔记", summary=summary, boundary=boundary, evidence=evidence, sources=[s.replace("\\", "/") for s in d["sources"]], sha256=d["sha256"], pages=d["pages"], links=[dict(label="arXiv 原文", url="https://arxiv.org/abs/"+arxiv)], verified=DATE, mappings=[]))
for i, title, short, year, authors, url, summary, boundary, seed, depth, evidence in external_rows:
    if canonical(i) != i:
        continue
    papers.append(dict(id=i, title=title, short=short, year=year, authors=authors, collected=False, note=None, scope="滚雪球新增 · 未收集 PDF", summary=summary, boundary=boundary, evidence=evidence, sources=[], links=[dict(label="论文 / 作者来源", url=url)], verified=DATE, seed=seed, depth=depth, mappings=[]))
known_ids = {p["id"] for p in papers}
for a in annotations["papers"]:
    if a["id"] in known_ids or a.get("collected"):
        continue
    papers.append(dict(id=a["id"], title=a["title"], short=a["title"].split(":")[0], year=a["year"], authors=a["authors"], collected=False, note=None, scope="公开文献记录 · PDF 待收集", summary=a.get("summary", a.get("question", "")), boundary=a.get("boundary", ""), evidence=a.get("evidence", ""), sources=[], links=a.get("links", []), verified=DATE, seed=a.get("discovery", "研究者公开论文记录"), depth=1, discovery_method="context_search" if a["id"].startswith("C") else "author_search", mappings=[]))
by_id = {p["id"]: p for p in papers}
# Editorial additions are separate from collection metadata and survive a rebuild.
overlay_path = SITE / "_tools/rq-map/world-synthesis-overlay.json"
overlay = json.loads(overlay_path.read_text(encoding="utf-8")) if overlay_path.exists() else {}
for addition in overlay.get("branches", []):
    existing = next((b for b in branches if b["id"] == addition["id"]), None)
    if existing is None:
        branches.append(addition)
    else:
        existing.update(addition)
for addition in overlay.get("papers", []):
    by_id[addition["id"]].update(addition)
for node in routes + parents + branches:
    node["anchors"] = list(dict.fromkeys(canonical(i) for i in node["anchors"]))
for b in branches:
    for role in ["core", "support"]:
        b[role] = list(dict.fromkeys(canonical(i) for i in b[role]))
        if role == "support":
            b[role] = [i for i in b[role] if i not in b["core"]]
        for i in b[role]:
            by_id[i]["mappings"].append(dict(rq=b["id"], role=role))
branch_by_id = {b["id"]: b for b in branches}
for p in papers:
    a = annotations_by_id.get(p["id"])
    if not a:
        continue
    p["annotation"] = a
    p["scope"] = {"abstract_review":"本地 PDF · 摘要初读", "method_checked":"本地 PDF · 方法条件已核查", "existing_notes":"本地 PDF · 既有阅读笔记"}.get(a.get("review_status"), p["scope"]) if p["collected"] else p["scope"]
    for rq in a.get("rqs", []):
        if rq not in branch_by_id or any(m["rq"] == rq for m in p["mappings"]):
            continue
        role = a.get("mapping_roles", {}).get(rq, a.get("mapping_role", "support"))
        branch_by_id[rq][role].append(p["id"])
        p["mappings"].append(dict(rq=rq, role=role))

# Verified arrows run from earlier work to the paper that cites it.
# The condition-change interpretation is our synthesis; the citation is independently evidenced.
edges = []
def edge(a, b, change, evidence, kind="citation", url=None):
    a, b = canonical(a), canonical(b)
    if url is None:
        links = by_id[b]["links"]
        url = links[0]["url"] if links else None
    edges.append(dict(id=f"{a}-{b}", source=a, target=b, kind=kind, change=change, evidence=evidence, url=url))

edge("S01", "P121", "低维概率动力学 → 压缩视觉与循环动态；仍须处理模型被策略利用", "P121 PDF pp.9、11、16 对 PILCO 的讨论与引用")
edge("S02", "P121", "控制器/循环世界模型框架 → 可运行的视觉环境实验", "P121 PDF p.2 明确沿用 2015 工作的概念和术语，p.20 参考文献")
edge("P121", "S03", "两阶段模型与演化控制 → 潜空间价值梯度与长程策略学习", "Dreamer §5 Control with latent dynamics 明确对照 World Models", url="https://arxiv.org/html/1912.01603v3#S5")
edge("S05", "S03", "在线潜空间规划 → 学习动作和价值，考虑想象窗口之外的收益", "Dreamer §4 Reconstruction、§5 明确采用并对照 PlaNet", url="https://arxiv.org/html/1912.01603v3#S4")
edge("S03", "P123", "动作有监督的控制学习 → 无动作标签的视频与潜动作；属于相关工作对照", "P123 PDF p.15 引用 Dream to Control；P123 方法的任务变化据其摘要/正文归纳")
edge("S06", "P150", "领域特定的程序理论 → 用 LLM 写通用 Python，并支持探索与转移", "P150 PDF p.2 将[13,17,67]列为更接近的问题设置；p.14 [67]")
edge("S22", "P150", "每步 LLM 推理行动 → LLM 编写环境模型，再用独立规划器复用", "P150 PDF p.2 明确与 ReAct 对照")
edge("P150", "P156", "确定性、单个大程序 → 随机、部分可观测、多个带权程序专家", "P156 PDF p.1 明确指出 WorldCoder [3] 的适用限制；p.11 参考文献")
edge("S04", "P156", "数据密集神经世界模型 → 从少量经验合成局部程序专家", "P156 PDF p.1 对照 Dreamer[1]，p.11 对应 DreamerV3 2023")
edge("P123", "P081", "可控潜动作 → 跨情境共享动作语义与迁移", "P081 PDF §1–2 讨论潜动作泛化；p.10 引用 Genie")
edge("P142", "P157", "元强化学习的隐藏机制任务 → 基础模型跨轮总结与规则突变适应", "P157 PDF p.1、Alchemy 设置；对 Wang 等 Alchemy 的引用")
edge("S12", "P143", "给定对象/机器观察 → 允许主动放置对象、检验假设与更新信念", "P143 PDF pp.2–4 明确写明继承 ACRE 外观与 Blicket 机器")
edge("P002", "P017", "静态最合理解释 → 新信息改变因果关系强弱", "P017 PDF p.3 Table 1 引用 ART/Bhagavatula 2020；是任务对照，不声称直接方法继承")
edge("S13", "P017", "一般可撤销 NLI → 专门研究因果关系的支持与削弱", "P017 PDF p.3 明确区分 Rudinger 2020 与 δ-CAUSAL，p.11 引用")
edge("S13", "P021", "文字可撤销推断 → 反常视频中随观察揭示更新解释", "P021 PDF p.10 参考文献[31]；任务变化据正文归纳")
edge("P011", "P015", "默认/反事实任务比较 → 分离规则归纳和规则执行", "P015 与本地 abductive/conclusion.md 均标明 Wu 等 2023 的反事实设置；详见 P015 正文", kind="synthesis")
edge("S07", "L163", "人工设计/探索连续自动机 → 基础模型引导模拟参数搜索", "ASAL PDF pp.1–2、p.14 明确列出 Lenia 基底")
edge("S08", "L163", "行为新颖性搜索 → 以基础模型表征定义模拟的新颖性与多样性", "ASAL PDF p.16 引用 Lehman & Stanley 2011；非声称原封不动继承算法")
edge("S09", "P145", "记忆与反思的社会角色 → Game Master 维护物理/社会/数字行动后果", "P145 PDF p.8 明确采用 Park et al. 2023 相同的关联记忆结构")
edge("P138", "P128", "逐句故事图像 → 带显式历史记忆的多镜头视频", "P128 PDF p.13 [25] 引用 StoryGAN；任务差异为本图比较")
edge("P039", "P128", "图像故事中的视觉记忆 → 镜头级视频记忆与历史帧选择", "P128 PDF p.14 [37] 引用 Make-a-Story")
edge("S27", "P127", "粗到细长视频扩散 → 分层叙事关键帧与扩散渲染", "P127 PDF p.14 引用 NUWA-XL；比较表示层次，不声称单线技术继承")
edge("S10", "P104", "推理文字链 → 显式动作/预测状态交替与 MCTS 规划", "P104 PDF pp.1–2、p.4 明确比较 CoT")
edge("S11", "P104", "同为多路径搜索；RAP 额外显式建模状态转移", "P104 PDF p.2 写 concurrently：并行相关工作，不是已证实的先后继承", kind="comparison")
edge("S14", "P001", "算法混合专家/新手控制 → 人类自主接管与交还控制", "P001 PDF pp.1–2 对照 DAgger 的随机门控与实时专家局限")
edge("S20", "P041", "理解机器错误边界 → 联合优化机器预测器与向人求助策略", "P041 PDF p.7 引用 Bansal 等 2019；任务与目标变化据正文归纳")
edge("S15", "P059", "识别人的通道可用性 → 同时选择主动帮助内容与交互方式", "P059 PDF p.2 明确指出 Human I/O 未处理主动意图生成，p.18 [41]")
edge("S16", "P059", "预测数字后续动作 → 面对真实情境协调内容、时机和通道", "P059 PDF pp.2–3 明确比较 OmniActions，p.18 [34]")
edge("S23", "P059", "BDI 用户建模 → 聚焦如何低打扰地递送主动帮助", "P059 PDF p.18 [33] 引用 Satori；条件对照据两篇摘要归纳")
edge("S25", "P059", "低负荷的日常知识发现 → 紧迫、社会受限情境中的帮助递送", "P059 §1 明确比较 AiGet", url="https://arxiv.org/html/2509.09255v1#S1")
edge("S18", "S17", "大屏语音/手势指涉 → 可穿戴 AR 的注视、手势、视觉与对话历史", "GazePointAR PDF pp.2–3 明确追溯 Bolt 1980，p.14 [9]", url="https://makeabilitylab.cs.washington.edu/media/publications/Lee_GazepointarAContextAwareMultimodalVoiceAssistantForPronounDisambiguationInWearableAugmentedReality_CHI2024.pdf#page=2")
edge("S17", "P061", "理解人的空间指向 → 智能体也用与语音同步的空间手势表达", "P061 PDF p.3 指出空间交流不对称；p.16 [38]")
edge("S24", "P061", "物体上的查询/操作入口 → 空间手势与动作示范", "P061 PDF p.3 引用 XR-Objects [12] 并讨论输出仍主要靠语言的限制")
edge("S19", "P149", "交互设计原则 → 训练何时澄清的对话动作策略", "P149 PDF p.1、p.13 明确引用 Amershi 等 2019；是设计背景，非算法继承")
edge("P149", "P159", "学习问/答策略 → 显式条件 DAG、裁剪与提问效率目标", "P159 PDF p.11 引用 Learning to Clarify；§1 对既有方法的结构缺失分析")
edge("S21", "P159", "答案及其成立条件 → 主动询问缺失条件并裁剪推理分支", "P159 PDF p.7 数据集设置、p.14 Sun 等 2022 条目")
edge("P055", "P059", "混合主动权与打扰成本 → XR 多模态可用性与主动帮助", "本图按问题框架建立的概念桥；本轮未证实 P059 直接引用 P055", kind="synthesis")
edge("P143", "P157", "合成环境主动实验 → 包含人执行动作的 3D 取证与规则变更", "本图对已实现条件的比较；未将其标成直接引用", kind="synthesis")
edge("P147", "P160", "可运行环境与计划树修改 ↔ 大规模设定与上下文管理", "两者产物不同；由本图并列比较，不是后一篇已经补齐前者能力", kind="comparison")
edge("S26", "P038", "感知错误的游戏交互设计 ↔ 语言不确定表达与依赖", "本地 conclusion.md 并列阅读线索；两篇独立问题，未核实直接引用", kind="comparison")
edge("P002", "P008", "文本前后观察的解释 → 遮蔽视频事件的描述与解释", "P008 PDF pp.1–2 讨论语言溯因任务，p.14 [5] 引用 Bhagavatula 等 2020")
edge("P008", "P030", "VAR 视频编码与解释生成 → 语言假设筛选结合图像想象", "P030 PDF p.2 明确回顾 REASONER/Liang 等 2022；p.5 沿用 VAR 数据")
edge("P002", "P019", "文本溯因 NLI → 比较原因/后果图像并解释选择", "P019 PDF p.1 明确称 inspired by Bhagavatula et al. 2019 的文本 abductive NLI")
edge("P002", "P021", "一般常识解释 → 意外视频事件与证据逐步揭示", "P021 PDF p.2 将 Bhagavatula 等[3]列为语言计算溯因起点")
edge("P138", "P039", "故事级一致性判别 → 视觉记忆中的实体/背景与指代保持", "P039 PDF p.3 Story Generation 明确称 Li 等[30]/StoryGAN 提出初始任务")

# New author collections: attach verified citations and label analytical comparisons.
aid_to_id = {a["arxiv_id"]:a["id"] for a in annotations["papers"] if a.get("arxiv_id")}
new_lanes = []
def team_relation(aid, bid, rq, title, change, evidence, kind="citation"):
    a = aid_to_id.get(aid, aid)
    b = aid_to_id.get(bid, bid)
    if a not in by_id or b not in by_id:
        return
    edge(a,b,change,evidence,kind=kind)
    new_lanes.append(dict(route="world",rq=rq,title=title,papers=[a,b]))

team_relation("2512.24766","2606.04811","W2d","从生成运动到执行检验",
    "以生成视频恢复三维物体流并控制 → 将生成模型作为固定被测对象，独立评价执行成功",
    "Dream.exe PDF p.3 明确讨论 Dream2Flow，并区分本工作的评价定位")
team_relation("2605.13724","2609.02886","W3a","少步视频方法进入长程训练流程",
    "任意步 flow map 蒸馏 → 在多骨干世界模型中用于自回归适配，再进行 DMD",
    "SolarWM PDF p.5 明列 teacher-forced AnyFlow autoregressive initialization")
team_relation("2411.04983","2606.32026","W1d","从冻结潜空间规划到测试时适应",
    "离线学模型、测试时优化动作 → 执行新转移后更新部分模型参数再规划",
    "AdaJEPA PDF p.9 比较 DINO-WM 的 Frozen/Adapt；p.14 明确沿用其 PushT 设置")
team_relation("P158","2606.02564","W4d","规则评测成为测试时监督参照",
    "评估生成视频的规则执行 → 用外部 VLM 生成目标和过程查询并优化视频 LoRA",
    "VLM-as-Teacher PDF pp.2–3 引用 RULER-Bench，p.6 Table II 使用其指标；不声称基准本身提供优化方法")
team_relation("2511.16669","2606.02564","W4d","两种外部推理支持的位置",
    "VLM 先预测下一事件文字 → VLM 对生成过程提供测试时可微监督",
    "资料库对照 VANS PDF pp.4、12 与教师方法 PDF pp.4、6；本轮未核实直接引用",kind="comparison")
team_relation("2607.19343","2608.24101","W1c","实体未来与稀疏轨迹两种动作接口",
    "给定部分实体像素轨迹、预测其余后果 → 联合提出动作和稀疏轨迹，生成并评分多个未来",
    "资料库比较 Masked Visual Actions PDF pp.3–7 与 TrAct pp.3–5；不是已核实的技术继承",kind="comparison")
team_relation("P150","C01","W1b","可执行机制已有直接前作",
    "从交互合成世界程序 → 把任务分数、可回答性和主动探针一起用于局部机制编辑",
    "WorldCoder 既有全文笔记与 ESBM 作者摘要的条件比较；尚未在本轮核查后者引用表",kind="comparison")

lanes = [
    ("world", "W1c", "视觉世界模型：从预测到控制", ["S01", "P121", "S03", "P123", "P081"]),
    ("world", "W1c", "第二轮追溯：Dreamer 的状态表示从哪里来", ["S05", "S03", "P123"]),
    ("world", "W1b", "程序机制：放宽确定性与整体程序假设", ["S06", "P150", "P156"]),
    ("world", "W1d", "主动发现：从已有观察到实验", ["S12", "P143", "P157"]),
    ("world", "W1d", "跨试次学习与规则突变", ["P142", "P157"]),
    ("world", "W2b", "新证据可以推翻什么", ["S13", "P017"]),
    ("world", "W2b", "可撤销推断转向视频", ["S13", "P021"]),
    ("world", "W2b", "从文本解释到视频解释与想象", ["P002", "P008", "P030"]),
    ("world", "W2b", "溯因问题如何变成多图比较", ["P002", "P019"]),
    ("world", "W3b", "长故事：从图像记忆到镜头记忆", ["P138", "P039", "P128"]),
    ("world", "W3b", "长视频的结构分解", ["S27", "P127"]),
    ("world", "W3c", "演化：从规则基底到自动搜索", ["S07", "L163"]),
    ("world", "W3c", "新颖性也是一种搜索目标", ["S08", "L163"]),
    ("world", "W3c", "社会行为与共同世界", ["S09", "P145"]),
    ("world", "W4a", "文字链变为状态规划", ["S10", "P104"]),
    ("xr", "X1a", "第二轮追溯：空间交流从输入走向输出", ["S18", "S17", "P061"]),
    ("xr", "X2b", "主动帮助必须适应人的通道", ["S15", "P059"]),
    ("xr", "X2b", "从预测动作到协调帮助", ["S16", "P059"]),
    ("xr", "X2b", "用户意图与情境递送", ["S23", "P059"]),
    ("xr", "X2a", "澄清：从交互原则到条件结构", ["S19", "P149", "P159"]),
    ("xr", "X2a", "问题来源：答案为何还附带条件", ["S21", "P159"]),
    ("xr", "X2c", "谁决定接管", ["S14", "P001"]),
    ("xr", "X2c", "评价单位变成团队", ["S20", "P041"]),
    ("xr", "X1c", "由实验到人执行的取证", ["S12", "P143", "P157"]),
]
lanes = [dict(route=r, rq=q, title=t, papers=[canonical(i) for i in p]) for r,q,t,p in lanes]
lanes.extend(new_lanes)

bridges = [
    dict(id="B1", title="让人参与机制辨别，而不只是补充事实", question="智能体维护多个隐藏机制假设时，怎样选择一个值得请求人执行的空间取证动作？", rqs=["W1d", "W2b", "X1c", "X2b", "X2c"], papers=["P143", "P157", "P159", "P059", "P041"], known="IVRE 已让智能体主动实验；P157 已让人执行 3D 放置/移动；GPS 已优化提问，但规则已知。", delta="把未知机制、人的行动负担、介入通道和证据收益放到同一个闭环中。", test="比较直接建议、文本澄清、自由取证与成本敏感取证；同时测假设淘汰、任务成功、打扰次数/身体负担、错误介入与修复时间。"),
    dict(id="B2", title="可修正的假设成为 XR 交互对象", question="怎样向人呈现少量有区分度的假设、来源与缺失证据，并让修正改变后续行为？", rqs=["W2b", "X1a", "X3a", "X3b"], papers=["P021", "P038", "P061", "P080", "P091", "P097"], known="新证据修正、空间表达、置信表达和交互解释分别已有工作；可见 CoT 不能直接当成内部真因。", delta="在对象和任务上绑定假设，而不是仅展示一个置信数；明确区分用户确认指涉与用户提供新证据。", test="对照单一解释、概率显示与可编辑假设；测恰当依赖、纠错成本、共享指涉、错误记忆持续与恢复。"),
    dict(id="B3", title="规则编辑后的局部保持与长期后果", question="创作者修改一条规则后，怎样只更新应受影响的状态和事件，并保持其余设定？", rqs=["W1a", "W1b", "W2c", "W3b", "W3d", "X4a"], papers=["P154", "P150", "P156", "P071", "P147", "P160", "P158"], known="代码世界模型、数字孪生干预和创作计划树均已有；AutoWorldBuilder 尚未实现关系解析，DreamGarden 的撤销并非精确依赖分析。", delta="把规则本身当作可版本化、可执行和可验证的编辑对象，检查多步因果后果与不受影响部分。", test="使用有真值规则的可执行小世界；同时测规则满足、编辑局部性、长期一致、不同合法演化和用户修改成本。"),
]
for route in routes:
    route["short_title"] = "世界机制的学习、修订与一致演化" if route["id"] == "world" else "共享理解、主动权与协作修复"
for bridge in bridges:
    bridge["papers"] = list(dict.fromkeys(canonical(p) for p in bridge["papers"]))
    if bridge["id"] == "B3":
        bridge.update(status="deferred", title="规则编辑方向：暂缓拟题", question="先核对相关论文的能力、输入条件与验证范围，再重新界定问题。", known="WorldCoder、PoE-World 和 ESBM 已研究可执行机制及修订；WorldEvolver 的更新发生在部署上下文。当前文献用于对照不同条件。", delta="暂不提出新的 RQ；不将可执行、可修订、可验证本身标为研究空白。", test="先完成论文标注，再确定是否存在值得验证的具体差别。")
        bridge["papers"].extend(i for i in ["C01","C02"] if i in by_id)

family_groups = [dict(ids=["P026", "P103"], reason="Coconut 的不同本地版本"), dict(ids=["P102", "P137"], reason="Long-Context State-Space Video World Models 的不同文件"), dict(ids=["P127", "P134"], reason="MovieDreamer 的不同本地版本"), dict(ids=["P042", "P045"], reason="同一叙事因果研究的后续/早期版本，题名不同")]
for group in family_groups:
    for i in group["ids"]:
        if i in by_id:
            by_id[i]["family"] = group
for p in papers:
    p["aliases"] = [a for a,c in aliases.items() if c == p["id"] and not a.startswith("L")]
    if "seed" in p:
        p["seed"] = canonical(p["seed"])

# Original numbered questions are translated; other questions are identified as paraphrases.
paper_questions = {
    "P061": ("作者明确 RQ 的中文转述", "RQ1：在什么 XR 情境中，文字/语音回应会妨碍空间理解与参与？RQ2：手部具身智能体应具有什么属性，才能协调时机、表现和交互？", "PDF p.4 §3 Formative Study"),
    "P091": ("作者明确 RQ 的中文转述", "RQ1：交互解释能否提高核查准确率？RQ2：怎样影响核查时间和努力？RQ3：用户是否更偏好交互解释？", "PDF p.2 研究问题段落"),
    "P150": ("依作者问题与方法改写", "能否用少量环境交互编写可执行世界模型，并通过乐观约束驱动探索与跨环境迁移？", "PDF pp.1–3 §1、§2.1–2.2"),
    "P156": ("依作者引言问题改写", "怎样表示世界动力学，才能以少量经验学习，又支持随机性、部分可观测性和组合规划？", "PDF p.1 Introduction，p.3 建模假设"),
    "P154": ("依作者任务定义改写", "LLM 能否把自然语言世界描述补全为可执行的 PDDL 模型？", "正文任务定义及基准构建；输入已给谓词/动作签名"),
    "P157": ("依作者引言与实验改写", "基础模型能否主动选取信息、跨试次学习隐藏机制，并适应规则突然改变？", "PDF p.1 Abstract、Introduction；Feature World 与 Alchemy 实验"),
    "P143": ("依作者任务定义改写", "当现有视觉观察不足以确定因果关系时，智能体能否主动实验以减少不确定性？", "PDF pp.2–4 IVRE 的交互任务定义"),
    "P059": ("依作者引言问题改写", "主动 AR 助手应提供什么帮助，又应在何种情境下用什么低干扰方式递送？", "PDF pp.2–3；§4 what/how 双模块"),
    "P041": ("依作者研究目标改写", "能否联合学习预测器和求助策略，让人机整体效用优于各自独立优化？", "PDF p.1 问题与架构，p.7 交互边界"),
    "P159": ("依作者问题定义改写", "条件知识已在文档中时，怎样主动问出缺失条件，并避免无效澄清？", "PDF p.1 Introduction；DAG 推理与动态裁剪"),
    "P149": ("依作者引言改写", "歧义请求出现时，怎样用有限数据让助手学会澄清，而不是猜测或过度罗列？", "PDF pp.1–2 Introduction、Figure 1"),
    "P017": ("依作者任务定义改写", "新信息怎样增强或削弱常识因果关系，怎样评价这种变化？", "PDF p.3 对 δ-NLI 的区分；δ-CAUSAL 与 CESAR"),
    "P021": ("依作者任务定义改写", "面对意外视频事件，模型能否推断隐藏事件，并在新证据揭示时修正解释？", "PDF pp.1–3；Forecaster / Detective / Reporter 设置"),
    "P147": ("依作者引言问题改写", "LLM 游戏开发工具怎样适配创作者工作流，并支持不同程度的自主生成和人工介入？", "PDF p.1 Abstract / Introduction、Figure 1"),
    "P163": ("依作者三个研究目标改写", "基础模型能否帮助搜索目标模拟现象、时间上的新颖性与多样人工生命形态？", "PDF pp.1–2 三类搜索目标；pp.4–9 方法与实验"),
}
for identifier, (kind, question, location) in paper_questions.items():
    if identifier in by_id:
        by_id[identifier]["research_question"] = dict(kind=kind, text=question, location=location)

folder_counts = collections.Counter(s.split("/")[0] for p in papers if p["collected"] for s in p["sources"])
for key, rows in [("routes", routes), ("parents", parents)]:
    for addition in overlay.get(key, []):
        next(row for row in rows if row["id"] == addition["id"]).update(addition)
edges.extend(overlay.get("edges", []))
lanes.extend(overlay.get("lanes", []))
local_files = {s for p in papers if p["collected"] for s in p["sources"]}
actual_files = {str(p.relative_to(ROOT)).replace("\\", "/") for folder in folder_counts for p in (ROOT / folder).rglob("*.pdf")}
assert local_files == actual_files, f"Inventory changed: {local_files ^ actual_files}"
assert len(by_id) == len(papers)
assert all(p["mappings"] for p in papers), [p["id"] for p in papers if not p["mappings"]]
assert all(i in by_id for node in routes + parents + branches for i in node["anchors"])
assert len({e["id"] for e in edges}) == len(edges)
assert all(e["source"] in by_id and e["target"] in by_id for e in edges)
assert all(any(e["source"] == a and e["target"] == b for e in edges) for lane in lanes for a,b in zip(lane["papers"], lane["papers"][1:]))

data = dict(schema_version=1, updated=DATE, routes=routes, parents=parents, branches=branches, papers=papers, edges=edges, lanes=lanes, bridges=bridges, families=family_groups,
    coverage=dict(pdf_files=len(local_files), local_documents=sum(p["collected"] for p in papers), existing_notes=len(records), map_only=len(extra), external_papers=len(external_rows), folders=[dict(name=f, files=n, documents=sum(any(s.startswith(f+"/") for s in p["sources"]) for p in papers if p["collected"])) for f,n in sorted(folder_counts.items())], historical_aliases={"P003":"P002", "P082":"P081", "P109":"P103"}, supplements=[dict(path="abductive/Abductive Reasoning XR Agent.docx", use="用于理解假设呈现、主动取证、修复和人的成本；研究草稿中的空白主张须用论文核查。"),dict(path="abductive/conclusion.md",use="作为 Bubbleu 等外部论文的检索线索；不作为原论文证据。"),dict(path="VideoGeneration/VideoGen × World Model × Storytelling 交叉领域高影响论文深度研究报告.docx",use="对照长视频、叙事、动作控制三支；补查 NUWA-XL，修正‘视觉一致即因果一致’的混同。"),dict(path="Reasoning/Learning_Long-form_Movie_Prior_via_Large_Language_Models.notes.md",use="与 P161 对照，保留稀疏分镜和布局指标的适用边界。")]),
    methodology=["两条核心 RQ、父子层级及‘条件变化’均是本图的研究综合，不声称由某一篇最早提出；每一层列出支撑论文。", "实线箭头表示后者正文/参考文献确实引用前者；箭头上的问题变化是归纳比较，引用本身不等于全部方法继承。虚线表示本图的概念关联或并行对照。", "颜色仅表示是否有本地 PDF：蓝色已收集，橙色未收集。新检索到的论文即使有在线全文也仍是未收集；本次不下载它们的 PDF。", "本地 168 个 PDF 按 SHA-256 对应 161 个不同文件内容；不同版本仍保留各自节点并提示关联，不宣称是 161 项独立研究。", "覆盖九个文献目录及四份辅助材料。原网页方向标签较宽，本图依据论文问题重新分支；通用 AI、统计与创作方法标为支撑，不当作已解决 XR 或世界机制。", "以本地论文及草稿为种子，优先向后追溯作者在引言/相关工作明确定位的问题；核对论文原文、官方记录或作者页面。第二轮实例：Genie→Dreamer→PlaNet，AgentHands→GazePointAR→Put-That-There。", "这是围绕关键问题的滚雪球快照，检索截至 2026-09-17；未穷尽全部参考文献或前向引用。没有证据时保留为综合关联，不伪造继承。", "L162–L164 是此前未入网页笔记的三份本地 PDF，本次只补入有边界的脉络摘要，不冒充已有完整阅读笔记。"])

out = SITE / "_data/literature_rq.json"
data["coverage"]["map_only"] = sum(p["collected"] and not p["note"] for p in papers)
data["coverage"]["historical_aliases"] = {a:c for a,c in aliases.items() if not a.startswith("L")}
archive_manifest = ROOT / "duplicate-paper-archive/2026-09-17/archive-manifest.json"
data["coverage"]["archived_duplicates"] = len(json.loads(archive_manifest.read_text(encoding="utf-8"))["moves"]) if archive_manifest.exists() else 0
data["methodology"][3] = f"按当前目录与 SHA-256 清单核对：{len(local_files)} 个活跃 PDF、{sum(p['collected'] for p in papers)} 个本地文献节点。duplicate-paper-archive 中归档的重复/旧版本不重复计数，历史 ID 保留别名跳转。"
data["methodology"][-1] = "TeaCache、ASAL、Diffusion as Shader 已随本地目录同步成为 P162–P164，使用当前正式笔记；没有把这些已收集文献误标成外部检索项。"
data["coverage"]["external_papers"] = sum(not p["collected"] for p in papers)
data["methodology"][0] = "长期母问题、父子层级及条件变化均为文献组织框架。候选选题与母问题分别呈现；B3 暂缓拟题，先标注文献。"
data["methodology"][2] = "颜色仅表示本地 PDF 是否存在：蓝色已收集，橙色未收集。证据深度与复现状态另用文字标注；在线摘要、下载 PDF、提取全文与方法核查是不同状态。"
data["methodology"][4] = "覆盖现有文献目录及研究者收藏。新增记录注明摘要初读或方法核查；方法支撑不等于已解决对应应用问题。"
data["methodology"][6] = "检索快照更新至 " + DATE + "；作者署名检索与引用滚雪球分别记录。未穷尽全部团队工作或参考文献，没有证据时不建立引用继承边。"
data["methodology"].extend(overlay.get("methodology", []))
out.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"papers":len(papers),"local_documents":data["coverage"]["local_documents"],"external":data["coverage"]["external_papers"],"branches":len(branches),"edges":len(edges),"folders":len(folder_counts)}, ensure_ascii=False))
