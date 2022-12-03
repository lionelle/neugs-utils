
import unittest
import sys
import os


if __name__ == '__main__':
    up1 = os.path.abspath('..')
    print("Add path for test purposes " + up1)
    sys.path.insert(0, up1)
    from neugs_utils import TierMasteryJSONTestRunner
    
    suite = unittest.defaultTestLoader.discover('examples')
    with open('results.json', 'w') as f:
        TierMasteryJSONTestRunner(visibility='visible', stream=f).run(suite)
