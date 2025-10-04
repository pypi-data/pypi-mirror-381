"""Install command implementation for Claude Code/Desktop integration."""

import json
import shutil
import sys
from pathlib import Path
from typing import Dict, Literal, Optional

import click
from rich.panel import Panel

from ..utils import console


def detect_installation_type() -> Literal["pipx", "pip", "dev"]:
    """Detect how mcp-browser was installed.

    Returns:
        "pipx" if installed via pipx
        "pip" if installed via pip in a virtual environment
        "dev" if running from development directory
    """
    executable = Path(sys.executable)

    # Check for pipx installation
    # pipx installs in ~/.local/pipx/venvs/<package>/
    if ".local/pipx" in str(executable) or "pipx/venvs" in str(executable):
        return "pipx"

    # Check for development mode
    # In dev mode, we're likely in a venv in the project directory
    project_indicators = [".git", "pyproject.toml", "setup.py"]
    current = Path.cwd()
    for _ in range(5):  # Check up to 5 levels up
        if any((current / indicator).exists() for indicator in project_indicators):
            return "dev"
        if current.parent == current:
            break
        current = current.parent

    # Check if in a virtual environment
    if hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    ):
        return "pip"

    # Default to pip
    return "pip"


def get_command_path() -> str:
    """Get the appropriate command path based on installation type.

    Returns:
        Command string to use in MCP configuration
    """
    install_type = detect_installation_type()

    if install_type == "pipx":
        # pipx installations can use the direct command
        return "mcp-browser"

    elif install_type == "pip":
        # Try to find mcp-browser in PATH
        which_path = shutil.which("mcp-browser")
        if which_path:
            return which_path

        # Fallback to direct command
        return "mcp-browser"

    else:  # dev
        # For development, use the mcp-server.py script with the current Python
        # Find the script location
        script_locations = [
            Path.cwd() / "scripts" / "mcp-server.py",
            Path(__file__).parent.parent.parent.parent / "scripts" / "mcp-server.py",
        ]

        for script_path in script_locations:
            if script_path.exists():
                # Return python executable and script path
                return f"{sys.executable}"

        # Fallback to command
        return "mcp-browser"


def get_command_args(install_type: str) -> list:
    """Get command arguments based on installation type.

    Args:
        install_type: The detected installation type

    Returns:
        List of command arguments
    """
    if install_type == "dev":
        # For dev mode, if we're using python directly, include the script path
        script_locations = [
            Path.cwd() / "scripts" / "mcp-server.py",
            Path(__file__).parent.parent.parent.parent / "scripts" / "mcp-server.py",
        ]

        for script_path in script_locations:
            if script_path.exists():
                return [str(script_path), "mcp"]

    return ["mcp"]


def get_claude_code_config_path() -> Path:
    """Get the Claude Code configuration file path."""
    return Path.home() / ".claude" / "settings.local.json"


def get_claude_desktop_config_path() -> Optional[Path]:
    """Get the Claude Desktop configuration file path based on OS.

    Returns:
        Path to config file, or None if OS not supported
    """
    if sys.platform == "darwin":  # macOS
        return (
            Path.home()
            / "Library"
            / "Application Support"
            / "Claude"
            / "claude_desktop_config.json"
        )
    elif sys.platform == "linux":
        return Path.home() / ".config" / "Claude" / "claude_desktop_config.json"
    elif sys.platform == "win32":
        import os

        appdata = os.environ.get("APPDATA")
        if appdata:
            return Path(appdata) / "Claude" / "claude_desktop_config.json"

    return None


def load_or_create_config(config_path: Path) -> Dict:
    """Load existing config or create new one.

    Args:
        config_path: Path to configuration file

    Returns:
        Configuration dictionary
    """
    if config_path.exists():
        try:
            with open(config_path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            console.print(
                f"[yellow]Warning: Invalid JSON in {config_path}, creating new config[/yellow]"
            )
            return {}
        except Exception as e:
            console.print(
                f"[yellow]Warning: Could not read {config_path}: {e}[/yellow]"
            )
            return {}

    return {}


def save_config(config_path: Path, config: Dict) -> bool:
    """Save configuration to file.

    Args:
        config_path: Path to configuration file
        config: Configuration dictionary

    Returns:
        True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        config_path.parent.mkdir(parents=True, exist_ok=True)

        # Write with pretty formatting
        with open(config_path, "w") as f:
            json.dump(config, f, indent=2)

        return True
    except Exception as e:
        console.print(f"[red]Error saving config to {config_path}: {e}[/red]")
        return False


def update_mcp_config(config_path: Path, force: bool = False) -> bool:
    """Update MCP configuration with mcp-browser server.

    Args:
        config_path: Path to configuration file
        force: Whether to overwrite existing configuration

    Returns:
        True if successful, False otherwise
    """
    # Load or create config
    config = load_or_create_config(config_path)

    # Ensure mcpServers section exists
    if "mcpServers" not in config:
        config["mcpServers"] = {}

    # Check if mcp-browser already configured
    if "mcp-browser" in config["mcpServers"] and not force:
        console.print(
            "[yellow]mcp-browser is already configured. Use --force to overwrite.[/yellow]"
        )
        return False

    # Detect installation and get command
    install_type = detect_installation_type()
    command = get_command_path()
    args = get_command_args(install_type)

    # Update configuration
    config["mcpServers"]["mcp-browser"] = {"command": command, "args": args}

    # Save configuration
    if save_config(config_path, config):
        console.print(f"[green]✓[/green] Updated configuration at {config_path}")
        console.print(f"  Installation type: [cyan]{install_type}[/cyan]")
        console.print(f"  Command: [cyan]{command}[/cyan]")
        console.print(f"  Args: [cyan]{args}[/cyan]")
        return True

    return False


@click.command()
@click.option(
    "--target",
    type=click.Choice(["claude-code", "claude-desktop", "both"], case_sensitive=False),
    default="claude-code",
    help="Installation target (default: claude-code)",
)
@click.option("--force", is_flag=True, help="Overwrite existing configuration")
def install(target: str, force: bool):
    """⚙️ Install MCP Browser configuration for Claude Code/Desktop.

    \b
    Automatically detects your installation type and configures MCP Browser
    for use with Claude Code or Claude Desktop.

    \b
    Installation types detected:
      • pipx: Installed via pipx (uses 'mcp-browser' command)
      • pip:  Installed via pip (uses full path)
      • dev:  Development mode (uses Python script)

    \b
    Examples:
      mcp-browser install                         # Install for Claude Code
      mcp-browser install --target claude-desktop # Install for Claude Desktop
      mcp-browser install --target both           # Install for both
      mcp-browser install --force                 # Overwrite existing config

    \b
    Configuration locations:
      Claude Code:    ~/.claude/settings.local.json
      Claude Desktop: OS-specific location
        • macOS:   ~/Library/Application Support/Claude/
        • Linux:   ~/.config/Claude/
        • Windows: %APPDATA%/Claude/

    \b
    After installation:
      1. Restart Claude Code or Claude Desktop
      2. The 'mcp-browser' MCP server should be available
      3. Start the server with: mcp-browser start
    """
    console.print(
        Panel.fit(
            "[bold]Installing MCP Browser Configuration[/bold]\n\n"
            f"Target: [cyan]{target}[/cyan]\n"
            f"Force overwrite: [cyan]{force}[/cyan]",
            title="Installation",
            border_style="blue",
        )
    )

    success_count = 0
    total_count = 0

    # Install for Claude Code
    if target in ["claude-code", "both"]:
        total_count += 1
        console.print("\n[bold]Installing for Claude Code...[/bold]")
        config_path = get_claude_code_config_path()

        if update_mcp_config(config_path, force):
            success_count += 1
        else:
            console.print("[red]✗[/red] Failed to update Claude Code configuration")

    # Install for Claude Desktop
    if target in ["claude-desktop", "both"]:
        total_count += 1
        console.print("\n[bold]Installing for Claude Desktop...[/bold]")
        config_path = get_claude_desktop_config_path()

        if config_path is None:
            console.print(
                f"[red]✗[/red] Claude Desktop config path not found for {sys.platform}"
            )
        elif update_mcp_config(config_path, force):
            success_count += 1
        else:
            console.print("[red]✗[/red] Failed to update Claude Desktop configuration")

    # Summary
    console.print()
    if success_count == total_count:
        console.print(
            Panel.fit(
                "[bold green]✓ Installation Complete![/bold green]\n\n"
                "[bold]Next steps:[/bold]\n"
                "1. Restart Claude Code or Claude Desktop\n"
                "2. Start the MCP Browser server:\n"
                "   [cyan]mcp-browser start[/cyan]\n"
                "3. Install the Chrome extension from the dashboard\n\n"
                "[dim]The mcp-browser MCP server should now be available[/dim]",
                title="Success",
                border_style="green",
            )
        )
    elif success_count > 0:
        console.print(
            Panel.fit(
                f"[bold yellow]⚠ Partial Success[/bold yellow]\n\n"
                f"Configured {success_count} of {total_count} targets\n"
                "Check error messages above for details",
                title="Warning",
                border_style="yellow",
            )
        )
    else:
        console.print(
            Panel.fit(
                "[bold red]✗ Installation Failed[/bold red]\n\n"
                "No configurations were updated\n"
                "Check error messages above for details",
                title="Error",
                border_style="red",
            )
        )
        sys.exit(1)
