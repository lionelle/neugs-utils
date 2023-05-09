"""
A simple tool set developed for non-traditional grading and other grading 
tools within the grade-scope autograder environment.

Features:
    Tier Mastery Grading: 
    Focuses on mastery based grading in grading tiers, meaning
    grades are corrected, so only the tests are passed in order based on groups. If any
    test in a group stops, so does all grading until the previous group is fixed. 

    Common tiers are (COMMON_ONE, COMMON_TWO, COMMON_THREE, COMMON_FOUR) which is
    "Learning", "Approaching", "Meets", "Exceeds". To tag a test in a tier use the
    tier decorator. An example of a common test setup with tier grading would be as follows

    Example:
    from gradescope_utils.autograder_utils.decorators import number, tags
    from neugs_utils import tier, COMMON_ONE, COMMON_TWO, COMMON_THREE

    class TestOne(unittest.TestCase):
        @tier(COMMON_THREE)
        @tags("Learning")  #tags should come *after* tiers if they are used at all
        @number(3.0)
        def test_random(self):
            result = 6
            for i in (6, 5, 61):
                self.assertEqual(result, i, "this is my message, that display due to TWO failing")

        @tier(COMMON_TWO)
        @number(2.0)
        def test_approaching(self):
            result = 3
            self.assertEqual(result, 5, "this should fail")

        @tier(COMMON_TWO)
        @number(2.0)
        def test_some_other_approaching(self):
            result = 5
            self.assertEqual(result, 5, "this should pass")

        @tier(COMMON_ONE)
        @number(1.0)
        def test_valid(self):
            self.assertEqual(5, 5, "really!")

        @tier(COMMON_ONE)
        @number(1.1)
        def test_valid2(self):
            self.assertEqual(6, 6, "really!")

    Given the example above, and assuming default points of 1 point per tier, the above student would earn
    1 point, and will be encouraged to submit again to completed Tier Two and Tier 3

    In run_test.py make sure to change JSONTestRunner to TierMasteryJSONTestRunner
        
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        TierMasteryJSONTestRunner(visibility='visible', stream=f).run(suite)

Utilities:
    There are also a number of additional utility functions added in common_tests.py and context_managers.py.
    These are meant to be for utility to help with common grading tasks. 


This module is still in early stages of development! 

Todo:
    * Add standards based grading / tagging

"""


from typing import Union, List, Tuple, Set, Any
from .tier_grading import TierMasteryJSONTestRunner, tier, \
    COMMON_ONE, COMMON_TWO, COMMON_THREE, COMMON_FOUR


__version__ = "0.0.6"


def common_msg(msg : str, expected : Any, actual : Any) -> str:
    """Generates a common message format of 
       msg
         expected: val
         actual:  val

    Args:
        msg (str): An informative message for the student
        expected (Any): the expected value
        actual (Any): the actual value

    Returns:
        str: a string formatted for student view
    """
    return f"{msg}\n\tExpected: {expected}\n\t  Actual: {actual}"


def strip_prompt(prompt: str, outputs: Tuple[str]) -> List[str]:
    """Removes prompts from every output line provided

    Args:
        prompt (str): the prompt to remove (needs to be exact)
        outputs (Tuple[str]): the output line

    Returns:
        List[str]: a list of outputs with the prompts removed
    """
    return [output.replace(prompt, '').strip() if prompt in output else output for output in outputs]


def strip_prompts(prompts: Set[str], outputs: Tuple[str]) -> List[str]:
    """Removes a set of prompts from every output line as found

    Args:
        prompts (Set[str]): a list of prompts to remove
        outputs (Tuple[str]): a list of output lines

    Returns:
        List[str]: a set of output lines with prompts removed
    """
    out = list(outputs)
    for prompt in prompts:
        out = strip_prompt(prompt, tuple(out))
    return out
