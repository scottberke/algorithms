import unittest
from algorithms.search.binary_search.binary_search import *
import random

class BinarySearchTest(unittest.TestCase):
    def test_iterative_binary_search_found(self):
        arr = [ random.randint(0,100) for i in range(25) ]
        target = arr[len(arr)//2]
        arr = sorted(arr)
        result = search(arr, target)
        self.assertEqual(
            target,
            arr[result]
        )


    def test_iterative_binary_search_not_found(self):
        arr = [ random.randint(0,100) for i in range(25) ]
        target = 101
        arr = sorted(arr)
        result = search(arr, target)
        self.assertFalse(
            result
        )

    def test_recursive_binary_search(self):
        arr = [ random.randint(0,100) for i in range(25) ]
        target = arr[len(arr)//2]
        arr = sorted(arr)
        result = recursive_search(arr, target)
        self.assertEqual(
            target,
            arr[result]
        )

if __name__ == "__main__":
    unittest.main()
