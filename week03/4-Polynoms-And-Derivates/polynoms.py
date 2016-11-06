from format_output import format_str


class Polynom:

    def __init__(self, coef, var, power):
        self.coef = coef
        self.var = var
        self.power = power

    def __str__(self):
        return format_str(self.coef, self.var, self.power)

    def __eq__(self, other):
        if self.coef == other.coef and self.var == other.var and \
                self.power == other.power:
            return True

        return False

    def calc_derivat(self):
        return Polynom(self.coef * self.power, self.var, self.power - 1)


def main():
    pass

if __name__ == '__main__':
    main()
