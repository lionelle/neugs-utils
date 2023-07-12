# Getting Started

This page provides a quick overview of how to get started with neugs-utils, and a few examples of how to use it for your classes.

## Installation

To install neugs-utils, run the following command:

```bash
pip install neugs-utils
```

## Mastery Grading Example

To start off, create an empty file called ```example.rst```.  
Our Mastery grading has four Common tiers *(COMMON_ONE, COMMON_TWO, COMMON_THREE, COMMON_FOUR)* which correspond to "Learning", "Approaching", "Meets", "Exceeds".   
Add the following example of a common test setup with tier grading to your ```example.rst``` file.  
This example assumes default points of 1 point per tier, and so the student would earn 1 point, and will be encouraged to submit again to complete Tier Two and Tier 3


**Example:**
      
```
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


Ensure your ```conf.py``` has these extensions:

```
extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.coverage',
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',
    "sphinx.ext.githubpages",
    'sphinx.ext.autodoc',
    'myst_parser', # Markdown support for Sphinx
]
```


Add ```example.rst``` to the toctree directive in ```index.rst```. This tells Sphinx the hierarchy and relations between the files in your docs.


For more on how to get started with Sphinx, see the [quick-start guide](https://www.sphinx-doc.org/en/master/usage/quickstart.html)



### Building the Autograder.zip 

To build the autograder, you simply run it in the directory that contains your src and test directories. It will read and pull every file from your tests folder. You do not have to make a test runner, it will do that for you. 

```bash
neugs-build -o autograder.zip 
```

You will then upload the autograder.zip (or whatever you called it) to Gradescope. 


## Combing Autograding and Manual Grading

TODO: Albert to add this example using one of his courses.