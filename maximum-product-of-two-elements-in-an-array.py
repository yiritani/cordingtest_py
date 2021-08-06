from itertools import combinations
from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        rev = sorted(nums)[::-1]
        return (rev[0]-1) * (rev[1]-1)




s = Solution()
print(s.maxProduct([3,4,5,2]))