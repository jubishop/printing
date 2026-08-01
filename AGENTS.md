# Printing

## Environment

The user is in Pacific Time. Use PST/PDT unless asked otherwise. The user's
default shell is fish.

## Project memory and tracking

Repository context lives in `memory/`, `prints/`, and GitHub issues:

- `memory/`: long-lived setup facts, preferences, validated workflows,
  troubleshooting knowledge, and case histories. Search before writing and
  update an existing note when possible. New or updated pages must follow
  `memory/README.md`; move stale notes to `memory/archive/`.
- `prints/`: dated records of actual print attempts. Start from
  `prints/TEMPLATE.md` and record observed settings and outcomes, not intended
  settings alone.
- GitHub Issues (`jubishop/printing`): planned prints, tuning tasks, failures to
  investigate, and other lifecycle-tracked work.

Use `qmd` for topic lookup when available:

- `qmd search "known term"` for printer names, model names, profile IDs, and
  exact settings.
- `qmd query "question" --no-rerank` for fuzzy or open-ended lookup.
- `qmd get <path>[:line] -l N` to fetch a page or slice.

Hooks under `bin/hooks/` refresh the local qmd index after Git operations once
`bin/install-hooks` has been run. If qmd is unavailable, use `rg` and read the
known files directly.

Cross-repository memory belongs in `~/memory/`; printing-specific knowledge
belongs in this repository.

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
