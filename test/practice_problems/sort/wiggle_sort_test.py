import unittest
import random

from practice_problems.sort.wiggle_sort import *

class WiggleSortTest(unittest.TestCase):
    # Helpers
    def check_result(self, result):
        res = True
        for i in range(len(result)-1):
            first = result[i]
            second = result[i+1]
            if i%2 == 0:
                res = res and (first <= second)
            else:
                res = res and (first >= second)
        return res

    # Tests
    def test_wiggle_sort(self):
        nums = [3, 5, 2, 1, 6, 4]
        result = wiggle_sort(nums)
        self.assertTrue(
            self.check_result(result)
        )

    def test_wiggle_sort_larger_set(self):
        nums = random.sample(range(1,1000), 100)
        result = wiggle_sort(nums)
        self.assertTrue(
            self.check_result(result)
        )

    def test_wiggle_sort_all_same(self):
        nums = [3, 3, 3, 3, 3, 3]
        result = wiggle_sort(nums)
        self.assertTrue(
            self.check_result(result)
        )

if __name__ == "__main__":
    unittest.main()
