"""Render the report from its JSON. Usage: python render-lineage.py [output-directory]."""
import csv, html, json, sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
ROOT=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(__file__).resolve().parents[1]/'problem-lineage'
DATA=json.loads((ROOT/'problem-lineage-research.json').read_text(encoding='utf-8'))
PAPERS=DATA['papers']; DIRS=DATA['directions']; LINEAGES=DATA['lineages']; NOTES=DATA['notes']
MERGES=DATA['merges']; CONTROL_MAP=DATA['control_map']; APPLICATIONS=DATA['applications']; SEARCH=DATA['search_log']; TAXONOMY_SCHEMA=DATA['taxonomy_schema']
UPDATE=DATA['recent_evidence']
import lineage_reading as reading
import direction_analysis as direction_analysis
reading.catalog=UPDATE['papers']; reading.routes=UPDATE['directions']
UPDATE_CSS=reading.CSS
def render_reading_panel(code): return reading.panel(code,report=True)
render_recent_catalog=reading.render_recent_catalog
H=html.escape
def ref(keys):
    if isinstance(keys,str):keys=keys.split()
    return ' <span class="refs">'+ ' · '.join(f'<a href="#paper-{k}">{H(k)}</a>' for k in keys)+'</span>'
def p(text,keys=None,label='推断'):
    return '<p><span class="tag '+ ('paper' if label=='论文' else 'pending' if label=='待核' else 'infer')+'">['+label+']</span> '+H(text)+(ref(keys) if keys else '')+'</p>'
def table(headers,rows):
    return '<div class="scroll"><table><thead><tr>'+''.join('<th>'+H(x)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+x+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>'
def origin_badge(a):
    label,style={'库内主表':('库内','library'),'既有补充参考':('既有补充','supplement'),'本次库外新找到':('库外','external')}[a['origin']]
    return f'<span class="origin-tag origin-{style}" title="{H(a["origin_detail"])}">{label}</span>'

def facet(label,value,note=''):
    return '<div class="facet"><span class="facet-label">'+H(label)+'</span><span>'+H(value)+'</span>'+('<small>'+H(note)+'</small>' if note else '')+'</div>'

def taxonomy_cells(a):
    t=a['taxonomy']
    task=t['task']+('（'+t['task_note']+'）' if t['task_note'] else '')
    secondary='次：'+' / '.join(t['contribution_secondary']) if t['contribution_secondary'] else ''
    return [
        facet('任务',task)+facet('论文类型',t['paper_type']),
        facet('贡献落点','主：'+t['contribution_primary'],secondary)+facet('具体落点',t['contribution_focus'])+facet('生成范式',t['generation_paradigm'],t['paradigm_note']),
        facet('控制信号',' / '.join(t['control_signals']) or '无')+facet('目标性质',' / '.join(t['target_properties']) or '不适用',t['property_note'])
    ]

def bibrow(k,foundation=False):
    a=PAPERS[k]
    return ['[推断] '+('奠基代表' if foundation else '近期进展／近邻')+'<div>'+origin_badge(a)+'</div>',f'<a href="#paper-{k}"><b>{H(a["title"])}</b></a><small>[论文] '+H('; '.join(a['authors']))+'</small>',
            '[论文] '+H(str(a['year'])+' · '+a['venue'])+f'<small>首版 {a["first_year"]}；<a href="{H(a["venue_source"])}">venue 依据</a></small>']+taxonomy_cells(a)

css='''*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:125px}body{margin:0;background:#f4f7f6;color:#203b35;font:16px/1.75 system-ui,-apple-system,"PingFang SC",sans-serif}header,main{max-width:1240px;margin:auto;padding:28px}header{padding-bottom:10px}h1{font-size:32px;line-height:1.35}h2{font-size:25px}h3{font-size:20px}h4{font-size:17px}a{color:#126c5a;overflow-wrap:anywhere}nav{position:sticky;top:0;z-index:4;background:#f4f7f6f5;backdrop-filter:blur(8px);border-bottom:1px solid #d6e3db;padding:10px 22px;display:flex;justify-content:center;gap:9px;flex-wrap:wrap}nav a{padding:2px 10px;border:1px solid #b5ccc0;border-radius:18px;text-decoration:none;font-size:14px}.card{background:white;border:1px solid #d7e4db;border-radius:13px;margin:0 0 24px;padding:26px}.tag{font-size:12px;white-space:nowrap;border-radius:4px;padding:2px 5px}.paper{background:#ddf0e3;color:#24573c}.infer{background:#fff0c7;color:#6e4f17}.pending{background:#e9edf4;color:#58627b}.badge{display:inline-block;background:#176850;color:white;border-radius:18px;padding:4px 13px;font-size:13px}.lead,.note{padding:14px 18px;background:#eef5f0;border-radius:6px}.warn{padding:14px 18px;background:#fff5df;border-radius:6px}small{display:block;color:#60796e;font-size:12px;margin-top:5px}.refs{font-size:13px;white-space:normal}details{border:1px solid #dce6e0;border-radius:8px;padding:14px;margin:15px 0}summary{cursor:pointer;font-weight:600}details[open]>summary{margin-bottom:12px}.scroll{overflow:auto}table{border-collapse:collapse;width:100%;font-size:14px}th,td{vertical-align:top;text-align:left;border-bottom:1px solid #dce6e0;padding:11px}th{background:#f1f6f2}td{min-width:105px}td:nth-child(2){min-width:240px}button,input,select{font:inherit;padding:9px 13px;border:1px solid #a9c5b7;border-radius:6px;background:white;color:#203b35}button{cursor:pointer}input{width:min(100%,550px)}.toolbar{display:flex;flex-wrap:wrap;gap:9px;margin:12px 0}.paper-card:target{outline:3px solid #65a087}.paper-card h3{margin-top:0}.meta{font-size:14px;color:#587164}.stat{display:inline-block;margin:5px 18px 5px 0;font-weight:600}footer{padding:20px;color:#587164}.experiment{border-left:4px solid #4e8d70;padding-left:18px}.kicker{font-size:13px;letter-spacing:.05em;color:#6a8178}.claim{margin:10px 0}.claim b{color:#264c3d}dt{font-weight:bold;margin-top:15px}dd{margin:4px 0 0}.hidden{display:none!important}@media(max-width:700px){header,main{padding:15px}.card{padding:17px}h1{font-size:25px}h2{font-size:21px}nav{gap:5px;padding:8px}nav a{font-size:12px}table{min-width:720px}}@media print{nav,.toolbar,.no-print{display:none}body{background:white;font-size:10pt}.card{border:0;padding:0;break-inside:auto}details{break-inside:auto}a{color:inherit;text-decoration:none}header,main{padding:0}h2,h3,summary{break-after:avoid}.scroll{overflow:visible}table{font-size:8pt}td{min-width:0!important}small{font-size:8pt}.refs{font-size:8pt}}'''
css+='''.origin-tag{display:inline-block;margin-top:7px;padding:1px 7px;border-radius:4px;font-size:11px;line-height:1.7;white-space:nowrap}.origin-library{background:#e1f1e6;color:#24603c}.origin-supplement{background:#e7edf9;color:#355789}.origin-external{background:#f0e6f7;color:#72458b}.facet{margin-bottom:10px;overflow-wrap:anywhere}.facet:last-child{margin-bottom:0}.facet-label{display:block;font-size:12px;font-weight:650;color:#637c71;margin-bottom:2px}.facet small{line-height:1.6}.taxonomy-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:18px;padding:18px;background:#f3f7f4;border-radius:8px;margin:14px 0}.taxonomy-grid>div{min-width:0}.task-definition{display:grid;grid-template-columns:150px minmax(0,1fr);gap:10px 16px}.task-definition dt,.task-definition dd{margin:0}.paper-summary{border-left:3px solid #8bb59f;padding:2px 0 2px 16px;margin:20px 0}.source-details{font-size:13px;background:#f8faf9}.source-details summary{font-weight:400}.lineage-table table{min-width:1120px;table-layout:fixed}.lineage-table th:nth-child(1){width:9%}.lineage-table th:nth-child(2){width:24%}.lineage-table th:nth-child(3){width:13%}.lineage-table th:nth-child(4){width:15%}.lineage-table th:nth-child(5){width:23%}.lineage-table th:nth-child(6){width:16%}.lineage-table td{min-width:0}@media(max-width:700px){.taxonomy-grid{grid-template-columns:1fr}.task-definition{grid-template-columns:1fr;gap:4px}.task-definition dd{margin-bottom:12px}}@media print{.lineage-table table{min-width:0}.taxonomy-grid{grid-template-columns:repeat(3,minmax(0,1fr))}}'''
parts=['<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+H(DATA['title'])+'</title><style>'+css+UPDATE_CSS+'</style></head><body>']
parts.append('<header><span class="badge">Topics · 问题谱系与阅读更新</span><h1>'+H(DATA['title'])+'</h1><p>2026-10-16 更新：8 个方向的问题演进、早期代表作、里程碑与最近邻技术局限；原全文阅读日期单列。</p><div class="lead">'+p('8 个名称不等于 8 个独立问题。较清晰的结构是两组共享方法问题、一组具有包含关系的信息获取问题，加上教学持续改进和观众信息控制两个有条件的扩展。', ['PERMA','CINE','SUSP'])+'</div></header>')
parts.append('<p class="lead"><a href="https://soniasuns.github.io/topics/">返回 Topics</a> · <a href="#recent-reading">近期补充阅读与发表状态</a></p>')
parts.append('<nav>'+''.join(f'<a href="#{d["code"]}">{d["code"]}</a>' for d in DIRS)+'<a href="#papers">38 篇拆解</a><a href="#merges">合并判断</a><a href="#control">控制机制</a><a href="#apps">应用</a><a href="#audit">核查账本</a></nav><main>')
parts.append('<section class="card" id="reading"><h2>读法与核实范围</h2>')
for note in NOTES:parts.append(p(note.split('] ',1)[1],label=note[1:note.index(']')]))
counts={x:sum(a['origin']==x for a in PAPERS.values()) for x in ['库内主表','既有补充参考','本次库外新找到']}
parts.append('<p>'+''.join(f'<span class="stat">{H(k)} {v} 篇</span>' for k,v in counts.items())+'</p>')
parts.append('<p><a href="problem-lineage-research.json">下载结构化 JSON</a> · <a href="paper-index.csv">论文索引 CSV</a></p>')
parts.append(table(['编号','名称','一句话定义'],[[f'<a href="#{d["code"]}">{d["code"]}</a>',H(d['name']),'[推断] '+H(d['definition'])] for d in DIRS]))
parts.append(p('所有方向定义是研究工作定义，沿用当前 topics 页面的问题范围；不是论文本身提出了这 8 个名称。最近论文的原文链接与版本见各卡。'))
parts.append('<details id="taxonomy-guide"><summary>任务分类读法 · 六个维度</summary>')
for label,key in [('任务（主轴，单选）','tasks'),('贡献落点（主落点 1 个，次落点可多选）','contributions'),('控制信号（多选，没有则无）','control_signals'),('目标性质（多选）','target_properties'),('生成范式（单选）','generation_paradigms'),('论文类型（单选）','paper_types')]:
    parts.append('<p><b>'+label+'：</b>'+H(' / '.join(TAXONOMY_SCHEMA[key]))+'</p>')
for note in TAXONOMY_SCHEMA['notes']:parts.append(p(note.replace('分类均为[推断]：','分类规则：')))
parts.append('</details>')
parts.append('</section>')
for d in DIRS:
    parts.append(f'<section class="card" id="{d["code"]}"><div class="kicker">{d["code"]} · 两步研究结果</div><h2>{H(d["name"])}</h2>'+p(d['definition']))
    parts.append(direction_analysis.panel(d['code']))
    parts.append(render_reading_panel(d['code']))
    parts.append('<h3>第一步 · 它最接近谁</h3>')
    for lid in d['lineages']:
        l=LINEAGES[lid]
        parts.append('<details><summary>'+lid+' · '+H(l['name'])+f'（{len(l["papers"])} 篇）</summary>'+p(l['relation'],l['papers'])+p(l['distance'],l['papers']))
        if l.get('missing'):parts.append('<div class="warn">'+p(l['missing'],label='待核')+'</div>')
        parts.append('<p class="meta">[推断] 后三列为按原文整理的任务分类；点击标题查看任务定义、证据与推进。</p><div class="lineage-table">'+table(['谱系位置','标题／完整作者','年份／venue','任务／论文类型','贡献落点／生成范式','控制信号／目标性质'],[bibrow(k,i==0) for i,k in enumerate(l['papers'])])+'</div>')
        parts.append('</details>')
    parts.append('<h3>第二步 · 综合与可证伪实验</h3>')
    for field,label in [('history','原始问题与演变'),('boundary','前沿证据边界'),('core','候选核心问题'),('why','为什么不是仅加数据／算力')]:
        parts.append('<h4>'+label+'</h4>'+p(d[field],d['sources']))
    parts.append('<div class="experiment"><h4>实验提案 · 尚未执行</h4>')
    for field,label in [('case','案例'),('operation','操作／自变量'),('controls','对照'),('metrics','指标'),('falsifier','可推翻结果')]:parts.append('<p><b>'+label+'：</b><span class="tag infer">[推断]</span> '+H(d['experiment'][field])+'</p>')
    parts.append('</div><h4>已有工作与差别</h4>'+p(d['neighbours'],d['sources'])+'<div class="lead">'+p(d['verdict'],d['sources'])+'</div></section>')

parts.append('<section class="card" id="merges"><h2>哪些方向应该合并</h2>')
parts.append(table(['方向','共享核心','判断','依据'],[[H(m['group']),'[推断] '+H(m['core']),'[推断] '+H(m['decision']),'[推断] '+H(m['reason'])+ref(m['sources'])] for m in MERGES]))
parts.append(p('选题顺序建议：先用 XR-S/B 的“证据到来后依赖撤销”做一个窄 benchmark 与 baseline；把 XR-L/D 的主动补证作为下一层。若合作更偏物理/几何生成，则选择 XR-C/A 的隐藏机制与影响范围实验。AIGC-C 保留为独立叙事研究备选；XR-E 以教学策略跨任务迁移与回归实验作为独立立项门槛。这个排序依据问题可测性及你已有经历，不是对合作老师意愿或资源的推测。',['PERMA','BLACK','S3','VANS','GIVE','PHYS']))
parts.append(p('合作关联仅以作者与问题匹配为依据：VANS 包含 Jing Liao；GIVE 与 S3 包含 Xiaojuan Qi。前者可讨论视频答案与任务推理，后者可讨论几何控制/主动空间证据。未推定合作承诺或导师当前兴趣。',['VANS','GIVE','S3']))
parts.append('</section><section class="card" id="control"><h2>外部控制与模型内部控制：已经做到哪里</h2>')
parts.append(table(['层次','论文','操作归类与边界分析'],[['[推断] '+H(a),'[论文] '+H(b),'[推断] '+H(c)+ref(ks)] for a,b,c,ks in CONTROL_MAP]))
parts.append(p('对 VOID 的有效性应采用分工解释：VLM 主要识别潜在影响区，VDM 根据配对训练与生成先验产生轨迹，第二遍抑制形变。VLM 不需要独自精确求解整段物理运动。消融支持这些模块有用，但尚不能唯一证明所有收益来自“因果推理能力”。',['VOID','OMNI']))
parts.append(p('“内部控制”已有 condition fusion、attention、memory/KV 与 parameter update 等具体做法。下一步可试把 evidence validity / causal dependency 映射为 token-level conditioning invalidation，再用同预算、同输入、同生成器实验检验；这是一项方法假设，不是已经验证的因果表示。',['PERMA','WEAVE','COG','DSCM']))
parts.append('</section><section class="card" id="apps"><h2>长期应用场景与可用进展</h2>'+p('下面是可研究的应用切口，不是论文已验证这些产业效果。每行给一篇已核实发表的近邻与一篇较新 arXiv 近邻；最相关与最新并不总是同一篇，不能为满足“最新”抹去任务距离。'))
app_rows=[]
for code,domain,scenario,accepted,recent,limit in APPLICATIONS:
    a=PAPERS[accepted];b=PAPERS[recent]
    app_rows.append([code+'<br>'+H(domain),'[推断] '+H(scenario),f'<a href="#paper-{accepted}">{H(a["title"])}</a><small>[论文] {H(a["venue"])}</small>',f'<a href="#paper-{recent}">{H(b["title"])}</a><small>[论文] arXiv:{b["arxiv"]} · 首版 {b["first_year"]}</small>','[推断] '+H(limit)+ref([accepted,recent])])
parts.append(table(['方向／领域','场景','已发表近邻','较新 arXiv 近邻','距离与风险'],app_rows))
parts.append('</section><section class="card" id="papers"><h2>逐篇拆解 · 38 篇去重记录</h2><p>同一论文只保留一个完整拆解，跨方向复用上面的链接。绿色为原文明示；黄色为证据强度与隐含前提的分析；灰色为待核。</p><div class="toolbar no-print"><input id="search" aria-label="搜索论文" placeholder="搜索论文、作者、数据集或方法"><select id="origin" aria-label="来源筛选"><option value="">全部来源</option><option>库内主表</option><option>既有补充参考</option><option>本次库外新找到</option></select><button id="expand">展开全部拆解</button><button id="collapse">收起全部拆解</button><button id="print">打印完整报告</button></div><p id="count" aria-live="polite"></p>')
fields=[('question','研究问题','论文'),('case','案例／平台','论文'),('operation','被控制或改变的变量','论文'),('method','技术路线与 baseline 差别','论文'),('strength','证据能支持多强的结论','推断'),('premise','明示前提／设置','论文'),('assumption','隐含假设及外推风险','推断')]
for k,a in PAPERS.items():
    parts.append(f'<article class="paper-card" id="paper-{k}" data-origin="{H(a["origin"])}"><details><summary>{k} · {H(a["title"])}</summary>')
    parts.append('<div class="meta">[论文] '+H('; '.join(a['authors']))+'<br>[论文] '+H(f'{a["year"]} · {a["venue"]}；首版 {a["first_year"]}')+f' · <a href="{H(a["venue_source"])}">发表依据</a><br>'+H(a['venue_proof'])+'</div>')
    t=a['taxonomy']
    parts.append('<p class="meta">[推断] 任务分类</p><div class="taxonomy-grid">'+''.join('<div>'+cell+'</div>' for cell in taxonomy_cells(a))+'</div>')
    parts.append('<div class="paper-summary"><h4>任务定义</h4><dl class="task-definition">')
    for field,label in [('inputs','输入'),('outputs','输出'),('invariants','必须保持不变的内容'),('judgement','判断对错的方式')]:
        parts.append('<dt>'+label+'</dt><dd>'+p(t['task_definition'][field],label='推断' if field=='invariants' else '论文')+'</dd>')
    parts.append('</dl><h4>证据类型</h4>'+p(' / '.join(t['evidence_types']),label='论文')+p(t['evidence_detail'],label='论文'))
    parts.append('<h4>一句话 · 它在所属任务里推进了什么</h4>'+p(t['one_sentence_advance'],label='论文')+f'<small>依据：<a href="{H(a["full_source"])}">{H(k)} 正文</a> · {H(a["locator"])}</small></div>')
    for key,label,tag in fields:
        parts.append('<div class="claim"><b>'+label+'：</b>'+p(a[key],label=tag)+f'<small>依据：<a href="{H(a["full_source"])}">{H(k)} 正文</a> · {H(a["locator"])}</small></div>')
    parts.append('<details class="source-details"><summary>原文与核实记录</summary>')
    ids=('arXiv:'+a['arxiv']+'；' if a['arxiv'] else '')+'；'.join('DOI:'+x for x in a['doi'])
    parts.append('<p>[论文] '+H(ids)+(' '+H(a['identifier_note']) if a['identifier_note'] else '')+f'<br><a href="{H(a["source"])}">原始摘要</a> · <a href="{H(a["full_source"])}">已读正文 {H(a["version"])}</a> · <a href="{H(a["local_evidence"])}">本地正文定位文本</a></p>')
    parts.append('<p>'+H(a['origin']+' · '+a['origin_detail'])+'<br>'+H(a['read_scope']+'；'+a['read_date'])+'<br>[论文] 定位：'+H(a['locator'])+'</p></details>')
    links=[d['code'] for d in DIRS if any(k in LINEAGES[l]['papers'] for l in d['lineages'])]
    parts.append('<p>关联方向：'+' · '.join(f'<a href="#{code}">{code}</a>' for code in links)+'</p></details></article>')
parts.append('</section>'+render_recent_catalog()+'<section class="card" id="audit"><h2>检索账本与保留缺口</h2>')
parts.append(p('检索使用公开 web search、arXiv 原始摘要/HTML、CVF、ICLR/NeurIPS proceedings、ACL Anthology、AAAI、作者正式版本。第三方聚合站只作线索，不作为技术结论的证据。以下按查询主题合并记录，不冒充系统综述的全量 PRISMA 流程。'))
parts.append(table(['范围','实际查询／获取方式','结果','状态'],[[H(s['area']),H(s['query']),H(s['result'])+(f'<br><a href="{H(s["url"])}">已打开摘要</a>' if s.get('url') else ''),H(s['kind'])] for s in SEARCH]))
parts.append('<div class="warn">'+p('L9 当前只有 2 篇核实的直接代表作，第三篇写为未找到；其余 9 条脉络各 3–6 篇。GPS 缺 arXiv/DOI 但有正式 proceedings。未核的人评人数未补造，预印本未冒记为已录用。',label='待核')+'</div>')
parts.append(p('审读时重点纠正了五类混淆：表征学习≠视频生成；视觉合理≠个体反事实真值；history consistency≠证据有效性；当前修补≠跨任务学习；镜头顺序≠观众知识。以上是本轮分析自检，未声称经过独立专家审稿。',['STATE','VOID','PERMA','CINE','SUSP']))
parts.append('</section><footer>本报告与 Topics 的 XR／AIGC 阅读入口同步；新补充摘要卡与原全文拆解分列。所有提案实验均尚未执行。</footer></main>')
parts.append('''<script>
const cards=[...document.querySelectorAll('.paper-card')];
const search=document.querySelector('#search'),origin=document.querySelector('#origin');
function filter(){const q=search.value.toLowerCase().trim();let n=0;for(const c of cards){const show=(!q||c.textContent.toLowerCase().includes(q))&&(!origin.value||c.dataset.origin===origin.value);c.classList.toggle('hidden',!show);if(show)n++;}document.querySelector('#count').textContent=`显示 ${n} / ${cards.length} 篇`;}
search.addEventListener('input',filter);origin.addEventListener('change',filter);filter();
document.querySelector('#expand').onclick=()=>cards.filter(c=>!c.classList.contains('hidden')).forEach(c=>c.querySelector('details').open=true);
document.querySelector('#collapse').onclick=()=>cards.forEach(c=>c.querySelector('details').open=false);
function reveal(){const id=decodeURIComponent(location.hash.slice(1));if(!id)return;const el=document.getElementById(id);if(!el)return;if(el.classList.contains('paper-card')){search.value='';origin.value='';filter();el.querySelector('details').open=true;}for(let p=el.parentElement;p;p=p.parentElement)if(p.tagName==='DETAILS')p.open=true;setTimeout(()=>el.scrollIntoView({block:'start'}),20);}
window.addEventListener('hashchange',reveal);reveal();
</script></body></html>''')
(ROOT/'problem-lineage-research.html').write_text(''.join(parts), encoding='utf-8')
with (ROOT/'paper-index.csv').open('w',newline='',encoding='utf-8-sig') as f:
    writer=csv.writer(f);writer.writerow(['key','title','authors','first_year','venue_year','venue','arxiv','doi','version','read_date','origin','source','full_source','locator','task','task_note','contribution_primary','contribution_secondary','contribution_focus','control_signals','target_properties','generation_paradigm','paper_type','inputs','outputs','invariants','judgement','evidence_types','evidence_detail','one_sentence_advance'])
    for a in PAPERS.values():
        t=a['taxonomy'];td=t['task_definition']
        writer.writerow([a['key'],a['title'],'; '.join(a['authors']),a['first_year'],a['year'],a['venue'],a['arxiv'],'; '.join(a['doi']),a['version'],a['read_date'],a['origin'],a['source'],a['full_source'],a['locator'],t['task'],t['task_note'],t['contribution_primary'],'; '.join(t['contribution_secondary']),t['contribution_focus'],'; '.join(t['control_signals']) or '无','; '.join(t['target_properties']) or '不适用',t['generation_paradigm'],t['paper_type'],td['inputs'],td['outputs'],td['invariants'],td['judgement'],'; '.join(t['evidence_types']),t['evidence_detail'],t['one_sentence_advance']])
print(json.dumps(dict(papers=len(PAPERS),directions=len(DIRS),lineages=len(LINEAGES),origins=counts,output=str(ROOT/'problem-lineage-research.html')),ensure_ascii=False))



if ROOT.name == "problem-lineage":
    rendered=(ROOT/"problem-lineage-research.html").read_text(encoding="utf-8").replace("本地正文定位文本", "原文定位入口（不分发全文副本）")
    (ROOT/"problem-lineage-research.html").write_text(rendered,encoding="utf-8")
    technical_assets='<!-- technical-inline:start --><link rel="stylesheet" href="../static/technical-annotations.css"><script defer src="../static/technical-annotations.js"></script><!-- technical-inline:end -->'
    rendered=rendered.replace('<button id="print">打印完整报告</button>', '')
    rendered=rendered.replace('</head>',technical_assets+'<link rel="stylesheet" href="../static/direction-analysis.css"></head>')
    (ROOT/"problem-lineage-research.html").write_text(rendered,encoding="utf-8")
    (ROOT/"index.html").write_text(rendered,encoding="utf-8")
    import runpy
    runpy.run_path(str(Path(__file__).resolve().parent/'integrate-resources.py'))
