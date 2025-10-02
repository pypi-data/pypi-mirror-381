from typer.testing import CliRunner
import vscode_pytest_update_snapshot as pkg
import vscode_pytest_update_snapshot.__main__ as cli
from pathlib import Path
import tomllib
import re
import importlib
from importlib.metadata import PackageNotFoundError

runner = CliRunner()

def test_version_flag_prints_and_exits(monkeypatch):
    # Patch the exported __version__ on the package object
    monkeypatch.setattr(pkg, "__version__", "9.9.9-test", raising=False)

    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "9.9.9-test"

def test_init_version_matches_pyproject():
    # Locate pyproject.toml at repo root (pytest rootdir)
    pyproject = Path.cwd() / "pyproject.toml"
    data = tomllib.loads(pyproject.read_text(encoding="utf-8"))
    expected = data["project"]["version"]

    import vscode_pytest_update_snapshot as pkg
    # If you want to be extra cautious, reload to avoid stale cache
    importlib.reload(pkg)

    assert pkg.__version__ == expected

def test_init_reads_version_from_metadata(monkeypatch):
    # Make importlib.metadata.version return a fixed semver
    monkeypatch.setattr("importlib.metadata.version", lambda name: "1.2.3", raising=True)

    import vscode_pytest_update_snapshot as pkg
    importlib.reload(pkg)  # recompute __version__

    assert pkg.__version__ == "1.2.3"

def test_init_fallback_when_not_installed(monkeypatch):
    def raise_not_found(_):
        raise PackageNotFoundError
    monkeypatch.setattr("importlib.metadata.version", raise_not_found, raising=True)

    import vscode_pytest_update_snapshot as pkg
    importlib.reload(pkg)

    assert pkg.__version__ == "0+unknown"

SEMVERish = re.compile(r"^\d+\.\d+\.\d+([-.+][0-9A-Za-z.]+)?$")

def test_version_has_valid_shape():
    import vscode_pytest_update_snapshot as pkg
    importlib.reload(pkg)
    assert SEMVERish.match(pkg.__version__) or pkg.__version__ == "0+unknown"
