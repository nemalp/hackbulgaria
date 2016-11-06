import sys


def count(text, element):
    if element == 'words':
        count = len(text.split())

    elif element == 'chars':
        count = len(text)

    else:
        count = text.count('\n')

    return count


def main():
    arguments = sys.argv
    filename = arguments[1]
    element = arguments[2]

    with open(filename, 'r') as f:
        text = f.read()

    print(count(text, element))

if __name__ == '__main__':
    main()
