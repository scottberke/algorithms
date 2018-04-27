import unittest

from practice_problems.misc_concepts.robot_in_grid import *

class RobotInGridTest(unittest.TestCase):
    def test_path_1(self):
        grid = [ [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 0], ]

        only_path = [(0,0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]

        self.assertEqual(
            find_path(grid),
            only_path
        )

    def test_path_2(self):
        grid = [ [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 0] ]

        only_path = [(0,0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3)]

        self.assertEqual(
            find_path(grid),
            only_path
        )

    def test_path_not_found(self):
        grid = [ [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0], ]

        self.assertFalse(
            find_path(grid)
        )

    def test_path_rec_1(self):
        grid = [ [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 0],
                 [0, 0, 0, 0], ]

        only_path = [(0,0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]

        self.assertEqual(
            find_path_recursive(grid),
            only_path
        )

    def test_path_rec_2(self):
        grid = [ [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 0],
                 [0, 0, 1, 0],
                 [0, 0, 0, 0] ]

        only_path = [(0,0), (1, 0), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3), (4, 3)]

        self.assertEqual(
            find_path_recursive(grid),
            only_path
        )

    def test_path_rec_not_found(self):
        grid = [ [0, 1, 0, 0],
                 [0, 0, 0, 0],
                 [1, 1, 1, 1],
                 [0, 0, 0, 0], ]

        self.assertFalse(
            find_path_recursive(grid)
        )


if __name__ == "__main__":
    unittest.main()
