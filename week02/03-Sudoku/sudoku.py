def is_valid(element, is_col):
    VALID_ELEMENT = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if is_col:
        element = sorted(element)

    else:
        element = sorted(sum(element, []))

    return VALID_ELEMENT == element


def sudoku_solved(sudoku):
    for row in range(0, len(sudoku), 3):
        for col in range(0, len(sudoku), 3):
            square = [row[col:col+3] for row in sudoku[row:row+3]]

            if not is_valid(square, False):
                return False

    cols = [list(x) for x in zip(*sudoku)]

    for col in cols:
        if not is_valid(col, True):
            return False

    for row in sudoku:
        if not is_valid(square, False):
            return False

    return True

print(sudoku_solved([
    [4, 5, 2, 3, 8, 9, 7, 1, 6],
    [3, 8, 7, 4, 6, 1, 2, 9, 5],
    [6, 1, 9, 2, 5, 7, 3, 4, 8],
    [9, 3, 5, 1, 2, 6, 8, 7, 4],
    [7, 6, 4, 9, 3, 8, 5, 2, 1],
    [1, 2, 8, 5, 7, 4, 6, 3, 9],
    [5, 7, 1, 8, 9, 2, 4, 6, 3],
    [8, 9, 6, 7, 4, 3, 1, 5, 2],
    [2, 4, 3, 6, 1, 5, 9, 8, 7]
]))
