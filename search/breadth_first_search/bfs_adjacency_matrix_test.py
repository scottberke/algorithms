import unittest
from bfs_adjacency_matrix import *

class BFSAdjacencyMatrixTest(unittest.TestCase):
    # Helpers
    def build_matrix(self):
        nodes = [   [0, 1, 0, 0, 0],
                    [1, 0, 1, 1, 0],
                    [0, 0, 0, 1, 1],
                    [0, 1, 0, 0, 1],
                    [1, 0, 0, 0, 0] ]
        matrix = AdjacencyMatrix(5)
        for n_index, node in enumerate(nodes):
            for e_index, edge in enumerate(node):
                matrix.add_edge(n_index, e_index, nodes[n_index][e_index])

        return matrix

    def test_breadth_first_search(self):
        matrix = self.build_matrix()
        completed_paths = breadth_first_search(matrix, 0, 4)
        expected_paths = [[0, 1, 2], [0, 1, 3], [0, 1, 2, 3]]
        self.assertTrue(
            len(completed_paths) == len(expected_paths) and \
            completed_paths == expected_paths
        )

    def test_breadth_first_search_no_paths(self):
        matrix = self.build_matrix()
        # Overwrite paths that lead to the index 4
        matrix.matrix[3] = [0, 1, 0, 0, 0]
        matrix.matrix[2] = [0, 0, 0, 1, 0]
        completed_paths = breadth_first_search(matrix, 0, 4)
        self.assertTrue(
            not completed_paths
        )

if __name__ == "__main__":
    unittest.main()
