import sys
from pathlib import Path
sys.path.insert(0, str(Path.cwd().parent))

import unittest
from entities.TestPersonnummer import TestPersonnummer
from entities.TestSamordningsnummer import TestSamordningsnummer
from entities.TestOrganisationsnummer import TestOrganisationsnummer

from util.TestLuhnsAlgorithm import TestLuhnsAlgorithm

class TestSuite:
    def runTests(self):
        t1 = unittest.TestLoader().loadTestsFromTestCase(TestPersonnummer)
        t2 = unittest.TestLoader().loadTestsFromTestCase(TestSamordningsnummer)
        t3 = unittest.TestLoader().loadTestsFromTestCase(TestOrganisationsnummer)
        t4 = unittest.TestLoader().loadTestsFromTestCase(TestLuhnsAlgorithm)

        testSuite = unittest.TestSuite([t1, t2, t3, t4])

        unittest.TextTestRunner().run(testSuite)

if __name__ == '__main__':
    unittest.main()
