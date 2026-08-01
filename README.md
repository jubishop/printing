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
- [`models/`](models/README.md): model files only when their licenses permit
  redistribution, with provenance recorded alongside them.
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
permit redistribution; otherwise keep only provenance and print notes here.

There is currently no repository-wide license. Third-party materials retain
their upstream terms, and an individual original artifact may receive its own
license later.
