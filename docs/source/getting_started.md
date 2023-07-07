# Getting Started

This page provides a quick overview of how to get started with neugs-utils, and a few examples of how to use it for your classes.

## Installation

To install neugs-utils, run the following command:

```bash
pip install neugs-utils
```

## Mastery Grading Example
TODO: start example here, describe what each part does and why, this is based off of the stuff you have in features but with some cleanup. 



### Building the Autograder.zip 

To build the autograder, you simply run it in the directory that contains your src and test directories. It will read and pull every file from your tests folder. You do not have to make a test runner, it will do that for you. 

```bash
neugs-build -o autograder.zip 
```

You will then upload the autograder.zip (or whatever you called it) to Gradescope. 


## Combing Autograding and Manual Grading

TODO: Albert to add this example using one of his courses.