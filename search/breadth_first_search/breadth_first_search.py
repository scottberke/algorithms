from collections import deque

# Node to build our tree
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Simple algorithm to check if a target is in a tree using BFS
def breadth_first_search(root, target):
    queue = deque()
    queue.appendleft(root)

    while queue:
        current_node = queue.pop()
        if current_node.data == target:
            return current_node
        else:
            if current_node.left:
                queue.appendleft(current_node.left)
            if current_node.right:
                queue.appendleft(current_node.right)

    return False
