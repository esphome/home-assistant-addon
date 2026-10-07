import importlib.util
import shutil
from pathlib import Path
from types import ModuleType

import pytest

ROOT = Path(__file__).parent.parent


def _load() -> ModuleType:
    spec = importlib.util.spec_from_file_location(
        "bump_version", ROOT / "script" / "bump-version.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


bump_version = _load()


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> list[list[str]]:
    (tmp_path / "template").mkdir()
    shutil.copy(ROOT / "template" / "addon_config.yaml", tmp_path / "template")
    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("GITHUB_OUTPUT", raising=False)
    calls: list[list[str]] = []
    monkeypatch.setattr(bump_version.generate, "main", calls.append)
    return calls


def _run(monkeypatch: pytest.MonkeyPatch, version: str) -> int:
    monkeypatch.setattr("sys.argv", ["bump-version.py", version])
    return bump_version.main()


def _versions() -> dict[str, str]:
    return {
        target: str(bump_version._read_version(target))
        for target in ("stable", "beta", "dev")
    }


@pytest.mark.parametrize(
    ("older", "newer"),
    [
        ("2026.9.2", "2026.10.0b1"),
        ("2026.10.0b1", "2026.10.0"),
        ("2026.10.0b1", "2026.10.0b2"),
        ("2026.10.0", "2026.10.1"),
        ("2025.12.3", "2026.1.0b1"),
    ],
)
def test_release_key_ordering(older: str, newer: str) -> None:
    assert (
        bump_version.Version.parse(older).release_key
        < bump_version.Version.parse(newer).release_key
    )


def test_stable_does_not_override_newer_beta(
    repo: list[list[str]], monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    output = tmp_path / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    _run(monkeypatch, "2026.10.0b1")
    _run(monkeypatch, "2026.9.2")

    versions = _versions()
    assert versions["beta"] == "2026.10.0b1"
    assert versions["stable"] == "2026.9.2"
    assert repo[-1] == ["stable"]
    assert output.read_text().splitlines() == [
        "beta_updated=true",
        "beta_updated=false",
    ]


@pytest.mark.parametrize("beta", ["2026.9.2b1", "2026.9.2"])
def test_stable_overrides_older_or_equal_beta(
    repo: list[list[str]], monkeypatch: pytest.MonkeyPatch, beta: str, tmp_path: Path
) -> None:
    _run(monkeypatch, beta)
    output = tmp_path / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    _run(monkeypatch, "2026.9.2")

    versions = _versions()
    assert versions["beta"] == "2026.9.2"
    assert versions["stable"] == "2026.9.2"
    assert repo[-1] == ["stable", "beta"]
    assert output.read_text() == "beta_updated=true\n"


def test_dev_does_not_update_beta(
    repo: list[list[str]], monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    output = tmp_path / "github_output"
    monkeypatch.setenv("GITHUB_OUTPUT", str(output))
    before = _versions()
    _run(monkeypatch, "2026.11.0-dev20261010")

    versions = _versions()
    assert versions["dev"] == "2026.11.0-dev20261010"
    assert versions["beta"] == before["beta"]
    assert repo[-1] == ["dev"]
    assert output.read_text() == "beta_updated=false\n"
