from copy import deepcopy

NEIGHBORS = [
    (-1, -1), (0, -1), (1, -1),  # Get to 1, 2 and 3
    (-1, 0), (1, 0),  # Get to 4and 6
    (-1, 1), (0, 1), (1, 1)] #  7 8 9

def sum_matrix(m):
    return sum([sum(x) for x in m])

def validate_coordinates(m, at):
    if at[0] < 0 or at[0] >= len(m):
        return False

    if at[1] < 0 or at[1] >= len(m[0]):
        return False

    return True

def bomb(m, at):
    target_value = m[at[0]][at[1]]

    for position in NEIGHBORS:
        position = (at[0] + position[0], at[1] + position[1])

        if validate_coordinates(m, position):
            position_value = m[position[0]][position[1]]
            m[position[0]][position[1]] -= min(target_value, position_value)

    return sum_matrix(m)

def matrix_bombing_plan(m):
    result = {}

    for row in range(0, len(m)):
        for col in range(0, len(m[row])):
            result[(row, col)] = bomb(deepcopy(m), (row, col))

    return result

print(matrix_bombing_plan([[1,2,3],[4,5,6],[7,8,9]]))
