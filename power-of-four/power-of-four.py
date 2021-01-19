import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n > 1 and n <= 3:
            return False
        if math.sqrt(n) % 4 == 0:
            return True
        return False






if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(1))