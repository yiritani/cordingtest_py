from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island = 1
        for ii, iv in enumerate(grid):
            for ji, jv in enumerate(iv):
                # print(ii, ji, jv)
                if ii == 0 or ii == len(grid):
                    break
                # print(grid[ii][ji])
                if 0 < int(grid[ii][ji]) < len(grid):
                    # print(grid[ii-1][ji])
                    # print(grid[ii][ji-1])
                    # print(grid[ii][ji+1])
                    # print(grid[ii+1][ji])
                    if max(int(grid[ii-1][ji]), int(grid[ii][ji-1]), int(grid[ii][ji+1]), int(grid[ii+1][ji])) == 0:
                        island += 1

        return island


s = Solution()
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

s.numIslands(grid)