"""SSH key management commands for Flow CLI.

Commands to list, sync, and manage SSH keys between the local system and the
Provider's platform.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Any, TypedDict

import click
from rich.console import Console

import flow.sdk.factory as sdk_factory
from flow.adapters.metrics.telemetry import Telemetry
from flow.cli.app import OrderedDYMGroup
from flow.cli.commands.base import BaseCommand
from flow.cli.ui.presentation.animated_progress import AnimatedEllipsisProgress
from flow.cli.ui.presentation.next_steps import render_next_steps_panel
from flow.cli.ui.presentation.table_styles import create_flow_table, wrap_table_in_panel
from flow.cli.ui.runtime.shell_completion import complete_ssh_key_identifiers as _complete_ssh_keys
from flow.cli.utils.error_handling import cli_error_guard
from flow.cli.utils.json_output import iso_z, print_json
from flow.cli.utils.ssh_key_index_cache import SSHKeyIndexCache
from flow.cli.utils.step_progress import StepTimeline
from flow.cli.utils.theme_manager import theme_manager as _tm
from flow.cli.utils.user_utils import UserInfoError, get_sanitized_username
from flow.core.keys.identity import (
    _load_all as load_all_key_metadata,
)
from flow.core.keys.identity import (
    get_local_key_private_path as _id_get_local,
)
from flow.core.keys.identity import (
    store_key_metadata,
)
from flow.core.utils.ssh_key import (
    LocalSSHKey,
    PlatformSSHKey,
    discover_local_ssh_keys,
    match_local_key_to_platform,
    normalize_public_key,
)
from flow.domain.ssh.resolver import SmartSSHKeyResolver

logger = logging.getLogger(__name__)

# Constants
AUTO_KEY_PREFIX = "flow-auto-"
FLOW_PREFIX = "flow:"
PLATFORM_ID_PREFIX = "sshkey_"
AUTO_SENTINEL = "_auto_"


def truncate_platform_id(platform_id: str, max_len: int = 10) -> str:
    """Truncate platform ID for display, keeping prefix intact."""
    if not platform_id or len(platform_id) <= max_len:
        return platform_id

    # Keep the sshkey_ prefix and first few chars of the actual ID
    if platform_id.startswith("sshkey_"):
        return f"sshkey_{platform_id[7 : 7 + max_len - 7]}…"
    return f"{platform_id[: max_len - 1]}…"


def truncate_key_name(name: str, max_len: int = 26) -> str:
    """Truncate key name for consistent display using center-ellipsis.

    If the name starts with the active bullet ("● "), preserve it and
    center-truncate the remainder so the overall length does not exceed
    max_len.
    """
    if not name or len(name) <= max_len:
        return name

    ellipsis = "…"
    bullet_prefix = "● "

    # Preserve leading bullet if present
    if name.startswith(bullet_prefix):
        core = name[len(bullet_prefix) :]
        remaining_len = max_len - len(bullet_prefix)
        if remaining_len <= len(ellipsis):
            return f"{bullet_prefix}{ellipsis}"

        available = remaining_len - len(ellipsis)
        left_len = (available + 1) // 2
        right_len = available // 2

        if len(core) <= available:
            return f"{bullet_prefix}{core}"

        right_part = core[-right_len:] if right_len > 0 else ""
        return f"{bullet_prefix}{core[:left_len]}{ellipsis}{right_part}"

    # Generic center truncation
    if max_len <= len(ellipsis):
        return ellipsis

    available = max_len - len(ellipsis)
    left_len = (available + 1) // 2
    right_len = available // 2

    right_part = name[-right_len:] if right_len > 0 else ""
    return f"{name[:left_len]}{ellipsis}{right_part}"


# ============================================================================
# Helper Functions for SSH Key List Command
# ============================================================================


def _fetch_ssh_key_data(flow) -> tuple[list, list[LocalSSHKey], list[PlatformSSHKey]]:
    """Fetch SSH key data from config, local system, and platform.

    Returns:
        tuple: (configured_keys, local_keys, platform_keys)
    """
    configured_keys = flow.config.provider_config.get("ssh_keys", [])
    local_keys = discover_local_ssh_keys()

    # Get platform keys via provider
    raw_keys = flow.list_platform_ssh_keys()
    platform_keys = [PlatformSSHKey.from_api(rk) for rk in raw_keys]

    return configured_keys, local_keys, platform_keys


class EnrichedKeyMapping(TypedDict):
    """Result of enriching and mapping local SSH keys with platform data.

    Attributes:
        user_keys: List of (name, path) tuples for user-provided keys
        auto_keys: List of (name, path) tuples for auto-generated keys
        key_tuple_to_platform: Maps (key_name, path_str) tuples to platform_id strings
        local_platform_ids: Set of platform IDs that have corresponding local key files
    """

    user_keys: list[tuple[str, Path]]
    auto_keys: list[tuple[str, Path]]
    key_tuple_to_platform: dict[tuple[str, str], str]
    local_platform_ids: set[str]


def _enrich_and_map_keys(
    local_keys: list[LocalSSHKey],
    platform_keys: list[PlatformSSHKey],
    metadata: dict[str, Any],
) -> EnrichedKeyMapping:
    """Enrich local keys with platform data and create mappings.

    This consolidates key enrichment and platform mapping into a single pass:
    1. Starts with raw filesystem scan (e.g., "id_ed25519")
    2. Uses metadata to enrich with platform names and build platform_id mappings
    3. Does cryptographic matching (pubkey/fingerprint) for any unmapped keys
    4. Categorizes into user_keys vs auto_keys for display

    Args:
        local_keys: List of LocalSSHKey objects from discover_local_ssh_keys()
        platform_keys: List of PlatformSSHKey objects from platform API
        metadata: Metadata dict from ~/.flow/ identity store

    Returns:
        EnrichedKeyMapping with:
            - user_keys: List of (name, path) tuples for user keys (enriched names)
            - auto_keys: List of (name, path) tuples for auto-generated keys (enriched names)
            - key_tuple_to_platform: Dict mapping (name, path) -> platform_id
            - local_platform_ids: Set of platform IDs that have local files

    Example:
        Input:  local_keys=[("id_ed25519", Path)]
        Output: {"user_keys": [("production-key", Path), ("staging-key", Path)],
                 "key_tuple_to_platform": {("production-key", "..."): "sshkey_111", ...},
                 ...}
    """

    user_keys = []
    auto_keys = []
    key_tuple_to_platform = {}
    local_platform_ids = set()

    # Phase 1: Enrich keys using metadata (authoritative source)
    # ============================================================
    # Metadata provides: platform names, platform IDs, auto-generated flags
    # This replaces generic filenames with meaningful platform names

    # Track which file paths we've processed (one file can have multiple platform IDs)
    metadata_processed_paths = set()

    # Initially categorize scanned keys by prefix (will be replaced by metadata)
    scanned_user_keys = []
    scanned_auto_keys = []
    for key_pair in local_keys:
        if key_pair.name.startswith(AUTO_KEY_PREFIX):
            scanned_auto_keys.append((key_pair.name, key_pair.private_key_path))
        else:
            scanned_user_keys.append((key_pair.name, key_pair.private_key_path))

    # Process metadata to enrich names and build platform mappings
    for platform_id, info in metadata.items():
        if not isinstance(info, dict) or "private_key_path" not in info:
            continue

        private_path = Path(info["private_key_path"])
        if not private_path.exists():
            continue

        # Normalize path for consistent comparison with discover_local_ssh_keys() results
        private_path = private_path.resolve()

        path_str = str(private_path)
        key_name = info.get("key_name", private_path.stem)
        is_auto = info.get("auto_generated", False) or key_name.startswith(AUTO_KEY_PREFIX)

        # Remove scanned entries for this path (only once per unique file)
        if path_str not in metadata_processed_paths:
            scanned_user_keys = [(n, p) for n, p in scanned_user_keys if str(p) != path_str]
            scanned_auto_keys = [(n, p) for n, p in scanned_auto_keys if str(p) != path_str]
            metadata_processed_paths.add(path_str)

        # Add enriched entry with platform name
        if is_auto:
            display_name = (
                f"{FLOW_PREFIX}{key_name}" if not key_name.startswith(FLOW_PREFIX) else key_name
            )
            auto_keys.append((display_name, private_path))
        else:
            user_keys.append((key_name, private_path))

        # Build platform mapping
        key_tuple_to_platform[(key_name, str(private_path))] = platform_id
        local_platform_ids.add(platform_id)

    # Add back any scanned keys that weren't in metadata (will be matched cryptographically)
    user_keys.extend(scanned_user_keys)
    auto_keys.extend(scanned_auto_keys)

    # Phase 2: Cryptographic matching for unmapped keys
    # ==================================================
    # For keys not in metadata, try to find their platform ID using:
    # 1. Public key content matching (most reliable)
    # 2. Fingerprint matching (fallback)
    # 3. Name matching (last resort)

    for key_pair in local_keys:
        # Skip if already mapped via metadata
        if (key_pair.name, str(key_pair.private_key_path)) in key_tuple_to_platform:
            continue

        # Use shared matching utility (tries content, fingerprint, name in order)
        platform_id = match_local_key_to_platform(
            key_pair.private_key_path, platform_keys, match_by_name=True
        )

        # Record the match
        if platform_id:
            path_resolved = str(key_pair.private_key_path.resolve())
            key_tuple_to_platform[(key_pair.name, path_resolved)] = platform_id
            local_platform_ids.add(platform_id)

    return {
        "user_keys": user_keys,
        "auto_keys": auto_keys,
        "key_tuple_to_platform": key_tuple_to_platform,
        "local_platform_ids": local_platform_ids,
    }


def _render_json_output(
    configured_keys,
    user_keys,
    auto_keys,
    platform_keys,
    key_tuple_to_platform,
    local_platform_ids,
    show_auto,
) -> None:
    """Render JSON output for automation."""
    # Build configured keys list
    configured = []
    for key_ref in configured_keys:
        if isinstance(key_ref, str) and key_ref.startswith(PLATFORM_ID_PREFIX):
            configured.append(
                {
                    "type": "platform_id",
                    "id": key_ref,
                    "present_local": key_ref in local_platform_ids,
                    "present_platform": True,
                }
            )
        else:
            # Local path or name
            p = Path(str(key_ref)).expanduser().resolve()
            local_path = str(p)

            has_platform = any(
                pid for (name, path), pid in key_tuple_to_platform.items() if path == local_path
            )
            configured.append(
                {
                    "type": "local",
                    "path": local_path,
                    "present_local": True,
                    "present_platform": has_platform,
                }
            )

    # Build local keys list
    local_list = [
        {
            "name": name,
            "path": str(path),
            "platform_id": key_tuple_to_platform.get((name, str(path.resolve())), None),
        }
        for name, path in user_keys
    ]

    if show_auto:
        local_list += [
            {
                "name": name,
                "path": str(path),
                "platform_id": key_tuple_to_platform.get(
                    (name.replace(FLOW_PREFIX, ""), str(path.resolve())), None
                ),
            }
            for name, path in auto_keys
        ]

    # Build platform keys list
    platform_list = [
        {
            "id": getattr(pk, "fid", None),
            "name": getattr(pk, "name", None),
            "required": getattr(pk, "required", False),
        }
        for pk in platform_keys
    ]

    print_json(
        {
            "configured": configured,
            "local": local_list,
            "platform": platform_list,
        }
    )


def _compute_statistics(
    configured_keys, user_keys, platform_keys, key_tuple_to_platform, local_platform_ids
) -> tuple[int, int]:
    """Compute statistics about local-only and platform-only keys.

    Returns:
        tuple: (local_only_count, platform_only_count)
    """
    # Count local-only keys (not uploaded)
    local_only_count = 0
    for key_ref in configured_keys:
        if not isinstance(key_ref, str) or key_ref.startswith(PLATFORM_ID_PREFIX):
            continue

        p = Path(key_ref).expanduser().resolve()
        has_platform = any(
            pid for (name, path), pid in key_tuple_to_platform.items() if path == str(p)
        )
        if p.exists() and not has_platform:
            local_only_count += 1

    # Add user keys not in config and not on platform
    for name, path in user_keys:
        if not key_tuple_to_platform.get((name, str(path)), ""):
            local_only_count += 1

    # Count platform-only keys (missing locally)
    platform_only_count = sum(1 for pkey in platform_keys if pkey.fid not in local_platform_ids)

    return local_only_count, platform_only_count


def _sync_keys_to_platform(console, user_keys, key_tuple_to_platform, ssh_key_manager) -> int:
    """Sync local user keys to platform.

    Returns:
        int: Number of keys synced
    """
    from rich.text import Text

    synced_count = 0
    timeline = None

    try:
        timeline = StepTimeline(console, title="flow ssh-keys", title_animation="auto")
        timeline.start()
        idx_sync = timeline.add_step("Uploading SSH keys", show_bar=True)
        timeline.start_step(idx_sync)

        # Show interrupt hint
        accent = _tm.get_color("accent")
        hint = Text()
        hint.append("  Press ")
        hint.append("Ctrl+C", style=accent)
        hint.append(" to stop syncing. Keys already uploaded remain on platform.")
        timeline.set_active_hint_text(hint)
    except Exception:
        logger.debug("Failed to initialize timeline", exc_info=True)
        timeline = None

    try:
        for name, path in user_keys:
            pub_path = path.with_suffix(".pub")
            if not pub_path.exists():
                continue

            # Check if already synced
            if (name, str(path)) in key_tuple_to_platform:
                console.print(f"  - {name} already synced")
                continue

            try:
                result = ssh_key_manager.get_or_create_key_if_file_path([str(path)])
                if result:
                    console.print(f"  ✓ Uploaded {name}")
                    synced_count += 1
            except Exception as e:
                from rich.markup import escape

                console.print(f"  ✗ Failed to upload {name}: {escape(str(e))}")
                logger.debug(f"Upload failed for {name}", exc_info=True)
    finally:
        if timeline is not None:
            timeline.complete_step()
            timeline.finish()

    return synced_count


def _render_table_output(
    console,
    configured_keys,
    user_keys,
    auto_keys,
    platform_keys,
    key_tuple_to_platform,
    local_platform_ids,
    show_auto,
    verbose,
) -> tuple[int, list[dict[str, str]]]:
    """Render the SSH keys table.

    Returns:
        tuple: (active_key_count, displayed_refs)
    """

    # Helper functions
    def checkmark(is_true: bool) -> str:
        return "[success]✓[/success]" if is_true else "[dim]-[/dim]"

    def active_dot(is_active: bool) -> str:
        return "●" if is_active else ""

    # Create table
    table = create_flow_table(show_borders=False, expand=False)
    table.add_column("#", style="white", width=4, header_style="bold white", justify="right")
    table.add_column("Name", style="white", width=26, header_style="bold white", justify="left")
    table.add_column("Local", style="white", width=8, header_style="bold white", justify="center")
    table.add_column(
        "Platform", style="white", width=10, header_style="bold white", justify="center"
    )
    table.add_column("Active", style="white", width=8, header_style="bold white", justify="center")
    if verbose:
        table.add_column(
            "ID",
            style=_tm.get_color("warning"),
            width=14,
            header_style="bold white",
            justify="left",
        )

    # Build lookups
    platform_keys_by_id = {pkey.fid: pkey for pkey in platform_keys}
    required_key_ids = {pkey.fid for pkey in platform_keys if getattr(pkey, "required", False)}

    # Track state
    active_key_count = 0
    row_index = 1
    displayed_refs: list[dict[str, str]] = []
    seen: set[str] = set()

    # 1. Show active keys (from config) first
    for key_ref in configured_keys:
        found = False

        # Special case: deprecated '_auto_' sentinel
        if isinstance(key_ref, str) and key_ref.strip() == AUTO_SENTINEL:
            name = truncate_key_name("Generate on Mithril [dim](deprecated)[/dim]")
            row = [str(row_index), name, checkmark(False), checkmark(False), active_dot(True)]
            if verbose:
                row.append("")
            table.add_row(*row)
            active_key_count += 1
            displayed_refs.append({"ref": AUTO_SENTINEL, "type": "sentinel"})
            row_index += 1
            continue

        # Check if it's a platform ID
        if (
            isinstance(key_ref, str)
            and key_ref.startswith(PLATFORM_ID_PREFIX)
            and key_ref in platform_keys_by_id
        ):
            pkey = platform_keys_by_id[key_ref]

            # Find local key for this platform ID
            local_path = None
            for (_name, path), pid in key_tuple_to_platform.items():
                if pid == key_ref:
                    local_path = path
                    break

            name = truncate_key_name(getattr(pkey, "name", ""))
            if key_ref in required_key_ids:
                name = f"{name} [dim](required)[/dim]"

            row = [
                str(row_index),
                name,
                checkmark(bool(local_path)),
                checkmark(True),
                active_dot(True),
            ]
            if verbose:
                row.append(truncate_platform_id(key_ref))
            table.add_row(*row)

            active_key_count += 1
            seen.add(f"platform:{key_ref}")
            if local_path:
                seen.add(f"local:{local_path}")
            displayed_refs.append({"ref": key_ref, "type": "platform_id"})
            row_index += 1
            found = True

        if not found:
            # Unknown or missing key
            local_guess = False
            guessed_path: Path | None = None

            if isinstance(key_ref, str) and key_ref.startswith(PLATFORM_ID_PREFIX):
                mapped = _id_get_local(key_ref)
                if mapped and mapped.exists():
                    guessed_path = mapped
                    local_guess = True

            if not local_guess:
                p = Path(str(key_ref)).expanduser().resolve()
                guessed_path = p
                local_guess = p.exists()

            name = truncate_key_name(str(key_ref))
            if key_ref in required_key_ids:
                name = f"{name} [dim](required)[/dim]"

            row = [str(row_index), name, checkmark(local_guess), checkmark(False), active_dot(True)]
            if verbose:
                row.append("")
            table.add_row(*row)

            active_key_count += 1
            if isinstance(key_ref, str):
                seen.add(f"config:{key_ref}")
            if local_guess and guessed_path:
                seen.add(f"local:{guessed_path}")

            if (
                isinstance(key_ref, str)
                and key_ref.startswith(PLATFORM_ID_PREFIX)
                and not local_guess
            ):
                displayed_refs.append({"ref": key_ref, "type": "platform_id"})
            else:
                displayed_refs.append({"ref": str(guessed_path or key_ref), "type": "local"})
            row_index += 1

    # 2. Add available keys (not active) - keys that match platform keys
    available_user_keys = [
        (n, p)
        for n, p in user_keys
        if key_tuple_to_platform.get((n, str(p)), "")
        and key_tuple_to_platform.get((n, str(p)), "") not in configured_keys
    ]

    if configured_keys and available_user_keys:
        table.add_section()

    for name, path in available_user_keys:
        platform_id = key_tuple_to_platform.get((name, str(path)), "")
        display_name = name.replace(FLOW_PREFIX, "") if name.startswith(FLOW_PREFIX) else name

        if platform_id and platform_id in platform_keys_by_id:
            row_name = truncate_key_name(getattr(platform_keys_by_id[platform_id], "name", ""))
        else:
            row_name = truncate_key_name(display_name)

        row = [
            str(row_index),
            row_name,
            checkmark(True),
            checkmark(bool(platform_id)),
            active_dot(False),
        ]
        if verbose:
            row.append(truncate_platform_id(platform_id) if platform_id else "")
        table.add_row(*row)

        seen.add(f"local:{path}")
        if platform_id:
            seen.add(f"platform:{platform_id}")
            displayed_refs.append({"ref": platform_id, "type": "platform_id"})
        else:
            displayed_refs.append({"ref": str(path), "type": "local"})
        row_index += 1

    # 3. Add auto-generated keys (if requested)
    if show_auto and auto_keys:
        if configured_keys or available_user_keys:
            table.add_section()

        keys_to_show = auto_keys if verbose else auto_keys[:5]

        for name, path in keys_to_show:
            platform_id = key_tuple_to_platform.get((name, str(path)), "")
            is_configured = platform_id in configured_keys
            display_name = name.replace(FLOW_PREFIX, "")

            row = [
                str(row_index),
                f"[dim]{display_name}[/dim]",
                f"[dim]{checkmark(True)}[/dim]",
                f"[dim]{checkmark(bool(platform_id))}[/dim]",
                f"[dim]{active_dot(is_configured)}[/dim]",
            ]
            if verbose:
                row.append(f"[dim]{truncate_platform_id(platform_id) if platform_id else ''}[/dim]")
            table.add_row(*row)

            displayed_refs.append(
                {"ref": platform_id or str(path), "type": "platform_id" if platform_id else "local"}
            )
            row_index += 1

        if not verbose and len(auto_keys) > 5:
            remaining = len(auto_keys) - 5
            filler = [
                "[dim]…[/dim]",
                f"[dim]... {remaining} more auto-generated[/dim]",
                "[dim]...[/dim]",
                "[dim]...[/dim]",
                "[dim]...[/dim]",
            ]
            if verbose:
                filler.append("[dim]...[/dim]")
            table.add_row(*filler)

    # 4. Add platform-only keys (no local copy)
    platform_only = [
        pkey
        for pkey in platform_keys
        if pkey.fid not in local_platform_ids
        and (not getattr(pkey, "name", "").startswith(AUTO_KEY_PREFIX) or show_auto)
    ]

    if platform_only:
        if configured_keys or available_user_keys or (show_auto and auto_keys):
            table.add_section()

        for pkey in platform_only:
            if f"platform:{pkey.fid}" in seen:
                continue

            is_configured = pkey.fid in configured_keys
            name = truncate_key_name(getattr(pkey, "name", ""))
            if pkey.fid in required_key_ids:
                name = f"{name} [dim](required)[/dim]"

            row = [
                str(row_index),
                name,
                checkmark(False),
                checkmark(True),
                active_dot(is_configured),
            ]
            if verbose:
                row.append(truncate_platform_id(pkey.fid))
            table.add_row(*row)

            seen.add(f"platform:{pkey.fid}")
            displayed_refs.append({"ref": pkey.fid, "type": "platform_id"})
            row_index += 1

    # Display table
    wrap_table_in_panel(table, "SSH Keys", console)

    # Save indices for quick reference
    SSHKeyIndexCache().save_indices(displayed_refs)

    return active_key_count, displayed_refs


@click.command()
@click.option("--sync", is_flag=True, help="Upload local SSH keys to platform")
@click.option("--show-auto", is_flag=True, help="Show auto-generated keys (hidden by default)")
@click.option("--legend", is_flag=True, help="Show a legend explaining columns and icons")
@click.option("--verbose", "-v", is_flag=True, help="Show file paths and detailed information")
@click.option("--json", "output_json", is_flag=True, help="Output JSON for automation")
def list(sync: bool, show_auto: bool, legend: bool, verbose: bool, output_json: bool) -> None:
    """List SSH keys and their state in a simplified, intuitive view.

    \b
    Columns:
      Local     - ✓ present on this machine (private key exists)
      Platform  - ✓ uploaded to current provider (public key on platform)
      Active    - ● used for Flow tasks (configured in ~/.flow/config.yaml)

    \b
    Common Workflows:
      1. First time setup:
         $ flow ssh-key list --sync               # Upload local keys to platform
         # Then add the platform ID to ~/.flow/config.yaml (see: flow ssh-keys info <sshkey_ID>)
         ssh_keys:
           - sshkey_XXX

      2. Check which keys are active:
         $ flow ssh-key list                      # Active keys show ● in the Active column

      3. Clean up unused keys:
         $ flow ssh-key list --show-auto          # Include auto-generated keys
         $ flow ssh-keys delete sshkey_XXX        # Remove from platform
    """
    try:
        console = _tm.create_console()
    except Exception:
        console = Console()

    # Fetch data with progress indicator (skip in JSON mode)
    if output_json:
        flow = sdk_factory.create_client(auto_init=True)
        configured_keys, local_keys, platform_keys = _fetch_ssh_key_data(flow)
    else:
        with AnimatedEllipsisProgress(console, "Loading SSH keys", start_immediately=True):
            flow = sdk_factory.create_client(auto_init=True)
            configured_keys, local_keys, platform_keys = _fetch_ssh_key_data(flow)

    # Load metadata and enrich keys with platform data
    metadata = load_all_key_metadata()

    # Single consolidated pass: enrich names, categorize, and build platform mappings
    enriched = _enrich_and_map_keys(local_keys, platform_keys, metadata)
    user_keys = enriched["user_keys"]
    auto_keys = enriched["auto_keys"]
    key_tuple_to_platform = enriched["key_tuple_to_platform"]
    local_platform_ids = enriched["local_platform_ids"]

    # JSON output (early return)
    if output_json:
        _render_json_output(
            configured_keys,
            user_keys,
            auto_keys,
            platform_keys,
            key_tuple_to_platform,
            local_platform_ids,
            show_auto,
        )
        Telemetry().log_event(
            "ssh_keys.get",
            {"sync": sync, "show_auto": show_auto, "legend": legend, "verbose": verbose},
        )
        return

    # Show initial explanation if no keys configured
    if not configured_keys:
        console.print("\n[warning]ℹ️  No SSH keys configured for Flow tasks.[/warning]")
        if user_keys:
            console.print("   You have local SSH keys that can be used.")
            if not sync:
                console.print(
                    "   Run [accent]flow ssh-key list --sync[/accent] to upload them first."
                )
        console.print()

    # Render table
    active_key_count, displayed_refs = _render_table_output(
        console,
        configured_keys,
        user_keys,
        auto_keys,
        platform_keys,
        key_tuple_to_platform,
        local_platform_ids,
        show_auto,
        verbose,
    )

    # Compute and display statistics
    local_only_count, platform_only_count = _compute_statistics(
        configured_keys, user_keys, platform_keys, key_tuple_to_platform, local_platform_ids
    )

    if active_key_count > 0:
        console.print(
            f"\n[success]✓ {active_key_count} key{'s' if active_key_count > 1 else ''} active for Flow tasks.[/success]"
        )

    if local_only_count or platform_only_count:
        parts = []
        if local_only_count:
            parts.append(
                f"{local_only_count} local key{'s' if local_only_count != 1 else ''} need upload"
            )
        if platform_only_count:
            parts.append(
                f"{platform_only_count} platform key{'s' if platform_only_count != 1 else ''} missing locally"
            )
        console.print(f"[warning]! {'; '.join(parts)}.[/warning]")

    if auto_keys and not show_auto:
        console.print(
            f"[dim]ℹ {len(auto_keys)} auto-generated key{'s' if len(auto_keys) != 1 else ''} hidden. Use --show-auto to show.[/dim]"
        )

    # Show helpful tips
    from flow.cli.ui.presentation.next_steps import render_next_steps_panel as _ns

    tips: list[str] = [
        "flow ssh-keys info 1",
        "flow ssh-keys delete 1",
    ]

    # Suggest linking unmapped platform IDs
    platform_keys_by_id = {pkey.fid: pkey for pkey in platform_keys}
    unmapped_ids = [
        key_ref
        for key_ref in configured_keys
        if isinstance(key_ref, str)
        and key_ref.startswith(PLATFORM_ID_PREFIX)
        and key_ref not in platform_keys_by_id
        and _id_get_local(key_ref) is None
    ]
    if unmapped_ids:
        tips.insert(0, f"flow ssh-keys link {unmapped_ids[0]} ~/.ssh/id_ed25519")

    render_next_steps_panel(console, tips, title="Tips")

    if legend:
        console.print(
            "\n[dim]Legend:[/dim]\n"
            "[dim]- Local: ✓ present on this machine (private key exists)[/dim]\n"
            "[dim]- Platform: ✓ uploaded to current provider (public key on platform)[/dim]\n"
            "[dim]- Active: ● configured for new tasks (listed in ~/.flow/config.yaml)[/dim]\n"
            "[dim]- History: 'flow ssh-keys info <key>' shows past launches (may be empty even if Active)[/dim]"
        )

    # Sync keys if requested
    if sync:
        console.print("\n[bold]Syncing local keys to platform...[/bold]")
        try:
            ssh_key_manager = flow.get_ssh_key_manager()
        except AttributeError:
            console.print("[warning]SSH key management not supported by current provider[/warning]")
            return

        synced_count = _sync_keys_to_platform(
            console, user_keys, key_tuple_to_platform, ssh_key_manager
        )

        if synced_count > 0:
            console.print(
                f"\n[success]Synced {synced_count} key{'s' if synced_count != 1 else ''}[/success]"
            )
        else:
            console.print("\n[warning]All user keys already synced[/warning]")

    # Show actionable next steps if no keys configured
    if not configured_keys:
        console.print("\n[warning]⚠️  No SSH keys configured for Flow tasks[/warning]")

        synced_user_keys = [(n, p) for n, p in user_keys if (n, str(p)) in key_tuple_to_platform]

        if synced_user_keys:
            name, path = synced_user_keys[0]
            platform_id = key_tuple_to_platform[(name, str(path))]
            console.print("\n[dim]Add to ~/.flow/config.yaml:[/dim]")
            console.print(f"[dim]ssh_keys:\n  - {platform_id}[/dim]")
        elif user_keys:
            try:
                from flow.cli.ui.presentation.next_steps import render_next_steps_panel as _ns

                _ns(console, ["flow ssh-key list --sync"], title="Next steps")
            except Exception:
                console.print(
                    "\nNext: [accent]flow ssh-key list --sync[/accent] to upload your keys"
                )
        else:
            render_next_steps_panel(console, ["ssh-keygen -t ed25519"], title="Next steps")

    Telemetry().log_event(
        "ssh_keys.get", {"sync": sync, "show_auto": show_auto, "legend": legend, "verbose": verbose}
    )


@click.command()
@click.argument("key_id", shell_complete=_complete_ssh_keys)
@click.option("--verbose", "-v", is_flag=True, help="Show full public key")
@click.option("--json", "output_json", is_flag=True, help="Output JSON for automation")
def details(key_id: str, verbose: bool, output_json: bool) -> None:
    """Show detailed information about an SSH key.

    KEY: Platform SSH key ID (e.g., sshkey_abc123), key name, or an index (N or :N) from the last 'flow ssh-key list' output

    Shows:
    - Key metadata (name, creation date)
    - Tasks that launched with this key
    - Local key mapping
    """
    try:
        console = _tm.create_console()
    except Exception:
        console = Console()

    try:
        try:
            Telemetry().log_event("ssh_keys.describe", {"verbose": verbose})
        except Exception as e:
            logger.debug(f"Failed to log telemetry: {e}")
        # Get Flow instance and provider-first key view
        flow = sdk_factory.create_client(auto_init=True)
        try:
            ssh_key_manager = flow.get_ssh_key_manager()
        except AttributeError:
            ssh_key_manager = None

        # Get the key details with progress
        with AnimatedEllipsisProgress(console, "Fetching SSH key details"):
            # Accept index, platform ID, platform name, or local key name/path
            from pathlib import Path as _Path

            resolved_key_id = key_id
            key = None
            local_path_from_index = None
            resolved_from_index = False

            # 0) Index shortcuts via SSHKeyIndexCache
            try:
                if key_id.isdigit() or key_id.startswith(":"):
                    ref, err = SSHKeyIndexCache().resolve_index(key_id)
                    if err:
                        console.print(f"\n[error]{err}[/error]")
                        try:
                            render_next_steps_panel(
                                console,
                                [
                                    "flow ssh-key list  [muted]— refresh indices[/muted]",
                                    "Use index shortcuts: [accent]:N[/accent] or [accent]N[/accent]",
                                ],
                                title="Tips",
                            )
                        except Exception:
                            console.print(
                                "[dim]Tip: Re-run 'flow ssh-key list' to refresh indices, then use :N or N[/dim]"
                            )
                        return
                    if ref:
                        resolved_from_index = True
                        rtype = ref.get("type")
                        rval = ref.get("ref", "")
                        if rtype == "platform_id":
                            resolved_key_id = rval
                            if ssh_key_manager is not None:
                                key = ssh_key_manager.get_key(resolved_key_id)
                        elif rtype == "local":
                            # If the cached ref looks like a platform ID, promote it
                            # so index-based describe works even when the list view
                            # couldn't fetch platform keys.
                            if isinstance(rval, str) and rval.startswith("sshkey_"):
                                resolved_key_id = rval
                            # Also try to treat it as a local path for mapping
                            lp = _Path(rval).expanduser().resolve()
                            local_path_from_index = lp if lp.exists() else None
            except Exception as e:
                logger.debug(f"Failed to resolve index {key_id}: {e}")

            # Load platform keys via provider (preferred), fallback to manager
            platform_keys: list
            raw = flow.list_platform_ssh_keys()
            platform_keys = [PlatformSSHKey.from_api(rk) for rk in raw]
            # Fallback to provider-managed list when available
            if not platform_keys and ssh_key_manager is not None:
                platform_keys = ssh_key_manager.list_keys()
            platform_keys_by_id = {getattr(k, "fid", ""): k for k in platform_keys}

            # Fallback: if we didn't find the key in the current project scope,
            # try listing across all projects via the provider init interface.
            if (
                key is None
                and resolved_key_id.startswith("sshkey_")
                and resolved_key_id not in platform_keys_by_id
            ):
                init_interface = flow.get_provider_init()
                all_raw = init_interface.list_ssh_keys(project_id=None)
                if all_raw:
                    all_keys = [PlatformSSHKey.from_api(rk) for rk in all_raw]
                    for k2 in all_keys:
                        if getattr(k2, "fid", "") == resolved_key_id:
                            key = k2
                            break

            # 1) Direct platform ID (prefer resolved id)
            if key is None and resolved_key_id.startswith("sshkey_"):
                key = platform_keys_by_id.get(resolved_key_id)

            # 2) Exact platform name
            if key is None:
                matches = [k for k in platform_keys if getattr(k, "name", "") == key_id]
                if len(matches) == 1:
                    resolved_key_id = getattr(matches[0], "fid", key_id)
                    key = matches[0]
                elif len(matches) > 1:
                    console.print(f"\n[warning]Multiple keys found with name '{key_id}':[/warning]")
                    for m in matches[:15]:
                        console.print(f"  • {m.name} ({m.fid})")
                    if len(matches) > 15:
                        console.print(f"  [dim]... and {len(matches) - 15} more[/dim]")
                    console.print(
                        "\n[dim]Please use the platform ID (sshkey_xxx) with this command[/dim]"
                    )
                    return

            # 2b) If an index resolved to a non-sshkey value, try matching name again
            if (
                key is None
                and resolved_from_index
                and not resolved_key_id.startswith("sshkey_")
                and resolved_key_id != key_id
            ):
                matches = [k for k in platform_keys if getattr(k, "name", "") == resolved_key_id]
                if len(matches) == 1:
                    resolved_key_id = getattr(matches[0], "fid", resolved_key_id)
                    key = matches[0]

            # 3) Local name/path resolution → map by pubkey content
            if key is None:
                # Local name/path resolution → map by pubkey content
                local_path = None
                if ssh_key_manager is not None:
                    local_resolver = SmartSSHKeyResolver(ssh_key_manager)
                    local_path = local_resolver.resolve_ssh_key(key_id)
                if local_path is None:
                    local_path = local_path_from_index
                if local_path is not None:
                    pub_path = local_path.with_suffix(".pub")
                    if pub_path.exists():
                        pub_content = pub_path.read_text().strip()
                        normalized_local = pub_content.strip()
                        for pk in platform_keys:
                            # Prefer public_key direct match when available
                            if getattr(pk, "public_key", None):
                                normalized_pk = pk.public_key.strip()
                                if normalized_local == normalized_pk:
                                    resolved_key_id = getattr(pk, "fid", resolved_key_id)
                                    key = pk
                                    break
                            # Fallback to fingerprint match
                            if not getattr(pk, "public_key", None) and getattr(
                                pk, "fingerprint", None
                            ):
                                import base64
                                import hashlib

                                parts = normalized_local.split()
                                if len(parts) >= 2:
                                    decoded = base64.b64decode(parts[1].encode())
                                    fp = hashlib.md5(decoded).hexdigest()  # nosec
                                    lp_f = ":".join(fp[i : i + 2] for i in range(0, len(fp), 2))
                                    a = lp_f.replace(":", "").lower()
                                    b = str(pk.fingerprint).replace(":", "").lower()
                                    if a == b:
                                        resolved_key_id = getattr(pk, "fid", resolved_key_id)
                                        key = pk
                                        break

            # 4) Final fallback: try as platform ID again (use resolved id)
            if key is None:
                key = platform_keys_by_id.get(resolved_key_id)

            if not key:
                # If the ID looks like a platform ID and is configured, show a partial view
                configured_keys = flow.config.provider_config.get("ssh_keys", [])
                if (
                    isinstance(resolved_key_id, str)
                    and resolved_key_id.startswith("sshkey_")
                    and (resolved_key_id in configured_keys or key_id in configured_keys)
                ):
                    from rich.panel import Panel
                    from rich.table import Table

                    # Build a minimal table with what we know
                    t = Table(show_header=False, box=None, expand=False)
                    t.add_column("f1", style="muted")
                    t.add_column("f2")
                    t.add_row("ID", resolved_key_id)
                    t.add_row("Configured", "yes")
                    # Try to find a local mapping via identity store first
                    local_path = None
                    mapped = _id_get_local(resolved_key_id)
                    if mapped is not None and mapped.exists():
                        local_path = mapped
                    # Do not guess a local key; require explicit link/repair.
                    if local_path:
                        t.add_row("Local key", str(local_path))
                    else:
                        t.add_row("Local key", "unknown")

                    console.print(Panel(t, title="SSH Key", border_style="dim"))

                    # Try to show recent tasks using this key
                    try:
                        init_interface = flow.get_provider_init()
                        records = init_interface.list_tasks_by_ssh_key(resolved_key_id, limit=20)
                        if records:
                            console.print("\n[bold]Recent tasks using this key:[/bold]")
                            for rec in records[:10]:
                                console.print(
                                    f"  • {rec.get('name') or rec.get('task_id')}  "
                                    f"[{rec.get('status', '?')}]  {rec.get('instance_type', '')}  {iso_z(rec.get('created_at'))}"
                                )
                    except Exception as e:
                        logger.debug(f"Failed to list tasks by SSH key: {e}")

                    try:
                        render_next_steps_panel(
                            console,
                            [
                                "flow ssh-key list --sync  [muted]— upload local keys[/muted]",
                                "flow ssh-keys link <sshkey_ID> ~/.ssh/id_ed25519  [muted]— create a local mapping[/muted]",
                                "flow ssh-key list -v      [muted]— verify platform ID[/muted]",
                            ],
                            title="Next steps",
                        )
                    except Exception:
                        console.print(
                            "\n[dim]Tip: Try 'flow ssh-key list --sync' to upload your local keys, then rerun describe.[/dim]"
                        )
                    return
                # Otherwise, keep the error UX but prioritize the link fix when applicable
                console.print(f"\n[error]SSH key '{key_id}' not found[/error]")
                try:
                    tips = [
                        "flow ssh-key list -v  [muted]— show platform IDs[/muted]",
                        "flow ssh-keys info <sshkey_ID>",
                    ]
                    try:
                        # If input looks like a platform ID and there is no local mapping, suggest link first
                        if (
                            isinstance(resolved_key_id, str)
                            and resolved_key_id.startswith("sshkey_")
                            and _id_get_local(resolved_key_id) is None
                        ):
                            tips.insert(
                                0, f"flow ssh-keys link {resolved_key_id} ~/.ssh/id_ed25519"
                            )
                    except Exception as e:
                        logger.debug(f"Failed to check if key has local mapping: {e}")
                    render_next_steps_panel(console, tips, title="Tips")
                except Exception:
                    console.print(
                        "[dim]Tip: Run 'flow ssh-key list -v' to see platform IDs, then rerun: flow ssh-keys info <sshkey_ID>[/dim]"
                    )
                return

            # Check for local copy
            local_keys = discover_local_ssh_keys()

            local_path = None
            for key_pair in local_keys:
                pub_path = key_pair.private_key_path.with_suffix(".pub")
                if pub_path.exists():
                    local_pub = pub_path.read_text().strip()
                    if (
                        hasattr(key, "public_key")
                        and key.public_key
                        and normalize_public_key(local_pub) == normalize_public_key(key.public_key)
                    ):
                        local_path = key_pair.private_key_path
                        break

            # Get configured SSH keys
            configured_keys = flow.config.provider_config.get("ssh_keys", [])
            is_configured = (resolved_key_id in configured_keys) or (key_id in configured_keys)

        # JSON output
        if output_json:
            created = getattr(key, "created_at", None)
            # Gather tasks using key (best-effort)
            tasks_json = []
            try:
                # We attempt to re-run the provider listing with a smaller limit to avoid rework
                init_interface = flow.get_provider_init()
                if hasattr(init_interface, "list_tasks_by_ssh_key"):
                    records = init_interface.list_tasks_by_ssh_key(resolved_key_id, limit=50)
                    for rec in records:
                        tasks_json.append(
                            {
                                "task_id": rec.get("task_id"),
                                "name": rec.get("name") or rec.get("task_id"),
                                "status": rec.get("status"),
                                "instance_type": rec.get("instance_type"),
                                "created_at": iso_z(rec.get("created_at")),
                                "region": rec.get("region"),
                            }
                        )
            except Exception:
                tasks_json = []

            out = {
                "id": getattr(key, "fid", None) or key_id,
                "name": getattr(key, "name", None) or None,
                "created_at": iso_z(created) if created else None,
                "local_path": str(local_path) if local_path else None,
                "configured": is_configured,
                "tasks": tasks_json,
            }
            print_json(out)
            return

        # Create a formatted panel for key info
        from rich.panel import Panel
        from rich.table import Table

        info_table = Table(show_header=False, box=None, padding=(0, 1))
        info_table.add_column(style="bold")
        info_table.add_column()

        info_table.add_row("Platform ID", key.fid)
        info_table.add_row("Name", key.name)
        if hasattr(key, "created_at") and key.created_at:
            info_table.add_row("Created", str(key.created_at))

        if local_path:
            info_table.add_row("Local key", str(local_path))
        else:
            info_table.add_row("Local key", "[dim]Not found[/dim]")

        if is_configured:
            info_table.add_row("Status", "[success]● Active[/success] (in ~/.flow/config.yaml)")
        else:
            info_table.add_row("Status", "[dim]Available[/dim]")

        console.print("\n")
        from flow.cli.utils.theme_manager import theme_manager as _tm_panel

        console.print(
            Panel(
                info_table,
                title="[bold]SSH Key Details[/bold]",
                border_style=_tm_panel.get_color("accent"),
            )
        )

        # Find tasks using this key
        console.print("\n[bold]Tasks launched with this key:[/bold]")

        with AnimatedEllipsisProgress(console, "Searching task history"):
            tasks_using_key = []

            # Provider-neutral approach: ask provider init interface if supported
            try:
                init_interface = flow.get_provider_init()
                if hasattr(init_interface, "list_tasks_by_ssh_key"):
                    records = init_interface.list_tasks_by_ssh_key(resolved_key_id, limit=100)
                    for rec in records:
                        tasks_using_key.append(
                            {
                                "name": rec.get("name") or rec.get("task_id", "task-unknown"),
                                "status": rec.get("status", "unknown"),
                                "instance_type": rec.get("instance_type", "N/A"),
                                "created_at": rec.get("created_at"),
                                "task_id": rec.get("task_id"),
                                "region": rec.get("region", "unknown"),
                            }
                        )
                else:
                    console.print("[dim]Task history not available for this provider[/dim]")
            except Exception as e:
                from rich.markup import escape

                console.print(f"[warning]Could not fetch task history: {escape(str(e))}[/warning]")

        if tasks_using_key:
            # Sort by creation date (newest first)
            tasks_using_key.sort(key=lambda x: x["created_at"] or "", reverse=True)

            # Create a simple table
            from flow.cli.ui.presentation.table_styles import create_flow_table

            table = create_flow_table(show_borders=False, expand=False)
            from flow.cli.utils.theme_manager import theme_manager as _tm_cols

            table.add_column("Task", style=_tm_cols.get_color("accent"), width=20)
            table.add_column("Status", style="white", width=10)
            table.add_column("GPU", style=_tm_cols.get_color("warning"), width=8)
            table.add_column("Region", style=_tm_cols.get_color("info"), width=12)
            table.add_column("Started", style="dim")

            # Group running tasks first
            running_tasks = [t for t in tasks_using_key if t["status"] == "running"]
            other_tasks = [t for t in tasks_using_key if t["status"] != "running"]

            ordered_tasks = running_tasks + other_tasks

            for task_data in ordered_tasks[:15]:  # Show up to 15 tasks
                status_color = {
                    "running": "green",
                    "completed": "blue",
                    "failed": "red",
                    "cancelled": "yellow",
                    "pending": "cyan",
                }.get(task_data["status"].lower(), "white")

                created_str = "Unknown"
                if task_data["created_at"]:
                    try:
                        # Handle both datetime objects and ISO strings
                        if isinstance(task_data["created_at"], str):
                            from datetime import datetime

                            created_dt = datetime.fromisoformat(
                                task_data["created_at"].replace("Z", "+00:00")
                            )
                            created_str = created_dt.strftime("%m-%d %H:%M")
                        else:
                            created_str = task_data["created_at"].strftime("%m-%d %H:%M")
                    except Exception:
                        created_str = str(task_data["created_at"])[:10]

                # Extract GPU type from instance type
                gpu_type = (
                    task_data["instance_type"].split("-")[0]
                    if "-" in task_data["instance_type"]
                    else task_data["instance_type"]
                )

                # Truncate long task names
                task_name = task_data["name"]
                if len(task_name) > 20:
                    task_name = task_name[:17] + "..."

                table.add_row(
                    task_name,
                    f"[{status_color}]{task_data['status']}[/{status_color}]",
                    gpu_type,
                    task_data.get("region", "").replace("us-", "").replace("-1", ""),
                    created_str,
                )

            console.print(table)

            if len(tasks_using_key) > 15:
                console.print(f"\n[dim]... and {len(tasks_using_key) - 15} more tasks[/dim]")

            # Show summary stats
            running_count = len([t for t in tasks_using_key if t["status"] == "running"])
            total_count = len(tasks_using_key)

            console.print(
                f"\n[dim]Total: {total_count} tasks • {running_count} currently running[/dim]"
            )

            # Show quick action for running tasks
            if running_tasks:
                recent_running = running_tasks[0]
                try:
                    render_next_steps_panel(
                        console, [f"flow ssh {recent_running['name']}"], title="Next Steps"
                    )
                except Exception:
                    console.print(
                        f"\n[dim]Connect: [accent]flow ssh {recent_running['name']}[/accent][/dim]"
                    )
        else:
            try:
                from flow.cli.ui.presentation.nomenclature import get_entity_labels as _labels

                console.print(f"[dim]No {_labels().empty_plural} found using this key[/dim]")
            except Exception:
                console.print("[dim]No tasks found using this key[/dim]")
            if not is_configured:
                console.print("\n[dim]To use this key, add it to ~/.flow/config.yaml:[/dim]")
                console.print(f"[dim]ssh_keys:\n  - {resolved_key_id}[/dim]")
                console.print(
                    f"[dim]Command (with yq): yq -i '.ssh_keys += [\"{resolved_key_id}\"]' ~/.flow/config.yaml[/dim]"
                )
                console.print(
                    f"[dim]Fallback (append): printf '\nssh_keys:\n  - {resolved_key_id}\n' >> ~/.flow/config.yaml[/dim]"
                )

        # Show public key if available (collapsed by default)
        if hasattr(key, "public_key") and key.public_key and verbose:
            console.print("\n[bold]Public key:[/bold]")
            console.print(Panel(key.public_key.strip(), border_style="dim"))
        elif hasattr(key, "public_key") and key.public_key:
            # Show fingerprint instead of full key
            import base64
            import hashlib

            try:
                # Parse the public key to get fingerprint
                key_data = key.public_key.strip().split()[1]  # Get the base64 part
                decoded = base64.b64decode(key_data)
                fingerprint = hashlib.md5(decoded).hexdigest()
                fp_formatted = ":".join(
                    fingerprint[i : i + 2] for i in range(0, len(fingerprint), 2)
                )
                console.print(f"\n[dim]Fingerprint: {fp_formatted}[/dim]")
                console.print("[dim]Use --verbose to see full public key[/dim]")
            except Exception:
                console.print("\n[dim]Use --verbose to see full public key[/dim]")

    except Exception as e:
        from rich.markup import escape

        console.print(f"[error]Error: {escape(str(e))}[/error]")
        raise click.ClickException(str(e)) from e


@click.command()
@click.argument("key_id", shell_complete=_complete_ssh_keys)
@click.option("--unset", is_flag=True, help="Unset required (make key optional)")
def require(key_id: str, unset: bool) -> None:
    """Mark an SSH key as required (admin only).

    KEY_ID: Platform SSH key ID (e.g., sshkey_abc123)

    Requires project admin privileges. When a key is required, Mithril expects
    it to be included in launches for the project. Flow also auto-includes
    required keys during launches.
    """
    try:
        console = _tm.create_console()
    except Exception:
        console = Console()

    try:
        flow = sdk_factory.create_client(auto_init=True)
        try:
            ssh_key_manager = flow.get_ssh_key_manager()
        except AttributeError:
            console.print("[warning]SSH key management not supported by current provider[/warning]")
            return

        # Validate key exists
        key = ssh_key_manager.get_key(key_id)
        if not key:
            console.print(f"[error]SSH key {key_id} not found[/error]")
            return

        # Update required flag
        set_required = not unset
        try:
            ok = ssh_key_manager.set_key_required(key_id, set_required)
            if ok:
                label = "required" if set_required else "optional"
                console.print(f"[success]✓[/success] Marked {key_id} as {label}")
            else:
                console.print("[error]Failed to update key requirement[/error]")
        except Exception as e:
            from flow.errors import AuthenticationError

            if isinstance(e, AuthenticationError):
                console.print(
                    "[error]Access denied.[/error] You must be a project administrator to change required keys."
                )
                try:
                    render_next_steps_panel(
                        console,
                        [
                            "flow ssh-keys require <sshkey_FID>  [muted]— ask a project admin[/muted]",
                        ],
                        title="Next steps",
                    )
                except Exception:
                    console.print(
                        "[dim]Tip: Ask a project admin to run: flow ssh-keys require <sshkey_FID>[/dim]"
                    )
                return
            raise

    except Exception as e:
        from rich.markup import escape

        console.print(f"[error]Error: {escape(str(e))}[/error]")
        raise click.ClickException(str(e)) from e


@click.command()
@click.argument("key_identifier", shell_complete=_complete_ssh_keys)
def delete(key_identifier: str) -> None:
    """Delete an SSH key from the platform.

    KEY_IDENTIFIER: Platform SSH key ID (e.g., sshkey_abc123) or key name
    """
    try:
        console = _tm.create_console()
    except Exception:
        console = Console()

    try:
        # Get provider and optional manager from Flow instance
        flow = sdk_factory.create_client(auto_init=True)
        try:
            ssh_key_manager = flow.get_ssh_key_manager()
        except AttributeError:
            ssh_key_manager = None

        # Resolve key identifier to platform ID: support index (:N/N), ID, name, or local path
        key_id = key_identifier
        # 0) Try index cache
        try:
            if key_identifier.isdigit() or key_identifier.startswith(":"):
                ref, err = SSHKeyIndexCache().resolve_index(key_identifier)
                if err:
                    console.print(f"[error]{err}[/error]")
                    try:
                        render_next_steps_panel(
                            console,
                            [
                                "flow ssh-key list  [muted]— refresh indices[/muted]",
                                "Use index shortcuts: [accent]:N[/accent] or [accent]N[/accent]",
                            ],
                            title="Tips",
                        )
                    except Exception:
                        console.print(
                            "[dim]Tip: Re-run 'flow ssh-key list' to refresh indices, then use :N or N[/dim]"
                        )
                    return
                if ref:
                    resolved_local_path = None
                    if ref.get("type") == "platform_id":
                        key_id = ref.get("ref", key_identifier)
                    elif ref.get("type") == "local":
                        # If the cached ref looks like a platform ID, promote it.
                        promote = ref.get("ref")
                        if isinstance(promote, str) and promote.startswith("sshkey_"):
                            key_id = promote
                        # Map local path by pubkey to platform ID (best-effort)
                        from pathlib import Path as _Path

                        lp = _Path(ref.get("ref", "")).expanduser().resolve()
                        resolved_local_path = lp if lp.exists() else None
                        pub = lp.with_suffix(".pub")
                        if pub.exists():
                            content = pub.read_text().strip()
                            for k in ssh_key_manager.list_keys():
                                if getattr(k, "public_key", None) and normalize_public_key(
                                    content
                                ) == normalize_public_key(k.public_key):
                                    key_id = k.fid
                                    break
                    # If still not a platform id and we had a local index, it's local-only
                    if not key_id.startswith("sshkey_") and ref.get("type") == "local":
                        path_hint = (
                            str(resolved_local_path)
                            if resolved_local_path
                            else ref.get("ref", "local key")
                        )
                        console.print(
                            f"[warning]This key exists only locally ({path_hint}). Nothing to delete on platform.[/warning]"
                        )
                        try:
                            render_next_steps_panel(
                                console,
                                [
                                    "flow ssh-keys upload <path>",
                                    "rm -i <path> <path>.pub  [muted]— remove locally[/muted]",
                                ],
                                title="Next steps",
                            )
                        except Exception:
                            console.print(
                                "[dim]To upload to platform: flow ssh-keys upload <path>  ·  To remove locally: rm -i <path> <path>.pub[/dim]"
                            )
                        return
        except Exception as e:
            logger.debug(f"Failed to resolve index for delete command: {e}")

        # Load platform keys via provider (preferred), fallback to manager
        platform_keys: list
        raw = flow.list_platform_ssh_keys()
        platform_keys = [PlatformSSHKey.from_api(rk) for rk in raw]
        if not platform_keys and ssh_key_manager is None:
            console.print("[warning]SSH key management not supported by current provider[/warning]")
            return
        if not platform_keys and ssh_key_manager is not None:
            platform_keys = ssh_key_manager.list_keys()

        # 1) If not a platform ID yet, try name → ID
        if not key_id.startswith("sshkey_"):
            matching_keys = [k for k in platform_keys if getattr(k, "name", "") == key_identifier]

            if not matching_keys:
                console.print(f"[error]SSH key '{key_identifier}' not found[/error]")
                console.print("\n[dim]Available keys:[/dim]")
                all_keys = ssh_key_manager.list_keys()
                for key in all_keys[:10]:  # Show first 10 keys
                    console.print(f"  • {key.name} ({key.fid})")
                if len(all_keys) > 10:
                    console.print(f"  [dim]... and {len(all_keys) - 10} more[/dim]")
                return

            if len(matching_keys) > 1:
                console.print(
                    f"[warning]Multiple keys found with name '{key_identifier}':[/warning]"
                )
                for key in matching_keys:
                    console.print(f"  • {key.name} ({key.fid})")
                console.print(
                    "\n[dim]Please use the platform ID (sshkey_xxx) to delete a specific key[/dim]"
                )
                return

            key_id = getattr(matching_keys[0], "fid", key_identifier)
            console.print(f"[dim]Found key: {matching_keys[0].name} ({key_id})[/dim]")

        # Confirm deletion
        if not click.confirm(f"Delete SSH key {key_id}?"):
            return

        try:
            # Try provider delete first (via Flow facade)
            if flow.delete_platform_ssh_key(key_id):
                console.print(f"[success]✓[/success] Deleted SSH key {key_id}")
                return
            raise RuntimeError("Provider deletion returned False")
        except Exception as e:
            # Normalize common provider errors without importing provider-specific types
            msg = str(e).lower()
            if "not found" in msg:
                console.print(f"[error]SSH key {key_id} not found[/error]")
                console.print("[dim]The key may have already been deleted[/dim]")
                return
            from rich.markup import escape

            console.print(f"[error]{escape(str(e))}[/error]")
            raise click.ClickException(str(e)) from e

    except click.ClickException:
        raise
    except Exception as e:
        from rich.markup import escape

        console.print(f"[error]Error: {escape(str(e))}[/error]")
        raise click.ClickException(str(e)) from e


@click.command()
@click.argument("key_id")
@click.argument("private_key_path")
def link(key_id: str, private_key_path: str) -> None:
    """Link a platform SSH key ID to a local private key.

    Stores a local mapping so runs and details can find your key even
    when the provider cannot list it in the current project.

    Example:
      flow ssh-keys link sshkey_abc123 ~/.ssh/id_ed25519
    """
    try:
        console = _tm.create_console()
    except Exception:
        console = Console()

    try:
        if not isinstance(key_id, str) or not key_id.startswith("sshkey_"):
            console.print("[error]KEY_ID must look like sshkey_…[/error]")
            raise click.ClickException("Invalid KEY_ID")

        priv = Path(private_key_path).expanduser().resolve()
        if priv.suffix == ".pub":
            priv = priv.with_suffix("")
        if not priv.exists():
            console.print(f"[error]Private key not found: {priv}")
            raise click.ClickException("Private key not found")
        pub = priv.with_suffix(".pub")
        if not pub.exists():
            console.print(f"[error]Missing public key: {pub}")
            raise click.ClickException("Missing public key")

        from flow.sdk.helpers.security import check_ssh_key_permissions as _check

        _check(priv)

        try:
            store_key_metadata(
                key_id=key_id,
                key_name=priv.stem,
                private_key_path=priv,
                project_id=None,
                auto_generated=False,
            )
        except Exception as e:
            from rich.markup import escape

            console.print(f"[error]Failed to store mapping: {escape(str(e))}[/error]")
            raise click.ClickException("Failed to store mapping") from e

        console.print(f"[success]✓[/success] Linked {key_id} → {priv}")
        try:
            render_next_steps_panel(
                console,
                ["flow ssh-key list -v  [muted]— verify mapping[/muted]"],
                title="Next steps",
            )
        except Exception:
            pass

    except click.ClickException:
        raise
    except Exception as e:
        from rich.markup import escape

        console.print(f"[error]Error: {escape(str(e))}[/error]")
        raise click.ClickException(str(e)) from e


class SSHKeysCommand(BaseCommand):
    """SSH keys management command."""

    @property
    def name(self) -> str:
        """Command name."""
        return "ssh-key"

    @property
    def help(self) -> str:
        """Command help text."""
        return "Manage SSH keys"

    def get_command(self) -> click.Command:
        """Return the ssh-key command group."""

        @click.group(name="ssh-key", cls=OrderedDYMGroup, invoke_without_command=True)
        @click.option(
            "--verbose", "-v", is_flag=True, help="Show detailed SSH key management guide"
        )
        @cli_error_guard(self)
        def ssh_keys_group(verbose: bool):
            """Manage SSH keys.

            \b
            Examples:
                flow ssh-key list                      # Show all SSH keys
                flow ssh-key upload ~/.ssh/id_rsa.pub  # Upload new key
                flow ssh-key delete sshkey_xxx         # Remove key

            Run 'flow ssh-key' alone to see the complete SSH setup guide.
            """
            # Get the Click context to check if a subcommand was invoked
            ctx = click.get_current_context()

            # Show the SSH Key Management Guide if no subcommand was provided
            if ctx.invoked_subcommand is None:
                try:
                    console = _tm.create_console()
                except Exception:
                    console = Console()
                lines = [
                    "[bold]Initial setup:[/bold]",
                    "  flow ssh-key list --sync          # Upload local keys",
                    "  flow ssh-key list                 # View all keys",
                    "  # Copy platform ID (sshkey_xxx) and add to ~/.flow/config.yaml",
                    "  flow ssh-key repair               # Map platform IDs to local private keys",
                    "",
                    "[bold]Key locations:[/bold]",
                    "  ~/.ssh/                           # Standard SSH keys",
                    "  ~/.flow/keys/                     # Flow-specific keys",
                    "  ~/.flow/config.yaml               # Active key configuration",
                    "",
                    "[bold]Common patterns:[/bold]",
                    "  # Use existing GitHub key",
                    "  flow ssh-key upload ~/.ssh/id_ed25519.pub",
                    "",
                    "  # Generate new key for Flow",
                    "  ssh-keygen -t ed25519 -f ~/.ssh/flow_key",
                    "  flow ssh-key upload ~/.ssh/flow_key.pub",
                    "",
                    "[bold]Configuration in ~/.flow/config.yaml:[/bold]",
                    "  ssh_keys:",
                    "    - sshkey_abc123                 # Platform ID",
                    "    - ~/.ssh/id_rsa                 # Local path",
                    "",
                    "[bold]Troubleshooting:[/bold]",
                    "  • Permission denied → Check key is added: flow ssh-key list",
                    "  • ID has no local key → Run: flow ssh-key repair",
                    "  • Key not found → Run: flow ssh-key list --sync",
                    "  • Multiple keys → Configure in ~/.flow/config.yaml",
                ]
                try:
                    from flow.cli.commands.feedback import feedback as _fb

                    _fb.info("\n".join(lines), title="SSH Key Management Guide", neutral_body=True)
                except Exception:
                    # Fallback to simple prints if feedback panel fails
                    console.print("\nSSH Key Management Guide\n")
                    for ln in lines:
                        console.print(ln)

        @click.command()
        @click.argument("key_path", shell_complete=_complete_ssh_keys)
        @click.option("--name", help="Name for the SSH key on platform (skips interactive prompt)")
        @click.option("--json", "output_json", is_flag=True, help="Output JSON for automation")
        @cli_error_guard(self)
        def upload(key_path: str, name: str | None, output_json: bool):
            """Upload a specific SSH key to the platform.

            \b
            KEY_PATH: Path to your SSH key file. Accepts either:
              - Private key (e.g., ~/.ssh/id_ed25519) – Flow will read or generate the corresponding .pub
              - Public key (e.g., ~/.ssh/id_ed25519.pub)

            If --name is not provided, you'll be prompted to enter a name for the key,
            with the filename (without extension) as the default.
            """
            path = Path(key_path).expanduser().resolve()
            logger.debug(f"Resolved key path: {path}, exists: {path.exists()}")

            if not path.is_file():
                raise FileNotFoundError(f"Key file not found: {path}")

            logger.debug(
                f"Starting SSH key upload: key_path={key_path}, name={name}, output_json={output_json}"
            )

            try:
                console = _tm.create_console()
            except Exception as e:
                logger.warning(f"Failed to create themed console, using default: {e}")
                console = Console()

            # Get provider and optional SSH key manager
            logger.debug("Creating SDK client and getting provider")
            flow = sdk_factory.create_client(auto_init=True)
            provider = flow.provider
            logger.debug(f"Provider created: {type(provider).__name__}")

            # Determine key name - prompt if not provided
            if name:
                key_name = name
                logger.debug(f"Using provided key name: {key_name}")
            else:
                # Get username prefix for default name
                try:
                    username = get_sanitized_username(flow)[:10]
                    username_prefix = f"{username}-"
                    logger.debug(f"Using username prefix: {username_prefix}")
                except UserInfoError as e:
                    logger.debug(f"Could not get username: {e}, using key name without prefix")
                    username_prefix = ""

                default_name = f"{username_prefix}{path.stem}"
                logger.debug(f"Generated default name: {default_name}")
                if not output_json:
                    # Interactive prompt for key name
                    try:
                        key_name = click.prompt(
                            "Enter a name for this key",
                            default=default_name,
                            show_default=True,
                            type=str,
                        ).strip()
                        if not key_name:
                            key_name = default_name
                        logger.debug(f"User provided key name: {key_name}")
                    except (click.Abort, KeyboardInterrupt):
                        console.print("\n[warning]Upload cancelled[/warning]")
                        return
                    except Exception as e:
                        logger.debug(f"Prompt failed, using default: {e}")
                        key_name = default_name
                else:
                    # Non-interactive mode (JSON output) - use default
                    key_name = default_name
                    logger.debug(f"Using default key name (JSON mode): {key_name}")

            uploaded_id = provider.upload_ssh_key(path, key_name, deduplicate=False)
            logger.info(f"Successfully uploaded SSH key with ID: {uploaded_id}")

            if output_json:
                from flow.cli.utils.json_output import print_json

                print_json({"status": "uploaded", "id": uploaded_id, "name": name})
                return

            console.print(
                f"[success]✓[/success] Uploaded SSH key to platform as {key_name} ({uploaded_id})"
            )

        ssh_keys_group.add_command(list, name="list")
        ssh_keys_group.add_command(upload, name="upload")
        ssh_keys_group.add_command(details, name="info")
        ssh_keys_group.add_command(link, name="link")
        ssh_keys_group.add_command(repair, name="repair")
        ssh_keys_group.add_command(delete)
        ssh_keys_group.add_command(require)

        return ssh_keys_group


@click.command()
@click.option(
    "--all", "scan_all", is_flag=True, help="Scan all project keys, not just configured ones"
)
@click.option("--json", "output_json", is_flag=True, help="Output JSON with repair results")
def repair(scan_all: bool, output_json: bool) -> None:
    """Repair SSH key mappings by linking platform IDs to local private keys.

    By default, this scans only the SSH keys configured in your Flow config and
    attempts to find matching local private keys. Use --all to scan all keys in
    your Mithril project.
    """
    try:
        console = _tm.create_console()
    except Exception:
        console = Console()

    try:
        flow = sdk_factory.create_client(auto_init=True)
        try:
            ssh_key_manager = flow.get_ssh_key_manager()
        except AttributeError:
            ssh_key_manager = None

        # Determine target platform key IDs
        target_ids: list[str] = []
        configured = []
        cfg = flow.config.provider_config or {}
        configured = cfg.get("ssh_keys", [])
        default_key = cfg.get("default_ssh_key")
        if default_key:
            configured.append(default_key)

        if scan_all:
            # All project keys via provider/manager
            raw = flow.list_platform_ssh_keys()
            target_ids = [rk.get("id") or rk.get("fid") for rk in raw]
        else:
            # Configured platform IDs only
            target_ids = [k for k in configured if isinstance(k, str) and k.startswith("sshkey_")]

        target_ids = [tid for tid in target_ids if isinstance(tid, str) and tid]
        target_ids = list(dict.fromkeys(target_ids))  # stable dedup

        results = []
        fixed_count = 0
        already_count = 0
        unresolved: list[str] = []

        # Resolve each ID
        for key_id in target_ids:
            # Skip if mapping already exists
            existing_path = _id_get_local(key_id)
            if existing_path is not None:
                already_count += 1
                results.append(
                    {"id": key_id, "status": "already_mapped", "path": str(existing_path)}
                )
                continue

            # Try manager-based local match (uses pubkey/fingerprint logic)
            matched_path = None
            if ssh_key_manager is not None:
                matched_path = ssh_key_manager.find_matching_local_key(key_id)

            if matched_path is not None and matched_path.exists():
                # Persist mapping via identity service
                try:
                    store_key_metadata(
                        key_id=key_id,
                        key_name=matched_path.stem,
                        private_key_path=matched_path,
                        project_id=None,
                        auto_generated=False,
                    )
                    fixed_count += 1
                    results.append({"id": key_id, "status": "mapped", "path": str(matched_path)})
                except Exception:
                    results.append(
                        {"id": key_id, "status": "error", "error": "failed_to_store_mapping"}
                    )
            else:
                unresolved.append(key_id)
                results.append({"id": key_id, "status": "unresolved"})

        if output_json:
            print_json(
                {
                    "scanned": len(target_ids),
                    "fixed": fixed_count,
                    "already": already_count,
                    "unresolved": unresolved,
                    "results": results,
                }
            )
            return

        # Human-readable output
        console.print(
            f"[accent]Scanned:[/accent] {len(target_ids)}  [success]Fixed:[/success] {fixed_count}  [muted]Already:[/muted] {already_count}  [warning]Unresolved:[/warning] {len(unresolved)}"
        )
        for r in results:
            status = r.get("status")
            if status == "mapped":
                console.print(f"  [success]✓[/success] {r['id']} → {r['path']}")
            elif status == "already_mapped":
                console.print(f"  [dim]- already[/dim] {r['id']} → {r['path']}")
            elif status == "unresolved":
                console.print(f"  [warning]![/warning] {r['id']} (no local private key found)")
            else:
                console.print(f"  [error]✗[/error] {r['id']} — {r.get('error', 'error')}")

        if unresolved:
            console.print("\n[warning]Some keys are unresolved.[/warning] Suggestions:")
            console.print("  • Ensure your local ~/.ssh contains the matching private key")
            console.print("  • Or set MITHRIL_SSH_KEY=/path/to/private/key for runs")
            console.print("  • Or upload your local key: flow ssh-keys upload ~/.ssh/<key>.pub")

    except Exception as e:
        from rich.markup import escape

        console.print(f"[error]Error: {escape(str(e))}[/error]")
        raise click.ClickException(str(e)) from e


# Export command instance
command = SSHKeysCommand()
