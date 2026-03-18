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
4. GitHub Actions will automatically build and publish to PyPI

## Publishing

### PyPI (automated via GitHub Actions)

Push a `v*` tag — the CI pipeline will build and publish automatically using Trusted Publishing (OIDC, no token required).

```bash
git tag v0.1.0
git push origin v0.1.0
```

### PyPI (manual)

```bash
uv build
uv publish --token pypi-<your-token>
```

Get your API token at https://pypi.org/manage/account/token/

### Company Nexus (manual)

```bash
uv build
uv publish \
  --publish-url http://<nexus-host>/repository/pypi-internal/ \
  --username <nexus-username> \
  --password <nexus-password>
```

Or use environment variables to avoid credentials in shell history:

```bash
export UV_PUBLISH_USERNAME=<nexus-username>
export UV_PUBLISH_PASSWORD=<nexus-password>
uv publish --publish-url http://<nexus-host>/repository/pypi-internal/
```
