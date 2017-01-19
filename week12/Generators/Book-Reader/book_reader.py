import zipfile
import getch


def book_reader():
    with zipfile.ZipFile('Book.zip') as z:
        zip_content = [f.filename for f in z.infolist()]

    for file_ in zip_content:
        with open(file_, 'r') as f:
            line = f.readline()

            while line:
                result = ''
                if str(line).startswith('#'):
                    line = f.readline()

                    while str(line).startswith('#') is False:
                        result += line
                        line = f.readline()

                    yield result

                line = f.readline()  # chapter

book = book_reader()

for chapter in book:
    space = getch.getch() == ' '
    # enter = getch.getch() == '\n'
    if space:
        print(chapter)
