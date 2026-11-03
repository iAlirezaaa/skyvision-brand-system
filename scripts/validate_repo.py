#!/usr/bin/env python3
"""Minimal, dependency-free Sky Vision source checks."""
from pathlib import Path
import json
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
required = [
  "README.md", "ROADMAP.md", "AGENTS.md", "HANDOFF.md",
  "brandbook/BRAND_BOOK.md", "brandbook/APPROVAL_MATRIX.md",
  "docs/PRODUCT_UI.md", "docs/ART_DIRECTION.md",
  "docs/fa/README.md", "assets/ASSET_REGISTER.md",
  "tokens/skyvision.tokens.json", "tokens/skyvision.css",
  "skills/skyvision-brand-guardian/SKILL.md",
  "skills/skyvision-ui-designer/SKILL.md",
  "skills/skyvision-asset-curator/SKILL.md",
  "skills/skyvision-brandbook-editor/SKILL.md",
]
errors = []
for f in required:
    if not (ROOT / f).is_file():
        errors.append("Missing required file: " + f)
try:
    d = json.loads((ROOT / "tokens/skyvision.tokens.json").read_text(encoding="utf-8"))
    for mode in ("brand", "light", "dark", "status"):
        assert mode in d["color"], f"Missing palette mode: {mode}"
        for key, value in d["color"][mode].items():
            if not (isinstance(value, str) and len(value) == 7 and value.startswith("#") and all(c in "0123456789abcdefABCDEF" for c in value[1:])):
                errors.append(f"Invalid HEX: {mode}.{key}")
except Exception as e:
    errors.append("Token JSON error: " + str(e))
for svg in sorted((ROOT / "assets/svg").glob("*.svg")):
    try:
        root = ET.parse(svg).getroot()
        if "viewBox" not in root.attrib:
            errors.append("Missing viewBox: " + str(svg))
    except Exception as e:
        errors.append(f"Bad SVG {svg}: {e}")
for md in [ROOT / "brandbook/BRAND_BOOK.md", ROOT / "ROADMAP.md"]:
    if md.is_file() and len(md.read_text(encoding="utf-8")) < 500:
        errors.append("Suspiciously short: " + str(md))
print(f"Checked {len(required)} files, JSON tokens and SVG motifs.")
if errors:
    for e in errors: print("FAIL", e)
    sys.exit(1)
print("PASS — structural checks only (not contrast, licensing or design approval).")
