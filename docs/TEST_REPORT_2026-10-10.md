# QUALITY TEST REPORT — The Invisible Intruder: Beneath the Boot

Date: 2026-10-10
Scope: static review of evidence/events.csv, student/QUESTIONS.md, instructor/ANSWER_KEY.md, tools/validate_case.py, docs/QUALITY_GATE.md and the 30 scenario/expediente inventory.
Status: **FAIL / NOT SUBMISSION READY**. No executable GitHub Actions run or blind playtest has been performed.

## Test results
| ID | Test | Result | Finding |
|---|---|---|---|
| T01 | CSV schema | PASS (inspection) | Six required columns are present in the 10-row fixture. |
| T02 | Unique event identifiers | PASS (inspection) | EV-001 through EV-010 are unique. |
| T03 | Timestamp syntax | PASS (inspection) | All 10 timestamps use UTC ISO 8601 Z notation. |
| T04 | Corpus depth | FAIL | Only 10 events in main evidence corpus. |
| T05 | Evidence provenance | FAIL | No individual acquisition records, source exports, SHA-256 manifest, or custody ledger. |
| T06 | Unique solvability of 20 questions | FAIL | Q14 asks which event must be normalized without defining which clock governs each event; Q19 is an open-ended judgment rather than a uniquely gradable answer; Q20 permits multiple reasonable acquisitions. |
| T07 | Time normalization | FAIL | EV-008 says host +120 seconds but does not establish whether each other record uses host time or reference UTC. |
| T08 | TPM authenticity | PASS (labeling only) | EV-005 clearly labels PCR7 as simulated; no verified TPM quote exists. |
| T09 | Firmware compromise claim | PASS (limited) | Existing evidence does not prove malicious firmware flashing; the key avoids claiming it does. |
| T10 | Instructor/student separation | FAIL (release gate) | Instructor answer key is in the same repository tree; must be excluded from student distribution. |
| T11 | Reproducible evidence generation | FAIL | No full artifact generator or reproducibility record. |
| T12 | 30 playable labs | FAIL | 30 scenario briefs and 30 case dossiers exist, but independent evidence sets, validated answers and walkthroughs are missing. |
| T13 | Validator completeness | FAIL | Current validator checks only row count, IDs, host, parseable timestamps and a literal string; it does not check question solvability, event ordering, provenance, custody, release contents, or difficulty. |
| T14 | IP boundary | PASS (reviewed core files only) | CoreShield manuscript or proprietary module code not observed in the five inspected core files. This is NOT a complete repository-wide secrets or IP audit. |
| T15 | Blind investigator playtest | NOT RUN | Requires independent investigator and finished evidence. |

## Prioritized remediation
1. Select one coherent investigation arc from the 30 scenarios; do not equate 30 briefs with 30 HTB Sherlocks.
2. Generate realistic, fully fictional multi-source forensic artifacts with documented provenance and SHA-256 hashes.
3. Fix per-source clock provenance, normalize all timeline events and validate ordering.
4. Rewrite questions to have unique machine-checkable answers and exact record citations.
5. Build a private instructor solution and a separately packaged student release that excludes the answer key.
6. Expand validators to test schema, event relationships, hashes, custody and student release contents.
7. Run blind playtests and adjust difficulty based on measured results.

## Release decision
**BLOCKED.** Insane difficulty and $1,250 maximum payout are goals, not certified outcomes or guaranteed compensation. Keep repository private and do not publish proprietary CoreShield material.
