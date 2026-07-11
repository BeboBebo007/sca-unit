import json
from pathlib import Path


def test_demo_examples_are_valid_json_and_show_structural_change():
    baseline = json.loads(Path("demo_examples/baseline_user.json").read_text(encoding="utf-8-sig"))
    changed = json.loads(Path("demo_examples/changed_user.json").read_text(encoding="utf-8-sig"))

    assert "user" in baseline
    assert "user" in changed
    assert "roles" not in baseline["user"]
    assert changed["user"]["roles"] == ["admin"]
