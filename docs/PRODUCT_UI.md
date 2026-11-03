# Sky Vision — Project-Control Product UI Specification (v0.1)

## Principle
A fast, legible application for creative production that works from day one with **no images**. Images and illustrated brands add personality, never essential functionality.

## Domain model
`Workspace → Project → Phase/Board → Task → Subtask`. Linked: assignee, custom status, custom field schema, dependency, attachment, comment, activity record, deadline and permissions.

Task fields (minimum): stable ID, title, project ID, status ID, priority, owner, created/updated, due date and optional body. Status has stable ID, editable label, color, display order and archival flag. Do not persist only hex color as status identity.

## Primary navigation
- Home / Overview
- Projects
- My Tasks
- Boards
- Timeline
- Calendar
- Reports
- Workspace settings

Keep side navigation consistent in LTR and RTL; keyboard navigation and proper landmarks required.

## MVP screens
1. **Overview**: 3–5 simple metrics and relevant recent tasks; no card imagery needed.
2. **Project list**: name, owner, status, completion, upcoming due items; table and search.
3. **Kanban**: custom status columns; draggable or keyboard-movable tasks; same state as list.
4. **List/table**: dense sortable and filterable tasks with bulk actions.
5. **Task detail**: editable fields, history, checklist, comments, dependencies and attachment slot.
6. **Settings**: statuses (add/remove/reorder/color), custom fields, System/Light/Dark, density.

## Task card design
Default: title, status, owner initials, due date, priority and blocked state. Thumbnail is optional and no placeholder should waste space. Compact, standard, expanded density modes. Full data must remain accessible without hovering.

## Interactions
- Add/edit task, drag or keyboard-move between statuses.
- Show saving/saved/failed states. Failed edits require retry and do not silently disappear.
- Search and filters preserve state and offer a clear reset action.
- Support multiple users, conflicts and permission-denied messages.
- Custom field layout can be reordered by workspace roles with a reset option.
- Honor `prefers-reduced-motion`; never autoplay audio.

## Semantics and accessibility
Buttons have accessible names; correct focus indicator; contrast evaluated against real surfaces; status has both text and color; error messages explicitly name action; keyboard alternatives to all drag/drop actions; at least 44px touch targets where applicable; RTL and zoom tested.

## Themes
Use semantic design tokens. Dark mode: subdued surfaces, enough contrast, low decorative density. Light mode: warm paper background and restrained gold actions. Status names and data hierarchy must match exactly.

## Edge-case design states
Empty workspace, empty board, no search results, loading, offline, save conflict, API failure, no permission, missing asset, overdue, blocked, archived, success confirmation, slow sync. Each state includes specific recovery action.

## Acceptance scenarios
- User creates a project and 8 tasks without uploading an image.
- User creates a custom “QC” status with a selected color; all views reflect it.
- User changes theme without losing edits.
- User searches and opens the correct task from List and Kanban.
- User receives useful feedback when save fails and can recover.

**Status:** Specification, not a claim of implemented software.
