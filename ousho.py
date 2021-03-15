import random
from collections import Counter
import collections

def chumon(aaa):
    result = []
    for j in range(10):
        for i in range(100):
            # print(aaa[random.randint(1,4)])
            result.append(aaa[random.randint(1,4)])

    print(collections.Counter(result))
    c = collections.Counter(result)

    saisho = []
    for i, k in c.items():
        # print(i,k)
        if (k * 13) % 3 == 0:
            saisho.append(i)
            # return i
    if len(saisho) <= 1:
        return saisho

    for i, k in c.items():
        moji = str(k)
        if moji[-1] == '3':
            return i

    return 'raisu'


koho = {1:'chili', 2:'subuta', 3:'hoikoro', 4:'yakisoba' ,5:'rice'}
print(chumon(koho))