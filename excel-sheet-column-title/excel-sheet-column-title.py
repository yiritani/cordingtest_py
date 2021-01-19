class Solution:
    def convertToTitle(self, n: int) -> str:
        sum = ""
        while n:

            sum = chr(ord('A') + ((n-1) % 26)) + sum
            n = (n - 1) // 26
        return sum

if __name__ == '__main__':
    example = 52
    s = Solution()
    print(s.convertToTitle(example))
