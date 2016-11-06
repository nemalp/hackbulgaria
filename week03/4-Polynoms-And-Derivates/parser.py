import re


class Parser:

    def __init__(self, string):
        self.string = string
        self.exp = self.parse_exp()
        self.polynoms = {}

    def get_coef(self, exp):
        if exp == 'x':
            return 1
        return int(exp.split('x')[0])

    def get_power(self, exp):
        if len(exp) > 1:
            return int(exp[len(exp) - 1])
        else:
            if exp[0].isdigit():
                return 0
            else:
                return 1

    def build_dict(self):
        for exp in self.exp:
            power = self.get_power(exp)

            if not exp[0].isdigit():
                if power not in self.polynoms.keys():
                    self.polynoms[power] = [self.get_coef(exp[0])]

                else:
                    self.polynoms[power].append(self.get_coef(exp[0]))

            else:
                if power not in self.polynoms.keys():
                    self.polynoms[power] = [int(x) for x in exp]
                else:
                    self.polynoms[power].append(int(''.join([x for x in exp])))

        return self.polynoms

    def parse_exp(self):
        return [x.split('^') for x in re.split('[+|-]', self.string)]


def main():
    pass

if __name__ == '__main__':
    main()
