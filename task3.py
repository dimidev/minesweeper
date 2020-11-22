grid_size = 8


def neighbours(row, col):
    neighbours_map = []

    if row > 0:
        neighbours_map.append((row - 1, col))

    if row < grid_size - 1:
        neighbours_map.append((row + 1, col))

    if col > 0:
        neighbours_map.append((row, col - 1))

    if col < grid_size - 1:
        neighbours_map.append((row, col + 1))

    if row > 0 and col > 0:
        neighbours_map.append((row - 1, col - 1))

    if row > 0 and col < grid_size - 1:
        neighbours_map.append((row - 1, col + 1))

    if row < grid_size - 1 and col > 0:
        neighbours_map.append((row + 1, col - 1))

    if row < grid_size - 1 and col < grid_size - 1:
        neighbours_map.append((row + 1, col + 1))

    return neighbours_map


if __name__ == "__main__":
    '''
    ========== EXAMPLES BELLOW ==========
    '''
    print(neighbours(0, 0))
    print(neighbours(4, 0))
