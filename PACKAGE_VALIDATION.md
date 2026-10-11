# Student ZIP packaging — repeatable release procedure

## Release asset

- Repository path: [`downloads/The_Invisible_Intruder_HTB_Student.zip`](downloads/The_Invisible_Intruder_HTB_Student.zip)
- Type: password-protected ZIP
- Intended audience: students and authorized reviewers
- Confidential instructor keys: **never** include in this archive or any public GitHub path

## Automatic package checks

The repository includes [`tools/validate_student_package.py`](tools/validate_student_package.py), which uses only Python's standard library.

From the repository root:

```bash
python3 tools/validate_student_package.py
```

This performs **metadata checks**: archive exists, ZIP directory can be parsed, paths are safe, duplicate names are absent, expected student documents are named, and obvious instructor-only filenames are absent. Without the password it intentionally exits with status **2** (incomplete validation), not success.

For full file integrity verification, provide the password **locally through an environment variable** (never commit or paste it into GitHub):

```bash
# Linux/macOS
read -rs SHERLOCK_ZIP_PASSWORD
export SHERLOCK_ZIP_PASSWORD
python3 tools/validate_student_package.py
unset SHERLOCK_ZIP_PASSWORD
```

On PowerShell:

```powershell
$env:SHERLOCK_ZIP_PASSWORD = Read-Host "ZIP password"
python tools/validate_student_package.py
Remove-Item Env:SHERLOCK_ZIP_PASSWORD
```

The full check extracts members **in memory**, checks the SHA-256 manifest, reads the student questions and reports the archive digest. It does not expose or validate instructor answers. No secret is saved to disk by this script.

## Manual acceptance gates

- [ ] Script exits with code 0 when run with the correct password.
- [ ] Verify the expected count and uniqueness of the 20 investigation questions.
- [ ] Inspect text and structured data for embedded answer keys, not only suspicious filenames.
- [ ] Complete an independent blind solve with evidence citations.
- [ ] Confirm a reviewer can access a separately restricted instructor walkthrough.
- [ ] Review prior public commits for sensitive instructor materials.
- [ ] Confirm the password is shared privately through the authorized challenge channel.

## Current status

**Packaging documentation and a repeatable verification script are published.** A successful end-to-end run against the encrypted ZIP has **not** been independently demonstrated in this update. Therefore a 10/10 *verified* packaging score would be premature.

## Educational use

This archive contains fictional and simulated defensive investigation material. No permission to assess third-party systems is granted. See [Educational Purpose Notice](EDUCATIONAL_PURPOSE_NOTICE.md).
