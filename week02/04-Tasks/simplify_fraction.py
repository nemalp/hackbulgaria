import math


def simplify_fraction(fraction):
    gcd_ = math.gcd(fraction[0], fraction[1])

    return fraction[0] // gcd_, fraction[1] // gcd_


def main():
    print(simplify_fraction((63, 462)))

if __name__ == '__main__':
    main()
