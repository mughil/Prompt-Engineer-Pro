#!/usr/bin/env python3
"""Lightweight repository integrity checks; uses only the Python standard library."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []

# Check concrete local Markdown paths referenced by SKILL.md.
skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
for match in re.finditer(r"`((?:references|examples)/[^ `*]+\.md)`", skill):
    rel = match.group(1)
    if not (ROOT / rel).is_file():
        errors.append(f"SKILL.md references missing file: {rel}")

# Check all Markdown links in the manifest's documented source tree.
manifest = (ROOT / "MANIFEST.md").read_text(encoding="utf-8")
for match in re.finditer(r"`((?:references|examples|evals)/[^ `*]+\.(?:md|json))`", manifest):
    rel = match.group(1)
    if not (ROOT / rel).is_file():
        errors.append(f"MANIFEST.md references missing file: {rel}")

eval_path = ROOT / "evals" / "evals.json"
try:
    payload = json.loads(eval_path.read_text(encoding="utf-8"))
    cases = payload.get("evals")
    if not isinstance(cases, list) or not cases:
        errors.append("evals/evals.json must contain a non-empty 'evals' array")
    else:
        if any(not isinstance(case, dict) for case in cases):
            errors.append("Every evaluation case must be an object")
        else:
            ids = [case.get("id") for case in cases]
            if len(ids) != len(set(ids)):
                errors.append("Evaluation case IDs must be unique")
            for case in cases:
                if not case.get("name") or not isinstance(case.get("prompt"), str) or not case.get("expected_output"):
                    errors.append(f"Evaluation case is missing required fields: {case.get('id')}")
except (OSError, json.JSONDecodeError) as exc:
    errors.append(f"Cannot read valid evals/evals.json: {exc}")

if errors:
    print("Repository validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Repository validation passed.")
