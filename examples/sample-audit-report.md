# Design Fidelity Audit: Shared Button Primitive

## Audit Summary

- Overall status: Mixed
- Confidence: High
- Design drift level: Moderate
- Primary concern: the button primitive bypasses semantic color and spacing tokens in reusable code.

## Design Authority Reviewed

- Primary reference: `fixtures/basic-button/design-system.md`
- Supporting references: `fixtures/basic-button/button.css`
- Authority quality: Strong

## Scope and Evidence

- Reviewed files: `button.css`
- Excluded files or areas: None
- Evidence notes: This audit covers one primitive, so conclusions should not be generalized to the entire UI surface.

## Fidelity Scorecard

| Dimension | Status | Notes |
| --- | --- | --- |
| Color and semantic tokens | Violates | Background color uses a hardcoded hex instead of a semantic token. |
| Spacing and sizing scale | Partial | Padding uses a non-token value that does not match the documented spacing scale. |
| Typography alignment | Aligned | Font size matches the documented body size token. |
| Radius, elevation, and motion | Aligned | Border radius matches the documented radius token. |
| State fidelity | Not assessed | No hover, focus, or disabled state provided in scope. |
| Primitive reuse | Partial | Local values suggest the primitive can drift further as variants are added. |

## Findings

| Severity | File | Evidence | Why it matters | Recommended fix |
| --- | --- | --- | --- | --- |
| High | `button.css:2` | `background-color: #ff4500;` | Shared primitives should express brand intent through semantic tokens, not direct hex values. | Replace with `var(--color-primary)` or the project's approved semantic alias. |
| Medium | `button.css:4` | `padding: 12px;` | A non-token spacing value creates inconsistent rhythm and encourages arbitrary follow-on values. | Replace with approved spacing tokens such as `var(--spacing-md)` and `var(--spacing-lg)` based on the intended density. |

## Remediation Priorities

1. Replace the hardcoded background color with the approved semantic color token.
2. Normalize padding to the documented spacing scale.
3. Add state styles using existing system primitives before introducing new button variants.

## Confidence and Unknowns

- Confirmed: color token bypass and spacing-scale drift are directly supported by the reviewed code and design reference.
- Inferred risks: if this primitive is copied into variants, the same hardcoded values are likely to spread.
- Unknowns: the design reference does not specify hover or focus state requirements for this fixture.

## Recommended Next Step

Update the shared button primitive to use semantic tokens, then rerun the audit before propagating the component into additional variants.
