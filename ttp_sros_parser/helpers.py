"""Helper Functions."""
import glob
import sys
import os


def create_folder(directory: str):
    """Create a folder.

    Args:
        directory (str): directory to create.
    """
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def globfindfile(regex):
    """Locate a file in the DIR by passing the regex value (ie:(*.log)).

    The returned value by calling the function is the file. If the path is passed in, the full path is returned back -
    not just the filename.

    Args:
        regex (str): Some regex pattern
    """
    try:
        files = list(glob.glob(regex))
        if len(files) == 0:
            sys.exit(f"No {regex} file found.")
        return files
    except Exception as err_mssg:
        print(f"Something went wrong, {err_mssg}")
