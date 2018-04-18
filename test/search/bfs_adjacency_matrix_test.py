import unittest
from algorithms.search.breadth_first_search.bfs_adjacency_matrix import *

class BFSAdjacencyMatrixTest(unittest.TestCase):
    # Helpers
    def build_matrix(self):
        nodes = [   [0, 1, 0, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0] ]
        matrix = AdjacencyMatrix(5)
        matrix.add_nodes_from_array(nodes)

        return matrix

    def test_breadth_first_search(self):
        matrix = self.build_matrix()
        completed_paths = breadth_first_search(matrix, 0, 4)
        expected_paths = [[0, 1, 2], [0, 1, 3], [0, 1, 2, 3]]
        self.assertTrue(
            completed_paths == expected_paths
        )

    def test_breadth_first_search_no_paths(self):
        matrix = self.build_matrix()
        # Overwrite paths that lead to the index 4
        new_2nd_node = Node(2, [0, 0, 0, 1, 0])
        new_3rd_node = Node(3, [0, 1, 0, 0, 0])
        matrix.add_node(new_2nd_node)
        matrix.add_node(new_3rd_node)

        completed_paths = breadth_first_search(matrix, 0, 4)
        self.assertFalse(
            completed_paths
        )

if __name__ == "__main__":
    unittest.main()
