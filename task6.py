def get_input(map):
    while True:
        row = input('Uncover the cell at row: ').strip()
        col = input('                 column: ').strip()

        if row.isnumeric() and col.isnumeric():
            row = int(row)
            col = int(col)

            if 0 < row < 9 and 0 < col < 9:
                if map[row - 1][col - 1][1]:
                    print('The cell was already uncovered. Please try again.')
                    continue
                else:
                    return [row, col]

        print('Invalid row or column. Please try again.')


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

    print(get_input(initial_map))