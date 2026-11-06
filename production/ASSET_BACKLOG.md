# Sky Vision — Complete Visual Asset Production Backlog

**Status:** Proposed execution queue · 2026-11-06
**Total:** 166 individually tracked deliverables across 14 families.
**Current inventory snapshot:** 20 drafts, 146 queued, 0 approved (see `ASSET_INVENTORY.json`).
**Active work:** All 12 background IDs now have repository PNG drafts. BG-09/10 PNG drafts are not pixel-seamless-certified; exact-repeat light/dark SVG masters are available under `assets/svg/`. LG-03 has an exploratory PNG and a separate editable SVG study; both remain unapproved.

## How to use this list

This file is the human-readable **visual production list of work to do** in the repository. Every row below is a planned task with a stable ID, priority and status. `queued` means the task remains to be done; it does not mean an output exists. The machine-readable `ASSET_INVENTORY.json` is authoritative for live status and exact file paths. Generate queued visuals in coherent batches first, preserving one standalone deliverable per ID; then run QC across the batch and revise failed items before moving them to review. Update the list and inventory as each batch is added. Draft work is not approved identity. Operational documents such as PowerPoint and contract templates are tracked separately in [`DOCUMENT_BACKLOG.md`](DOCUMENT_BACKLOG.md).

> **Exactly one standalone image per visual asset ID**. If a deliverable contains an icon collection, make one clean overview sheet, not several unrelated collages. Do not combine unrelated IDs into one image. Batch generation is allowed; QC and owner review remain required before approval.

## Production status

- **Queued** — not yet produced.
- **Draft** — a visual attempt exists; no approval implied.
- **Review** — candidate filed with proof, awaiting approval.
- **Approved** — explicit owner sign-off, file in GitHub, manifest checked.
- **Blocked** — missing rights, reference, decision or implementation.

## Scope

| Family | Count | Current state |
|---|---:|---|
| BG — Backgrounds | 12 | 12 draft; 0 queued |
| LG — Logo and marks | 10 | LG-03 draft; 9 queued |
| CL — Color system | 8 | Queued |
| TY — Typography | 8 | Queued |
| MT — Motifs and patterns | 14 | Queued |
| IC — Icons | 14 | IC-01/03 draft; 11 queued |
| DS — UI components | 20 | Queued |
| PM — Project-management screens | 16 | Queued |
| MB — Mobile product screens | 10 | Queued |
| ST — UX states and edge cases | 12 | Queued |
| WB — Website and marketing | 12 | Queued |
| AP — Brand applications | 14 | Queued |
| MO — Motion | 8 | Queued |
| QA — Production QA and handoff | 8 | Queued |

## Full asset list

### BG — Backgrounds

Hero and utility imagery. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| BG-01 | Primary dark celestial hero background | P0 | draft |
| BG-02 | Quiet secondary dark background | P0 | draft |
| BG-03 | Primary light celestial hero background | P0 | draft |
| BG-04 | Quiet secondary light background | P0 | draft |
| BG-05 | Minimal slide/document background | P1 | draft |
| BG-06 | Mobile dark celestial wallpaper | P1 | draft |
| BG-07 | Mobile light celestial wallpaper | P1 | draft |
| BG-08 | Footer wave divider background | P1 | draft |
| BG-09 | Dark seamless repeat tile | P1 | draft |
| BG-10 | Light seamless repeat tile | P1 | draft |
| BG-11 | Presentation title background | P1 | draft |
| BG-12 | Abstract orbit-only UI backdrop | P1 | draft |

### LG — Logo and marks

Master identity tests. Default aspect **1:1**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| LG-01 | Primary logotype lockup horizontal | P0 | queued |
| LG-02 | Primary stacked mark lockup | P0 | queued |
| LG-03 | Symbol only study | P0 | queued |
| LG-04 | Compact micro-icon mark | P0 | queued |
| LG-05 | One-color dark mark | P1 | queued |
| LG-06 | One-color light mark | P1 | queued |
| LG-07 | Clear-space and safety-zone diagram | P1 | queued |
| LG-08 | Optical size 16/24/48/128 test | P1 | queued |
| LG-09 | Forbidden-logo-usage comparison | P1 | queued |
| LG-10 | Logo signature animation keyframe | P1 | queued |

### CL — Color system

Swatches, semantic usage and proof. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| CL-01 | Primary brand palette sheet | P0 | queued |
| CL-02 | Extended support palette sheet | P0 | queued |
| CL-03 | Light theme neutral scale | P0 | queued |
| CL-04 | Dark theme neutral scale | P0 | queued |
| CL-05 | Semantic status palette + noncolor examples | P0 | queued |
| CL-06 | Accessible text-on-surface combinations | P0 | queued |
| CL-07 | Gold accent and print approximation | P1 | queued |
| CL-08 | Color misuse examples | P1 | queued |

### TY — Typography

Latin/Persian brand and product typesetting. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| TY-01 | Latin display and brand hierarchy | P1 | queued |
| TY-02 | Product UI type scale | P1 | queued |
| TY-03 | English–Persian font pairing comparison | P1 | queued |
| TY-04 | RTL title and body layout | P1 | queued |
| TY-05 | Numbers, dates and tabular alignment | P1 | queued |
| TY-06 | Responsive typography scale | P1 | queued |
| TY-07 | Readable dense-table typography | P1 | queued |
| TY-08 | Editorial wordmark lettering study | P1 | queued |

### MT — Motifs and patterns

Reusable celestial visual grammar. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| MT-01 | Core orbital motif study | P1 | queued |
| MT-02 | Crescent family | P1 | queued |
| MT-03 | Cloud curl family | P1 | queued |
| MT-04 | Wave ribbon family | P1 | queued |
| MT-05 | Star/compass family | P1 | queued |
| MT-06 | Gold-line dividers | P1 | queued |
| MT-07 | Corner ornaments | P1 | queued |
| MT-08 | Circular frames and badges | P1 | queued |
| MT-09 | Seamless orbital pattern | P1 | queued |
| MT-10 | Seamless wave pattern | P1 | queued |
| MT-11 | Minimal product decorative motifs | P1 | queued |
| MT-12 | Dark border ornaments | P1 | queued |
| MT-13 | Light border ornaments | P1 | queued |
| MT-14 | Celestial signature key visual | P1 | queued |

### IC — Icons

Product and brand icon sheets. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| IC-01 | Primary navigation icon family | P1 | draft |
| IC-02 | Secondary navigation icon family | P1 | draft |
| IC-03 | Task actions icon family | P1 | draft |
| IC-04 | Project and board actions | P1 | queued |
| IC-05 | Status and priority symbols | P1 | queued |
| IC-06 | File and media icons | P1 | queued |
| IC-07 | User and team icons | P1 | queued |
| IC-08 | Calendar and timeline icons | P1 | queued |
| IC-09 | Chart and report icons | P1 | queued |
| IC-10 | Notification and feedback icons | P1 | queued |
| IC-11 | Permission and security icons | P1 | queued |
| IC-12 | Search, filter and sorting icons | P1 | queued |
| IC-13 | App icon and favicon sizes | P1 | queued |
| IC-14 | RTL and disabled icon variants | P1 | queued |

### DS — UI components

Reusable accessible components. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| DS-01 | Primary / secondary / tertiary button sheet | P0 | queued |
| DS-02 | Text inputs / textarea / search | P0 | queued |
| DS-03 | Select / combo / autocomplete | P0 | queued |
| DS-04 | Checkbox / radio / switch | P0 | queued |
| DS-05 | Tabs and segmented selectors | P0 | queued |
| DS-06 | Navigation sidebar | P0 | queued |
| DS-07 | Top bar and breadcrumbs | P0 | queued |
| DS-08 | Status chips and tags | P0 | queued |
| DS-09 | Task cards compact and full | P0 | queued |
| DS-10 | Project cards no image | P0 | queued |
| DS-11 | Data tables and list rows | P0 | queued |
| DS-12 | Modal and confirmation dialog | P0 | queued |
| DS-13 | Drawers and inspectors | P1 | queued |
| DS-14 | Tooltips and popovers | P1 | queued |
| DS-15 | Pagination and infinite-list states | P1 | queued |
| DS-16 | Toast, banner and alerts | P1 | queued |
| DS-17 | Dropdown and context menu | P1 | queued |
| DS-18 | Progress and metric components | P1 | queued |
| DS-19 | Date picker and scheduling | P1 | queued |
| DS-20 | Keyboard focus and interaction states | P1 | queued |

### PM — Project-management screens

No-image workflow designs. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| PM-01 | Dashboard overview dark | P0 | queued |
| PM-02 | Dashboard overview light | P0 | queued |
| PM-03 | Project directory/list | P0 | queued |
| PM-04 | Create project wizard | P0 | queued |
| PM-05 | Kanban board with custom columns | P0 | queued |
| PM-06 | Dense tasks table | P0 | queued |
| PM-07 | Task details inspector | P0 | queued |
| PM-08 | Task field customization | P0 | queued |
| PM-09 | Status builder and palette picker | P0 | queued |
| PM-10 | Timeline and Gantt | P0 | queued |
| PM-11 | Calendar and agenda | P1 | queued |
| PM-12 | Dependencies / blocked tasks | P1 | queued |
| PM-13 | Team workload allocation | P1 | queued |
| PM-14 | Reports and analytics | P1 | queued |
| PM-15 | Files and asset review optional | P1 | queued |
| PM-16 | Workspace permissions and settings | P1 | queued |

### MB — Mobile product screens

Responsive app screens. Default aspect **9:16**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| MB-01 | Mobile home dashboard dark | P1 | queued |
| MB-02 | Mobile home dashboard light | P1 | queued |
| MB-03 | Mobile project directory | P1 | queued |
| MB-04 | Mobile Kanban condensed | P1 | queued |
| MB-05 | Mobile tasks list | P1 | queued |
| MB-06 | Mobile task detail edit | P1 | queued |
| MB-07 | Mobile quick-add workflow | P1 | queued |
| MB-08 | Mobile activity and notifications | P1 | queued |
| MB-09 | Mobile profile and theme settings | P1 | queued |
| MB-10 | Mobile navigation and search | P1 | queued |

### ST — UX states and edge cases

State-specific recoverable designs. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| ST-01 | Empty workspace | P1 | queued |
| ST-02 | Empty board and no tasks | P1 | queued |
| ST-03 | No search results | P1 | queued |
| ST-04 | Loading skeleton | P1 | queued |
| ST-05 | Offline and reconnecting | P1 | queued |
| ST-06 | Failed save with retry | P1 | queued |
| ST-07 | Unsaved changes conflict | P1 | queued |
| ST-08 | Permission denied | P1 | queued |
| ST-09 | Archived and read-only | P1 | queued |
| ST-10 | Overdue and blocked | P1 | queued |
| ST-11 | Success and confirmation | P1 | queued |
| ST-12 | Bulk-action and destructive confirmation | P1 | queued |

### WB — Website and marketing

Responsive pages. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| WB-01 | Marketing homepage desktop | P1 | queued |
| WB-02 | Product overview page | P1 | queued |
| WB-03 | Feature detail page | P1 | queued |
| WB-04 | Brand/about page | P1 | queued |
| WB-05 | Studio work and portfolio | P1 | queued |
| WB-06 | Case-study detail page | P1 | queued |
| WB-07 | Pricing/plan concept optional | P1 | queued |
| WB-08 | Contact and lead form | P1 | queued |
| WB-09 | Blog/journal landing | P1 | queued |
| WB-10 | Blog article typography | P1 | queued |
| WB-11 | Documentation/help center | P1 | queued |
| WB-12 | Marketing homepage mobile | P1 | queued |

### AP — Brand applications

Physical and digital brand touchpoints. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| AP-01 | Business card front and back | P1 | queued |
| AP-02 | Letterhead / document page | P1 | queued |
| AP-03 | Email signature template | P1 | queued |
| AP-04 | Presentation cover | P1 | queued |
| AP-05 | Presentation content slide | P1 | queued |
| AP-06 | Social feed square | P1 | queued |
| AP-07 | Vertical story 9:16 | P1 | queued |
| AP-08 | Professional profile banner | P1 | queued |
| AP-09 | YouTube / video cover | P1 | queued |
| AP-10 | Event poster and signage | P1 | queued |
| AP-11 | Notebook application | P1 | queued |
| AP-12 | Desk merchandise application | P1 | queued |
| AP-13 | Sticker / patch set | P1 | queued |
| AP-14 | Product one-page PDF cover | P1 | queued |

### MO — Motion

Single-frame design references (not functioning videos). Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| MO-01 | Logo animation storyboard | P2 | queued |
| MO-02 | Orbit parallax motion reference | P2 | queued |
| MO-03 | Hero ambient motion design | P2 | queued |
| MO-04 | Loading indicator keyframe | P2 | queued |
| MO-05 | Transition system | P2 | queued |
| MO-06 | Reduced-motion static fallback | P2 | queued |
| MO-07 | Notification/feedback motion reference | P2 | queued |
| MO-08 | Motion do-not guide | P2 | queued |

### QA — Production QA and handoff

Evidence and output standards. Default aspect **16:9**; final dimension/export policy: [DELIVERY_STANDARD.md](DELIVERY_STANDARD.md).

| ID | Deliverable | Priority | Status |
|---|---|---|---|
| QA-01 | Export size/ratio cheat sheet | P2 | queued |
| QA-02 | SVG/PNG/transparency inspection sheet | P2 | queued |
| QA-03 | Light/dark parity comparison | P2 | queued |
| QA-04 | Accessibility focus and contrast proof | P2 | queued |
| QA-05 | Persian RTL visual QA sheet | P2 | queued |
| QA-06 | Brand consistency do/don't sheet | P2 | queued |
| QA-07 | Small logo-size proof | P2 | queued |
| QA-08 | Design-to-code handoff diagram | P2 | queued |

## Sequencing / critical path

1. **BG-01** — approve/revise primary dark hero; preserve one-frame standalone composition. See [brief](briefs/BG-01.md).
2. Generate the remaining background family as a cohesive batch, then QC and revise each image against its ID brief.
3. Generate the logo-study batch while preserving separate files per ID; no final identity approval implied.
4. Generate the color and typography foundation batch; validate token contrast independently.
5. Generate motif and icon families in coherent batches, then foundations and PM flows.

The next candidate is not automatically approved or created by completing an earlier task. Every approval must be explicit; revise the queue after feedback.

## Acceptance gate for each ID

- [ ] Exactly one standalone output image with intended format and aspect.
- [ ] Native reference quality: 2D illustrative, no unintended photoreal 3D / plastic CGI.
- [ ] Consistent navy, ivory, desaturated blue, restrained gold; preserved motif family.
- [ ] Legible functional labels; product screens still work without pictures.
- [ ] Adequate negative space, safe area, correct typography/RTL where relevant.
- [ ] Export checked, no artifacts/false alpha, file integrity/size verified.
- [ ] Repository path and manifest provenance recorded; source protected.
- [ ] Explicit owner review; status then changed to approved.

Machine-readable [inventory](ASSET_INVENTORY.json) is authoritative for IDs, statuses and output paths. Never mark approved without a real GitHub file and recorded sign-off.
