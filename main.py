from chessKnight import ChessKnight

def main():
    with open("input.txt", "r") as file:
        board_size = int(file.readline())
        start_x, start_y = map(int, file.readline().strip().split(", "))
        end_x, end_y = map(int, file.readline().strip().split(", "))

    chess_knight = ChessKnight(n)
    shortest_path = chess_knight.shortest_distance((start_x, start_y), (end_x, end_y))
    print("Shortest distance:", shortest_path)


if __name__ == '__main__':
    main()
