import itertools


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


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factorization(n):
    pr_factors = prime_factors(n)
    dict_ = {x: pr_factors.count(x) for x in pr_factors}

    return sorted(list(dict_.items()))


print(prime_factorization(89))


def group(input):
    import re

    string_input = ''.join(str(x) for x in input)
    pattern = re.compile(r'(.)\1*')
    groups = [list(map(int, list(match.group())))
              for match in pattern.finditer(string_input)]


    return groups

print(group([1, 1, 1, 2, 3, 1, 1]))


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

    word = 'ivan'
    count = 0

    rows = 5
    cols = 4

    diags = [[matrix[i-j][j] for j in range(i + 1) if (i - j) < rows and j < cols]
             for i in list(range(rows + cols - 1))]

    for d in diags:
        d = ''.join(d)
        if word in d or word in d[::-1]:
            count += 1

    for row in matrix:
        row = ''.join(row)
        if word in row or word in row[::-1]:
            count += 1

    cols = [list(x) for x in zip(*matrix)]

    for col in cols:
        col = ''.join(col)
        if word in col or word in col[::-1]:
            count += 1


word_counter(
            [['i', 'v', 'a', 'n'],
             ['e', 'v', 'n', 'h'],
             ['i', 'n', 'a', 'v'],
             ['m', 'v', 'v', 'n'],
             ['q', 'r', 'i', 't']]
)
