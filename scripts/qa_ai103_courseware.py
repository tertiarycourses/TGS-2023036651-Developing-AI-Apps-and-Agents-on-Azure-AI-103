#!/usr/bin/env python3
"""Structural/alignment QA. Rendered visual QA is performed separately."""

import csv, json, re
from pathlib import Path
from statistics import mean, median
from docx import Document
from pptx import Presentation
from pypdf import PdfReader

R=Path(__file__).resolve().parents[1]; C=R/"courseware"; A=R/"assessment"; L=R/"labs"
T="Developing AI Apps and Agents on Azure (AI-103)"; V="5.0"; CODE="TGS-2023036651"
P=C/f"{T}-v{V}.pptx"; PP=C/f"{T}-v{V}.pdf"; LG=C/f"LG-{T}.docx"; LGP=C/f"LG-{T}.pdf"; LP=C/f"LP-{T}.docx"; LPP=C/f"LP-{T}.pdf"
M=json.loads((C/"slide_map.json").read_text()); Q=[]
def ck(sec,name,ok,detail=""): Q.append((sec,name,bool(ok),detail))
def dt(p):
 d=Document(p); z=[x.text for x in d.paragraphs]
 for t in d.tables:
  for r in t.rows: z.append(" | ".join(c.text for c in r.cells))
 return "\n".join(z)
def toc(p):
 d=Document(p); return "TOC \\o" in d._element.xml and "updateFields" in d.settings._element.xml

prs=Presentation(P); texts=["\n".join(x.text for x in s.shapes if hasattr(x,"text") and x.text.strip()) for s in prs.slides]; alltext="\n".join(texts); counts=[len(s.shapes) for s in prs.slides]
ck("A PPT","PPTX/PDF exist",P.exists() and PP.exists())
ck("A PPT","2-day scale",len(prs.slides)>=200,f"{len(prs.slides)} slides")
ck("A PPT","Single matching cover version",texts[0].count("Version 5.0")==1 and CODE in texts[0])
ck("A PPT","Two completed trainer profiles","TRAINING TEAM PROFILE" in alltext and "Tertiary Infotech Academy Trainer" in alltext and "Dr. Alfred Ang" in alltext and "Complete before class" not in alltext and "________________" not in alltext)
ck("A PPT","Briefing before assessment",M["admin_briefing"]<M["admin_assessment"])
ck("A PPT","TRAQOM front and end","TRAQOM" in texts[M["admin_attendance"]-1] and "TRAQOM" in texts[M["closing_attendance"]-1])
ck("A PPT","Closing block order",M["closing_assessment"]<M["closing_flow"]<M["closing_attendance"]<M["closing_thanks"])
ck("A PPT","No click-by-click slides","DETAILED LAB GUIDE" not in alltext and not re.search(r"Lab \d+ Step \d+",alltext))
ck("A PPT","Editable native charts",sum(x.has_chart for s in prs.slides for x in s.shapes)>=10)
ck("A PPT","ImageGen visuals",sum(x.shape_type==13 for s in prs.slides for x in s.shapes)>=3)
ck("A PPT","All transitions",sum(s._element.find("{http://schemas.openxmlformats.org/presentationml/2006/main}transition") is not None for s in prs.slides)==len(prs.slides))
overflow=[(i,x.name) for i,s in enumerate(prs.slides,1) for x in s.shapes if x.top is not None and x.height is not None and x.top+x.height>prs.slide_height]
ck("A PPT","Zero shape-bound overflow",not overflow,str(overflow[:5]))
ck("A PPT","Visual density",mean(counts)>=24,f"mean {mean(counts):.1f}; median {median(counts):.1f}; max {max(counts)}")
ck("A PPT","Current AI-103 scope","AI-103" in alltext and "16 Apr 2026" in alltext)

anchors=[]; types={"image":"MODEL","arch":"ARCH","flow":"ARCH","contract":"CONFIG","code":"CODE","chart":"MODEL","decision":"MODEL","failure":"EVIDENCE","activity":"EVIDENCE","verify":"EVIDENCE"}
for key,n in sorted(M.items(),key=lambda x:x[1]):
 if re.match(r"topic\d+_(image|arch|flow|contract|code|chart|decision|failure|source|inputs|sourcecode\d|sourceflow|assets|evidence)$",key) or re.match(r"lab\d+_(activity|verify)$",key):
  suffix=key.rsplit("_",1)[-1]
  anchor=types.get(suffix,"CODE" if suffix.startswith("sourcecode") else "EVIDENCE")
  anchors.append((n,key,anchor,texts[n-1].splitlines()[0] if texts[n-1] else ""))
with (C/f"QA-TECHNICAL-ANCHORS-v{V}.csv").open("w",newline="",encoding="utf-8") as f:
 w=csv.writer(f,lineterminator="\n"); w.writerow(["slide","key","anchor","title"]); w.writerows(anchors)
content=[n for n,kind in enumerate(prs.slides,1) if n in [x[0] for x in anchors]]
ck("A PPT","Zero unanchored instructional slides",len(anchors)>=170 and len(set(content))==len(anchors),f"{len(anchors)} anchored; 0 GENERAL")

lgt,lpt=dt(LG),dt(LP)
ck("C LP","DOCX/PDF",LP.exists() and LPP.exists()); ck("C LP","Cover/version",CODE in lpt and "DOCUMENT VERSION CONTROL RECORD" in lpt and "5.0" in lpt); ck("C LP","Live TOC",toc(LP)); ck("C LP","Actual slide map",all(f"Slide {M[f'lab{i:02d}_activity']}" in lpt for i in range(1,11))); ck("C LP","Assessment 60+60","60 minutes" in lpt and "A1–A6" in lpt)
ck("D LG","DOCX/PDF",LG.exists() and LGP.exists()); ck("D LG","Cover/version",CODE in lgt and "DOCUMENT VERSION CONTROL RECORD" in lgt and "5.0" in lgt); ck("D LG","Live TOC",toc(LG)); ck("D LG","Ten detailed labs",all(f"Lab {i:02d}" in lgt for i in range(1,11)) and lgt.count("Troubleshooting Checklist")>=10 and lgt.count("Unchanged MicrosoftLearning exercise instructions")>=10); ck("D LG","LG Markdown mirror",len(list(C.glob("LG-*.md")))==1 and "Lab 10" in next(C.glob("LG-*.md")).read_text())
dirs=sorted(x for x in L.glob("lab-*") if x.is_dir()); ck("E Labs","Ten individual lab folders",len(dirs)==10,str(len(dirs))); ck("E Labs","README per lab",all((x/"README.md").exists() for x in dirs)); ck("E Labs","One hands-on root",not (R/"activities").exists())
source_manifest=json.loads((L/"OFFICIAL-SOURCE-MANIFEST.json").read_text())
import hashlib
source_errors=[]
for repo,entry in source_manifest.items():
 for path,digest in entry["files"].items():
  p=L/"official"/repo/path
  if not p.exists() or hashlib.sha256(p.read_bytes()).hexdigest()!=digest:source_errors.append(str(p))
ck("E Labs","Exact pinned MicrosoftLearning learner source",len(source_manifest)==5 and sum(len(x["files"]) for x in source_manifest.values())==453 and not source_errors,f"{len(source_manifest)} repos; {sum(len(x['files']) for x in source_manifest.values())} files; errors {len(source_errors)}")
ck("E Labs","Trainer solutions withheld",sum(x.get("trainer_solution_file_count_private",0) for x in source_manifest.values())==68 and not any(p.is_file() and any(x.lower() in ("solution","solutions") for x in p.relative_to(L/"official").parts) for p in (L/"official").rglob("*")))
ck("E Labs","MIT licenses",all((L/"official"/repo/"LICENSE").exists() for repo in source_manifest))

af=sorted(A.glob("*.docx")); cand=[x for x in af if not x.name.startswith("Answer")]
ck("B Assessment","Four DOCX",len(af)==4); ck("B Assessment","WA + PP candidates",len(cand)==2 and any(x.name.startswith("WA ") for x in cand) and any(x.name.startswith("PP ") for x in cand))
wa=dt(next(x for x in af if x.name.startswith("WA "))); pp=dt(next(x for x in af if x.name.startswith("PP "))); wak=dt(next(x for x in af if x.name.startswith("Answer to WA"))); ppk=dt(next(x for x in af if x.name.startswith("Answer to PP")))
ck("B Assessment","WA K1-K6",len(re.findall(r"Question \d+ \(K\d\)",wa))==6 and all(x in wa+wak for x in [f"K{i}" for i in range(1,7)])); ck("B Assessment","PP A1-A6",len(re.findall(r"Task \d+ \(A\d\)",pp))==6 and all(x in pp+ppk for x in [f"A{i}" for i in range(1,7)])); ck("B Assessment","60-minute papers","60 minutes" in wa and "60 minutes" in pp); ck("B Assessment","Open-ended only","multiple choice" not in (wa+pp).lower()); ck("B Assessment","LMS link","lms-tms.tertiaryinfotech.com" in wa and "lms-tms.tertiaryinfotech.com" in pp); ck("B Assessment","Git-ignored","/assessment/" in (R/".gitignore").read_text())

ck("F Files","Current PDF pages",len(PdfReader(str(PP)).pages)==len(prs.slides) and len(PdfReader(str(LGP)).pages)>10 and len(PdfReader(str(LPP)).pages)>3); ck("F Files","One live deck",len(list(C.glob(f"{T}-v*.pptx")))==1)
secs=["A PPT","B Assessment","C LP","D LG","E Labs","F Files"]; out=["# AI-103 Courseware QA v5.0","","Structural/alignment audit. Rendered visual audit is recorded separately.",""]
for sec in secs:
 rows=[x for x in Q if x[0]==sec]; fail=[x for x in rows if not x[2]]; out.append(f"## {sec}: {'FAIL' if fail else 'PASS'}")
 for _,n,ok,d in rows: out.append(f"- {'PASS' if ok else 'FAIL'} — {n}"+(f" — {d}" if d else ""))
 out.append("")
out += ["## K/A Coverage","","| Code | Instrument | Source |","| --- | --- | --- |"]
for i,slide in enumerate([M["topic01_contract"],M["topic10_chart"],M["topic04_decision"],M["topic08_contract"],M["topic05_chart"],M["topic09_image"]],1): out.append(f"| K{i} | WA Question {i} | Trainer slide {slide} |")
for i,(lab,slide) in enumerate([("Lab 03",M["lab03_activity"]),("Lab 10",M["lab10_activity"]),("Labs 06 and 07",M["lab06_activity"]),("Labs 04 and 05",M["lab05_activity"]),("Lab 09",M["lab09_activity"]),("Lab 10",M["lab10_activity"])],1): out.append(f"| A{i} | PP Task {i} | {lab}; trainer slide {slide} |")
fail=[x for x in Q if not x[2]]; out += ["",f"## Overall: {'FAIL' if fail else 'PASS (structural/alignment)'}"]
(C/f"QA-REPORT-v{V}.md").write_text("\n".join(out),encoding="utf-8"); print("\n".join(out)); raise SystemExit(bool(fail))
