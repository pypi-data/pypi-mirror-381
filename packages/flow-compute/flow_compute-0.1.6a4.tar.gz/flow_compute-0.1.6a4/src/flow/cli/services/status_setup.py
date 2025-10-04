"""Setup helpers for status command pre-execution concerns."""

from __future__ import annotations

import os


def apply_project_env(project: str | None) -> None:
    """If provided, set project env vars before creating Flow().

    The provider context resolves the project from ``MITHRIL_PROJECT_ID``.
    Set that primary variable, and also set legacy ``MITHRIL_PROJECT`` for
    downstream helpers that still read it.
    """
    if not project:
        return
    try:
        # Primary env used by provider context
        os.environ["MITHRIL_PROJECT_ID"] = project
        # Legacy alias used by some CLI helpers
        os.environ["MITHRIL_PROJECT"] = project
    except Exception:
        pass


def apply_force_refresh() -> None:
    """Clear HTTP caches when --force-refresh is set."""
    try:
        # Clear cache through the HTTP client pool
        from flow.adapters.http.client import HttpClientPool

        # Clear all pooled clients' caches
        for client in HttpClientPool._clients.values():
            if hasattr(client, "clear_cache"):
                client.clear_cache()
    except Exception:
        pass
