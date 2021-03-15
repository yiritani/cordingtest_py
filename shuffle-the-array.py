from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[i+n])
        return result


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,4,3,2,1]
    n = 4
    s.shuffle(nums, n)