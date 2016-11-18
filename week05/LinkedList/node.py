class Node:

    def __init__(self, data=None, next_=None, prev=None):
        self.__data = data
        self.__next = next_
        self.__prev = prev

    def __str__(self):
        return str(self.__data)

    def get_prev(self):
        return self.__prev

    def get_next(self):
        return self.__next

    def set_prev(self, prev):
        self.__prev = prev

    def set_next(self, next_):
        self.__next = next_

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data
