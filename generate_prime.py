def prime_v1(num):
    result = []
    cnt = 0
    for i in range(2, num):
        for j in range(2, i):
            cnt += 1
            if i % j == 0:
                break
        else:
            result.append(i)
    print(result)
    print(cnt)


def prime_v2(num):
    result = [2]
    cnt = 0
    for i in range(3, num):
        if i % 2 == 0:
            continue
        for j in range(3, i, 2):
            cnt += 1
            if i % j == 0:
                break
        else:
            result.append(i)
    print(result)
    print(cnt)


def prime_v3(num):
    result = []
    cache = {}
    cnt = 0
    for i in range(2, num):
        is_prime = cache.get(i)
        if is_prime is False:
            continue
        result.append(i)
        for j in range(i * 2, num + 1, i):
            cnt += 1
            cache[j] = False
    print(result)
    print(cnt)


import time

start = time.time()
prime_v1(10000)
print(f'v1:{time.time() - start}')

start = time.time()
prime_v2(10000)
print(f'v2:{time.time() - start}')

start = time.time()
prime_v3(10000)
print(f'v3:{time.time() - start}')
