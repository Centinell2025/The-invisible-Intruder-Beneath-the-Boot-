#!/usr/bin/env python3
"""Deterministic offline evidence inventory; standard library only.
Never modifies evidence or prints answer keys.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
import sys

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    ap = argparse.ArgumentParser(description="Produce deterministic inventory for extracted Sherlock evidence")
    ap.add_argument("evidence_dir", type=Path, help="Extracted student evidence directory")
    ap.add_argument("--output", type=Path, default=Path("evidence_inventory.csv"))
    args = ap.parse_args()
    root = args.evidence_dir.resolve()
    if not root.is_dir():
        ap.error("evidence_dir must be an existing directory")
    out = args.output.resolve()
    if out == root or root in out.parents:
        ap.error("output must be outside the extracted evidence directory")
    files = sorted((p for p in root.rglob("*") if p.is_file() and not p.is_symlink()), key=lambda p: p.relative_to(root).as_posix())
    if not files:
        ap.error("No evidence files found")
    rows = []
    for path in files:
        relative = path.relative_to(root).as_posix()
        rows.append({"relative_path":relative,"bytes":path.stat().st_size,"sha256":sha256(path),"extension":path.suffix.lower()})
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["relative_path","bytes","sha256","extension"])
        writer.writeheader()
        writer.writerows(rows)
    print(json.dumps({"status":"inventory_created","files":len(rows),"output":str(out)},sort_keys=True))
    return 0

if __name__ == "__main__":
    sys.exit(main())
