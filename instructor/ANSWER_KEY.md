# RESTRICTED — Instructor / reviewer only
Do not distribute with student ZIP or publicly expose.

This **draft** sample supports Q1–Q12 and Q15–Q20 only partially; Q13–Q14 require explicit normalization context and the full Insane case needs additional sources. Reviewer must verify each prompt against raw artifacts before publishing.

Reference observations:
- Host: NB-WS-014 (EV-001 onward)
- Date: 2026-09-17 UTC
- Approved ticket: CHG-2048; window 02:00–03:00 UTC (EV-001)
- Account: nb-maint (EV-002)
- Boot discrepancy: EV-004; baseline enabled (EV-003); observed disabled (EV-004)
- PCR7 is simulated, not a hardware attestation (EV-005)
- Offset: +120 seconds (EV-008)
- Connection: 192.0.2.14 -> 198.51.100.27:443 (EV-007); attribution not established
- Maintenance permits OS servicing only, no firmware flash (EV-009)
- No firmware image or verified TPM quote was acquired (EV-010)
- **Defensible conclusion:** boot-state discrepancy is evidenced, but malicious firmware modification is **not proven**.

Avoid giving speculative attacker identities, payload hashes, or unobserved commands as answers.
