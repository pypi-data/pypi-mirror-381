"""Secret storage helpers with keyring fallback."""

from __future__ import annotations

import contextlib
from typing import Optional

import keyring  # type: ignore[import]

_SERVICE_NAME = "grounding_cli"


def _key_name(name: str) -> str:
    return f"token::{name}"


def has_keyring() -> bool:
    try:
        keyring.get_keyring()
        return True
    except Exception:
        return False


def store_secret(name: str, secret: str) -> None:
    if not secret:
        return
    if has_keyring():
        keyring.set_password(_SERVICE_NAME, _key_name(name), secret)


def load_secret(name: str, fallback: Optional[str] = None) -> Optional[str]:
    if has_keyring():
        try:
            stored = keyring.get_password(_SERVICE_NAME, _key_name(name))
            if stored:
                return stored
        except Exception:
            pass
    return fallback


def delete_secret(name: str) -> None:
    if has_keyring():
        with contextlib.suppress(Exception):
            keyring.delete_password(_SERVICE_NAME, _key_name(name))


__all__ = ["store_secret", "load_secret", "delete_secret", "has_keyring"]
