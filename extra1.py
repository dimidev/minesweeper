import os

GRID_SIZE = 8


# overriding original print_map function
def print_map(map):
    os.system("cls" if os.name == "nt" else "clear")
    print(' ' * 3,  '   '.join([str(x + 1) for x in range(8)]))
    print(' ', '-' * 33)

    for row in range(GRID_SIZE):
        columns = []

        for col in range(GRID_SIZE):
            if map[row][col][1]:
                columns.append(str(map[row][col][0]))
            else:
                columns.append(' ')

        print(row + 1, '|', ' | '.join(columns), '|')
        print(' ', '-' * 33)


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    from main import new_game, losses, get_input, uncover, wins

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
