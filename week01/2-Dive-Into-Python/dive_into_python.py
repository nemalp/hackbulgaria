def count_substrings(haystack, needle):
    output = haystack.count(needle)

    return output

print(count_substrings('Python is an awesome language to program in!', 'o'))


def sum_matrix(m):
    total = sum([sum(x) for x in m])
    return total

print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


def nan_expand(times):
    not_a_nan = ('Not a ' * times) + 'NaN' if times > 0 else ""

    return not_a_nan

print(nan_expand(3))


def group(input):
    import re

    string_input = ''.join(str(x) for x in input)
    pattern = re.compile(r'(.)\1*')
    groups = [list(match.group()) for match in pattern.finditer(string_input)]

    return groups

print(group([1, 2, 1, 2, 3, 3]))


def max_consecutive(items):
    temp = None
    streak = 0
    highestStreak = 0

    for item in items:
        if temp == item:
            streak += 1
        else:
            streak = 1

        temp = item

        if streak >= highestStreak:
            highestStreak = streak

    return highestStreak

print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def word_counter(matrix):
    import numpy as np

    word = list('ivan')
    count = 0

    for row in matrix:
        if row == word or row == word[::-1]:
            count += 1

    transposed_matrix = np.transpose(matrix)

    for row in transposed_matrix:
        print(row == row)
        # if row == word or row == word[::-1]:
        #    count += 1
        pass

    print(transposed_matrix)

    for row in matrix:
        pass

word_counter(
            [['i', 'v', 'a', 'n'],
             ['e', 'v', 'n', 'h'],
             ['i', 'n', 'a', 'v'],
             ['m', 'v', 'v', 'n'],
             ['q', 'r', 'i', 't']]
)
