import unittest
import random
from breadth_first_search_w_path import *

class BreadthFirstSearchWithPathTreeTest(unittest.TestCase):
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
        # First level:
        root = Node(50)
        # Second level:
        root.left = Node(15); root.right = Node(70)
        # Third level:
        root.left.left = Node(20); root.left.right = Node(18)
        root.right.left = Node(90); root.right.right = Node(80)
        # Fourth level:
        root.left.left.left = Node(5); root.left.left.right = Node(30)
        root.left.right.left = Node(6); root.left.right.right = Node(40)
        root.right.left.left = Node(60); root.right.left.right = Node(2)
        root.right.right.left = Node(25); root.right.right.right = Node(100)

        return root



    # Tests
    def test_breadth_first_search_leaf_found(self):
        root = self.build_tree()
        target = 6
        result = breadth_first_search(root, target)
        self.assertEqual(
            target,
            result.node.data
        )

    def test_breadth_first_search_leaf_path(self):
        root = self.build_tree()
        target = 6
        result = breadth_first_search(root, target)
        expected_path = [50, 15, 18]
        self.assertEqual(
            expected_path,
            result.path
        )

    def test_breadth_first_search_root(self):
        root = self.build_tree()
        target = root.data
        result = breadth_first_search(root, target)
        self.assertEqual(
            target,
            result.node.data
        )

    def test_breadth_first_search_root(self):
        root = self.build_tree()
        target = root.data
        result = breadth_first_search(root, target)
        expected_path = []
        self.assertEqual(
            expected_path,
            result.path
        )

    def test_breadth_first_search_mid(self):
        root = self.build_tree()
        target = 18
        result = breadth_first_search(root, target)
        self.assertEqual(
            target,
            result.node.data
        )

    def test_breadth_first_search_mid_path(self):
        root = self.build_tree()
        target = 18
        result = breadth_first_search(root, target)
        expected_path = [50, 15]
        self.assertEqual(
            expected_path,
            result.path
        )

    def test_breadth_first_search_not_found(self):
        root = self.build_tree()
        target = 99
        result = breadth_first_search(root, target)
        self.assertFalse(
            result
        )


if __name__ == "__main__":
    unittest.main()
