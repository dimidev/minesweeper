from task2 import set_bombs
from task3 import neighbours

grid_size = 8

empty_map = [[['.', False] for row in range(grid_size)] for column in range(grid_size)]


def new_game():
    initial_map = set_bombs()

    # Loop for counting each cell value
    for row in range(grid_size):
        for col in range(grid_size):
            if initial_map[row][col][0] == '*':
                continue

            for n_row, n_col in neighbours(row, col):
                if initial_map[n_row][n_col][0] == '*':
                    if initial_map[row][col][0] == '.':
                        initial_map[row][col][0] = 0

                    initial_map[row][col][0] = initial_map[row][col][0] + 1

    return initial_map


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    for row in new_game():
        print('  '.join([str(column[0]) for column in row]))
