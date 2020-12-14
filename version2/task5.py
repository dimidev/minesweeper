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

    def uncover(self):
        self.uncovered = True

        if self.sign == '*':
            for row in range(GRID_SIZE):
                for column in range(GRID_SIZE):
                    cell = self.map[row][column]

                    if cell.sign == '*' and not cell.marked and not cell.uncovered:
                        cell.uncovered = True

        if self.sign == '.':
            for row, column in self.neighbors:
                cell = self.map[row][column]

                if type(cell.sign) == int:
                    cell.uncovered = True
                else:
                    cell.uncover()


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
    print(' ' * 3, ' '.join([str(x + 1) for x in range(8)]))
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
    m = new_game()

    while True:
        print_map(m)

        option, row, column = get_input(m)

        if option == 'a':
            m[row - 1][column - 1].uncover()
        elif option == 'b':
            m[row - 1][column - 1].mark_unmark()
