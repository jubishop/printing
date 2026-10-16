# Printing

<!-- project-starter:begin -->
Project Starter manages this block; add project rules after it. Project rules
take precedence over this block and the foundation pages wherever they differ.

- Keep durable guidance and non-derivable context in [memory](memory/README.md),
  and designs, decisions, and research in [docs](docs/README.md). Before
  non-trivial work or writing memory, search with `bin/knowledge search "term"`
  or `bin/knowledge query "question" --no-rerank`, then read results with
  `bin/knowledge get <path> -l 80`. Markdown sources are authoritative.
- If configured QMD fails, tell the user immediately and attempt repair. If
  repair fails, pause knowledge-dependent work until the user approves a
  fallback; never silently substitute `rg` or direct reads. See
  [search failures](docs/foundation/knowledge-search.md#search-failures).
- Use td for work with multiple stages, interruptions, blockers, or handoffs;
  run `td usage --new-session -q` once per new context and keep handoffs
  current. See [task tracking](docs/foundation/task-tracking.md).
- Follow the [engineering policy](docs/foundation/engineering-policy.md):
  fewer dependencies, red-green tests for behavior changes, flaky tests fixed
  or tracked in an issue, cohesive files and pages, checkout-isolated
  validation, and the latest stable toolchains.
- Deliver by [kind of change](docs/foundation/engineering-policy.md#kinds-of-change):
  commit text, such as Markdown and AI skill prose, directly on the default
  branch without checks; commit development code, such as tests, CI, and
  tooling, directly after its checks pass; and deliver production code through
  a pull request after its checks.
- Run [checks](docs/foundation/engineering-policy.md#checks) by change: the
  relevant checks while editing, and `bin/check --full` before merging or
  releasing production code unless an enforced CI gate runs it. Reuse passing
  results.
- Keep accepted decisions separate from proposals, preserve unrelated changes,
  and keep generated caches out of Git. Keep secrets out of public
  repositories only; a private one may commit them.
- Run `bin/setup` after cloning, `bin/doctor` to diagnose setup, and
  `bin/qmd-index` after uncommitted knowledge edits. Managed files listed in
  `.project-starter.json` change only through Project Starter or a recorded
  override with its reason.
<!-- project-starter:end -->

## Project memory and tracking

Repository context lives in `memory/`, `prints/`, and GitHub issues:

- `memory/`: long-lived setup facts, preferences, validated workflows,
  troubleshooting knowledge, and case histories. New or updated pages must follow
  `memory/README.md`; move stale notes to `memory/archive/`.
- `prints/`: dated records of actual print attempts. Start from
  `prints/TEMPLATE.md` and record observed settings and outcomes, not intended
  settings alone.
- GitHub Issues (`jubishop/printing`): planned prints, tuning tasks, failures to
  investigate, and other lifecycle-tracked work.

## Print workflow

- Jubi uses a Bambu Lab X2D with 0.4 mm hardened-steel nozzles. Treat this as a
  hardware baseline and verify the active machine, plate, nozzle, and material
  configuration for every print.
- When given a MakerWorld URL, inspect the exact selected profile, intended
  plate, and requested material before choosing a workflow.
- Prefer Bambu Handy on iOS when a compatible profile can be printed unchanged
  with ordinary filament mapping.
- Do not require Studio solely because the uploaded profile was authored for a
  different Bambu printer. If MakerWorld/Handy presents that exact profile as
  compatible after selecting X2D, cloud slicing can adapt it to the selected
  printer, filament, and plate while retaining important process choices.
- X2D compatibility does not make otherwise similar profiles equivalent. When
  multiple profile cards look alike, compare their actual support, strength,
  adhesion, speed, and compensation settings before recommending one.
- Use Bambu Studio for supports or support-interface routing, custom
  material/nozzle assignments, tuning, orientation, preview inspection, or any
  requested model/profile modification.
- Handy can preserve and map a dedicated support filament already encoded in a
  profile; it does not create that setup. If the mapping screen contains one
  filament, a separate support spool will not be used.
- Do not infer active material from embedded profile provenance. Verify project
  assignments, sliced preview, print mapping, and, when diagnosing a completed
  job, print history.
- A 3MF downloaded after filtering MakerWorld for X2D may still be the original
  uploader's printer-targeted file. Use it to inspect geometry and retained
  process choices, not as proof of the final cloud-sliced X2D machine settings;
  confirm live X2D eligibility and the final Handy mapping.
- Jubi wants hands-on app help and a complete preflight. Verify UI state after
  each consequential action and do not claim a configuration or slice was
  checked when it was not.
- Immediately before sending a print, verify that every available calibration
  control is explicitly set to `Auto`. This includes Auto Bed Leveling, Flow
  Dynamics Calibration, and Nozzle Offset Calibration when Bambu Studio shows
  them. Do not send the job if any available calibration is set to `On`, `Off`,
  or a manual value.
- Do not start or send a physical print unless Jubi explicitly asks after the
  preflight.
- Treat settings in historical cases as evidence, not universal defaults.

## Public repository and artifacts

- Never commit credentials, Bambu account/session data, LAN access codes,
  printer serial numbers, private URLs or photos, or machine-specific absolute
  paths.
- Do not commit third-party models or profiles until their redistribution terms
  have been checked and recorded. A repository-wide license cannot override an
  upstream asset's license.
- Record source URL, creator, profile ID, observed license and date, local
  modifications, and relevant tool versions alongside every committed model.
- Inspect 3MF and slicer exports for embedded metadata before committing them.
- Keep generated G-code out of Git. Introduce Git LFS before adding large binary
  model or project files; do not enable it speculatively.
