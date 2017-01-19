def compress(iterable, mask):
    for x in zip(iterable, mask):
        if x[1] is True:
            yield x[0]

print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
