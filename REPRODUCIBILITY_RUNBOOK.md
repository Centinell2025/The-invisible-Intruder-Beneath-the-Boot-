# Reproducibility — executable workflow

This page connects the public reproducibility protocol to executable, standard-library-only checks. It does **not** publish instructor answers.

## 1. Verify student ZIP

```bash
python3 tools/validate_student_package.py
```

This runs public archive metadata checks. A password-protected archive requires the password supplied locally via `SHERLOCK_ZIP_PASSWORD` for a complete manifest verification; an incomplete check is **not** a pass. See [PACKAGE_VALIDATION.md](PACKAGE_VALIDATION.md).

## 2. Extract into a working directory

Use a trusted ZIP extractor. Preserve the downloaded archive unchanged and never extract over the source directory. Obtain the password from the authorized instructor/submission channel.

## 3. Build a deterministic evidence inventory

```bash
python3 tools/build_evidence_inventory.py ./extracted/evidence --output ./review_output/evidence_inventory.csv
```

The command lists each extracted evidence file, size and SHA-256 digest in stable path order. It writes **outside** the extracted evidence directory. Save the resulting CSV privately with the review notes.

## 4. Create a private evidence-to-answer trace

Copy [ANSWER_TRACE_TEMPLATE.csv](ANSWER_TRACE_TEMPLATE.csv) into a **private local** working directory. Complete all 20 entries, recording exact source records, reasoning and an independent review outcome. Never push the completed file to this public repository.

```bash
python3 tools/check_answer_trace.py ./private_review/answer_trace.csv --evidence-dir ./extracted
```

Exit code 0 means the required fields and evidence paths are present and all entries are marked reviewed. It **does not prove** that answers are correct or that the reviewer was independent. Exit code 2 means incomplete evidence trace.

## 5. Independent acceptance

A reviewer who has never seen the key must reproduce the answers from student materials alone. Record the reviewer's findings in restricted materials and resolve ambiguous questions before claiming complete reproducibility.

## Limits and status

- The repository now contains an inventory tool and a trace-completeness checker, but **neither tool has been demonstrated against a freshly extracted student ZIP in this update**.
- All 20 answers still require independent verification.
- This is synthetic forensic training; simulated boot observations do not constitute hardware TPM attestation.
- Do not publish the private trace, solution keys or instructor walkthrough.
