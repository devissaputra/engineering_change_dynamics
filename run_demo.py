#!/usr/bin/env python3
import json
from research.model import heterogeneity,load_projects,load_summary,residuals,validate_bundle
ps=load_projects()
print(json.dumps(load_summary(),indent=2,ensure_ascii=False))
print(json.dumps({"primary":heterogeneity(ps,20),"sensitivity_n30":heterogeneity(ps,30),"largest_residuals":residuals(ps)[:10]},indent=2))
print("bundle_validation:","PASS" if validate_bundle() else "FAIL")
