import os
import glob
from typing import List

from cabinet.consts import UTENSILS_DIR_FULL_PATH


def dir_parser(filename: str) -> List[str]:
    """
    Parses the utensils directory, defined as UTENSILS_DIR_FULL_PATH, and
    returns the
    """
    contents = glob.glob(f"{UTENSILS_DIR_FULL_PATH}/*")

    file_to_run: str

    for content in contents:
        if os.path.isfile(content) and filename in content:
            file_to_run = content

    if not file_to_run:
        raise FileNotFoundError("no utensil found with given input")

    return file_to_run
