# SKY VISION — Brand & Product Design Roadmap

**Version:** 0.1 | **Planning basis:** 2026-11-03 | **Status:** Proposed, not a delivery date commitment

## North star

Establish one searchable and enforceable Sky Vision identity system that can be used independently by humans, AI agents, web teams and a **fully functional image-optional project-management app**.

## One-by-one visual production program (added 2026-11-03)

- [x] Publish an exhaustive versioned visual inventory of **166 individual images** in 14 families at [production backlog](production/ASSET_BACKLOG.md) with machine records.
- [x] Define independent brief, export naming/ratios, review gates and approval statuses.
- [ ] Review and upload BG-01 primary dark hero image, preserving provenance.
- [ ] Only then create BG-02, BG-03, BG-04, followed by LG-01, CL-01 and MT-01 as **separate images**, one asset ID at a time.
- [ ] Expand the inventory with new IDs rather than silently merging unrelated deliverables.
- [ ] Import original raster concept archive (12 pending) only with public repository distribution rights checked.

For each item: `queued → draft → review → approved`, where approval requires an explicit owner decision **and verified repository output**. Completion of a file or AI generation is not approval.

## Phase 0 — Archive and guardrails

**Goal:** prevent loss of source images, decisions, product scope and brand intent.

- [x] Establish the working repository and versioned Markdown brand book.
- [x] Document naming boundary: SKY VISION is canonical; LUNARA and ORBITRA are historical concept labels.
- [x] Establish change-control rules, owner approval gate and agent handoff.
- [ ] Import **all** original raster assets from the source archive into the repository and verify exact hashes.
- [ ] Confirm redistribution rights/visibility for public GitHub and decide license.
- [ ] Add asset thumbnails and original/derived provenance to the asset ledger.

**Exit:** all source assets traceable and backed up, protected decisions recorded, no broken links.

## Phase 1 — Identity foundation (P0)

- [x] Write v0.1 positioning, tone, visual grammar and brand value hypotheses.
- [x] Propose semantic light/dark colors and motif usage principles.
- [ ] Review naming/trademark and compare at least three mark candidates.
- [ ] Select and formally approve final logo, mark and clear-space rules.
- [ ] Color-proof palette with contrast and printing tests.
- [ ] Choose/verify commercial and Persian webfont licenses.

**Exit:** ADR with signed final identity decisions, optical logo master files, small-size proofs, legal/licensing checklist.

## Phase 2 — Design system (P0)

- [ ] Formalize semantic tokens with JSON schema and buildable CSS outputs.
- [ ] Build icon and motif system: full, compact, monochrome and RTL-compatible assets.
- [ ] Define components: button, input, dropdown, tooltip, badge, table, task card, modal and toast.
- [ ] Complete light/dark/high-contrast and mobile states.
- [ ] Automated accessibility and screenshot regression on core screens.

**Exit:** component documentation + tested reference implementation + keyboard/RTL/reduced-motion audits.

## Phase 3 — Image-free PM product shell (P0)

- [ ] Workspace/project navigation and searchable project list.
- [ ] Create/edit/delete tasks; custom statuses with configurable colors and ordering.
- [ ] List + Kanban views backed by one task model.
- [ ] Task details, configurable fields, dependencies, attachments and activity log.
- [ ] Persist edits, handle offline/failed saves and permission boundaries.

**Exit:** representative user completes project/task workflows without images, using mouse and keyboard, with state consistency across views.

## Phase 4 — Advanced production workflows (P1)

- [ ] Timeline/Gantt, calendar, milestones and dependency/critical-path visualization.
- [ ] Asset-aware task cards; optional thumbnails and per-file review status.
- [ ] Filters, saved views, roles, automation and notifications.
- [ ] Templates for animation/VFX pipeline phases; avoid hardcoding department names.
- [ ] Performance and large-board usability QA.

**Exit:** real-world project scenario passes collaborative use and data-integrity tests.

## Phase 5 — Marketing and deliverables (P1)

- [ ] Responsive site templates (home, product, about, project/case study, contact).
- [ ] Brand book PDF generated from approved Markdown; print-safe proof.
- [ ] Social, stationery, presentation and motion usage templates.
- [ ] Bilingual English/Persian content and RTL proofreading.
- [ ] Public preview and project documentation screenshots using Sky Vision, not historical names.

**Exit:** approved kit exported in SVG/PNG/PDF/HTML + usage/license manifest.

## Phase 6 — Governance and automation (P2)

- [ ] PR templates and status checks enforce brand and asset validation.
- [ ] Update/upgrade guide for agent handoffs; change impact and rollback.
- [ ] Release tagging and immutable archive of approved versions.
- [ ] Compare new UI options against accessibility, usability, performance and continuity baselines.
- [ ] Define approval owners and review cadence.

**Exit:** reproducible design releases, no undocumented core changes.

## Priority definitions

- **P0:** required to preserve brand, legal clarity, or basic product usability.
- **P1:** extends real use cases after foundation.
- **P2:** improves scale, operations and maintainability.

## Product acceptance metrics (targets, not actual results)

| Dimension | Acceptance target |
|---|---|
| Image independence | All essential task operations possible without uploaded artwork |
| Theming | Light/dark feature and semantics parity |
| Accessibility | WCAG 2.2 AA audit for representative workflows |
| Data integrity | Status changes reflected consistently across views |
| Recoverability | Clear retry/error and unsaved-change states |
| Assets | Original provenance and hashes recorded, changes versioned |
| Brand governance | Core changes require an ADR with explicit approval |

## Decisions needed from owner

1. Are public repository redistribution and reuse restrictions acceptable for the original artwork?
2. Which logo direction becomes the official Sky Vision mark?
3. Is this a studio-first brand, a product-first brand, or a shared parent identity?
4. Are products under Sky Vision to use separate sub-brand names?
5. Which types of commercial fonts and icon sources are allowed?

Until resolved, keep related artifacts labeled **proposed** and do not imply official approval.

## Release discipline

`v0.x` = exploratory design system; `v1.0` = approved identity and usable design deliverables. For each milestone record decisions, tests, new assets, known gaps and next actions in `HANDOFF.md`. Do not mark unchecked roadmap items complete without evidence.
