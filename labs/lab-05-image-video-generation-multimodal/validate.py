#!/usr/bin/env python3
"""Validate a learner's review record for the synthetic AI-103 vision exercise."""
import json,sys
from pathlib import Path
if len(sys.argv)!=2: raise SystemExit('Usage: python3 validate.py review.json')
review=json.loads(Path(sys.argv[1]).read_text())
required={'model_version':str,'approved':bool,'unsupported_claims':list,'missing_attributes':list,'alt_text_issue':str,'human_reviewer':str}
for key,kind in required.items():
 if key not in review or type(review[key]) is not kind:raise SystemExit(f'FAIL: {key} must be {kind.__name__}')
brief=json.loads((Path(__file__).parent/'data/product-brief.json').read_text())
sample=json.loads((Path(__file__).parent/'data/sample-output.json').read_text())
prohibited=set(brief['prohibited_claims'])&set(sample['claims'])
if prohibited and not prohibited.issubset(set(review['unsupported_claims'])):raise SystemExit('FAIL: prohibited claim was not recorded')
if prohibited and review['approved']:raise SystemExit('FAIL: sample with prohibited claim cannot be approved')
if not review['human_reviewer'].strip():raise SystemExit('FAIL: reviewer is required')
print('PASS: review schema, prohibited-claim decision, and reviewer')
