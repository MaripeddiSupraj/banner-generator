#!/usr/bin/env python3
"""Validate a Supraj.dev banner-generator output against the skill contract."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED_SECTIONS = [
    "TOPIC",
    "VISUAL INTERPRETATION",
    "CONCEPT 1",
    "CONCEPT 2",
    "CONCEPT 3",
    "RECOMMENDED CONCEPT",
    "THUMBNAIL",
    "ARTICLE HERO",
    "OG / SOCIAL",
    "DESIGN NOTES",
    "FINAL QUALITY CHECK",
]

REQUIRED_PROMPT_FIELDS = ["Prompt:", "Avoid:"]
REQUIRED_QUALITY_CHECKS = [
    "technically meaningful",
    "readable at thumbnail size",
    "unique from generic AI art",
    "suitable for Supraj.dev",
    "thumbnail and hero are related but not identical",
]


def validate(text: str) -> list[str]:
    errors: list[str] = []
    upper = text.upper()

    for section in REQUIRED_SECTIONS:
        if section not in upper:
            errors.append(f"Missing required section: {section}")

    # We expect three asset prompts, therefore at least three Prompt fields.
    if text.count("Prompt:") < 3:
        errors.append("Expected at least three Prompt: fields (thumbnail, hero, OG/social)")

    if text.count("Avoid:") < 3:
        errors.append("Expected at least three Avoid: fields (thumbnail, hero, OG/social)")

    for check in REQUIRED_QUALITY_CHECKS:
        pattern = re.compile(rf"{re.escape(check)}\s*:\s*(PASS|FAIL)", re.IGNORECASE)
        if not pattern.search(text):
            errors.append(f"Missing PASS/FAIL quality check: {check}")

    # Guardrail against accidentally returning a near-empty template.
    if len(text.strip()) < 1200:
        errors.append("Output is suspiciously short; expected a fully developed banner specification")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate-banner-spec.py <generated-output.txt>")
        return 2

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"ERROR: file not found: {path}")
        return 2

    text = path.read_text(encoding="utf-8")
    errors = validate(text)

    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS")
    print("Banner specification satisfies the structural contract.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
