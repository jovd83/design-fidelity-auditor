# Design Fidelity Auditor

[![version](https://img.shields.io/badge/version-2.1.0-blue)](CHANGELOG.md)
[![status](https://img.shields.io/badge/status-stable-brightgreen)](SKILL.md)
[![category](https://img.shields.io/badge/category-design-0a7ea4)](SKILL.md)
[![license](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![validation](https://img.shields.io/badge/validation-executable-success)](#local-validation)

Audit frontend implementation for design-system drift before it becomes product drift.

`design-fidelity-auditor` is an AgentSkill for reviewing UI code against a canonical design system. It helps an agent or engineer answer questions like:

- Are we still using approved tokens?
- Did this component bypass theme primitives with hardcoded values?
- Are spacing, typography, motion, and interaction states still aligned?
- Which issues are true policy violations versus lower-confidence drift risks?

The skill is intentionally review-first. It is built to generate a structured audit artifact, not to silently redesign the UI.

## What This Skill Does

- inspects CSS, Tailwind, JSX, TSX, Angular templates, Vue SFCs, and related UI files
- reads project design authority such as `DESIGN.md`, token files, theme config, or primary primitives
- produces a fidelity scorecard plus evidence-backed findings
- recommends the smallest system-aligned remediation for each issue
- distinguishes confirmed violations from ambiguous cases

## What This Skill Does Not Do

- replace accessibility review, browser QA, or visual regression testing
- invent a design system when the project has none
- maintain shared cross-repository governance infrastructure
- auto-apply broad UI changes unless the user explicitly requests implementation work

## Repository Layout

```text
.
|-- SKILL.md
|-- README.md
|-- CHANGELOG.md
|-- assets/
|   `-- audit-report-template.md
|-- evals/
|   `-- evals.json
|-- examples/
|   `-- sample-audit-report.md
|-- fixtures/
|   `-- basic-button/
|       |-- button.css
|       |-- design-system.md
|       `-- expected-findings.json
|-- reports/
|   `-- .gitkeep
|-- scripts/
|   |-- score_audit_report.py
|   `-- validate_audit_report.py
`-- benchmarks/
    `-- README.md
```

## Inputs

The skill works best when given both:

- UI implementation under review
- design authority for comparison

Typical design authority inputs:

- `DESIGN.md`
- CSS custom property token files
- Tailwind theme or config
- component library primitives
- design-system guidelines or generated design notes

Typical implementation inputs:

- CSS or SCSS
- JSX or TSX
- Tailwind class strings
- Angular or Vue templates
- inline styles

## Output

The canonical output is a markdown audit report with:

- audit summary
- design authority reviewed
- scope and evidence
- fidelity scorecard
- findings with severity and file evidence
- remediation priorities
- confidence and unknowns
- recommended next step

Use [assets/audit-report-template.md](assets/audit-report-template.md) as the default structure.

## Dispatcher Telemetry

If this skill is selected by a dispatcher and telemetry is enabled, log the dispatch decision before returning the audit result.

Preferred commands:

```bash
./log-dispatch.sh --skill design-fidelity-auditor --intent audit_ui_fidelity --reason "Design-system drift audit requested" --decision HANDOFF
```

On Windows:

```powershell
.\log-dispatch.cmd --skill design-fidelity-auditor --intent audit_ui_fidelity --reason "Design-system drift audit requested" --decision HANDOFF
```

If the logger is not present in the current repository, use the nearest installed `skill-dispatcher` logger when available. If no logger exists, continue the audit and explicitly note that telemetry could not be recorded.

## Audit Philosophy

This skill uses a simple evidence hierarchy:

1. Token source or theme config
2. Canonical design-system docs such as `DESIGN.md`
3. Established repository primitives
4. Visual references or generated design notes
5. General design best practices

That ordering matters. A strong audit should not confuse taste with policy.

## Dispatcher Alignment

This repository now declares the full dispatcher-facing metadata needed for reliable routing in `SKILL.md`, including:

- `dispatcher-category: design`
- `dispatcher-capabilities` for token audit and drift detection
- `dispatcher-accepted-intents` for audit and compliance-review routing
- `dispatcher-input-artifacts` and `dispatcher-output-artifacts`
- `dispatcher-risk: low`
- `dispatcher-writes-files: true`
- `dispatcher-persistent-directories: reports`
- `dispatcher-layer: feedback`
- `dispatcher-lifecycle: active`

That makes the skill easy to route as a focused review specialist rather than a generic frontend helper.

## Memory Boundaries

This repository keeps memory intentionally scoped:

- Runtime memory: current audit evidence and findings in the active thread
- Project-local memory: optional saved audit report inside the repo when explicitly requested, preferably under `reports/`
- Shared memory: intentionally out of scope for this skill

If your environment supports a shared-memory or governance skill, integrate at that boundary rather than embedding shared memory into this repository.

## Local Validation

If an audit report is written to disk, validate its structure:

```bash
python scripts/validate_audit_report.py path/to/report.md
```

Score a saved report against the bundled basic fixture:

```bash
python scripts/score_audit_report.py path/to/report.md fixtures/basic-button/expected-findings.json
```

These scripts are lightweight checks, not full semantic evaluation. They are meant to catch regressions in report structure and core finding coverage.

When you want a predictable project-local artifact path, save reports under `reports/`.

## Evaluations

Prompt-based evals live in [evals/evals.json](evals/evals.json). They cover:

- hardcoded token bypasses
- arbitrary spacing and sizing values
- incomplete design references
- proper handling of uncertainty
- remediation guidance quality

## Extending The Skill

Good extension points:

- add more fixtures in `fixtures/` for specific stacks such as Tailwind, Angular, or component-library variants
- strengthen the scoring harness with domain-specific expectations
- add CI that validates example artifacts and benchmark fixtures on each change

Avoid adding speculative infrastructure unless it directly improves audit quality or installability.

## Publishing Notes

For public GitHub packaging, this repository is already structured so a maintainer can add:

- a project `LICENSE` file
- CI to run the validation scripts
- additional fixtures and benchmark cases
- release notes tied to `metadata.version` in `SKILL.md`

Current version: `2.1.0`

## Suggested Use

Use this skill when another agent or reviewer needs a fast, evidence-backed answer to:

`Does this UI still honor the design system, and if not, what exactly drifted?`
