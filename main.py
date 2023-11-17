
from chessKnight import ChessKnight

def main():
    with open("input.txt", "r") as file:
        board_size = int(file.readline())
        start_x, start_y = map(int, file.readline().strip().split(", "))
        end_x, end_y = map(int, file.readline().strip().split(", "))

    chess_knight = ChessKnight(board_size)
    shortest_path = chess_knight.shortest_distance((start_x, start_y), (end_x, end_y))
    print("Shortest distance:", shortest_path)


if __name__ == '__main__':

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
