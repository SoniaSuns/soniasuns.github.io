"""Shared HTML for the eight direction histories; no client-side data dependency."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'data/direction-analysis.json').read_text(encoding='utf-8'))
PAPERS = DATA['papers']
DIRECTIONS = {d['code']: d for d in DATA['directions']}
H = html.escape


def paper_body(key):
    p = PAPERS[key]
    items = [('原文方法', p['method']), ('已经解决', p['solved']),
             ('尚未解决 · 分析', p['remaining']), ('技术引入的代价 · 分析', p['tradeoff'])]
    if p['author_limit']:
        items.append(('原文明示的限制／设置边界', p['author_limit']))
    out = '<dl class="da-findings">' + ''.join(
        f'<div><dt>{H(label)}</dt><dd>{H(text)}</dd></div>' for label, text in items) + '</dl>'
    out += f'<p class="da-source"><a href="{H(p["source"])}">原文依据</a> · {H(p["locator"])}</p>'
    if p.get('extra_source'):
        out += f'<p class="da-source"><a href="{H(p["extra_source"])}">作者项目与数据说明</a></p>'
    for a in p['assessments']:
        out += ('<details class="da-assessment"><summary>后续论文如何评价这篇工作 · '+H(a['by'])+'</summary>'
                '<p>'+H(a['text'])+'</p><p><b>比较边界：</b>'+H(a['boundary'])+'</p>'
                f'<p class="da-source"><a href="{H(a["source"])}">评价原文</a> · {H(a["locator"])}</p></details>')
    return out


def card(code, group, item):
    key = item['key']; p = PAPERS[key]
    meta = str(p['year'])+' · '+p['venue']
    if p.get('first_year', p['year']) != p['year']:
        meta += ' · 首版 '+str(p['first_year'])
    out = f'<article class="da-paper" id="da-{code}-{group}-{key}"><p class="da-meta">{H(meta)}</p>'
    out += f'<h5><a href="{H(p["source"])}">{H(p["title"].replace("A$^2$RD", "A²RD"))}</a></h5>'
    if 'fit' in item:
        out += '<p class="da-fit"><b>为何选它：</b>'+H(item['fit'])+'</p>'
    if 'transition' in item:
        out += '<p class="da-fit"><b>推进了哪一步：</b>'+H(item['transition'])+'</p><p><b>留下的断点：</b>'+H(item['residual'])+'</p>'
    if 'role' in item:
        out += '<p class="da-fit"><b>'+H(item['role'])+'</b> · '+H(item['comparison'])+'</p>'
    return out + paper_body(key) + '</article>'


def panel(code):
    d = DIRECTIONS[code]
    out = f'<section class="direction-analysis" id="analysis-{code}" aria-labelledby="analysis-title-{code}">'
    out += f'<p class="da-meta">问题演进与技术局限 · {DATA["date"]}</p><h3 id="analysis-title-{code}">{code} · 从早期基础到当前研究缺口</h3>'
    out += '<p class="da-overview">'+H(d['summary'])+'</p>'
    out += '<div class="da-position"><h4>早期代表作选得是否合适？</h4><p>'+H(d['foundation_judgement'])+'</p></div>'
    out += '<h4>领域真正关注的问题</h4><ol class="da-questions">'+''.join('<li>'+H(q)+'</li>' for q in d['questions'])+'</ol>'
    out += '<p class="da-note">'+H(DATA['interpretation'])+'</p>'
    groups = [('foundations','01 · 早期代表作：为什么选、解决了什么、没有解决什么'),
              ('milestones','02 · 中间里程碑：每一步怎样推进，又留下什么'),
              ('neighbors','03 · 最近邻：已有解法、竞争边界与技术代价')]
    for group, title in groups:
        out += '<details class="da-stage"><summary>'+H(title)+f'<span>{len(d[group])} 篇</span></summary>'
        out += '<div class="da-paper-list">'+''.join(card(code,group,x) for x in d[group])+'</div></details>'
    out += '<h4>更深层的原则问题</h4><div class="da-principles">'+''.join(
        '<article><h5>'+H(x['title'])+'</h5><p>'+H(x['text'])+'</p></article>' for x in d['principles'])+'</div>'
    out += '<div class="da-proposal"><h4>还值得做什么 · 研究判断</h4><p>'+H(d['gap'])+'</p>'
    out += '<h4>真值与评测怎样获得</h4><p>'+H(d['truth'])+'</p>'
    out += '<details class="da-experiment"><summary>可证伪的最小实验 · 尚未执行</summary><dl class="da-findings">'
    for key, label in [('case','具体案例'),('operation','实验操作'),('controls','必须比较的基线'),('metrics','评价指标'),('falsifier','什么结果会推翻假设')]:
        out += '<div><dt>'+label+'</dt><dd>'+H(d['experiment'][key])+'</dd></div>'
    out += '</dl></details></div>'
    links = []
    for key in d['reading']:
        group = next(g for g, _ in groups if any(x['key']==key for x in d[g]))
        links.append(f'<a href="#da-{code}-{group}-{key}">{H(key)}</a>')
    out += '<p class="da-reading"><b>建议阅读顺序：</b>'+' → '.join(links)+'</p>'
    out += '<ul class="da-connections">'+''.join(
        f'<li><a href="#analysis-{x["code"]}">{x["code"]}</a> · {H(x["text"])}</li>' for x in d['connections'])+'</ul>'
    return out + '</section>'


def overview_link(code):
    return f'<p class="da-overview-link"><a href="#analysis-{code}">新增：早期代表作 → 里程碑 → 最近邻 → 技术局限与实验假设</a></p>'
