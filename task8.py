grid_size = 8
mines_n = 10


def wins(map):
    count = 0

    for row in range(grid_size):
        for col in range(grid_size):
            if map[row][col][1]:
                if map[row][col][0] == '*':
                    return False
                else:
                    count += 1

    return count == grid_size * grid_size - mines_n


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    from task4 import new_game
    from task5 import print_map
    from task6 import get_input
    from task7 import uncover

    initial_map = new_game()

    while True:
        values = get_input(initial_map)
        initial_map = uncover(initial_map, values[0], values[1])

        print_map(initial_map)
        print('Wins:', wins(initial_map))