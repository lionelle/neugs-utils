
import unittest
import sys
import os
from neugs_utils import TierMasteryJSONTestRunner

if __name__ == '__main__':
    #up1 = os.path.abspath('..')
    #print("Add path for test purposes " + up1)
    #sys.path.insert(0, up1)
   
    suite = unittest.defaultTestLoader.discover('tests/examples')
    with open('results.json', 'w') as f:
        TierMasteryJSONTestRunner(visibility='visible', stream=f).run(suite)
