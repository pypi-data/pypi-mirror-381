"""Supabase REST helpers for the Grounding CLI."""

from __future__ import annotations

import hashlib
import json
import time
from typing import Any, Dict, List, Optional, Tuple

import requests
from rich.console import Console

from .config import Session, get_session, get_setting, set_session
from .oauth import refresh_session as refresh_supabase_session, OAuthError
from .settings import DEFAULT_SUPABASE_ANON_KEY, DEFAULT_SUPABASE_CLIENT_ID, DEFAULT_SUPABASE_URL

console = Console()


class GroundingAPIError(RuntimeError):
    """Raised when a Supabase call fails."""


class GroundingAPI:
    """Lightweight wrapper around the Supabase REST API."""

    def __init__(
        self,
        supabase_url: Optional[str] = None,
        anon_key: Optional[str] = None,
        session: Optional[Session] = None,
    ) -> None:
        self.supabase_url = (supabase_url or get_setting("supabase_url") or DEFAULT_SUPABASE_URL or "").rstrip("/")
        self.anon_key = anon_key or get_setting("supabase_anon_key") or DEFAULT_SUPABASE_ANON_KEY
        self.client_id = get_setting("supabase_client_id") or DEFAULT_SUPABASE_CLIENT_ID
        self.session = session or get_session()
        if not self.supabase_url:
            raise GroundingAPIError("Supabase URL is not configured. Run `grounding auth login` with --supabase-url.")
        if not self.anon_key:
            raise GroundingAPIError(
                "Supabase anon key missing. Set the GROUNDING_SUPABASE_ANON_KEY environment variable or run `grounding config supabase` to save it."
            )
        if not self.session:
            raise GroundingAPIError("Not authenticated. Run `grounding auth login` first.")
        self._ensure_session_valid()

    # ---------------------------------------------------------------------
    # Low-level HTTP helpers
    # ---------------------------------------------------------------------
    def _request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        url = f"{self.supabase_url}{path}"
        headers = kwargs.setdefault("headers", {})
        headers.setdefault("Authorization", f"Bearer {self.session.access_token}")
        headers.setdefault("apikey", self.anon_key)
        headers.setdefault("Content-Type", "application/json")
        try:
            response = requests.request(method, url, timeout=30, **kwargs)
        except requests.RequestException as error:
            raise GroundingAPIError(f"Request to {url} failed: {error}") from error
        if response.status_code >= 400:
            try:
                payload = response.json()
            except json.JSONDecodeError:
                payload = {"error": response.text}
            raise GroundingAPIError(f"Supabase request failed ({response.status_code}): {payload}")
        return response

    # ------------------------------------------------------------------
    # MCP tokens
    # ------------------------------------------------------------------
    def list_agent_tokens(self) -> List[Dict[str, Any]]:
        response = self._request(
            "GET",
            "/rest/v1/mcp_api_tokens",
            params={
                "select": "id,agent_id,token_prefix,developer_id,is_active,metadata,created_at,expires_at",
                "order": "created_at.desc",
            },
        )
        return response.json()

    def issue_agent_token(self, agent_name: str) -> Dict[str, Any]:
        payload = {"agent_name": agent_name}
        response = self._request(
            "POST",
            "/rest/v1/rpc/issue_mcp_agent_token",
            json=payload,
        )
        return response.json()

    def revoke_agent_token(self, token_id: str) -> None:
        self._request(
            "POST",
            "/rest/v1/rpc/revoke_mcp_agent_token",
            json={"token_id": token_id},
        )

    def update_agent_token_metadata(self, token_id: str, label: Optional[str] = None, metadata: Optional[Dict[str, Any]] = None) -> None:
        """Update token metadata including label."""
        # First, fetch existing metadata
        response = self._request(
            "GET",
            "/rest/v1/mcp_api_tokens",
            params={
                "select": "metadata",
                "id": f"eq.{token_id}",
                "limit": "1",
            },
        )
        data = response.json()
        if not data:
            raise GroundingAPIError(f"Token {token_id} not found.")

        # Merge with existing metadata
        existing_meta = data[0].get("metadata") or {}
        meta = existing_meta.copy()

        if metadata is not None:
            meta.update(metadata)
        if label is not None:
            meta["label"] = label
        meta["created_via"] = "cli"

        # Update with merged metadata
        self._request(
            "PATCH",
            f"/rest/v1/mcp_api_tokens?id=eq.{token_id}",
            json={"metadata": meta},
        )

    def verify_agent_token(self, token: str) -> Dict[str, Any]:
        prefix, token_hash = self._split_and_hash_token(token)
        params = {
            "select": "id,agent_id,token_prefix,developer_id,is_active,metadata,created_at,expires_at",
            "token_prefix": f"eq.{prefix}",
            "token_hash": f"eq.{token_hash}",
            "limit": "1",
        }
        response = self._request(
            "GET",
            "/rest/v1/mcp_api_tokens",
            params=params,
        )
        data = response.json()
        if not data:
            raise GroundingAPIError("Token not found or hash mismatch for this developer.")
        return data[0]

    def set_agent_token_billing_mode(self, token_id: str, billing_mode: str) -> None:
        """Set billing mode for an agent token.

        Args:
            token_id: The UUID of the token to update
            billing_mode: Either 'subscription' or 'credits'

        Raises:
            GroundingAPIError: If billing_mode is invalid or update fails
        """
        if billing_mode not in ('subscription', 'credits'):
            raise GroundingAPIError("billing_mode must be 'subscription' or 'credits'")

        self.update_agent_token_metadata(token_id, metadata={"billing_mode": billing_mode})

    def get_billing_status(self) -> Dict[str, Any]:
        """Get current billing status including subscription and credit balance.

        Returns:
            Dict with 'subscription' and 'credits' keys containing billing info
        """
        user_id = self.session.user.get("id")
        if not user_id:
            raise GroundingAPIError("User ID not found in session.")

        # Query for active subscription
        sub_response = self._request(
            "GET",
            "/rest/v1/stripe_subscriptions",
            params={
                "developer_id": f"eq.{user_id}",
                "status": "eq.active",
                "select": "tier,call_limit,call_limit_period,current_period_start,current_period_end",
                "limit": "1",
            },
        )

        # Query for credit balance
        credit_response = self._request(
            "GET",
            "/rest/v1/developer_credits",
            params={
                "developer_id": f"eq.{user_id}",
                "select": "balance_cents,currency",
                "limit": "1",
            },
        )

        sub_data = sub_response.json()
        credit_data = credit_response.json()

        return {
            "subscription": sub_data[0] if sub_data else None,
            "credits": credit_data[0] if credit_data else None,
        }

    @staticmethod
    def _split_and_hash_token(token: str) -> Tuple[str, str]:
        if "." not in token:
            raise GroundingAPIError("Token must be in prefix.secret format.")
        prefix, secret = token.split(".", 1)
        digest = hashlib.sha256(token.encode("utf-8")).hexdigest()
        return prefix, digest

    def _ensure_session_valid(self) -> None:
        if not self.session:
            raise GroundingAPIError("Not authenticated. Run `grounding auth login` first.")
        expires_at = getattr(self.session, "expires_at", None)
        now = int(time.time())
        if expires_at and expires_at - now > 120:
            return
        try:
            refreshed = refresh_supabase_session(
                self.supabase_url,
                self.session.refresh_token,
                client_id=self.client_id,
                anon_key=self.anon_key,
            )
        except OAuthError as error:
            raise GroundingAPIError(f"Failed to refresh session: {error}") from error
        set_session(refreshed)
        self.session = refreshed


__all__ = ["GroundingAPI", "GroundingAPIError"]
