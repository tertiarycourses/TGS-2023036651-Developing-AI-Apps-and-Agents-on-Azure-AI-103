#!/usr/bin/env python3
"""Validate grounded, typed text-analysis records against synthetic source messages."""
import json,sys
from pathlib import Path
if len(sys.argv)!=2:raise SystemExit('Usage: python3 validate.py analysis.json')
base=Path(__file__).parent
messages={m['id']:m for m in json.loads((base/'data/messages.json').read_text())}
records=json.loads(Path(sys.argv[1]).read_text())
if not isinstance(records,list) or len(records)!=len(messages):raise SystemExit('FAIL: one record per source message required')
seen=set()
for r in records:
 ident=r.get('message_id'); source=messages.get(ident)
 if not source or ident in seen:raise SystemExit('FAIL: missing/duplicate source ID')
 seen.add(ident)
 for key in ('topic','sentiment','summary','evidence_span','language'):
  if not isinstance(r.get(key),str) or not r[key].strip():raise SystemExit(f'FAIL: {ident} {key}')
 if not isinstance(r.get('entities'),list) or not all(isinstance(x,str) for x in r['entities']):raise SystemExit(f'FAIL: {ident} entities')
 if type(r.get('sensitive_content')) is not bool or type(r.get('review_required')) is not bool:raise SystemExit(f'FAIL: {ident} bool fields')
 if r['evidence_span'] not in source['text']:raise SystemExit(f'FAIL: {ident} evidence is not exact source text')
 if r['language']!=source['language']:raise SystemExit(f'FAIL: {ident} language')
 if source['sensitive'] and (not r['sensitive_content'] or not r['review_required']):raise SystemExit(f'FAIL: {ident} sensitive content needs review')
print('PASS: typed records, exact evidence, language, and sensitive-content review')
