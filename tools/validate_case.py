#!/usr/bin/env python3
"""Validate the synthetic case fixture, instructor mappings and question count.
Not a blind playtest or Insane difficulty certification.
"""
import csv
import re
from datetime import datetime, timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
with (root/'evidence/events.csv').open(newline='',encoding='utf-8') as f:
    rows=list(csv.DictReader(f))
assert len(rows)==40, f'Expected 40 events; got {len(rows)}'
required={'record_id','timestamp_utc','source','host','event_type','details'}
assert set(rows[0])==required, 'Unexpected CSV schema'
ids=[r['record_id'] for r in rows]
assert ids==[f'EV-{i:03d}' for i in range(1,41)], 'Missing, duplicate or unordered IDs'
times=[]
for r in rows:
    assert r['host']=='NB-WS-014'
    t=datetime.fromisoformat(r['timestamp_utc'].replace('Z','+00:00'))
    assert t.tzinfo==timezone.utc
    times.append(t)
assert times==sorted(times), 'CSV timeline out of order'
assert all('CoreShield' not in str(r) for r in rows), 'Protected module reference in fixture'
questions=(root/'student/QUESTIONS.md').read_text(encoding='utf-8')
assert len(re.findall(r'^\\d+\\. ',questions,re.M))==20, 'Question count mismatch'
key=(root/'instructor/ANSWER_KEY.md').read_text(encoding='utf-8')
entries=[]
for line in key.splitlines():
    cells=[cell.strip() for cell in line.strip().split('|')]
    if len(cells)==5 and cells[1].isdigit() and cells[2].startswith('`'):
        entries.append((cells[1], cells[2].strip('`'), cells[3]))
assert len(entries)==20, 'Answer key must contain 20 mappings'
assert [int(x[0]) for x in entries]==list(range(1,21)), 'Question numbers do not align'
lookup={r['record_id']:r['details'] for r in rows}
for number,answer,record in entries:
    assert record in lookup, f'Q{number} references missing record {record}'
    assert answer.lower() in lookup[record].lower(), f'Q{number} answer not present in {record}'
assert 'not a hardware attestation' in ' '.join(r['details'] for r in rows)
print('PASS: 40 ordered synthetic events, 20 grounded question-answer mappings, UTC timestamps, unique IDs.')
