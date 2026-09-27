#!/usr/bin/env python3
"""Export the current Learner Guide DOCX as a learner-readable Markdown mirror."""
from pathlib import Path
from docx import Document
from docx.oxml.ns import qn
from docx.table import Table
from docx.text.paragraph import Paragraph

root = Path(__file__).resolve().parents[1]
source = root / 'courseware' / 'LG-Developing AI Apps and Agents on Azure (AI-103).docx'
target = root / 'courseware' / 'LG-Developing AI Apps and Agents on Azure (AI-103).md'
doc = Document(source)
lines = ['# Developing AI Apps and Agents on Azure (AI-103) — Learner Guide', '', 'Course code: TGS-2023036651 · Version 4.0', '']
for child in doc.element.body.iterchildren():
    if child.tag == qn('w:p'):
        p = Paragraph(child, doc)
        value = p.text.strip()
        if not value:
            continue
        style = p.style.name or ''
        if style.startswith('Heading'):
            try:
                depth = min(6, int(style.split()[-1]))
            except ValueError:
                depth = 2
            lines.extend([f"{'#' * depth} {value}", ''])
        elif style == 'List Bullet':
            lines.append(f'- {value}')
        elif style == 'List Number':
            lines.append(f'1. {value}')
        else:
            lines.extend([value, ''])
    elif child.tag == qn('w:tbl'):
        table = Table(child, doc)
        rows = [[c.text.strip().replace('|', '\\|').replace('\n', ' / ') for c in row.cells] for row in table.rows]
        if rows:
            lines.append('| ' + ' | '.join(rows[0]) + ' |')
            lines.append('| ' + ' | '.join(['---'] * len(rows[0])) + ' |')
            lines.extend('| ' + ' | '.join(row) + ' |' for row in rows[1:])
            lines.append('')
target.write_text('\n'.join(lines).rstrip() + '\n', encoding='utf-8')
print(target)
