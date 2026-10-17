"""Render the unified catalog and matrix from reviewed public JSON."""
import html,json,re,csv
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'video-generation-pool'
DATA=json.loads((ROOT/'data/technical-annotations.json').read_text(encoding='utf-8'))
P=DATA['records']; H=lambda v:html.escape(str(v)); index={r['key']:r for r in P}
def val(v):return ' / '.join(map(str,v)) if isinstance(v,list) else str(v or '无')
def field(k,v):return '<div><b>'+H(k)+'</b><span>'+H(val(v))+'</span></div>'
def paperlink(r):return f'<a href="#{r["id"]}">{H(r["title"])}</a>'
def card(r):
    t=r['taxonomy'];f=r['technical']
    tags=[('任务',t['task']),('主贡献',t['contribution_primary']),('次贡献',t['contribution_secondary']),('控制信号',t['control_signals']),('目标性质',t['target_properties']),('生成范式',t['generation_paradigm']),('论文类型',t['paper_type'])]
    technical=[('Model',f['model']),('Backbone',f['backbone']),('生成方式',f['mechanism']),('Condition 标签 [推断]',f['condition_tags']),('条件内容与来源',f['conditions_detail']),('本论文训练／适应数据',f['training_datasets'])]
    details=[('任务输入',t['task_input']),('任务输出',t['task_output']),('必须保持',t['task_invariants']),('判断对错',t['correctness_criteria']),('证据类型',t['evidence_types']),('user study 样本量／说明',t['user_study_sample']),('一句话推进',t['one_sentence_advance']),('训练信号，具体做什么',f['training_signal_plain']),('条件注入，具体怎么接入',f['conditioning_plain']),('辅助模型',f['auxiliary_models']),('底座预训练数据',f['pretraining_datasets']),('评测数据／协议',f['evaluation_datasets']),('不确定性',t.get('uncertainty','')),('原文定位',r['evidence']['locator']),('阅读范围',r['evidence']['scope'])]
    search_text=' '.join([r['title'],r['id'],*r['directions'],json.dumps(t,ensure_ascii=False),json.dumps(f,ensure_ascii=False)])
    # Search normalization must not create lowercased copies of case-sensitive paper URLs.
    search=H(re.sub(r'https?://[^\s"]+','',search_text).lower())
    return f'<article class="catalog-paper" id="{r["id"]}" data-key="{r["key"]}" data-task="{H(t["task"])}" data-primary="{H(t["contribution_primary"])}" data-contributions="{H(val([t["contribution_primary"]]+t["contribution_secondary"]))}" data-directions="{H(val(r["directions"]))}" data-search="{search}"><p class="meta">{H(r["id"])} · {H(r["year"])} · {H(r["venue"])} · {H(val(r["directions"])) if r["directions"] else ""}</p><h3><a href="{H(r["source_url"])}">{H(r["title"])}</a></h3><div class="tax-tags">'+''.join('<span><b>'+H(k)+'</b> '+H(val(v))+'</span>' for k,v in tags)+'</div><p class="concrete"><b>主贡献，具体做什么：</b>'+H(f['contribution_plain'])+'</p><div class="facts">'+''.join(field(k,v) for k,v in technical)+'</div><details><summary>任务定义、完整数据与原文依据</summary><div class="facts">'+''.join(field(k,v) for k,v in details)+'</div><p>'+H(t.get('classification_basis','[推断] 分类映射'))+f'</p><a href="{H(r["evidence"]["url"])}">原文依据 ↗</a> · arXiv {H(r["arxiv_id"] or "未核实／无")}</details></article>'
eligible=[r for r in P if r['taxonomy']['task'] in DATA['tasks'] and r['taxonomy']['contribution_primary'] in DATA['contributions']]
uncertain=len(P)-len(eligible);video=sum(r['taxonomy']['task']!='其他（说明）' for r in eligible)
matrix=[];md=['# 任务 × 贡献落点','',f'共 {len(P)} 篇去重记录；{len(eligible)} 篇任务与主贡献已可映射，其中视频任务 {video} 篇、其他邻近任务 {len(eligible)-video} 篇；{uncertain} 篇不确定，单列而不强行归格。分类为 [推断]。','', '每格为 主 / 共现。主：主贡献计一次；共现：主或次贡献出现即计一次，同篇同格去重。共现格之间不互斥。','']
md+=['|任务|'+'|'.join(DATA['contributions'])+'|','|---|'+'---|'*len(DATA['contributions'])]
for task in DATA['tasks']:
    cells=[];mdcells=[]
    for contribution in DATA['contributions']:
        primary=[r for r in eligible if r['taxonomy']['task']==task and r['taxonomy']['contribution_primary']==contribution]
        co=[r for r in eligible if r['taxonomy']['task']==task and contribution in [r['taxonomy']['contribution_primary']]+r['taxonomy']['contribution_secondary']]
        reps=sorted(co,key=lambda r:(r not in primary,not bool(r['directions']),-int(str(r['year'])) if str(r['year']).isdigit() else 0))[:3]
        cells.append(f'<td><button class="matrix-filter" data-task="{H(task)}" data-contribution="{H(contribution)}">{len(primary)} / {len(co)}</button>'+''.join('<small>'+paperlink(r)+'</small>' for r in reps)+'</td>')
        mdcells.append(f'{len(primary)} / {len(co)}'+('；'+'；'.join(r['title'] for r in reps) if reps else ''))
    matrix.append('<tr><th>'+H(task)+'</th>'+''.join(cells)+'</tr>');md.append('|'+task+'|'+'|'.join(mdcells)+'|')
(OUT/'matrix.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
qhtml=[]
for q in DATA['questions']:
    neighbors=''.join('<li>'+paperlink(index[n['key']])+'<p>'+H(n['reason'])+'</p><div class="neighbor-facts">'+field('Backbone',index[n['key']]['technical']['backbone'])+field('Condition',index[n['key']]['technical']['conditions_detail'])+field('训练数据',index[n['key']]['technical']['training_datasets'])+'</div></li>' for n in q['neighbors'])
    qhtml.append(f'<article class="question" id="q{q["id"]}"><h3>{q["id"]}. {H(q["title"])}</h3><p class="meta">[推断] 主格：{H(q["task_label"])} × {H(q["contribution_label"])}</p><p>{H(q["contract"])}</p><ol>{neighbors}</ol><p class="concrete">{H(q["updated_boundary"])}</p><details><summary>可检验的研究设计</summary><p>{H(q["experiment"])}</p><p>{H(q["role"])}</p></details></article>')
(OUT/'research_mapping.json').write_text(json.dumps(DATA['questions'],ensure_ascii=False,indent=2),encoding='utf-8')
taxonomyfile=OUT/'taxonomy-fragment.html'
if not taxonomyfile.exists():
    old=(OUT/'index.html').read_text(encoding='utf-8');match=re.search(r'<section id="view-taxonomy"[^>]*>(.*?)</section>',old,re.S)
    if not match:raise RuntimeError('Existing taxonomy section missing; refusing to replace schema')
    fragment=re.sub(r'<p class="scope-note".*?</p>','',match.group(1),flags=re.S)
    fragment=re.sub(r'<p[^>]*>[^<]*<b>统计范围：原始75篇。</b>.*?</p>','',fragment,flags=re.S)
    taxonomyfile.write_text(fragment,encoding='utf-8')
taxonomy=taxonomyfile.read_text(encoding='utf-8')
taxonomy=taxonomy.replace('当前15篇优先标少步/实时，其中多数还同时是AR；10篇因reward/benchmark或跨生成器而范式不确定。','原始标注中有15篇优先标少步/实时，其中多数还同时是AR；另10篇因reward/benchmark或跨生成器而范式不确定。此次增加具体生成方式，原标签保留。')
taxonomy=taxonomy.replace('0个其他不说明目标轴完备。','“其他”现在包含邻近的图像、语言、agent 等任务；不确定仍然单列，不能用“其他”代替未核实。')
taxonomy=taxonomy.replace('本池按来源目的抽样，Post-Training配额天然提高训练信号占比。24篇训练信号主贡献是池内分布，不是领域份额；3D、长叙事各只有3个确定样本，任何空格论证都应先扩池再下结论。','本池按研究方向和来源选择，当前 XR／AIGC 邻近工作的加入改变了分母。统计见更新后的任务 × 贡献矩阵；不能把池内分布解释为领域份额。')
taxonomy=taxonomy.replace('矩阵只统计主贡献，每篇恰好计一次；次贡献另存，可用于理解相邻工作。','矩阵同时报告主贡献和共现：主贡献计一次，共现纳入主、次贡献且同篇同格去重。')
extension='''<h3>在原 taxonomy 上增加的技术字段</h3><p>原六条分类轴和任务定义、证据、推进点全部保留。Backbone 描述网络结构；生成方式描述 diffusion／flow／GAN／程序渲染等过程及整段／逐帧／逐块顺序，不能把 DiT 与 autoregressive 当成互斥标签。</p><p>Condition 细分 text、image、video、pose、audio、object、scene、mask、camera、trajectory、action、identity 等，同时说明条件由用户提供、内部估计还是只用于训练。细标签是 [推断] 的归一化，原控制信号分类保持原样。</p><p>数据分为本论文训练／微调／测试时适应、底座预训练、评测三栏。“无新增训练”“非生成论文不适用”“原文明确未公开”“本轮待核”分别表达，不能互换。主贡献使用具体操作说明；原贡献大类不删改。</p>'''
page='''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Video Generation · 任务、论文与研究题</title><link rel="stylesheet" href="catalog.css"></head><body><header><p class="eyebrow">VIDEO GENERATION · XR / AIGC</p><h1>从任务找到论文，再看它具体改了什么</h1><p>原 taxonomy 保留，模型、条件和数据直接列在题目下方。</p><p class="meta">更新于 2026-10-15 · <a href="../">返回 Topics</a> · <a href="papers.csv">原论文池 CSV</a> · <a href="papers_all_topics.csv">全部论文 CSV</a> · <a href="../data/technical-annotations.json">全部技术字段 JSON</a></p></header><nav><button data-panel="catalog">论文与题目</button><button data-panel="matrix">任务 × 贡献共现</button><button data-panel="questions">15 个研究题</button><button data-panel="taxonomy">Taxonomy 与边界</button></nav><main>'''
page+='<section id="view-catalog"><div class="toolbar"><label>搜索题目、model、condition、dataset<input id="query" type="search" placeholder="例如 DiT、pose、Ego4D、VOID"></label><label>任务<select id="task"><option value="">全部</option>'+''.join(f'<option>{H(t)}</option>' for t in DATA['tasks'])+'</select></label><label>贡献<select id="contribution"><option value="">全部主／次贡献</option>'+''.join(f'<option>{H(t)}</option>' for t in DATA['contributions'])+'</select></label><label>方向<select id="direction"><option value="">全部</option>'+''.join(f'<option>{H(t)}</option>' for t in sorted({d for r in P for d in r['directions']}))+'</select></label><button id="reset">重置</button></div><p id="count" aria-live="polite"></p><div id="catalog">'+''.join(card(r) for r in sorted(P,key=lambda r:(not bool(r['directions']),r['id'])))+'</div><div class="pagination"><button id="prev">上一页</button><span id="page-status"></span><button id="next">下一页</button></div></section>'
page+=f'<section id="view-matrix" hidden><h2>任务 × 贡献落点：主贡献与共现</h2><p>{len(P)} 篇去重记录中，{len(eligible)} 篇的任务与主贡献可映射：视频任务 {video} 篇，其他邻近任务 {len(eligible)-video} 篇；另 {uncertain} 篇不确定。<b>这不是领域论文占比，也不是完整会议普查。</b></p><p>每格 <b>主贡献数 / 共现数</b>。共现包含主、次贡献，同篇同格只计一次；点击数字筛选该格，最多列 3 篇代表。分类映射均为 [推断]。未知次贡献可能使共现数偏低。</p><div class="tablewrap"><table><thead><tr><th>任务</th>'+''.join('<th>'+H(c)+'</th>' for c in DATA['contributions'])+'</tr></thead><tbody>'+''.join(matrix)+'</tbody></table></div><p>空格仅表示在本论文池当前已分类部分未见；未分类条目与抽样偏差均可能改变它，不能据此判断“没人做”“不值得做”。其他任务包括图像生成、澄清、代码 agent、导航与因果分析；它们保留为可迁移邻近工作，不混入视频任务的分母。</p><p><a href="matrix.md">下载矩阵</a></p></section>'
summaries=[]
for item in DATA.get('task_summaries',[]):
    task=item['task'];task=task.replace('3D/4D一致','3D/4D 一致');group=[r for r in eligible if r['taxonomy']['task']==task]
    if not group:continue
    text=item['text'];definition=text.split('本池落点：')[0];issue=text.split('核心未解问题：')[-1].split('依据：')[0] if '核心未解问题：' in text else ''
    if task=='编辑与修改':issue='VOID 已验证删除后的互动重生成，GIVE 已把几何状态转移用于编辑，PermaVid 已有记忆更新。可继续检验未知影响范围、新机制、延迟后果和独立 Keep 指标，不能把这些已有能力说成空白。'
    contributions=Counter(r['taxonomy']['contribution_primary'] for r in group)
    ev=Counter(e for r in group for e in set(r['taxonomy']['evidence_types']) if e in ['定量 benchmark','消融','user study','仅定性展示','定性展示'])
    summaries.append('<article class="panel"><h3>'+H(task)+f' · {len(group)} 篇</h3><p>'+H(definition)+'</p><p>[推断] 当前池内主贡献：'+H('；'.join(f'{k} {v}' for k,v in contributions.most_common()))+'。</p><p>已明确记录的证据（可重叠）：'+H('；'.join(f'{k} {v}' for k,v in ev.items()) or '暂不足以汇总')+'；未核实证据不计，不能把缺字段当作没有实验。</p><p>[推断] 核心问题：'+H(issue)+'</p></article>')
sparse=[]
old_sparse={(x['task'].replace('3D/4D一致','3D/4D 一致'),x['contribution']):x for x in DATA.get('sparse_cell_interpretations',[])}
for task in DATA['tasks']:
    for c in DATA['contributions']:
        primary=[r for r in eligible if r['taxonomy']['task']==task and r['taxonomy']['contribution_primary']==c]
        co=[r for r in eligible if r['taxonomy']['task']==task and c in [r['taxonomy']['contribution_primary']]+r['taxonomy']['contribution_secondary']]
        if len(primary)>1:continue
        old=old_sparse.get((task,c),{});reason=old.get('verdict','[推断] 当前池的选择性覆盖不足以判断不可做或不值得做；需要针对该任务契约检索和可行性实验。')
        if co:reason='[推断] 至少已有 '+str(len(co))+' 篇在主／次贡献中涉及，主格稀疏不能解释为没人做。 '+reason
        else:reason='[推断] 在本论文池已分类部分未见；'+reason.replace('[推断] ','')
        sparse.append('<tr><td>'+H(task)+' × '+H(c)+'</td><td>'+str(len(primary))+' / '+str(len(co))+'</td><td>'+H(reason)+(' <br>'+ '；'.join(paperlink(r) for r in co[:2]) if co else '')+'</td></tr>')
page=page.replace('<p><a href="matrix.md">下载矩阵</a></p></section>','<p><a href="matrix.md">下载矩阵</a></p><h2>按任务阅读</h2>'+''.join(summaries)+'<details><summary>空格与稀疏格：能支持什么判断</summary><p>以下为主贡献数 ≤1 的格；使用共现数交叉检查。判断是池内解释，不是全领域新颖性结论。</p><div class="tablewrap"><table><thead><tr><th>任务 × 贡献</th><th>主 / 共现</th><th>判断与依据</th></tr></thead><tbody>'+''.join(sparse)+'</tbody></table></div></details></section>')
page+='<section id="view-questions" hidden><h2>15 个研究题及最近的三篇邻居</h2><p>[推断] 按任务契约与方法机制选邻居；跨图像、语言、导航工作的迁移边界单列。广义优化题的主格是默认落点，需随具体视频任务调整。</p>'+''.join(qhtml)+'</section>'
page+='<section id="view-taxonomy" hidden>'+taxonomy+extension+'</section></main><script src="catalog.js"></script></body></html>'
(OUT/'index.html').write_text(page,encoding='utf-8')
with (OUT/'papers_all_topics.csv').open('w',encoding='utf-8-sig',newline='') as f:
    fields=list(dict.fromkeys(['id','title','year','venue','arxiv_id','directions']+list(P[0]['taxonomy'])+list(P[0]['technical'])+['source_url']))
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader()
    for r in P:
        row={**r,**r['taxonomy'],**r['technical']};w.writerow({k:json.dumps(v,ensure_ascii=False) if isinstance(v,(list,dict)) else v for k,v in row.items() if k in fields})
print(f'Rendered {len(P)} papers; {len(eligible)} classified; {uncertain} uncertain; {len(DATA["questions"])} questions')
import runpy
runpy.run_path(str(ROOT/'scripts/integrate-resources.py'))
