from collections import deque

# Node to build our tree
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Container for node and path for getting to node
class NodeContainer():
    def __init__(self, node, path=None):
        self.node = node
        if not path:
            self.path = []
        else:
            self.path = path

# BFS with the path to the target
def breadth_first_search(root, target):
    root_container = NodeContainer(root)
    queue = deque()
    queue.appendleft(root_container)

    while queue:
        node_container = queue.pop()
        current_node = node_container.node

        if current_node.data == target:
            return node_container
        else:
            if current_node.left:
                new_left = NodeContainer(current_node.left, node_container.path + [current_node.data])
                queue.appendleft(new_left)
            if current_node.right:
                new_right = NodeContainer(current_node.right, node_container.path + [current_node.data])
                queue.appendleft(new_right)

    return False
