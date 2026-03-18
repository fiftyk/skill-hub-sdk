import re
import skill_hub_sdk


def test_import():
    assert skill_hub_sdk is not None


def test_version_format():
    version = skill_hub_sdk.__version__
    assert re.match(r"^\d+\.\d+\.\d+", version), f"Invalid version: {version}"
