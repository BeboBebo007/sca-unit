from pathlib import Path


def test_local_demo_launcher_exists_and_starts_service():
    content = Path("run_demo.ps1").read_text(encoding="utf-8-sig")
    assert "http://127.0.0.1:8765" in content
    assert "Start-Process $url" in content
    assert "-m private_server.start_local" in content
