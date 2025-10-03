"""Configuration and state persistence for the Grounding CLI."""

from __future__ import annotations

import json
import os
import stat
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

from platformdirs import user_config_dir, user_cache_dir

from .keyring_secrets import store_secret, load_secret, delete_secret, has_keyring

_DEFAULT_ENV_LOADED = False


def _load_default_env() -> None:
    global _DEFAULT_ENV_LOADED
    if _DEFAULT_ENV_LOADED:
        return

    candidate_env = os.environ.get('GROUNDING_ENV_FILE')
    search_paths = []
    if candidate_env:
        search_paths.append(Path(candidate_env))
    package_env = Path(__file__).resolve().parent / '.env'
    search_paths.append(package_env)
    repo_env = Path(__file__).resolve().parent.parent / '.env'
    search_paths.append(repo_env)

    for env_path in search_paths:
        if not env_path or not env_path.exists():
            continue
        try:
            for line in env_path.read_text(encoding='utf-8').splitlines():
                line = line.strip()
                if not line or line.startswith('#') or '=' not in line:
                    continue
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()
                if not key:
                    continue
                aliases = {
                    'SUPABASE_URL': 'GROUNDING_SUPABASE_URL',
                    'SUPABASE_ANON_KEY': 'GROUNDING_SUPABASE_ANON_KEY',
                }
                target_key = aliases.get(key, key)
                if target_key.startswith('GROUNDING_') and target_key not in os.environ:
                    os.environ[target_key] = value
        except OSError:
            continue

    _DEFAULT_ENV_LOADED = True


_load_default_env()

_APP_NAME = "grounding"
_APP_AUTHOR = "FeatureGrounding"

_CONFIG_DIR = Path(user_config_dir(_APP_NAME, _APP_AUTHOR))
_CACHE_DIR = Path(user_cache_dir(_APP_NAME, _APP_AUTHOR))
_STATE_FILE = _CONFIG_DIR / "state.json"


def ensure_directories() -> None:
    """Ensure that config and cache directories exist with safe permissions."""

    for directory in (_CONFIG_DIR, _CACHE_DIR):
        directory.mkdir(parents=True, exist_ok=True)
        _ensure_private_permissions(directory)


def _ensure_private_permissions(path: Path) -> None:
    if os.name == "posix":
        try:
            path.chmod(stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR)
        except PermissionError:
            # Non-fatal – best effort on mounts.
            pass


@dataclass
class Session:
    """Represents an authenticated Supabase session."""

    access_token: str
    refresh_token: str
    expires_at: Optional[int]
    token_type: str = "bearer"
    user: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_payload(cls, payload: Dict[str, Any]) -> "Session":
        expires_raw = payload.get("expires_at")
        try:
            expires_at = int(expires_raw) if expires_raw is not None else None
        except (TypeError, ValueError):
            expires_at = None
        return cls(
            access_token=payload.get("access_token", ""),
            refresh_token=payload.get("refresh_token", ""),
            expires_at=expires_at,
            token_type=payload.get("token_type", "bearer"),
            user=payload.get("user", {}),
        )

    def as_dict(self) -> Dict[str, Any]:
        return {
            "access_token": self.access_token,
            "refresh_token": self.refresh_token,
            "expires_at": self.expires_at,
            "token_type": self.token_type,
            "user": self.user,
        }


def load_state() -> Dict[str, Any]:
    ensure_directories()
    if not _STATE_FILE.exists():
        return {}
    try:
        with _STATE_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return {}


def save_state(state: Dict[str, Any]) -> None:
    ensure_directories()
    tmp_file = _STATE_FILE.with_suffix(".tmp")
    with tmp_file.open("w", encoding="utf-8") as file:
        json.dump(state, file, indent=2, sort_keys=True)
        file.flush()
        os.fsync(file.fileno())
    tmp_file.replace(_STATE_FILE)
    _ensure_private_permissions(_STATE_FILE)


def get_session() -> Optional[Session]:
    state = load_state()
    if "session" not in state:
        return None
    session_payload = state.get("session")
    if not isinstance(session_payload, dict):
        return None
    if not session_payload.get("access_token"):
        return None
    return Session.from_payload(session_payload)


def set_session(session: Optional[Session]) -> None:
    state = load_state()
    if session is None:
        state.pop("session", None)
    else:
        state["session"] = session.as_dict()
    save_state(state)


def get_setting(key: str, default: Optional[str] = None) -> Optional[str]:
    env_key = f"GROUNDING_{key.upper()}"
    if env_key in os.environ:
        return os.environ[env_key]
    state = load_state()
    settings = state.get("settings", {})
    if not isinstance(settings, dict):
        return default
    value = settings.get(key)
    return value if isinstance(value, str) else default


def set_setting(key: str, value: str) -> None:
    state = load_state()
    settings = state.setdefault("settings", {})
    settings[key] = value
    save_state(state)


def clear_settings(keys: Optional[list[str]] = None) -> None:
    state = load_state()
    if "settings" not in state:
        return
    if keys is None:
        state.pop("settings", None)
    else:
        settings = state.get("settings") or {}
        for key in keys:
            settings.pop(key, None)
    save_state(state)


def get_token(name: str) -> Optional[Dict[str, Any]]:
    state = load_state()
    tokens = state.get("tokens") or {}
    token = tokens.get(name)
    if not isinstance(token, dict):
        return None
    secret = token.get("token")
    stored = load_secret(name, secret)
    result = dict(token)
    if stored:
        result["token"] = stored
    return result


def list_tokens() -> Dict[str, Dict[str, Any]]:
    state = load_state()
    tokens = state.get("tokens") or {}
    return {str(k): v for k, v in tokens.items() if isinstance(v, dict)}


def set_token(name: str, token_payload: Dict[str, Any]) -> None:
    state = load_state()
    tokens = state.setdefault("tokens", {})
    secret = token_payload.get("token")
    if secret:
        store_secret(name, secret)
        if has_keyring():
            token_payload = {**token_payload, "token": None}
    tokens[name] = token_payload
    save_state(state)


def delete_token(name: str) -> None:
    state = load_state()
    tokens = state.get("tokens")
    if isinstance(tokens, dict) and name in tokens:
        tokens.pop(name)
        save_state(state)
    delete_secret(name)


__all__ = [
    "Session",
    "get_session",
    "set_session",
    "load_state",
    "save_state",
    "get_setting",
    "set_setting",
    "clear_settings",
    "get_token",
    "list_tokens",
    "set_token",
    "delete_token",
    "ensure_directories",
]
