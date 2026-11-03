# Sky Vision — Agent Handoff

**Updated:** 2026-11-03  
**Current state:** Brand Book v0.1 and roadmap published as working proposals. Repository began as an empty public GitHub project.

## Purpose
Build a single coherent Sky Vision identity across studio/brand, website and a lightweight-but-scalable creative project-management system. The central functional principle is **productivity without images**. Decorative illustrations and thumbnails are optional.

## Established / protected
- The user-supplied circular moon/wave illustration is the primary aesthetic reference.
- Primary identity: midnight navy, warm ivory, desaturated mist blue and muted gold.
- Motif vocabulary: orbit, crescent, cloud, wave, star/compass and thin gold connectors.
- Sky Vision is the target identity; mockup names LUNARA and ORBITRA are historical exploratory text only.
- Changes to canonical brand, licensing, source art or product principles require approval, recorded in ADRs.

## Source of truth
- `brandbook/BRAND_BOOK.md`: editorial system, identity rules, product styling.
- `brandbook/APPROVAL_MATRIX.md`: what is approved vs pending.
- `ROADMAP.md`: prioritized work and testable phase exits.
- `tokens/`: proposed semantic color and spacing values.
- `assets/ASSET_REGISTER.md`: original archive record and present repository status.

## Recent work
- Created repository README, canonical brand book and roadmap.
- Prepared agent skills, design tokens, working SVG studies and product interface spec.
- **Important limitation:** Original PNG/JPEG concept boards are in the downloadable source archive; do not assume they exist in GitHub before checking paths. Never mark source-asset import complete until files and checksums are verified.

## Immediate next steps
1. Confirm original asset rights and push original reference/concept image files unchanged with hashes.
2. Make 3–5 distinct logo candidates, verify at 16/24/48 px and record owner choice.
3. Test candidate palette for real contrast in light/dark UI; issue adjusted semantic token values.
4. Implement a no-image List/Kanban prototype sharing one data model.
5. Build visual brand-book export and presentation preview from exact approved/working source.
6. Review Phase 0 exit criteria and open unresolved items as GitHub issues.

## Do not do
- Do not overwrite concept originals or delete archived experiments.
- Do not call the current logo, tagline, fonts or mockup copy finalized.
- Do not add invented statistics, testimonials or product availability claims.
- Do not publish a commercial asset license without express authorization.

## Definition of done
Paths linked; design rules recorded; checks passed with evidence; contrast/RTL reviewed for UI; state of approval clear; agent handoff updated; roadmap boxes checked only when complete.

## 2026-11-03 addendum
- Implemented browser-only no-image PM prototype at `preview/index.html` with searchable List/Board, light/dark, add task, add custom status and local persistence. It is not a production app and has not undergone end-to-end browser audit.
- Created downloadable 15-page landscape PDF brand-book companion (not yet hosted in GitHub).
- Logged raster SHA-256 hashes in `assets/RASTER_MANIFEST.json`; all binary GitHub statuses remain **pending**.
- Opened issues #1–#4 for transfer/approval/accessibility/product componentization.
- CI workflow is present; the connected GitHub status APIs have not established an executed passing Actions run. Check repository Actions manually before claiming CI green.
