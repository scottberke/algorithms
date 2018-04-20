import unittest
import random

from algorithms.sort.selection_sort import *

class SelectionSortTest(unittest.TestCase):
    def test_selection_sort_simple_even(self):
        arr = [4, 3, 2, 1]
        arr_copy = arr[::]
        arr_copy.sort()
        self.assertEqual(
            selection_sort(arr),
            arr_copy
        )

    def test_selection_sort_simple_odd(self):
        arr = [5, 4, 3, 2, 1]
        arr_copy = arr[::]
        arr_copy.sort()
        self.assertEqual(
            selection_sort(arr),
            arr_copy
        )

    def test_selection_sort_large(self):
        arr = random.sample(range(500), 500)
        arr_copy = arr[::]
        arr_copy.sort()
        self.assertEqual(
            selection_sort(arr),
            arr_copy
        )


if __name__ == "__main__":
    unittest.main()
