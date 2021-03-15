from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = []
        for i in range(len(mat)):
            result.append(mat[i][i])
            if (i, i) == (i, (len(mat[i])-1)-i):
                continue
            result.append(mat[i][(len(mat[i])-1)-i])
        return sum(result)


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1],
           [1, 1, 1, 1]]
    print(s.diagonalSum(mat))
