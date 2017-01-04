from collections import deque
from panda import Panda


class PandaSocialNetwork:

    def __init__(self):
        self.graph = {}

    def get_pandas(self):
        return list(self.graph.keys())

    def has_panda(self, panda):
        return panda in self.graph

    def add_panda(self, panda):
        if self.has_panda(panda):
            return

        self.graph[panda] = set()

    def make_friends(self, panda1, panda2):
        self.add_panda(panda1)
        self.add_panda(panda2)

        self.graph[panda1].add(panda2)
        self.graph[panda2].add(panda1)

    def are_friends(self, panda1, panda2):
        check1 = panda1 in self.graph[panda2]
        check2 = panda2 in self.graph[panda1]

        if (check1 and not check2) or (check2 and not check1):
            raise AssertionError('Something is wrong with the Graph')

        return check1 and check2

    def friends_of_panda(self, panda):
        if panda not in self.graph.keys():
            return False

        return self.graph[panda]

    def connection_level(self, start: Panda, target: Panda):
        q = deque()
        visited = set()
        paths = {start: None}

        q.append((0, start))
        visited.add(start)

        while q:
            level, current = q.popleft()

            if current == target:
                path = []

                while target is not None:
                    path.append(target)
                    target = paths[target]

                return (level, list(reversed(path)))

            for neighbour in self.graph[current]:
                if neighbour not in visited:
                    q.append((level + 1, neighbour))
                    visited.add(neighbour)
                    paths[neighbour] = current

        return -1

    def are_connected(self, panda1, panda2):
        return self.connection_level(panda1, panda2) != -1

    def how_many_gender_in_network(self, level, panda, gender):
        pass
