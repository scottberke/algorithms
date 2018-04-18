import unittest
import random

from recursive_multiply import *

class RecursiveMultiplyTest(unittest.TestCase):
    def test_recursive_multiply_simple(self):
        num1 = 2
        num2 = 2
        self.assertEqual(
            multiply(num1, num2),
            num1 * num2
        )

    def test_recursive_multiply_random(self):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        self.assertEqual(
            multiply(num1, num2),
            num1 * num2
        )

    def test_recursive_multiply_quicker_simple(self):
        num1 = 2
        num2 = 2
        self.assertEqual(
            multiply_quicker(num1, num2),
            num1 * num2
        )

    def test_recursive_multiply_quicker_random(self):
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)

        self.assertEqual(
            multiply_quicker(num1, num2),
            num1 * num2
        )



if __name__ == "__main__":
    unittest.main()
