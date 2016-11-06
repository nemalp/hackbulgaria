import sys
from random import randint


def generate_random_numbers(number):
    return ' '.join([str(randint(1, number)) for n in range(number)])


def create_file(filename, num):
    with open(filename, 'w') as f:
        f.write(generate_random_numbers(int(num)))


def main():
    arguments = sys.argv
    create_file(arguments[1], arguments[2])

if __name__ == '__main__':
    main()
