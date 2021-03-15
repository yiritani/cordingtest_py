from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(1, len(nums)+1):
            result.append((sum(nums[0:i])))
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.runningSum([3,1,2,10,1]))