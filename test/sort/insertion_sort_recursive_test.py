import unittest
import random

from algorithms.sort.insertion_sort_recur import *

class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort_simple_even(self):
        arr = [4, 3, 2, 1]
        arr_copy = arr[::]
        arr_copy.sort()
        self.assertEqual(
            insertion_sort(arr),
            arr_copy
        )

    def test_insertion_sort_simple_odd(self):
        arr = [5, 4, 3, 2, 1]
        arr_copy = arr[::]
        arr_copy.sort()
        self.assertEqual(
            insertion_sort(arr),
            arr_copy
        )

    def test_insertion_sort_large(self):
        arr = random.sample(range(500), 500)
        arr_copy = arr[::]
        arr_copy.sort()
        self.assertEqual(
            insertion_sort(arr),
            arr_copy
        )


if __name__ == "__main__":
    unittest.main()
