from typing import Tuple
from collections import Counter

def count_char(chars: str) -> Tuple:
    # cache = {}
    # chars = chars.replace(" ", "", -1).lower()
    # for char in chars:
    #     if char not in cache:
    #         cache[char] = 1
    #     else:
    #         cache[char] += 1
    #
    # return max(cache, key=cache.get), max(cache.values())

    cache = Counter()
    chars = chars.lower()
    for char in chars:
        if not char.isspace():
            cache[char] += 1
    max_char = max(cache, key=cache.get)

    return max_char, cache[max_char]


if __name__ == '__main__':
    s = 'This is a pen. This is an apple. Applepen.'
    print(count_char(s))
