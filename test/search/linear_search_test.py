import unittest
from algorithms.search.linear_search.linear_search import *
import random

class LinearSearchTest(unittest.TestCase):
    def test_linear_search_found(self):
        arr = [ random.randint(0,100) for i in range(25) ]
        target = arr[len(arr)//2]
        result = search(arr, target)
        self.assertEqual(
            target,
            arr[result]
        )


    def test_linear_search_not_found(self):
        arr = [ random.randint(0,100) for i in range(25) ]
        target = 101
        result = search(arr, target)
        self.assertFalse(
            result
        )

if __name__ == "__main__":
    unittest.main()
