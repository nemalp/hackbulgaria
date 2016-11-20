from node import Node


class LinkedList:
    def __init__(self, head=None):
        self.__size = 0
        self.__head = head
        self.__tail = None

    def add_element(self, data):
        new_node = Node(data)

        if not self.size():
            self.__head = self.__tail = Node(data)
            self.__size += 1

            return self.__head

        self.__tail.set_next(new_node)
        self.__tail = new_node
        self.__size += 1

    def index(self, index):
        element = self.__head

        for idx in range(index):
            element = element.get_next()

        return element

    def size(self):
        return self.__size

    def remove(self, idx):
        if self.size() > 0:
            if idx == 0:
                self.__head = self.index(idx + 1)
            else:
                prev_node = self.index(idx - 1)
                next_node = self.index(idx + 1)
                prev_node.set_next(next_node)

            self.__size -= 1

    def to_list(self):
        list_ = []
        element = self.__head

        while element:
            list_.append(element.get_data())
            element = element.get_next()

        return list_

    def add_at_index(self, idx, data):
        if self.size() == 0:
            self.add_first(data)
        else:
            new_node = Node(data)
            prev_node = self.index(idx - 1)
            new_node.set_next(prev_node.get_next())
            prev_node.set_next(new_node)

        self.__size += 1

    def add_first(self, data):
        new_node = Node(data, self.__head)

        if self.__head:
            self.__head.set_prev(new_node)
        self.__head = self.__tail = new_node
        self.__size += 1

    def add_list(self, list_):
        for el in list_:
            self.add_element(el)

    def add_linked_list(self, ll):
        ll = ll.to_list()
        self.add_list(ll)

    def ll_from_to(self, start_index, end_index):
        ll = LinkedList()
        l = []

        for idx in range(start_index, end_index + 1):
            l.append(self.index(idx).get_data())

        ll.add_list(l)

        return ll

    def pop(self):
        el = self.__tail
        self.remove(self.size() - 1)

        return el.get_data()

    def reduce_to_unique(self):
        ll = LinkedList()
        list_ = list(set(self.to_list()))
        ll.add_list(list_)

        return ll
