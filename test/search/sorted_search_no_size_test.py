import unittest
import random
from sorted_search_no_size import *


class SortedSearchNoSizeTest(unittest.TestCase):
    def test_sorted_search_found(self):
        length = random.randint(1, 100)
        arr = Listy(sorted(random.sample(range(100), length)))
        index = random.randint(1, length)
        self.assertEqual(
            listy_search(arr, arr[index]),
            index
        )

    def test_sorted_search_not_found(self):
        length = random.randint(1, 100)
        arr = Listy(sorted(random.sample(range(100), length)))
        value = random.randint(100, 200)
        self.assertFalse(
            listy_search(arr, value)
        )

if __name__ == "__main__":
    unittest.main()
