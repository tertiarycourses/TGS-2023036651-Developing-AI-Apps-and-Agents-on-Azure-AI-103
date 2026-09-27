#!/usr/bin/env python3
"""Score learner-provided retrieval rankings; does not call Azure AI Search."""
import json,sys
from pathlib import Path
if len(sys.argv)!=2:raise SystemExit('Usage: python3 evaluate.py rankings.json')
base=Path(__file__).parent
queries=json.loads((base/'data/judged-queries.json').read_text())
docs={d['chunk_id']:d for d in json.loads((base/'data/support-docs.json').read_text())}
rankings=json.loads(Path(sys.argv[1]).read_text())
if set(rankings)!={q['query_id'] for q in queries}:raise SystemExit('FAIL: one ranking per judged query required')
for q in queries:
 ids=rankings[q['query_id']]
 if not isinstance(ids,list) or not ids or len(ids)!=len(set(ids)):raise SystemExit('FAIL: ranking must be a nonempty unique list')
 for id in ids:
  if id not in docs:raise SystemExit('FAIL: unknown chunk '+id)
  if docs[id]['tenant_id']!=q['tenant_id']:raise SystemExit('FAIL: cross-tenant retrieval '+id)
 hits=len(set(ids[:3])&set(q['relevant_chunk_ids']))
 print(q['query_id'],f'precision@3={hits/min(3,len(ids)):.3f}',f'recall@3={hits/len(q["relevant_chunk_ids"]):.3f}')
print('PASS: rankings are source-bound and tenant-filtered')
