# Technical QA — Student Package

## Confirmed checks

- Archive: `downloads/The_Invisible_Intruder_HTB_Student.zip`
- ZIP successfully extracted in an offline review using the challenge password.
- The archive contains `QUESTIONS.md`, `EVIDENCE_GUIDE.md`, `SHA256SUMS.txt` and 14 synthetic evidence files.
- All 14 SHA-256 manifest entries matched their respective extracted files.
- The student questions contain 20 cross-source investigation prompts.
- The inspected student archive contains no files labeled as instructor answer keys or walkthroughs.

## Remaining acceptance gates

- Run an independent analyst blind solve; not completed.
- Confirm each of the 20 questions has a unique, reproducible answer with evidence citations; not independently completed.
- Verify separate instructor access and ensure that no answer keys are exposed through release assets or git history.
- Calibrate the claimed Insane difficulty from independent testing; not established.

## Evidence boundaries

All data is synthetic. The provided boot-state records are simulated observations, not hardware TPM attestation or a firmware acquisition. Network flow records alone do not prove file-content exfiltration. This is an educational defensive investigation, not an actual incident report.
