# Asset Register — provenance and repository presence

**Do not infer upload from a filename.** This register records assets supplied/generated in the conversation and the previous downloadable archive. Each raster file must be marked **GitHub: pending** until its Git blob is verified.

## Original supplied aesthetic reference
| Archive path | Source | Repository status |
|---|---|---|
| `assets/reference/original-celestial-artwork.jpeg` | User-uploaded illustration | Pending binary transfer |

## Historical exploratory concepts
| Archive path | Content | GitHub status |
|---|---|---|
| `assets/concepts/branding/lunara-brand-identity-board.png` | Branding direction, LUNARA placeholder | Pending |
| `assets/concepts/website/lunara-website-concept.png` | Website direction | Pending |
| `assets/concepts/app/lunara-mobile-dark.png` | Dark mobile layouts | Pending |
| `assets/concepts/app/lunara-mobile-light.png` | Light mobile layouts | Pending |
| `assets/concepts/app/lunara-states-scenarios.png` | Empty, error, loading, offline and success | Pending |
| `assets/concepts/app/lunara-expanded-journey.png` | Onboarding, filters, activity and calendar | Pending |
| `assets/concepts/project-management/skyvision-project-management-concept.png` | PM concept with ORBITRA placeholder | Pending |
| `assets/concepts/motifs/celestial-motif-sheet.png` | Motifs sheet | Pending |
| `assets/concepts/motifs/celestial-pattern-quartet.png` | Pattern studies | Pending |
| `assets/concepts/motifs/celestial-clipart-sheet.png` | Decorative motif library | Pending |
| `assets/concepts/motifs/celestial-background-quartet.png` | Light/dark backgrounds | Pending |

## Newly generated design production attempt (not part of the 12-source manifest)

### Added production assets

| Inventory ID | File | QC result |
|---|---|---|
| BG-01 | `assets/production/BG/BG-01.png` | 1672×941 RGB; centered open circular 2D wave/cloud/orbit hero on midnight navy; draft, below 4K target. |
| BG-02 | `assets/production/BG/BG-02.png` | Revised 1672×941 RGB; quiet navy negative space, fine corner orbits, small compass star and restrained lower 2D ribbon wave. Preview inspected; draft, not text-contrast tested or approved. |
| BG-03 | `assets/production/BG/BG-03.png` | 1672×941 RGB; warm ivory with broad open area, quiet pale-blue wave and sparse gold stars. Batch preview inspected; draft, text-contrast/print not tested. |
| BG-04 | `assets/production/BG/BG-04.png` | 1672×941 RGB; visual pass as quiet ivory utility background, open center, restrained lower wave/clouds and sparse gold orbit lines. Draft; not contrast-tested or approved. |
| BG-05 | `assets/production/BG/BG-05.png` | 1672×941 RGB; quiet ivory document background with ample reading space and a single lower-right ribbon motif. Draft; not print-tested or approved. |
| BG-07 | `assets/production/BG/BG-07.png` | 941×1672 RGB; warm light mobile wallpaper with lower circular 2D ribbon motif and clear upper field. Draft. |
| BG-08 | `assets/production/BG/BG-08.png` | 1672×941 RGB; 2D wave footer divider along lower edge, clear field above. Draft. |
| BG-09 | `assets/production/BG/BG-09.png` | 1254×1254 RGB; dark orbital repeat tile. 2×2 tiled preview has no obvious seam; exact pixel seamlessness not certified. Draft. |
| BG-10 | `assets/production/BG/BG-10.png` | 1254×1254 RGB; light cloud/wave/orbit repeat tile. 2×2 tiled preview has no obvious seam; exact pixel seamlessness not certified. Draft. |
| BG-11 | `assets/production/BG/BG-11.png` | 1672×941 RGB; midnight title background with open left text area and 2D ribbon/orbit artwork weighted right. Draft. |
| BG-12 | `assets/production/BG/BG-12.png` | 1672×941 RGB; minimal midnight orbit-only backdrop with clear center. Draft. |
| IC-01 | `assets/production/IC/IC-01.png` | 1600×900 RGB; five primary navigation icon concepts on midnight navy. Rendered from editable `IC-01.svg`; draft, not tested at 16px. |
| IC-02 | `assets/production/IC/IC-02.png` | 1600×900 RGB; Calendar, Files, Search, Alerts and Settings secondary navigation concepts. Rendered from editable `IC-02.svg`; draft, not tested at 16px. |
| IC-03 | `assets/production/IC/IC-03.png` | 1600×900 RGB; Add Task, Edit, Complete, Due Date and Delete concepts. Rendered from editable `IC-03.svg`; preview inspected; draft, not tested at 16px. |
| BG-06 | `assets/production/BG/BG-06.png` | Revised 941×1672 RGB; 2D circular ivory/mist-blue ribbon with cloud curls and gold orbits; upper clock-safe area. Preview inspected; draft, device crop not tested. |
| MO-01 | `assets/production/MO/MO-01-logo-signature.gif` | 640×640, 36 frames, 90 ms/frame, infinite loop; code-drawn animation, reviewed visually. |
| MO-02 | `assets/production/MO/MO-02-orbit-loop.gif` | 640×640, 24 frames, 90 ms/frame, infinite loop; seam mean absolute RGB difference 0.18/255. |
| MO-03 | `assets/production/MO/MO-03.png` | Revised 1672×941 RGB 16:9 motion storyboard; three phases of one 2D ribbon ring, first/last frame composition matches. Draft; not an animation. |
| IC-01 | `assets/production/IC/primary-navigation-icons.svg` | Original vector family of five navigation symbols; SVG parses and scales cleanly. |

These are drafts, not approved brand assets. Generated PNGs are 1672px/941px class, below the 4K delivery target. GIF quality is suitable for small web previews; use the source SVG/geometry to make larger motion exports. Manifest hashes, exact dimensions and statuses are in `assets/RASTER_MANIFEST.json` and `production/ASSET_INVENTORY.json`.

### Current generated assets

| Path | Dimensions / format | QC | Status |
|---|---|---|---|
| `assets/raster/skyvision-hero-01.png` | 1672×941 RGB PNG | Individually inspected: one crescent/orbit scene, no text, clean wide composition. Good for web preview; below 4K production target. | Draft |
| `assets/raster/skyvision-moon-orbit-01.png` | 1254×1254 RGBA PNG | Failed visual edge QC: unwanted bright fringe/noise around motif. Kept as rejected iteration for traceability. | Rejected; do not use |
| `assets/raster/skyvision-crescent-cutout-01.png` | 1254×1254 RGBA PNG | Alpha channel confirmed, but visual inspection still shows fringe/noise; not accepted as a clean cutout. | Rejected; do not use |

Hashes and file sizes are maintained in `assets/RASTER_MANIFEST.json`. User-supplied references and their roles are listed in `assets/ATTACHED_REFERENCE_MANIFEST.json`.

| Planned output path | Source | GitHub status |
|---|---|---|
| `assets/production/BG/BG-01.png` | Generated dark celestial hero background | **DRAFT — present in GitHub; hash and dimensions recorded; not approved** |

See [production inventory](../production/ASSET_INVENTORY.json) for the 166-asset backlog. All twelve BG draft files are present and recorded; none are approved.

## Live vector asset studies
New original SVG motif studies under `assets/svg/` are editable **proposals**. Their existence does not imply final logo approval.

### Isolated transparent vector motifs

| File | Subject | QC |
|---|---|---|
| `assets/svg/skyvision-crescent-motif.svg` | Crescent with small orbit/star details | XML parses; viewBox present; no background rectangle; rendered preview inspected. |
| `assets/svg/skyvision-cloud-curl-motif.svg` | Single cloud curl flowing into a ribbon | XML parses; viewBox present; no background rectangle; rendered preview inspected. |
| `assets/svg/skyvision-compass-star-motif.svg` | Four-point compass star and orbit rings | XML parses; viewBox present; no background rectangle; rendered preview inspected. |
| `assets/svg/skyvision-seamless-pattern-dark.svg` | Midnight repeat pattern tile | SVG pattern tile repeats at 256×256; rendered 2×2 preview; internal join RGB difference 0. |
| `assets/svg/skyvision-seamless-pattern-light.svg` | Warm ivory repeat pattern tile | SVG pattern tile repeats at 256×256; rendered 2×2 preview; internal join RGB difference 0. |

The three motif SVGs are transparent cutouts; the two pattern SVGs are opaque repeat backgrounds. All five are outside the 166-image inventory and remain editable proposals. They do not replace or redefine the circular primary logo study.

## Asset submission protocol
1. Confirm artwork publishing permissions and repository visibility.
2. Copy originals byte-for-byte from the downloadable archive without renaming internally.
3. Add SHA-256, pixel dimensions, source label, creation date (if known) and license state to a machine-readable manifest.
4. Validate hash equality to archived copy.
5. Commit in a branch; tag or archive old versions; do not rewrite originals.
6. Update this register from Pending to Verified only after GitHub fetch confirms the binary.
