from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        result = [[] for i in range(len(rowSum))]
        for i in rowSum:
            for j in range(i):




rowSum = [3, 8]
colSum = [4, 7]
s = Solution()
s.restoreMatrix(rowSum,colSum)