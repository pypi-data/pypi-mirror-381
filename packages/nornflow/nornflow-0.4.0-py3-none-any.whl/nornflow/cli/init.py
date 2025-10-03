import os
import shutil
from pathlib import Path

import typer

from nornflow import NornFlow, NornFlowBuilder
from nornflow.cli.constants import (
    FILTERS_DIR,
    GREET_USER_TASK_FILE,
    HELLO_WORLD_TASK_FILE,
    INIT_BANNER,
    NORNFLOW_SETTINGS,
    NORNIR_DEFAULT_CONFIG_DIR,
    SAMPLE_NORNFLOW_FILE,
    SAMPLE_NORNIR_CONFIGS_DIR,
    SAMPLE_VARS_FILE,
    SAMPLE_WORKFLOW_FILE,
    TASKS_DIR,
    WORKFLOWS_DIR,
)
from nornflow.cli.exceptions import CLIInitError
from nornflow.cli.show import show_catalog, show_nornflow_settings
from nornflow.exceptions import NornFlowError

app = typer.Typer()


@app.command()
def init(ctx: typer.Context) -> None:
    """
    Initialize NornFlow by setting up the necessary configuration files and directories.
    """
    try:
        # Setup builder based on context
        builder = setup_builder(ctx)

        # Display banner and get user confirmation
        if not get_user_confirmation():
            return

        # Setup main directory structure and configuration files
        setup_directory_structure()
        setup_nornflow_settings_file(ctx.obj.get("settings"))

        # Create required directories before building NornFlow to prevent initialization errors
        create_required_directories()

        # Build NornFlow to get settings with vars_dir
        nornflow = builder.build()

        # Setup sample content including vars directory from settings
        setup_sample_content(nornflow)

        # Show information about the initialized setup
        show_info_post_init(nornflow)

    except FileNotFoundError as e:
        CLIInitError(
            message=f"File not found: {e}",
            hint="Check that all required template files exist in the installation directory.",
            original_exception=e,
        ).show()
        raise typer.Exit(code=2)  # noqa: B904

    except PermissionError as e:
        CLIInitError(
            message=f"Permission denied: {e}",
            hint="Check that you have write permissions to the current directory.",
            original_exception=e,
        ).show()
        raise typer.Exit(code=2)  # noqa: B904

    except shutil.Error as e:
        CLIInitError(
            message=f"Error copying file: {e}",
            hint="There may be an issue with file permissions or the files already exist.",
            original_exception=e,
        ).show()
        raise typer.Exit(code=2)  # noqa: B904

    except NornFlowError as e:
        CLIInitError(
            message=f"NornFlow error: {e}",
            hint="There was an issue with the NornFlow configuration.",
            original_exception=e,
        ).show()
        raise typer.Exit(code=2)  # noqa: B904

    except Exception as e:
        CLIInitError(
            message=f"Unexpected error during initialization: {e}",
            hint="This may be a bug. Please report it if the issue persists.",
            original_exception=e,
        ).show()
        raise typer.Exit(code=2)  # noqa: B904


def create_required_directories() -> None:
    """Create all required directories before NornFlow initialization."""
    create_directory(TASKS_DIR)
    create_directory(WORKFLOWS_DIR)
    create_directory(FILTERS_DIR)

    # If vars_dir is different from default, it will be created later
    # based on the actual settings after NornFlow is built


def setup_builder(ctx: typer.Context) -> NornFlowBuilder:
    """Set up and configure the NornFlowBuilder."""
    builder = NornFlowBuilder()
    settings = ctx.obj.get("settings")
    if settings:
        builder.with_settings_path(settings)
    return builder


def get_user_confirmation() -> bool:
    """Display banner and get user confirmation to proceed."""
    display_banner()
    if not typer.confirm("Do you want to continue?", default=True):
        typer.secho("Initialization aborted.", fg=typer.colors.RED)
        return False
    return True


def setup_directory_structure() -> None:
    """Set up the main directory structure."""
    typer.secho(f"NornFlow will be initialized at {NORNIR_DEFAULT_CONFIG_DIR.parent}", fg=typer.colors.GREEN)

    if create_directory(NORNIR_DEFAULT_CONFIG_DIR):
        for item in SAMPLE_NORNIR_CONFIGS_DIR.iterdir():
            if item.is_dir():
                shutil.copytree(item, NORNIR_DEFAULT_CONFIG_DIR / item.name)
            else:
                shutil.copy(item, NORNIR_DEFAULT_CONFIG_DIR / item.name)
        typer.secho(
            f"Created a sample 'nornir_configs' directory: {NORNIR_DEFAULT_CONFIG_DIR}",
            fg=typer.colors.GREEN,
        )


def setup_nornflow_settings_file(settings: str) -> None:
    """Set up the NornFlow settings file."""
    if not os.getenv("NORNFLOW_SETTINGS"):
        if not settings and not NORNFLOW_SETTINGS.exists():
            shutil.copy(SAMPLE_NORNFLOW_FILE, NORNFLOW_SETTINGS)
            typer.secho(f"Created a sample 'nornflow.yaml': {NORNFLOW_SETTINGS}", fg=typer.colors.GREEN)
        elif settings:
            typer.secho(f"Trying to use informed settings file: {settings}", fg=typer.colors.YELLOW)
        else:
            typer.secho(f"Settings file already exists: {NORNFLOW_SETTINGS}", fg=typer.colors.YELLOW)


def setup_sample_content(nornflow: NornFlow) -> None:
    """Set up sample tasks, workflows, filters, and vars directories."""
    # Copy sample files to the already created directories
    copy_sample_files_to_dir(
        TASKS_DIR, [HELLO_WORLD_TASK_FILE, GREET_USER_TASK_FILE], "Created sample tasks in directory: {}"
    )

    copy_sample_files_to_dir(
        WORKFLOWS_DIR, [SAMPLE_WORKFLOW_FILE], "Created a sample 'hello_world' workflow in directory: {}"
    )

    # Use vars_dir from NornFlow settings instead of hardcoded constant
    vars_dir = Path(nornflow.settings.vars_dir)
    create_directory_and_copy_sample_files(
        vars_dir, [SAMPLE_VARS_FILE], "Created a sample 'defaults.yaml' in vars directory: {}"
    )


def copy_sample_files_to_dir(dir_path: Path, sample_files: list[Path], sample_message: str) -> None:
    """Copy sample files to an existing directory."""
    for sample_file in sample_files:
        shutil.copy(sample_file, dir_path / sample_file.name)
    typer.secho(sample_message.format(dir_path), fg=typer.colors.GREEN)


def create_directory_and_copy_sample_files(
    dir_path: Path, sample_files: list[Path], sample_message: str
) -> None:
    """
    Create a directory if it doesn't exist and copy sample files into it.

    Args:
        dir_path (Path): The path of the directory to create.
        sample_files (list[Path]): The list of sample files to copy into the directory.
        sample_message (str): The message to display after copying the sample files.
    """
    if create_directory(dir_path):
        for sample_file in sample_files:
            shutil.copy(sample_file, dir_path / sample_file.name)
        typer.secho(sample_message.format(dir_path), fg=typer.colors.GREEN)


def create_directory(dir_path: Path) -> bool:
    """Create a directory if it doesn't exist.

    Args:
        dir_path (Path): The path of the directory to create.

    Returns:
        bool: True if the directory was created, False if it already existed.
    """
    if not dir_path.exists():
        dir_path.mkdir(parents=True, exist_ok=True)
        typer.secho(f"Created directory: {dir_path}", fg=typer.colors.GREEN)
        return True
    typer.secho(f"Directory already exists: {dir_path}", fg=typer.colors.YELLOW)
    return False


def display_banner() -> None:
    """
    Display a banner message with borders.
    """
    # Print the ASCII banner first in purple
    typer.secho(INIT_BANNER, fg=typer.colors.MAGENTA)

    banner_message = (
        "The 'init' command creates directories, and samples for configs, tasks and\n"
        "workflows files, all with default values that you can modify as desired.\n"
        "No customization of 'init' parameters available yet.\n\nDo you want to continue?"
    )
    lines = banner_message.split("\n")
    max_length = max(len(line) for line in lines)
    border = "+" + "-" * (max_length + 2) + "+"
    typer.secho(border, fg=typer.colors.CYAN, bold=True)
    for line in lines:
        padded_line = line + " " * (max_length - len(line))
        typer.secho(f"| {padded_line} |", fg=typer.colors.CYAN, bold=True)
    typer.secho(border, fg=typer.colors.CYAN, bold=True)


def show_info_post_init(nornflow: NornFlow) -> None:
    """
    Display all information about NornFlow, equivalent to running 'nornflow show --all'.
    """
    show_nornflow_settings(nornflow)
    show_catalog(nornflow)
