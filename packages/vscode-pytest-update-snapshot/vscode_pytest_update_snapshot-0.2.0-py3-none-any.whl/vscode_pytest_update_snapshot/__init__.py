# src/vscode_pytest_update_snapshot/__init__.py
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("vscode-pytest-update-snapshot")
except PackageNotFoundError:
    # package not installed (e.g., running from a source checkout without editable install)
    __version__ = "0+unknown"
