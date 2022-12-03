import unittest
from gradescope_utils.autograder_utils.decorators import number, weight, tags

from neugs_utils import tier, COMMON_ONE, COMMON_TWO, COMMON_THREE
from random import randint


class TestOne(unittest.TestCase):
 
    @tier(COMMON_THREE)
    @tags("Learning")
    @number(3.0)
    def test_random(self):
        result = randint(0,100)
        for i in (6, 5, 61):
            self.assertEqual(result, i, "this is my message")

    @tier(COMMON_TWO)
    @number(2.0)
    def test_random2(self):
        result = randint(0,100)
        self.assertEqual(result, 5, "this is my message")

    @tier(COMMON_ONE)
    def test_valid(self):
        self.assertEqual(5, 5, "really!")

    @tier(COMMON_ONE)
    def test_valid2(self):
        self.assertEqual(6, 6, "really!")


if __name__ == '__main__':
    unittest.main()
