"""Test the copied foundation in disposable repositories; no network or models."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
import unittest

SOURCE = Path(__file__).resolve().parents[1]


class KnowledgeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="project starter tests ")
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.repo = self.base / "main checkout"
        self.repo.mkdir()
        for name in ("bin", "docs", "memory", "tests"):
            shutil.copytree(SOURCE / name, self.repo / name, ignore=shutil.ignore_patterns("__pycache__"))
        # Adopted docs can link to the optional GitHub workflow.
        if (SOURCE / ".github").is_dir():
            shutil.copytree(SOURCE / ".github", self.repo / ".github")
        (self.repo / ".config").mkdir()
        shutil.copy2(SOURCE / ".config/knowledge.json", self.repo / ".config/knowledge.json")
        for name in ("README.md", "AGENTS.md", ".gitignore", ".project-starter.json"):
            shutil.copy2(SOURCE / name, self.repo / name)
        if (SOURCE / ".envrc").exists():
            shutil.copy2(SOURCE / ".envrc", self.repo / ".envrc")
        self.tools = self.base / "fake tools"
        self.tools.mkdir()
        for name, target in (("python3", sys.executable), ("git", shutil.which("git"))):
            (self.tools / name).symlink_to(target)
        self.events = self.base / "events.jsonl"
        self.env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
        self.env.update(HOME=str(self.base / "home"), PATH=str(self.tools), GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
                        PYTHONDONTWRITEBYTECODE="1", EVENTS=str(self.events), APPROVALS=str(self.base / "approvals.jsonl"),
                        OLD_HOOKS=str(self.base / "old-hooks.jsonl"), QMD_CONFIG_DIR="/wrong-config",
                        XDG_CACHE_HOME="/wrong-cache", INDEX_PATH="/wrong-index")
        self.tool("qmd", '''
import json, os, subprocess, sys, time
from pathlib import Path
if sys.argv[1:] == ["--version"]:
    if os.environ.get("BROKEN_QMD"):
        sys.exit(9)
    version = os.environ.get("QMD_TEST_VERSION", "2.1.0")
    revision = os.environ.get("QMD_TEST_REVISION", "test")
    if os.environ.get("QMD_TEST_GIT_VERSION"):
        revision = subprocess.check_output(
            ["git", "-C", str(Path(__file__).parent), "rev-parse", "--short", "HEAD"], text=True).strip()
    print(f"qmd {version} ({revision})")
    sys.exit(0)
record = {"command": sys.argv[1], "cwd": os.getcwd(),
          "config": os.environ["QMD_CONFIG_DIR"], "cache": os.environ["XDG_CACHE_HOME"],
          "index": os.environ["INDEX_PATH"], "arguments": sys.argv[2:]}
record["collections"] = json.loads((Path(record["config"]) / "index.yml").read_text())["collections"]
with open(os.environ["EVENTS"], "a") as stream:
    stream.write(json.dumps(record) + "\\n")
if sys.argv[1] in ("update", "embed"):
    time.sleep(float(os.environ.get("QMD_TEST_DELAY", "0.02")))
    if sys.argv[1] == "update" and os.environ.get("FAIL_UPDATE"):
        sys.exit(23)
    if sys.argv[1] == "embed" and os.environ.get("FAIL_EMBED"):
        sys.exit(24)
    if not os.environ.get("NO_INDEX"):
        Path(record["index"]).touch()
else:
    if os.environ.get("FAIL_QUERY"):
        print("partial results must not escape")
        sys.exit(25)
    if os.environ.get("EDIT_DURING_QUERY"):
        with (Path.cwd() / "docs/README.md").open("a") as stream:
            stream.write("Changed during lookup.\\n")
    print(json.dumps(record))
''')
        self.tool("direnv", '''
import json, os, sys
from pathlib import Path
if sys.argv[1:] == ["status", "--json"]:
    print(json.dumps({"state": {"foundRC": {"allowed": int(os.environ.get("DIRENV_ALLOWED", "0")), "path": str(Path.cwd() / ".envrc")}}}))
elif sys.argv[1:] == ["version"]:
    print("2.37.1")
else:
    with open(os.environ["APPROVALS"], "a") as stream:
        stream.write(json.dumps(sys.argv[1:]) + "\\n")
''')
        self.run_command("git", "init", "-b", "main")
        self.run_command("git", "config", "user.name", "Starter test")
        self.run_command("git", "config", "user.email", "test@example.invalid")

    def tool(self, name, body):
        path = self.tools / name
        path.write_text("#!" + sys.executable + "\n" + body)
        path.chmod(0o755)

    def run_command(self, *args, root=None, extra=None, check=True, input=None):
        result = subprocess.run(args, cwd=root or self.repo, env=self.env | (extra or {}),
                                text=True, capture_output=True, input=input, timeout=30)
        if check:
            self.assertEqual(result.returncode, 0, (args, result.stdout, result.stderr))
        return result

    def records(self):
        return [json.loads(line) for line in self.events.read_text().splitlines()] if self.events.exists() else []

    def drain(self, root=None):
        self.run_command("bin/qmd-index", root=root)

    def commit(self):
        self.run_command("git", "add", ".")
        self.run_command("git", "commit", "-m", "Fixture")
        self.drain()

    def wait_for_command(self, count):
        deadline = time.monotonic() + 10
        while len(self.records()) < count:
            self.assertLess(time.monotonic(), deadline)
            time.sleep(0.02)

    def tree_state(self):
        result = {}
        for base in (self.repo / ".cache", self.repo / ".config", self.repo / "bin"):
            if base.exists():
                for path in base.rglob("*"):
                    if path.is_file():
                        stat = path.stat()
                        result[str(path)] = (stat.st_mtime_ns, stat.st_size, path.read_bytes())
        return result

    def test_lookup_waits_for_worker_lock_release_after_completed_refresh(self):
        self.run_command("bin/setup")
        document = self.repo / "docs/README.md"
        document.write_text(document.read_text() + "\nChanged reference.\n")
        gate = self.base / "release gate"
        gate.touch()
        ready = self.base / "worker releasing"
        shim = self.base / "os boundary"
        shim.mkdir()
        # Hold the OS unlock boundary after the worker records completion.
        (shim / "sitecustomize.py").write_text('''
import fcntl, os, sys, time
from pathlib import Path
original = fcntl.flock
def flock(file, operation):
    if "--worker" in sys.argv and operation == fcntl.LOCK_UN:
        Path(os.environ["RELEASE_READY"]).touch()
        while Path(os.environ["RELEASE_GATE"]).exists():
            time.sleep(0.01)
    return original(file, operation)
fcntl.flock = flock
''')
        env = self.env | {"PYTHONPATH": str(shim), "RELEASE_READY": str(ready), "RELEASE_GATE": str(gate)}
        process = subprocess.Popen(["bin/knowledge", "search", "reference"], cwd=self.repo, env=env,
                                   text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        try:
            deadline = time.monotonic() + 10
            while not ready.exists():
                self.assertLess(time.monotonic(), deadline, "Worker never reached the unlock boundary")
                time.sleep(0.01)
            with self.assertRaises(subprocess.TimeoutExpired):
                process.communicate(timeout=0.5)
        finally:
            gate.unlink(missing_ok=True)
            stdout, stderr = process.communicate(timeout=10)
        self.assertEqual(process.returncode, 0, (stdout, stderr))
        self.assertEqual(json.loads(stdout)["command"], "search")

    def test_unrelated_repositories_share_home_models_and_keep_local_indexes(self):
        self.run_command("bin/setup")
        models = self.base / "home/.cache/qmd/models"
        self.assertTrue(models.is_dir())
        (models / "existing.gguf").write_text("downloaded once")
        other = self.base / "unrelated project"
        shutil.copytree(self.repo, other, ignore=shutil.ignore_patterns(".git", ".cache", "qmd"))
        self.run_command("git", "init", "-b", "main", root=other)
        self.run_command("bin/setup", root=other)
        self.assertEqual((other / ".cache/qmd/models").resolve(), models)
        self.assertEqual((other / ".cache/qmd/models/existing.gguf").read_text(), "downloaded once")
        self.assertFalse(os.path.samefile(self.repo / ".cache/qmd/index.sqlite", other / ".cache/qmd/index.sqlite"))

    def test_model_migration_deduplicates_but_rejects_conflicts(self):
        models = self.base / "home/.cache/qmd/models"
        local = self.repo / ".cache/qmd/models"
        models.mkdir(parents=True)
        local.mkdir(parents=True)
        (models / "existing.gguf").write_text("shared")
        (local / "existing.gguf").write_text("different")
        result = self.run_command("bin/setup", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("conflict", result.stderr.lower())
        self.assertFalse(local.is_symlink())
        self.assertEqual((local / "existing.gguf").read_text(), "different")
        (local / "existing.gguf").write_text("shared")
        (local / "another.gguf").write_text("another model")
        self.run_command("bin/setup")
        self.assertTrue(local.is_symlink())
        self.assertEqual(local.resolve(), models)
        self.assertEqual((models / "another.gguf").read_text(), "another model")

    def test_model_link_migration_preserves_external_source_and_repairs_broken_links(self):
        source = self.base / "old model cache"
        source.mkdir()
        (source / "existing.gguf").write_text("preserve external source")
        local = self.repo / ".cache/qmd/models"
        local.parent.mkdir(parents=True)
        local.symlink_to(source)
        self.run_command("bin/setup")
        self.assertEqual(local.resolve(), self.base / "home/.cache/qmd/models")
        self.assertEqual((source / "existing.gguf").read_bytes(), (local / "existing.gguf").read_bytes())
        local.unlink()
        local.symlink_to(self.base / "missing")
        self.run_command("bin/setup")
        self.assertEqual(local.resolve(), self.base / "home/.cache/qmd/models")

    def test_lookups_refresh_uncommitted_changes_without_polluting_stdout(self):
        self.run_command("bin/setup")
        for command in ("search", "query", "vsearch", "get", "multi-get", "ls"):
            with self.subTest(command=command):
                note = self.repo / "docs/README.md"
                note.write_text(note.read_text() + "\nNew " + command + " guidance.\n")
                initial = len(self.records())
                result = self.run_command("bin/knowledge", command, "reference")
                self.assertEqual(json.loads(result.stdout)["command"], command)
                self.assertEqual([r["command"] for r in self.records()[initial:]], ["update", "embed", command])
                initial = len(self.records())
                self.run_command("bin/knowledge", command, "reference")
                self.assertEqual([r["command"] for r in self.records()[initial:]], [command])

    def test_lookup_refuses_failed_refresh_and_recovers_on_next_attempt(self):
        self.run_command("bin/setup")
        for failure in ("FAIL_UPDATE", "FAIL_EMBED"):
            with self.subTest(failure=failure):
                note = self.repo / "docs/README.md"
                note.write_text(note.read_text() + "\nChanged.\n")
                initial = len(self.records())
                result = self.run_command("bin/knowledge", "search", "reference", extra={failure: "1"}, check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertNotIn("search", [r["command"] for r in self.records()[initial:]])
                self.assertIn("Report", result.stderr)
                self.assertIn("pause", result.stderr)
                self.assertEqual(json.loads(self.run_command("bin/knowledge", "search", "reference").stdout)["command"], "search")

    def test_lookup_repairs_missing_database_and_changed_configuration(self):
        self.run_command("bin/setup")
        for missing in (".cache/qmd/index.sqlite", ".config/qmd/index.yml"):
            with self.subTest(missing=missing):
                (self.repo / missing).unlink()
                self.run_command("bin/knowledge", "search", "reference")
                self.assertTrue((self.repo / missing).is_file())
        source = self.repo / ".config/knowledge.json"
        config = json.loads(source.read_text())
        config["collections"]["docs"]["context"]["/"] = "Updated collection"
        source.write_text(json.dumps(config))
        record = json.loads(self.run_command("bin/knowledge", "search", "reference").stdout)
        self.assertEqual(record["collections"]["docs"]["context"]["/"], "Updated collection")

    def test_lookup_requires_database_after_successful_refresh(self):
        self.run_command("bin/setup")
        (self.repo / ".cache/qmd/index.sqlite").unlink()
        initial = len(self.records())
        result = self.run_command("bin/knowledge", "search", "reference", extra={"NO_INDEX": "1"}, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertNotIn("search", [r["command"] for r in self.records()[initial:]])

    def test_lookup_refresh_timeout_returns_no_results(self):
        self.run_command("bin/setup")
        self.run_command("git", "config", "knowledge.searchRefreshTimeout", "0.1")
        (self.repo / ".cache/qmd/index.sqlite").unlink()
        initial = len(self.records())
        result = self.run_command("bin/knowledge", "search", "reference", extra={"QMD_TEST_DELAY": "0.4"}, check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("timed out", result.stderr)
        self.assertNotIn("search", [r["command"] for r in self.records()[initial:]])
        self.drain()
        self.run_command("bin/knowledge", "search", "reference")

    def test_lookup_discards_results_when_sources_change_or_qmd_fails(self):
        self.run_command("bin/setup")
        for failure in ("EDIT_DURING_QUERY", "FAIL_QUERY", "BROKEN_QMD"):
            with self.subTest(failure=failure):
                result = self.run_command("bin/knowledge", "search", "reference", extra={failure: "1"}, check=False)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("Report", result.stderr)
                self.run_command("bin/knowledge", "search", "reference")

    def test_lookup_missing_tool_reports_failure_without_fallback(self):
        self.run_command("bin/setup")
        (self.tools / "qmd").unlink()
        result = self.run_command("bin/knowledge", "search", "reference", check=False)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn("Report", result.stderr)
        self.assertIn("pause", result.stderr)


if __name__ == "__main__":
    unittest.main()
