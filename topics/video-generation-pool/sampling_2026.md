# 2026 年集中扩样：新增 120 篇

核验截止：2026-10-14。原池 75 篇，新增 120 篇，合计 195 篇；其中 arXiv 首发年为 2026 的共有 140 篇。

## 纳入与抽样口径

- 年份严格按已打开的 arXiv 摘要页首发日期筛选为 2026，最早 2026-01-01，最晚 2026-09-30；会议年另列。arXiv ID 月份与提交日期可能跨月，不用 ID 推定准确月份。
- 刷新三个指定 GitHub README 和 CVPR / ICLR / NeurIPS 2026 官方目录，保留快照哈希；排除原池 arXiv ID，并按规范化标题二次查重。
- 这是按来源分层、按主题覆盖作目的性选择的扩样，不是随机样本。选择时兼顾控制、编辑、事件状态、长时记忆、交互、RL、蒸馏、数据和评测；数量不能用来推断全领域占比。
- 主来源配额最终为 Post-Training 44、Interactive World Model 44、会议录用来源 32。会议层先交叉核对清单条目，再从官方目录补充事件和编辑论文；32 篇中28篇也出现于指定 GitHub 清单，4篇由 CVPR 官方目录独立发现。每篇只计一个主来源，全部已核实来源另列。
- Controllable 的2026首发层仅2篇，均已在原75篇，因此新增0；不将其他清单论文伪记为此来源。ICCV 无2026届次。
- 会议层为 CVPR 15、NeurIPS 16、ICLR 1。严格首发年限制下本轮未强制会议均衡，不能把 ICLR 数量少解释为该会缺乏相关工作。
- 新增120篇均实际打开并阅读摘要，保存摘要URL、打开时间、页面SHA-256和中文阅读短记；32篇会议主来源另打开官方摘要核对标题及内容。其余 venue 中14篇仅有 arXiv 作者声明，明确标注，未当作官方录用证据。
- 保留4篇相邻方向并显式提示边界：P098（3D音视频场景）、P103（无推理时视频的WAM）、P161（vector-graph rollout）、P182（latent后果验证）。它们不应在后续标注中被默认当成RGB视频方法。

## 来源统计

| 来源 | 主抽样篇数（互斥） | 全部来源命中（可重叠） |
|---|---:|---:|
| controllable | 0 | 0 |
| posttraining | 44 | 66 |
| worldmodel | 44 | 53 |
| CVPR2026 | 15 | 15 |
| ICLR2026 | 1 | 1 |
| NeurIPS2026 | 16 | 16 |

来源链接：[Controllable](https://github.com/mayuelala/Awesome-Controllable-Video-Generation)、[Post-Training](https://github.com/people-robots/Awesome-Video-Generation-Post-Training)、[Interactive World Model](https://github.com/liujiuming123/Awesome-Interactive-World-Model)、[CVPR 2026](https://openaccess.thecvf.com/CVPR2026?day=all)、[ICLR 2026](https://proceedings.iclr.cc/paper_files/paper/2026)、[NeurIPS 2026](https://neurips.cc/virtual/2026/papers.html)。

## 标注与综合状态

本轮完成论文池扩样。新增120篇为“摘要已核验；待全文标注”，六轴、证据类型、user study样本量、必须保持的内容等仍待全文核验，不根据摘要硬填。中文短记为摘要概述；检索主题带[推断]，不等同于正式taxonomy标注。

原有75篇全文片段标注、矩阵、57个空格/稀疏格分析、15题邻居保持为原始cohort的结果。旧综合中的“在本论文池内未见”仅指原75篇，不能延伸到195篇。尤其新增ActWorld、CreFlow、MechVerse、TIE等可能改变邻近工作定位，需要完成全文标注后重算；本轮不提前宣称研究缺口。

## 可复核文件

- `papers.csv`：195篇总表，含cohort与annotation_status。
- `papers_2026_additions.csv`：新增120篇。
- `papers_annotated75.csv`：原始75篇完整标注快照。
- `provenance_2026.csv`：新增论文逐来源位置。
- `abstract_manifest_2026.json`：120篇摘要打开与页面哈希记录。
- `source_manifest_2026.json`、`sampling_strata_2026.csv`：来源快照和分层口径。

全文和摘要原始页面快照仅在本地留作复核，不随网站发布。
