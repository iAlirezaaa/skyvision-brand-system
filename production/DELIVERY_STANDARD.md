# Sky Vision — Single-Asset Production Standard

**Applies to every** `production/ASSET_INVENTORY.json` **record.** This is a proposal, not a license grant or final brand approval.

## One ID = one deliverable image

Each asset is independently designed, rendered, inspected and reviewed. Do **not** combine unrelated backlog IDs into a mosaic. For a category explicitly calling for a sheet, create **one** tidy sheet showing its own variants only. Draft variations are internal and are not new deliverables.

## File naming and paths

- Main file: `assets/production/<FAMILY>/<ID>.png` (example: `assets/production/BG/BG-01.png`). Keep IDs stable after publication.
- Editable master when appropriate: `assets/editable/<FAMILY>/<ID>.svg` or an accepted source document; don't claim a raster is editable vector.
- Revision files: `<ID>-v02.png`, etc. Preserve older versions in `assets/archive/`; original user references remain immutable.
- Descriptive provenance: source, revision, tools/model if relevant, dimensions, rights/approval, SHA-256 and review decision.

## Visual-output quality targets (not proof of compliance)

| Type | Design frame | Recommended target |
|---|---|---|
| Desktop hero/background | 16:9 | 3840 × 2160 px |
| Desktop app / full website | 16:9 | 3840 × 2160 px |
| Mobile wallpaper/screens | 9:16 | 2160 × 3840 px |
| Marks, icon sheets, patterns | Square or sheet ratio | 2048 × 2048 px or SVG master |
| Standalone website divider | Wide | 3840 × 1080 px |
| Print applications | Physical layout | Vector/PDF master and print proof |

Generated draft resolution may be lower; do not claim 4K unless the actual exported dimensions qualify. Prefer real SVG geometry for marks/icons (not automatic traced noisy raster). One PNG preview per inventory ID remains the default review format.

## Reference lock

Use the supplied original celestial 2D illustration as the aesthetic anchor: deep midnight blue, ivory/light sand, smoky mist blue, delicate gold orbital lines, stylized cloud curls and layered wave ribbons. Maintain painterly but clean handcrafted 2D shapes, restrained fine lines and generous empty space. No photo, plastic 3D, neon glows, generic sci-fi HUD, typography over artwork unless requested, or unnecessary scene elements.

For utility backgrounds, central whitespace is mandatory. A decorative background must not reduce contrast or compete with UI data. UI screens must remain understandable in both themes without any image.

## File quality gate

1. Validate actual dimension and aspect, absence of unintended text/watermarks, and edge/pixel integrity.
2. Confirm real alpha channel where transparency is required; checkerboard-looking pixels are not transparency.
3. Test logo at 16/24/48px and screen content at realistic viewport sizes.
4. Check contrast on actual background and focus/error states. A mockup is not accessibility evidence.
5. Check Persian direction, shaping, numbers, minimum font size if applicable.
6. Record file hash, source/reference, rights/visibility, revision and explicit acceptance.
7. Add a review link and update `production/ASSET_INVENTORY.json`; run validators.

## Status transition

`queued → draft → review → approved` with **explicit owner acceptance**. Set `blocked` when source rights, design input or export checks fail. Revisions return to `draft`. Approval is never inferred from file existence.
