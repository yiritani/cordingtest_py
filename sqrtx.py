import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))

if __name__ == '__main__':
    s = Solution()
    x = 8
    print(s.mySqrt(x))