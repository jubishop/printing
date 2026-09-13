---
status: current
---

# Knowledge workflow

Printing uses the Project Starter search component for its memory and reference
documents. Existing print records and memory formats remain unchanged.

Run `bin/install-hooks` (or `bin/setup`) to prepare the repository search and
its Git hooks. Run `bin/doctor` for read-only diagnostics. Each checkout has a
separate index; existing model files are preserved.

## Search

From the root, use `bin/knowledge`. Setup also creates a repository-local
`git knowledge` alias when that name is free, so the command works from any
subdirectory. An existing alias is preserved.

```sh
git knowledge search "worktree" -c docs
git knowledge query "how should decisions be recorded" --no-rerank
git knowledge get qmd://docs/development-workflow.md -l 80
git knowledge context list
```

Choose keyword search for names and known terms. Use a semantic query for
broader questions. Read a focused source page before relying on a result.
Source Markdown remains authoritative. Known-file reads and broader source
searches after a successful lookup with no matches remain appropriate. Follow
the [failure policy](#search-failures) when a configured lookup fails.

The command supplies QMD configuration, cache, and database paths only to
the QMD process. It does not change the shell's cache directory or depend on
personal shell wrappers. It refuses named indexes to keep checkout isolation.
If an executable must be selected explicitly, use an absolute local setting:

```sh
git config --local knowledge.qmdPath /absolute/path/to/qmd
```

The shared `.config/knowledge.json` defines Markdown collections, exclusions,
and short descriptions attached to search results. The helper renders an
ignored `.config/qmd/index.yml` with absolute paths. Change the shared JSON,
then refresh; direct QMD collection/context edits to the generated file will
be replaced. The starter supports `**/*.md` collection patterns.

## Refresh and recovery

`post-checkout`, `post-commit`, `post-merge`, and `post-rewrite` hooks request
background refreshes. The foreground command is:

```sh
bin/qmd-index
```

Git hooks do not run on every file save. Run this command after uncommitted
knowledge edits when current search results matter. It waits for the requested
refresh and returns its success or failure. Every knowledge lookup verifies
source, configuration, database presence, and successful refresh state before
returning results. Stale or unknown inputs trigger a coordinated refresh.
Refresh messages go to stderr so JSON output remains valid. Unchanged inputs
reuse the existing index and embeddings.

Automatic refresh waits up to 60 seconds. Set a positive local
`knowledge.searchRefreshTimeout` value in seconds when a project needs a
different bound. A timeout returns an error without results; the background
worker may still finish. Use `bin/doctor` and the foreground refresh to inspect
and recover. Explicit foreground refreshes can wait for larger indexing jobs.

Results are buffered until QMD succeeds and freshness is checked again. If
sources change during the lookup, discard the results and return an error.
This verifies indexed inputs and completed refresh state, not the semantic
quality of search results or the internal integrity of the SQLite database.

One worker serves each checkout. It hashes indexed Markdown and configuration,
including optional home notes, to skip unchanged inputs. Bursts of requests
share the worker. If inputs change during indexing, the worker runs another
pass. QMD itself handles incremental index and embedding updates. A failed
update does not start embedding. Git does not wait for indexing to finish.

Freshness includes the QMD release version, including prerelease and build
metadata. It excludes the optional Git commit suffix in `qmd --version`, which
can identify an unrelated surrounding repository. QMD subprocesses do not
inherit Git repository selectors from hooks. Diagnostics retain the full
reported version. After replacing a custom QMD build without changing its
release version, run `bin/qmd-index --force`.

Use `bin/qmd-index --force` to rebuild even when recorded inputs match.
Inspect `.cache/qmd/index.log` after failure. Logs rotate at approximately
1 MB on worker start, retaining one previous file. A stopped worker releases
its operating-system lock; rerun the foreground command to recover. Avoid
direct `qmd update` and `qmd embed`, which bypass this coordination.

### Search failures

When configured QMD fails, immediately tell the user what failed. Run
`bin/doctor`, inspect the refresh log, and attempt a focused repair. Verify
recovery by repeating the failed lookup successfully. Do not report success
from a command that returned an error, timed out, or discarded stale results.

If repair fails, pause knowledge-dependent work until the user explicitly
approves a fallback. Do not silently substitute `rg`, direct Markdown reads,
another index, or a different search tool to bypass the failure. Unrelated
work may continue when it does not depend on the missing knowledge.

A successful lookup with no matches is not a tool failure. Reading known
files and broadening that successful search remain allowed. A project may
deliberately operate without optional QMD, but its absence or failure does
not establish that decision; use an existing explicit project choice or ask
the user. Keep the Markdown source usable in that approved mode.

## Validation

Run `python3 -B -m unittest discover -s tests -v` and `git diff --check`.
The tests use disposable repositories and a simulated QMD process.
