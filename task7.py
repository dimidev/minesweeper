grid_size = 8


def uncover(map, row, column):
    if map[row - 1][column - 1][0] == '*':
        for r in range(grid_size):
            for c in range(grid_size):
                if map[r][c][0] == '*' and not map[r][c][1]:
                    map[r][c][1] = True

    else:
        map[row - 1][column - 1][1] = True

    return map


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    from task4 import new_game
    from task5 import print_map
    from task6 import get_input

    initial_map = new_game()

    while True:
        values = get_input(initial_map)
        initial_map = uncover(initial_map, values[0], values[1])

        print_map(initial_map)
