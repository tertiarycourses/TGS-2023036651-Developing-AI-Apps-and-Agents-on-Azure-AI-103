#!/usr/bin/env python3
"""Validate bounded synthetic agent tool traces; no cloud call is performed."""
import json,sys
from pathlib import Path
if len(sys.argv)!=2:raise SystemExit('Usage: python3 validate.py traces.json')
records=json.loads(Path(sys.argv[1]).read_text())
if not isinstance(records,list) or len(records)<2:raise SystemExit('FAIL: allowed and denied traces required')
outcomes=set()
for t in records:
 if t.get('tool') not in ('search_knowledge','create_ticket'):raise SystemExit('FAIL: unapproved tool')
 if not isinstance(t.get('arguments'),dict) or not t.get('tenant_id'):raise SystemExit('FAIL: missing typed arguments or tenant')
 if not isinstance(t.get('turns'),int) or t['turns']>5 or t['turns']<1:raise SystemExit('FAIL: turn budget')
 if t['tool']=='search_knowledge' and t['arguments'].get('tenant_id')!=t['tenant_id'] and t.get('outcome')!='denied':raise SystemExit('FAIL: cross-tenant search allowed')
 if t['tool']=='create_ticket' and t.get('approval')!='approved' and t.get('outcome')!='denied':raise SystemExit('FAIL: unapproved ticket action')
 if t.get('outcome')=='allowed' and t['tool']=='search_knowledge' and not t.get('citation'):raise SystemExit('FAIL: no citation')
 outcomes.add(t.get('outcome'))
if outcomes!={'allowed','denied'}:raise SystemExit('FAIL: both allowed and denied cases required')
print('PASS: tool allowlist, tenant isolation, approvals, budget, and citations')
