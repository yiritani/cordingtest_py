from typing import List
from itertools import permutations

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        are = []
        for i in permutations(nums):
            print(i)
            # are.append(((i[0], i[1]), (i[2], i[3])))
            # print(are)


if __name__ == '__main__':
    s = Solution()
    nums = [6,2,6,5,1,2]
    s.arrayPairSum(nums)
