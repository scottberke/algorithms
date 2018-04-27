import unittest

from practice_problems.sort.sorted_merge import *

class SortedMergeTest(unittest.TestCase):
    def test_merge(self):
        a = [1, 3, 5, 7, 9, 11, 32, 41]
        b = [2, 4, 6, 8, 15, 25, 52]
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 25, 32, 41, 52]

        self.assertEqual(
            merge(a, b),
            expected
        )

    def test_buffer_merge(self):
        a = [1, 3, 5, 7, None, None, None, None]
        b = [2, 4, 6, 8]
        expected = [1, 2, 3, 4, 5, 6, 7, 8]

        self.assertEqual(
            buffer_merge(a,b),
            expected
        )

    def test_merge_w_one_empty(self):
        a = [1, 3, 5, 7, 9, 11, 32, 41]
        b = []

        self.assertEqual(
            merge(a, b),
            a
        )


    def test_buffer_merge_w_one_empty(self):
        a = [1, 3, 5, 7, 9, 11, 32, 41]
        b = []

        self.assertEqual(
            buffer_merge(a, b),
            a
        )

if __name__ == '__main__':
    unittest.main()
