import os
import json
import pytest

from framework.runner import ScraperFrameworkRunner
from framework.validators import FrameworkValidator


def minimal_setup(tmp_path):
    os.chdir(tmp_path)
    os.makedirs('.scraper-spec/templates', exist_ok=True)
    os.makedirs('.scraper-spec/memory', exist_ok=True)
    with open('.scraper-spec/templates/baseline-template.json', 'w') as f:
        json.dump({"metadata": {"created_date": "", "site_target": "", "test_query": ""}, "results": []}, f)
    with open('.scraper-spec/templates/log-template.json', 'w') as f:
        json.dump({"timestamp": "", "site": "", "query": ""}, f)
    with open('.scraper-spec/templates/diff-template.json', 'w') as f:
        json.dump({"mismatches": []}, f)
    with open('.scraper-spec/templates/selectors-template.yaml', 'w') as f:
        f.write("site_config:\n  base_url: ''\n  selectors: {}\n  filters: {}\n  params: {}\n")
    with open('.scraper-spec/templates/debug-log-template.json', 'w') as f:
        json.dump({"timestamp": "", "site": "", "query": "", "errors": []}, f)
    with open('.scraper-spec/memory/constitution.md', 'w') as f:
        f.write("# Constitution\n")
    for d in ('specs', 'baselines/screenshots', 'logs/regressions', 'logs/debug', 'docs', 'framework'):
        os.makedirs(d, exist_ok=True)
    with open('framework/plan.md', 'w') as f:
        f.write("Acquire → Identify → Collect → Extract")


def test_runtime_log_schema_validation_fails_on_missing_keys(tmp_path):
    minimal_setup(tmp_path)
    v = FrameworkValidator()
    bad = {"timestamp": "2025-01-01T00:00:00Z"}
    assert v.validate_log_json(bad) is False


def test_debug_log_schema_validation_fails_on_missing_keys(tmp_path):
    minimal_setup(tmp_path)
    v = FrameworkValidator()
    bad = {"site": "x"}
    assert v.validate_debug_log_json(bad) is False


def test_baseline_artifact_completeness_missing_snapshot(tmp_path, monkeypatch):
    minimal_setup(tmp_path)
    r = ScraperFrameworkRunner()

    # Simulate missing snapshot after baseline writes
    original_exists = os.path.exists

    def fake_exists(path):
        if path.endswith('.snapshot.html'):
            return False
        return original_exists(path)

    monkeypatch.setattr(os.path, 'exists', fake_exists)

    assert r.baseline('sitea', 'q') is False


