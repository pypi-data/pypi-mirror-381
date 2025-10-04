"""CLI controller extracted from package init to keep files small.

Provides the PromptCLI class used by console entrypoints.
"""
from __future__ import annotations

import argparse
import json
import logging
import os
import platform
import sys
from pathlib import Path
from typing import Any
from dataclasses import dataclass


from ..config import HOME_DIR, LOG_DIR
from .. import background_hotkey, logger, paste, update as manifest_update, updater
from ..features import (
    is_background_hotkey_enabled,
    is_mcp_enabled,
)
from ..menus import (
    ensure_unique_ids,
    list_styles,
    list_prompts,
    load_template,
    PROMPTS_DIR,
)
from ..variables import (
    reset_file_overrides,
    reset_single_file_override,
    list_file_overrides,
    storage,
)
from ..launchers import maybe_handoff_to_preferred_installation

try:  # Optional background hotkey service
    from ..services import global_shortcut_service  # type: ignore
except Exception:  # pragma: no cover - service unavailable
    global_shortcut_service = None

from .dependencies import check_dependencies, dependency_status
from .template_select import select_template_cli, pick_prompt_cli
from .render import render_template_cli
from ..gui.file_append import _append_to_files
from .update import perform_update


@dataclass
class UninstallOptions:
    """Options controlling the uninstall routine."""

    all: bool = False
    dry_run: bool = False
    force: bool = False
    purge_data: bool = False
    keep_user_data: bool = False
    no_backup: bool = False
    non_interactive: bool = False
    verbose: bool = False
    json: bool = False
    platform: str | None = None
    remove_orphans: bool = False
    confirm_orphans: bool = False
    print_elevated_script: bool = False


class PromptCLI:
    """High level command line interface controller."""

    def __init__(self) -> None:
        self.log_dir = LOG_DIR
        try:
            self.log_dir.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass
        self.log_file = self.log_dir / "cli.log"
        self._log = logging.getLogger("prompt_automation.cli")
        if not self._log.handlers:
            # Elevate to DEBUG when troubleshooting is enabled via env var
            level = logging.DEBUG if os.environ.get("PROMPT_AUTOMATION_DEBUG") else logging.INFO
            self._log.setLevel(level)
            try:
                self._log.addHandler(logging.FileHandler(self.log_file))
            except Exception:
                self._log.addHandler(logging.StreamHandler())

    # Expose helper functions as methods for convenience
    check_dependencies = staticmethod(check_dependencies)
    dependency_status = staticmethod(dependency_status)
    select_template_cli = staticmethod(select_template_cli)
    pick_prompt_cli = staticmethod(pick_prompt_cli)
    render_template_cli = staticmethod(render_template_cli)
    _append_to_files = staticmethod(_append_to_files)

    def _render_template_by_id(self, args: argparse.Namespace) -> int:
        """Render a template by ID with variable substitution (for workflow automation)."""
        from ..renderer import load_template
        from ..menus import render_template
        
        # Find template by ID
        template_id = args.template
        template_file = None
        
        for style in list_styles():
            for tmpl_path in list_prompts(style):
                try:
                    tmpl_data = load_template(tmpl_path)
                    if tmpl_data.get("id") == template_id:
                        template_file = tmpl_path
                        break
                except Exception:
                    continue
            if template_file:
                break
        
        if not template_file:
            print(f"Error: Template with ID {template_id} not found", file=sys.stderr)
            return 1
        
        # Load template
        try:
            tmpl_data = load_template(template_file)
        except Exception as e:
            print(f"Error loading template {template_id}: {e}", file=sys.stderr)
            return 1
        
        # Parse variables from --var flags
        variables = {}
        if args.var:
            for var_str in args.var:
                if "=" not in var_str:
                    print(f"Error: Invalid variable format '{var_str}' (expected key=value)", file=sys.stderr)
                    return 1
                key, value = var_str.split("=", 1)
                variables[key.strip()] = value
        
        # Render template with variables
        try:
            result = render_template(tmpl_data, values=variables)
            # render_template can return str or tuple[str, dict]
            if isinstance(result, tuple):
                rendered_text = result[0]
            else:
                rendered_text = result
        except Exception as e:
            print(f"Error rendering template: {e}", file=sys.stderr)
            return 1
        
        # Output based on --output flag
        if args.output == "stdout":
            # Handle Unicode output properly for Windows console
            try:
                print(rendered_text)
            except UnicodeEncodeError:
                # Fallback: encode to ASCII with xmlcharrefreplace for Windows console
                print(rendered_text.encode(sys.stdout.encoding or 'utf-8', errors='xmlcharrefreplace').decode(sys.stdout.encoding or 'utf-8'))
        elif args.output == "clipboard":
            try:
                paste.copy_to_clipboard(rendered_text)
                print(f"✅ Template {template_id} rendered and copied to clipboard", file=sys.stderr)
            except Exception as e:
                print(f"Error copying to clipboard: {e}", file=sys.stderr)
                print("\n--- Output ---", file=sys.stderr)
                print(rendered_text)
                return 1
        elif args.output == "file":
            import time
            # Write to ~/.prompt-automation/workflow-renders/ to avoid cluttering root
            render_dir = Path.home() / ".prompt-automation" / "workflow-renders"
            render_dir.mkdir(parents=True, exist_ok=True)
            filename = render_dir / f"rendered_{template_id}_{int(time.time())}.md"
            try:
                filename.write_text(rendered_text, encoding="utf-8")
                print(f"✅ Template {template_id} rendered and saved to: {filename}", file=sys.stderr)
            except Exception as e:
                print(f"Error writing to file: {e}", file=sys.stderr)
                return 1
        
        return 0

    def _maybe_register_background_hotkey(self) -> None:
        """Best-effort background hotkey registration."""
        if not global_shortcut_service:
            return
        if not getattr(global_shortcut_service, "available", True):
            try:
                self._log.warning("global_shortcut_service_unavailable")
            except Exception:
                pass
            return
        try:
            if not storage.get_background_hotkey_enabled():
                return
            if not is_background_hotkey_enabled():
                try:
                    self._log.warning("background_hotkey_env_disabled")
                except Exception:
                    pass
                return
            payload = storage._load_settings_payload()
            settings = payload.get("background_hotkey") or {}
            settings["espanso_enabled"] = storage.get_espanso_enabled()
            background_hotkey.ensure_registered(settings, global_shortcut_service)

            def _toggle_bg_hotkey(enabled: bool) -> None:
                if not global_shortcut_service:
                    return
                try:
                    if enabled:
                        if is_background_hotkey_enabled():
                            payload = storage._load_settings_payload()
                            s = payload.get("background_hotkey") or {}
                            s["espanso_enabled"] = storage.get_espanso_enabled()
                            background_hotkey.ensure_registered(s, global_shortcut_service)
                        else:
                            try:
                                self._log.warning("background_hotkey_env_disabled")
                            except Exception:
                                pass
                            background_hotkey.unregister(global_shortcut_service)
                    else:
                        background_hotkey.unregister(global_shortcut_service)
                except Exception as exc:
                    try:
                        self._log.error("background_hotkey_toggle_failed error=%s", exc)
                    except Exception:
                        pass

            def _toggle_espanso(enabled: bool) -> None:
                if not global_shortcut_service:
                    return
                try:
                    if storage.get_background_hotkey_enabled():
                        if is_background_hotkey_enabled():
                            payload = storage._load_settings_payload()
                            s = payload.get("background_hotkey") or {}
                            s["espanso_enabled"] = enabled
                            background_hotkey.ensure_registered(s, global_shortcut_service)
                        else:
                            try:
                                self._log.warning("background_hotkey_env_disabled")
                            except Exception:
                                pass
                            background_hotkey.unregister(global_shortcut_service)
                    else:
                        background_hotkey.unregister(global_shortcut_service)
                except Exception as exc:
                    try:
                        self._log.error("espanso_toggle_failed error=%s", exc)
                    except Exception:
                        pass

            storage.add_boolean_setting_observer(
                "background_hotkey_enabled", _toggle_bg_hotkey
            )
            storage.add_boolean_setting_observer("espanso_enabled", _toggle_espanso)
        except Exception as e:
            try:
                self._log.error("background_hotkey_init_failed error=%s", e)
            except Exception:
                pass

    def _run_mcp_command(self, args: argparse.Namespace) -> int:
        """Execute MCP debug sub-commands."""

        from ..mcp import client as mcp_client

        command = getattr(args, "mcp_command", None)
        try:
            if command == "registry":
                path = args.path.expanduser().resolve()
                registry = mcp_client.load_registry_cached(path)
                payload = {
                    "path": str(path),
                    "providers": [mcp_client.provider_to_dict(provider) for provider in registry.providers],
                }
                print(json.dumps(payload, indent=2, sort_keys=True))
                return 0
            if command == "credentials":
                path = args.path.expanduser().resolve()
                data = mcp_client.load_credentials_cached(path)
                payload = {
                    "path": str(path),
                    "credentials": data,
                }
                print(json.dumps(payload, indent=2, sort_keys=True))
                return 0
            if command == "discover":
                accepted = list(args.accept or ())
                registry_path = args.registry.expanduser().resolve()
                credentials_path = args.credentials.expanduser().resolve() if args.credentials else None
                discovery = mcp_client.discover_provider(
                    args.provider,
                    registry_path=registry_path,
                    credentials_path=credentials_path,
                    accepted=accepted,
                    refresh=getattr(args, "refresh", False),
                )
                payload = {
                    "provider": args.provider,
                    "discovery": mcp_client.discovery_to_dict(discovery),
                }
                print(json.dumps(payload, indent=2, sort_keys=True))
                return 0
            if command == "call":
                accepted = list(args.accept or ())
                registry_path = args.registry.expanduser().resolve()
                credentials_path = args.credentials.expanduser().resolve() if args.credentials else None
                try:
                    arguments = json.loads(args.arguments) if args.arguments else {}
                except json.JSONDecodeError as exc:
                    print(json.dumps({"error": f"invalid JSON for --arguments: {exc}"}, sort_keys=True))
                    return 1
                if not isinstance(arguments, dict):
                    print(json.dumps({"error": "--arguments must be a JSON object"}, sort_keys=True))
                    return 1
                result = mcp_client.call_tool(
                    args.provider,
                    args.tool,
                    arguments,
                    registry_path=registry_path,
                    credentials_path=credentials_path,
                    accepted=accepted,
                )
                payload = {
                    "provider": args.provider,
                    "tool": args.tool,
                    "result": result,
                }
                print(json.dumps(payload, indent=2, sort_keys=True))
                return 0
            raise ValueError(f"unknown mcp command: {command}")
        except Exception as exc:  # pragma: no cover - defensive
            print(json.dumps({"error": str(exc)}, sort_keys=True))
            return 1

    def main(self, argv: list[str] | None = None) -> None:
        """Program entry point."""
        args_list = list(argv or sys.argv[1:])
        if platform.system() == "Windows":
            result = maybe_handoff_to_preferred_installation(
                argv=args_list,
                current_executable=Path(sys.argv[0]),
            )
            if result is not None:
                raise SystemExit(result)

        # Load environment from config file if it exists
        config_dir = HOME_DIR
        env_file = config_dir / "environment"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if "=" in line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    os.environ.setdefault(key.strip(), value.strip())

        parser = argparse.ArgumentParser(prog="prompt-automation")
        parser.add_argument(
            "--troubleshoot", action="store_true", help="Show troubleshooting help and paths"
        )
        parser.add_argument(
            "--version", action="store_true", help="Print version and exit"
        )
        parser.add_argument(
            "--prompt-dir", type=Path, help="Directory containing prompt templates"
        )
        parser.add_argument(
            "--list", action="store_true", help="List available prompt styles and templates"
        )
        parser.add_argument(
            "--tree",
            action="store_true",
            help="Render hierarchical tree when used with --list (opt-in)",
        )
        parser.add_argument(
            "--flat",
            action="store_true",
            help="Force flat listing (overrides feature flag)",
        )
        parser.add_argument(
            "--filter",
            type=str,
            metavar="PATTERN",
            help="Filter templates/folders by case-insensitive substring",
        )
        parser.add_argument(
            "--reset-log", action="store_true", help="Clear usage log database"
        )
        parser.add_argument(
            "--reset-file-overrides",
            action="store_true",
            help="Clear stored reference file paths & skip flags",
        )
        parser.add_argument(
            "--reset-one-override",
            nargs=2,
            metavar=("TEMPLATE_ID", "NAME"),
            help="Reset a single placeholder override",
        )
        parser.add_argument(
            "--list-overrides", action="store_true", help="List current file/skip overrides"
        )
        parser.add_argument("--gui", action="store_true", help="Launch GUI (default)")
        parser.add_argument(
            "--terminal", action="store_true", help="Force terminal mode instead of GUI"
        )
        parser.add_argument(
            "--focus", action="store_true", help="Focus existing GUI instance if running (no new window)"
        )
        parser.add_argument(
            "--update", "-u", action="store_true", help="Check for and apply updates"
        )
        parser.add_argument(
            "--self-test",
            action="store_true",
            help="Run dependency and template health checks and exit",
        )
        parser.add_argument(
            "--espanso-sync",
            action="store_true",
            help="Validate, mirror, and update the espanso package, then restart",
        )
        parser.add_argument(
            "--espanso-skip-install",
            action="store_true",
            help="Skip espanso install/update (validate+mirror only)",
        )
        parser.add_argument(
            "--espanso-auto-bump",
            choices=("off", "patch"),
            default=None,
            help="Auto-bump patch version before mirroring",
        )
        parser.add_argument(
            "--espanso-clean",
            action="store_true",
            help="Backup and remove local espanso match files and uninstall legacy/conflicting packages",
        )
        parser.add_argument(
            "--espanso-clean-deep",
            action="store_true",
            help="Deep clean: backup and remove ALL local match/*.yml (not just base.yml)",
        )
        parser.add_argument(
            "--espanso-no-sync",
            action="store_true",
            help="When used with --espanso-clean-deep, skip the automatic sync step",
        )
        parser.add_argument(
            "--espanso-clean-list",
            action="store_true",
            help="List local match files and installed packages (no changes)",
        )
        parser.add_argument(
            "--espanso-reset",
            action="store_true",
            help="One-shot: deep clean local matches + uninstall legacy packages, then sync",
        )
        parser.add_argument(
            "--assign-hotkey",
            action="store_true",
            help="Interactively set or change the global GUI hotkey",
        )
        parser.add_argument(
            "--hotkey-status",
            action="store_true",
            help="Show current hotkey and platform integration status",
        )
        parser.add_argument(
            "--hotkey-repair",
            action="store_true",
            help="Re-write hotkey integration files and verify (safe)",
        )
        parser.add_argument(
            "--enable-background-hotkey",
            action="store_true",
            help="Enable background hotkey integration and persist",
        )
        parser.add_argument(
            "--disable-background-hotkey",
            action="store_true",
            help="Disable background hotkey integration and persist",
        )
        parser.add_argument(
            "--enable-espanso",
            action="store_true",
            help="Enable espanso integration for background hotkey and persist",
        )
        parser.add_argument(
            "--disable-espanso",
            action="store_true",
            help="Disable espanso integration for background hotkey and persist",
        )
        parser.add_argument(
            "--theme",
            choices=["light", "dark", "system"],
            help="Override theme for this run (does not persist)",
        )
        parser.add_argument(
            "--persist-theme",
            action="store_true",
            help="Persist the provided --theme value to settings.json",
        )
        parser.add_argument(
            "--hierarchy",
            choices=["on", "off"],
            help="Enable or disable hierarchical templates for this run (mimics theme toggle)",
        )
        parser.add_argument(
            "--persist-hierarchy",
            action="store_true",
            help="Persist the provided --hierarchy value to settings.json",
        )
        parser.add_argument(
            "--show-reminders",
            action="store_true",
            help="Print reminders for a selected template and exit (no prompting)",
        )
        parser.add_argument(
            "--template",
            type=int,
            metavar="ID",
            help="Render template by ID (e.g., --template 13023)",
        )
        parser.add_argument(
            "--var",
            action="append",
            metavar="KEY=VALUE",
            help="Set template variable (format: key=value, can be used multiple times)",
        )
        parser.add_argument(
            "--output",
            choices=["clipboard", "stdout", "file"],
            default="clipboard",
            help="Output destination (default: clipboard)",
        )
        sub = parser.add_subparsers(dest="command")
        if is_mcp_enabled():
            mcp_parser = sub.add_parser(
                "mcp",
                help="Debug Model Context Protocol providers",
                description=(
                    "Inspect registry metadata and interact with providers using the "
                    "Model Context Protocol."
                ),
            )
            mcp_sub = mcp_parser.add_subparsers(dest="mcp_command", required=True)
            registry_cmd = mcp_sub.add_parser(
                "registry", help="Show the configured MCP providers from a registry file"
            )
            registry_cmd.add_argument(
                "--path",
                required=True,
                type=Path,
                help="Path to an MCP registry JSON file",
            )
            credentials_cmd = mcp_sub.add_parser(
                "credentials", help="Show credentials loaded for MCP providers"
            )
            credentials_cmd.add_argument(
                "--path",
                required=True,
                type=Path,
                help="Path to an MCP credentials JSON file",
            )
            discover_cmd = mcp_sub.add_parser(
                "discover", help="Initialize a provider and emit discovery metadata"
            )
            discover_cmd.add_argument("provider", help="Provider identifier to initialize")
            discover_cmd.add_argument(
                "--registry",
                required=True,
                type=Path,
                help="Path to an MCP registry JSON file",
            )
            discover_cmd.add_argument(
                "--credentials",
                type=Path,
                help="Path to an MCP credentials JSON file",
            )
            discover_cmd.add_argument(
                "--accept",
                nargs="*",
                default=(),
                help="Provider identifiers that already have recorded consent",
            )
            discover_cmd.add_argument(
                "--refresh",
                action="store_true",
                help="Bypass cached discovery metadata",
            )
            call_cmd = mcp_sub.add_parser(
                "call", help="Invoke a specific tool exposed by an MCP provider"
            )
            call_cmd.add_argument("provider", help="Provider identifier to use")
            call_cmd.add_argument("tool", help="Tool name to invoke")
            call_cmd.add_argument(
                "--registry",
                required=True,
                type=Path,
                help="Path to an MCP registry JSON file",
            )
            call_cmd.add_argument(
                "--credentials",
                type=Path,
                help="Path to an MCP credentials JSON file",
            )
            call_cmd.add_argument(
                "--accept",
                nargs="*",
                default=(),
                help="Provider identifiers that already have recorded consent",
            )
            call_cmd.add_argument(
                "--arguments",
                type=str,
                default="{}",
                help="JSON object containing tool arguments",
            )
        uninstall = sub.add_parser(
            "uninstall",
            aliases=["remove"],
            help="Uninstall Prompt Automation",
            description=(
                "Remove the application and optional user data. "
                "Requires UNINSTALL_FEATURE_FLAG=1. "
                "Exit codes: 0 success, 1 invalid options, 2 removal failure."
            ),
        )
        uninstall.add_argument("--all", action="store_true", help="Remove all components")
        uninstall.add_argument("--dry-run", action="store_true", help="Preview actions without executing")
        uninstall.add_argument("--force", action="store_true", help="Force removal even if in use")
        uninstall.add_argument("--purge-data", action="store_true", help="Delete all associated data")
        uninstall.add_argument("--keep-user-data", action="store_true", help="Preserve user data only")
        uninstall.add_argument("--no-backup", action="store_true", help="Do not create data backups")
        uninstall.add_argument("--non-interactive", action="store_true", help="Run without prompts")
        uninstall.add_argument("--verbose", action="store_true", help="Increase output verbosity")
        uninstall.add_argument("--json", action="store_true", help="Emit JSON output")
        uninstall.add_argument("--platform", help="Target platform override")
        uninstall.add_argument(
            "--print-elevated-script",
            action="store_true",
            help="Emit a script to remove artifacts requiring elevated privileges",
        )
        uninstall.add_argument(
            "--remove-orphans",
            action="store_true",
            help="Remove orphan prompt-automation executables",
        )
        uninstall.add_argument(
            "--confirm-orphans",
            action="store_true",
            help="Prompt before removing orphan executables",
        )
        args = parser.parse_args(args_list)
        if args.command == "mcp":
            return self._run_mcp_command(args)
        # Register background hotkey if configured
        self._maybe_register_background_hotkey()

        if args.enable_background_hotkey:
            storage.set_background_hotkey_enabled(True)
        if args.disable_background_hotkey:
            storage.set_background_hotkey_enabled(False)
        if args.enable_espanso:
            storage.set_espanso_enabled(True)
        if args.disable_espanso:
            storage.set_espanso_enabled(False)

        if args.command == "uninstall":
            if os.environ.get("UNINSTALL_FEATURE_FLAG", "1") == "0":
                print("[prompt-automation] Uninstall feature disabled. Set UNINSTALL_FEATURE_FLAG=1 to enable.")
                return 1
            from ..uninstall import run_uninstall

            options = UninstallOptions(
                all=args.all,
                dry_run=args.dry_run,
                force=args.force,
                purge_data=args.purge_data,
                keep_user_data=args.keep_user_data,
                no_backup=args.no_backup,
                non_interactive=args.non_interactive,
                verbose=args.verbose,
                json=args.json,
                platform=args.platform,
                remove_orphans=args.remove_orphans,
                confirm_orphans=args.confirm_orphans,
                print_elevated_script=args.print_elevated_script,
            )
            return run_uninstall(options)

        if args.version:
            try:
                from importlib.metadata import version as _dist_version
                print(f"prompt-automation { _dist_version('prompt-automation') }")
            except Exception:
                print("prompt-automation (version unknown)")
            return

        if args.prompt_dir:
            path = args.prompt_dir.expanduser().resolve()
            os.environ["PROMPT_AUTOMATION_PROMPTS"] = str(path)
            self._log.info("using custom prompt directory %s", path)

        if args.assign_hotkey:
            from .. import hotkeys

            hotkeys.assign_hotkey()
            return

        if args.hotkey_status:
            from .hotkey_cmds import show_hotkey_status
            show_hotkey_status()
            return

        if args.hotkey_repair:
            from .hotkey_cmds import repair_hotkey
            repair_hotkey()
            return

        if args.update:
            perform_update(args)
            return

        if args.espanso_sync:
            # Delegate to module to keep concerns isolated
            from .. import espanso_sync as _esp
            argv: list[str] = []
            if args.espanso_skip_install:
                argv.append("--skip-install")
            if args.espanso_auto_bump:
                argv.extend(["--auto-bump", args.espanso_auto_bump])
            _esp.main(argv)
            return

        if args.espanso_clean or args.espanso_clean_list or args.espanso_clean_deep:
            from .espanso_cmds import clean_env
            from .. import espanso_sync as _esp
            # Perform requested clean
            clean_env(list_only=args.espanso_clean_list, deep=args.espanso_clean_deep)
            # If deep clean was requested and not explicitly disabled, run a sync automatically
            if args.espanso_clean_deep and not args.espanso_no_sync and not args.espanso_clean_list:
                _esp.main([])
            return

        if args.espanso_reset:
            # Deep clean and then run sync using the same orchestrator entry
            from .espanso_cmds import clean_env
            from .. import espanso_sync as _esp
            clean_env(list_only=False, deep=True)
            _esp.main([])
            return

        try:
            # Use importlib to load package module for stable patching/import behavior
            import importlib
            _cli_pkg = importlib.import_module('prompt_automation.cli')
            _cli_pkg.ensure_unique_ids(PROMPTS_DIR)
        except ValueError as e:
            print(f"[prompt-automation] {e}")
            return

        if args.self_test:
            from .self_test import run_self_test
            gui_mode = not args.terminal and (
                args.gui or os.environ.get("PROMPT_AUTOMATION_GUI") != "0"
            )
            run_self_test(gui_mode)
            return

        if args.reset_log:
            from .overrides import clear_usage_log
            clear_usage_log()
            return
        if args.reset_file_overrides:
            from .overrides import clear_all_overrides
            clear_all_overrides()
            return
        if args.reset_one_override:
            from .overrides import clear_one_override
            tid, name = args.reset_one_override
            clear_one_override(tid, name)
            return
        if args.list_overrides:
            from .overrides import show_overrides
            show_overrides()
            return

        if args.list:
            # If --tree provided (or feature flag enabled and not overridden by --flat) use hierarchical view
            try:
                from ..features import is_hierarchy_enabled
                use_tree = (args.tree or is_hierarchy_enabled()) and not args.flat
            except Exception:
                use_tree = args.tree and not args.flat
            if use_tree:
                from ..services.hierarchy import TemplateHierarchyScanner, HierarchyNode, filter_tree
                scanner = TemplateHierarchyScanner()
                tree = scanner.scan()
                if args.filter:
                    tree = filter_tree(tree, args.filter)

                def _print(node: HierarchyNode, indent: int = 0) -> None:
                    prefix = "  " * indent
                    if node.type == "folder" and node.name:
                        print(f"{prefix}{node.name}/")
                    for ch in node.children:
                        if ch.type == "folder":
                            _print(ch, indent + 1)
                        else:
                            print(f"{prefix}  {Path(ch.relpath).name}")

                _print(tree)
            else:
                pat = args.filter.lower() if args.filter else None
                for style in list_styles():
                    items = [p for p in list_prompts(style) if not pat or pat in p.name.lower()]
                    if not items:
                        continue
                    print(style)
                    for tmpl_path in items:
                        print(f"  {tmpl_path.name}")
            return

        if args.troubleshoot:
            print(
                "Troubleshooting tips:\n- Ensure dependencies are installed.\n- Logs stored at",
                self.log_dir,
                "\n- Usage DB:",
                logger.DB_PATH,
            )
            return

        # Handle template rendering by ID (workflow automation support)
        if args.template is not None:
            return self._render_template_by_id(args)

        gui_mode = not args.terminal and (
            args.gui or os.environ.get("PROMPT_AUTOMATION_GUI") != "0" or args.focus
        )

        # Observability: log the incoming event and intended mode
        try:
            self._log.debug(
                "hotkey_event_received source=CLI focus=%s gui=%s terminal=%s",
                bool(args.focus), bool(args.gui), bool(args.terminal),
            )
        except Exception:
            pass

        self._log.info("running on %s", platform.platform())

        # Fast path: try to focus existing GUI instance before any dependency checks
        if gui_mode:
            try:
                from ..gui.single_window import singleton as _sw_singleton
                self._log.debug("hotkey_handler_invoked action=focus_app_attempt")
                if _sw_singleton.connect_and_focus_if_running():
                    try:
                        self._log.debug("hotkey_handler_invoked action=focus_app")
                    except Exception:
                        pass
                    return
            except Exception:
                pass

        import importlib
        _cli_pkg = importlib.import_module('prompt_automation.cli')
        if not _cli_pkg.check_dependencies(require_fzf=not gui_mode):
            return
        from ..dev import is_dev_mode
        if not is_dev_mode():
            try:  # never block startup
                updater.check_for_update()
            except Exception:
                pass
            manifest_update.check_and_prompt()
        # Theme resolution: allow CLI override and optional persistence
        try:
            if args.theme:
                if args.persist_theme:
                    from ..theme import resolve as _tres
                    _tres.set_user_theme_preference(args.theme)
                else:
                    os.environ['PROMPT_AUTOMATION_THEME'] = args.theme
            if args.hierarchy:
                # Map to boolean
                enabled = args.hierarchy == "on"
                if args.persist_hierarchy:
                    from ..features import set_user_hierarchy_preference as _set_h
                    _set_h(enabled)
                else:
                    os.environ['PROMPT_AUTOMATION_HIERARCHICAL_TEMPLATES'] = "1" if enabled else "0"
        except Exception:
            pass

        if gui_mode:
            from .. import gui
            try:
                self._log.debug("hotkey_handler_invoked action=show_app")
            except Exception:
                pass
            gui.run()
            return

        banner = Path(__file__).resolve().parent.parent / "resources" / "banner.txt"
        print(banner.read_text())

        try:
            self._log.debug("hotkey_handler_invoked action=terminal")
        except Exception:
            pass

        tmpl: dict[str, Any] | None = select_template_cli()
        if not tmpl:
            return

        # Fast inspection path: print reminders and exit
        if args.show_reminders:
            try:
                from ..reminders import extract_template_reminders, partition_placeholder_reminders
                tlist = extract_template_reminders(tmpl)
                phs = tmpl.get("placeholders") or []
                pmap = partition_placeholder_reminders(phs, tlist)
                if tlist:
                    print("Reminders:")
                    for s in tlist:
                        print(f" - {s}")
                else:
                    print("Reminders: (none)")
                if pmap:
                    print("\nPlaceholder Reminders:")
                    for name, items in pmap.items():
                        print(f" [{name}]")
                        for s in items:
                            print(f"  - {s}")
                return
            except Exception as e:
                print(f"[prompt-automation] Failed to print reminders: {e}")
                return

        res = render_template_cli(tmpl)
        if res:
            text, var_map = res
            print("\n" + "=" * 60)
            try:
                from ..theme import resolve as _tres, model as _tmodel, apply as _tapply
                _name = _tres.ThemeResolver(_tres.get_registry()).resolve()
                _theme = _tmodel.get_theme(_name)
                heading = _tapply.format_heading("RENDERED OUTPUT:", _theme)
            except Exception:
                heading = "RENDERED OUTPUT:"
            print(heading)
            print("=" * 60)
            print(text)
            print("=" * 60)

            # Append to recent history (non-intrusive; ignore failures)
            try:
                from ..history import record_history
                record_history(tmpl, rendered_text=text, final_output=text)
            except Exception:
                pass

            if input("\nProceed with clipboard copy? [Y/n]: ").lower() not in {"n", "no"}:
                paste.copy_to_clipboard(text)
                print(
                    "\n[prompt-automation] Text copied to clipboard. Press Ctrl+V to paste where needed."
                )
                _append_to_files(var_map, text)
                logger.log_usage(tmpl, len(text))

                # Optional Todoist post-action (non-blocking). Uses same omission rules as GUI.
                try:
                    from ..services.todoist_action import build_summary_and_note, send_to_todoist
                    summary, note = build_summary_and_note(
                        action=str(var_map.get("action") or ""),
                        type_=str(var_map.get("type") or ""),
                        dod=str(var_map.get("dod") or ""),
                        nra=str(var_map.get("nra") or ""),
                    )
                    if summary.strip():
                        ok, _msg = send_to_todoist(summary, note)
                        if not ok:
                            print("[prompt-automation] Todoist send failed; output remains in clipboard.")
                except Exception:
                    # Never block CLI flow due to post-action
                    try:
                        print("[prompt-automation] Todoist send failed; output remains in clipboard.")
                    except Exception:
                        pass


__all__ = ["PromptCLI"]
