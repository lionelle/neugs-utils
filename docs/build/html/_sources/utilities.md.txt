# Utility Scripts
The following scripts can aid in the process.

## neugs-add
```Usage: neugs-add [OPTIONS] OUT [MODULES]...```   

  Builds a new test file. Requires the file to write to, it is suggest to
  added a class, but not required, and suggested to add modules which match
  the student files  being tested. Currently defaults to a set of imports
  related to TierMastery grading.

  ### positional arguements  
  out (str): file to save to     
  cl (str): test class     
  modules(List[str]): files to import (usually student files) 

  ### options
  -c, --cl TEXT    
  --help         Show this message and exit.   

  ### example    
  ```Example: neugs-add -c TestSimpleCalc tests/test_simple_calc.py```   

  Will result in the creation of a new test file ```test_simple_calc.py``` under the ```test``` sub-directory.         
  Note that ```TestSimpleCalc``` is the test class.      


  
## neugs-build
```Usage: neugs-build [OPTIONS]``` 

  Command line tool for generating autograder_files. For the most part the
  default execution will work. Reads files in dir, adds them to a zipfile
  (out), and can add some of the standard four autograder files incase they
  want to be replaced   

  ### positional arguements      
  out (str): file to save     
  dir (str): tests directory     
  cpp (bool): include c/cpp compilers     
  grading_type (str): mastery or standard     
  test_only (bool): run system but don't write to zip file

  ### options
  -o, --out TEXT           The file name of the autograder.  [default:
                           autograder.zip]   
  -d, --test-dir TEXT      The directory to pull tests from.  [default: tests]   
  --cpp                    Add C/CPP compiler to setup files.   
  -t, --grading-type TEXT  Grading types allowed [mastery, standard]
                           [default: mastery]   
  --test-only              Print out feedback, but don't build zip.   
  --help                   Show this message and exit.     

  ### example    
  ```Example: neugs-build tests```     
     
  This will create an autograder.zip with all your tests and files needed.   
  Upload the autograder to Gradescope.    




