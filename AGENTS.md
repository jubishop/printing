# Printing

<!-- project-starter:begin -->
Project Starter manages this block; add project rules after it. Project rules
take precedence over this block and the foundation pages wherever they differ.

- Keep durable guidance and non-derivable context in [memory](memory/README.md),
  and designs, decisions, and research in [docs](docs/README.md). Before
  non-trivial work or writing memory, search with `bin/knowledge search "term"`
  or `bin/knowledge query "question" --no-rerank`, then read results with
  `bin/knowledge get <path> -l 80`. Markdown sources are authoritative.
- If configured QMD fails, follow `~/AGENTS.md` for a failed knowledge search,
  repairing it as
  [search failures](docs/foundation/knowledge-search.md#search-failures)
  describes.
- Follow the [engineering policy](docs/foundation/engineering-policy.md):
  fewer dependencies, red-green tests for behavior changes, cohesive files and
  pages, checkout-isolated validation, and the latest stable toolchains.
- Run [checks](docs/foundation/engineering-policy.md#checks) by change:
  `bin/check --documents-only` for text, the relevant checks while editing
  code, and `bin/check --full` before merging or releasing production code
  unless an enforced CI gate runs it. Reuse passing results.
- Keep accepted decisions separate from proposals, and keep generated caches
  out of Git. Keep secrets out of public repositories only; a private one may
  commit them.
- Run `bin/setup` after cloning, `bin/doctor` to diagnose setup, and
  `bin/qmd-index` after uncommitted knowledge edits. Managed files listed in
  `.project-starter.json` change only through Project Starter or a recorded
  override with its reason.
<!-- project-starter:end -->

## Project memory and tracking

This is a reference and model repository, not a development project. Do not
create GitHub issues for prints, troubleshooting, follow-ups, or user-only
steps such as signing in. This overrides issue-tracking and pending-step
requirements in the shared guidance. A print request is handled in its chat
or left unprinted; do not create a planned-print queue or persist routine
session blockers. Track progress in `docs/` only for a print or design that is
actively being iterated.

Besides memory and docs, repository context lives in:

- `prints/`: dated records of actual print attempts. Start from
  `prints/TEMPLATE.md` and record observed settings and outcomes, not intended
  settings alone.
- `models/`: stored models and profiles with provenance and licensing records.

## Print workflow

- Jubi uses a Bambu Lab X2D with 0.4 mm hardened-steel nozzles, as
  [X2D setup](memory/x2d-setup.md) records. Treat this as a hardware baseline
  and verify the active machine, plate, nozzle, and material assignments for
  every print, never inferring material from embedded profile provenance.
- Prepare every print, MakerWorld URLs included, with the
  [MakerWorld workflow](memory/makerworld-workflow.md): it chooses between
  Bambu Handy and Bambu Studio and gives the exact-profile preflight.
- For every print that needs supports, use the dedicated support filament for
  the support interfaces, expected on the auxiliary nozzle's external feed.
  Verify the live spool and final interface mapping, and ask Jubi before
  sending the print if the spool appears absent or can't be verified there.
- Jubi wants hands-on app help and a complete preflight. Verify UI state after
  each consequential action and do not claim a configuration or slice was
  checked when it was not.
- Immediately before sending a print, verify that every calibration control
  the app shows, such as Auto Bed Leveling, Flow Dynamics Calibration, and
  Nozzle Offset Calibration, is explicitly `Auto`. Do not send the job while
  any is `On`, `Off`, or a manual value.
- Do not start or send a physical print unless Jubi explicitly asks after the
  preflight.
- Treat settings in historical cases as evidence, not universal defaults.

## Public repository and artifacts

- Never commit credentials, Bambu account/session data, LAN access codes,
  printer serial numbers, private URLs or photos, or machine-specific absolute
  paths, including any embedded in 3MF or slicer-export metadata.
- Commit models, profiles, and slicer exports only as the
  [models policy](models/README.md) allows: a third-party one only once its
  redistribution terms, which no repository-wide license overrides, are
  checked and recorded, and never generated G-code. Set up Git LFS in the
  commit that first adds a large binary model or project file, not before.
