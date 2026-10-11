# 115-event Sherlock review package

This branch reserves a review track for a **single** Sherlock, *The Invisible Intruder — Beneath the Boot*. The complete 115-event offline package was assembled and structurally tested as a **separate local deliverable**, not uploaded to this branch. The repository's existing 40-event case remains a distinct preliminary fixture and must not be mistaken for the 115-event release.

Offline review package components:
- Student ZIP: 115 synthetic correlated events, 20 investigation questions, synthetic attestation and change-control artifacts, SHA-256 evidence manifest.
- Restricted instructor ZIP: 20-answer key, walkthrough, QA report.
- Full private review ZIP: combined source materials.

Automated structural checks passed: UTC timestamp format, chronological ordering, 20 question and answer records, evidence-manifest hashes, ZIP integrity, and exclusion of instructor answers from student ZIP.

**Not yet HTB submission ready:** independent blind playtest and external difficulty validation remain outstanding. No real firmware image, verified hardware TPM quote, or proprietary CoreShield module code is included.
