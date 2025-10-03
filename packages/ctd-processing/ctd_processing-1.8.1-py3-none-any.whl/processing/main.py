import importlib.metadata
import logging
import sys
from pathlib import Path

from platformdirs import user_log_dir

try:
    import typer
except ImportError:
    raise ImportError(
        "The 'ctdpro' extra is required to use this feature. Install with: pip install ctd-processing[ctdpro]"
    )

from seabirdfilehandler import CnvFile, HexCollection

from processing.procedure import Procedure
from processing.settings import Configuration
from processing.utils import default_seabird_exe_path

logger = logging.getLogger(__name__)


APPNAME = "ctdpro"
log_file_path = (
    Path(user_log_dir(APPNAME)).joinpath(APPNAME).with_suffix(".log")
)
app = typer.Typer()


@app.callback()
def common(
    ctx: typer.Context,
    verbose: bool = typer.Option(
        False, "--verbose", "-v", help="Enable verbose output."
    ),
):
    ctx.obj = {"verbose": verbose}
    if not log_file_path.exists():
        log_file_path.parent.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.DEBUG if verbose else logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler(),
        ],
    )


@app.command()
def run(
    processing_target: str = typer.Argument(
        "",
        help="The target file to process.",
    ),
    path_to_configuration: str = typer.Argument(
        "processing_config.toml",
        help="The path to the configuration file.",
    ),
    procedure_fingerprint_directory: str = typer.Option(
        "",
        "--fingerprint",
        "-f",
        help="The path to a fingerprint directory. If none given, no fingerprints will be created.",
    ),
    file_type_dir: str = typer.Option(
        "",
        "--file-type",
        "-t",
        help="The path to a file type directory. If none given, the files will not be separated into file type directories.",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="An option to allow more verbose output.",
    ),
):
    """
    Processes one target file using the given procedure workflow file.
    """
    path_to_config = Path(path_to_configuration)
    if path_to_config.exists():
        config = Configuration(path_to_config)
    else:
        sys.exit("Could not find the configuration file.")
    config["input"] = processing_target
    Procedure(
        configuration=config,
        procedure_fingerprint_directory=procedure_fingerprint_directory,
        file_type_dir=file_type_dir,
        verbose=verbose,
    )


@app.command()
def convert(
    input_dir: str = typer.Argument(
        ...,
        help="The data directory with the target .hex files.",
    ),
    psa_path: str = typer.Argument(
        ...,
        help="The path to the .psa for datcnv.",
    ),
    output_dir: str = typer.Option(
        "",
        "--output",
        "-o",
        help="The directory to store the converted .cnv files in.",
    ),
    xmlcon_dir: str = typer.Option(
        "",
        "--xmlcons",
        "-x",
        help="The directory to look for .xmlcon files.",
    ),
    pattern: str = typer.Option(
        "",
        "--pattern",
        "-p",
        help="A name pattern to filter the target .hex files with.",
    ),
) -> list[Path]:
    """
    Converts a list of Sea-Bird raw data files (.hex) to .cnv files.
    Does either use an explicit list of paths or searches for all .hex files in
    the given directory.
    """
    if not output_dir:
        output_dir = input_dir
    if not xmlcon_dir:
        xmlcon_dir = input_dir
    hexes = HexCollection(
        path_to_files=input_dir,
        pattern=pattern,
        file_suffix="hex",
        path_to_xmlcons=xmlcon_dir,
    )
    resulting_cnvs = []
    proc_config = {
        "output_dir": output_dir,
        "modules": {
            "datcnv": {"psa": psa_path},
        },
    }
    procedure = Procedure(
        proc_config,
        auto_run=False,
        verbose=True if len(hexes) == 1 else False,
    )
    with typer.progressbar(hexes, label="Converting files:") as progress:
        for hex in progress:
            try:
                result = procedure.run(hex.path_to_file)
            except Exception as e:
                logger.error(f"Failed to convert: {hex.path_to_file}, {e}")
            else:
                resulting_cnvs.append(result)
    return resulting_cnvs


@app.command()
def batch(
    input_dir: str = typer.Argument(
        ...,
        help="The data directory with the target files.",
    ),
    config: str = typer.Argument(
        ...,
        help="Either an explicit config as dict or a path to a .toml config file.",
    ),
    pattern: str = typer.Option(
        ".cnv",
        "--pattern",
        "-p",
        help="A name pattern to filter the target files with.",
    ),
) -> list[Path] | list[CnvFile]:
    """
    Applies a processing config to multiple .hex or. cnv files.
    """
    resulting_cnvs = []
    if isinstance(config, dict):
        proc_config = config
    else:
        proc_config = Configuration(config)
    procedure = Procedure(proc_config, auto_run=False)
    with typer.progressbar(
        Path(input_dir).rglob(f"*{pattern}*"), label="Processing files:"
    ) as progress:
        for file in progress:
            try:
                result = procedure.run(file)
            except Exception as e:
                logger.error(f"Error when processing {file}: {e}")
            else:
                resulting_cnvs.append(result)
    return resulting_cnvs


try:
    from processing.gui.procedure_config_view import run_gui
except ImportError:
    pass
else:

    @app.command()
    def edit(file: str):
        """
        Opens a procedure workflow file in GUI for editing.
        """
        run_gui(file)


@app.command()
def show(file: typer.FileText):
    """
    Display the contents of a procedure workflow file.
    """
    content = file.read()
    print(content, end="")


@app.command()
def check():
    """
    Assures that all requirements to use this tool are met.
    """
    if not default_seabird_exe_path().exists():
        print(
            "You are missing a Sea-Bird Processing installation or are not using the default path. Please ensure that a valid installation can be found in Program Files (x86)/Sea-Bird/SBEDataProcessing-Win32/"
        )
    print("All set, you are ready to go.")


@app.command()
def log(
    number_of_entries: int = typer.Argument(
        30, help="The number of entries to print."
    ),
):
    """
    Prints the last x entries of the log file.
    """
    if not log_file_path.exists():
        return
    lines = log_file_path.read_text().splitlines()
    last_x_lines = lines[-number_of_entries:]
    for line in last_x_lines:
        print(line)


@app.command()
def version():
    """
    Displays the version number of this software.
    """
    print(importlib.metadata.version("ctd-processing"))


if __name__ == "__main__":
    app()
