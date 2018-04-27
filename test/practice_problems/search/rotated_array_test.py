import unittest
import random
from collections import *

from practice_problems.search.rotated_array import *

class RotatedArrayTest(unittest.TestCase):
    def create_rotated_array(self, skip=1, high=100):
        arr = deque(list(range(1, high, skip)))
        rotate_by = random.randint(1, high//2)
        arr.rotate(rotate_by)
        return list(arr)

    def test_rotated_array_found(self):
        arr = self.create_rotated_array()
        for i in arr:
            res = search_rotated_array(arr, 0, len(arr) - 1, i)
            self.assertEqual(
                res, i
            )

    def test_rotated_array_not_found(self):
        arr = self.create_rotated_array(skip=2) # only odd numbers
        even_num = 40
        res = search_rotated_array(arr, 0, len(arr) - 1, even_num )
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()
