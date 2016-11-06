# A function for counting the digits of a number
def sum_of_digits(number):
    result = 0
    number = str(abs(number))
    result = sum([int(n) for n in number])

    return result

print(sum_of_digits(-110))


# Create list with the digits of a number
def to_digits(number):
    return [int(x) for x in str(number)]

print(to_digits(123))


# Create number from array
def to_number(digits):
    result = ''
    for digit in digits:
        result += str(digit)

    return int(result)

print(to_number([1, 2, 3]))


# Count the vowels in a string
def count_vowels(string):
    string = string.lower()
    counter = 0
    # can use string
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'w']

    for s in string:
        if s in vowels:
            counter += 1

    return counter

print(count_vowels('Theistareykjarbunga'))


# Count the consonants in a string
def count_consonants(string):
    string = string.lower()
    number_of_consonants = 0
    consonants = 'bcdfghjklmnpqrstvxz'

    for s in string:
        if s in consonants:
            number_of_consonants += 1

    return number_of_consonants

print(count_consonants('Python'))


# Check if a given number is prime
def prime_number(num):
    if num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                return False

        return True

print(prime_number(5))


# Sum of the factorials of the digits in the number
def fact_digits(n):
    n = str(n)
    total = 0

    for number in n:
        number = int(number)
        factorial = 1

        for i in range(2, number + 1):
            factorial *= i

        total += factorial

    return total

print(fact_digits(999))


# fibonacci sequince
def fibonacci(n):
    result = []
    a = 1
    b = 1
    while len(result) < n:
        result.append(a)
        next_fib = a + b
        a = b
        b = next_fib
    return result

print(fibonacci(2))


def fib_number(n):
    seq = fibonacci(n)
    return ''.join([str(x) for x in seq])

print(fib_number(10))


# Check if a given string is palindrome
def palindrome(string):
    string = str(string)
    reversed_str = string[::-1]

    if string == reversed_str:
        return True
    else:
        return False

print(palindrome('kapak'))


# Dictionary with all characters from a string
def char_histogram(string):
    obj = {}

    for char in string:
        occurences = string.count(char)
        obj[char] = occurences

    return obj

print(char_histogram('AAAAaaa!!!'))
