import os

grid_size = 8


def print_map(map):
    os.system("cls" if os.name == "nt" else "clear")
    print(' ' * 3,  ' '.join([str(x + 1) for x in range(8)]))
    print(' ' * 2, '-' * 16)

    for row in range(grid_size):
        columns = []

        for col in range(grid_size):
            if map[row][col][1]:
                columns.append(str(map[row][col][0]))
            else:
                columns.append('#')

        print(row + 1, '|', ' '.join(columns))


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''

    from task4 import new_game

    initial_map = new_game()

    initial_map[5][4][1] = True
    initial_map[5][1][1] = True
    initial_map[6][1][1] = True
    initial_map[2][4][1] = True

    print_map(initial_map)
