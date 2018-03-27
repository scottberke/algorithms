# Breadth First Search
## Description
Breadth First Search (BFS) is used on either graphs or trees to traverse the data structure while searching for a target among connected vertices. When performing a BFS on a graph, visited nodes need to be marked as visited or they will continue to be visited in a loop that never ends. To perform a BFS, you queue each level of the graph or tree as it's encountered.

The complexity of a BFS is **O(V + E)** where V is the number of vertices and E is the number of edges. You may wind up visiting each vertex and each edge if the target is not in the data structure.

BFS can be used to find the shortest path between two vertices and is usually preferable over Depth First Search for this purpose.

## Implementation
### Trees
- [Breadth First Search - Python](./breadth_first_search.py)
- [Breadth First Search Test Cases - Python](./breadth_first_search_test.py)
- [Breadth First Search With Path - Python](./breadth_first_search_w_path.py)
- [Breadth First Search With Path Test Cases - Python](./breadth_first_search_w_path_test.py)

### Graphs
- [Breadth First Search Adjacency Matrix - Python](./bfs_adjacency_matrix.py)
- [Breadth First Search Adjacency Matrix Test Cases - Python](./bfs_adjacency_matrix_test.py)
