import sys


def main():
    input_ = [x.rstrip() for x in sys.stdin if x.rstrip() != '']
    type_signatures = {}
    composition = tuple(input_[-1].split(' . '))

    for n in range(len(input_) - 1):
        func_def = input_[n].split()
        fname = func_def[0]
        type1 = func_def[2]
        type2 = func_def[4]

        if fname not in type_signatures.keys():
            type_signatures[fname] = (type1, type2)

    for idx, f in enumerate(composition):
        func = type_signatures[f]
        func_input_type = func[0]

        if idx + 1 < len(composition):  # ensure we are still in range
            next_func = type_signatures[composition[idx + 1]]
            next_func_return_type = next_func[1]

            if func_input_type != next_func_return_type:
                return False

    return True


if __name__ == '__main__':
    print(main())
