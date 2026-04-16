# Benchmarks

This directory documents the lightweight benchmark approach for `design-fidelity-auditor`.

## Current Scope

The repository currently ships one minimal fixture in `fixtures/basic-button/` plus two helper scripts:

- `scripts/validate_audit_report.py`
- `scripts/score_audit_report.py`

These are intentionally small and deterministic. They do not attempt semantic grading of every sentence. Instead, they verify that:

- required sections are present
- expected terms and remediation cues appear
- the report shape remains stable across revisions

## Why This Is Lightweight

This skill repository is meant to stay installable and easy to understand. A heavy benchmark framework would be premature unless the fixture set grows substantially.

## Suggested Future Expansion

- add Tailwind-focused fixtures that include arbitrary values and tokenized alternatives
- add component-library fixtures that test primitive reuse and override drift
- add partial-authority fixtures that verify correct use of `Unknown` severity and reduced confidence
- wire the validation and scoring scripts into CI
