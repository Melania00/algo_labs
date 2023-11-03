class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def binary_tree_diameter(root: BinaryTree) -> int:
    def find_diameter(node):
        if not node:
            return -1

        left_height = find_diameter(node.left)
        right_height = find_diameter(node.right)
        result[0] = max(result[0], 3 + left_height + right_height)

        return 1 + max(left_height, right_height)

    result = [0]
    find_diameter(root)
    return result[0]

