#!/usr/bin/env python3
"""Validate the structural shape of a saved design fidelity audit report."""

from __future__ import annotations

import sys
from pathlib import Path


REQUIRED_HEADINGS = [
    "# Design Fidelity Audit:",
    "## Audit Summary",
    "## Design Authority Reviewed",
    "## Scope and Evidence",
    "## Fidelity Scorecard",
    "## Findings",
    "## Remediation Priorities",
    "## Confidence and Unknowns",
    "## Recommended Next Step",
]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_audit_report.py <report.md>")
        return 2

    report_path = Path(sys.argv[1])
    if not report_path.is_file():
        print(f"Report not found: {report_path}")
        return 2

    content = report_path.read_text(encoding="utf-8")
    missing = [heading for heading in REQUIRED_HEADINGS if heading not in content]

    if missing:
        print("Validation failed. Missing required headings:")
        for heading in missing:
            print(f"- {heading}")
        return 1

    print("Validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
