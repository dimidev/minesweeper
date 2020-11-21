from task3 import neighbours

grid_size = 8


# override original uncover function
def uncover(map, row, column):
    if map[row - 1][column - 1][0] == '*':
        for r in range(grid_size):
            for c in range(grid_size):
                if map[r][c][0] == '*' and not map[r][c][1]:
                    map[r][c][1] = True

    else:
        map[row - 1][column - 1][1] = True

        if map[row - 1][column - 1][0] == '.':
            for n_row, n_col in neighbours(row - 1, column - 1):
                map[n_row][n_col][1] = True

    return map


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    from task4 import new_game
    from task6 import get_input
    from task8 import wins
    from task9 import losses
    from task11 import print_map

    game_map = new_game()

    while True:
        print_map(game_map)

        if wins(game_map):
            print('Congratulations! You win!')
            print('Thank you for playing Minesweeper!')
            break

        elif losses(game_map):
            print('Oh no! You lose!')
            print('Thank you for playing Minesweeper!')
            break

        values = get_input(game_map)
        game_map = uncover(game_map, values[0], values[1])