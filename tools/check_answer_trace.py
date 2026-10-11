#!/usr/bin/env python3
"""Validate a private 20-question evidence trace without disclosing answers."""
import argparse
import csv
from pathlib import Path
import re
import sys

REQUIRED = ["question_id","question_text","answer_private","primary_artifact","record_identifier","secondary_artifact","secondary_record","timestamp_source","timestamp_normalization","reasoning_private","alternative_interpretation","reviewer_result","reviewer_notes"]

def main():
    p = argparse.ArgumentParser(description="Check completeness of private evidence citations")
    p.add_argument("trace_csv", type=Path)
    p.add_argument("--evidence-dir", type=Path)
    args = p.parse_args()
    with args.trace_csv.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None or any(k not in reader.fieldnames for k in REQUIRED):
            print("FAIL: Missing required CSV columns", file=sys.stderr)
            return 1
        rows = list(reader)
    expected = [f"Q{i:02d}" for i in range(1,21)]
    actual = [r["question_id"].strip() for r in rows]
    if actual != expected:
        print("FAIL: Must contain exactly Q01 through Q20 in order, with no duplicates",file=sys.stderr)
        return 1
    incomplete = []
    invalid_paths = []
    for row in rows:
        q = row["question_id"]
        for col in ["question_text","answer_private","primary_artifact","record_identifier","reasoning_private","reviewer_result"]:
            if not (row.get(col) or "").strip():
                incomplete.append(f"{q}:{col}")
        if row["reviewer_result"].strip().lower() != "pass":
            incomplete.append(f"{q}:independent_review_not_passed")
        if args.evidence_dir and row["primary_artifact"].strip():
            root = args.evidence_dir.resolve()
            candidate = (root / row["primary_artifact"].strip()).resolve()
            if not candidate.is_relative_to(root) or not candidate.is_file():
                invalid_paths.append(q)
    print(f"Questions: {len(rows)}/20; missing or unapproved fields: {len(incomplete)}; missing evidence paths: {len(invalid_paths)}")
    if incomplete:
        print("Incomplete identifiers: "+", ".join(incomplete))
    if invalid_paths:
        print("Invalid primary evidence path for: "+", ".join(invalid_paths))
    if incomplete or invalid_paths:
        return 2
    print("PASS: Private trace has 20 reviewed entries with source references. This does not prove correctness or independent blind solving.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
