""" Adds additional language support to the testing library
"""
from typing import List
import os
import subprocess

def c_compile(c_files: List[str], out_file:str = "a.out", force:bool = False, compiler="clang -Wall") -> str:
    """Compiles using the clang compiler by default. Will only compile if 
    the file doesn't already exist

    Args:
        c_files (List[str]): list of input files
        out_file (str, optional): _the file to save out. Defaults to "a.out".
        force (bool, optional): Force recompile even if it already exists. Defaults to False.
        compiler (str, optional): the compiler to use with arguments. Defaults to clang -Wall
    Returns:
        str: A list of warnings and errors if they happen.
    """
    if not os.path.isfile(out_file) or force:
        compile_command = compiler.split() + c_files + ["-o", out_file]
        compiled = subprocess.run(compile_command, capture_output=True)
        if (compiled.stderr):
            return "Code failed to compile or had warnings\n{0}".format(compiled.stderr.decode())
    return ''


def run_range(file:str, start : int , end: int) -> str:
        """Runs subprocess passing in start and end as the first two parameters 
        
        Args:
            file (str): the file / program to run
            start (int): test id of the start test
            end (int): test id of the end test
        Returns:
            str: items printed to stderr
        """
        command = subprocess.run([file, str(start), str(end)], capture_output=True)
        if (command.stderr):
            return command.stderr.decode()
        return ''