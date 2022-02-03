import sys
import subprocess

from cabinet.tools import dir_parser, bin_resolver
from cabinet.consts import UTENSILS_DIR_FULL_PATH


def main():
    all_args = sys.argv
    command_to_run = all_args[1]
    args = all_args[2:]

    utensils = dir_parser(UTENSILS_DIR_FULL_PATH)

    if command_to_run in utensils.keys():
        binary = bin_resolver(utensils[command_to_run])

        if binary:
            subprocess.run([*binary, utensils[command_to_run]["path"], *args])
        else:
            print("filetype not supported")
    else:
        print("No utensils found")


if __name__ == "__main__":
    main()
