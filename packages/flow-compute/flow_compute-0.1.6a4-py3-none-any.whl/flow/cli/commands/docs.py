"""Docs command for Flow CLI.

Provides quick access to documentation links sourced from centralized
link definitions in `flow.utils.links`. Keeps URLs consistent across the
codebase.
"""

from __future__ import annotations

import click

from flow.cli.commands.base import BaseCommand, console
from flow.cli.utils.theme_manager import theme_manager


class DocsCommand(BaseCommand):
    """Show documentation links."""

    @property
    def name(self) -> str:
        return "docs"

    @property
    def help(self) -> str:
        return "Show links to the Flow/Mithril documentation"

    def get_command(self) -> click.Command:
        @click.command(name=self.name, help=self.help)
        @click.option(
            "--verbose",
            "verbose",
            is_flag=True,
            help="Show additional popular documentation links",
        )
        def docs(verbose: bool) -> None:
            """Print documentation links from the centralized link module."""
            from flow.utils.links import DocsLinks  # Local import to avoid early import cycles

            accent = theme_manager.get_color("accent")
            console.print(f"[bold {accent}]Flow Documentation[/bold {accent}]")

            # Root docs
            console.print(f"Quickstart: [accent]{DocsLinks.flow_quickstart()}[/accent]")

            # Common starting points (keep compute quickstart only)

            if verbose:
                # Popular deep links when requested
                console.print(
                    f"Compute quickstart: [accent]{DocsLinks.compute_quickstart()}[/accent]"
                )
                console.print(f"Spot bids: [accent]{DocsLinks.spot_bids()}[/accent]")
                console.print(
                    f"Spot auction mechanics: [accent]{DocsLinks.spot_auction_mechanics()}[/accent]"
                )
                console.print(f"Startup scripts: [accent]{DocsLinks.startup_scripts()}[/accent]")
                # Replace regions with ephemeral storage and add persistent storage
                console.print(
                    f"Ephemeral storage: [accent]{DocsLinks.ephemeral_storage()}[/accent]"
                )
                console.print(
                    f"Persistent storage: [accent]{DocsLinks.persistent_storage()}[/accent]"
                )

            # Hint when not verbose
            if not verbose:
                from flow.cli.ui.presentation.next_steps import (
                    render_next_steps_panel as _render_ns,
                )

                _render_ns(console, ["flow docs --verbose"], title="Next Steps")

        return docs


# Export command instance
command = DocsCommand()
