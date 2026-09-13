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
        self.env.update(PATH=str(self.tools), GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull,
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
