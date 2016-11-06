import sys
import os.path


def read_file(filename):
    with open(filename, 'r') as f:
        file_content = f.read()

    return file_content


def has_arguments():
    return len(sys.argv[1:]) >= 1


def is_filename_valid(filename):
    return os.path.isfile(filename)


def main():
    if has_arguments():
        for filename in sys.argv[1:]:
            if is_filename_valid(filename):
                print(read_file(filename))

            else:
                print('Invalid filename')

    else:
        return 'No arguments provided'


if __name__ == '__main__':
    main()
