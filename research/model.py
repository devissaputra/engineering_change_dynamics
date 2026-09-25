from __future__ import annotations
import csv, json
from collections import defaultdict
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def classify(internal, external): return 'both' if internal and external else 'internal_only' if internal else 'external_only' if external else 'neither'
def aggregate(rows):
    counts={'internal_only':0,'external_only':0,'neither':0,'both':0}; projects=defaultdict(lambda:[0,0,0])
    for r in rows:
        i=str(r['internal_quality']).lower()=='true'; e=str(r['external_quality']).lower()=='true'; counts[classify(i,e)]+=1
        p=projects[r['project']]; p[0]+=1; p[1]+=int(i); p[2]+=int(e)
    return counts,{k:{'n':v[0],'internal_share':v[1]/v[0],'external_share':v[2]/v[0]} for k,v in projects.items()}
def load_summary(): return json.loads((ROOT/'results/empirical_summary.json').read_text())
def load_packaged_projects():
    with (ROOT/'data/derived/primary_results.csv').open() as f:return list(csv.DictReader(f))
def validate_bundle():
    s=load_summary()['headline_metrics']; p=load_packaged_projects()
    return s['n_commits']==2533 and s['n_projects']==54 and s['internal_only']+s['external_only']+s['neither']+s['both']==2533 and len(p)==10
