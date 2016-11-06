import math


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        self.value = self.numerator / self.denominator

    def __str__(self):
        if self.numerator / self.denominator == float(
            self.numerator // self.denominator):

            return str(self.numerator)

        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False

        return self.value == other.value

    def __add__(self, other):
        return simplify_fraction(Fraction(
                        self.numerator * other.denominator +
                        other.numerator * self.denominator,
                        self.denominator * other.denominator))

    def __sub__(self, other):
        if self.denominator != other.denominator:
            return simplify_fraction(Fraction(
                            self.numerator * other.denominator -
                            other.numerator * self.denominator,
                            self.denominator * other.denominator))

    def __mul__(self, other):
        return Fraction(
            self.numerator * self.numerator,
            self.denominator * self.denominator)


def simplify_fraction(fraction):
    gcd_ = math.gcd(fraction.numerator, fraction.denominator)

    return Fraction(fraction.numerator // gcd_, fraction.denominator // gcd_)

def main():

    a = Fraction(1, 2)
    b = Fraction(2, 4)

    print(a == b)  # True
    print(a + b)  # 1
    print(a - b)  # 0
    print(a * b)  # 1 / 4


if __name__ == '__main__':
    main()
