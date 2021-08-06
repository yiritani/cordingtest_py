from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        indexes = {i for i in range(len(nums))}

        for iIndex, iVal in enumerate(nums):
            ind = indexes - {iIndex}
            cnt = 0
            for j in ind:
                if iVal > nums[j]:
                    cnt += 1
            else:
                result.append(cnt)
        return result
