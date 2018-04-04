import unittest
import random

from radix_sort import *

class LSDRadixSortTest(unittest.TestCase):
    def test_radix_sort_simple(self):
        arr = [3, 2, 1]
        self.assertEqual(
            radix_sort(arr),
            sorted(arr)
        )

    def test_radix_sort_complex(self):
        arr = [170, 45, 75, 90, 2, 802, 2, 66]
        self.assertEqual(
            radix_sort(arr),
            sorted(arr)
        )

    def test_radix_sort_complex_random(self):
        arr = random.sample(range(1000), 100)
        self.assertEqual(
            radix_sort(arr),
            sorted(arr)
        )

    def test_radix_sort_similar_digits(self):
        arr = [10000, 1000, 100, 10, 0]
        self.assertEqual(
            radix_sort(arr),
            sorted(arr)
        )

class MSDRadixSortTest(unittest.TestCase):
    def test_msd_radix_sort_simple(self):
        arr = [3, 2, 1]
        max_digits = len(str(max(arr)))
        self.assertEqual(
            msd_radix_sort(arr, max_digits - 1),
            sorted(arr)
        )

    def test_msd_radix_sort_complex(self):
        arr = [170, 45,75, 810, 90, 2, 802, 2, 66]
        max_digits = len(str(max(arr)))
        self.assertEqual(
            msd_radix_sort(arr, max_digits - 1),
            sorted(arr)
        )

    def test_msd_radix_sort_complex_random(self):
        arr = random.sample(range(1000), 100)
        max_digits = len(str(max(arr)))
        self.assertEqual(
            msd_radix_sort(arr, max_digits - 1),
            sorted(arr)
        )

    def test_msd_radix_sort_similar_digits(self):
        arr = [10000, 1000, 100, 10, 0]
        max_digits = len(str(max(arr)))
        self.assertEqual(
            msd_radix_sort(arr, max_digits - 1),
            sorted(arr)
        )



if __name__ == "__main__":
    unittest.main()
