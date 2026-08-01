# Memory

Long-lived repository notes for agents and humans: hardware facts, user
preferences, validated workflows, troubleshooting lessons, and external
references.

Memory is not auto-loaded. Discover pages with `qmd` when available; otherwise
use `rg`. Before writing, search first and update an existing related page when
possible.

## Index

- [X2D setup](x2d-setup.md) — stable hardware capabilities and verification
  boundaries.
- [MakerWorld workflow](makerworld-workflow.md) — Handy-first routing and the
  complete profile preflight.
- [Build-plate-holder PETG case](cases/2026-07-27-build-plate-holder.md) — warp,
  likely layer shift, and dual-nozzle support-interface routing.
- [X2D/P2S poop-bin preflight](cases/2026-07-28-poop-bin.md) — a support-free
  profile appropriately routed to Handy.
- [X2D no-logo toolbox preflight](cases/2026-07-28-toolbox.md) — exact 3MF
  inspection and plate selection.
- [IKEA SKADIS tool-holder preflight](cases/2026-07-31-skadis-tool-holder.md) —
  cross-printer Handy conversion and comparison of two support-free profiles.

## Scope

Use memory for:

- User preferences, feedback, and corrections.
- Stable hardware capabilities and recurring workflow constraints.
- Validated diagnostic approaches and reusable failure lessons.
- Dated case histories that explain why a rule exists.
- Pointers to upstream profiles, documentation, and tools.

Do not use memory for:

- Planned prints and TODOs; use GitHub issues.
- A full record of every print; use `prints/`.
- Model files or generated slicer output; use `models/` subject to its policy.
- Facts that can be derived directly from a checked-in artifact.
- Secrets, device identifiers, account data, private paths, or other details
  unsuitable for a public repository.

## Format

Each memory page is one Markdown file with frontmatter:

```yaml
---
name: kebab-case-slug
description: one-line summary used in search results
type: user | feedback | project | reference
status: active | resolved # project notes only; omit for other types
---
```

Types:

- `user`: user facts and preferences.
- `feedback`: corrections and validated ways of working.
- `project`: non-derivable ongoing context. Use absolute dates and include
  `status`.
- `reference`: stable external facts, diagnostic knowledge, and case history.

For `feedback` and `project` pages, lead with the rule or fact and then explain:

```text
**Why:** the evidence, past incident, constraint, or strong preference.

**How to apply:** when and where the guidance takes effect.
```

Use `[[page-name]]` to cross-link memory pages. Keep this index updated whenever
a page is added, moved, or removed.

## Archive

Move stale or superseded notes into `memory/archive/`. A resolved `project`
page must have `status: resolved`. Archived pages stay in Git history but are
excluded from qmd indexing so outdated guidance does not compete with active
knowledge.
