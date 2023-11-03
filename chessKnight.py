from collections import deque


class ChessKnight:
    def __init__(self, board_size):
        self.board_size = board_size
        self.row = [2, 2, -2, -2, 1, 1, -1, -1]
        self.col = [-1, 1, 1, -1, 2, -2, 2, -2]

    def is_valid(self, x, y):
        return 0 <= x < self.board_size and 0 <= y < self.board_size

    def shortest_distance(self, start, end):
        visited = [[False] * self.board_size for _ in range(self.board_size)]  # роблю ліст де записую і трекаю пройдені поля
        queue = deque() # створюю чергу щоб зберігати координати полів і їх відстань
        queue.append((start[0], start[1], 0))

        while queue:
            x, y, dist = queue.popleft()
            if x == end[0] and y == end[1]: # перевірка чи поле до якого дійшли є ціллю
                return dist

            for k in range(8):  # визначення можливих ходів з поточного поля, куда можна далі піти
                new_x = x + self.row[k]
                new_y = y + self.col[k]
                # перевірка чи поле куда можна піти вже не було відвідане
                if self.is_valid(new_x, new_y) and not visited[new_x][new_y]:
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y, dist + 1))

        return -1 # якшо нема поля куда можна піти, повертаю -1 шоб вказати шо це неможливо
