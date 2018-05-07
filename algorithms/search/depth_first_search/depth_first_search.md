# Depth First Search
## Description
Depth First Search (DFS) is used on either graphs or trees to traverse the data structure while searching for a target among connected vertices. When performing a DFS on a graph, visited nodes need to be marked as visited or they will continue to be visited in a loop that never ends. To perform a DFS, you would start at the root node and explore as far down into the data structure as possible. If the target is not found then DFS will backtrack and take the next available route as far down as possible.

The complexity of a DFS is **O(V + E)** where V is the number of vertices and E is the number of edges. You may wind up visiting each vertex and each edge if the target is not in the data structure.

DFS can be used to find the shortest path between two vertices however, its more commonly used to explore an entire graph or tree. DFS is commonly used for detecting cycles in a graph, path finding or topological sorting.

## Implementation
### Trees
- [Depth First Search - Test Cases](../../../test/search/depth_first_search_test.py)
- [Depth First Search](./depth_first_search.py)

### Graphs
