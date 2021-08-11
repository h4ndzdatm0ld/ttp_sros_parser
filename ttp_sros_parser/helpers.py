"""Helper Functions."""
import glob, sys, os


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def globfindfile(regex):
    """This function will simply locate a file in the DIR by passing the regex value (ie:(*.log))
    The returned value by calling the function is the file. If the path is passed in, the full path is returned back -
    not just the filename.
    """
    try:
        files = []
        if len(glob.glob(regex)) == 0:
            sys.exit(f"No {regex} file found.")
        else:
            # for file in glob.glob(regex):
            #     files.append(file)
            files = [file for file in glob.glob(regex)]
        return files

    except Exception as e:
        print(f"Something went wrong, {e}")
