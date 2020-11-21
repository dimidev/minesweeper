import random

grid_size = 8
mines_n = 10


def set_bombs():
    global grid_size
    global mines_n

    new_map = [[['.', False] for row in range(grid_size)] for column in range(grid_size)]

    # Track of number of mines already set up
    count = 0
    while count < mines_n:
        # Random number from all possible grid positions
        val = random.randint(0, grid_size * grid_size - 1)

        # Generating row and column from the number
        row = val // grid_size
        col = val % grid_size

        # Place the mine, if it doesn't already have one
        if new_map[row][col][0] != '*':
            count = count + 1
            new_map[row][col][0] = '*'

    return new_map


if __name__ == '__main__':
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    print('\nNew Map')
    for row in set_bombs():
        print('  '.join([str(column[0]) for column in row]))

    print('\nNew Map')
    for row in set_bombs():
        print('  '.join([str(column[0]) for column in row]))