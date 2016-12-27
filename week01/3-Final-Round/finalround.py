import re


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
    is_up = all(x < y for x, y in zip(seq, seq[1:]))
    is_down = all(x > y for x, y in zip(seq, seq[1:]))

    if is_up:
        return 'Up!'
    elif is_down:
        return 'Down!'
    else:
        return False

print(increasing_or_decreasing([9, 8, 7, 6]))


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


key_combinations = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def numbers_to_message(pressed_sequence):
    is_upper = False
    pattern = re.compile(r'(\-?\d)\1*')
    string = ''.join([str(x) for x in pressed_sequence])

    result = [match.group() for match in pattern.finditer(string)]
    message = ''

    for el in result:
        key = el[0]

        if key == '0':
            message += ' '

        elif key in key_combinations.keys():
            if len(el) > len(key_combinations[key]):
                if key == '7' or key == '9':
                    idx = (len(el) % 4) - 1

                else:
                    idx = (len(el) % 3) - 1
            else:
                idx = len(el) - 1

            if is_upper:
                message += key_combinations[key][idx].upper()
                is_upper = False
            else:
                message += key_combinations[key][idx]

        if key == '1':
            is_upper = True

    print(message)

numbers_to_message([2, 2, 2, 2])
numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2])
numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0,
                    3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2])


def map_letters_to_numbers(keyboard: dict):
    dict_ = {}

    for key, val in keyboard.items():
        for idx, letter in enumerate(val):
            dict_[letter] = key * (idx+1)

    return dict_


def message_to_numbers(message):
    letters_to_numbers = map_letters_to_numbers(key_combinations)
    numbers = []
    result = []

    for letter in message:
        if letter.isupper():
            numbers.append('1')
            numbers.append(list(letters_to_numbers[letter.lower()]))
        elif letter == ' ':
            numbers.append('0')
        else:
            numbers.append(list(letters_to_numbers[letter]))

    for n in range(len(numbers)):
        result.append(numbers[n])
        if n + 1 < len(numbers) and numbers[n][0] == numbers[n+1][0]:
            result.append(['-1'])

    result = [int(y) for x in result for y in x]
    return result

message_to_numbers('aabbcc')
message_to_numbers('Ivo e Panda')
message_to_numbers('abc')
