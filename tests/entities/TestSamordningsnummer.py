import unittest
from src.entities.Samordningsnummer import Samordningsnummer
from tests.testCases import valid_samordningsnummer, invalid_samordningsnummer

class TestSamordningsnummer(unittest.TestCase):
    def testPersonnummer(self):
        for i in valid_samordningsnummer:
            self.assertTrue(Samordningsnummer(i))

        for j in invalid_samordningsnummer:
            self.assertRaises(Exception, Samordningsnummer, j)

if __name__ == '__main__':
    unittest.main()
