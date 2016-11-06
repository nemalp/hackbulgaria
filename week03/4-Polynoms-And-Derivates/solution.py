import sys
from parser import Parser
from polynoms import Polynom


def print_output():
    string = sys.argv[1]
    parser = Parser(string)
    dict_ = parser.build_dict()
    polynoms = []
    derivatives = []

    for power in dict_:
        coef = sum(dict_[power])
        p = Polynom(coef, 'x', power)
        d = Polynom(coef, 'x', power).calc_derivat()

        if len(dict_) == 1 and power == 0:
            derivatives.insert(0, str(d))
            pass

        if power != 0:
            polynoms.insert(0, str(p))
            d = Polynom(coef, 'x', power).calc_derivat()
            derivatives.insert(0, str(d))

        else:
            polynoms.append(str(p))
    print(dict_)

    print("The derivative of f(x) = {} is:".format(' + '.join(polynoms)))
    print("f'(x) = {}".format(' + '.join(derivatives)))


def main():
    print_output()

if __name__ == '__main__':
    main()
