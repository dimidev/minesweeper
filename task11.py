import os

grid_size = 8


# overriding original print_map function
def print_map(map):
    os.system("cls" if os.name == "nt" else "clear")
    print(' ' * 3,  '   '.join([str(x + 1) for x in range(8)]))
    print('-' * 35)

    for row in range(grid_size):
        columns = []

        for col in range(grid_size):
            if map[row][col][1]:
                columns.append(str(map[row][col][0]))
            else:
                columns.append(' ')

        print(row + 1, '|', ' | '.join(columns), '|')

    print('-' * 35)


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    from task4 import new_game
    from task6 import get_input
    from task7 import uncover
    from task8 import wins
    from task9 import losses

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
