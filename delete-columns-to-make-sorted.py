from typing import List
import D



class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        for i in strs:
            tmp = list(i)
            if sum([ord(i) for i in tmp]) % 3 != 0:
                cnt += 1
        return cnt

s = Solution()
print(s.minDeletionSize(["zyx","wvu","tsr"]))