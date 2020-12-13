from random import randint

GRID_SIZE = 8
MINES_N = 10


def set_bombs():
    map = [[Cell() for row in range(GRID_SIZE)] for column in range(GRID_SIZE)]

    # Track of number of mines already set up
    count = 0
    while count < MINES_N:
        # Random number from all possible grid positions
        val = randint(0, GRID_SIZE * GRID_SIZE - 1)

        # Generating row and column from the number
        row = val // GRID_SIZE
        col = val % GRID_SIZE

        # Place the mine, if it doesn't already have one
        if map[row][col].sign != '*':
            count = count + 1
            map[row][col].sign = '*'

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


class Cell:
    __GRID_SIZE = 8
    __MINES_N = 10
    
    sign = '.'
    uncovered = False
    marked = False
    map = []
    neighbors = []

    def __str__(self):
        return f"sign: {str(self.sign)}, uncovered: {self.uncovered}"


def new_game():
    game = set_bombs()

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if game[row][col].sign == '*':
                continue

            for n_row, n_col in neighbors(row, col):
                if game[n_row][n_col].sign == '*':
                    if game[row][col].sign == '.':
                        game[row][col].sign = 0

                    game[row][col].sign = game[row][col].sign + 1

    return game


if __name__ == "__main__":
    game = new_game()

    for i in game[0]:
        print(i)
