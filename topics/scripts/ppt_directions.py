"""Shared, server-rendered direction contracts and paper roles from the PPT review."""
import html
import json
import re
import dataset_recommendations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
def read(name):
    return json.loads((ROOT / 'data' / (name + '.json')).read_text(encoding='utf-8'))
PLAN = read('ppt-direction-plan')
UPDATES = read('ppt-paper-updates')
TECH = read('technical-annotations')
RESOURCE = read('finetune-resources')
H = html.escape
def norm(s):
    return re.sub('[^a-z0-9]', '', s.lower().split('(')[0].split('（')[0])

def fields(items):
    return '<dl class="dp-facts">' + ''.join('<div><dt>'+H(k)+'</dt><dd>'+H(v)+'</dd></div>' for k,v in items) + '</dl>'

def card(code, p):
    out = f'<article class="dp-paper" id="dp-{code}-{H(p["key"])}" data-paper-key="{H(p["key"])}">'
    out += '<p class="dp-meta">'+H(str(p.get('year',''))+' · '+p.get('venue','发表状态见原记录'))+'</p>'
    out += '<h4><a href="'+H(p['source'])+'">'+H(p['title'])+'</a></h4>'
    out += '<p class="dp-role">[推断] '+H(p['role'])+' · 主阅读归属 '+H(p['primary'])+'</p>'
    out += '<p><b>为什么放在这里：</b>'+H(p['reason'])+'</p>'
    out += fields([('原文推进',p.get('method','见原论文记录')),('证据边界',p.get('remaining','未核实，不能把方向假设当作论文结果'))])
    if p.get('details'):
        out += '<div class="dp-manual-labels">'+fields(p['details'].items())+'</div>'
    else:
        matching=next((r for r in TECH['records'] if norm(r['title'])==norm(p['title']) or 'lineage:'+p['key'] in r['aliases'] or 'recent:'+p['key'] in r['aliases']),None)
        if not matching:
            r=next((r for r in RESOURCE['records'] if norm(r['title'])==norm(p['title'])),{})
            conceptual=p['key'] in ['GROUND','TMS','MIXED','ACTIVE']
            unknown='不适用：概念／理论工作，不是视频生成模型' if conceptual else '不确定：尚未在现有技术标签中核实'
            out+='<div class="dp-manual-labels">'+fields([
                ('Model',r.get('model') or unknown),('Backbone／生成方式',unknown),('Condition',unknown),
                ('训练／适应 dataset',r.get('training_datasets') or unknown),('Finetune 资源','不适用：概念工作' if conceptual else '见已审计资源卡；无卡则未核实，不推定为零'),
                ('原任务／贡献／类型 [推断]','其他：理论／交互原则；贡献落点不适用' if conceptual else '不确定：表示／训练信号等落点需原文逐项核定，不据标题硬选'),
                ('目标性质／视频生成范式',unknown),('输入／输出／Keep／判断方式','见上方方法和证据边界；未独立核实的项保持不确定'),
                ('证据类型／user study','原文研究设置见历史谱系；本轮未新增样本量核验')])+'</div>'
    out += '<p class="dp-meta"><a href="'+H(p['source'])+'">原文依据</a> · '+H(p.get('locator','沿用已核查记录'))+'</p>'
    if p.get('extra_source'):
        out += '<p class="dp-meta"><a href="'+H(p['extra_source'])+'">作者项目／发表依据</a></p>'
    return out+'</article>'

def panel(code):
    d=next(x for x in PLAN['directions'] if x['code']==code)
    catalog=read('direction-paper-membership')['directions'][code]
    out=f'<section class="dp-contract" id="plan-{code}"><p class="dp-meta">PPT 更新 · {PLAN["date"]} · slides '+', '.join(map(str,d['slides']))+' · 以下方向定义、归属和实验均为 [推断]</p>'
    out+='<p class="dp-question">'+H(d['question'])+'</p>'
    out+=fields([('触发',d['trigger']),('输出',d['output']),('必须保持',d['keep']),('任务边界',d['boundary'])])
    out+='<h3>研究链条</h3><ol class="dp-pipeline">'+''.join('<li>'+H(s)+'</li>' for s in d['pipeline'])+'</ol>'
    out+='<p class="dp-challenge"><b>为什么这个场景有独特问题：</b>'+H(d['challenge'])+'</p>'
    out+='<details><summary>最小可证伪实验 · 尚未执行</summary>'+fields([(label,d['experiment'][key]) for key,label in [('case','案例'),('operation','操作'),('controls','对照'),('metrics','指标'),('falsifier','失败判据')]])+'</details>'
    bykey={x['key']:x for x in catalog}
    out+=dataset_recommendations.panel(code)
    out+='<h3>先读这 3 篇 · 接近度与角色分开标</h3><div class="dp-reading">'+''.join(card(code,bykey[k]) for k in d['reading'])+'</div>'
    remaining=[p for p in catalog if p['key'] not in d['reading']]
    out+='<h3>方向内论文重新归组</h3><p class="dp-meta">同一论文可支持多个方向；下列主归属是阅读组织。基础理论和工程仓库不冒充直接视频方法。已有技术标签与资源记录仍随论文显示。</p>'
    for group in ['直接方法','数据／评测','可借用组件','基础理论','边界参照','工程参考']:
        ps=[p for p in remaining if p['role']==group]
        if ps:
            out+='<details class="dp-group"><summary>'+group+f' · {len(ps)} 项</summary>'+''.join(card(code,p) for p in ps)+'</details>'
    out+='<p class="dp-meta"><a href="https://soniasuns.github.io/topics/data/direction-paper-membership.csv">下载论文—方向—角色归属 CSV</a> · <a href="#analysis-'+code+'">查看历史谱系与原文局限</a></p></section>'
    return out

def scenarios(prefix=''):
    out='<section class="dp-scenarios panel" id="'+prefix+'aigc-scenarios"><h2>同一个生成问题，换到不同场景后真正变了什么？</h2><p>[推断] 以下是研究设计对照，不是既有论文已验证的结论。先选场景，再看四个 AIGC 问题及评测。</p><div class="dp-scenario-buttons" aria-label="选择应用场景">'
    for s in PLAN['scenarios']:
        out+='<button type="button" data-scenario="'+prefix+s['id']+'" aria-pressed="false">'+H(s['name'])+'</button>'
    out+='</div>'
    for s in PLAN['scenarios']:
        out+='<article class="dp-scenario" data-scenario-panel="'+prefix+s['id']+'"><h3>'+H(s['name'])+'</h3>'+fields([('真值在哪里',s['truth']),('具体案例',s['example']),('独特挑战',s['unique'])])+'<ul>'+''.join('<li>'+H(t)+'</li>' for t in s['axes'])+'</ul>'+fields([('怎样判断成功',s['evaluation']),('检验场景是否真的特殊',s['test'])])+'</article>'
    out+='<p class="dp-challenge">'+H(PLAN['crosscutting'])+'</p><details><summary>原 PPT 中需要保留的证据边界与修正</summary>'
    for c in PLAN['corrections']:
        out+='<p><b>'+H(c['claim'])+'：</b>'+H(c['correction'])+' <small>'+H(c['locator'])+'</small>'+(' <a href="'+H(c['source'])+'">原文</a>' if c['source'] else '')+'</p>'
    return out+'</details></section>'
