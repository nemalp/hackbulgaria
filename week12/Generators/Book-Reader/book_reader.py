import zipfile
from getch import getch


def book_reader():
    with zipfile.ZipFile('Book.zip') as z:
        zip_content = [f.filename for f in z.infolist()]

        for file_ in zip_content:
            with z.open(file_, 'r') as f:
                line = f.readline().decode('utf-8')

                while line:
                    result = ''
                    result += line
                    line = f.readline().decode('utf-8')

                    while str(line).startswith('#') is False and \
                            str(line) != '':
                        result += line
                        line = f.readline().decode('utf-8')

                    yield result

book = book_reader()

for chapter in book:
    space = getch()
    if space == ' ':
        print(chapter)
