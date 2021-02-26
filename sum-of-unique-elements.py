from typing import List

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sum = 0
        tmp = nums[0]
        nums.sort()
        for i,v in enumerate(nums):
            if nums[i] == nums[i+1]:
                nums.pop(i)




s = Solution()
n = [1,2,3,2]
print(s.sumOfUnique(n))