# Sky Vision Proposed Design Tokens

`skyvision.tokens.json` is the current **flat Sky Vision v0.1 application-specific token document**. It uses plain key-value objects and is **not validated as a standards-compliant W3C Design Tokens Community Group (DTCG) token file**. The `$schema` field in the current draft must not be interpreted as proof of conformance.

- `skyvision.css`: the current manually authored CSS variable proposal.
- `../scripts/contrast_audit.py`: checks selected light/dark text and control border pairs. Diagnostic by default.
- `../docs/ACCESSIBILITY_COLOR_AUDIT.md`: current measured findings and possible alternatives.

**Known issue:** white text on the proposed light accent is around 4.10:1; normal text target is 4.5:1. Some UI border colors do not provide 3:1 on adjacent panel colors when those borders convey control boundaries. Do not use the values as a guarantee of WCAG compliance.

Before token v1.0:
1. Convert to a verified token schema or document this as a deliberately custom JSON format.
2. Generate CSS from one source of truth instead of hand-maintaining two representations.
3. Test typography, surfaces, semantic status and accessible focus/interaction states in both themes.
4. Present before/after palette change for explicit brand approval.
