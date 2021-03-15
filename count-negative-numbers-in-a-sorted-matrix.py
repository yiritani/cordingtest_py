from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return len([i for i in sum(grid, []) if i<0])


s = Solution()
grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]

print(s.countNegatives(grid))