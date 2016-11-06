def is_number_balanced(n):
    n = str(n)
    middle = len(n) // 2
    left_part = sum([int(x) for x in n[:middle]])

    if len(n) % 2 != 0:
        right_part = sum([int(x) for x in n[middle:][1:]])
    else:
        right_part = sum([int(x) for x in n[middle:]])

    if right_part == left_part:
        return True
    else:
        return False

print(is_number_balanced(1238033))


def increasing_or_decreasing(seq):
    is_up = all(x<y for x, y in zip(seq, seq[1:]))
    is_down = all(x>y for x, y in zip(seq, seq[1:]))

    if is_up:
        return 'Up!'
    elif is_down:
        return 'Down!'
    else:
        return False

print(increasing_or_decreasing([9,8,7,6]))


def get_largest_palindrome(number):
    for n in range(number - 1, 0, -1):
        n = str(n)
        if n == n[::-1]:
            return n
            break

print(get_largest_palindrome(994687))


def sum_of_numbers(string):
    import re
    numbers = sum([int(x) for x in re.findall('(\d+)', string)])

    return numbers

print(sum_of_numbers('ab12'))


def birthday_ranges(birthdays, ranges):
    result = []

    for r in ranges:
        start = r[0]
        end = r[1]
        counter = 0

        for birthday in birthdays:
            if start <= birthday <= end:
                counter += 1

        result.append(counter)

    return result


print(birthday_ranges([1, 2, 3, 4, 5],
                      [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


def numbers_to_message(pressed_sequence):
    print(pressed_sequence)

numbers_to_message([2, 2, 2, 2])
