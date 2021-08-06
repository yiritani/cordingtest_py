from typing import List
from collections import Counter

def pop_few_number(x: List[int], y: List[int]) -> None:
    xdic , ydic = Counter(x), Counter(y)

    for k in xdic:
        if ydic.get(k):
            if xdic[k] < ydic[k]:
                x[:] = [i for i in x if i != k]
            elif xdic[k] > ydic[k]:
                y[:] = [i for i in y if i != k]

if __name__ == '__main__':
    x = [1,2,3,4,4,5,5,8,10]
    y = [4,5,5,5,6,7,8,8,10]
    pop_few_number(x,y)
    print(x)
    print(y)
