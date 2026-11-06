# SKY VISION — Brand System / سیستم برند

> **Working design system · v0.1 · concepts are not approved final identity**

> **پایگاه کاری برند · نسخه‌ی ۰.۲ · طرح‌ها هنوز هویت نهایی تأییدشده نیستند**

## Brand database / پایگاه اطلاعات برند

**English:** This repository is the bilingual working source of truth for Sky Vision identity, product UI, visual assets, design tokens, provenance, and production planning. Browse the [Brand Database](preview/index.html) or read the [full overview in English and Persian](docs/BRAND_DATABASE.md).

**فارسی:** این ریپو مرجع دوزبانه‌ی هویت Sky Vision، رابط محصول، دارایی‌های بصری، توکن‌های طراحی، منشأ فایل‌ها و برنامه‌ی تولید است. [پایگاه برند](preview/index.html) را مرور کنید یا [معرفی کامل فارسی و انگلیسی](docs/BRAND_DATABASE.md) را بخوانید.

## Repository map / نقشه‌ی ریپو

| Path | Purpose |
|---|---|
| `brandbook/` | Brand book, approval matrix, export guidance / برندبوک و تأییدها |
| `tokens/` | Semantic design tokens / توکن‌های طراحی |
| `docs/` | Product, art direction, accessibility, bilingual database / راهنماها |
| `assets/svg/` | Editable motif studies / موتیف‌های برداری قابل ویرایش |
| `assets/raster/` | Generated visual drafts / پیش‌نویس‌های تصویری تولیدشده |
| `assets/reference/attached/` | Owner supplied reference images / تصاویر مرجع پیوست‌شده |
| `production/` | Asset briefs, inventory, quality and delivery rules / برنامه و کنترل کیفیت |
| `preview/` | Local browsable brand database / پایگاه قابل مرور |

### Current visual previews / پیش‌نمایش‌های تصویری

- [Signature key visual](assets/production/MO/MO-03.png) — standalone celestial artwork / تصویر کلیدی مستقل
- [Website homepage concept](assets/production/WB/WB-01-homepage-concept.html) — responsive editorial landing page / طرح صفحه‌ی فرود واکنش‌گرا
- [Animated signature](assets/production/MO/MO-01-logo-signature.gif) — looping GIF / گیف حلقه‌ای
- [Browse the production files](assets/production/) — backgrounds, icons and motion / پس‌زمینه، آیکون و موشن

Newly generated files and attached references are indexed in `assets/ASSET_REGISTER.md` and `assets/RASTER_MANIFEST.json`. Generated artwork remains draft until human acceptance.

Sky Vision is a celestial-inspired identity system for a creative studio and an **image-optional project-management product**. It combines a crafted editorial surface with practical, accessible, high-density workflows.

## Explore

- [Brand Book v0.1](brandbook/BRAND_BOOK.md) — positioning, visual grammar, palette, typography, logo rules, digital and print applications
- [Brand roadmap](ROADMAP.md) — milestones, priorities, acceptance criteria, owner decisions
- [Design tokens](tokens/skyvision.tokens.json) — semantic light/dark palette, spacing and typography
- [UI specification](docs/PRODUCT_UI.md) — boards, lists, details, timeline, statuses, no-image UI
- [Source asset ledger](assets/ASSET_REGISTER.md) — records of reference art and concept boards
- [Agent rules](AGENTS.md), [Skills](skills/), [Handoff](HANDOFF.md)
- [Persian overview](docs/fa/README.md)

## Working identity (not an approved trademark)

**Colors:** midnight navy, warm ivory, mist blue, muted gold, soft sand.  
**Motifs:** orbital arcs, crescent, sparse stars, stylized clouds and flowing bands.  
**Product principle:** clarity, control, legibility and speed first; illustration is decorative and may be disabled.

Our reference images include a celestial original and exploratory LUNARA/ORBITRA boards. Those names are not Sky Vision brand names and their UI copy is not normative.

## Change safety

- Original concept/reference images must never be overwritten. Preserve provenance, versions and owner approvals.
- Proposed changes to core brand, name, assets, product goals, or licensing require an explicit before/after review and approval.
- Accessible light/dark and image-free project management views are baseline requirements.
- Do not infer rights clearance or publication approval from a mockup or an AI-generated concept.

## Status

This repository houses **working documentation and original vector motif proposals**. Some earlier raster concept boards are preserved in the accompanying local archive but may not yet be uploaded to this GitHub repository. The [asset register](assets/ASSET_REGISTER.md) distinguishes recorded source material from repository-hosted files.

**License:** Not specified. No open-source reuse permission is granted by the presence of files in this repository.

## Production inventory — one asset at a time

See the bilingual [Work to Do list](production/WORK_TO_DO.md) for the practical remaining-work summary.

**166 proposed individual visual deliverables**, organized into 14 families. These are the full *work plan*, not completed images.

- [Full human-readable production backlog](production/ASSET_BACKLOG.md)
- [PowerPoint, contract and operational document backlog](production/DOCUMENT_BACKLOG.md)
- [Machine-readable inventory with IDs, status, priority and output paths](production/ASSET_INVENTORY.json)
- [Production/export standard](production/DELIVERY_STANDARD.md)
- [First item brief: BG-01](production/briefs/BG-01.md)
- [Reusable single-item brief](production/BRIEF_TEMPLATE.md)
- [UI component and screen inventory](docs/COMPONENT_CATALOG.md)
- [Repository gap audit](docs/REPOSITORY_AUDIT_2026-11-03.md)
- [Initial color contrast findings](docs/ACCESSIBILITY_COLOR_AUDIT.md)
- [Source/rights caution](docs/CONTENT_AND_RIGHTS.md)

**Active status:** BG-01 is an unapproved *draft* generated in conversation, **not yet a verified GitHub image file**. No visual output is marked approved. All original raster archive items remain pending transfer. Design and source files must not be asserted present simply because they are listed in metadata.

**Validation:** `python scripts/validate_repo.py`, `python scripts/check_inventory.py`, `python scripts/verify_raster_manifest.py`, `python scripts/contrast_audit.py`. Structural checks do not prove accessibility, design approval or CI-green status.

## Try the UI study

[Image-free interactive project board (HTML)](preview/index.html). It runs locally in a browser, uses localStorage only, and is **not** a hosted or production-ready service.

## Review queue

- [Original raster archive import and hash verification](https://github.com/iAlirezaaa/skyvision-brand-system/issues/1)
- [Master logo selection](https://github.com/iAlirezaaa/skyvision-brand-system/issues/2)
- [Contrast, accessibility, Persian typography](https://github.com/iAlirezaaa/skyvision-brand-system/issues/3)
- [Product UI componentization](https://github.com/iAlirezaaa/skyvision-brand-system/issues/4)

A **15-page visual PDF companion** exists in the downloadable source-assets package; it is not currently uploaded to this GitHub repository.
