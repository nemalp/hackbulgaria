def chain(iterible_one, iterible_two):
    for x in iterible_one:
        yield x

    for y in iterible_two:
        yield y

print(list(chain(range(0, 4), range(4, 8))))
