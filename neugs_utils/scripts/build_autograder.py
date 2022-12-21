"""
Support script for building autograders.
"""
import click
from zipfile import ZipFile
import os
from typing import List, Union, Tuple


def get_all_file_paths(directory : str) -> List[str]:
    """
        Grabs all the files in the directory provided, to write them out to the tests directory.
        While it will get files in sub directories, it does not currently handle
        keeping those subdirectories when writing!
    Args:
        directory (str): directory to scan

    Returns:
        List[str]: a list of files found
    """
    # initializing empty file paths list
    file_paths = []

    # crawling through directory and subdirectories
    for root, directories, files in os.walk(directory):
        for filename in files:
            if "__" in root: continue # skip special python directories TODO: improve this!
            # join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    # returning all file paths
    return file_paths

def new_test_loc(file: str) -> str:
    """converts a file found to be put into the tests directory
    TODO: this function should be updated to be more flexible.
    Args:
        file (str): the file to convert path to tests directory in the zip

    Returns:
        str: tests/file
    """
    return "tests/" + os.path.basename(file)


def check_or_get(file : str, override:List[str]) -> Tuple[str, str]:
    """Checks to see if the file is in the override list, else
    provides a default file from the templates directory
    Args:
        file (str): the file to process
        override (List[str]): the override list of files

    Returns:
        Tuple[str, str]: name of the file to write, and the path to the file
    """
    for f in override:
        if file in f:
            return (f, f)
    # not found use common list
    dirname = os.path.dirname(__file__)
    return (file, os.path.join(dirname, f"templates/{file}"))

@click.command()
@click.option("--out", "-o", default="autograder.zip")
@click.argument("dir")
@click.argument("override", nargs=-1)
def build_autograder(out: str, dir: str, override: List[str]):
    """Commandline tool for generating autograder_files. For the most part
    the default execution will work. Reads files in dir, addes them 
    to a zipfile (out), and can add some of the standard four autograder files
    incase they want to be replaced
    Args:
        out (str): file to save
        dir (str): tests directory
        override (Union[List[str], None]): List of files to replace the default autograder files, names must match
    """
    paths = get_all_file_paths(dir)
    common_files_default = ("requirements.txt", "run_autograder", "run_tests.py", "setup.sh")


    with ZipFile(out, 'w') as zip:
        for file in paths:
            zip.write(file, arcname=new_test_loc(file))
        for file in common_files_default:
            name, full = check_or_get(file, override)
            zip.write(full, arcname=name)


if __name__ == "__main__":
    build_autograder()





