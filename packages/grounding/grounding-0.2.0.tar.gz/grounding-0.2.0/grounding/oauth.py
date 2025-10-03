"""OAuth PKCE helpers for the Grounding CLI."""

from __future__ import annotations

import base64
import hashlib
import json
import secrets
import threading
import time
import webbrowser
from dataclasses import dataclass
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
from typing import Dict, Optional
from urllib.parse import urlencode, urlparse, parse_qs

import requests
from rich.console import Console
from rich.panel import Panel

from .config import Session

console = Console()


class OAuthError(RuntimeError):
    """Raised when the OAuth flow fails."""


@dataclass
class OAuthResult:
    code: str
    state: str


class _CallbackHandler(BaseHTTPRequestHandler):
    """Simple HTTP handler to receive the OAuth redirect."""

    queue: "queue.Queue[OAuthResult]"  # type: ignore[name-defined]
    expected_state: str

    def do_GET(self) -> None:  # noqa: N802 - method name from BaseHTTPRequestHandler
        parsed = urlparse(self.path)
        if parsed.path != "/callback":
            self.send_error(HTTPStatus.NOT_FOUND, "Unknown path")
            return
        params = parse_qs(parsed.query)
        code = params.get("code", [None])[0]
        state = params.get("state", [None])[0] or ""
        if not code:
            self.send_error(HTTPStatus.BAD_REQUEST, "Missing code")
            return
        # Note: State is managed by Supabase for OAuth provider flows, not validated here
        # PKCE code_verifier provides CSRF protection
        payload = OAuthResult(code=code, state=state)
        self.queue.put(payload)  # type: ignore[attr-defined]
        content = "<html><body><h2>Login complete</h2><p>You may close this window.</p></body></html>"
        encoded = content.encode("utf-8")
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()
        self.wfile.write(encoded)

    def log_message(self, format: str, *args) -> None:  # noqa: D401, N802
        """Silence default request logging."""


@dataclass
class OAuthConfig:
    supabase_url: str
    provider: str
    scopes: str
    redirect_host: str
    redirect_port: int
    anon_key: Optional[str] = None
    audience: Optional[str] = None
    client_id: Optional[str] = None
    open_browser: bool = True
    use_local_server: bool = True


def _generate_code_verifier() -> str:
    return base64.urlsafe_b64encode(secrets.token_bytes(32)).decode("utf-8").rstrip("=")


def _code_challenge(verifier: str) -> str:
    digest = hashlib.sha256(verifier.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest).decode("utf-8").rstrip("=")


def _generate_state() -> str:
    return secrets.token_urlsafe(16)


def _build_authorize_url(config: OAuthConfig, state: str, code_challenge: str, redirect_uri: str) -> str:
    params = {
        "provider": config.provider,
        "redirect_to": redirect_uri,
        "response_type": "code",
        "code_challenge": code_challenge,
        "code_challenge_method": "S256",
        "flow_type": "pkce",
    }
    # Note: For OAuth providers like GitHub, Supabase manages scopes via Dashboard config
    # Only pass scope for OIDC flows when needed
    if config.client_id:
        params["client_id"] = config.client_id
    if config.audience:
        params["audience"] = config.audience
    query = urlencode(params, doseq=True)
    return f"{config.supabase_url.rstrip('/')}/auth/v1/authorize?{query}"


def _start_callback_server(config: OAuthConfig, queue):  # type: ignore[no-untyped-def]
    server = HTTPServer((config.redirect_host, config.redirect_port), _CallbackHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server, thread


def perform_pkce_flow(config: OAuthConfig, timeout: float = 300.0) -> Session:
    if not config.supabase_url:
        raise OAuthError("Supabase URL is not configured")

    verifier = _generate_code_verifier()
    challenge = _code_challenge(verifier)
    state = _generate_state()
    redirect_uri = f"http://{config.redirect_host}:{config.redirect_port}/callback"

    authorize_url = _build_authorize_url(config, state, challenge, redirect_uri)

    callback_queue = None
    server = None
    thread = None

    if config.use_local_server:
        import queue

        callback_queue = queue.Queue(maxsize=1)
        _CallbackHandler.queue = callback_queue  # type: ignore[attr-defined]
        _CallbackHandler.expected_state = state  # type: ignore[attr-defined]
        try:
            server, thread = _start_callback_server(config, callback_queue)
        except OSError as error:  # port in use
            console.print(Panel.fit(f"[red]Failed to bind to {redirect_uri}: {error}. Falling back to manual code entry."))
            config.use_local_server = False

    if config.open_browser:
        webbrowser.open(authorize_url, new=1, autoraise=True)
        console.print(Panel.fit("Browser opened for authentication. Complete the login to continue."))
    else:
        console.print(Panel.fit(f"Open the following URL in your browser to complete login:\n{authorize_url}"))

    code = None

    if config.use_local_server and callback_queue is not None:
        try:
            result: OAuthResult = callback_queue.get(timeout=timeout)  # type: ignore[assignment]
            code = result.code
        except Exception:  # queue.Empty
            pass
        finally:
            if server:
                server.shutdown()
            if thread:
                thread.join(timeout=2)

    if not code:
        console.print("If the browser did not redirect back automatically, paste the full callback URL here.")
        try:
            manual_input = console.input("Callback URL: ").strip()
        except (EOFError, KeyboardInterrupt) as error:
            raise OAuthError("Login aborted.") from error
        parsed = urlparse(manual_input)
        code = parse_qs(parsed.query).get("code", [None])[0]
        if not code:
            raise OAuthError("Provided URL did not include OAuth code.")

    token_endpoint = f"{config.supabase_url.rstrip('/')}/auth/v1/token?grant_type=pkce"
    payload: Dict[str, str] = {
        "auth_code": code,
        "code_verifier": verifier,
    }
    if config.client_id:
        payload["client_id"] = config.client_id

    headers = {"Content-Type": "application/json"}
    if config.anon_key:
        headers["apikey"] = config.anon_key

    try:
        response = requests.post(token_endpoint, json=payload, headers=headers, timeout=30)
    except requests.RequestException as error:
        raise OAuthError(f'Failed to reach Supabase token endpoint: {error}') from error
    if response.status_code >= 400:
        try:
            details = response.json()
        except json.JSONDecodeError:
            details = {"error": response.text}
        raise OAuthError(f"Failed to exchange code for token ({response.status_code}): {details}")

    data = response.json()
    session = Session.from_payload(data)
    if not session.access_token or not session.refresh_token:
        raise OAuthError("Authentication succeeded but session payload is incomplete.")
    return session


__all__ = ["OAuthConfig", "perform_pkce_flow", "OAuthError"]


def refresh_session(supabase_url: str, refresh_token: str, *, client_id: Optional[str] = None, anon_key: Optional[str] = None) -> Session:
    if not supabase_url:
        raise OAuthError("Supabase URL is not configured")
    if not refresh_token:
        raise OAuthError("Missing refresh token; please login again.")

    token_endpoint = f"{supabase_url.rstrip('/')}/auth/v1/token"
    payload: Dict[str, str] = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
    }
    if client_id:
        payload["client_id"] = client_id

    headers: Dict[str, str] = {"Content-Type": "application/json"}
    if anon_key:
        headers["apikey"] = anon_key

    try:
        response = requests.post(token_endpoint, json=payload, headers=headers, timeout=30)
    except requests.RequestException as error:
        raise OAuthError(f'Failed to refresh session: {error}') from error

    if response.status_code >= 400:
        try:
            details = response.json()
        except json.JSONDecodeError:
            details = {"error": response.text}
        raise OAuthError(f"Refresh failed ({response.status_code}): {details}")

    data = response.json()
    new_session = Session.from_payload(data)
    if not new_session.access_token or not new_session.refresh_token:
        raise OAuthError("Refresh succeeded but returned session payload is incomplete.")
    return new_session


__all__.append("refresh_session")
