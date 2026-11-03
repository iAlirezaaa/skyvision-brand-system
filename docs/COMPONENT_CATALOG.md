# Sky Vision — Component Inventory and Implementation Gaps

**Scope:** UI product design backlog, not implemented functionality. Source: `docs/PRODUCT_UI.md` and `production/ASSET_INVENTORY.json`.

## Core components (P0)

| Component | Variants/states | Needs in QA |
|---|---|---|
| Button | primary, secondary, tertiary, disabled, loading, destructive | focus, accessible name, hit area, light/dark |
| Inputs | text, search, multiline, number, date, invalid, read-only | label, error, keyboard |
| Selection | select, combobox, checkbox, radio, switch | option nav, announcements |
| Table/list | sorting, filtering, selection, empty, loading | responsive density, keyboard |
| Task card | default, selected, blocked, overdue, optional image | all content without thumbnail |
| Status chip | editable name + color + icon/text | never color-only |
| Sidebar/nav | expanded, collapsed, mobile | focus order, RTL |
| Dialog/drawer | open, close, dirty, error | Escape, focus trap/return |
| Snackbar/alert | success, error, warning, offline | live region, recovery action |
| Project card | default without artwork, optional preview | task count and state readable |
| Date/calendar | selected, disabled, range, overdue | keyboard and locale |
| Timeline | drag/resize dependencies, milestone | keyboard alternatives, readable dates |
| Progress | fraction/count/percentage | actual numbers, not just color |
| Avatar/profile | initials fallback, image optional | no external-image dependency |
| Empty state | not-found, no tasks, no access | specific call to action |

## Product screen map

**P0:** Overview; Projects; Create Project; List/Board; Task Detail; Status Editor; Custom Fields; Settings. **P1:** Timeline, Calendar, Dependencies, Team Workload, Reports, Media Review. **P2:** Analytics comparisons, automation, templates, notifications.

## Engineering separation

The current `preview/index.html` is a local browser demonstration. It has no server auth, multi-user data model or transactional persistence. Do not claim it supports live collaboration or production resilience.

## Validation scenarios

- Start from an empty workspace and create a project plus tasks **without images**.
- Add/reorder/customize a status and see it reflected in List and Board.
- Use keyboard for every action, including task movement.
- Toggle theme without losing data or status meaning.
- Recover from network/offline/save failure.
- Switch English/Persian and check RTL alignment and number formatting.

## Cross-reference

One visual deliverable for each component board is planned under inventory IDs `DS-01` … `DS-20`. Actual implementation and test evidence are separate work items.
