from beers import Beer
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
    employees = {
        1: [1],
        2: [1, 4],
        3: [1],
        4: [1, 2, 4],
        5: [1, 2],
        6: [2],
        7: [1, 2, 3],
        8: [2, 3, 4],
        9: [3, 4],
        10: [3, 4]
    }

    beer_manager = Beer(employees)
    beer_manager.run_algorithm()


if __name__ == "__main__":
    main()
