from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        result, duplicate = [], []
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                duplicate.append(nums[i])
        for i in nums:
            if i not in duplicate:
                result.append(i)
        return sum(result)



s = Solution()
n = [1,2,3,2]
print(s.sumOfUnique(n))