# skill-hub-sdk

Skill Hub Python SDK.

## Installation

```bash
pip install skill-hub-sdk
```

## Development

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Lint
uv run ruff check src/
uv run ruff format src/
```

## Release

1. Update `version` in `pyproject.toml`
2. Commit and push
3. Create and push a tag: `git tag v0.x.x && git push origin v0.x.x`
4. GitLab CI will automatically build and publish to the Package Registry
