#!/usr/bin/env python3
"""Student archive release gate. Standard-library only; never prints answers."""
import argparse
import hashlib
import os
from pathlib import Path, PurePosixPath
import re
import sys
import zipfile

def fail(message):
    raise ValueError(message)

def main():
    parser = argparse.ArgumentParser(description="Validate Sherlock student ZIP before distribution")
    parser.add_argument("--archive", default="downloads/The_Invisible_Intruder_HTB_Student.zip")
    parser.add_argument("--password-env", default="SHERLOCK_ZIP_PASSWORD")
    args = parser.parse_args()
    archive = Path(args.archive)
    if not archive.is_file():
        fail(f"Archive missing: {archive}")
    digest = hashlib.sha256(archive.read_bytes()).hexdigest()
    print(f"Archive SHA256: {digest}")
    with zipfile.ZipFile(archive) as z:
        bad = z.testzip() if not any(i.flag_bits & 1 for i in z.infolist()) else None
        if bad:
            fail(f"Corrupt archive member: {bad}")
        files = [i for i in z.infolist() if not i.is_dir()]
        if not files:
            fail("Empty student archive")
        for i in files:
            p = PurePosixPath(i.filename.replace("\\", "/"))
            if p.is_absolute() or ".." in p.parts or "\x00" in i.filename:
                fail(f"Unsafe archive member: {i.filename!r}")
            if i.file_size > 250 * 1024 * 1024:
                fail(f"Oversized archive member: {i.filename}")
        names = [i.filename.replace("\\", "/") for i in files]
        lowered = [x.lower() for x in names]
        if len(set(lowered)) != len(lowered):
            fail("Duplicate or case-colliding archive member paths")
        forbidden = re.compile(r"(?:^|[/_.-])(answer.?key|walkthrough|instructor|solution|grading.?key|private.?notes)(?:[/_.-]|$)", re.I)
        suspicious = [x for x in names if forbidden.search(x)]
        if suspicious:
            fail("Possible instructor-only filenames: " + ", ".join(suspicious))
        required = ("QUESTIONS.md", "EVIDENCE_GUIDE.md", "SHA256SUMS.txt")
        for filename in required:
            if not any(x == filename or x.endswith("/" + filename) for x in names):
                fail(f"Required file missing: {filename}")
        print(f"PASS: {len(files)} safe archive entries; required student documents present; no suspicious instructor filenames")
        pwd = os.environ.get(args.password_env)
        if not pwd:
            print(f"NOT VERIFIED: encrypted contents, question count and evidence hashes. Set {args.password_env} and rerun.")
            return 2
        decoded = {}
        for i in files:
            decoded[i.filename.replace("\\", "/")] = z.read(i, pwd=pwd.encode())
        manifest_path = next(x for x in names if x.endswith("SHA256SUMS.txt"))
        root = manifest_path[:-len("SHA256SUMS.txt")]
        manifest = decoded[manifest_path].decode("utf-8-sig")
        verified = 0
        for line in manifest.splitlines():
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            match = re.fullmatch(r"([0-9a-fA-F]{64})\s+\*?(.+)", line.strip())
            if not match:
                fail("Invalid SHA256SUMS entry format")
            expected, relpath = match.groups()
            key = root + relpath.lstrip("./")
            if key not in decoded:
                fail(f"Manifest references missing file: {relpath}")
            actual = hashlib.sha256(decoded[key]).hexdigest()
            if actual.lower() != expected.lower():
                fail(f"Evidence hash mismatch: {relpath}")
            verified += 1
        if not verified:
            fail("Manifest has no entries")
        qpath = next(x for x in names if x.endswith("QUESTIONS.md"))
        qtext = decoded[qpath].decode("utf-8-sig")
        print(f"PASS: {verified} manifest hashes verified; QUESTIONS.md readable ({len(qtext)} characters)")
        print("MANUAL GATES: verify 20 unique answers, no embedded solution values, blind playtest and private instructor delivery")
        return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, zipfile.BadZipFile, RuntimeError, UnicodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
