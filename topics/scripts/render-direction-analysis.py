"""Update existing Topics HTML without rebuilding or replacing the paper library.

Run build-direction-analysis.py first, then this script and render-lineage.py.
Markers make this operation idempotent. Existing direction/overview content stays.
"""
import re
from pathlib import Path
import direction_analysis as analysis

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'index.html'
page = path.read_text(encoding='utf-8')
for code in analysis.DIRECTIONS:
    start, end = f'<!-- direction-analysis-start:{code} -->', '<!-- direction-analysis-end -->'
    block = start + analysis.panel(code) + end
    if start in page:
        page, n = re.subn(re.escape(start)+'.*?'+re.escape(end), lambda _:block, page, flags=re.S)
    else:
        pattern = r'(<article\b[^>]*\bid="'+re.escape(code)+r'"[^>]*>.*?</h2>)'
        page, n = re.subn(pattern,lambda m:m[1]+block,page,count=1,flags=re.S)
    assert n == 1, (code,n)
    start, end = f'<!-- direction-analysis-overview:{code} -->', '<!-- direction-analysis-overview-end -->'
    block = start + analysis.overview_link(code) + end
    if start in page:
        page, n = re.subn(re.escape(start)+'.*?'+re.escape(end),lambda _:block,page,flags=re.S)
    else:
        pattern = r'(<article\b[^>]*\bid="overview-'+re.escape(code)+r'"[^>]*>.*?)(</article>)'
        page,n = re.subn(pattern,lambda m:m[1]+block+m[2],page,count=1,flags=re.S)
    assert n == 1, (code,'overview',n)
asset = '<link rel="stylesheet" href="static/direction-analysis.css">'
if asset not in page:
    page = page.replace('</head>',asset+'</head>',1)
path.write_text(page,encoding='utf-8')
print(f'Updated {len(analysis.DIRECTIONS)} inline analyses and overview links: {path}')
