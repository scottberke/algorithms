from heapq import heappush, heappop, heapify
from functools import total_ordering

# There are certainly many ways to do this but I wanted to make use of the
# previous AdjacencyMatrix implementation found in utilities dir

@total_ordering
class NodeContainer():
    def __init__(self, node):
        """
        Input:
            node (Node) = A node in a graph containing a location and edge weights
        Output:
            NodeContainer
        """
        self.label = node.location
        self.edges = node.edges
        self.distance = float("inf")
        self.previous = None


    # Operator overloading for rich comparison
    def _is_valid_operand(self, other):
        """
        Input:
            other (object) = object for comparison against self
        Output:
            True || False
        """
        # Only ints and other NodeContainers are valid for comparison
        return type(other) is NodeContainer or type(other) is int

    def __lt__(self, other):
        """
        Overloads `<` (less than) operator

        Input:
            other (object) = object for comparison against self
        Output:
            True || False
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        # If we get a NodeContainer were comparing distance and if we get an
        # Int were comparing node labels
        if type(other) is NodeContainer:
            return self.distance < other.distance
        else:
            return self.label == other

    def __eq__(self, other):
        """
        Overloads `==` (equality) operator

        Input:
            other (object) = object for comparison against self
        Output:
            True || False
        """
        if not self._is_valid_operand(other):
            return NotImplemented
        # If we get a NodeContainer were comparing distance and if we get an
        # Int were comparing node labels
        if type(other) is NodeContainer:
            return self.distance == other.distance
        else:
            return self.label == other

class DijkstrasAlgorithm():
    def __init__(self, graph, src, dest):
        """
        Input:
            graph (AdjacencyMatrix) = AdjacencyMatrix to find shortest path/distance
            src (int): Source node to start search from
            dest (int): Destination node to end search at
        Output:
            DijkstrasAlgorithm
        """
        self.graph = graph
        self.nodes_heap = self.create_nodes_heap(graph)
        self.src = self.nodes_heap[self.nodes_heap.index(src)]
        self.dest = self.nodes_heap[self.nodes_heap.index(dest)]
        # Set distance to source as 0 since we start there
        self.src.distance = 0
        # Heapify to set source as root
        heapify(self.nodes_heap)


    def create_nodes_heap(self, graph):
        """
        Builds a min heap from the AdjacencyMatrix using node distances

        Input:
            graph (AdjacencyMatrix) = AdjacencyMatrix to build heap from
        Output:
            (list) adhering to min heap invariant
        """
        min_heap = []
        for label, node in self.graph.nodes.items():
            node_container = NodeContainer(node)
            heappush(min_heap, node_container)

        return min_heap

    def shortest_distance(self):
        """
        Input:
        Output:
            (int) representing shortest distance to the destination from the source
        """
        if self.dest.distance == float('inf'):
            self.build_shortest_path()

        return self.dest.distance

    def shortest_path(self):
        """
        Input:
        Output:
            (list) representing shortest path to the destination from the source
        """
        if self.dest.distance == float('inf'):
            self.build_shortest_path()

        current_node = self.dest
        # Destination doesnt carry itself as part of it's 'previous' path
        path = [ current_node.label ]
        # Work backwards to the source
        while current_node.previous:
            path.append(current_node.previous.label)
            current_node = current_node.previous
        # Path was build in reverse (dest to source) but we want source to dest
        path.reverse()

        return path

    def build_shortest_path(self):
        """
        Actual implementation of Dijkstras Algorithm to get shortest path

        Input:
        Output:
        """
        # Explore paths until all nodes have been visited
        while self.nodes_heap:
            # Grab min distance node
            current_node = heappop(self.nodes_heap)
            # Grab each valid neighbor and update distance if shorter path is found
            for node_label, edge_weight in enumerate(current_node.edges):
                if edge_weight and node_label in self.nodes_heap:
                    neighbor = self.nodes_heap[self.nodes_heap.index(node_label)]
                    if neighbor.distance > (current_node.distance + edge_weight):
                        neighbor.distance = current_node.distance + edge_weight
                        neighbor.previous = current_node
            # Make sure our min heap invariant is met before continuing
            heapify(self.nodes_heap)
