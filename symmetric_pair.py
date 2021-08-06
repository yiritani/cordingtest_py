from typing import Any, List


def serch_symmetric(input: List) -> List:
    cache = {}
    for pairs in input:
        first, second = pairs[0], pairs[1]
        value = cache.get(second)
        if not value:
            cache[first] = second
        elif value == first:
            yield first, second

if __name__ == '__main__':
    input = [(1, 2), (3, 5), (4, 7), (5, 3), (7, 4)]
    for l in serch_symmetric(input):
        print(l)
