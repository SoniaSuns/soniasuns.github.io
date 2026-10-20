"""Inline test-dataset recommendations; source facts are separate from adaptation."""
import html
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'data/direction-test-datasets.json').read_text(encoding='utf-8'))
H=html.escape

def panel(code):
    d=DATA['directions'][code]
    out=f'<section class="dt-datasets" id="datasets-{code}"><h3>适合测试的数据集与缺失协议</h3><p class="dp-meta">核查 {DATA["checked"]} · 数据内容／获取状态来自官方资料；用途选择、补标与指标建议为 [推断]。</p>'
    out+='<p class="dp-question">[推断] '+H(d['start'])+'</p>'
    for i in d['items']:
        s=DATA['datasets'][i['dataset']]
        out+='<details class="dt-dataset"><summary>'+H(s['name'])+' <span class="dp-meta">· '+H(i['fit'])+'</span></summary><dl class="dp-facts">'
        for label,value in [('类型',s['kind']),('原有数据／任务',s['facts']),('获取状态',s['access']),('怎么改成你的测试 [推断]',i['adapt']),('测什么 [推断]',i['metrics'])]:
            out+='<div><dt>'+H(label)+'</dt><dd>'+H(value)+'</dd></div>'
        out+='</dl><p class="dp-meta"><a href="'+H(s['source'])+'">官方数据／论文入口</a> · '+H(s['locator'])+'</p></details>'
    out+='<p class="dp-challenge"><b>还缺什么 [推断]：</b>'+H(d['missing'])+'</p><p><b>划分与测试协议 [推断]：</b>'+H(d['split'])+'</p>'
    out+='<p class="dp-meta">“可直接测”仅指上方限定的子任务，不代表覆盖整个 direction。论文定义的 benchmark 与已核实可获取的数据分开标注；未下载全量数据或运行实验。</p></section>'
    return out
