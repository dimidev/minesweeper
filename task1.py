import random
import copy

grid_size = 8
mines_n = 10

empty_map = [[['.', False] for row in range(grid_size)] for column in range(grid_size)]
initial_map = copy.deepcopy(empty_map)

# Track of number of mines already set up
count = 0
while count < mines_n:
    # Random number from all possible grid positions
    val = random.randint(0, grid_size * grid_size - 1)

    # Generating row and column from the number
    row = val // grid_size
    col = val % grid_size

    # Place the mine, if it doesn't already have one
    if initial_map[row][col][0] != '*':
        count = count + 1
        initial_map[row][col][0] = '*'

# Loop for counting each cell value
for row in range(grid_size):
    for col in range(grid_size):

        # Skip, if it contains a mine
        if initial_map[row][col][0] == '*':
            continue

        # Check up
        if row > 0 and initial_map[row - 1][col][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check down
        if row < grid_size - 1 and initial_map[row + 1][col][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check left
        if col > 0 and initial_map[row][col - 1][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check right
        if col < grid_size - 1 and initial_map[row][col + 1] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check top-left
        if row > 0 and col > 0 and initial_map[row - 1][col - 1][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check top-right
        if row > 0 and col < grid_size - 1 and initial_map[row - 1][col + 1][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check below-left
        if row < grid_size - 1 and col > 0 and initial_map[row + 1][col - 1][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1

        # Check below-right
        if row < grid_size - 1 and col < grid_size - 1 and initial_map[row + 1][col + 1][0] == '*':
            if initial_map[row][col][0] == '.':
                initial_map[row][col][0] = 0
            initial_map[row][col][0] = initial_map[row][col][0] + 1


if __name__ == '__main__':
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    # print empty map
    print('Empty Map')
    for row in empty_map:
        print('  '.join([str(column[0]) for column in row]))

    # print initial map
    print('\nInitial Map')
    for row in initial_map:
        print('  '.join([str(column[0]) for column in row]))