# AGENTS.md — Sky Vision design governance

## Mission
Maintain a searchable, versioned, human- and agent-readable design source of truth for the Sky Vision brand, website and image-optional creative project-management product.

## Required reading order
1. `README.md`
2. `brandbook/BRAND_BOOK.md` and `brandbook/APPROVAL_MATRIX.md`
3. `ROADMAP.md`
4. `docs/PRODUCT_UI.md`
5. `assets/ASSET_REGISTER.md`
6. `docs/decisions/`
7. Relevant skill in `skills/`

## Protected decisions
Do NOT silently change the Sky Vision name, brand purpose, motif family, source art, primary palette strategy, accessibility baseline, no-image task workflow, folder taxonomy, licensing terms or prior decisions. A proposed change must state: **from → to**, reason, alternatives, affected files, migration, rollback and measurable tests. Request owner approval before making a protected decision canonical.

Never overwrite original images. Derivative works must have a distinct filename, version and source record. Never relabel LUNARA/ORBITRA exploration as approved Sky Vision identity.

## Visual asset production contract

Read `production/ASSET_INVENTORY.json`, `production/ASSET_BACKLOG.md`, `production/DELIVERY_STANDARD.md` and the exact `production/briefs/<ID>.md` before creating a visual. **One visual deliverable per asset ID, one at a time**, not a mass collage. Do not skip a queued item unless owner or dependency review changes order. Record evidence and request acceptance before marking `approved`; never silently upgrade a conversation-only concept or a missing raster.

**Do not change the canonical theme palette to conceal failing color contrast without an owner-approved ADR.** Produce measured audit and proposal first (`docs/ACCESSIBILITY_COLOR_AUDIT.md`). CI can validate structure; it cannot certify aesthetics, rights or accessibility.

## Work sequence
1. Check existing conventions and issues; make a small scoped plan.
2. Identify whether proposed, approved or archived artifacts are affected.
3. Work in a branch for substantial changes; produce preview and verification evidence.
4. Update design tokens, docs, linked usage examples and change log together.
5. Validate with `python scripts/validate_repo.py`; evaluate light/dark, keyboard, RTL, reduced motion, contrast and no-image flows when applicable.
6. Update `HANDOFF.md` with changed paths, tests, gaps and next action.
7. Do not mark roadmap items complete without evidence.

## Quality hierarchy
Accessibility + data integrity > usability + legibility > brand tone > atmospheric decoration. Product controls must be clearly named, never communicated with color or illustration alone.

## Agent routing
- Brand decisions: `skills/skyvision-brand-guardian/SKILL.md`
- Book writing: `skills/skyvision-brandbook-editor/SKILL.md`
- Product/UI: `skills/skyvision-ui-designer/SKILL.md`
- Files/export/provenance: `skills/skyvision-asset-curator/SKILL.md`

## Truthfulness and safety
Do not claim production readiness, accessibility compliance, trademark clearance, copyright ownership, license grants, tests passed, or features implemented without corresponding proof. Repository is public; do not add confidential source assets or client names without permission.
