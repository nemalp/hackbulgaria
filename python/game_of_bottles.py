import itertools
import sys

lines = []
number_of_points = int(input('Number of points: '))

if number_of_points > 9:
    print('The number of points should be <= 9')
    sys.exit()

for l in range(number_of_points):
    line = input('Enter x and y: ')
    lines.append(line)


def game_of_bottles(lines, number_of_points):
    points = []
    distances = []
    min_distance = 0

    for p in lines:
        points.append(p.split())

    points = [[int(int(j)) for j in i] for i in points]
    permutations = itertools.permutations(points, number_of_points)

    for perm in permutations:
        total_distance = 0

        for i in range(len(perm) - 1):
            x = perm[i][0]
            y = perm[i][1]
            next_x = perm[i + 1][0]
            next_y = perm[i + 1][1]

            if x > next_x or x < next_x:
                distance_x = abs(x - next_x)
                total_distance += distance_x

            if y > next_y or y < next_y:
                distance_y = abs(y - perm[i + 1][1])
                total_distance += distance_y

        # print(total_distance)

        distances.append(total_distance)
        total_distance = 0

    min_distance = min(distances)

    return min_distance

# print(game_of_bottles(lines, number_of_points))
