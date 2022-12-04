from gradescope_utils.autograder_utils.files import check_submitted_files
import io, contextlib
import pycodestyle
from typing import Union, List
from ..neugs_utils import common_style_ignore_list

def check_files(student_files : List[str]) -> Union(str, None):
    """_summary_

    Args:
        student_files (List[str]): _description_
        None (_type_): _description_

    Returns:
        _type_: _description_
    """
    missing_files = check_submitted_files(student_files)
    if len(missing_files) != 0:
        return "Missing required files:\n\t" + " ".join(missing_files)
    return None


def check_style(student_files: List[str], ignore =common_style_ignore_list ) -> Union(str, None):
    """_summary_

    Args:
        None (_type_): _description_
        student_files (List[str], ignore, optional): _description_. Defaults to common_style_ignore_list )->Union(str.

    Returns:
        _type_: _description_
    """
    with io.StringIO() as buf, contextlib.redirect_stdout(buf):
        style_checker = pycodestyle.StyleGuide(ignore=ignore)
        report = style_checker.check_files(student_files)
        if report.total_errors != 0:
            return "\nDoes not pass the style checker:\n" + buf.getvalue()
        return None