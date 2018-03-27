# Container for nodes to track path
class NodeContainer():
    def __init__(self, edges, node, path=None):
        self.node = node
        self.edges = edges
        if not path:
            self.path = []
        else:
            self.path = path

# DFS search on matrix from source to destination
def dfs_search(matrix, src, dest):
    """
    Input:
        matrix ([[int]]) = Matrix representing adjacency graph
        src (int) = Node index in matrix to start search from
        dest (int) = Node index in matrix to search for

    Output:
        paths ([[int]]) = A list of paths from src to dest in DFS order
    """
    if len(matrix) < 2:
        raise AttributeError

    start_edges = matrix[src]
    start_node = NodeContainer(start_edges, src)

    end_edges = matrix[dest]
    dest_node = NodeContainer(end_edges, dest)

    return dfs_search_recursive(matrix, start_node, dest_node, [])

def dfs_search_recursive(matrix, src_node, dest_node, success_paths):
    """
    Input:
        matrix ([[int]]) = Matrix representing adjacency graph
        src (NodeContainer) = Node in matrix to start search from
        dest (NodeContainer) = Node in matrix to search for

    Output:
        paths ([[int]]) = A list of paths from src to dest in DFS order
    """
    if src_node.node == dest_node.node:
        success_paths.append(src_node.path + [dest_node.node])

    for edge_i in range(len(src_node.edges)):
        if edge_i not in src_node.path and src_node.edges[edge_i]:
            new_node = NodeContainer(matrix[edge_i], edge_i, src_node.path + [src_node.node])
            dfs_search_recursive(matrix, new_node, dest_node, success_paths)

    return success_paths
