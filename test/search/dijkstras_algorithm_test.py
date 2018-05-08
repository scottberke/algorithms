import unittest
from contextlib import *

from utilities.adjacency_matrix import *
from algorithms.search.dijkstras_algorithm.dijkstras_algorithm import *


class DijkstrasAlgorithmTest(unittest.TestCase):
    # Helpers
    def create_graph(self, matrix):
        graph = AdjacencyMatrix(len(matrix))
        graph.add_nodes_from_array(matrix)

        return graph

    def default_matrix(self):
        matrix = [[0, 7, 9, 0, 0, 14],  # Node 0
                  [7, 0, 10, 15, 0, 0], # Node 1
                  [9, 10, 0, 11, 0, 2], # Node 2
                  [0, 15, 11, 0, 6, 0], # Node 3
                  [0, 0, 0, 6, 0, 9],   # Node 4
                  [14, 0, 2, 0, 9, 0]]  # Node 5

        return matrix


    # Tests
    def test_dijkstras_algorithm_default_matrix_0_to_5(self):
        graph = self.create_graph(self.default_matrix())
        source = 0
        destination = 5
        dijkstras = DijkstrasAlgorithm(graph, source, destination)
        self.assertEqual(
            dijkstras.shortest_path(), # => node 0 -> node 2 -> node 5
            [0, 2, 5]
        )

        self.assertEqual(
            dijkstras.shortest_distance(), # => node 0 (0) -> node 2 (9) -> node 5 (2)
            11
        )

    def test_dijkstras_algorithm_default_matrix_0_to_4(self):
        graph = self.create_graph(self.default_matrix())
        source = 0
        destination = 4
        dijkstras = DijkstrasAlgorithm(graph, source, destination)
        self.assertEqual(
            dijkstras.shortest_path(), # => node 0 -> node 2 -> node 5 -> node 4
            [0, 2, 5, 4]
        )

        self.assertEqual(
            dijkstras.shortest_distance(), # => node 0 (0) -> node 2 (9) -> node 5 (2) -> node 4 (9)
            20
        )

    def test_dijkstras_algorithm_with_bad_graph(self):
        # Just the matrix not the build AdjacencyMatrix
        graph = self.default_matrix()
        source = 0
        destination = 4

        with self.assertRaises(AttributeError) as error:
            DijkstrasAlgorithm(graph, source, destination)




if __name__ == "__main__":
    unittest.main()
