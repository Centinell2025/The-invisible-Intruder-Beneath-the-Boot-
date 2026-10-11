# The Invisible Intruder — Beneath the Boot

**Restricted instructor writeup — not for students.**

**Scenario:** Northbridge Systems (fictional). All evidence is synthetic. Proposed difficulty: Insane candidate, subject to HTB review.

## Investigation and answers

Q1 — UTC Security logon: **2026-09-18T01:42:00Z**. SEC-3001; clock_domains.csv; unified_events.csv. Apply 90-second correction.

Q2 — Suspect remote-session LogonId: **0x8d32**. SEC-3001/3002/3004, excluding SEC-3005/3006/3007.

Q3 — Parent process record: **PROC-700**. PROC-701 parent GUID matches PROC-700 process GUID; exclude PROC-703.

Q4 — Created and invoked task: **\Microsoft\Windows\Maintenance\CacheHealth**. SEC-3003, TASK-901/902, PROC-702.

Q5 — Was suspect task authorized by CHG-802? **NO**. Approved InventoryAgent update has different scope.

Q6 — Earliest suspect remote-management process: **PROC-700**. Correct host-local time to 01:46 UTC, before PROC-701.

Q7 — Account spanning logon, script, task: **NORTHBRIDGE\svc_update**. SEC-3001, PROC-701, TASK-901.

Q8 — TaskScheduler log-clear process: **PROC-704**. GUID lineage to PROC-700 and wevtutil command.

Q9 — Security log cleared event ID: **1102**. SEC-3004, LogonId 0x8d32; separate from TaskScheduler disruption.

Q10 — Minutes from remote logon to task creation: **10**. 01:42 to 01:52 UTC after time normalization.

Q11 — First matching outbound flow: **FLOW-501**. DNS-801 resolution 198.51.100.42, matching WKS-17 egress.

Q12 — Aggregate outbound bytes: **267396**. FLOW-501 19284 + FLOW-502 248112; exclude internal decoy.

Q13 — Ratio second to first flow: **12.87**. 248112 / 19284 rounded to two decimals.

Q14 — File path read on FS-01: **\\FS-01\Operations\quarterly-recovery-plan.pdf**. FS-601, exclude FS-602. ReadData is not proof of exfiltration.

Q15 — Minutes from logon to file access: **61**. 01:42 to 02:43 UTC.

Q16 — First changed recovery-anchor record: **BOOT-202**. Compare BOOT-201 baseline, BOOT-202 observation, CHG-803 pending.

Q17 — Observed PCR7 digest: **5f7b2a11**. BOOT-202/203 and attestation_baseline.json; enrolled baseline is 1b4a8c20.

Q18 — Cryptographically verified hardware TPM quote? **NO**. Simulation/no-hardware-quote; see acquisition log.

Q19 — Confirmed file-content exfiltration? **NO**. NetFlow and ReadData alone do not show content transfer; payload and contents not acquired.

Q20 — Firmware compromise classification: **UNPROVEN**. Synthetic boot observations without native firmware image or hardware TPM quote cannot establish compromise.

## Evidence limitations

This is a synthetic DFIR investigation. Selected records are exports rather than native EVTX/PCAP. No packet payload, acquired file contents, firmware image, or verified hardware TPM quote is provided. The challenge does **not** establish confirmed data exfiltration or firmware compromise. This writeup should be blind-playtested before HTB submission.
