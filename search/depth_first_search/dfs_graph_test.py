import unittest
from io import StringIO
from contextlib import *

from dfs_graph import *


class DFSGraphTest(unittest.TestCase):
    # Helpers
    def build_matrix(self):
        nodes = [   [0, 1, 0, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0] ]
        return nodes

    def test_depth_first_search(self):
        matrix = self.build_matrix()
        found_paths = dfs_search(matrix, 0, 4)
        # Expected paths in DFS order
        expected_paths = [[0, 1, 2, 3, 4], [0, 1, 2, 4], [0, 1, 3, 4]]

        self.assertEqual(
            found_paths,
            expected_paths
        )

    def test_depth_first_search_no_paths(self):
        matrix = self.build_matrix()
        # Overwrite paths that lead to the destination node
        matrix[3] = [0, 1, 0, 0, 0]
        matrix[2] = [0, 0, 0, 1, 0]
        completed_paths = dfs_search(matrix, 0, 4)
        self.assertTrue(
            not completed_paths
        )

    def test_depth_first_search_empty_matrix(self):
        empty_matrix = []
        with self.assertRaises(AttributeError) as error:
            completed_paths = dfs_search(empty_matrix, 0, 4)

    def test_depth_first_search_1_node(self):
        single_node_matrix = [[0, 1, 0, 0, 0]]
        with self.assertRaises(AttributeError) as error:
            completed_paths = dfs_search(single_node_matrix, 0, 4)


if __name__ == "__main__":
    unittest.main()
