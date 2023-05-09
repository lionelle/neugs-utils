import os
import sys
#up1 = os.path.abspath('../..')
#print("Add path for test purposes " + up1)
#sys.path.insert(0, up1)




import unittest
from gradescope_utils.autograder_utils.decorators import number, tags
from neugs_utils.context_managers import Capturing
from neugs_utils import tier, COMMON_ONE, COMMON_TWO, COMMON_THREE
from random import randint

def some_func():
    val = input("this is my input")
    print(f"this is your input: {val}\n{val}" )

class TestOne(unittest.TestCase):

    @tier(COMMON_ONE)
    def test_capture(self):
        with Capturing("hello") as output:
            some_func()
        self.assertEqual(output[1], "hello")
   
        

    @tier(COMMON_THREE)
    @tags("Learning")
    @number(3.0)
    def test_random(self):
        print("ehlleloe")
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
