import html
H=html.escape
CSS='\n.reading-update{border:1px solid #a9c6bd;border-radius:12px;background:#f4faf7;padding:20px;margin:22px 0;overflow-wrap:anywhere}\n.reading-update-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}\n.reading-update-card{background:#fff;border:1px solid #d4e2dc;border-radius:9px;padding:16px;min-width:0}\n.reading-update-card h4{margin:6px 0 12px;line-height:1.5;font-size:16px}.reading-update-card p{font-size:14px}\n.reading-update-meta{font-size:12px!important;color:#506b61}.reading-update details{margin-top:16px}\n.reading-update details .reading-update-card{margin-top:10px}\n@media(max-width:900px){.reading-update-grid{grid-template-columns:1fr}.reading-update{padding:14px}}\n'
def refcard(key, base='', rank=None):
    p=catalog[key]
    return ('<article class="reading-update-card">'+
      f'<p class="reading-update-meta">{str(rank)+" · " if rank else ""}{H(p["venue"])} · {H(p["publication_status"])}</p>'+
      f'<h4><a href="{H(p["source"])}">{H(p["title"])}</a></h4>'+
      f'<p><b>论文明确内容</b> {H(p["finding"])}</p><p><b>与本方向的距离</b> {H(p["boundary"])}</p>'+
      f'<p class="reading-update-meta"><a href="{H(p["venue_source"])}">发表依据</a> · <a href="{base}#recent-{key}">核对记录</a></p></article>')

def panel(code, report=False):
    r=routes[code]; base='' if report else 'problem-lineage/'
    title='最推荐先读的 3 篇' if code.startswith('AIGC') else '2026 已发表近邻 · 优先阅读'
    body=f'<section class="reading-update" data-reading-update="{code}"><p class="reading-update-meta">2026-10-15 · [推断] 阅读排序</p><h3>{title}</h3><p>{H(r["focus"])}</p><p class="note">{H(r["boundary"])}</p>'
    body+='<div class="reading-update-grid">'+''.join(refcard(k,base,i+1) for i,k in enumerate(r['primary']))+'</div>'
    if r['more']:
        body+='<details><summary>继续阅读与补充边界（'+str(len(r['more']))+' 篇）</summary>'+''.join(refcard(k,base) for k in r['more'])+'</details>'
    if not report: body+=f'<p><a class="button" href="problem-lineage/#{code}">阅读问题谱系、完整实验与逐篇拆解 →</a></p>'
    return body+'</section>'

def render_recent_catalog():
    out='<section class="card" id="recent-reading"><h2>近期补充阅读与发表状态</h2><p>补充卡按摘要／项目页记录；已有全文拆解保留原阅读日期。排序与方向迁移属于 [推断]。正式发表包含会议归属已确认的工作，具体核实源逐篇提供。</p><p><a href="recent-reading.csv">下载本次补充阅读 CSV</a></p>'
    for key,p in catalog.items():
        out+=f'<div id="recent-{key}">'+refcard(key)
        out+='<p class="meta">核对：'+H(p['read_scope'])+' · '+H(p['read_date'])+' · arXiv: '+H(p['arxiv'] or '未核实／未找到')+'</p>'
        if p.get('deep_analysis_key'): out+='<p><a href="#paper-'+p['deep_analysis_key']+'">已有全文拆解 →</a></p>'
        out+='</div>'
    return out+'</section>'
