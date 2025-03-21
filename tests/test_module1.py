# python -m unittest discover tests

import unittest
from Hazel.module1 import *

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(getage(), 46.07529089664613)

if __name__ == '__main__':
    unittest.main()
