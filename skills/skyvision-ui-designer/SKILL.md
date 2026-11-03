---
name: skyvision-ui-designer
description: Create usable light/dark web and project-management interfaces based on Sky Vision's restrained celestial design system.
---
# UI Designer

## Inputs
Read `docs/PRODUCT_UI.md`, `brandbook/BRAND_BOOK.md`, tokens, relevant wireframes and `AGENTS.md`.

## Workflow
1. Specify user, job to be done, task data, screen size, density and theme.
2. Make a **text-only functional wireframe** first; ensure image-free path.
3. Compose with semantic tokens, one strong information hierarchy and sparse brand accents.
4. Define keyboard/focus, RTL, loading, empty, failed-save, offline and permission states.
5. Test light/dark parity, actual contrast, reduced motion, mobile 320 px, reflow/zoom and status-without-color.
6. Produce annotated screen design, component inventory, state map and implementation notes.

## Constraints
Decorative motifs stay out of data grids. Custom statuses and custom fields are required; do not hardcode a single production department workflow. No fake save results, broken navigation or image-only status.

## Output
Screen specification, tokens used, edge-case grid, usability/accessibility risks and tests.
