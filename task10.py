from task4 import new_game
from task5 import print_map
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
