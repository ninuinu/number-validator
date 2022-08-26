import unittest
from src.entities.Organisationsnummer import Organisationsnummer
from tests.testCases import valid_organisationsnummer, invalid_organisationsnummer

class TestOrganisationsnummer(unittest.TestCase):
    def testPersonnummer(self):
        for i in valid_organisationsnummer:
            self.assertTrue(Organisationsnummer(i))

        for j in invalid_organisationsnummer:
            self.assertRaises(Exception, Organisationsnummer, j)

if __name__ == '__main__':
    unittest.main()
