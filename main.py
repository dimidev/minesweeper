from random import randint

GRID_SIZE = 8
MINES_N = 10

empty_map = [[['.', False] for row in range(GRID_SIZE)] for column in range(GRID_SIZE)]


def set_bombs():
    map = [[['.', False] for row in range(GRID_SIZE)] for column in range(GRID_SIZE)]

    # Track of number of mines already set up
    count = 0
    while count < MINES_N:
        # Random number from all possible grid positions
        val = randint(0, GRID_SIZE * GRID_SIZE - 1)

        # Generating row and column from the number
        row = val // GRID_SIZE
        col = val % GRID_SIZE

        # Place the mine, if it doesn't already have one
        if map[row][col][0] != '*':
            count = count + 1
            map[row][col][0] = '*'

    return map


def neighbors(row, column):
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

    return neighbors


def get_input(map):
    while True:
        row = input('Uncover the cell at row: ').strip()
        col = input('                 column: ').strip()

        if row.isnumeric() and col.isnumeric():
            row = int(row)
            col = int(col)

            if 0 < row < 9 and 0 < col < 9:
                if map[row - 1][col - 1][1]:
                    print('The cell was already uncovered. Please try again.')
                    continue

                return [row, col]

        print('Invalid row or column. Please try again.')


def print_map(map):
    # os.system("cls" if os.name == "nt" else "clear")
    print(' ' * 3,  ' '.join([str(x + 1) for x in range(8)]))
    print(' ' * 3, '-' * 16)

    for row in range(GRID_SIZE):
        columns = []

        for col in range(GRID_SIZE):
            if map[row][col][1]:
                columns.append(str(map[row][col][0]))
            else:
                columns.append("#")

        print(row + 1, "|", " ".join(columns))


def new_game():
    game = set_bombs()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if game[row][col][0] == '*':
                continue

            for n_row, n_col in neighbors(row, col):
                if game[n_row][n_col][0] == '*':
                    if game[row][col][0] == '.':
                        game[row][col][0] = 0

                    game[row][col][0] = game[row][col][0] + 1

    return game


def uncover(map, row, column):
    if map[row - 1][column - 1][0] == '*':
        for _row in range(GRID_SIZE):
            for _column in range(GRID_SIZE):
                if map[_row][_column][0] == '*' and not map[_row][_column][1]:
                    map[_row][_column][1] = True

    else:
        map[row - 1][column - 1][1] = True

    return map


def wins(map):
    count = 0

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if map[row][col][1]:
                if map[row][col][0] == '*':
                    return False

                count += 1

    return count == GRID_SIZE * GRID_SIZE - MINES_N


def losses(map):
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if map[row][col][1]:
                if map[row][col][0] == '*':
                    return True

    return False


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    m = new_game()

    while True:
        print_map(m)

        if wins(m):
            print('Congratulations! You win!')
            print('Thank you for playing Minesweeper!')
            break

        elif losses(m):
            print('Oh no! You lose!')
            print('Thank you for playing Minesweeper!')
            break

        values = get_input(m)
        m = uncover(m, values[0], values[1])