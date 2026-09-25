#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,io,json,sys,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:sys.path.insert(0,str(ROOT))
from research.model import CATEGORIES,heterogeneity,project_table_from_rows,residuals,wilson_interval

URL="https://zenodo.org/records/7078179/files/manual_labels.csv?download=1"
EXPECTED_MD5="a099d942098227a1fc8127759e55850e"
EXPECTED_SHA256="e1f20419341ab6c03a23da5c35cbb9d7e9fa2c7ed210d76c14293f15119b8941"

def fetch():
    req=urllib.request.Request(URL,headers={"User-Agent":"Mozilla/5.0 ResearchBundle/1.1"})
    payload=urllib.request.urlopen(req,timeout=60).read()
    md5=hashlib.md5(payload).hexdigest();sha=hashlib.sha256(payload).hexdigest()
    if md5!=EXPECTED_MD5:raise SystemExit(f"FAIL: Zenodo MD5 changed: {md5}")
    if EXPECTED_SHA256 and sha!=EXPECTED_SHA256:raise SystemExit(f"FAIL: Zenodo SHA-256 changed: {sha}")
    rows=list(csv.DictReader(io.StringIO(payload.decode("utf-8-sig"))))
    return payload,rows,md5,sha

def check_projects(got):
    with (ROOT/"data/derived/project_composition.csv").open(newline="",encoding="utf-8") as f:pack=list(csv.DictReader(f))
    if len(pack)!=len(got):raise SystemExit("FAIL: project table row count differs")
    for a,b in zip(pack,got):
        if a["project"]!=b["project"] or int(a["n"])!=b["n"]:raise SystemExit("FAIL: project identity/count differs")
        for c in CATEGORIES:
            if int(a[c+"_count"])!=b[c+"_count"]:raise SystemExit(f"FAIL: category count differs {b['project']}/{c}")
            for suffix in ("share","ci_low","ci_high"):
                if abs(float(a[c+"_"+suffix])-b[c+"_"+suffix])>1.5e-6:raise SystemExit(f"FAIL: interval/share differs {b['project']}/{c}/{suffix}")

def check_heterogeneity(got_projects):
    with (ROOT/"data/derived/heterogeneity_results.csv").open(newline="",encoding="utf-8") as f:pack={int(r["min_project_n"]):r for r in csv.DictReader(f)}
    for cut in (10,20,30,40,50):
        z=heterogeneity(got_projects,cut);r=pack[cut]
        for key in ("chi_square","p_value","cramers_v","min_expected_count"):
            if abs(float(r[key])-z[key])>max(1e-6,abs(z[key])*1e-6):raise SystemExit(f"FAIL: heterogeneity differs {cut}/{key}")
        if int(r["projects"])!=z["projects"] or int(r["n_commits"])!=z["n_commits"] or int(r["cells_expected_lt5"])!=z["cells_expected_lt5"]:raise SystemExit(f"FAIL: heterogeneity counts differ {cut}")

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--check",action="store_true");args=ap.parse_args()
    payload,rows,md5,sha=fetch()
    print("zenodo_md5:",md5);print("zenodo_sha256:",sha);print("rows:",len(rows))
    ps=project_table_from_rows(rows)
    if len(rows)!=2533 or len(ps)!=54:raise SystemExit("FAIL: source dimensions changed")
    if args.check:
        check_projects(ps);check_heterogeneity(ps)
        s=json.loads((ROOT/"results/empirical_summary.json").read_text())
        h=s["headline_metrics"]
        if h["perfective_count"]!=1022 or h["corrective_count"]!=685 or h["other_count"]!=826:raise SystemExit("FAIL: summary category counts differ")
        print("zenodo_rebuild: PASS")
    else:
        print(json.dumps({"primary":heterogeneity(ps,20),"sensitivity_n30":heterogeneity(ps,30),"largest_residuals":residuals(ps)[:10]},indent=2))

if __name__=="__main__":main()
