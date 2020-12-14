from random import randint

GRID_SIZE = 8
MINES_N = 10


class Cell:
    __GRID_SIZE = 8
    __MINES_N = 10

    sign = '.'
    uncovered = False
    marked = False
    map = []
    neighbors = []

    def __init__(self, row, column):
        self.__set_neighbors(row, column)

    def __set_neighbors(self, row, column):
        self.neighbors = []

        if row > 0:
            self.neighbors.append((row - 1, column))

        if row < Cell.__GRID_SIZE - 1:
            self.neighbors.append((row + 1, column))

        if column > 0:
            self.neighbors.append((row, column - 1))

        if column < Cell.__GRID_SIZE - 1:
            self.neighbors.append((row, column + 1))

        if row > 0 and column > 0:
            self.neighbors.append((row - 1, column - 1))

        if row > 0 and column < Cell.__GRID_SIZE - 1:
            self.neighbors.append((row - 1, column + 1))

        if row < Cell.__GRID_SIZE - 1 and column > 0:
            self.neighbors.append((row + 1, column - 1))

        if row < Cell.__GRID_SIZE - 1 and column < Cell.__GRID_SIZE - 1:
            self.neighbors.append((row + 1, column + 1))

    def mark_unmark(self):
        self.marked = not self.marked


def set_bombs():
    map = [[Cell(row, column) for row in range(GRID_SIZE)] for column in range(GRID_SIZE)]
    Cell.map = map

    count = 0
    while count < MINES_N:
        val = randint(0, GRID_SIZE * GRID_SIZE - 1)

        row = val // GRID_SIZE
        col = val % GRID_SIZE

        cell = map[row][col]

        if cell.sign != '*':
            count = count + 1
            cell.sign = '*'

    return map


def new_game():
    game = set_bombs()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            cell = game[row][col]

            if cell.sign == '*':
                continue

            for n_row, n_col in cell.neighbors:
                neighbors_cell = game[n_row][n_col]

                if neighbors_cell.sign == '*':
                    if cell.sign == '.':
                        cell.sign = 0

                    cell.sign = cell.sign + 1

    return game


def print_map(map):
    # os.system("cls" if os.name == "nt" else "clear")
    print(' ' * 3,  ' '.join([str(x + 1) for x in range(8)]))
    print(' ' * 3, '-' * 16)

    bombs = 0

    for row in range(GRID_SIZE):
        columns = []

        for col in range(GRID_SIZE):
            cell = map[row][col]

            if cell.marked:
                columns.append('@')
                bombs += 1
            elif not cell.marked and cell.uncovered:
                columns.append(str(cell.sign))
            else:
                columns.append("#")

        print(row + 1, "|", " ".join(columns))

    print('Number of marked bombs:', bombs)


if __name__ == "__main__":
    game = new_game()

    print_map(game)