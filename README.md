# The Invisible Intruder — Beneath the Boot

**Sherlock-style DFIR training | Fictional investigation | Difficulty: Insane (proposed, unvalidated)**

A simulated intrusion investigation into a possible boot-chain compromise at **Northbridge Systems**, a fictional organization. Examine Windows security and process records, scheduled tasks, network telemetry, file access, and simulated boot-state observations. Distinguish supported findings from hypotheses: the evidence does **not** constitute a native firmware acquisition or a hardware TPM attestation.

## Student package

**[Download the student ZIP](downloads/The_Invisible_Intruder_HTB_Student.zip)**

The archive is password-protected. Obtain the password through the authorized challenge submission or instructor. Never publish instructor answers in this repository.

After extracting the archive:

1. Read `EVIDENCE_GUIDE.md` for evidence sources, timestamps and limitations.
2. Open `QUESTIONS.md` and work through the 20 investigation prompts.
3. Validate the extracted evidence against `SHA256SUMS.txt` before relying on it.
4. Record each answer with an exact artifact, record identifier and explanation; distinguish facts, uncertainty and alternative hypotheses.

## Investigation learning outcomes

- Correlate Windows Security, Sysmon, scheduled-task, DNS and network-flow evidence.
- Normalize event timestamps using the source clock reference instead of assuming all clocks are synchronized.
- Examine potential persistence, access and recovery-related changes without inferring attribution from one event.
- Evaluate simulated UEFI/Secure Boot/TPM observations while avoiding unsupported claims of hardware compromise.
- Produce an evidence-cited incident timeline and defensible containment recommendations.

## Distribution and integrity

| Asset | Audience | Purpose |
| --- | --- | --- |
| `downloads/The_Invisible_Intruder_HTB_Student.zip` | Students and authorized reviewers | Student exercise and synthetic evidence |
| `EDUCATIONAL_PURPOSE_NOTICE.md` | Public | Ethical use, authorization and ownership notice |
| `REVIEWER_GUIDE.md` | Public | Evaluation scope and limitations |
| `QA_STUDENT_PACKAGE.md` | Public | Reported package checks and outstanding validation |
| Instructor answer key / walkthrough | Restricted | **Not included in public student distribution** |

The QA report records earlier extraction and hash checks. **These checks have not been independently rerun as part of this README revision.** The proposed Insane difficulty has not been independently established by a blind playtest.

## Submission readiness

- [x] Public student ZIP linked from README
- [x] Ethical/educational notice linked
- [x] Reviewer guide and QA report available
- [ ] Independently reproduce all 20 answers from student artifacts
- [ ] Complete a blind solve and difficulty calibration
- [ ] Confirm reviewer access to the separate, private instructor walkthrough
- [ ] Verify that public release artifacts and Git history do not disclose solutions

## Responsible use

This is a **fictional, synthetic, defensive training exercise**. It grants no authorization to access or test systems owned by others. Perform testing only in environments you own or are expressly authorized to assess.

**Uso ético y educativo:** Este ejercicio ficticio y simulado se ofrece exclusivamente para formación defensiva autorizada. No autoriza pruebas ni accesos a sistemas de terceros sin permiso expreso.

See [Educational Purpose Notice](EDUCATIONAL_PURPOSE_NOTICE.md). The project does not claim endorsement, acceptance or affiliation with Hack The Box.

## Documentation index

For a role-based navigation guide, evidence-handling requirements, scope limitations and release boundaries, see **[Documentation Index](DOCUMENTATION_INDEX.md)**. The index separates student, reviewer and release-manager instructions and records the remaining validation tasks.

## Packaging verification

Before delivering the archive, run the [student package validator](tools/validate_student_package.py) and follow the [repeatable packaging procedure](PACKAGE_VALIDATION.md). The validator checks ZIP structure and filenames; with the password supplied locally it also verifies the internal SHA-256 manifest. An incomplete run is not a passing release check.
