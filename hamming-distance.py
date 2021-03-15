import math

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        print(int(bin(x)[2:])%x)
        print(int(bin(y)[2:])%y)





x = 1
y = 4
s = Solution()
s.hammingDistance(x,y)
