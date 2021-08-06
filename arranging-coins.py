import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        print(math.factorial(n) / n)



s = Solution()
n = 8
print(s.arrangeCoins(n))


# https://leetcode.com/problems/arranging-coins/