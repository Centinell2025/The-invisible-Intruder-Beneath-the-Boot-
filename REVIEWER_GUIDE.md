# Reviewer guide — The Invisible Intruder: Beneath the Boot

## Purpose

Assess whether the student exercise is solvable, reproducible, appropriately scoped, and accurately labeled. The investigation is fictional and uses synthetic forensic records.

## Student delivery

- [Student ZIP](downloads/The_Invisible_Intruder_HTB_Student.zip)
- [Student distribution checklist](STUDENT_PACKAGE.md)
- [Package QA report](QA_STUDENT_PACKAGE.md)
- [Ethical and educational notice](EDUCATIONAL_PURPOSE_NOTICE.md)

The password must be provided separately through an authorized channel. Do not infer that a public repository provides private instructor access.

## Suggested evaluation sequence

1. **Integrity:** extract the ZIP, inspect filenames and validate `SHA256SUMS.txt`.
2. **Completeness:** confirm all 20 prompts have their required evidence files.
3. **Reproducibility:** independently derive each answer and record artifact and record ID.
4. **Ambiguity:** test alternative answers, clock-offset assumptions and contradictory evidence.
5. **Reasoning:** evaluate cross-source correlations and explicit uncertainty.
6. **Security:** confirm the student release excludes answer keys and that git history is reviewed.
7. **Difficulty:** conduct a timed blind solve before accepting the proposed Insane rating.

## Critical evidence limitations

The package includes simulated boot-state information; it is **not** hardware TPM attestation, a native firmware dump, or proof of a real-world bootkit. Network metadata alone does not establish exfiltration. Attribute actions only to identities or processes that the evidence actually supports.

## Current verdict

**Ready for reviewer access to the public student archive; not yet technically certified as a final Insane Sherlock.** Independent solve, private writeup availability and full release checks remain outstanding.
