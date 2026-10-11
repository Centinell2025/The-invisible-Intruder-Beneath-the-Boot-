# LAB-10 — Boot Driver

**Track:** The Invisible Intruder — Beneath the Boot  
**Difficulty goal:** advanced DFIR (not independently rated)  
**Environment:** fictional Northbridge Systems; offline synthetic training only.

## Investigation objective
Assess an unfamiliar boot-start driver using file metadata and trust records.

## Required evidence to develop
- driver list
- catalog signatures
- baseline

## Analyst tasks
1. Verify artifact provenance, identifiers, and UTC timestamp format.
2. Reconstruct relevant events and account for known clock offsets.
3. Correlate at least two independent sources before reaching a conclusion.
4. Record alternative benign explanations and evidence limitations.
5. Produce a finding with artifact citations and confidence level.

## Primary challenge
Which driver warrants verification?

## Expected deliverable
A one-page investigation note with a timeline, supporting record IDs, hypothesis comparison, and next acquisition step. **Do not infer a firmware compromise from an alert alone.**

## Development status
**Scenario specification only — not a playable or validated lab yet.** Requires dedicated synthetic artifacts, unique answer keys, reproducibility checks, and blind testing before submission.

## Intellectual-property boundary
No private CoreShield book passages, proprietary source, internal module design, credentials, or real-world IP addresses are used.
