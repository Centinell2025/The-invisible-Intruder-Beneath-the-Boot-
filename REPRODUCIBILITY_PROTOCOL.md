# Reproducible Investigation Protocol

**Scenario:** The Invisible Intruder — Beneath the Boot. **Organization:** fictional Northbridge Systems. **Purpose:** defensible, repeatable analysis of synthetic DFIR evidence.

## Definition of reproducibility

A result is reproducible only when a second analyst, using the unchanged student archive and documented assumptions, derives the same conclusion from identifiable source records. Documentation alone is not proof of reproducibility.

## Preconditions

1. Preserve the original downloaded ZIP and record its SHA-256 digest.
2. Obtain the archive password through the authorized submission channel; never put it in a public file.
3. Follow [PACKAGE_VALIDATION.md](PACKAGE_VALIDATION.md) to verify the archive and its SHA-256 manifest.
4. Record operating system, Python version, ZIP digest, investigation start date, and any parsing tools used.
5. Work on extracted copies, never edit source evidence.

## Deterministic investigation workflow

### Step 1 — Inventory

Record each extracted evidence filename, byte size, SHA-256 hash, format, clock domain, timestamp field, and expected event identifier. If an identifier is absent, cite the exact file and line/row number; note that row numbers may change if a file is sorted.

### Step 2 — Time normalization

- Identify each source clock and the documented reference for it before correlating events.
- Convert to a single UTC timeline only when the offset is supported by evidence.
- Record the original timestamp, original timezone or offset, normalization formula and resulting UTC time.
- Preserve contradictory clock references rather than silently choosing one.
- If a source cannot be normalized reliably, label the timestamp uncertain and avoid strict ordering claims.

### Step 3 — Cross-source correlation

For every significant claim, document the primary record and any corroboration: event/logon IDs, process GUIDs, host/user identities, task names, DNS queries, network endpoints, file paths or simulated boot-state changes. Separate direct observations from interpretations.

### Step 4 — Question-by-question trace

Use [ANSWER_TRACE_TEMPLATE.csv](ANSWER_TRACE_TEMPLATE.csv) as a **private working template**. The public template contains no solutions. For each of the 20 questions, privately record:
- Question identifier and exact question wording
- Answer and accepted equivalent forms
- Exact source path and record/line ID
- Secondary corroboration or explicit lack thereof
- Timestamp normalization assumption
- Reasoning, counterexample and uncertainty
- Independent reviewer result (pass, ambiguous, fail)

Never commit completed answer traces or instructor walkthroughs to the public repository.

### Step 5 — Blind solve

Give a fresh analyst only the student ZIP, password and public instructions. Record time to completion, ambiguous questions, missing artifacts, and whether each response can be justified with a precise evidence citation. Compare with a restricted instructor answer key only after the blind solve.

## Acceptance criteria

- [ ] All 14 evidence-file hashes verified in a fresh run (previous QA reports 14; rerun required)
- [ ] Every one of the 20 questions has at least one exact artifact/record citation
- [ ] All derived times document the source clock and normalization rule
- [ ] Every answer has a unique, testable interpretation or explicitly documented accepted alternatives
- [ ] An independent analyst reproduces all 20 answers without seeing the instructor key
- [ ] No student archive or public git revision exposes restricted answers
- [ ] Disagreements are corrected in the student artifact or question and retested

## Evidence limitations

The exercise uses synthetic records. Simulated Secure Boot/TPM observations are not hardware attestation or native firmware evidence. Network metadata is not proof of exfiltration. Conclusions must stay within the evidence actually supplied.

## Status

**Protocol published; independent reproduction not yet demonstrated.** This document is a reproducibility standard and checklist, not a claim that the 20 answers have been independently verified.
