# Northeastern University Grade Scope Utility 

In progress gradescope utility used for alternative grading schemes, including mastery grading and standards grading. Additionally, contains utility functions used to make the grading process easier.

## Features

### Tier Mastery Grading: 

Focuses on mastery based grading in grading tiers, meaning
grades are corrected, so only the tests are passed in order based on groups. If any
test in a group stops, so does all grading until the previous group is fixed. 

Common tiers are (COMMON_ONE, COMMON_TWO, COMMON_THREE, COMMON_FOUR) which is
"Learning", "Approaching", "Meets", "Exceeds". To tag a test in a tier use the
tier decorator. An example of a common test setup with tier grading would be as follows


#### Example:

```python
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
```

Given the example above, and assuming default points of 1 point per tier, the above student would earn
1 point, and will be encouraged to submit again to completed Tier Two and Tier 3


In run_test.py make sure to change JSONTestRunner to TierMasteryJSONTestRunner
```python        
    
import unittest
from neugs_utils import TierMasteryJSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('/autograder/results/results.json', 'w') as f:
        TierMasteryJSONTestRunner(visibility='visible', stream=f).run(suite)
```

### Utilities:

There are also a number of additional utility functions added in common_tests.py and context_managers.py. These are meant to be for utility to help with common grading tasks. 


This module is still in early stages of development! 
