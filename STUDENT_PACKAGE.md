# Student package — distribution checklist

## Official student asset

[The_Invisible_Intruder_HTB_Student.zip](downloads/The_Invisible_Intruder_HTB_Student.zip)

This is the **only student archive currently published** in this repository. It is password-protected; distribute the password through the authorized submission channel, not through public answer files.

## Expected package structure

The current QA report records the following archive members:

- `EVIDENCE_GUIDE.md`: source and investigation guidance
- `QUESTIONS.md`: 20 investigation questions
- `SHA256SUMS.txt`: evidence integrity manifest
- `evidence/`: 14 synthetic evidence files, as recorded in the QA report

This is an **expected inventory based on the earlier QA report**, not a fresh archive extraction. Inspect the ZIP before claiming a final release.

## Pre-release checks

1. Open the ZIP using the password given to the reviewer and confirm it extracts cleanly.
2. Confirm every manifest entry maps to an existing file and verify its SHA-256 digest.
3. Confirm all 20 questions reference artifacts present in the extracted package.
4. Inspect every file for instructor-only material, answer values, walkthroughs and hidden grading rubrics.
5. Independently solve all 20 questions and record exact artifact citations.
6. Test with an analyst who has not seen the answer key; record ambiguous questions and completion time.
7. Provide the confidential instructor writeup via a **separate restricted location**.
8. Confirm download permissions and links using a reviewer account.

## Do not distribute publicly

Instructor answer keys, expected responses, scoring secrets, walkthroughs, private grading materials, credentials or any genuine sensitive data. A directory named `private` within a **public** repository is still publicly accessible.

## Evidence caveats

The scenario uses synthetic exports, including simulated boot-state observations. It is not a native firmware or TPM acquisition. Do not claim that exfiltration, hardware tampering or attacker identity is conclusively established unless independent evidence supports that conclusion.

## Status

**Documentation prepared; release validation incomplete.** This checklist does not certify that all ZIP checks or blind solves have been completed.
