# Candidate Theme Contrast — Initial Quantitative Review

**Date:** 2026-11-03 | **Status:** Findings for review, **not** verified WCAG compliance.  
**Source:** `tokens/skyvision.tokens.json`. Values below use standard WCAG relative luminance math; design tokens are still *proposed*.

| Pair | Light ratio | Dark ratio | Relevant threshold |
|---|---:|---:|---|
| Main text/background | 13.16:1 | 14.97:1 | 4.5:1 normal text |
| Main text/panel | 14.05:1 | 12.62:1 | 4.5:1 normal text |
| Muted text/panel | 6.03:1 | 8.73:1 | 4.5:1 normal text |
| Button text/button accent | **4.10:1** | 9.10:1 | 4.5:1 normal text |
| Functional border/panel | **1.44:1** | **1.81:1** | 3:1 when border identifies a control |
| Accent/background | 3.84:1 | 9.10:1 | 4.5:1 if used as small text |

The last two rows are contextual: decorative borders need not meet the control-boundary threshold, but meaningful control shapes, focus indicators and other non-text elements need sufficient perceptual contrast.

## Proposed accessible replacements (NOT approved canonical colors)

Keep brand gold `#D8B383` for illustration. For light-theme **functional interactive text/button surfaces** separately consider:
- Light functional accent `#8B6035` with white text: approx **5.49:1**; against paper `#FBF7F1`: approx **5.15:1**.
- Light functional border `#888888` against white: approx **3.54:1** when the boundary must be perceivable.
- Dark functional border `#6C8798` against dark panel `#14283A`: approx **3.99:1**.

Do not overwrite brand/canonical token values without an ADR and owner approval. Avoid indiscriminately strengthening *decorative* fine orbit lines.

## Next tests

- Validate all text sizes, disabled controls, errors and focus against the **actual composited** backgrounds.
- Verify focus outline against both adjacent colors.
- Validate status chips with text and/or icon (never color alone), including user-customizable status colors.
- Run keyboard-only, zoom/reflow, screen-reader, RTL/Persian and reduced-motion tests.
- Record before/after screenshots and accepted updated semantic values.

Run `python scripts/contrast_audit.py` for current diagnostic ratios. `--strict` will fail when any predefined text or UI-boundary pair misses its benchmark; don't enable it as a release gate until the token proposals are reconciled.
