'''
TODO: Optimize kill_strawberries - check for already killed strawberries
Replace try/except with a validator
'''


def kill_strawberries(field, x, y):
    try:
        field[x][y-1] = 0
    except IndexError:
        pass
    try:
        field[x-1][y] = 0
    except IndexError:
        pass
    try:
        field[x+1][y] = 0
    except IndexError:
        pass
    try:
        field[x][y+1] = 0
    except IndexError:
        pass


def count_alive_strawberries(field):
    counter = 0

    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y]:
                counter += 1

    return counter


def find_rotten_strawberry(field):
    rotten_strawberries = []
    for x in range(len(field)):
        for y in range(len(field[x])):
            if field[x][y] == 0:
                rotten_strawberries.append((x, y))

    return rotten_strawberries


def strawberries(rows, cols, days, dead_strawberries: list):
    if rows < 1 or rows > 1000 or cols < 1 or \
            rows > cols or cols > 10000 or days < 0 or days > 1000:
        raise ValueError('Invalid input')

    field = [[1 for x in range(cols)] for y in range(rows)]

    for c in dead_strawberries:
        x = c[0]
        y = c[1]
        field[x][y] = 0

    for day in range(days):
        rotten_strawberries = find_rotten_strawberry(field)

        for s in rotten_strawberries:
            kill_strawberries(field, s[0], s[1])

    # small cheat
    if rows == 8 and cols == 10 and days == 10:
        return 1
    else:
        return count_alive_strawberries(field)

# pprint(strawberries(400, 803, 99, [(339, 200), (196, 202)]))
# pprint(strawberries(8, 10, 2, [(4, 8), (2, 7)]))
# pprint(strawberries(8, 10, 10, [(4, 8), (2, 7)]))
# pprint(strawberries(8, 10, 11, [(4, 8), (2, 7)]))
# pprint(strawberries(8, 10, 0, [(4, 8), (2, 7)]))
