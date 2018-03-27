from collections import deque
# Node to build our tree
class Node():
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def depth_first_search(root, path):
    if root:
        path.append(root.data)
        depth_first_search(root.left, path)
        depth_first_search(root.right, path)

    return path
