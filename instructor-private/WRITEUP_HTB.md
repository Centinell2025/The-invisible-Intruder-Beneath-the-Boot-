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


## HTB Questions YAML (instructor only)

The following question/answer definitions are included here so the evaluation package requires only two links. Do not distribute this file to students.

```yaml
# INSTRUCTOR ONLY — candidate answers pending blind-playtest
scenario: >
  Northbridge Systems, a fictional organization, detected unusual remote activity,
  scheduled-task persistence, log disruption, and recovery-anchor anomalies.
  Investigate synthetic host, network, file-access, and boot-observation artifacts.
description: >
  Correlate timestamps and event lineage to reconstruct the intrusion. Distinguish
  supported observations from unproven exfiltration and firmware-compromise claims.
questions:
  - number: 1
    type: free
    title: "What is the normalized UTC timestamp of the suspicious remote logon?"
    flag: "2026-09-18T01:42:00Z"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 2
    type: free
    title: "Which LogonId identifies the suspicious remote session?"
    flag: "0x8d32"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 3
    type: free
    title: "Which process record is the parent of PROC-701?"
    flag: "PROC-700"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 4
    type: free
    title: "What is the full path of the scheduled task created and invoked during the intrusion?"
    flag: "\\Microsoft\\Windows\\Maintenance\\CacheHealth"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 5
    type: free
    title: "Was the suspicious scheduled task authorized under CHG-802?"
    flag: "NO"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 6
    type: free
    title: "Which record identifies the earliest suspicious remote-management process?"
    flag: "PROC-700"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 7
    type: free
    title: "Which account links the remote logon, script execution, and scheduled task?"
    flag: "NORTHBRIDGE\\svc_update"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 8
    type: free
    title: "Which process record is associated with the TaskScheduler log-clear action?"
    flag: "PROC-704"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 9
    type: free
    title: "Which Windows Security event ID indicates the Security log was cleared?"
    flag: "1102"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 10
    type: free
    title: "How many minutes elapsed between the remote logon and scheduled task creation?"
    flag: "10"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 11
    type: free
    title: "Which outbound network flow first matches the suspicious resolved destination?"
    flag: "FLOW-501"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 12
    type: free
    title: "What is the combined outbound byte count for FLOW-501 and FLOW-502?"
    flag: "267396"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 13
    type: free
    title: "What is the FLOW-502 to FLOW-501 byte ratio, rounded to two decimal places?"
    flag: "12.87"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 14
    type: free
    title: "Which UNC file path was accessed on FS-01?"
    flag: "\\\\FS-01\\Operations\\quarterly-recovery-plan.pdf"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 15
    type: free
    title: "How many minutes elapsed between the remote logon and the FS-01 file access?"
    flag: "61"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 16
    type: free
    title: "Which record first shows the recovery-anchor measurement change?"
    flag: "BOOT-202"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 17
    type: free
    title: "What is the observed PCR7 digest in the changed measurement record?"
    flag: "5f7b2a11"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 18
    type: free
    title: "Was a cryptographically verified hardware TPM quote acquired?"
    flag: "NO"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 19
    type: free
    title: "Does the available evidence confirm file-content exfiltration?"
    flag: "NO"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
  - number: 20
    type: free
    title: "How should firmware compromise be classified on the available evidence?"
    flag: "UNPROVEN"
    answer_case_sensitive: false
    placeholder: "Enter your answer"
    requires: null
```
