from functools import lru_cache
import time


def long_func(i):
    s = None
    for j in range(1000000):
        s += j * i
    print(s)


if __name__ == '__main__':
    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)

    start = time.time()
    for i in range(10):
        print(long_func(i))
    print(time.time() - start)