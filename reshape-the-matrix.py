from typing import List

class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        renketsu = [i for i in sum(nums, [])]
        num_list = [[] for i in range(r)]
        retsu = 0

        for index, num in enumerate(renketsu):
            num_list[retsu].append(num)
            if (index % r) + 1 == c:
                retsu += 1

        return renketsu



s = Solution()

nums = [[1,2], [3,4]]
r = 2
c = 4
print(s.matrixReshape(nums, r, c))