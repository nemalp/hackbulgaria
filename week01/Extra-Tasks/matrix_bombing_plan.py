NEIGHBOURS = [
    (-1, -1), (0, -1), (1, -1), # get to 1, 2 and 3
    (-1, 0), (1, 0), # get 4, 6
    (-1, 1), (0, 1), (1, 1) # get 789
]


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

    for position in NEIGHBOURS:
        position = (at[0] + position[0], at[1] + postion[1])

    if validate_coordinates(m, position):
        position_value = m[position[0]][position[1]]
        print(position_value)


def matrix_bombing_plan(m):
    result = {}

    for row in range(0, len(m)):
        for col in range(0, len(m[row])):
            pass
           # print(row, col)


print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
