# Documentation index — The Invisible Intruder: Beneath the Boot

**Audience:** Sherlock students, authorized reviewers and instructors. **Scenario:** fictional Northbridge Systems. **Discipline:** defensive digital forensics and incident response.

## Start here

| Role | First document | Next action |
| --- | --- | --- |
| Student | [README](README.md) | Download [student ZIP](downloads/The_Invisible_Intruder_HTB_Student.zip), obtain password through authorized channel, read `EVIDENCE_GUIDE.md` and `QUESTIONS.md` inside ZIP |
| Reviewer | [Reviewer guide](REVIEWER_GUIDE.md) | Validate the archive, evidence and all 20 answers independently |
| Release manager | [Student package checklist](STUDENT_PACKAGE.md) | Confirm archive integrity, exclusions and reviewer access |
| Quality assessor | [Package QA report](QA_STUDENT_PACKAGE.md) | Distinguish documented checks from remaining acceptance gates |
| All readers | [Ethical and educational notice](EDUCATIONAL_PURPOSE_NOTICE.md) | Respect authorization, fictional context and intellectual property |

## Scope and evidence boundaries

This is a **synthetic DFIR investigation**, not a report of a real breach. It uses Windows, process, network, file-access and simulated boot-state observations. It does not include native firmware acquisition or cryptographic hardware TPM attestation. Metadata alone must not be treated as proof of exfiltration, attribution or persistence.

## Evidence-handling expectations

1. Preserve the original ZIP unchanged.
2. Extract into a separate working directory after receiving the password through the authorized submission channel.
3. Validate each evidence file against the supplied `SHA256SUMS.txt`; record any mismatches before analysis.
4. Record a normalized UTC timeline, source filenames and exact record references.
5. Separate observed facts, analytical inferences, alternative explanations and unsupported claims.
6. Cite evidence for every answer and note any ambiguity rather than inventing facts.

## Documentation status and limitations

- Public README, reviewer guide, package checklist, QA report and ethical notice are available.
- Earlier QA documentation reports an extracted archive with 20 questions and 14 evidence files, and matching manifest hashes. These results have **not been rerun in this documentation-only update**.
- An independent blind solve, verification of answer uniqueness, private instructor walkthrough access and Git-history exposure review remain outstanding.
- **Insane** is a proposed difficulty, not a verified HTB rating or acceptance.

## Confidentiality and release boundaries

Student material may be public; instructor solutions must be restricted. A directory name such as `private` does not restrict access inside a public GitHub repository. Removing files from the latest commit does not erase them from Git history. Do not publish real credentials, customer data or sensitive artifacts.

## Ethical use

Training is exclusively for defensive, educational and expressly authorized purposes. / El entrenamiento se realiza exclusivamente con fines defensivos, educativos y con autorización expresa.

This project does not claim official endorsement, affiliation or acceptance by Hack The Box.
