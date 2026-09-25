#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,html
from pathlib import Path
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
def t(x,y,s,z=16,w="400",a="start"):return f'<text x="{x}" y="{y}" font-family="Arial, sans-serif" font-size="{z}" font-weight="{w}" text-anchor="{a}">{html.escape(str(s))}</text>'
def o(w,h):return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><rect width="100%" height="100%" fill="white"/>'
def read(name):
    with (ROOT/"data/derived"/name).open(encoding="utf-8") as f:return list(csv.DictReader(f))

def architecture():
    p=[o(1200,420),t(45,50,"Cross-Project Engineering Change Heterogeneity",28,"700"),t(45,82,"Zenodo ground truth → three-category coding → project composition → heterogeneity + sensitivity → bounded interpretation",14)]
    labs=[("Source","2,533 commits"),("Taxonomy","3 categories"),("Projects","54 estimates"),("Inference","χ² + Cramér V"),("Sensitivity","n thresholds")]
    for i,(a,b) in enumerate(labs):
        x=35+i*232;p+=[f'<rect x="{x}" y="145" width="185" height="120" rx="12" fill="#f7f7f7" stroke="#333"/>',t(x+92.5,185,a,17,"700","middle"),t(x+92.5,218,b,14,"400","middle")]
        if i<4:p.append(f'<line x1="{x+185}" y1="205" x2="{x+222}" y2="205" stroke="#222" stroke-width="2"/>')
    return "".join(p+["</svg>"])

def method():
    steps=["Map source flags to perfective, corrective, or other; reject impossible both=True rows.","Compute complete 54-project category counts, shares, and 95% Wilson intervals.","Use n≥20 projects for primary χ² inference so all expected counts exceed 5.","Repeat at n≥30/40/50 and inspect Pearson residuals without individual significance claims."]
    p=[o(1200,520),t(45,50,"Method",28,"700")]
    for i,s in enumerate(steps,1):
        y=105+(i-1)*95;p+=[f'<circle cx="75" cy="{y+30}" r="23" fill="#f0f0f0" stroke="#333"/>',t(75,y+36,i,16,"700","middle"),f'<rect x="120" y="{y}" width="1020" height="62" rx="10" fill="#fafafa" stroke="#444"/>',t(145,y+38,s,14)]
    return "".join(p+["</svg>"])

def composition():
    rows=read("category_summary.csv");p=[o(1050,560),t(40,45,"Pooled maintenance-intent composition",26,"700"),t(40,72,"2,533 manually classified commits",14)]
    base=455
    for i,r in enumerate(rows):
        v=float(r["share"]);x=150+i*280;h=v*700;y=base-h
        p+=[f'<rect x="{x}" y="{y}" width="150" height="{h}" fill="#555" fill-opacity="{0.78-i*0.12}"/>',t(x+75,y-12,f"{v*100:.1f}%",16,"700","middle"),t(x+75,base+30,r["category"].title(),14,"700","middle")]
    return "".join(p+["</svg>"])

def hetero():
    rows=sorted(read("project_composition.csv"),key=lambda r:float(r["perfective_share"]))
    p=[o(1200,680),t(40,45,"Project-level perfective share",26,"700"),t(40,72,"All 54 projects; dot position is observed share. Small-n uncertainty is available in the released table.",14)]
    left,right,top,bottom=90,1140,110,610
    for i,r in enumerate(rows):
        x=left+float(r["perfective_share"])*(right-left);y=top+i*(bottom-top)/(len(rows)-1)
        p.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="4.2" fill="#444"/>')
    for val in (0,.2,.4,.6,.8,1.0):
        x=left+val*(right-left);p+=[f'<line x1="{x}" y1="{top-10}" x2="{x}" y2="{bottom+10}" stroke="#ddd"/>',t(x,bottom+42,f"{val:.1f}",12,"400","middle")]
    p.append(t(600,665,"Perfective share",14,"700","middle"))
    return "".join(p+["</svg>"])

def sensitivity():
    rows=read("heterogeneity_results.csv");p=[o(1050,540),t(40,45,"Heterogeneity effect is stable after small-sample filtering",25,"700"),t(40,72,"Cramér's V for project×category composition",14)]
    left,base=120,430
    for i,r in enumerate(rows):
        v=float(r["cramers_v"]);x=150+i*170;h=v*900;y=base-h
        p+=[f'<rect x="{x}" y="{y}" width="95" height="{h}" fill="#666" fill-opacity="{0.82-i*0.08}"/>',t(x+47.5,y-10,f"{v:.3f}",13,"700","middle"),t(x+47.5,base+26,f'n≥{r["min_project_n"]}',12,"700","middle")]
    return "".join(p+["</svg>"])

def evaluation():
    p=[o(1200,500),t(45,50,"Evidence boundary",28,"700")]
    blocks=[("Supported","Maintenance-intent composition differs materially across sampled Apache projects."),("Robustness","Cramér's V stays near 0.30 after excluding increasingly small project samples."),("Taxonomy","Perfective/corrective/other are source categories—not two independent binary outcomes."),("Boundary","Commit intent is not requirements churn, design propagation, rework cost, or causal project performance.")]
    for i,(a,b) in enumerate(blocks):
        y=90+i*92;p+=[f'<rect x="55" y="{y}" width="1090" height="68" rx="10" fill="#f8f8f8" stroke="#444"/>',t(80,y+27,a,16,"700"),t(80,y+51,b,14)]
    return "".join(p+["</svg>"])

def render(out):
    out.mkdir(parents=True,exist_ok=True)
    fs={"architecture.svg":architecture(),"method.svg":method(),"category_composition.svg":composition(),"project_heterogeneity.svg":hetero(),"sensitivity.svg":sensitivity(),"evaluation.svg":evaluation()}
    for n,c in fs.items():ET.fromstring(c);(out/n).write_text(c,encoding="utf-8")
    return fs
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--out-dir",default=str(ROOT/"assets"));a=ap.parse_args();print("generated_figures:",len(render(Path(a.out_dir))))
if __name__=="__main__":main()
