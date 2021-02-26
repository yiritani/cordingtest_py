import collections

def search(strs):
    a,g,t,c = 0,0,0,0
    for i in strs:
        if i == 'a':
            a += 1
        if i == 'g':
            g += 1
        if i == 't':
            t += 1
        if i == 'c':
            c += 1

    print(g / (a+g+c+t))

def search2(strs):
    c = collections.Counter(strs)
    print(c['g'] / (c['a'] + c['g'] + c['t'] + c['c']))

import time


s = [i for j in range(10000000) for i in 'agtc']
start = time.time()
search(''.join(s))
print(time.time() - start)

start = time.time()
search2(''.join(s))
print(time.time() - start)
