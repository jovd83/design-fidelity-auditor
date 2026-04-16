#!/usr/bin/env python3
"""Score a saved audit report against a simple fixture expectation file."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 3:
        print(
            "Usage: python scripts/score_audit_report.py <report.md> <expected-findings.json>"
        )
        return 2

    report_path = Path(sys.argv[1])
    expected_path = Path(sys.argv[2])

    if not report_path.is_file():
        print(f"Report not found: {report_path}")
        return 2
    if not expected_path.is_file():
        print(f"Expectation file not found: {expected_path}")
        return 2

    report = report_path.read_text(encoding="utf-8")
    expected = json.loads(expected_path.read_text(encoding="utf-8"))

    required_sections = expected.get("required_sections", [])
    expected_keywords = expected.get("expected_keywords", [])

    section_hits = sum(1 for section in required_sections if section in report)
    keyword_hits = sum(1 for keyword in expected_keywords if keyword in report)

    total_checks = len(required_sections) + len(expected_keywords)
    if total_checks == 0:
        print("No checks defined.")
        return 2

    score = round(((section_hits + keyword_hits) / total_checks) * 100, 1)

    print(f"Score: {score}")
    print(f"Sections matched: {section_hits}/{len(required_sections)}")
    print(f"Keywords matched: {keyword_hits}/{len(expected_keywords)}")

    if score < 70:
      return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
