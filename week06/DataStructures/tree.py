from collections import deque
from node import TreeNode


class Tree:

    def __init__(self, root):
        self.root = TreeNode(root)
        self.nodes = 1

    def add_child(self, parent, child):
        tree_node = self.root._find(parent, self.root)
        tree_node._add_child(TreeNode(child))
        self.nodes += 1

    def find(self, x):
        return bool(self.root._find(x, self.root))

    def height(self):
        return len(self.tree_levels()) - 1

    def count_nodes(self):
        return self.nodes

    def tree_levels(self):
        q = deque()
        q.append(self.root)
        res = []
        res.append([self.root.data])

        while len(q):
            current = q.popleft()

            if current._children:
                current_lv_children = [child.data
                                       for child in current._children]

                res.append(current_lv_children)

            for child in current._children:
                q.append(child)

        return res

    """
    Returns a list of lists with the nodes foe each level1
    tree.tree_levels = [[5], [4, 3], [2]]
    """


def main():
    t = Tree(5)
    t.add_child(5, 4)
    t.add_child(5, 3)
    t.add_child(4, 2)
    print(t.height())
    print(t.count_nodes())

    # Works only with unique elements
    print(t.tree_levels())

if __name__ == '__main__':
    main()
