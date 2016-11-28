from collections import deque


class TreeNode:

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self._children = []

    def _add_child(self, child):
        self._children.append(child)

    def _find(self, x, root):
        stack = deque()
        stack.append(root)

        while len(stack):
            current_node = stack.pop()

            if current_node.data == x:
                return current_node

            for child in current_node._children:
                stack.append(child)
