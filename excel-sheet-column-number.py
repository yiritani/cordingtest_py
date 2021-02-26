import string
alpha = string.ascii_uppercase

class Solution:
    def titleToNumber(self, s) -> int:
        result = []
        right = len(s)-1
        kurai = 0

        while right >= 0:
            result.append(((ord(s[right])-64) * (26 ** kurai)))

            right -= 1
            kurai += 1

        return sum(result)

s = Solution()
str = 'AAA'
print(s.titleToNumber(str))