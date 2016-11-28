import os
import sys
sys.path.insert(0, '/home/c0re/hackbulgaria/week06/DataStructures/')
from pprint import pprint
from tree import Tree


def fill_tree(fs, path):
    for el in os.scandir(path):
        fs.add_child(path, el.path)

        if el.is_dir(follow_symlinks=False):
            fill_tree(fs, el.path)



def flatten_file_system1(path):
    fs = Tree(path)
    fill_tree(fs, path)

    result = [path for path in sorted(fs.tree_levels()[1])]
    result.insert(0, fs.root.data)

    all_levels = [path for sublist in sorted(fs.tree_levels())
           for path in sublist]

    for path in all_levels:
        if path not in result:
            result.append(path)

    return result

def flatten_file_system2(path):
    fs = Tree(path)
    fill_tree(fs, path)

    result = [path for sublist in fs.tree_levels()
           for path in sublist]

    return sorted(result)


def main():
    pprint(flatten_file_system1('/home/c0re/courses/personal'))
    print('\n')
    pprint(flatten_file_system2('/home/c0re/courses/personal'))

if __name__ == '__main__':
    main()
