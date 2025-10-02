# vscode-pytest-update-snapshot

Run `pytest` on the test under your cursor and update inline snapshots (VSCode-friendly).

## Install / Run (no install with uvx)

```bash
uvx vscode-pytest-update-snapshot tests/test_example.py 12
# ensure it uses your project venv interpreter:
uvx --python ".venv/Scripts/python.exe" vscode-pytest-update-snapshot tests/test_example.py 12
```

Pass extra pytest args after --:

```bash
uvx vscode-pytest-update-snapshot tests/test_example.py 12 -- -q -k "mycase"
```

## Requirements

- Python 3.10+ (tested on 3.12)
- **uv** installed on your PATH (`pipx install uv` or `pip install uvtools`—use your preferred method)
- A project virtual environment selected in VSCode *(bottom-right status bar → Select Interpreter)*
- These packages installed **in your project venv**:
  - `pytest`
  - `inline-snapshot` (with Ruff formatting, see config below)
  - `ruff`

Install with uv:

```
uv add pytest ruff inline-snapshot --dev
```

## Inline-snapshot formatting via Ruff

Add this to your `pyproject.toml`:

```
[tool.inline-snapshot]
# Format with Ruff; read/write via stdin/stdout so inline-snapshot can capture it
format-command = "ruff format --stdin-filename {filename}"

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.format]
quote-style = "double"
indent-style = "space"
docstring-code-format = true

[tool.pytest.ini_options]
addopts = "-q"
testpaths = ["tests"]
```

## VSCode setup

This repo includes templates for a handy “Update snapshot (test at cursor)” action.

### Keybinding

1. Open **Command Palette** → **Preferences: Open Keyboard Shortcuts (JSON)**.
2. Copy the contents of `template_keybindings.json` into the file and save.

> VSCode’s keybindings file supports comments (JSONC). You can keep the comments.

### Task

1. For a **workspace task**: open `.vscode/tasks.json` (create if missing) and copy from `template_tasks.json`.
2. For a **profile-level (user) task**: **Command Palette** → **Tasks: Open User Tasks**, then paste the task there.

> Either way, VSCode tasks also support comments (JSONC).

### Run it

- Put the cursor on a test line in a Python file.
- Press the configured shortcut (default `Ctrl+Alt+U`) or run **Terminal → Run Task → Update snapshot (test at cursor)**.
- Make sure your interpreter/venv is selected in the VSCode status bar so `pytest` and `inline-snapshot` are found.

## Install this CLI (editable during development)

```
uv pip install -e .
```

(or publish and use `uvx`, but for local dev the editable install is simplest.)
