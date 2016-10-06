import re

input_string = input("Enter a string: ")


def strings_and_numbers(input_string):
    data = []
    result = 0

    for ch in input_string:
        data.append([ch, input_string.count(ch)])

    unique_data = [list(x) for x in set(tuple(x) for x in data)]
    unique_data.sort(key=lambda x: x[1], reverse=True)

    counter = 9

    for item in unique_data:
        item[1] = counter
        counter -= 1

    unique_data = unique_data[:10]

    for el in unique_data:
        input_string = input_string.replace(el[0], str(el[1]))

    numbers = re.findall('(\d+)', input_string)

    for n in numbers:
        result += int(n)

    return result

# print(strings_and_numbers(input_string))
