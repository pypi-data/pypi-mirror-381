
# src\file_conversor\cli\multimedia\unsharp_cmd.py
import typer

from pathlib import Path
from typing import Annotated, List

from rich import print

# user-provided modules
from file_conversor.backend.image import PillowBackend
from file_conversor.cli.image._typer import FILTER_PANEL as RICH_HELP_PANEL
from file_conversor.cli.image._typer import COMMAND_NAME, UNSHARP_NAME

from file_conversor.config import Environment, Configuration, State, Log
from file_conversor.config.locale import get_translation

from file_conversor.utils import ProgressManager, CommandManager
from file_conversor.utils.typer_utils import InputFilesArgument, OutputDirOption, RadiusOption
from file_conversor.utils.validators import check_is_bool_or_none, check_path_exists, check_valid_options

from file_conversor.system.win.ctx_menu import WinContextCommand, WinContextMenu

# get app config
CONFIG = Configuration.get_instance()
STATE = State.get_instance()
LOG = Log.get_instance()

_ = get_translation()
logger = LOG.getLogger(__name__)

typer_cmd = typer.Typer()

EXTERNAL_DEPENDENCIES = PillowBackend.EXTERNAL_DEPENDENCIES


@typer_cmd.command(
    name=UNSHARP_NAME,
    rich_help_panel=RICH_HELP_PANEL,
    help=f"""
        {_('Applies unsharp mask to an image file.')}
    """,
    epilog=f"""
        **{_('Examples')}:**

        - `file_conversor {COMMAND_NAME} {UNSHARP_NAME} input_file.jpg -od D:/Downloads`

        - `file_conversor {COMMAND_NAME} {UNSHARP_NAME} input_file1.bmp -r 3`

        - `file_conversor {COMMAND_NAME} {UNSHARP_NAME} input_file.jpg -s 100 -t 15`        
    """)
def unsharp(
    input_files: Annotated[List[str], InputFilesArgument(PillowBackend)],

    radius: Annotated[int, RadiusOption()] = 2,

    strenght: Annotated[int, typer.Option("--strenght", "-s",
                                          help=f'{_("Unsharp strength, in percent")}',
                                          min=1,
                                          )] = 130,


    threshold: Annotated[int, typer.Option("--threshold", "-t",
                                           help=f'{_("Threshold controls the minimum brightness change that will be sharpened")}',
                                           min=1,
                                           )] = 4,

    output_dir: Annotated[Path, OutputDirOption()] = Path(),
):
    pillow_backend = PillowBackend(verbose=STATE['verbose'])

    def callback(input_file: Path, output_file: Path, progress_mgr: ProgressManager):
        logger.info(f"Processing '{output_file}' ... ")
        pillow_backend.unsharp_mask(
            input_file=input_file,
            output_file=output_file,
            radius=radius,
            percent=strenght,
            threshold=threshold,
        )
        progress_mgr.complete_step()

    cmd_mgr = CommandManager(input_files, output_dir=output_dir, overwrite=STATE["overwrite-output"])
    cmd_mgr.run(callback, out_stem="_unsharpened")

    logger.info(f"{_('Image unsharp')}: [green bold]{_('SUCCESS')}[/]")
