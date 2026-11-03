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

## Live vector asset studies
New original SVG motif studies under `assets/svg/` are editable **proposals**. Their existence does not imply final logo approval.

## Asset submission protocol
1. Confirm artwork publishing permissions and repository visibility.
2. Copy originals byte-for-byte from the downloadable archive without renaming internally.
3. Add SHA-256, pixel dimensions, source label, creation date (if known) and license state to a machine-readable manifest.
4. Validate hash equality to archived copy.
5. Commit in a branch; tag or archive old versions; do not rewrite originals.
6. Update this register from Pending to Verified only after GitHub fetch confirms the binary.
