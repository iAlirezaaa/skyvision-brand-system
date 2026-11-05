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

### Current generated assets

| Path | Dimensions / format | QC | Status |
|---|---|---|---|
| `assets/raster/skyvision-hero-01.png` | 1672×941 RGB PNG | Individually inspected: one crescent/orbit scene, no text, clean wide composition. Good for web preview; below 4K production target. | Draft |
| `assets/raster/skyvision-moon-orbit-01.png` | 1254×1254 RGBA PNG | Failed visual edge QC: unwanted bright fringe/noise around motif. Kept as rejected iteration for traceability. | Rejected; do not use |
| `assets/raster/skyvision-crescent-cutout-01.png` | 1254×1254 RGBA PNG | Alpha channel confirmed, but visual inspection still shows fringe/noise; not accepted as a clean cutout. | Rejected; do not use |

Hashes and file sizes are maintained in `assets/RASTER_MANIFEST.json`. User-supplied references and their roles are listed in `assets/ATTACHED_REFERENCE_MANIFEST.json`.

| Planned output path | Source | GitHub status |
|---|---|---|
| `assets/production/BG/BG-01.png` | A single dark celestial hero image generated in conversation (`celestial_yin_yang_orbit_in_midnight_blue.png`) | **DRAFT — source not verified in GitHub, not approved** |

See [production inventory](../production/ASSET_INVENTORY.json) for the 166-asset backlog. Do not include BG-01 as a hash-verified source image until the actual binary is transferred, its exact size and SHA-256 recorded, and permission confirmed.

## Live vector asset studies
New original SVG motif studies under `assets/svg/` are editable **proposals**. Their existence does not imply final logo approval.

## Asset submission protocol
1. Confirm artwork publishing permissions and repository visibility.
2. Copy originals byte-for-byte from the downloadable archive without renaming internally.
3. Add SHA-256, pixel dimensions, source label, creation date (if known) and license state to a machine-readable manifest.
4. Validate hash equality to archived copy.
5. Commit in a branch; tag or archive old versions; do not rewrite originals.
6. Update this register from Pending to Verified only after GitHub fetch confirms the binary.
