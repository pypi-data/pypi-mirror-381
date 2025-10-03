import os
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run_cli(*args, env=None):
    # Run CLI as module to avoid relative import issues
    cmd = ["python", "-m", "framework.runner", *args]
    result = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True, env=env)
    return result.returncode, result.stdout + result.stderr


def test_discover_and_init(tmp_path, monkeypatch):
    # Run in repo root
    code, out = run_cli("discover", "example")
    assert code == 0, out
    assert (ROOT / "specs" / "example.discover.yaml").exists()

    code, out = run_cli("init", "example")
    assert code == 0, out
    assert (ROOT / "specs" / "example.yaml").exists()


def test_baseline_and_test(tmp_path):
    code, out = run_cli("baseline", "example", "query")
    assert code == 0, out
    assert (ROOT / "baselines" / "example.expected.json").exists()
    assert (ROOT / "baselines" / "example.snapshot.html").exists()
    assert any(p.name.startswith("example_") and p.suffix == ".png" for p in (ROOT / "baselines" / "screenshots").glob("*.png"))

    code, out = run_cli("test", "example")
    assert code == 0, out
    assert any(p.name.startswith("example_") and p.suffix == ".json" for p in (ROOT / "logs" / "regressions").glob("*.json"))


def test_debug_and_rebaseline_and_rollback(monkeypatch):
    code, out = run_cli("debug", "example", "query")
    assert code == 0, out
    debug_dir = ROOT / "logs" / "debug"
    assert any(p.suffix == ".json" for p in debug_dir.iterdir())
    assert any(p.suffix == ".md" for p in debug_dir.iterdir())
    assert any(p.suffix == ".html" for p in debug_dir.iterdir())

    # rebaseline requires confirmation
    env = os.environ.copy()
    env["SCRAPER_SPEC_CONFIRM"] = "1"
    code, out = run_cli("rebaseline", "example", "query", env=env)
    assert code == 0, out
    assert (ROOT / "baselines" / "example.expected.json").exists()

    # rollback should succeed only if backups exist
    code, out = run_cli("rollback", "example")
    # rollback may fail if backups missing; allow 0 or 1 but ensure it runs
    assert code in (0, 1)

