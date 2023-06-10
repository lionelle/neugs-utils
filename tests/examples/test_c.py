import os
import sys
#up1 = os.path.abspath('../..')
#print("Add path for test purposes " + up1)
#sys.path.insert(0, up1)




import unittest
from gradescope_utils.autograder_utils.decorators import number, tags
from neugs_utils.context_managers import Capturing
from neugs_utils import tier, COMMON_ONE, COMMON_TWO, COMMON_THREE
from neugs_utils.language_support import c_compile, c_run
from typing import List, Dict


class TestC(unittest.TestCase):
    _out: str = "examples/test_c.out"
    _files: List[str] = ["-f", "Makefile"]

    def setUp(self) -> None:
        results = {}
        results["stderr"] = c_compile(self._files, self._out, compiler="make")
        self.check(results)
        return super().setUp()

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove(TestC._out)
        return super().tearDownClass()


    def check(self, results: Dict) -> None:
        if results["stderr"]:
            self.fail(results["stderr"])

    @tier(COMMON_ONE)
    @number(1.0)
    def test_unlimited_loop(self) -> None:
        """Tests an unlimited loop / timeout exception"""
        results = c_run(self._out, args=[1])
        print(results)
        self.check(results)

    @tier(COMMON_ONE)
    @number(1.0)
    def test_segfault(self) -> None:
        """Testing seg fault"""
        results = c_run(self._out, args=[2])
        print(results)
        self.check(results)
