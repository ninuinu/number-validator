import unittest
from src.entities.Personnummer import Personnummer
from tests.testCases import valid_personnummer, invalid_personnummer

class TestPersonnummer(unittest.TestCase):
    def testPersonnummer(self):
        for i in valid_personnummer:
            self.assertTrue(Personnummer(i))

        for j in invalid_personnummer:
            self.assertRaises(Exception, Personnummer, j)

if __name__ == '__main__':
    unittest.main()
