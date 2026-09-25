from __future__ import annotations
import csv,json,math
from pathlib import Path
from scipy.stats import chi2

ROOT=Path(__file__).resolve().parents[1]
CATEGORIES=("perfective","corrective","other")

def classify(internal,external):
    i=str(internal).lower()=="true";e=str(external).lower()=="true"
    if i and e:raise ValueError("Source taxonomy is expected to be mutually exclusive")
    return "perfective" if i else "corrective" if e else "other"

def wilson_interval(k,n,z=1.959963984540054):
    p=k/n;den=1+z*z/n
    center=(p+z*z/(2*n))/den
    half=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/den
    return p,center-half,center+half

def project_table_from_rows(rows):
    d={}
    for r in rows:
        c=classify(r["internal_quality"],r["external_quality"])
        p=d.setdefault(r["project"],{"project":r["project"],"n":0,"perfective_count":0,"corrective_count":0,"other_count":0})
        p["n"]+=1;p[c+"_count"]+=1
    out=[]
    for p in sorted(d.values(),key=lambda x:x["project"]):
        q=dict(p)
        for c in CATEGORIES:
            s,lo,hi=wilson_interval(p[c+"_count"],p["n"])
            q[c+"_share"]=s;q[c+"_ci_low"]=lo;q[c+"_ci_high"]=hi
        out.append(q)
    return out

def heterogeneity(projects,min_project_n=20):
    ps=[p for p in projects if int(p["n"])>=min_project_n]
    N=sum(int(p["n"]) for p in ps)
    cols={c:sum(int(p[c+"_count"]) for p in ps) for c in CATEGORIES}
    x=0.0;min_expected=float("inf");lt5=0
    for p in ps:
        for c in CATEGORIES:
            e=int(p["n"])*cols[c]/N;o=int(p[c+"_count"])
            x+=(o-e)**2/e;min_expected=min(min_expected,e);lt5+=e<5
    df=(len(ps)-1)*(len(CATEGORIES)-1)
    return {"min_project_n":min_project_n,"projects":len(ps),"n_commits":N,"chi_square":x,"df":df,"p_value":float(chi2.sf(x,df)),"cramers_v":math.sqrt(x/(N*min(len(ps)-1,len(CATEGORIES)-1))),"min_expected_count":min_expected,"cells_expected_lt5":int(lt5)}

def residuals(projects):
    N=sum(int(p["n"]) for p in projects)
    cols={c:sum(int(p[c+"_count"]) for p in projects) for c in CATEGORIES}
    out=[]
    for p in projects:
        for c in CATEGORIES:
            e=int(p["n"])*cols[c]/N;o=int(p[c+"_count"])
            out.append({"project":p["project"],"category":c,"observed":o,"expected":e,"pearson_residual":(o-e)/math.sqrt(e)})
    return sorted(out,key=lambda r:(-abs(r["pearson_residual"]),r["project"],r["category"]))

def load_projects():
    with (ROOT/"data/derived/project_composition.csv").open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def load_heterogeneity():
    with (ROOT/"data/derived/heterogeneity_results.csv").open(newline="",encoding="utf-8") as f:return list(csv.DictReader(f))
def load_summary():
    return json.loads((ROOT/"results/empirical_summary.json").read_text(encoding="utf-8"))

def validate_bundle():
    ps=load_projects()
    if len(ps)!=54 or sum(int(p["n"]) for p in ps)!=2533:return False
    if sum(int(p["perfective_count"]) for p in ps)!=1022:return False
    if sum(int(p["corrective_count"]) for p in ps)!=685:return False
    if sum(int(p["other_count"]) for p in ps)!=826:return False
    packed={int(r["min_project_n"]):r for r in load_heterogeneity()}
    for cut in (10,20,30,40,50):
        z=heterogeneity(ps,cut);r=packed[cut]
        if abs(float(r["chi_square"])-z["chi_square"])>1e-5:return False
        if abs(float(r["cramers_v"])-z["cramers_v"])>1e-5:return False
        if int(r["cells_expected_lt5"])!=z["cells_expected_lt5"]:return False
    s=load_summary()["headline_metrics"]
    return s["n_commits"]==2533 and s["n_projects"]==54 and abs(s["primary_cramers_v"]-0.301796)<1e-6 and s["source_categories_mutually_exclusive"] is True
