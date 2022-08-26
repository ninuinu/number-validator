import unittest
from src.util.luhnsAlgorithm import luhnsAlgorithm


class TestLuhnsAlgorithm(unittest.TestCase):
    def testLuhnsAlgorithm(self):
        self.assertEqual(luhnsAlgorithm("2109099180"), 0)
        self.assertEqual(luhnsAlgorithm("200809032386"), 6)
        self.assertEqual(luhnsAlgorithm("9001189811"), 1)
        self.assertEqual(luhnsAlgorithm("0000000000"), 0)
        self.assertEqual(luhnsAlgorithm("0000100008"), 8)


if __name__ == '__main__':
    unittest.main()
