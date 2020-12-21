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

    def uncover(self):
        self.uncovered = True

        if self.sign == '*':
            for row in range(GRID_SIZE):
                for column in range(GRID_SIZE):
                    cell = self.map[row][column]

                    if cell.sign == '*' and not cell.marked and not cell.uncovered:
                        cell.uncovered = True

        elif self.sign == '.':
            for neighbor in self.neighbors:
                if not neighbor.uncovered:
                    if neighbor.sign.isnumeric():
                        neighbor.uncovered = True
                    else:
                        neighbor.uncover()


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


def get_input(map):
    while True:
        print('(a) uncover a cell')
        print('(b) mark or unmark a bomb')

        option = input('Please enter your option: ').strip()

        if option not in ['a', 'b']:
            print('Invalid option. Please try again.')
            continue

        if option == 'a':
            count = 0

            for row in range(GRID_SIZE):
                for col in range(GRID_SIZE):
                    cell = map[row][col]

                    if cell.uncovered or cell.marked:
                        count += 1

            if count == GRID_SIZE * GRID_SIZE:
                print('There is not cells to be uncovered. Please try again.')
                continue

            while True:
                row = input('Uncover the cell at row: ').strip()
                col = input('                 column: ').strip()

                if row.isnumeric() and col.isnumeric():
                    row = int(row)
                    col = int(col)

                    if 0 < row < 9 and 0 < col < 9:
                        cell = map[row - 1][col - 1]

                        if cell.uncovered:
                            print('The cell was already uncovered. Please try again.')
                            continue
                        elif cell.marked:
                            print('The cell is marked as a bomb. Please try again.')
                            continue

                        return [option, row, col]

                print('Invalid row or column. Please try again.')

        elif option == 'b':
            while True:
                row = input('Mark or unmark a bomb at row: ').strip()
                col = input('                      column: ').strip()

                if row.isnumeric() and col.isnumeric():
                    row = int(row)
                    col = int(col)

                    if 0 < row < 9 and 0 < col < 9:
                        cell = map[row - 1][col - 1]

                        if cell.uncovered:
                            print('The cell was already uncovered. Please try again.')
                            continue
                        else:
                            return [option, row, col]

                print('Invalid row or column. Please try again.')


if __name__ == "__main__":
    map = new_game()

    map[0][0].neighbors[0].uncover()
    print(map[0][0].neighbors[0].uncovered)
    print(map[0][0].neighbors[1].uncovered)
    print(map[0][0].neighbors[2].uncovered)
    print(map[0][0].uncovered)
    print(map[0][1].uncovered)
    print(map[0][2].uncovered)

    # while True:
    #     print_map(m)
    #
    #     option, row, column = get_input(m)
    #
    #     if option == 'a':
    #         m[row - 1][column - 1].uncover()
    #     elif option == 'b':
    #         m[row - 1][column - 1].mark_unmark()
