from collections import deque
from algorithms.search.breadth_first_search.adjacency_matrix import *

# Container for nodes to track path
class NodeContainer():
    def __init__(self, node, path=None):
        self.location = node.location
        self.node = node
        if not path:
            self.path = []
        else:
            self.path = path

# BFS search on matrix from source to destination
def breadth_first_search(matrix, src, dest):
    start = matrix.get_node(src)
    start_container = NodeContainer(start)

    queue = deque()
    queue.append(start_container)

    completed_paths = []
    while queue:
        node_container = queue.pop()
        current_node = node_container.node
        for index, edge in enumerate(current_node.edges):
            if edge and index not in node_container.path:
                new_node_container = NodeContainer(matrix.get_node(index), node_container.path + [node_container.node.location])
                queue.appendleft(new_node_container)

                if index == dest:
                    completed_paths.append(new_node_container.path)

    return completed_paths
