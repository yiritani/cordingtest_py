from itertools import permutations
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in permutations(nums):
            result.append(i)
        return result




nums = [1, 2, 3]
s = Solution()
print(s.permute(nums))



