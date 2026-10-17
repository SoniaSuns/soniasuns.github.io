"""Validate resource coverage and stage arithmetic without fetching paper texts."""
from pathlib import Path
from collections import Counter
import csv,json
root=Path(__file__).resolve().parents[1]
d=json.loads((root/'data/finetune-resources.json').read_text(encoding='utf-8'))
rs=d['records'];byid={r['id']:r for r in rs};c=d['counts']
assert len(rs)==len(byid)==c['total']==774
assert sum(bool(r['library_id']) for r in rs)==c['main']==451
assert sum(bool(r['technical_key']) for r in rs)==c['technical']==287
assert sum(r['has_fulltext'] for r in rs)==c['fulltext']==761
assert sum(bool(r['reasoning_id']) for r in rs)==c['reasoning']==109
assert dict(Counter(r['status'] for r in rs))==c['status']
assert sum(r['max_reported_ft_gpus'] is not None for r in rs)==c['known_ft_gpu_count']==222
assert sum(r['has_ft_time'] for r in rs)==c['known_ft_device_hours']==93
for a,key in d['alias_index'].items():assert a in byid[key]['aliases']
for r in rs:
    assert r['source_url'].startswith(('https://','http://'))
    ft=[s for s in r['stages'] if s['role']=='ft' and s['comparable'] and s['is_gpu']]
    assert r['has_comparable_ft']==bool(ft)
    assert r['has_ft_time']==any(s['gpu_hours_max'] is not None for s in ft)
    known=[s['count_max'] for s in ft if s['count_max'] is not None]
    assert r['max_reported_ft_gpus']==(max(known) if known else None)
    for s in r['stages']:
        assert s['role'] in d['role_labels'] and s['source_url'].startswith(('https://','http://'))
        if s['is_gpu'] and s['count_min'] and s['wall_hours_min']:
            assert abs(s['gpu_hours_min']-s['count_min']*s['wall_hours_min'])<0.00011
            assert abs(s['gpu_hours_max']-s['count_max']*s['wall_hours_max'])<0.00011
with (root/'data/finetune-resources.csv').open(encoding='utf-8-sig',newline='') as f:
    csvrows=list(csv.DictReader(f))
assert [r['id'] for r in csvrows]==[r['id'] for r in rs]
raw=(root/'data/finetune-resources.json').read_text(encoding='utf-8')
assert 'C:\\' not in raw and 'fulltext/R' not in raw
print(json.dumps({'validated':c,'csv_rows':len(csvrows)},ensure_ascii=True))
