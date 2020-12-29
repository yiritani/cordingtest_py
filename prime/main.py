import math

def is_prime_v1(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

def is_prime_v2(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for i in range(2, math.floor(math.sqrt(num) + 1)):
        if num % i == 0:
            return False

    return True

def is_prime_v3(num: int) -> bool:
    if num <= 1:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    i = 3
    while i * i <=num:
        if num % i == 0:
            return False
        i += 2

    return True

if __name__ == '__main__':
    primeList = [2,3,5,7,11,13,17,19]
    nonPrimeList = [1,4,6,8,9,10,12,14,15,16,18,20]

    import time
    import random

    numbers = [random.randint(0,1000) for _ in range(100000)]
    start = time.time()

    for i in numbers:
        bool = is_prime_v1(i)
    print('v1', time.time()-start)

    start = time.time()
    for i in numbers:
        bool = is_prime_v2(i)
    print('v2', time.time()-start)

    start = time.time()
    for i in numbers:
        bool = is_prime_v3(i)
    print('v3', time.time()-start)