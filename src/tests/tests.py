import unittest
import sys

sys.path.append("/sourcecode")
from modules.computer import Computer

class TestSum(unittest.TestCase):

    def test_sum(self):
        c = Computer(3,3)
        self.assertEqual(c.sum(), 6, "Should be 6")

    def test_multiply(self):
        c = Computer (3,3)
        self.assertEqual(c.multiply(), 9, "Should be 9")

if __name__ == '__main__':
    unittest.main()