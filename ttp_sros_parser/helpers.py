"""Helper Functions."""
import glob
import sys
from pathlib import Path


def globfindfile(regex):
    """Locate a file in the DIR by passing the regex value (ie:(*.log)).

    The returned value by calling the function is the file. If the path is passed in, the full path is returned back -
    not just the filename.

    Args:
        regex (str): Some regex pattern
    """
    files = list(glob.glob(regex))
    if len(files) == 0:
        sys.exit(f"No {regex} file found.")
    return files


def check_file(file: str):
    """Check file exists."""
    file_path = Path(file)

    if not file.endswith((".cfg", ".txt", ".log")):
        raise ValueError(f"{file_path} must end with '.cfg', '.txt' or '.log'")
    if not file_path.exists():
        raise SystemExit(f"{file_path} doesn't exist.")
    return file
