"""Attach additive resource cards to the existing Topics pages; safe to rerun."""
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parents[1]
def assets(prefix):
    return '<!-- resource-inline:start --><link rel="stylesheet" href="'+prefix+'static/resources.css"><script defer src="'+prefix+'static/resource-core.js"></script><script defer src="'+prefix+'static/resource-inline.js"></script><!-- resource-inline:end -->'
for rel,prefix in [('index.html',''),('video-generation-pool/index.html','../'),('problem-lineage/index.html','../'),('problem-lineage/problem-lineage-research.html','../')]:
    path=ROOT/rel
    if not path.exists():continue
    s=path.read_text(encoding='utf-8')
    s=re.sub(r'<!-- resource-inline:start -->.*?<!-- resource-inline:end -->','',s,flags=re.S)
    s=s.replace('</head>',assets(prefix)+'</head>')
    path.write_text(s,encoding='utf-8')
main=ROOT/'index.html';s=main.read_text(encoding='utf-8')
if 'data-view="resources"' not in s:
    s=s.replace('    <button data-view="topic-trends"','    <button data-view="resources" aria-pressed="false" aria-controls="resources-view">训练资源 · 全库比较</button>\n    <button data-view="topic-trends"',1)
if 'id="resources-view"' not in s:
    s=s.replace('</main>','<section id="resources-view" hidden><p><a href="resources/" target="_blank" rel="noopener">单独打开训练资源与选题比较 ↗</a></p><iframe id="resources-frame" src="resources/" title="全库论文训练资源与 topic 比较" style="width:100%;border:0;min-height:1000px" loading="lazy"></iframe></section></main>')
main.write_text(s,encoding='utf-8')
reader=ROOT/'static/reader.js';s=reader.read_text(encoding='utf-8')
s=s.replace("'video-reasoning','topic-trends']","'video-reasoning','topic-trends','resources']")
if "target.closest('#resources-view')" not in s:
    s=s.replace("if(target.closest('#video-reasoning-view'))", "if(target.closest('#resources-view'))show('resources');else if(target.closest('#video-reasoning-view'))")
reader.write_text(s,encoding='utf-8')
# Preserve original details behavior after the new resource details element is added.
for rel in ['video-generation-pool/catalog.js','problem-lineage/index.html','problem-lineage/problem-lineage-research.html']:
    p=ROOT/rel;s=p.read_text(encoding='utf-8').replace("querySelector('details')","querySelector('details:not(.resource-inline)')");p.write_text(s,encoding='utf-8')
print('Resource cards attached to Topics, video pool, and lineage pages.')
for rel in ['video-reasoning-2024-2026/index.html','video-reasoning-2024-2026/model-data.html']:
    p=ROOT/rel;s=p.read_text(encoding='utf-8')
    s=re.sub(r'<!-- resource-inline:start -->.*?<!-- resource-inline:end -->','',s,flags=re.S)
    s=s.replace('</head>',assets('../').replace('resource-inline.js','resource-reasoning.js')+'</head>')
    if 'id="resource-scope-note"' not in s:
        s=s.replace('<nav>','<p id="resource-scope-note">训练资源核查覆盖 Topics 主库、技术标注池与 109 篇 R1/R2/R3 清单；批量标题筛选候选不视作已完成全文资源核查。<a href="../resources/">查看逐篇资源与统计 →</a></p><nav>',1)
    p.write_text(s,encoding='utf-8')
