from gradescope_utils.autograder_utils.files import check_submitted_files
import io
import contextlib
import pycodestyle
from typing import List


# Developed by Mark Miller for Khoury Align SF campus use. Placed for easy access.

common_style_ignore_list = [
    'E121', # Continuation line under-indented for hanging indent
    'E126', # Continuation line over-indented for hanging indent
    'W291', # Trailing whitespace
    'W503', # Line break before binary operator
    'W504', # Line break after binary operator
    'E501' # Relaxing the line length due to comments commonly going over 80
    ]


def check_files(student_files : List[str]) -> str:
    """checks to see if the files exist in the submission

    Args:
        student_files (List[str]): the names of files to check for

    Returns:
        str: A string listing which files were missing, or the empty string if no files were missing.
    """
    missing_files = check_submitted_files(student_files)
    return "Missing required files:\n\t" + " ".join(missing_files) if len(missing_files) != 0 else ''


def check_style(student_files: List[str], ignore : List[str] = common_style_ignore_list ) -> str:
    """Runs the files against a style checker to make sure they match the recommended python styles. 

    Args:
        student_files (List[str]): The student files to run pycodestyle on
        ignore (List[str], ignore, optional): List of ignores to pass onto pycodestyle . Defaults to common_style_ignore_list

    Returns:
        str:  string  if any style did not pass the style checker, or empty string if everything passed fine 
    """
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        style_checker = pycodestyle.StyleGuide(ignore=ignore)
        report = style_checker.check_files(student_files)        
        return "\nDoes not pass the style checker:\n" + buf.getvalue() if report.total_errors != 0 else ''
