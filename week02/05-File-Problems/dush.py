import sys
import os
from os.path import join, getsize


def get_path(path):
    return path


def main():
    path = get_path(sys.argv[1])
    total_size = 0

    for root, dirs, files in os.walk(path):
        for f in files:
            filepath = join(root, f)
            total_size += getsize(filepath)

    print(total_size)


if __name__ == '__main__':
    main()
