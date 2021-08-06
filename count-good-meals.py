from typing import List

import numpy as np


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers2=set([2**i for i in range(22)])
        deliciousness.sort()
        n=len(deliciousness)
        answ=0
        d={}
        for x in deliciousness:
            if x in d: d[x]+=1
            else: d[x]=1
        dKeys=list(d.keys())
        dValues=list(d.values())
        N=len(dKeys)
        for i in range(N):
            k=dKeys[i]
            v=dValues[i]
            if v>1 and k in powers2: answ+=v*(v-1)
            a=0
            for p2 in powers2:
                q=p2-k
                if q!=k and q in d:
                    a+=d[q]
            answ+=a*v
        answ//=2
        return answ % (10**9+7)



if __name__ == '__main__':
    deliciousness = [2160,1936,3,29,27,5,2503,1593,2,0,16,0,3860,28908,6,2,15,49,6246,1946,23,105,7996,196,0,2,55,457,5,3,924,7268,16,48,4,0,12,116,2628,1468]
    deliciousness = [1,3,5,7,9]
    print(Solution.countPairs("",deliciousness))
