# Printing

Public notes, repeatable workflows, and redistributable artifacts for Jubi's
3D-printing projects.

The current setup centers on a Bambu Lab X2D with 0.4 mm hardened-steel
nozzles. The repository is intended to make each print reproducible without
turning the settings from one successful print into universal defaults.

## Workflow

For a MakerWorld print, start with the exact selected profile and intended
plate:

1. Use Bambu Handy when the X2D-compatible profile can be printed unchanged
   with ordinary filament mapping.
2. Use Bambu Studio when the job needs support-interface routing, custom
   material or nozzle assignments, tuning, orientation changes, sliced-preview
   inspection, or any model/profile modification.
3. Verify the active material assignments, plate, sliced preview, and final
   print mapping before starting the print.

See [the detailed workflow](memory/makerworld-workflow.md) for the full
preflight.

## Repository layout

- [`memory/`](memory/README.md): durable setup knowledge, workflow decisions,
  troubleshooting guidance, and historical cases.
- [`prints/`](prints/TEMPLATE.md): reproducible records of individual print
  attempts and outcomes.
- [`models/`](models/README.md): redistributable model files plus settings-only
  reconstruction recipes for licensed projects that cannot be republished.
- [GitHub issues](https://github.com/jubishop/printing/issues): the print queue,
  tuning work, and other lifecycle-tracked tasks.

## Recording a print

1. Open a print-job issue from the repository template.
2. Record the source URL, exact profile or profile ID, observed license, desired
   material, and intended result.
3. After printing, copy [`prints/TEMPLATE.md`](prints/TEMPLATE.md) to a dated
   file and record the actual configuration, result, photos, and lessons.
4. Update an existing memory page when the result changes durable guidance;
   do not use memory as a duplicate print log.

## Models and licensing

Downloaded models and print profiles are not committed merely because they are
available online. Record the upstream creator, URL, profile ID, license, and the
date the license was checked. Commit third-party files only when their terms
permit redistribution.

When a 3MF required manual work, preserve the reusable result according to its
license:

1. If redistribution is permitted, commit the configured 3MF under `models/`
   with its provenance and modification record.
2. If redistribution is prohibited or unclear, keep the configured 3MF under
   the ignored `.local/models/` tree and commit a settings-only preset or
   reconstruction recipe under `models/`. The recipe must identify the exact
   authorized upstream download and include enough preflight evidence to
   reproduce and verify the project.

There is currently no repository-wide license. Third-party materials retain
their upstream terms, and an individual original artifact may receive its own
license later.
