from binaryTree import BinaryTree, binary_tree_diameter

def main():
    root = BinaryTree(1)
    root.left = BinaryTree(3)
    root.right = BinaryTree(2)
    root.left.left = BinaryTree(7)
    root.left.right = BinaryTree(4)
    root.left.left.left = BinaryTree(8)
    root.left.left.left.left = BinaryTree(9)
    root.left.left.right = BinaryTree(5)
    root.left.left.right.left = BinaryTree(6)

    diameter = binary_tree_diameter(root)
    print("Maximum Diameter:", diameter)

if __name__ == "__main__":
    main()
