import os
import shutil
from importlib.metadata import metadata
from typing import Annotated

import typer

from pipelex.exceptions import PipelexCLIError
from pipelex.libraries.library_config import LibraryConfig
from pipelex.tools.config.manager import config_manager

PACKAGE_NAME = __name__.split(".", maxsplit=1)[0]
PACKAGE_VERSION = metadata(PACKAGE_NAME)["Version"]


def do_init_libraries(directory: str = ".", overwrite: bool = False) -> None:
    try:
        target_dir = os.path.join(directory, "pipelex_libraries")
        os.makedirs(directory, exist_ok=True)

        library_config = LibraryConfig(config_dir_path=target_dir)
        library_config.export_libraries(overwrite=overwrite)

        if overwrite:
            typer.echo(f"✅ Successfully initialized pipelex libraries at '{target_dir}' (all files overwritten)")
        else:
            typer.echo(f"✅ Successfully initialized pipelex libraries at '{target_dir}' (only created non-existing files)")
    except Exception as exc:
        msg = f"Failed to initialize libraries at '{directory}': {exc}"
        raise PipelexCLIError(msg) from exc


def do_init_config(reset: bool = False) -> None:
    """Initialize pipelex configuration in the current directory."""
    config_template_dir = os.path.join(config_manager.pipelex_root_dir, "config_template")
    target_config_dir = config_manager.pipelex_config_dir

    os.makedirs(target_config_dir, exist_ok=True)

    try:
        copied_files: list[str] = []
        existing_files: list[str] = []

        def copy_directory_structure(src_dir: str, dst_dir: str, relative_path: str = "") -> None:
            """Recursively copy directory structure, handling existing files."""
            for item in os.listdir(src_dir):
                src_item = os.path.join(src_dir, item)
                dst_item = os.path.join(dst_dir, item)
                relative_item = os.path.join(relative_path, item) if relative_path else item

                if os.path.isdir(src_item):
                    os.makedirs(dst_item, exist_ok=True)
                    copy_directory_structure(src_item, dst_item, relative_item)
                elif os.path.exists(dst_item) and not reset:
                    existing_files.append(relative_item)
                else:
                    shutil.copy2(src_item, dst_item)
                    copied_files.append(relative_item)

        copy_directory_structure(config_template_dir, target_config_dir)

        # Report results
        if copied_files:
            typer.echo(f"✅ Copied {len(copied_files)} files to {target_config_dir}:")
            for file in sorted(copied_files):
                typer.echo(f"   • {file}")

        if existing_files:
            typer.echo(f"ℹ️  Skipped {len(existing_files)} existing files (use --reset to overwrite):")
            for file in sorted(existing_files):
                typer.echo(f"   • {file}")

        if not copied_files and not existing_files:
            typer.echo(f"✅ Configuration directory {target_config_dir} is already up to date")

    except Exception as exc:
        msg = f"Failed to initialize configuration: {exc}"
        raise PipelexCLIError(msg) from exc


# Typer group for init commands
init_app = typer.Typer(help="Initialization commands", no_args_is_help=True)


@init_app.command("libraries")
def init_libraries_cmd(
    directory: Annotated[str, typer.Argument(help="Directory where to create the pipelex_libraries folder")] = ".",
    overwrite: Annotated[bool, typer.Option("--overwrite", "-o", help="Warning: If set, existing files will be overwritten.")] = False,
) -> None:
    do_init_libraries(directory=directory, overwrite=overwrite)


@init_app.command("config")
def init_config_cmd(
    reset: Annotated[bool, typer.Option("--reset", "-r", help="Warning: If set, existing files will be overwritten.")] = False,
) -> None:
    do_init_config(reset=reset)
