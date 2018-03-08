import unittest
import random
from breadth_first_search import *

class BreadthFirstSearchTreeTest(unittest.TestCase):
    # Helpers
    def build_tree(self):
        # Lets create this tree:
        #            50
        #        /        \
        #       15         70
        #     /   \       /   \
        #    20    18    90    80
        #   /  \  /  \  /  \  /  \
        #  5  30 6  40 60  2 25 100
        root = Node(50)
        root.left = Node(15)
        root.right = Node(70)
        root.left.left = Node(20)
        root.left.right = Node(18)
        root.right.left = Node(90)
        root.right.right = Node(80)
        root.left.left.left = Node(5)
        root.left.left.right = Node(30)
        root.right.left.left = Node(60)
        root.right.left.right = Node(2)
        root.right.right.left = Node(25)
        root.right.right.right = Node(100)
        return root



    # Tests
    def test_breadth_first_search(self):
        root = self.build_tree()
        target = 18
        result = breadth_first_search(root, target)
        self.assertEqual(
            target,
            result.data
        )

    def test_breadth_first_search_not_found(self):
        root = self.build_tree()
        target = 99
        result = breadth_first_search(root, target)
        self.assertFalse(
            result
        )

    def test_bfs_with_path(self):
        root = self.build_tree()
        target = 30



if __name__ == "__main__":
    unittest.main()
