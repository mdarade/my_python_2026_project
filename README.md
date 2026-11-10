# my-python-2026-project

Python 3.13 project managed with [uv](https://docs.astral.sh/uv/), developed in a VS Code dev container.

## Getting started

Open the folder in VS Code and run **Dev Containers: Reopen in Container**. The container
installs Python, syncs dependencies, and sets up the git pre-commit hooks.

```bash
uv run hello        # run the app
make check          # lint, format check, type check, tests (same as CI)
```

## Layout

```
src/my_python_2026_project/   application code
tests/                        pytest tests
.devcontainer/                dev container definition
.github/workflows/ci.yml      CI: runs `make check` equivalents on every push / PR
```

## Common tasks

| Command | What it does |
| --- | --- |
| `make test` | Run pytest with coverage (fails under 80%) |
| `make lint` | Ruff lint |
| `make format` | Ruff auto-format |
| `make type-check` | mypy (strict) |
| `make check` | Everything CI runs |
| `uv add <pkg>` | Add a runtime dependency |
| `uv add --dev <pkg>` | Add a dev dependency |
