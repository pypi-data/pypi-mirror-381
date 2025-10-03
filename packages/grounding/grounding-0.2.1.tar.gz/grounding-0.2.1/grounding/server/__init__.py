"""Helpers for accessing the bundled Node.js MCP server."""

from __future__ import annotations

import shutil
from importlib import resources
from pathlib import Path

from platformdirs import user_cache_dir

_CACHE_BASE = Path(user_cache_dir("grounding", "FeatureGrounding")) / "server"


def _copy_resource_tree(src, dst: Path) -> None:  # type: ignore[no-untyped-def]
    if src.is_file():
        with resources.as_file(src) as source_path:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source_path, dst)
    else:
        dst.mkdir(parents=True, exist_ok=True)
        for child in src.iterdir():
            _copy_resource_tree(child, dst / child.name)


def _sync_package_assets(target: Path) -> None:
    package_root = resources.files("grounding.server").joinpath("node")
    if target.exists():
        shutil.rmtree(target)
    _copy_resource_tree(package_root, target)


def get_server_root() -> Path:
    """Return a filesystem directory containing the Node.js server sources."""

    target = _CACHE_BASE / "node"
    marker = target / ".synced"
    changed = True
    if marker.exists():
        current = marker.read_text().strip()
        from .. import __version__  # Lazy import to avoid circular dependency

        if current == __version__:
            changed = False
    if changed:
        _sync_package_assets(target)
        marker.parent.mkdir(parents=True, exist_ok=True)
        from .. import __version__

        marker.write_text(__version__, encoding="utf-8")
    return target


__all__ = ["get_server_root"]
