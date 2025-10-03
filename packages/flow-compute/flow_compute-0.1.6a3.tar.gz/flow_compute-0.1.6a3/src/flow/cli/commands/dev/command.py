"""Dev command - persistent development VM with optional isolated environments.

Provides a persistent VM for development with two modes:

1. Default mode: Direct VM execution (no containers)
2. Named environments: Container-isolated environments for different projects
"""

from __future__ import annotations

import logging
import shlex
import time
from contextlib import suppress

import click

from flow.cli.commands.base import BaseCommand, console
from flow.cli.commands.dev.executor import DevContainerExecutor
from flow.cli.commands.dev.upload_manager import DevUploadManager
from flow.cli.commands.dev.utils import sanitize_env_name
from flow.cli.commands.dev.vm_manager import DevVMManager
from flow.cli.utils.error_handling import cli_error_guard
from flow.errors import AuthenticationError, FlowError, TaskNotFoundError, ValidationError
from flow.sdk.client import Flow

logger = logging.getLogger(__name__)


class DevCommand(BaseCommand):
    """Development environment command implementation."""

    @property
    def name(self) -> str:
        return "dev"

    @property
    def help(self) -> str:
        return """Persistent dev VM (default instance: h100) - default runs directly, named envs use containers

Examples:
  flow dev                         # SSH to VM
  flow dev -- nvidia-smi           # Check GPUs (trailing command)
  flow dev -- python train.py      # Run script"""

    def get_command(self) -> click.Command:
        @click.command(name=self.name, help=self.help)
        @click.argument("cmd_arg", required=False)
        @click.argument("remote_cmd", nargs=-1)
        @click.option(
            "--env",
            "-e",
            default="default",
            help="Environment: 'default' (VM) or named (container)",
        )
        @click.option(
            "--instance-type",
            "-i",
            help=(
                "Instance type for dev VM (e.g., a100, h100). If an existing dev VM"
                " has a different instance type, a new dev VM is created instead of reusing."
            ),
        )
        @click.option(
            "--region", "-r", help="Preferred region for the dev VM (e.g., us-central1-b)"
        )
        @click.option("--image", help="Docker image for container execution")
        @click.option(
            "--ssh-keys",
            "-k",
            multiple=True,
            help=(
                "Authorized SSH keys (repeatable). Accepts: platform key ID like 'sshkey_ABC123', "
                "a local private key path like '~/.ssh/id_ed25519', or a key name like 'id_ed25519'. "
                "Repeat -k/--ssh-keys for multiple values. Example: "
                "-k ~/.ssh/id_ed25519 -k sshkey_ABC123 -k work_laptop"
            ),
        )
        @click.option("--reset", "-R", is_flag=True, help="Reset all containers")
        @click.option(
            "--stop",
            "-S",
            is_flag=True,
            help=(
                "Stop the current user's most recent dev VM (pending/provisioning or running). "
                "Use 'flow cancel <task-id>' to stop others."
            ),
        )
        @click.option("--info", "status", is_flag=True, help="Show dev environment status")
        @click.option(
            "--status", "status", is_flag=True, help="Show dev environment status", hidden=True
        )
        @click.option("--force-new", is_flag=True, help="Force creation of new dev VM")
        @click.option("--max-price-per-hour", "-m", type=float, help="Maximum hourly price in USD")
        @click.option(
            "--upload/--no-upload",
            default=True,
            help="Upload current directory to VM (default: upload)",
        )
        @click.option(
            "--upload-path", default=".", help="Path to upload (default: current directory)"
        )
        @click.option(
            "--no-unique", is_flag=True, help="Don't append unique suffix to VM name on conflict"
        )
        @click.option(
            "--json", "output_json", is_flag=True, help="Output JSON (for use with --info)"
        )
        @click.option("--verbose", "-v", is_flag=True, help="Show detailed examples and workflows")
        @click.option(
            "--flat/--nested",
            "flat",
            default=False,
            help=(
                "Place current dir contents directly into parent (flat). Default uploads into '~/<dir>'."
            ),
        )
        @cli_error_guard(self)
        def dev(
            cmd_arg: str | None,
            remote_cmd: tuple[str, ...],
            env: str,
            instance_type: str | None,
            region: str | None,
            image: str | None,
            ssh_keys: tuple,
            reset: bool,
            stop: bool,
            status: bool,
            force_new: bool,
            max_price_per_hour: float | None,
            upload: bool,
            upload_path: str,
            flat: bool,
            no_unique: bool,
            output_json: bool,
            verbose: bool,
        ):
            if verbose:
                console.print("\n[bold]Flow Dev - Architecture & Usage:[/bold]\n")
                console.print("[underline]Two Modes:[/underline]")
                console.print("1. DEFAULT: Direct VM execution (no containers)")
                console.print("   • Commands run directly on persistent VM")
                console.print("   • Packages install to /root")
                console.print("   • Zero overhead, maximum speed")
                console.print("   • Like SSH but with auto code upload\n")
                console.print("2. NAMED ENVS: Container isolation")
                console.print("   • Each env gets isolated container")
                console.print("   • Packages install to /envs/NAME")
                console.print("   • Clean separation between projects")
                console.print("   • Read-only access to /root as /shared\n")
                console.print("[underline]Examples:[/underline]")
                console.print("# Default environment (direct VM):")
                console.print("flow dev                           # SSH to VM")
                console.print("flow dev -- pip install numpy       # Install on VM")
                console.print("flow dev -- python train.py         # Uses numpy")
                console.print("flow dev -- nvidia-smi              # Check GPUs\n")
                console.print("# Named environments (containers):")
                console.print("flow dev -e ml -- pip install tensorflow")
                console.print("flow dev -e web -- npm install express")
                console.print("flow dev -e ml -- python app.py    # Has TF, not express\n")
                console.print("# Management:")
                console.print("flow dev --info                    # Check VM & environments")
                console.print("flow dev --stop                    # Stop VM completely\n")
                console.print("[underline]File Structure:[/underline]")
                console.print("/root/           # Default env & shared data")
                console.print("/envs/ml/        # Named env 'ml'")
                console.print("/envs/web/       # Named env 'web'\n")
                console.print("[underline]Key Points:[/underline]")
                console.print("• Code auto-uploads on each run (rsync - only changes)")
                console.print(
                    "• Code sync is owned by CLI; provider background uploads are disabled for dev VMs"
                )
                console.print("• VM persists until you --stop")
                console.print("• Default env = your persistent workspace")
                console.print("• Named envs = isolated project spaces\n")
                return

            tokens = list(remote_cmd) if remote_cmd else []
            if tokens and cmd_arg:
                # When both are present, Click assigned the first token to cmd_arg; include it
                tokens = [cmd_arg] + tokens
            command = " ".join(tokens) if tokens else None
            if (
                not command
                and cmd_arg
                and (
                    " " in cmd_arg
                    or cmd_arg.startswith(
                        ("python", "bash", "sh", "./", "nvidia-smi", "pip", "npm", "node")
                    )
                )
            ):
                command = cmd_arg

            self._execute(
                command,
                env,
                instance_type,
                region,
                image,
                ssh_keys,
                reset,
                stop,
                status,
                force_new,
                max_price_per_hour,
                upload,
                upload_path,
                flat,
                no_unique,
                output_json,
            )

        return dev

    def _execute(
        self,
        command: str | None,
        env_name: str,
        instance_type: str | None,
        region: str | None,
        image: str | None,
        ssh_keys: tuple,
        reset: bool,
        stop: bool,
        status: bool,
        force_new: bool,
        max_price_per_hour: float | None,
        upload: bool,
        upload_path: str,
        flat: bool,
        no_unique: bool,
        output_json: bool,
    ) -> None:
        from flow.cli.ui.presentation.animated_progress import AnimatedEllipsisProgress

        progress = None
        printed_existing_msg = False
        if not stop and not status:
            initial_msg = "Starting flow dev"
            if command:
                cmd_preview = command if len(command) <= 30 else command[:27] + "..."
                initial_msg = f"Preparing to run: {cmd_preview}"
            progress = AnimatedEllipsisProgress(
                console, initial_msg, transient=True, start_immediately=True
            )

        try:
            # Lazy import heavy SDK pieces after we start progress so users see immediate feedback
            from flow.sdk.client import Flow as _Flow  # local import
            from flow.sdk.ssh_utils import SSHNotReadyError  # local import

            flow_client = _Flow()
            vm_manager = DevVMManager(flow_client)

            if stop:
                from flow.cli.ui.presentation.animated_progress import (
                    AnimatedEllipsisProgress as _AEP,
                )

                with _AEP(console, "Stopping dev VM", start_immediately=True):
                    if vm_manager.stop_dev_vm():
                        console.print("[success]✓[/success] Dev VM stopped")
                    else:
                        console.print("[warning]No dev VM found[/warning]")
                return

            if status:
                if progress:
                    progress.__exit__(None, None, None)
                self._show_status(vm_manager, flow_client, output_json=output_json)
                return

            # SSH keys preflight: unify with flow ssh behavior via shared helper.
            try:
                from flow.cli.utils.ssh_launch_keys import resolve_launch_ssh_keys as _res_keys
            except Exception:
                # Fallback: treat CLI tuple directly to avoid blocking execution
                _res_keys = None  # type: ignore[assignment]

            effective_keys: list[str] = []
            if _res_keys is not None:
                effective_keys = _res_keys(flow_client, ssh_keys)
            else:
                effective_keys = list(ssh_keys) if ssh_keys else []

            if not effective_keys:
                from flow.cli.utils.ssh_key_messages import print_no_ssh_keys_guidance as _nsk

                _nsk("for dev VM", level="error")
                raise SystemExit(1)
            else:
                from flow.cli.commands.base import console as _console

                with suppress(Exception):
                    keys_preview = ", ".join(effective_keys[:3])
                    if len(effective_keys) > 3:
                        keys_preview += f" (+{len(effective_keys) - 3} more)"
                    _console.print(f"[dim]Using SSH keys:[/dim] {keys_preview}")

            from flow import DEFAULT_ALLOCATION_ESTIMATED_SECONDS
            from flow.cli.utils.step_progress import (
                AllocationProgressAdapter,
                SSHWaitProgressAdapter,
                StepTimeline,
            )

            if progress:
                with suppress(Exception):
                    progress.__exit__(None, None, None)
                progress = None
            timeline = StepTimeline(console, title="flow dev", title_animation="auto")
            timeline.start()
            # Stabilize denominator early to avoid 1/1 → 2/2 → 3/3 jumps.
            # Typical path when creating a new VM: Check → Submit → Allocate → Provision (4 steps).
            # We'll increase this to 4 only in the create-new path below to avoid misleading counts
            # when an existing VM is reused.
            try:
                timeline.reserve_total(3)
            except Exception:
                pass

            # Show an active lookup step while we query the API for an existing VM
            step_idx_lookup = timeline.add_step("Checking for existing dev VM", show_bar=False)
            timeline.start_step(step_idx_lookup)
            vm = vm_manager.find_dev_vm(
                include_not_ready=True, region=region, desired_instance_type=instance_type
            )
            # Mark lookup complete with a brief note for context
            try:
                if vm is None:
                    timeline.complete_step("no VM")
                else:
                    vm_name = getattr(vm, "name", None) or ":dev"
                    if getattr(vm, "ssh_host", None):
                        timeline.complete_step(f"found: {vm_name}")
                    else:
                        timeline.complete_step(f"found: {vm_name} (provisioning)")
            except Exception:
                # UI nicety only – ignore rendering errors
                pass

            # If a different-shape dev VM exists and a specific instance type was requested,
            # note it for messaging and (optionally) stopping when --force-new is set.
            existing_any_vm = None
            if instance_type:
                try:
                    existing_any_vm = vm_manager.find_dev_vm(include_not_ready=True, region=region)
                except Exception:
                    existing_any_vm = None
                if existing_any_vm and not vm:
                    try:
                        existing_type = getattr(existing_any_vm, "instance_type", None)
                        if (
                            existing_type
                            and existing_type.lower().strip() != instance_type.lower().strip()
                        ):
                            console.print(
                                f"Existing dev VM has instance '{existing_type}', requested '{instance_type}'. Creating a new dev VM."
                            )
                    except Exception:
                        pass

            if force_new and (vm or existing_any_vm):
                from flow.cli.ui.presentation.animated_progress import (
                    AnimatedEllipsisProgress as _AEP,
                )

                with _AEP(console, "Force stopping existing dev VM", start_immediately=True):
                    vm_manager.stop_dev_vm()
                    vm = None

            # Wait for provisioning if necessary
            if vm and not vm.ssh_host:
                try:
                    from flow.sdk.ssh_utils import DEFAULT_PROVISION_MINUTES

                    # Quick step to cover endpoint resolution/API refresh which can take a moment
                    step_idx_prepare = timeline.add_step("Preparing SSH endpoint", show_bar=False)
                    timeline.start_step(step_idx_prepare)

                    # Fast-path: refresh single task to populate SSH fields (list() may omit)
                    with suppress(FlowError):
                        vm_ref = flow_client.get_task(vm.task_id)
                        if getattr(vm_ref, "ssh_host", None):
                            vm = vm_ref

                    # Fast-path 2: directly resolve endpoint via provider
                    if not getattr(vm, "ssh_host", None):
                        try:
                            host, port = flow_client.resolve_ssh_endpoint(vm.task_id)
                            if host:
                                vm.ssh_host = host
                                vm.ssh_port = port
                        except (FlowError, AttributeError, ValueError):
                            pass

                    # Close the quick prepare step with a succinct note
                    try:
                        if getattr(vm, "ssh_host", None):
                            timeline.complete_step("resolved")
                        else:
                            timeline.complete_step("waiting")
                    except Exception:
                        pass

                    try:
                        baseline = int(getattr(vm, "instance_age_seconds", 0) or 0)
                    except (TypeError, ValueError):
                        baseline = 0

                    if not getattr(vm, "ssh_host", None):
                        # Use the standard provisioning window (~20m)
                        step_idx_provision = timeline.add_step(
                            f"Provisioning instance (up to {DEFAULT_PROVISION_MINUTES}m)",
                            show_bar=True,
                            estimated_seconds=DEFAULT_PROVISION_MINUTES * 60,
                            baseline_elapsed_seconds=baseline,
                        )
                        ssh_adapter = SSHWaitProgressAdapter(
                            timeline,
                            step_idx_provision,
                            DEFAULT_PROVISION_MINUTES * 60,
                            baseline_elapsed_seconds=baseline,
                        )
                        in_ssh_wait = True
                        with ssh_adapter:
                            from flow.cli.utils.step_progress import (
                                build_provisioning_hint as _bph,
                            )

                            hint = _bph("VM", "flow dev")
                            with suppress(Exception):
                                timeline.set_active_hint_text(hint)
                            if getattr(flow_client.config, "provider", "") == "mock":
                                time.sleep(1.0)
                                vm = flow_client.get_task(vm.task_id)
                            else:
                                try:
                                    vm = flow_client.wait_for_ssh(
                                        task_id=vm.task_id,
                                        timeout=DEFAULT_PROVISION_MINUTES * 60,
                                        show_progress=False,
                                        progress_adapter=ssh_adapter,
                                    )
                                except (SSHNotReadyError, KeyboardInterrupt):
                                    try:
                                        timeline.finish()
                                    except Exception:
                                        pass
                                    console.print("\n[accent]✗ SSH wait interrupted[/accent]")
                                    console.print(
                                        "\nThe dev VM should still be provisioning. You can check later with:"
                                    )
                                    console.print("  [accent]flow dev[/accent]")
                                    console.print(
                                        f"  [accent]flow status {vm.name or vm.task_id}[/accent]"
                                    )
                                    raise SystemExit(1)
                        in_ssh_wait = False
                        # If endpoint is already available at this point, give a tiny nudge of feedback
                        from flow.cli.utils.ssh_helpers import SshStack as _S

                        with suppress(FlowError):
                            ssh_key_path, _err = flow_client.get_task_ssh_connection_info(
                                vm.task_id
                            )
                            if ssh_key_path and getattr(vm, "ssh_host", None):
                                start_wait = time.time()
                                while not _S.is_ssh_ready(
                                    user=getattr(vm, "ssh_user", "ubuntu"),
                                    host=vm.ssh_host,
                                    port=getattr(vm, "ssh_port", 22),
                                    key_path=ssh_key_path,
                                ):
                                    if time.time() - start_wait > 90:
                                        break
                                    with suppress(Exception):  # UI nicety only
                                        ssh_adapter.update_eta()
                                    time.sleep(1)
                    else:
                        # Endpoint is already available; provide a concise confirmation
                        try:
                            vm_name = getattr(vm, "name", None) or ":dev"
                            console.print(f"Using existing dev VM: {vm_name}")
                            printed_existing_msg = True
                        except Exception:
                            pass
                        if progress:
                            progress.update_message(f"Using existing dev VM: {vm.name}")
                            progress.__exit__(None, None, None)
                            progress = None
                except Exception as e:
                    timeline.fail_step(str(e))
                    raise

            if not vm:
                # Dev VM creation proceeds without the global real-provider guard
                # to keep the flow streamlined. The starters command handles
                # user confirmation for billable launches.

                # Show a lightweight spinner while we submit the allocation request.
                # This avoids a perceived "hang" between discovery and allocation steps.
                try:
                    timeline.reserve_total(4)
                except Exception:
                    pass
                step_idx_request = timeline.add_step(
                    "Submitting allocation request", show_bar=False
                )
                timeline.start_step(step_idx_request)
                try:
                    vm = vm_manager.create_dev_vm(
                        instance_type=instance_type,
                        region=region,
                        ssh_keys=effective_keys,
                        max_price_per_hour=max_price_per_hour,
                        no_unique=no_unique,
                    )
                    try:
                        timeline.complete_step("submitted")
                    except Exception:
                        pass
                except Exception as e:
                    # Mark the step as failed with a concise message, then re-raise
                    try:
                        timeline.fail_step(str(e))
                    except Exception:
                        pass
                    raise

                from flow.cli.commands.utils import wait_for_task as _wait_for_task

                step_idx_allocate = timeline.add_step(
                    "Allocating instance",
                    show_bar=True,
                    estimated_seconds=DEFAULT_ALLOCATION_ESTIMATED_SECONDS,
                )
                alloc_adapter = AllocationProgressAdapter(
                    timeline,
                    step_idx_allocate,
                    estimated_seconds=DEFAULT_ALLOCATION_ESTIMATED_SECONDS,
                )
                with alloc_adapter:
                    # Provide a standardized allocation hint
                    try:
                        from flow.cli.utils.step_progress import (
                            build_allocation_hint as _bah,
                        )

                        timeline.set_active_hint_text(_bah("flow dev", subject="allocation"))
                    except Exception:
                        pass
                    final_status = _wait_for_task(
                        flow_client,
                        vm.task_id,
                        watch=False,
                        task_name=vm.name,
                        show_submission_message=False,
                        progress_adapter=alloc_adapter,
                    )
                if final_status != "running":
                    try:
                        task = flow_client.get_task(vm.task_id)
                        msg = getattr(task, "message", None) or f"status: {final_status}"
                        timeline.steps[step_idx_allocate].note = msg
                    except Exception:
                        pass
                    timeline.fail_step("Allocation did not reach running state")

                    # Surface the error to the user before cancelling
                    error_details = f"Dev VM allocation failed with status: {final_status}"
                    try:
                        task = flow_client.get_task(vm.task_id)
                        if hasattr(task, "message") and task.message:
                            error_details = f"{error_details}\nDetails: {task.message}"
                    except Exception:
                        pass

                    # Only cancel if the task is truly stuck/failed (not just pending)
                    # Pending tasks may still be waiting for capacity
                    if final_status not in ["pending", "preparing"]:
                        try:
                            console.print(f"[warning]{error_details}[/warning]")
                            console.print("[dim]Cancelling failed allocation...[/dim]")
                            flow_client.cancel(vm.task_id)
                        except Exception as cancel_err:
                            console.print(f"[dim]Note: Failed to cancel task: {cancel_err}[/dim]")
                    else:
                        # Task is still pending - don't cancel, just inform user
                        console.print(f"[warning]{error_details}[/warning]")
                        console.print(
                            f"\n[accent]The dev VM ({vm.name or vm.task_id}) is still pending allocation.[/accent]"
                        )
                        console.print("You can check status with:")
                        console.print(f"  [accent]flow status {vm.name or vm.task_id}[/accent]")
                        console.print("Or cancel it with:")
                        console.print(f"  [accent]flow cancel {vm.name or vm.task_id}[/accent]")
                    return

                from flow.sdk.ssh_utils import DEFAULT_PROVISION_MINUTES

                baseline = 0
                try:
                    baseline = int(getattr(vm, "instance_age_seconds", None) or 0)
                except Exception:
                    baseline = 0
                # Use the standard provisioning window (~20m)
                step_idx_provision = timeline.add_step(
                    f"Provisioning instance (up to {DEFAULT_PROVISION_MINUTES}m)",
                    show_bar=True,
                    estimated_seconds=DEFAULT_PROVISION_MINUTES * 60,
                    baseline_elapsed_seconds=baseline,
                )
                ssh_adapter = SSHWaitProgressAdapter(
                    timeline,
                    step_idx_provision,
                    DEFAULT_PROVISION_MINUTES * 60,
                    baseline_elapsed_seconds=baseline,
                )
                in_ssh_wait = True
                with ssh_adapter:
                    try:
                        from flow.cli.utils.step_progress import (
                            build_provisioning_hint as _bph,
                        )

                        timeline.set_active_hint_text(_bph("VM", "flow dev"))
                    except Exception:
                        pass
                    if getattr(flow_client.config, "provider", "") == "mock":
                        time.sleep(1.0)
                        vm = flow_client.get_task(vm.task_id)
                    else:
                        try:
                            vm = flow_client.wait_for_ssh(
                                task_id=vm.task_id,
                                timeout=DEFAULT_PROVISION_MINUTES * 60,
                                show_progress=False,
                                progress_adapter=ssh_adapter,
                            )
                        except (SSHNotReadyError, KeyboardInterrupt):
                            try:
                                timeline.finish()
                            except Exception:
                                pass
                            console.print("\n[accent]✗ SSH wait interrupted[/accent]")
                            console.print(
                                "\nThe dev VM should still be provisioning. You can check later with:"
                            )
                            console.print("  [accent]flow dev[/accent]")
                            console.print(f"  [accent]flow status {vm.name or vm.task_id}[/accent]")
                            raise SystemExit(1)
                    # Keep the provisioning step active until an initial SSH handshake succeeds
                    # to avoid advancing to code-sync while the host isn't actually reachable yet.
                    try:
                        from flow.cli.utils.ssh_helpers import SshStack as _S

                        ssh_key_path, _err = flow_client.get_task_ssh_connection_info(vm.task_id)
                        if ssh_key_path and getattr(vm, "ssh_host", None):
                            start_wait = time.time()
                            # Bound the stabilization window to avoid masking truly slow boots
                            max_wait = 120  # seconds
                            while not _S.is_ssh_ready(
                                user=getattr(vm, "ssh_user", "ubuntu"),
                                host=vm.ssh_host,
                                port=getattr(vm, "ssh_port", 22),
                                key_path=ssh_key_path,
                            ):
                                if time.time() - start_wait > max_wait:
                                    break
                                try:
                                    ssh_adapter.update_eta()
                                except Exception:
                                    pass
                                time.sleep(1)
                    except Exception:
                        # Best-effort stabilization only; don't fail provisioning step here
                        pass
                in_ssh_wait = False
            else:
                if progress:
                    progress.update_message(f"Using existing dev VM: {vm.name}")
                    with suppress(Exception):
                        progress.__exit__(None, None, None)
                    progress = None
                # Avoid duplicate prints if we already confirmed earlier
                if not printed_existing_msg:
                    console.print(f"Using existing dev VM: {vm.name}")

            # Normalize env name early to avoid leaky path formation and double slashes
            sanitized_env = sanitize_env_name(env_name)

            # Upload code
            workdir_for_command: str | None = None
            if upload:
                upload_manager = DevUploadManager(
                    flow_client, vm, timeline, upload_mode=("flat" if flat else "nested")
                )
                # If the VM already has ssh_host, perform a brief readiness check here to
                # compute ProxyJump (if needed) and avoid rsync hangs.
                try:
                    if getattr(vm, "ssh_host", None):
                        step_idx_prepare = timeline.add_step(
                            "Preparing SSH endpoint", show_bar=False
                        )
                        timeline.start_step(step_idx_prepare)
                        # Force a short readiness check via provider SSH waiter
                        try:
                            provider = flow_client.get_remote_operations().provider  # type: ignore[attr-defined]
                            from flow.adapters.transport.ssh import (
                                ExponentialBackoffSSHWaiter as _W,
                            )

                            waiter = _W(provider)
                            # Attach the latest task view to reflect any endpoint changes
                            vm = provider.get_task(vm.task_id)
                            # Use a short timeout to avoid adding long delays in the common ready path
                            waiter.wait_for_ssh(vm, timeout=30)
                        except Exception:
                            # Best-effort: even if the probe fails, proceed; the upload step will present errors
                            pass
                        timeline.complete_step(note="resolved")
                except Exception:
                    # Do not block uploads on preflight UX issues
                    pass

                vm_dir, container_dir = upload_manager.upload(upload_path, sanitized_env)
                workdir_for_command = container_dir if sanitized_env != "default" else vm_dir

            executor = DevContainerExecutor(flow_client, vm)

            if reset:
                from flow.cli.ui.presentation.animated_progress import (
                    AnimatedEllipsisProgress as _AEP,
                )

                with _AEP(console, "Resetting all dev containers", start_immediately=True):
                    executor.reset_containers()
                console.print("[bold green]✓[/bold green] Containers reset successfully")
                return

            if command:
                interactive_commands = [
                    "bash",
                    "sh",
                    "zsh",
                    "fish",
                    "python",
                    "ipython",
                    "irb",
                    "node",
                ]
                original_command = command
                is_interactive = original_command.strip() in interactive_commands
                # If we performed an upload and resolved a working directory, run the command from there
                if workdir_for_command:
                    # Use $HOME for any leading '~' so expansion still occurs when quoted
                    wd = workdir_for_command
                    if wd == "~":
                        wd_expr = '"$HOME"'
                    elif wd.startswith("~/"):
                        # Preserve the remainder and allow HOME expansion; quote for spaces
                        remainder = wd[2:]
                        # Double-quote the argument so spaces are safe
                        wd_expr = '"$HOME/' + remainder.replace('"', '\\"') + '"'
                    else:
                        # Safe path without HOME expansion
                        wd_expr = shlex.quote(wd)
                    command = f"cd {wd_expr} && {original_command}"
                else:
                    command = original_command

                if progress:
                    progress.update_message("Preparing container environment")
                    time.sleep(0.3)
                    progress.__exit__(None, None, None)
                    progress = None

                # Close the step timeline before attaching or running commands to avoid UI overlap
                with suppress(Exception):
                    timeline.finish()

                if is_interactive:
                    console.print(f"Starting interactive session: {original_command}")
                else:
                    console.print(f"Executing: {original_command}")

                exit_code = executor.execute_command(
                    command, image=image, interactive=is_interactive, env_name=sanitized_env
                )

                if exit_code != 0 and not is_interactive:
                    raise SystemExit(exit_code)
            else:
                if sanitized_env != "default":
                    console.print(f"[dim]Connecting to environment '{sanitized_env}'[/dim]")
                else:
                    console.print(
                        "[dim]Once connected, you'll have a persistent Ubuntu environment[/dim]"
                    )

                if sanitized_env != "default":
                    env_dir = f"/envs/{sanitized_env}"
                    with suppress(Exception):
                        remote_ops = flow_client.get_remote_operations()
                        setup_cmd = f"mkdir -p {env_dir}"
                        remote_ops.execute_command(vm.task_id, setup_cmd)

                with suppress(Exception):
                    timeline.finish()

                shell_cmd = None
                if sanitized_env != "default":
                    shell_cmd = f'bash -lc "mkdir -p /envs/{sanitized_env} && cd /envs/{sanitized_env} && exec bash -l"'
                else:
                    # If we uploaded code and resolved a working directory, start the shell there
                    try:
                        if upload and "vm_dir" in locals() and vm_dir:
                            # Build a robust cd target: convert leading '~' to $HOME and quote for spaces
                            wd = vm_dir
                            if wd == "~":
                                path_expr = "$HOME"
                            elif wd.startswith("~/"):
                                path_expr = "$HOME/" + wd[2:].replace('"', '\\"')
                            else:
                                path_expr = wd.replace('"', '\\"')
                            # Wrap the path in double-quotes inside the bash -lc string (escape quotes)
                            shell_cmd = f'bash -lc "cd "{path_expr}" && exec bash -l"'
                    except Exception:
                        pass

                # Use provider remote operations directly to avoid relying on Task._provider
                try:
                    remote_ops = flow_client.get_remote_operations()
                except NotImplementedError:
                    remote_ops = None
                if not remote_ops:
                    from flow.errors import FlowError as _FlowError

                    raise _FlowError(
                        "Provider does not support shell access",
                        suggestions=[
                            "This provider does not support remote shell access",
                            "Use a provider that implements remote operations",
                            "Check provider documentation for supported features",
                        ],
                    )

                remote_ops.open_shell(
                    vm.task_id, command=shell_cmd, node=None, progress_context=None, record=False
                )

            # Next actions hints
            if not command or command in [
                "bash",
                "sh",
                "zsh",
                "fish",
                "python",
                "ipython",
                "irb",
                "node",
            ]:
                if env_name == "default":
                    self.show_next_actions(
                        [
                            "Run a command on your VM: [accent]flow dev 'python <your_script>.py'[/accent]",
                            "Create an isolated env: [accent]flow dev 'pip install <deps>' -e <env-name>[/accent]",
                            "Check dev VM status: [accent]flow status :dev[/accent]",
                        ]
                    )
                else:
                    self.show_next_actions(
                        [
                            f"Work in {env_name}: [accent]flow dev 'python <your_script>.py' -e {env_name}[/accent]",
                            "Switch to default: [accent]flow dev 'python <your_script>.py'[/accent]",
                            "List environments: [accent]ls /envs/[/accent]",
                        ]
                    )

        except AuthenticationError:
            self.handle_auth_error()
        except TaskNotFoundError as e:
            self.handle_error(f"Dev VM not found: {e}")
        except ValidationError as e:
            self.handle_error(f"Invalid configuration: {e}")
        except KeyboardInterrupt:
            # If interrupted while waiting for SSH, show context-aware hint
            with suppress(Exception):
                in_ssh_wait = bool(locals().get("in_ssh_wait"))
            in_wait = bool(locals().get("in_ssh_wait", False))
            if in_wait:
                with suppress(Exception):
                    if "timeline" in locals():
                        timeline.finish()
                console.print("\n[accent]✗ SSH wait interrupted[/accent]")
                console.print(
                    "\nThe dev VM should still be provisioning. You can check later with:"
                )
                with suppress(Exception):
                    vm_name = (vm.name if "vm" in locals() and vm else None) or ":dev"
                vm_name = locals().get("vm_name", ":dev")
                console.print("  [accent]flow dev[/accent]")
                console.print(f"  [accent]flow status {vm_name}[/accent]")
            else:
                console.print("\n[warning]Operation cancelled by user[/warning]")
            raise SystemExit(1)
        except Exception as e:
            error_msg = str(e)
            if "connection refused" in error_msg.lower():
                self.handle_error(
                    "Cannot connect to Docker daemon. Ensure Docker is installed and running on the dev VM.\n"
                    "You may need to SSH into the VM and install Docker: [accent]flow dev[/accent]"
                )
            elif "no such image" in error_msg.lower():
                self.handle_error(
                    f"Docker image not found: {image or 'default'}\n"
                    "The image will be pulled automatically on first use."
                )
            else:
                self.handle_error(str(e))
        finally:
            with suppress(Exception):
                if "timeline" in locals():
                    timeline.finish()

    def _show_status(
        self, vm_manager: DevVMManager, flow_client: Flow, output_json: bool = False
    ) -> None:
        vm = vm_manager.find_dev_vm()

        if not vm:
            if output_json:
                import json as _json

                console.print(_json.dumps({"schema_version": "1.0", "dev_vm": None}))
                return
            console.print("[warning]No dev VM available[/warning]")
            console.print("\nStart a dev VM with: [accent]flow dev[/accent]")
            return

        if output_json:
            import json as _json

            status_value = getattr(vm.status, "value", str(vm.status))
            payload = {
                "schema_version": "1.0",
                "dev_vm": {
                    "task_id": vm.task_id,
                    "name": vm.name,
                    "status": str(status_value).lower(),
                    "instance_type": vm.instance_type,
                    "ssh_host": vm.ssh_host,
                    "ssh_port": getattr(vm, "ssh_port", 22),
                    "started_at": vm.started_at.isoformat() if vm.started_at else None,
                },
            }
            try:
                executor = DevContainerExecutor(flow_client, vm)
                container_status = executor.get_container_status()
                payload["containers"] = container_status
            except Exception:
                payload["containers"] = {"active_containers": 0, "containers": []}
            console.print(_json.dumps(payload))
            return

        console.print("\n[bold]Dev VM Status[/bold]")
        console.print(f"Name: [accent]{vm.name}[/accent]")
        console.print(f"ID: [dim]{vm.task_id}[/dim]")
        from flow.cli.ui.formatters import TaskFormatter

        display_status = TaskFormatter.get_display_status(vm)
        status_text = TaskFormatter().format_status_with_color(display_status)
        console.print(f"Status: {status_text}")
        console.print(f"Instance: {vm.instance_type}")

        if vm.started_at:
            from datetime import datetime, timezone

            uptime = datetime.now(timezone.utc) - vm.started_at
            hours = int(uptime.total_seconds() // 3600)
            minutes = int((uptime.total_seconds() % 3600) // 60)
            console.print(f"Uptime: {hours}h {minutes}m")

        try:
            executor = DevContainerExecutor(flow_client, vm)
            container_status = executor.get_container_status()
            console.print("\n[bold]Containers[/bold]")
            console.print(f"Active: {container_status['active_containers']}")
            if container_status["containers"]:
                console.print("\nRunning containers:")
                for container in container_status["containers"]:
                    console.print(
                        f"  - {container.get('Names', 'unknown')} ({container.get('Status', 'unknown')})"
                    )
        except Exception:
            console.print("\n[dim]Unable to fetch container status[/dim]")


# Export command instance
command = DevCommand()
