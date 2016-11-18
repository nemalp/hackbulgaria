from node import Node


class LinkedList:
    def __init__(self, head=None):
        self.__size = 0
        self.__head = head
        self.__tail = None

    def add_element(self, data):
        new_node = Node(data, self.__head)

        if self.size() < 1:
            self.add_first(new_node)

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

    def remove(self, index):
        current_node = self.__head

    def pprint(self):
        pass

    def to_list(self):
        pass

    # add element and index N (Example: ll = [2 => 3 => 4]
    # ll.ad_at_index(1, "New data")
    # ll = [2 => "New data" =>  3 => 4]
    def add_at_index(self, index, data):
        pass

    def add_first(self, data):
        new_node = Node(data, self.__head)

        if self.__head:
            self.__head.set_prev(new_node)
        self.__head = self.__tail = new_node
        self.__size += 1

    def add_list(self, list_: list):
        pass

    def add_linked_list(self, ll):
        pass

    def ll_from_to(self, start_index, end_index):
        pass

    def pop(self):
        pass

    def reduce_to_unique(self):
        pass

ll = LinkedList()
ll.add_first(1)
ll.add_element(2)
ll.add_element(3)
