import unittest
from .language_support import make, c_run, c_compile
from typing import List, Optional
import os

class CUnitTest(unittest.TestCase):
    """ Wrapper for Python Unit Testing when testing a C program.

    Attributes:
        _out (str): The output file to be created. REQUIRED
        _make_file (str): The make file to use. If None, uses default.
        _files (List[str]): The files to compile. REQUIRED if not using make.
        _use_make (bool): Whether to use make or not. Default True.


    Raises:
        ValueError: _out is not implement/overridden
        ValueError: _files is not implemented/overridden if not using make

    Overrides:
        setUp: Compiles the code
        tearDownClass: Removes the output file
    """
    _out : str = None 
    _make_file : str = None
    _files : Optional[List[str]] = None
    _use_make : bool = True 

    def setUp(self) -> None:
        """Overrides setup to make it compile code as part of the setup."""
        if self._out is None:
            raise ValueError("Must set _out as a class variable")
        if self._make_file is False and self._files is None:
            raise ValueError("Must set _files if not using make")
        if self._use_make:
            if self._make_file is None:
                print("Using default make file.")
            results = make(self._out, self._make_file)
            self.check(results)
        else:
            results= {}
            results["stderr"] = c_compile(self._out, self._files)
            self.check(results)
        return super().setUp()
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the output file."""
        os.remove(cls._out)
        return super().tearDownClass()
    
    def check(self, results : dict) -> None:
        """Checks the results of the compilation."""
        if results["stderr"]:
            self.fail(results["stderr"])

    