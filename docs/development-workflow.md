---
status: current
---

# Development workflow

This page records this project's own commands and integrations. Shared rules
are in the [foundation pages](foundation/README.md).

## Setup

```sh
bin/setup
bin/doctor
bin/check --full
```

Setup needs Git and Python 3.9 or later, and checks also need ShellCheck.
QMD and direnv are optional; setup reports skipped features. Install td and
run `td init` as described in [task tracking](foundation/task-tracking.md).
Create `.envrc` only when the project needs environment settings, and review
it before running `direnv allow`; search does not need it.

## Knowledge search

Search covers `memory/` and `docs/`. Print records in `prints/` and model
notes in `models/` keep their own formats and are not indexed; read them
directly. Memory pages, including the dated cases in `memory/cases/`, follow
the [memory format](../memory/README.md#format), and each page's `name`
matches its filename.

## Checks

Follow the [check schedule](foundation/engineering-policy.md#checks). The
project has no application build or test suite and no `bin/check-application`,
so `bin/check --full` runs only the foundation checks.

GitHub validation is defined in [the workflow](../.github/workflows/check.yml),
which runs `bin/check --full` on pull requests and pushes to `main`.

## Runtime and toolchain versions

The project has no application runtime. Foundation checks need Python 3.9 or
later and ShellCheck; CI runs them on Ubuntu 24.04. Each committed model
records the CAD and slicer versions used to produce its exports in its own
README, as the [models policy](../models/README.md#required-provenance)
requires.

## Deployment

Nothing deploys from this repository. Pushing `main` publishes the notes,
records, and redistributable models to GitHub.

## Project Starter

`.project-starter.json` records the installed Project Starter release and the
hashes of its managed files. Update them with Project Starter's `bin/sync`,
and record any intentional local change as an override with its reason.
