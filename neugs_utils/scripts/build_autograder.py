"""
Support script for building autograders.
"""
import click
from zipfile import ZipFile
import os
from typing import List, Union, Tuple, Dict, Any
import neugs_utils.scripts.templates as templates


def get_config_files(config: Dict[str, Any]) -> Dict[str, str]:
    """Based on config settings, builds the four
    autograder required files:
        requirements.txt
        run_autograder
        run_tests.py
        setup.sh

    Args:
        config (Dict[str, Any]): config settings

    Returns:
        Dict[str, str]: file name, and contents.
    """
    config_files = {}
    config_files["requirements.txt"] = templates.get_template("requirements.txt")
    config_files["run_autograder"] = templates.get_template("run_autograder")
    config_files["setup.sh"] = templates.build_setup(config)
    config_files["run_tests.py"] = templates.build_runner(config)
    return config_files


def get_all_file_paths(directory: str) -> List[str]:
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
            if "__" in root:
                continue  # skip special python directories TODO: improve this!
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


@click.command()
@click.option(
    "--out",
    "-o",
    default="autograder.zip",
    show_default=True,
    help="The file name of the autograder.",
)
@click.option(
    "--test-dir",
    "-d",
    default="tests",
    show_default=True,
    help="The directory to pull tests from.",
)
@click.option(
    "--cpp", default=False, is_flag=True, help="Add C/CPP compiler to setup files."
)
@click.option(
    "--grading-type",
    "-t",
    default="mastery",
    show_default=True,
    help="Grading types allowed [mastery, standard]",
)
@click.option(
    "--test-only",
    is_flag=True,
    default=False,
    help="Print out feedback, but don't build zip.",
)
def build_autograder(
    out: str, test_dir: str, cpp: bool, grading_type: str, test_only: bool
) -> None:
    """Command line tool for generating autograder_files. For the most part
    the default execution will work. Reads files in dir, addes them
    to a zipfile (out), and can add some of the standard four autograder files
    incase they want to be replaced
    Args:
        out (str): file to save
        dir (str): tests directory
        cpp (bool): include c/cpp compilers
        grading_type (str): mastery or standard
        test_only (bool): run system but don't write to zip file
    """
    paths = get_all_file_paths(test_dir)

    config = {"cpp": cpp, "gtype": grading_type.casefold()}

    with ZipFile(out, "w") as zip:
        for file in paths:
            if test_only:
                print(f"Testing: would be writing {file} to zip.")
            else:
                zip.write(file, arcname=new_test_loc(file))
        for file, contents in get_config_files(config).items():
            if test_only:
                print(f"...writing to zip {file} with \n{contents}")
            else:
                zip.writestr(data=contents, zinfo_or_arcname=file)



if __name__ == "__main__":
    build_autograder()
