#!/usr/bin/env python3
"""Validate minimal synthetic scaffold; not an Insane-readiness certification."""
import csv
from datetime import datetime
from pathlib import Path
p=Path(__file__).resolve().parents[1]/"evidence"/"events.csv"
with p.open(newline="",encoding="utf-8") as f:
    rows=list(csv.DictReader(f))
assert len(rows)==10, f"Expected 10 records, got {len(rows)}"
ids=[r["record_id"] for r in rows]
assert len(ids)==len(set(ids)), "Duplicate record IDs"
for r in rows:
    assert r["host"]=="NB-WS-014"
    datetime.fromisoformat(r["timestamp_utc"].replace("Z","+00:00"))
assert all("CoreShield" not in str(r) for r in rows), "Proprietary manuscript data must not be embedded"
print("PASS: 10 synthetic records parse, IDs unique, timestamps valid.")
