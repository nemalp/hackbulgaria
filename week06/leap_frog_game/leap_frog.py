import sys
sys.path.insert(0, '/home/c0re/hackbulgaria/week06/DataStructures/')
from node import TreeNode


class Frog(TreeNode):

    def __init__(self, data, parent=None):
        super().__init__(data, parent=None)


def main():
    print(help(Frog))
    pass

if __name__ == '__main__':
    main()
