# SKY VISION | Brand Book v0.1

**Editorial identity + project-management design system**  
**Stage:** Working proposal | **Date:** 2026-11-03 | **Owner sign-off:** Pending

> This is a versioned working brand book, not a claim of approved identity, cleared trademarks, color-calibrated assets, or production-ready components.

## 01. Brand intent

**Working proposition:** Sky Vision helps creative teams see the whole picture without losing control of the smallest task.

- **Purpose:** Make complex creative production visible, organized, and easier to navigate.
- **Vision:** A recognizable, calm, craft-driven identity that connects studio, website, app, and production documentation.
- **Audience hypotheses:** Animation and VFX studios, creative directors, producers, independent teams, art departments and digital makers.
- **Personality:** Thoughtful / poetic / precise / composed / imaginative.
- **Promise (candidate):** Clarity for ambitious creative work.
- **One-line brand statement (candidate):** A clearer view of creative production.
- **Proof, case studies and positioning claims:** To be collected; do not manufacture them.

### The meaning of the visual language

The **orbit** represents connected work; the **crescent** represents iteration and phases; **waves and clouds** represent creative motion; **stars** represent milestones and clear points of attention. These are metaphors, not extra navigation controls.

## 02. Identity architecture

| Layer | Role | Rule |
|---|---|---|
| Sky Vision (name) | Working master brand | Keep spelling consistent; do not substitute LUNARA or ORBITRA |
| Editorial / marketing | Expressive personality | Large motifs, quiet composition, slow animation |
| Product / project control | Utility | Dense information, precise status, accessible controls |
| Motion + illustration | Atmosphere | Optional, non-blocking, reduced-motion alternative |
| Documentation | Trust | Searchable, versioned, human- and agent-readable |

**Source reference:** The supplied navy/cream/blue celestial illustration with an orbit-like circular wave, crescent and delicate gold marks. Derived previous app, web and branding boards are *exploration*, not approved finished assets.

## 03. Visual DNA

### Palette — proposed tokens, not color-certified

| Name | HEX | Intent |
|---|---|---|
| Midnight navy | `#0B1828` | Signature deep background |
| Deep panel | `#14283A` | Dark surfaces, secondary depth |
| Warm ivory | `#F7E9D8` | Paper warmth, light illustration |
| Mist blue | `#85A3BE` | Atmospheric movement and depth |
| Muted gold | `#D8B383` | Fine constellation lines and focused actions |
| Soft sand | `#D7C2A8` | Warm secondary contrast |
| Dark ink | `#1F2D3A` | Readable body text on light surfaces |

**Usage proportions (illustrative, not a hard rule):** 65–75% background/surface, 20–30% neutral/secondary, 5–10% accent. Dark app surfaces should be materially quieter than artwork. Gold must not carry status meaning alone.

### Functional semantic colors

| Status | Token | Suggested HEX | Display |
|---|---|---|---|
| Backlog / To do | `status.todo` | `#788C9D` | Label + color |
| In progress | `status.progress` | `#668BB0` | Label + color |
| Review | `status.review` | `#BE965A` | Label + color |
| Done | `status.done` | `#4F9C80` | Label + check |
| Blocked | `status.blocked` | `#C56865` | Label + icon |

Status hues are candidates; validate contrast on their *actual* backgrounds and for color-vision differences before release.

### Light and dark

- **Light:** `#FBF7F1` app background / `#FFFFFF` card surface / `#1F2D3A` text.
- **Dark:** `#0B1828` background / `#14283A` card surface / `#F7E9D8` main text.
- Both themes must preserve the **same navigation, fields, hierarchy, status semantics and interactions**.
- Theme preference: System / Light / Dark. Do not treat them as separate products.
- Accessibility target: WCAG 2.2 AA where applicable; measure and fix actual contrast, focus, error identification and non-text contrast, not simply appearance.

## 04. Signature motifs

| Motif | Construction | Best placement | Avoid |
|---|---|---|---|
| Orbital circle | 1–3 thin arcs, sparse alignment nodes, open center | Brand mark, splash, hero | Repeated full-size in each cell |
| Crescent | Clean asymmetrical shape, wide negative space | Identity, seasonal page | Decorative moon beside all actions |
| Wave ribbon | 2–4 smooth layered blue/ivory bands | Illustration, cover, footer | Behind body text |
| Cloud curl | Hand-drawn soft grouped curls | Empty state, hero edge | Dense UI backdrop |
| Star compass | 4 or 8 readable points, sparing | Dividers, milestones | Sparkle clutter |
| Gold connector | Thin rule, one dot or star | Section transitions | Gold frames around everything |

**Complexity rule:** One dominant motif per composition; remaining motifs support it. In product views, the *logo can be the only motif*.

### Minimum use size

- Full illustrative ring: preferably 160 px or larger.
- Simplified emblem: verify legibility at 24 px.
- Tiny contexts (favicon at 16 px): use a **single-star or simple crescent candidate**, not detailed waves.
- Stroke weight: must survive intended pixel density and print output; proof before production.

## 05. Logo / marks

**Current status:** Candidate SVG studies, *not* trademark-cleared final logos.

- Primary: horizontal name + independently drawable orbital symbol.
- Secondary: simplified symbol-only variant for app/icon/avatar.
- Monochrome: prepare navy-on-ivory and ivory-on-navy versions.
- Clear space (working rule): at least the height of the logo's central star on every side.
- No forced gradient, 3D bevel, unnecessary shadows, rotated wordmark, or stretched ring.
- No claim that generated letters or the LUNARA/ORBITRA mockups are authorized Sky Vision marks.
- Before finalization: owner selection, optical cleanup, small-size test, exact vector mastering, trademark/domain review and publication approval.

## 06. Typography

**Working pair:** Editorial serif (Georgia/Times fallback) + modern utility sans (Inter/system fallback).

- Marketing headings: serif, balanced tracking, restrained uppercase.
- Dashboards and dense interfaces: sans; predictable metrics and numeric alignment.
- Utility body: 15–16 px preferred; 14 px lower limit for dense metadata only.
- Titles have clear hierarchy; long text remains left-aligned in LTR or right-aligned in RTL.
- Persian: licensed Persian interface font needed; no artificially letter-spaced Persian. Test RTL punctuation, numbers and truncation.
- Real type licensing, webfont subsets and Persian glyph coverage are **open decisions**.

## 07. Grid and spacing

- Base spacing increment: 8 px; 4/8/16/24/32/48 scale.
- Border radii: 8/12/16 px; pill only for chips and compact badges.
- Desktop sidebar proposed 240 px, collapsible.
- Header proposed 64 px; touch targets target at least 44 x 44 px in mobile contexts.
- Use 8/12 column marketing layout; functional dashboard grid can be customized for density.
- Never let decoration shrink usable work area or reduce data scanning speed.

## 08. UI architecture: product-control baseline

The product must be useful with **zero uploaded images**.

**Primary objects:** Workspace → Project → Board / Phase → Task → Subtask / Checklist; users, roles, files and comments are related objects. Projects own customizable statuses and field schemas.

**Views:** List (default low-bandwidth), Kanban, Timeline/Gantt, Calendar, Dashboard. All views access the **same underlying task data**, not duplicated cards.

**Task card (essential):** Title, status, assignee, due date, priority, blocked indicator. Image thumbnail is optional and must never replace task text.

**Task details:** Description, customizable fields, status history, checklist, dependencies, attachments, comments, activity and permissions. Honor user-defined statuses and status colors.

**Priority design rule:** Actions in order of importance: create/find/edit/move a task → inspect progress/blockers → organize phases → admire the art.

### Core UI states to design and test

Empty project, no search results, loading/skeleton, offline, permission denied, error/retry, unsaved edit, conflict resolution, success, overdue, blocked and archived. Include labels and recovery actions, not only illustrations.

### Motion

- Micro-interaction 120–240 ms is a candidate, not a hard prescription.
- Respect `prefers-reduced-motion`.
- No sound/music by default. Animations must never be required to understand status.

## 09. Website system

- Hero expresses identity once; immediately provide product/portfolio clarity.
- Proposed IA: Overview / Product or Services / Work / About / Resources / Contact.
- Use the wave/orbit motifs at hero/footer transitions, not every content card.
- Editorial art uses larger negative space; forms and utility pages use accessible plain surfaces.
- Responsiveness: preserve headline scale, navigation visibility and legible tap targets.

## 10. Brand writing and microcopy

| Surface | Tone | Sample (candidate) |
|---|---|---|
| Brand headline | Poetic but concrete | `A clearer view of creative production.` |
| Product navigation | Direct | `Projects`, `Tasks`, `Timeline` |
| Empty board | Helpful | `No tasks yet. Create the first task.` |
| Error | Accountable | `Could not save changes. Retry.` |
| Confirmation | Specific | `Task moved to Review.` |

Avoid euphemisms that obscure whether work was saved, vague AI claims, forced cosmic metaphors and fabricated statistics.

## 11. Applications & quality bar

- **App:** Light/dark, high-density task UI, consistent semantic colors.
- **Website:** Hero, product page, about, responsive.
- **Brand stationery:** Business card, digital letterhead, social templates only after mark is selected.
- **Print:** Proof gold and navy with real ink/paper; never assume screen RGB translates directly to CMYK.
- **Export:** SVG for editable marks/motifs, transparent PNG for composition, PDF for review, accessible HTML/CSS for product.
- **QA:** Test 16/24/48 px marks, color contrast, typography, RTL, focus, zoom, reduced motion, no-image tasks and 320 px mobile layouts.

## 12. Governance and open approvals

**Current proposals:** visual direction, colors, typography approach, signature motifs and Sky Vision mark explorations.

**Not yet approved:** final logo design, legal/trademark rights, registered brand claim, exact palette, licenses for font/assets, brand tagline, motion standards and final product navigation taxonomy.

**Change process:** record `current → proposed`, reasoning, affected artifacts, migration, testing and rollback. Owner approval is required for canonical brand changes. Add ADR; increment brand-book version; keep original files immutable.

## Appendix: references and continuity

- `assets/reference/`: original user-provided source illustration (included in prior archive).
- `assets/concepts/`: original exploration boards, some with temporary LUNARA/ORBITRA names.
- `assets/svg/`: draft vector marks and decorative studies.
- `assets/ASSET_REGISTER.md`: authoritative provenance and repository presence status.
- `ROADMAP.md`: release plan and acceptance gates.

This markdown is the **canonical editable book**. Any PDF must report the same version and be regenerated from the current source before publication.
