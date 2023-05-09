import os
from .setup_file import build_setup
from .test_runner import build_runner


def get_template(filename: str) -> str:
    """Loads a template file into a string

    Args:
        filename (str): the file to load

    Returns:
        str: the file as a string
    """
    dirname = os.path.dirname(__file__)
    file = os.path.join(dirname, filename)

    f = open(file)
    contents = f.read()
    f.close()
    return contents
