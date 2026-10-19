"""Apply the reviewed PPT plan without replacing the original paper taxonomy.

Run after build-direction-analysis.py (if rebuilding history), then render-lineage.py.
This script is idempotent and does not alter original model/resource evidence.
"""
import copy
import csv
import html
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
ROOT=Path(__file__).resolve().parents[1]
def read(name): return json.loads((ROOT/'data'/f'{name}.json').read_text(encoding='utf-8'))
def write(name,data): (ROOT/'data'/f'{name}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def norm(s): return re.sub('[^a-z0-9]','',s.lower().split('(')[0].split('（')[0]).replace('a2rd','a2rd')
plan=read('ppt-direction-plan'); updates=read('ppt-paper-updates')
analysis=read('direction-analysis'); technical=read('technical-annotations'); resources=read('finetune-resources')
library=read('papers'); lib={p['id']:p for p in library}
lineagepath=ROOT/'problem-lineage/problem-lineage-research.json'
lineage=json.loads(lineagepath.read_text(encoding='utf-8'))
profiles=analysis['papers']
for key,p in lineage['recent_evidence']['papers'].items():
    if key not in profiles:
        profiles[key]={'key':key,'title':p['title'],'year':p['year'],'first_year':p['year'],'venue':p['venue'],'source':p['source'],'locator':p['read_scope'],'method':p['finding'],'solved':p['finding'],'remaining':p['boundary'],'tradeoff':'[推断] 迁移到当前任务时需重新控制输入、预算和评价对象。','author_limit':'','assessments':[],'library_id':'','evidence_date':p['read_date']}
for key,p in updates['papers'].items():
    profiles[key]={'key':key,'first_year':p['year'],'assessments':[],'library_id':'','evidence_date':plan['date'],**p}
for key,titlepart in [('SPLICE','ActionSplice'),('MIND','MindCube')]:
    pool=technical['records'] if key=='SPLICE' else resources['records']
    t=next(x for x in pool if titlepart in x['title'])
    if key=='SPLICE':
        method=t['technical']['contribution_plain'];source=t['source_url'];venue=t['venue']
    else:
        method='从有限视图构建空间 mental model，进行空间推理；不等于主动澄清。';source='https://arxiv.org/abs/2506.21458';venue=t['venue']
    profiles[key]={'key':key,'title':t['title'],'year':2026,'first_year':2026 if key=='SPLICE' else 2025,'venue':venue,'source':source,'locator':'原库正文核验记录；PPT 19／24 对照','method':method,'solved':method,'remaining':updates['roles'][key][2],'tradeoff':'[推断] 作为接口组件迁移时，需独立验证新任务的证据与预算。','author_limit':'','assessments':[],'library_id':t.get('library_id',''),'evidence_date':plan['date']}
profiles['ACE'].update(source='https://arxiv.org/html/2510.04618v3',first_year=2025,locator='方法；Appendix A.6 Pruning Trigger',method='Generator／Reflector／Curator 增量维护 playbook；新版包含去重、合并与 pruning。',remaining='没有建立用户协作惯例的适用范围、撤销判断和学习收益归因。')
profiles['MULTI']['method']='配对游戏世界与机制 DAG；生成概念验证使用 OpenJourney 的 peak-action 单帧，不是完整视频生成。'
profiles['MULTI']['remaining']='机制真值和配对协议可借用，但不能作为现实 XR 视频后果或学习迁移的直接证据。'

# Collect every existing direction reference; deduplicate by normalized title.
titlekey={norm(p['title']):k for k,p in profiles.items()}
original={d['code']:d for name in ['xr-directions','aigc-directions'] for d in read(name)}
histories={d['code']:d for d in analysis['directions']}
members={d['code']:{} for d in plan['directions']}
foundationkeys={i['key'] for d in histories.values() for i in d['foundations']}
def add(code,key,reason='',role=None):
    if key not in profiles: return
    p=profiles[key]
    override=updates['roles'].get(key)
    if override: primary,chosen,why=override
    else:
        primary=p.get('primary_direction',code)
        chosen=role or ('基础理论' if key in foundationkeys else '可借用组件')
        why=reason or '[推断] 沿用原方向的模块关系；不是完整解决当前问题的直接证据。'
    members[code][key]={**p,'primary':primary,'role':chosen,'reason':why}
    profiles[key].setdefault('primary_direction',primary)

techbykey={p['key']:p for p in technical['records']}
def from_support(pid):
    if pid in lib:
        p=lib[pid];k=titlekey.get(norm(p['title']))
        if k:return k
        k='LIB-'+pid
        profiles[k]={'key':k,'title':p['title'],'year':p['year'],'venue':p.get('venue','原库未单列；以论文链接为准'),'source':p['public_url'],'method':p['what'],'solved':p.get('gap',''),'remaining':p.get('boundary',''),'tradeoff':'','author_limit':'','assessments':[],'locator':p.get('source_evidence','原库记录'),'library_id':pid,'evidence_date':'沿用原库'}
    else:
        alias=technical['alias_index'].get('external:'+pid) or technical['alias_index'].get('library:'+pid)
        if not alias:return None
        p=techbykey[alias];k=titlekey.get(norm(p['title']))
        if k:return k
        k='TECH-'+p['id'];profiles[k]={'key':k,'title':p['title'],'year':p['year'],'venue':p['venue'],'source':p['source_url'],'method':p['technical']['contribution_plain'],'solved':p['taxonomy']['one_sentence_advance'],'remaining':p['taxonomy']['uncertainty'],'tradeoff':'','author_limit':'','assessments':[],'locator':p['evidence']['locator'],'library_id':'','evidence_date':'沿用原库'}
    titlekey[norm(profiles[k]['title'])]=k
    return k

for code,d in original.items():
    for s in d['support']:
        k=from_support(s['paper'])
        if k:add(code,k,s.get('established','')+' [推断] '+s.get('missing',''))
    for group in ['foundations','milestones','neighbors']:
        for i in histories[code][group]:add(code,i['key'],i.get('fit') or i.get('comparison') or i.get('transition',''))
    old=lineage['recent_evidence']['directions'][code]
    for k in old['primary']+old['more']:add(code,k)

extra={'XR-C':['LAB','MULTI','CAUSAL'], 'XR-S':['SPLICE','STREAMCODE','CODEVIDEO'], 'XR-L':['MIND','DISCOVER'], 'XR-E':['DISCOVER','VISTA'], 'AIGC-A':['CODEVIDEO'], 'AIGC-B':['SPLICE'], 'AIGC-C':[], 'AIGC-D':['DISCOVER','MIND','CODEVIDEO','SKETCH']}
for code,keys in extra.items():
    for k in keys:add(code,k)
# Direct clarification excludes co-formed goals; show these only as explicit boundaries.
for code in ['XR-L','XR-E']:
    if 'DISCOVER' in members[code]:members[code]['DISCOVER']['role']='边界参照'
if 'MIND' in members['XR-L']:members['XR-L']['MIND']['role']='边界参照'
if 'SKETCH' in members['XR-L']:members['XR-L']['SKETCH']['role']='边界参照'
for d in plan['directions']:
    for k in d['reading']:add(d['code'],k)
    old=histories[d['code']]
    old['summary']=d['question']+' '+d['boundary'];old['questions']=d['pipeline'];old['gap']='[推断] '+d['challenge'];old['truth']='[推断] '+d['keep']+' '+d['experiment']['metrics'];old['experiment']=d['experiment']
    # Keep historical papers and anchors; update proximity language rather than erasing history.
    for i in old['neighbors']:
        if i['key'] in updates['roles']:
            _,i['role'],i['comparison']=updates['roles'][i['key']]
all_keys={k for ps in members.values() for k in ps}
for key in all_keys:
    codes=[code for code,ps in members.items() if key in ps]
    if key in updates['roles']:
        primary=updates['roles'][key][0]
    elif len(codes)==1:
        primary=codes[0]
    elif key in foundationkeys:
        primary='跨方向基础：'+' / '.join(codes)
    else:
        primary='不确定：'+' / '.join(codes)+'（共享参考，未强行指定主归属）'
    profiles[key]['primary_direction']=primary
    for code in codes:
        members[code][key]['primary']=primary
        members[code][key].pop('primary_direction',None)
analysis['date']=plan['date'];analysis['interpretation']='论文方法／结果按原文记录；任务归属、迁移判断、技术代价与实验提案均为 [推断]。最新方向定义与优先阅读见本页 PPT 更新；历史谱系保留。'
write('direction-analysis',analysis)
membership={'date':plan['date'],'scope':plan['scope'],'directions':{k:list(v.values()) for k,v in members.items()}}
write('direction-paper-membership',membership)
with (ROOT/'data/direction-paper-membership.csv').open('w',encoding='utf-8-sig',newline='') as f:
    w=csv.writer(f);w.writerow(['direction','paper_key','title','year','venue','primary_reading_direction','role_in_direction','classification_reason','source'])
    for code,ps in members.items():
        for p in ps.values():w.writerow([code,p['key'],p['title'],p['year'],p['venue'],p['primary'],p['role'],p['reason'],p['source']])

# Additive reading roles: do not change six-axis taxonomy, technical fields, or costs.
bytitle={}
for code,ps in members.items():
    for p in ps.values():bytitle.setdefault(norm(p['title']),[]).append({'direction':code,'role':p['role'],'reason':p['reason'],'primary':p['primary']})
for name,data in [('papers',library),('technical-annotations',technical),('finetune-resources',resources)]:
    for p in data if isinstance(data,list) else data['records']:
        roles=bytitle.get(norm(p['title']))
        if not roles:continue
        p['direction_roles']=roles
        codes=sorted({x['direction'] for x in roles})
        if name=='papers':
            p['application_targets']=sorted(set(p.get('application_targets',[]))|{x for x in codes if x.startswith('XR-')})
            p['aigc_targets']=sorted(set(p.get('aigc_targets',[]))|{x for x in codes if x.startswith('AIGC-')})
        else:p['directions']=sorted(set(p.get('directions',[]))|set(codes))
    write(name,data)
for name in ['xr-directions','aigc-directions']:
    ds=read(name)
    for d in ds:
        new=next(x for x in plan['directions'] if x['code']==d['code'])
        for k in ['name','zh','question','trigger','output']:d[k]=new[k]
        d['distinction']=new['boundary'];d['summary']=new['question']+' '+new['boundary'];d['gap']=new['challenge'];d['progression']=new['pipeline'];d['ppt_plan']=new
        for s in d['support']:
            key=from_support(s['paper'])
            if key in members[d['code']]:
                p=members[d['code']][key];s['level']=p['role'];s['reading_primary']=p['primary'];s['classification_reason']=p['reason']
        d['paper_membership']=[{'key':p['key'],'role':p['role'],'primary':p['primary']} for p in members[d['code']].values()]
    write(name,ds)
overviews=read('overviews')
for o in overviews:
    if o['code'] not in members:continue
    d=next(x for x in plan['directions'] if x['code']==o['code'])
    o.update(name=d['zh'],summary=d['question'],boundary=d['boundary'],question=d['question'],evaluation=d['experiment']['metrics'],progression=d['pipeline'],gap=d['challenge'],hypothesis='[推断] '+d['experiment']['operation'],falsifier=d['experiment']['falsifier'],ppt_reading=d['reading'])
write('overviews',overviews)

# Revise the lineage report's substantive conclusions, not just its title.
for d in lineage['directions']:
    n=next(x for x in plan['directions'] if x['code']==d['code'])
    d.update(name=n['zh'],definition=n['question'],boundary=n['boundary'],core=n['challenge'],why=n['keep'],experiment=n['experiment'])
    d['verdict']='[推断] '+n['boundary'];d['neighbours']='[推断] 最新角色划分与阅读顺序见本方向的 PPT 更新；原历史谱系保留。'
for m in lineage['merges']:
    if m['group']=='XR-C + AIGC-A':m.update(decision='共享后果推断与执行方法，保留独立任务验证。',reason='XR-C 额外引入学员闭环、教学对照选择与无帮助迁移；若未验证这些，只是 AIGC-A 的教程应用。')
    if m['group']=='XR-S + AIGC-B':m.update(decision='共享证据与记忆修订方法，分别报告应用约束。',reason='XR 不能重写真实已执行动作；离线作品可版本化重剪，在线游戏也有不可撤回的玩家历史。')
    if m['group']=='XR-E':m.update(core='跨任务协作惯例、作用域与分工边界',reason='需要分离 agent 学习与用户熟练；不能把帮助减少或单任务 critic 提升等同于共同进步。')
lineage['date']=plan['date'];lineage['ppt_plan']=plan
lineagepath.write_text(json.dumps(lineage,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

# Replace whole direction articles using parsed positions, safe with nested articles.
class ElementRanges(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=False);self.text=text;self.lines=[0];self.stack=[];self.ranges={}
        for m in re.finditer('\n',text):self.lines.append(m.end())
        self.feed(text)
    def pos(self):a,b=self.getpos();return self.lines[a-1]+b
    def handle_starttag(self,tag,attrs):
        if tag=='article':self.stack.append((dict(attrs).get('id'),self.pos()))
    def handle_endtag(self,tag):
        if tag=='article' and self.stack:
            key,start=self.stack.pop()
            if key:self.ranges[key]=(start,self.text.index('>',self.pos())+1)

import ppt_directions as render
import direction_analysis as history
page=(ROOT/'index.html').read_text(encoding='utf-8');ranges=ElementRanges(page).ranges;edits=[]
for d in plan['directions']:
    c=d['code'];body='<article class="direction '+('aigc-direction ' if c.startswith('AIGC') else '')+'panel" id="'+c+'"><div class="eyebrow">'+c+' · '+html.escape(d['name'])+'</div><h2>'+html.escape(d['zh'])+'</h2>'+render.panel(c)
    body+='<!-- direction-analysis-start:'+c+' -->'+history.panel(c)+'<!-- direction-analysis-end --></article>'
    edits.append((*ranges[c],body))
    oid='overview-'+c;start,end=ranges[oid];opening=page[start:page.index('>',start)+1]
    body=opening+'<h3>'+c+' · '+html.escape(d['zh'])+'</h3><p class="overview-summary">'+html.escape(d['question'])+'</p><div class="dp-overview">'+render.fields([('任务边界',d['boundary']),('独特挑战',d['challenge']),('评价',d['experiment']['metrics'])])+'</div><p><a href="#'+c+'">阅读方向定义与重新归组的论文 →</a></p><!-- direction-analysis-overview:'+c+' -->'+history.overview_link(c)+'<!-- direction-analysis-overview-end --></article>'
    edits.append((start,end,body))
for start,end,body in sorted(edits,reverse=True):page=page[:start]+body+page[end:]
page=re.sub(r'<!-- ppt-scenarios:start -->.*?<!-- ppt-scenarios:end -->','',page,flags=re.S)
# Keep paper-library direction filters aligned with the reorganized reading routes.
def paper_opening(match):
    tag=match[0];pid=re.search(r'id="paper-([^"]+)"',tag)
    if not pid or pid[1] not in lib:return tag
    p=lib[pid[1]]
    for attr,key in [('data-xr','application_targets'),('data-aigc','aigc_targets')]:
        value=' '.join(p.get(key,[]))
        tag=re.sub(r'\b'+attr+r'="[^"]*"',lambda _:attr+'="'+html.escape(value)+'"',tag)
    return tag
page=re.sub(r'<article\b[^>]*class="paper"[^>]*>',paper_opening,page)
marker=re.search(r'<section\b[^>]*id="aigc-view"[^>]*>',page)
assert marker
page=page[:marker.end()]+'<!-- ppt-scenarios:start -->'+render.scenarios()+'<!-- ppt-scenarios:end -->'+page[marker.end():]
assets='<link rel="stylesheet" href="static/ppt-directions.css"><script defer src="static/ppt-directions.js"></script>'
if 'static/ppt-directions.css' not in page:page=page.replace('</head>',assets+'</head>')
(ROOT/'index.html').write_text(page,encoding='utf-8')
print(json.dumps({'directions':len(members),'unique_references':len(bytitle),'memberships':sum(len(x) for x in members.values()),'main_library_preserved':len(library),'taxonomy_records_preserved':len(technical['records']),'resource_records_preserved':len(resources['records'])}))
