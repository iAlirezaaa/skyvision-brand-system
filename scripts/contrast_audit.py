#!/usr/bin/env python3
"""Report WCAG contrast of candidate theme tokens.

Advisory by default: the current palette is NOT approved/accessibility-audited.
Use --strict after the palette has been fixed and formally reviewed.
"""
from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
colors = json.loads((ROOT / "tokens/skyvision.tokens.json").read_text(encoding="utf-8"))["color"]

def luminance(code):
    values = [int(code[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4 for v in values]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]

def contrast(a, b):
    la, lb = luminance(a), luminance(b)
    return (max(la, lb) + 0.05) / (min(la, lb) + 0.05)

checks = [
    ("foreground", "background", 4.5, "normal text"),
    ("foreground", "surface", 4.5, "normal text"),
    ("foregroundMuted", "surface", 4.5, "normal text"),
    ("accentForeground", "accent", 4.5, "normal button text"),
    ("border", "surface", 3.0, "meaningful UI boundary only"),
]
fails = []
for theme in ("light", "dark"):
    c = colors[theme]
    for key_a, key_b, minimum, purpose in checks:
        ratio = contrast(c[key_a], c[key_b])
        verdict = "PASS" if ratio >= minimum else "REVIEW"
        print(f"{theme:5} {key_a}/{key_b}: {ratio:.2f}:1 ({purpose}; {verdict})")
        if ratio < minimum:
            fails.append(f"{theme}.{key_a}/{key_b}")
print(f"Reported {len(checks)*2} candidate pairs; {len(fails)} below tested thresholds.")
if "--strict" in sys.argv and fails:
    print("FAIL (strict):", ", ".join(fails))
    sys.exit(1)
print("Advisory only: contrast math is not a complete WCAG/accessibility audit.")
