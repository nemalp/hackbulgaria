def format_str(coef, var, power):

    if power == 0:
        return str(coef)

    if coef == 0:
        return '0'

    if power == 1 and coef == 1:
        return str(var)

    if power == 1:
        return '{0}*{1}'.format(coef, var)

    if coef == 1:
        return '{0}^{1}'.format(var, power)

    return '{0}*{1}^{2}'.format(coef, var, power)


def main():
    pass


if __name__ == '__main__':
    main()
