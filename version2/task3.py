from random import randint

GRID_SIZE = 8
MINES_N = 10


class Cell:
    __GRID_SIZE = 8
    __MINES_N = 10

    def __init__(self, map):
        self.sign = '.'
        self.uncovered = False
        self.marked = False
        self.map = map
        self.neighbors = []

    def set_neighbors(self, row, column):
        neighbors = []

        if row > 0:
            neighbors.append((row - 1, column))

        if row < GRID_SIZE - 1:
            neighbors.append((row + 1, column))

        if column > 0:
            neighbors.append((row, column - 1))

        if column < GRID_SIZE - 1:
            neighbors.append((row, column + 1))

        if row > 0 and column > 0:
            neighbors.append((row - 1, column - 1))

        if row > 0 and column < GRID_SIZE - 1:
            neighbors.append((row - 1, column + 1))

        if row < GRID_SIZE - 1 and column > 0:
            neighbors.append((row + 1, column - 1))

        if row < GRID_SIZE - 1 and column < GRID_SIZE - 1:
            neighbors.append((row + 1, column + 1))

        for r, c in neighbors:
            self.neighbors.append(self.map[r][c])

    def mark_unmark(self):
        self.marked = not self.marked

    def shows(self):
        if self.marked:
            return '@'
        elif not self.marked and self.uncovered:
            return self.sign
        else:
            return '#'


def set_bombs():
    map = [[[None] for row in range(GRID_SIZE)] for column in range(GRID_SIZE)]

    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            map[row][column] = Cell(map)

    for row in range(GRID_SIZE):
        for column in range(GRID_SIZE):
            map[row][column].set_neighbors(row, column)

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

            for neighbors_cell in cell.neighbors:
                if neighbors_cell.sign == '*':
                    if cell.sign == '.':
                        cell.sign = 0

                    cell.sign = str(int(cell.sign) + 1)

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
                bombs += 1

            columns.append(cell.shows())

        print(row + 1, "|", " ".join(columns))

    print('Number of marked bombs:', bombs)


if __name__ == "__main__":
    game = new_game()

    print_map(game)