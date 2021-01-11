from typing import List
import numpy as np

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i, v in enumerate(nums):
        #     if v == target:
        #         return i
        #     if v > target:
        #         return i
        #
        # return len(nums)

        # nums = np.array(nums)
        return np.searchsorted(nums, target)





if __name__ == '__main__':
    s = Solution()
    nums = [1]
    target = 0
    print(s.searchInsert(nums,target))
