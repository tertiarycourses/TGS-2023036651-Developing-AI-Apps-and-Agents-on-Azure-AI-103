#!/usr/bin/env python3
"""Validate synthetic extraction provenance and human-review threshold."""
import json,sys
from pathlib import Path
if len(sys.argv)!=2:raise SystemExit('Usage: python3 validate.py extraction.json')
base=Path(__file__).parent
source=json.loads((base/'data/maintenance-record.json').read_text())
out=json.loads(Path(sys.argv[1]).read_text())
if out.get('document_id')!=source['document_id']:raise SystemExit('FAIL: wrong document ID')
if not isinstance(out.get('analyzer_version'),str) or not out['analyzer_version']:raise SystemExit('FAIL: analyzer version required')
fields=out.get('fields') or {}
if set(fields)!=set(source['expected_fields']):raise SystemExit('FAIL: expected fields missing or extra')
low=False
for name,item in fields.items():
 if not isinstance(item.get('value'),str) or not item['value']:raise SystemExit('FAIL: missing value '+name)
 if not isinstance(item.get('confidence'),(float,int)) or not 0<=item['confidence']<=1:raise SystemExit('FAIL: confidence '+name)
 if not isinstance(item.get('source_span'),str) or item['source_span'] not in source['source_text']:raise SystemExit('FAIL: source span '+name)
 low|=item['confidence']<0.8
if type(out.get('review_required')) is not bool or out['review_required']!=low:raise SystemExit('FAIL: review threshold decision')
print('PASS: schema, source provenance, and low-confidence review')
