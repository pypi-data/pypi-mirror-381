from framework.utils import check_constitution_compliance, generate_diff


def test_constitution_paths():
    assert check_constitution_compliance("specs/a.yaml")
    assert check_constitution_compliance("baselines/a.json")
    assert check_constitution_compliance("logs/a.json")
    assert check_constitution_compliance("framework/a.py")
    assert check_constitution_compliance("docs/a.md")
    assert not check_constitution_compliance("tmp/a.txt")


def test_generate_diff():
    expected = {"a": 1, "b": [1, 2], "c": {"x": "y"}}
    actual = {"a": 1, "b": [1, 2], "c": {"x": "y"}}
    diff = generate_diff(expected, actual, "base", "current")
    assert "mismatches" in diff
    assert diff["mismatches"] == []

