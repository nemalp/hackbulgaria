import sys
from cat import read_file


def sum_numbers(filename):
    file_content = read_file(filename)

    return sum([int(x) for x in file_content.split()])


def main():
    arguments = sys.argv
    print(sum_numbers(arguments[1]))

if __name__ == '__main__':
    main()
