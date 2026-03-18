# skill-hub-sdk

Skill Hub Python SDK。

## 安装

```bash
pip install skill-hub-sdk
```

## 开发

```bash
# 安装依赖
uv sync

# 运行测试
uv run pytest

# 代码检查
uv run ruff check src/
uv run ruff format src/
```

## 发版

1. 修改 `pyproject.toml` 中的 `version`
2. 提交并推送
3. 打 tag 并推送：`git tag v0.x.x && git push origin v0.x.x`
4. GitHub Actions 自动构建并发布到 PyPI

## 发布说明

### PyPI（GitHub Actions 自动发布）

推送 `v*` tag 后，CI 流水线会自动构建并通过 Trusted Publishing（OIDC，无需 token）发布。

```bash
git tag v0.1.0
git push origin v0.1.0
```

### PyPI（手动发布）

```bash
uv build
uv publish --token pypi-<your-token>
```

在 https://pypi.org/manage/account/token/ 获取 API token。

### 公司 Nexus（手动发布）

```bash
uv build
uv publish \
  --publish-url http://<nexus-host>/repository/pypi-internal/ \
  --username <nexus-用户名> \
  --password <nexus-密码>
```

也可以用环境变量避免凭据出现在 shell 历史中：

```bash
export UV_PUBLISH_USERNAME=<nexus-用户名>
export UV_PUBLISH_PASSWORD=<nexus-密码>
uv publish --publish-url http://<nexus-host>/repository/pypi-internal/
```
