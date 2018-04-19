import unittest
import random

from algorithms.sort.quick_sort import *

class QuickSortTest(unittest.TestCase):
    def test_quick_sort_simple_even(self):
        arr = [4, 3, 2, 1]
        arr_copy = arr[::]
        arr_copy.sort()
        quick_sort(arr, 0, len(arr) - 1)
        self.assertEqual(
            arr,
            arr_copy
        )

    def test_quick_sort_simple_odd(self):
        arr = [5, 4, 3, 2, 1]
        arr_copy = arr[::]
        arr_copy.sort()
        quick_sort(arr, 0, len(arr) - 1),

        self.assertEqual(
            arr,
            arr_copy
        )

    def test_quick_sort_large(self):
        arr = random.sample(range(500), 500)
        arr_copy = arr[::]
        arr_copy.sort()
        quick_sort(arr, 0, len(arr) - 1),
        self.assertEqual(
            arr,
            arr_copy
        )


if __name__ == "__main__":
    unittest.main()
