import sys
import subprocess

from cabinet.parser import dir_parser


def main():
    all_args = sys.argv
    script_to_run = all_args[1]
    args = all_args[2:]

    utensil = dir_parser(script_to_run)

    try:
        subprocess.run(["python3", utensil, *args])
    except Exception:
        print("something went wrong")


if __name__ == "__main__":
    main()
