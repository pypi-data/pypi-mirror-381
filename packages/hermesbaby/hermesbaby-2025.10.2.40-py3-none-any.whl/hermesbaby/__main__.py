################################################################
#                                                              #
#  This file is part of HermesBaby                             #
#                       the software engineer's typewriter     #
#                                                              #
#      https://github.com/hermesbaby                           #
#                                                              #
#  Copyright (c) 2024 Alexander Mann-Wahrenberg (basejumpa)    #
#                                                              #
#  License(s)                                                  #
#                                                              #
#  - MIT for contents used as software                         #
#  - CC BY-SA-4.0 for contents used as method or otherwise     #
#                                                              #
################################################################


import importlib.metadata
import json
import logging
import os
import platform
import re
import shutil
import subprocess
import sys
from importlib.resources import files
from pathlib import Path
from typing import List

import git
import kconfiglib
import typer
from cookiecutter.main import cookiecutter

__version__ = importlib.metadata.version("hermesbaby")

logger = logging.getLogger(__name__)

CFG_CONFIG_CUSTOM_FILE = ".hermesbaby"
CFG_CONFIG_DIR = Path(__file__).parent


_tool_path = Path(sys.executable).parent


def _get_template_dir():
    return files("hermesbaby").joinpath("templates")


_config_file = CFG_CONFIG_DIR / "Kconfig"
_kconfig = kconfiglib.Kconfig(str(_config_file))


def _load_config():
    global _kconfig
    hermesbaby__config_file = Path(os.getcwd()) / CFG_CONFIG_CUSTOM_FILE
    if hermesbaby__config_file.exists():
        _kconfig.load_config(str(hermesbaby__config_file))
        logger.info(f"Using configuration {hermesbaby__config_file}")
    else:
        logger.info("There is no '{hermesbaby__config_file}'. Using default config.")


def _set_env():
    os.environ["HERMESBABY_CWD"] = os.getcwd()


def _tools_load_external_tools() -> dict:
    file_path = CFG_CONFIG_DIR / "external_tools.json"
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        typer.echo(f"Error: {file_path} not found.")
        return {}


def _install_scoop() -> bool:
    """
    Attempts to install scoop in a headless manner by running the scoop installation
    command in PowerShell and providing the required input ('A') automatically.
    Returns True if the installation appears successful.
    """
    # This is the command suggested on https://scoop.sh/#/:
    install_command = (
        "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser -Force; "
        "iwr -useb get.scoop.sh | iex"
    )
    try:
        # Run the command in PowerShell.
        # The input "A\n" is piped to the process to simulate the user pressing 'A'.
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", install_command],
            input="A\n",
            # capture_output=True,
            text=True,
            check=True,
        )
        # After running the command, check if scoop is now installed.
        if shutil.which("scoop"):
            typer.echo("Scoop installation successful.")
            return True
        else:
            typer.echo("Scoop installation did not succeed.")
            return False
    except subprocess.CalledProcessError as e:
        typer.echo(f"Scoop installation failed: {e}")
        return False


def _tools_install_tool(tool: str, info: dict) -> bool:
    """
    Attempts to install a tool using the installation command specified in info.
    Returns True if the installation was successful, False otherwise.
    """
    if "install" not in info:
        typer.echo("      No installation command provided.")
        return False

    typer.echo(f"      Installing using command: {info['install']['windows']}")
    try:
        subprocess.run(info["install"]["windows"], shell=True, check=True)
    except subprocess.CalledProcessError as e:
        typer.echo(f"      Installation failed: {e}")
        return False

    # Verify that the tool is now available.
    if shutil.which(info["run"][platform.system().lower()]):
        typer.echo("      Installation successful.")
        return True
    else:
        typer.echo("      Installation did not succeed.")
        return False


class SortedGroup(typer.core.TyperGroup):
    def list_commands(self, ctx):
        commands = super().list_commands(ctx)
        return sorted(commands)


app = typer.Typer(
    help="The Software and Systems Engineers' Typewriter",
    no_args_is_help=True,
    cls=SortedGroup,
)

app_htaccess = typer.Typer(
    help="Manage access of published document",
    no_args_is_help=True,
)
app.add_typer(app_htaccess, name="htaccess")

app_tools = typer.Typer(
    help="Manage tools used during document build",
    no_args_is_help=True,
)
app.add_typer(app_tools, name="tools")

app_vscode_extensions = typer.Typer(
    help="Manage VSCode extensions",
    no_args_is_help=True,
)
app.add_typer(app_vscode_extensions, name="vscode")


@app.callback(invoke_without_command=False)
def version(
    version: bool = typer.Option(
        None,
        "--version",
        callback=lambda value: print(__version__) or exit() if value else None,
        is_eager=True,
        help="Show the version and exit.",
    )
):
    """CLI Tool hb"""


@app.command()
def new(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to create the project. Optional: defaults to '.' (current directory).",
    ),
    template: str = typer.Option(
        None, "--template", "-t", help="Template to use. Default: zero"
    ),
    list_templates: bool = typer.Option(
        False, "--list-templates", "-l", help="List available templates"
    ),
):
    """Create a new project"""

    _set_env()
    _load_config()

    templates_root_path = _get_template_dir()

    # If --list is provided, list available template directories and exit.
    if list_templates:
        try:
            templates = [d.name for d in templates_root_path.iterdir() if d.is_dir()]
        except Exception as e:
            typer.echo(f"Error listing templates: {e}", err=True)
            raise typer.Abort()
        if not templates:
            typer.echo(f"No templates found in {templates_root_path}")
        else:
            typer.echo("Available templates:")
            for t in sorted(templates):
                typer.echo(f"  - {t}")
        raise typer.Exit()

    if template is None:
        template = "zero"

    template_path = templates_root_path / template

    # The output directory is the current working directory plus

    # Error handling
    if not template_path.exists():
        typer.echo(
            f"Template does not exist. Choose from: {os.listdir(templates_root_path)}",
            err=True,
        )
        raise typer.Abort()

    # Check if target directory is empty or doesn't exist
    target_dir = Path(directory)
    if target_dir.exists():
        # Check if directory is empty
        if any(target_dir.iterdir()):
            typer.echo(
                f"Error: Directory '{directory}' is not empty. "
                f"Please choose an empty directory or one that doesn't exist.",
                err=True,
            )
            raise typer.Abort()

    # Execution

    cookiecutter(
        template=str(template_path),
        output_dir=directory,
        overwrite_if_exists=True,
        no_input=True,
    )

    typer.echo(
        f'Created new project in directory {directory} using template "{template}"'
    )


@app.command()
def html(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """Build to format HTML"""

    _set_env()
    _load_config()

    build_dir = Path(_kconfig.syms["BUILD__DIRS__BUILD"].str_value) / ctx.info_name

    executable = os.path.join(_tool_path, "sphinx-build")
    command = f"""
        {executable}
        -b html
        -W
        -c {str(CFG_CONFIG_DIR)}
        {_kconfig.syms["BUILD__DIRS__SOURCE"].str_value}
        {build_dir}
    """
    typer.echo(command)
    result = subprocess.run(command.split(), cwd=directory)
    sys.exit(result.returncode)


@app.command()
def html_live(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """Build to format HTML with live reload"""

    _set_env()
    _load_config()

    build_dir = Path(_kconfig.syms["BUILD__DIRS__BUILD"].str_value) / ctx.info_name
    executable = os.path.join(_tool_path, "sphinx-autobuild")
    command = f"""
        {executable}
        -b html
        -j 10
        -W
        -c {str(CFG_CONFIG_DIR)}
        {_kconfig.syms["BUILD__DIRS__SOURCE"].str_value}
        {build_dir}
        --watch {_kconfig.syms["BUILD__DIRS__CONFIG"].str_value}
        --re-ignore '_tags/.*'
        --port {int(_kconfig.syms["BUILD__PORTS__HTML__LIVE"].str_value)}
        --open-browser
    """
    typer.echo(command)
    result = subprocess.run(command.split(), cwd=directory)
    sys.exit(result.returncode)


@app.command()
def configure(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """Configure the project"""

    _set_env()
    _load_config()

    # Set environment variable KCONFIG_CONFIG to the value of CFG_CONFIG_CUSTOM_FILE
    os.environ["KCONFIG_CONFIG"] = CFG_CONFIG_CUSTOM_FILE

    # Check if we're running in a headless environment (like GitHub Codespace)
    is_headless = "DISPLAY" not in os.environ or not os.environ["DISPLAY"]

    # Use text-based config (menuconfig) in headless environments, GUI (guiconfig) otherwise
    config_tool = "menuconfig" if is_headless else "guiconfig"

    # Start the configuration tool as a subprocess
    command = f"{_tool_path}/{config_tool} {_config_file}"
    typer.echo(command)
    result = subprocess.run(command.split(), cwd=directory)

    # Don't retain any *.old file
    Path(CFG_CONFIG_CUSTOM_FILE + ".old").unlink(missing_ok=True)

    sys.exit(result.returncode)


@app.command()
def clean(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """Clean the build directory"""

    _set_env()
    _load_config()

    folder_to_remove = Path(directory) / _kconfig.syms["BUILD__DIRS__BUILD"].str_value
    typer.echo(f"Remove {folder_to_remove}")
    if Path(folder_to_remove).exists():
        shutil.rmtree(folder_to_remove)


@app.command()
def venv(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """Create a virtual environment from the python environment shipped with HermesBaby"""

    if not directory:
        typer.echo(ctx.get_help())
        raise typer.Exit()

    _set_env()
    _load_config()

    _flag_install = True

    _venv_dir = Path(directory) / Path(".venv")

    """Create a virtual environment using hb's own interpreter."""
    if _venv_dir.exists():
        typer.echo(f"Virtual environment in directory {_venv_dir} already exists with")
        _flag_install = False

        # Probe a little more if the venv is usable. If not exit with an error and suggest to remove the directory.
        python_executable = (
            _venv_dir / "bin" / "python"
            if platform.system() != "Windows"
            else _venv_dir / "Scripts" / "python.exe"
        )

        # Inside a try-except block try to run the python executable with --version. This is a probe to check if the venv is usable.
        try:
            subprocess.run([python_executable, "--version"], check=True)
        except Exception:
            typer.echo(
                f"Python executable {python_executable} is not usable in virtual environment. "
                f"Please remove the directory {_venv_dir} and try again."
            )
            raise typer.Exit(code=1)

    if _flag_install:
        typer.echo(
            f"Creating virtual environment at {_venv_dir} using Python at {sys.executable}..."
        )

        # Wrap the call inside a try-except block to handle errors gracefully
        try:
            subprocess.run([sys.executable, "-m", "venv", str(_venv_dir)], check=True)
            typer.echo("Virtual environment created successfully.")
        except subprocess.CalledProcessError as e:
            typer.echo(f"Error creating virtual environment: {e}", err=True)
            typer.echo(
                f"Remove the directory {_venv_dir} and try again if you want to create a new virtual environment."
            )
            raise typer.Exit(code=1)

    # If the file docs/requirements.txt exists, install the requirements
    requirements_file = Path(directory) / os.path.join(
        _kconfig.syms["BUILD__DIRS__CONFIG"].str_value, "requirements.txt"
    )

    if requirements_file.exists():
        typer.echo(
            f"Installing requirements from {requirements_file} into virtual environment under {_venv_dir}..."
        )

        # Depending on the OS the python executable is in the venv may differ.
        if platform.system() == "Windows":
            python_executable = _venv_dir / "Scripts" / "python.exe"
        else:
            python_executable = _venv_dir / "bin" / "python"

        # Wrap the call inside a try-except block to handle errors gracefully
        try:
            subprocess.run(
                [
                    python_executable,
                    "-m",
                    "pip",
                    "install",
                    "-r",
                    str(requirements_file),
                ],
                check=True,
            )
        except subprocess.CalledProcessError as e:
            typer.echo(
                f"Error installing requirements: {e}. Please check the requirements file."
            )
            raise typer.Exit(code=1)

        typer.echo("Requirements installed successfully.")

    if _flag_install:
        typer.echo("To activate the virtual environment, run:")
        typer.echo("    bash/git-bash: source .venv/bin/activate")
        typer.echo("    cmd: .venv\\Scripts\\activate.bat")


@app_htaccess.command()
def groups(
    ctx: typer.Context,
    members: List[str] = typer.Argument(
        None,
        help="Member or members to check. ",
    ),
):
    """Lists the groups one or more members are in. If more than one given, also the groups they share."""

    if not members:
        typer.echo("No members given.")
        typer.echo(ctx.get_help())
        raise typer.Exit()

    from .web_access_ctrl import shared_groups

    shared_groups.main(members)


@app_htaccess.command()
def members(
    ctx: typer.Context,
    groups: List[str] = typer.Argument(
        None,
        help="Group or groups to check. ",
    ),
):
    """List the members of one or more groups"""

    if not groups:
        typer.echo("No groups given.")
        typer.echo(ctx.get_help())
        raise typer.Exit()

    typer.echo("Grab a coffee, this may take a while...")

    from .web_access_ctrl import group_members

    group_members.main(groups)


# Obsolete. Use hb htaccess --update instead
@app_htaccess.command()
def update(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """Update/create web_root/.htaccess from htaccess.yaml"""

    if not directory:
        typer.echo(ctx.get_help())
        raise typer.Exit()

    _set_env()
    _load_config()

    from .web_access_ctrl import create_htaccess_entries

    yaml_template_file = CFG_CONFIG_DIR / "htaccess.yaml"
    yaml_file = Path(directory) / os.path.join(
        _kconfig.syms["BUILD__DIRS__CONFIG"].str_value, "htaccess.yaml"
    )
    outfile_file = Path(directory) / os.path.join(
        _kconfig.syms["BUILD__DIRS__SOURCE"].str_value, "web_root", ".htaccess"
    )
    expand_file = Path(directory) / os.path.join(
        _kconfig.syms["BUILD__DIRS__SOURCE"].str_value,
        "99-Appendix/99-Access-to-Published-Document/_tables/htaccess__all_users.yaml",
    )

    if not os.path.exists(yaml_file):
        typer.echo(f"Created template file {yaml_file}")
        shutil.copy(yaml_template_file, yaml_file)

    if not os.path.exists(expand_file):
        expand_file = None

    create_htaccess_entries.main("", yaml_file, outfile_file, expand_file)


@app.command()
def publish(
    ctx: typer.Context,
    directory: str = typer.Argument(
        ".",
        help="Directory where to execute the command. ",
    ),
):
    """
    Publish the build output to the configured server using SSH
    """

    _set_env()
    _load_config()

    publish_host = _kconfig.syms["PUBLISH__HOST"].str_value
    publish_user = _kconfig.syms["PUBLISH__USER"].str_value
    scm_owner_kind = _kconfig.syms["SCM__OWNER_KIND"].str_value
    scm_owner = _kconfig.syms["SCM__OWNER"].str_value

    publish_repo = _kconfig.syms["PUBLISH__REPO"].str_value
    if publish_repo == "":
        publish_repo = _kconfig.syms["SCM__REPO"].str_value

    dir_build = Path(directory) / _kconfig.syms["BUILD__DIRS__BUILD"].str_value

    # In case the publish_user is empty or not defined, use the scm_owner as default
    if not publish_user:
        publish_user = scm_owner
        typer.echo(
            f"No PUBLISH__USER defined. Using SCM__OWNER '{scm_owner}' as default user."
        )

    ssh_key_path = (
        Path(directory) / _kconfig.syms["PUBLISH__SSH_PATH"].str_value / "id_rsa"
    )

    try:
        _repo = git.Repo(search_parent_directories=True, path=directory)
        git_branch = _repo.active_branch.name
    except:
        typer.echo("Could not get git branch. Aborting publish step", err=True)
        raise typer.Exit(code=1)

    publish_url = f"https://{publish_host}/{scm_owner_kind}/{scm_owner}/{publish_repo}/{git_branch}"

    try:
        typer.echo(f"Publishing to {publish_url}")

        publish_source_folder = f"{dir_build}/html"

        # In case the publish_source_folder doesn't exist raise an exception:
        if not os.path.exists(publish_source_folder):
            raise Exception(
                f"Publish source folder {publish_source_folder} does not exist."
            )

        # Ensure the SSH key has correct permissions
        subprocess.run(["chmod", "600", str(ssh_key_path)], check=True, text=True)

        # Create and clean up remote directories
        ssh_cleanup_command = (
            f"ssh "
            f"-o StrictHostKeyChecking=no "
            f"-o UserKnownHostsFile=/dev/null "
            f"-i {ssh_key_path} "
            f"{publish_user}@{publish_host} "
            f'"(mkdir -p /var/www/html/{scm_owner_kind}/{scm_owner}/{publish_repo} '
            f"&&  cd /var/www/html/{scm_owner_kind}/{scm_owner}/{publish_repo} "
            f'&& rm -rf {git_branch})"'
        )
        subprocess.run(ssh_cleanup_command, shell=True, check=True, text=True)

        # Compress and transfer files
        tar_command = (
            f"tar -czf - "
            f"-C {publish_source_folder} . "
            f"| ssh "
            f"-o StrictHostKeyChecking=no "
            f"-o UserKnownHostsFile=/dev/null "
            f"-i {ssh_key_path} {publish_user}@{publish_host} "
            f'"(cd /var/www/html/{scm_owner_kind}/{scm_owner}/{publish_repo} '
            f"&& mkdir -p {git_branch} "
            f'&& tar -xzf - -C {git_branch})"'
        )
        subprocess.run(tar_command, shell=True, check=True, text=True)

        typer.echo(f"Published to {publish_url}")

    except Exception as e:
        typer.echo(f"Error during publishing: {e}", err=True)
        raise typer.Exit(code=1)


@app_tools.command()
def check_scoop(
    install: bool = typer.Option(
        False, "--install", help="Automatically install scoop if missing"
    )
):
    """
    Checks if scoop is installed
    and installs missing extensions if --install is specified.
    (Experimental feature)
    """
    if shutil.which("scoop"):
        typer.echo("Scoop is already installed.")
        return

    typer.echo("Scoop is missing.")
    if install:
        typer.echo("Attempting to install scoop headlessly...")
        if _install_scoop():
            typer.echo("Scoop was installed successfully.")
        else:
            typer.echo("Failed to install scoop automatically.")
            raise typer.Exit(code=1)
    else:
        typer.echo("Please install scoop manually from https://scoop.sh/")
        raise typer.Exit(code=1)


@app_tools.command()
def check(
    install: bool = typer.Option(
        False, "--install", help="Automatically install missing tools"
    ),
    tag: str = typer.Option(None, "--tag", help="Filter tag"),
):
    """
    Checks for the presence of necessary external tools
    and installs missing extensions if --install is specified.
    """
    tools = _tools_load_external_tools()  # Load commands from the JSON file

    if not tools:
        return

    if tag:
        tools = {k: v for k, v in tools.items() if tag in v.get("tags", [])}

    num_tools_missing = 0
    typer.echo("Checking system for required tools...\n")
    for tool, info in tools.items():
        typer.echo(f"   {tool}: ", nl=False)
        if shutil.which(info["run"][platform.system().lower()]):
            typer.echo("found")
            # If found, we skip the rest of this iteration.
            continue

        # If the tool is missing:
        typer.echo("missing")
        typer.echo(f"      Website: {info['website']}")
        try:
            install_cmd = info["install"][platform.system().lower()]
        except KeyError:
            install_cmd = None
        if install_cmd:
            typer.echo(f"      Install it via: {install_cmd}")
            if install:
                if not _tools_install_tool(tool, info):
                    num_tools_missing += 1
            else:
                num_tools_missing += 1
        else:
            num_tools_missing += 1

        typer.echo()

    if not num_tools_missing:
        typer.echo("\nAll tools are present. You are ready to go!")
    else:
        typer.echo(f"\n{num_tools_missing} tools are missing. Please install them.")
        raise typer.Exit(code=1)


# Helper functions for VSCode extensions management
def _vscode_check_code_available():
    """Check if VSCode CLI is available"""
    if not shutil.which("code"):
        typer.echo(
            "Visual Studio Code is not installed or 'code' command is not in PATH."
        )
        raise typer.Exit(code=1)


def _vscode_get_extensions_dir():
    """Get the extensions directory path"""
    extensions_dir = CFG_CONFIG_DIR / "vscode-extensions"
    if not extensions_dir.exists():
        typer.echo(f"Error: Directory {extensions_dir} not found.")
        raise typer.Exit(code=1)
    return extensions_dir


def _vscode_check_constraints(installed_version):
    """Check if installed VSCode version meets constraints"""
    constraints_file = CFG_CONFIG_DIR / "vscode-extensions" / "_constraints"

    if not constraints_file.exists():
        return None  # No constraints to check

    try:
        with open(constraints_file, "r") as f:
            content = f.read().strip()

        # Parse constraint like "code>=1.98.2"
        for line in content.split("\n"):
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            if line.startswith("code>="):
                required_version = line.replace("code>=", "").strip()

                # Compare versions
                try:
                    installed_parts = [int(x) for x in installed_version.split(".")]
                    required_parts = [int(x) for x in required_version.split(".")]

                    # Pad shorter version with zeros
                    max_len = max(len(installed_parts), len(required_parts))
                    installed_parts.extend([0] * (max_len - len(installed_parts)))
                    required_parts.extend([0] * (max_len - len(required_parts)))

                    if installed_parts >= required_parts:
                        return True, required_version
                    else:
                        return False, required_version
                except ValueError:
                    return None  # Can't parse versions

    except Exception as e:
        typer.echo(f"Warning: Could not read constraints file: {e}")
        return None

    return None


def _vscode_display_info():
    """Display VSCode installation path and version information"""
    # Display VSCode installation path
    code_path = shutil.which("code")
    if code_path:
        typer.echo()
        typer.echo(f"VSCode CLI path: {code_path}")

    # Get and display VSCode version
    installed_version = None
    try:
        result = subprocess.run(
            ["code", "--version"],
            capture_output=True,
            text=True,
            check=True,
            shell=True,
        )
        version_lines = result.stdout.strip().split("\n")
        if version_lines:
            installed_version = version_lines[0]
            typer.echo(f"VSCode version: {installed_version}")
            if len(version_lines) > 1:
                typer.echo(f"Commit: {version_lines[1]}")

            # Check constraints
            constraint_result = _vscode_check_constraints(installed_version)
            if constraint_result is not None:
                meets_constraint, required_version = constraint_result
                if meets_constraint:
                    typer.echo(f"✓ Version meets constraint: code>={required_version}")
                else:
                    typer.echo(
                        f"✗ Version does NOT meet constraint: code>={required_version}"
                    )
                    typer.echo(
                        f"  Please upgrade VSCode to version {required_version} or later"
                    )

    except subprocess.CalledProcessError as e:
        typer.echo(f"Could not retrieve VSCode version: {e}")

    typer.echo()  # Add blank line after info


def _vscode_load_recommendations(extensions_dir):
    """Load recommended extensions from directory"""
    version_pattern = re.compile(r"-(\d+\.\d+\.\d+)\.vsix$")
    recommendations = {}  # {extension_name: hb_version}
    try:
        for file in extensions_dir.iterdir():
            if file.is_file() and file.name.endswith(".vsix"):
                # Extract version from filename
                match = version_pattern.search(file.name)
                if match:
                    hb_version = match.group(1)
                    extension_name = version_pattern.sub("", file.name)
                    recommendations[extension_name] = hb_version
    except Exception as e:
        typer.echo(f"Error reading extensions directory: {e}")
        raise typer.Exit(code=1)

    if not recommendations:
        typer.echo(f"No .vsix files found in {extensions_dir}")
        raise typer.Exit(code=1)

    return recommendations, version_pattern


def _vscode_get_installed_extensions():
    """Get currently installed extensions with versions"""
    try:
        result = subprocess.run(
            ["code", "--list-extensions", "--show-versions"],
            capture_output=True,
            text=True,
            check=True,
            shell=True,
        )
        installed_extensions = {}  # {extension_name: installed_version}
        for line in result.stdout.splitlines():
            if "@" in line:
                name, version = line.rsplit("@", 1)
                installed_extensions[name] = version
        return installed_extensions
    except subprocess.CalledProcessError as e:
        typer.echo(f"Error listing VSCode extensions: {e}")
        raise typer.Exit(code=1)


def _vscode_compare_versions(installed_ver, hb_ver):
    """Compare semantic versions and return status"""
    try:
        inst_parts = [int(x) for x in installed_ver.split(".")]
        hb_parts = [int(x) for x in hb_ver.split(".")]

        # Pad shorter version with zeros
        max_len = max(len(inst_parts), len(hb_parts))
        inst_parts.extend([0] * (max_len - len(inst_parts)))
        hb_parts.extend([0] * (max_len - len(hb_parts)))

        if inst_parts > hb_parts:
            return "installed-newer"
        elif inst_parts < hb_parts:
            return "installed-older"
        else:
            return "installed"
    except (ValueError, AttributeError):
        # If version comparison fails, just return installed
        return "installed"


def _vscode_display_table(recommendations, installed_extensions):
    """Display the extensions table"""
    # Build table data
    table_data = []
    missing_extensions = []

    for ext_name, hb_version in sorted(recommendations.items()):
        if ext_name in installed_extensions:
            inst_version = installed_extensions[ext_name]
            status = _vscode_compare_versions(inst_version, hb_version)
        else:
            inst_version = ""
            status = "missing"
            missing_extensions.append(ext_name)

        table_data.append(
            {
                "extension": ext_name,
                "hb": hb_version,
                "installed": inst_version,
                "status": status,
            }
        )

    # Calculate column widths
    max_ext_len = max(len(row["extension"]) for row in table_data)
    max_hb_len = max(len(row["hb"]) for row in table_data)
    max_inst_len = max(len(row["installed"]) for row in table_data)
    max_status_len = max(len(row["status"]) for row in table_data)

    # Ensure minimum widths for headers
    max_ext_len = max(max_ext_len, len("extension"))
    max_hb_len = max(max_hb_len, len("version-hb"))
    max_inst_len = max(max_inst_len, len("version-installed"))
    max_status_len = max(max_status_len, len("status"))

    # Print table header
    header = (
        f"{'extension':<{max_ext_len}}  "
        f"{'version-hb':<{max_hb_len}}  "
        f"{'version-installed':<{max_inst_len}}  "
        f"{'status':<{max_status_len}}"
    )
    typer.echo(header)
    typer.echo("-" * len(header))

    # Print table rows
    for row in table_data:
        line = (
            f"{row['extension']:<{max_ext_len}}  "
            f"{row['hb']:<{max_hb_len}}  "
            f"{row['installed']:<{max_inst_len}}  "
            f"{row['status']:<{max_status_len}}"
        )
        typer.echo(line)

    return missing_extensions


@app_vscode_extensions.command(name="check")
def vscode_check():
    """Check VSCode extension status and display table"""
    _vscode_check_code_available()
    _vscode_display_info()

    extensions_dir = _vscode_get_extensions_dir()
    recommendations, _ = _vscode_load_recommendations(extensions_dir)
    installed_extensions = _vscode_get_installed_extensions()
    missing_extensions = _vscode_display_table(recommendations, installed_extensions)

    if missing_extensions:
        typer.echo(
            f"\n{len(missing_extensions)} extension(s) missing. "
            "Use 'hb vscode install' to install them from the VSIX files shipped with HermesBaby."
        )


@app_vscode_extensions.command(name="install")
def vscode_install():
    """Install missing VSCode extensions from embedded VSIX files"""
    _vscode_check_code_available()
    extensions_dir = _vscode_get_extensions_dir()
    recommendations, version_pattern = _vscode_load_recommendations(extensions_dir)
    installed_extensions = _vscode_get_installed_extensions()
    missing_extensions = _vscode_display_table(recommendations, installed_extensions)

    if missing_extensions:
        typer.echo(
            "\nAttempting to install missing extensions using embedded VSIX files..."
        )

        # Build a mapping of extension names to their VSIX file paths
        vsix_files = {}
        for file in extensions_dir.iterdir():
            if file.is_file() and file.name.endswith(".vsix"):
                match = version_pattern.search(file.name)
                if match:
                    extension_name = version_pattern.sub("", file.name)
                    vsix_files[extension_name] = file

        for ext in missing_extensions:
            if ext in vsix_files:
                vsix_path = vsix_files[ext]
                typer.echo(f"Installing {ext} from {vsix_path.name}...")
                try:
                    subprocess.run(
                        ["code", "--install-extension", str(vsix_path)],
                        check=True,
                        shell=True,
                    )
                    typer.echo(f"  Installed {ext} successfully.")
                except subprocess.CalledProcessError as e:
                    typer.echo(f"  Failed to install {ext}: {e}")
            else:
                typer.echo(f"  Warning: VSIX file not found for {ext}")

        # Re-run check after installation
        typer.echo("\nVerifying installation...\n")
        installed_extensions = _vscode_get_installed_extensions()
        _vscode_display_table(recommendations, installed_extensions)
    else:
        typer.echo("\nAll recommended extensions are already installed.")


@app_vscode_extensions.command(name="uninstall")
def vscode_uninstall():
    """Uninstall all recommended VSCode extensions"""
    _vscode_check_code_available()
    extensions_dir = _vscode_get_extensions_dir()
    recommendations, _ = _vscode_load_recommendations(extensions_dir)
    installed_extensions = _vscode_get_installed_extensions()
    _vscode_display_table(recommendations, installed_extensions)

    # Get list of recommended extensions that are currently installed
    installed_recommended = [
        ext_name
        for ext_name in recommendations.keys()
        if ext_name in installed_extensions
    ]

    if not installed_recommended:
        typer.echo("\nNo recommended extensions are currently installed.")
    else:
        typer.echo(
            f"\nUninstalling {len(installed_recommended)} recommended extension(s)..."
        )
        for ext in installed_recommended:
            typer.echo(f"Uninstalling {ext}...")
            try:
                subprocess.run(
                    ["code", "--uninstall-extension", ext],
                    check=True,
                    shell=True,
                )
                typer.echo(f"  Uninstalled {ext} successfully.")
            except subprocess.CalledProcessError as e:
                typer.echo(f"  Failed to uninstall {ext}: {e}")

        # Re-run check after uninstallation
        typer.echo("\nVerifying uninstallation...\n")
        installed_extensions = _vscode_get_installed_extensions()
        _vscode_display_table(recommendations, installed_extensions)


@app_tools.command()
def install():
    """Install the external tools necessary for documentation build"""

    typer.echo("Installing tools for CI/CD pipeline")

    # Check if running on Ubuntu Linux
    # Check if running on Linux
    system = platform.system()
    if system != "Linux":
        typer.echo(
            f"Error: This command is only supported on Debian-based Linux distributions. Detected system: {system}"
        )
        raise typer.Exit(code=1)

    # Check if it's a Debian-based distribution
    is_debian_based = False
    try:
        with open("/etc/os-release", "r") as f:
            os_info = f.read().lower()
            if "debian" in os_info or "ubuntu" in os_info:
                is_debian_based = True
    except FileNotFoundError:
        pass

    if not is_debian_based:
        typer.echo(
            "Error: This command is only supported on Debian-based Linux distributions."
        )
        raise typer.Exit(code=1)

    path = Path(__file__).parent

    command = f"{path}/setup.sh"
    typer.echo(command)
    result = subprocess.run(command.split(), cwd=path)

    sys.exit(result.returncode)


if __name__ == "__main__":
    app()
