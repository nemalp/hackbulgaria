def is_credit_card_valid(number):
    number = list(str(number))
    length = len(number)

    for i in range(length):
        if i % 2 != 0:
            number[i] = int(number[i]) * 2

    number = ''.join([str(x) for x in number])
    total = sum(map(int, number))

    return True if total % 10 == 0 else False

    '''
    doubled_odd_numbers = [int(str(number)[n]) * 2
                           for n in range(len(str(number))) if n % 2 != 0]

    even_numbers = [int(str(number)[n])
                    for n in range(len(str(number))) if n % 2 == 0]

    new_number = ''.join(map(str, even_numbers + doubled_odd_numbers))
    total = sum(map(int, new_number))

    return True if total % 10 == 0 else False
    '''

print(is_credit_card_valid(79927398713))
