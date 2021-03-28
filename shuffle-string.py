from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        result = [[] for i in range(len(indices))]
        for index, i in enumerate(indices):
            result[i] = s[index]
        return ''.join(result)



ll = Solution()
s = "aaiougrt"
indices = [4,0,2,6,7,3,1,5]
print(ll.restoreString(s,indices))


k = 'Hello'
print(k.lower())