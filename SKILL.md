---
name: design-fidelity-auditor
description: Audit implemented UI code for design-system drift. Use when an agent or engineer needs to verify that CSS, Tailwind, JSX, TSX, Vue, Angular templates, or component styling still honors the project's canonical design tokens, typography rules, spacing scale, interaction states, and visual conventions.
license: MIT
compatibility: Requires file-reading support. Works best in agents with shell access for fast repository inspection and line-level evidence collection.
metadata:
  author: OpenAI Codex
  version: "2.1.0"
  maturity: stable
  dispatcher-category: design
  dispatcher-capabilities: token-audit, design-system-compliance, drift-detection, remediation-planning, ui-governance
  dispatcher-accepted-intents: audit_ui_fidelity, verify_design_compliance, detect_design_drift, design_system_drift_review, review_token_usage
  dispatcher-input-artifacts: ui_code, design_system_reference, component_snapshot, routing_request
  dispatcher-output-artifacts: fidelity_scorecard, design_system_violation_report, remediation_plan
  dispatcher-stack-tags: design, frontend, css, tokens, quality, audit
  dispatcher-risk: low
  dispatcher-writes-files: true
  dispatcher-persistent-directories: reports
  dispatcher-layer: feedback
  dispatcher-lifecycle: active
  tags:
    - design
    - frontend
    - audit
    - tokens
    - fidelity
---

# Design Fidelity Auditor

Audit UI implementation against the source of design truth.

This skill is a design-governance and implementation-review skill. Its job is to identify where shipped or generated UI code has drifted away from the intended design system, distinguish direct evidence from inference, and produce a remediation-focused report that another engineer or agent can act on immediately.

Use it after code generation, during design QA, before merging UI-heavy changes, or when a team suspects that hand-tuned styling has bypassed tokens and system rules.





## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

## Telemetry & Logging
> [!IMPORTANT]
> All usage of this skill must be logged via the Skill Dispatcher to ensure audit logs and wallboard analytics are accurate:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason>` (or `./log-dispatch.sh` on Linux)

## Telemetry & Logging
> [!IMPORTANT]
> When this skill is selected through a dispatcher workflow and dispatcher telemetry is enabled, the selection must be logged before the audit result is returned.
>
> Preferred commands:
> `./log-dispatch.cmd --skill <skill_name> --intent <intent> --reason <reason> --decision HANDOFF`
> or
> `./log-dispatch.sh --skill <skill_name> --intent <intent> --reason <reason> --decision HANDOFF`
>
> If the local repository does not contain the logger, check for a neighboring `skill-dispatcher` installation and use its logger.
>
> If no dispatcher logger is available at all, continue without blocking and explicitly note that telemetry could not be recorded in the current workspace.

## Use This Skill When

- The user asks whether UI code still matches a design system, token set, or `DESIGN.md`.
- A generated interface needs a post-generation compliance pass before implementation continues.
- A pull request introduces custom CSS, Tailwind values, inline styles, or ad-hoc classes that may bypass the system.
- A team wants a structured fidelity scorecard instead of a loose design review.
- A downstream skill needs a `design_system_violation_report` or `fidelity_scorecard` as input.

## Do Not Use This Skill For

- Inventing a new design language when no design reference exists.
- Replacing accessibility review, visual regression testing, or browser-based QA.
- Acting as a full brand strategist or product designer.
- Auto-rewriting large UI surfaces unless the user explicitly asks for implementation changes after the audit.

## Responsibilities

This skill is responsible for:

- locating the most authoritative design reference available
- checking whether implementation uses approved tokens and system primitives
- identifying concrete design drift with file and line evidence whenever possible
- distinguishing hard violations from softer consistency risks
- proposing remediation that preserves the system's language

This skill is not responsible for:

- maintaining shared design infrastructure across repositories
- storing cross-project memory or policy centrally
- performing pixel-perfect screenshot diffing on its own
- overriding the design system because a local implementation "looks better"

## Inputs

Consume the strongest evidence available. Typical inputs include:

- `design_system_reference`
  Examples: `DESIGN.md`, token files, Tailwind config, theme files, component guidelines, Storybook docs, Figma export notes, Stitch output, screenshots with annotations.
- `ui_code`
  Examples: CSS, SCSS, Tailwind class strings, JSX, TSX, Vue SFCs, Angular templates, inline styles, component libraries.
- `component_snapshot` optional
  Used only as secondary evidence. Do not infer token names from screenshots alone unless the design reference is missing.
- `constraints` optional
  Examples: `read-only`, `focus on colors`, `tailwind-only`, `report top 5 issues`, `stay concise`.

## Evidence Priority

When multiple references disagree, use this order:

1. Explicit project token source or theme configuration
2. Current canonical design-system document such as `DESIGN.md`
3. Repository component patterns already established in primary UI primitives
4. Recent generated output notes or screenshots
5. General design best practices

State when the evidence is incomplete or contradictory. Never present inference as policy.

## Memory Model

Use the lightest memory boundary that fits the task.

- Runtime memory: Keep the active audit scope, evidence, and findings in working memory during the current task.
- Project-local memory: Persist an audit report only when the user asks for a saved artifact or when a local review workflow clearly benefits from one.
- Preferred local persistence path: when saving a report in-repo, prefer the `reports/` directory so downstream tools and maintainers have a predictable handoff location.
- Shared memory: Out of scope for this skill. If drift trends need to be aggregated across teams or repositories, integrate with a dedicated shared-memory or governance skill instead of embedding that concern here.

Do not silently promote temporary audit observations into persistent memory. Only persist findings that are stable, evidenced, and useful beyond the current review.

## Workflow

Follow this sequence unless the user asks for a narrower review.

1. Establish scope.
   Identify the files or components under review, the design authority, and whether the output should stay in chat or be written to disk.
2. Record telemetry when applicable.
   If the skill was selected by a dispatcher and logging is enabled, log the dispatch event before performing deeper audit work.
3. Gather design evidence.
   Read the strongest available reference files first: token definitions, theme config, `DESIGN.md`, component primitives, and any style conventions that function as policy.
4. Inspect implementation evidence.
   Read the relevant UI code and capture precise file and line references where possible.
5. Classify findings.
   Separate:
   - direct violations
   - probable drift risks
   - unknowns caused by missing or ambiguous design guidance
6. Score carefully.
   Produce a scorecard that rewards alignment but does not fake precision. If evidence is partial, lower confidence instead of overconfident scoring.
7. Recommend remediation.
   Suggest the smallest system-aligned fix for each issue. Prefer token adoption, primitive reuse, or config-level cleanup over one-off overrides.
8. Deliver the audit artifact.
   Use the output contract in `assets/audit-report-template.md`. If the user wants a saved artifact, prefer writing it under `reports/` and optionally validate it with `scripts/validate_audit_report.py`.

## Severity Model

Classify each finding as one of:

- `Critical`
  Breaks core design-system policy, brand safety, or global consistency. Examples: hardcoded brand colors replacing token usage in shared primitives.
- `High`
  Clear system bypass or repeated drift likely to spread. Examples: many arbitrary Tailwind values, custom font stack in reusable layout primitives.
- `Medium`
  Local inconsistency that should be corrected but is unlikely to destabilize the whole system alone.
- `Low`
  Minor cleanup or future-risk observation. Examples: redundant local alias, weak naming, slightly inconsistent token choice where guidance is ambiguous.
- `Unknown`
  Potential issue, but the design reference is incomplete or conflicting. Do not force a stronger severity without evidence.

## Output Contract

Produce a markdown report with these sections, in this order:

1. `# Design Fidelity Audit: <scope>`
2. `## Audit Summary`
3. `## Design Authority Reviewed`
4. `## Scope and Evidence`
5. `## Fidelity Scorecard`
6. `## Findings`
7. `## Remediation Priorities`
8. `## Confidence and Unknowns`
9. `## Recommended Next Step`

Within the report:

- Include overall confidence: `High`, `Medium`, or `Low`.
- Separate observed evidence from inferred risk.
- Include file references and line numbers when available.
- Use stable terminology: `design system`, `token`, `primitive`, `violation`, `drift risk`, `unknown`.
- Avoid fake percentages when the audit scope is too small or too incomplete.

### Fidelity Scorecard Dimensions

Score only the dimensions that can be supported by evidence:

- Color and semantic token usage
- Spacing and sizing scale discipline
- Typography alignment
- Border radius, elevation, and motion primitives
- State fidelity for hover, focus, active, disabled, and error states
- Primitive reuse and local override risk

If a dimension cannot be evaluated, mark it `Not assessed`.

## Handoff Contract

When invoked by a dispatcher-led workflow, accept these fields when available:

- `intent`
- `current_artifact_type`
- `target_artifact_type`
- `repo_context`
- `design_system_reference`
- `constraints`
- `allowed_write_risk`

Return a result shaped for downstream consumption:

- `deliverable`: markdown audit report
- `artifact_type`: `fidelity_scorecard` or `design_system_violation_report`
- `confidence`: `High`, `Medium`, or `Low`
- `recommended_next_step`: best follow-up action
- `follow_on_skill_type`: optional hint such as `execution`, `review`, or `design`

## Telemetry Contract

When this skill participates in a dispatcher-led workflow:

- log `HANDOFF` selections with `--skill design-fidelity-auditor`
- include the normalized `intent`
- keep the `reason` concrete and audit-specific
- treat telemetry as part of operational correctness, not optional polish

If telemetry cannot be recorded because the logger is unavailable, say so explicitly in the operating notes or final audit context rather than silently skipping it.

## Quality Bar

A strong audit should:

- tell another engineer exactly what drift exists and why it matters
- preserve the design system's terminology instead of replacing it with generic advice
- distinguish project policy from opinion
- give remediation that can be implemented without guesswork
- remain useful even when the design reference is partial, incomplete, or evolving

## Guardrails

- System first: prioritize the documented design system over local aesthetic preference.
- Evidence first: do not claim a violation unless you can point to code or a missing system-aligned reference.
- No silent redesign: audit and recommend; do not rewrite large surfaces unless the user explicitly requests implementation.
- No invented tokens: if the correct token is unknown, say so and describe the required characteristics instead.
- No false certainty: when references are ambiguous, mark the finding as `Unknown` or reduce confidence.
- Keep scope honest: if only one component was reviewed, do not generalize to the whole product.

## Escalation Rules

Pause and say so when:

- no trustworthy design authority exists
- multiple references conflict and the conflict changes the conclusion materially
- the user appears to want implementation changes rather than an audit artifact
- the review would be stronger with visual references, but only code is available

## Bundled Resources

- `README.md`
  Human-facing repository guide and installation notes.
- `assets/audit-report-template.md`
  Default output skeleton for audit reports.
- `examples/sample-audit-report.md`
  Example of a concise but production-grade audit deliverable.
- `fixtures/basic-button/`
  Minimal fixture for local regression testing.
- `evals/evals.json`
  Prompt-based regression checks for trigger quality and output quality.
- `scripts/validate_audit_report.py`
  Structural validator for saved reports.
- `scripts/score_audit_report.py`
  Lightweight benchmark helper for fixture-based report scoring.
- `reports/`
  Default location for saved audit artifacts when project-local persistence is requested.
