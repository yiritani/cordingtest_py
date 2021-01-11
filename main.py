import hashlib
from typing import Any
from collections import deque


class HashTable(object):

    def __init__(self, size=10) -> None:
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash(self, key) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), base=16) % self.size

    def add(self, key, value) -> None:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                data[1] = value
                break
        else:
            self.table[index].append([key, value])

    def print(self) -> None:
        for index in range(self.size):
            print(index, end=' ')
            for data in self.table[index]:
                print('-->', end=' ')
                print(data, end=' ')

            print()

    def get(self, key) -> Any:
        index = self.hash(key)
        for data in self.table[index]:
            if data[0] == key:
                return data[1]

    def __setitem__(self, key, value) -> None:
        return self.add(key, value)

    def __getitem__(self, key) -> Any:
        return self.get(key)


def reverse(queue) -> deque:
    r = deque()
    while queue:
        r.append(queue.pop())
        # print(queue.pop())
    [queue.append(d) for d in r]
    # return r

if __name__ == '__main__':
    # hash_table = HashTable()
    # hash_table['car'] = 'tesla'
    # # print(hash_table.table)
    # print(hash_table['car'])

    q = deque()
    q.append(1)
    q.append(2)
    q.append(3)
    q.append(4)
    reverse(q)
    print(q)
