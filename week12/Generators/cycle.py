import itertools


def cycle(iterable):

    '''
    for element in itertools.cycle(iterable):
        yield element
    '''
    while True:
        for x in iterable:
            yield x


endless = cycle(range(0, 10))

for item in endless:
    print(item)
