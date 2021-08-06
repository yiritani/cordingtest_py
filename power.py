import math

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False

        if n < 0:
            n = -n
        a = n / math.sqrt(n)

        if a == 1:
            return True

        print(n,a,math.sqrt(a), int(a*4))

        if (a * 4) % 4 == 0:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfFour(-225))


