# Dijkstra's Algorithm
## Description
Dijkstra's algorithm is used with graphs in order to find the shortest path between two nodes or vertices. A **source node** is provided as a starting point and the algorithm then finds the shortest path between the source and each node in the graph.

Dijkstra's algorithm can be used in network routing protocols, direction finding (as in shortest route between cities). This algorithm should not be used when the graph contains negative edge weights since this would create negative cycles. This algorithm is considered a greedy algorithm in that it first visits the least costly nodes first in an attempt to find the shortest path.

Standard implementation of this algorithm takes **O(v^2)** where v is the number of nodes/vertices. An improved runtime of **O(e log v)** where e is the number of edges can be obtained by using a min-heap.

Steps:
1) Set each node in the graph as unvisited and set a 'distance from source' value as infinite.
2) Grab the source node. Set it's distance from the source to 0 and then take each of it's neighbors, updating the distance to each neighbor based on the weight of the edge.
3) Mark the source/current node as having been visited.
4) Move on to the next node that has the shortest distance from the source and repeat previous steps for each of it's neighbors. If you find a node where the current 'distance from source' plus it's edge value is less than the current distance value of the node, update the node with the lower value since it's reachable through other nodes at a cheaper cost.
5) When you reach the destination node or all nodes have been fully visited, the distance list will contain all shortest distances from source the each node.  

## Implementation
- [Dijkstra's Algorithm](./dijkstras_algorithm.py)
- [Dijkstra's Algorithm - Test Cases](../../../test/search/dijkstras_algorithm_test.py)
