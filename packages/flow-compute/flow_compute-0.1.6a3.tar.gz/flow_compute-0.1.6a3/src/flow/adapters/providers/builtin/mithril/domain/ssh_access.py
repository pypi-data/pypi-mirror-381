"""SSH access resolution helpers for Mithril provider.

Encapsulates key matching/caching and bid-driven SSH access preparation so the
provider facade can remain thin.
"""

from __future__ import annotations

import logging
from pathlib import Path

from flow.core.keys.resolution import (
    resolve_env_key_path,
    resolve_key_reference,
)
from flow.core.utils.ssh_key_cache import SSHKeyCache

logger = logging.getLogger(__name__)


def parse_ssh_destination(ssh_destination: str | None) -> tuple[str | None, int]:
    """Parse SSH destination string into host and port.

    Args:
        ssh_destination: SSH destination in format "host:port" or just "host"

    Returns:
        Tuple of (host, port) where port defaults to 22
    """
    if not ssh_destination:
        return None, 22

    # Handle "host:port" format
    if ":" in ssh_destination:
        parts = ssh_destination.rsplit(":", 1)
        try:
            return parts[0], int(parts[1])
        except (ValueError, IndexError):
            return ssh_destination, 22

    return ssh_destination, 22


class SshAccessService:
    """Resolves local SSH key to use for a task and prepares access errors.

    This service depends on the provider's `ssh_key_manager` for platform key
    lookup and local key matching. It does not perform any network operations on
    its own beyond accessing the provider's collaborators.
    """

    def __init__(self, ssh_key_manager) -> None:  # type: ignore[no-any-unimported]
        self.ssh_key_manager = ssh_key_manager

    def get_task_ssh_connection_info(
        self,
        task_id: str,
        provider,
    ) -> tuple[Path | None, str]:
        """Get SSH connection info for a task.

        Returns (private_key_path, error_message). Error message is empty string
        on success.
        """
        ssh_cache = SSHKeyCache()

        # Try to discover platform keys to validate cached entry
        bid = provider.api.get_bid(task_id)
        platform_keys = None
        if bid:
            try:
                launch_spec = bid.get("launch_specification", {})
                platform_keys = launch_spec.get("ssh_keys", []) or None
            except Exception:
                platform_keys = None

        cached_path = ssh_cache.get_key_path(task_id, validate_with_platform_keys=platform_keys)
        if cached_path:
            logger.debug(f"Using cached SSH key path for task {task_id}: {cached_path}")
            return Path(cached_path), ""

        logger.debug(f"No cached SSH key found for task {task_id}, performing key discovery")

        ssh_key_path, error_msg = self.prepare_ssh_access(provider, bid)

        if ssh_key_path:
            try:
                ssh_cache.save_key_path(task_id, str(ssh_key_path), platform_key_ids=platform_keys)
                logger.debug(f"Cached SSH key path for task {task_id}: {ssh_key_path}")
            except Exception:
                logger.exception("Failed to save SSH key path to cache")

        return ssh_key_path, error_msg

    def prepare_ssh_access(self, provider, bid: dict) -> tuple[Path | None, str]:
        """Prepare SSH access by finding matching local keys for the bid.

        Returns (private_key_path, error_message). Error message is empty string
        on success.
        """
        # SSH keys configured on the bid
        launch_spec = bid.get("launch_specification", {})
        bid_ssh_keys = launch_spec.get("ssh_keys", []) or []

        # Respect explicit override for power-users/automation (support legacy alias)
        env_path = resolve_env_key_path(("MITHRIL_SSH_KEY", "Mithril_SSH_KEY"))
        if env_path is not None:
            return env_path, ""

        # If the bid has no SSH keys, try conservative fallbacks before failing.
        if not bid_ssh_keys:
            # 1) Try configured platform key IDs from provider config
            try:
                provider_cfg = (
                    provider.config.provider_config
                    if isinstance(provider.config.provider_config, dict)
                    else {}
                )
                cfg_keys = provider_cfg.get("ssh_keys")
                if isinstance(cfg_keys, list) and cfg_keys:
                    logger.debug(
                        "SSH fallback: trying provider-config keys: %s",
                        ", ".join([str(k) for k in cfg_keys]),
                    )
                    for key_id in cfg_keys:
                        try:
                            private_key_path = self.ssh_key_manager.find_matching_local_key(
                                str(key_id)
                            )
                            if private_key_path:
                                logger.debug(
                                    "SSH fallback success: using %s for key %s",
                                    private_key_path,
                                    key_id,
                                )
                                return private_key_path, ""
                        except Exception:
                            continue
            except Exception:
                pass

            # 2) If the task is still pending/starting, surface a more accurate message
            try:
                status = str(bid.get("status", "")).lower()
                instances = bid.get("instances", [])
                if status in {"pending", "open", "starting"} or not instances:
                    return (
                        None,
                        (
                            "Instance is still starting; SSH may not be ready yet.\n"
                            "Try again in 1–2 minutes, or run 'flow status' to check readiness."
                        ),
                    )
            except Exception:
                pass

            # 3) Fail with actionable guidance only when clearly keyless
            return (
                None,
                (
                    "This instance was created without SSH keys; authentication will fail.\n"
                    "Solutions:\n"
                    "  - Add a project SSH key and recreate the dev VM: flow ssh-keys upload ~/.ssh/<your_key>.pub && flow cancel <dev-vm> && flow dev\n"
                    "  - Or set MITHRIL_SSH_KEY=/path/to/private/key and retry\n"
                ),
            )

        # Resolve against platform keys and local names/paths deterministically
        for ssh_key_id in bid_ssh_keys:
            # Platform ID or path-like reference
            private_key_path = resolve_key_reference(ssh_key_id, self.ssh_key_manager)
            if private_key_path:
                return private_key_path, ""

        # No matching key found - build precise error (do not guess a local key)
        key_names: list[str] = []
        for key_id in bid_ssh_keys[:3]:
            try:
                key = self.ssh_key_manager.get_key(key_id)
            except Exception:
                key = None
            key_names.append(f"'{getattr(key, 'name', None)}' ({key_id})" if key else key_id)

        keys_desc = ", ".join(key_names)
        if len(bid_ssh_keys) > 3:
            keys_desc += f" and {len(bid_ssh_keys) - 3} more"

        return (
            None,
            (
                "No matching local SSH key found for required platform key(s): "
                f"{keys_desc}.\n"
                "To fix this:\n"
                "  1. Ensure the corresponding private key exists locally (check ~/.flow/keys and ~/.ssh)\n"
                "  2. Or export MITHRIL_SSH_KEY=/path/to/private/key and retry\n"
                "  3. Or upload your local key to the platform: flow ssh-keys upload ~/.ssh/<key>.pub\n"
            ),
        )
