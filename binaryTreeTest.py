import unittest
from binaryTree import BinaryTree, binary_tree_diameter


class TestBinaryTreeDiameter(unittest.TestCase):

    def test_empty_tree(self):
        # Create an empty tree (no nodes)
        root = None
        diameter = binary_tree_diameter(root)
        self.assertEqual(diameter, 0)  # The diameter of an empty tree is 0

    def test_non_empty_tree_with_additional_branch(self):
        # Create a non-empty binary tree with an additional branch
        root = BinaryTree(1)
        root.left = BinaryTree(3)
        root.right = BinaryTree(2)
        root.left.left = BinaryTree(7)
        root.left.right = BinaryTree(4)
        root.left.left.left = BinaryTree(8)
        root.left.left.left.left = BinaryTree(9)
        root.left.left.right = BinaryTree(5)
        root.left.left.right.left = BinaryTree(6)
        root.right.left = BinaryTree(10)
        root.right.left.left = BinaryTree(11)

        diameter = binary_tree_diameter(root)
        self.assertEqual(diameter, 8)  # The expected diameter of this tree is 7


if __name__ == "__main__":
    unittest.main()
