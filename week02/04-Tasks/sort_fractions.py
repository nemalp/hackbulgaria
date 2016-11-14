def sort_fractions(fractions):
    fractions = sorted([(i[0] / i[1], i) for i in fractions])

    return [i[1] for i in fractions]


def main():
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))


if __name__ == '__main__':
    main()
