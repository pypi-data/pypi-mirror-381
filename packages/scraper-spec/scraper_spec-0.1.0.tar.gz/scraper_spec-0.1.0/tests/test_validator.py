from framework.validators import FrameworkValidator
import json
import yaml


def test_validate_selectors_yaml():
    v = FrameworkValidator()
    data = {
        "site_config": {
            "base_url": "http://example.com",
            "selectors": {
                "search_input": "#q",
                "search_button": "#go",
                "results_container": "#results",
                "result_items": ".item",
                "pagination": ".next"
            },
            "filters": {
                "exclude_patterns": [],
                "include_patterns": []
            },
            "params": {
                "delay_ms": 1000,
                "max_retries": 3
            }
        }
    }
    assert v.validate_selectors_yaml(data)


def test_validate_baseline_log_diff_json():
    v = FrameworkValidator()
    baseline = {
        "metadata": {
            "baseline_version": "0.1.0",
            "created_date": "2024-01-01T00:00:00Z",
            "site_target": "example",
            "test_query": "query"
        },
        "results": []
    }
    assert v.validate_baseline_json(baseline)

    log = {
        "timestamp": "2024-01-01T00:00:00Z",
        "site": "example",
        "query": "query",
        "steps": [],
        "errors": []
    }
    assert v.validate_log_json(log)

    diff = {
        "baseline_file": "a.json",
        "current_file": "b.json",
        "mismatches": []
    }
    assert v.validate_diff_json(diff)

