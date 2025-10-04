from importlib.metadata import metadata, version as metadata_version
from packaging.version import parse, Version
from urllib.parse import urlparse
from urllib.parse import ParseResult


def _config() -> dict:
    config = metadata("avalan")
    package_version = metadata_version("avalan")
    return {
        "name": config["Name"],
        "version": package_version,
        "license": config["License"],
        "url": "https://avalan.ai",
    }


config = _config()


def license() -> str:
    assert "license" in config
    return config["license"]


def name() -> str:
    assert "name" in config
    return config["name"]


def version() -> Version:
    assert "version" in config
    return parse(config["version"])


def site() -> ParseResult:
    assert "url" in config
    return urlparse(config["url"])
