## Autogenerated runner by neugs_utils
import unittest
from neugs_utils import TierMasteryJSONTestRunner

if __name__ == '__main__':
    suite = unittest.defaultTestLoader.discover('tests')
    with open('results.json', 'w') as f:
        TierMasteryJSONTestRunner(visibility='visible', stream=f).run(suite)