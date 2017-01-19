import string
from random import choice, randint


def generate_word():
    word = ''.join([choice(string.ascii_letters)
                    for w in range(randint(2, 10))])
    return word


def book_generator(chapters=10, length_range=30):
    for i in range(1, chapters):
        chapter = '# Chapter {}\n'.format(i)

        for _ in range(length_range):
            chapter += generate_word() + ' '

        with open('random_chapters.txt', 'a') as f:
            f.write(chapter+'\n')

book_generator()
