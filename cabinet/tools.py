import pathlib
import shutil

from typing import Dict, Union
from cabinet.consts import SUPPORTED_FILETYPES


def dir_parser(path_to_dir: str) -> Dict[str, Dict[str, str]]:
    """
    Parses the given directory, and returns the path, stem and suffix for files.
    """
    files = pathlib.Path(path_to_dir).resolve().glob("*.*")

    files_data = {}

    for file in files:
        files_data[f"{file.stem}"] = {
            "suffix": file.suffix,
            "path": file.as_posix(),
        }

    return files_data


def bin_resolver(file_data: Dict[str, str]) -> Union[str, None]:
    """
    Resolves the right binary to run the script.
    """
    file_suffix = file_data["suffix"]

    if file_suffix in SUPPORTED_FILETYPES.keys():
        commands = SUPPORTED_FILETYPES[file_suffix].split(" ")
        commands[0] = shutil.which(commands[0])

        return commands

    return None
