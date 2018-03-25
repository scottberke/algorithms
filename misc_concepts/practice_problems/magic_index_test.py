import unittest
from magic_index import *

class MagicIndexTest(unittest.TestCase):
    def test_magic_index(self):
        arr = [ -1, 0, 1, 2, 4, 6 ] # arr[4] = 4
        self.assertEqual(
            magic_index(arr, 0, len(arr) - 1),
            4
        )

    def test_magic_index_not_found(self):
        arr = [ -1, 0, 1, 2, 5, 6 ]
        self.assertFalse(
            magic_index(arr, 0, len(arr) - 1)
        )

    def test_magic_index_bigger(self):
        arr = [-9, -4, -1, 0, 1, 2, 6, 8, 9, 15, 20 ] # arr[6] = 6
        self.assertEqual(
            magic_index(arr, 0, len(arr) - 1),
            6
        )

if __name__ == "__main__":
    unittest.main()
