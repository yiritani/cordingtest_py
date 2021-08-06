class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        result = 0
        extra = 0
        new = 0

        for key, val in dic.items():
            if len(dic) == 1:
                return val

            elif val % 2 == 0:
                result += val

            elif val % 2 != 0:
                extra = 1
                new += val - 1

        return (result + extra + new)


if __name__ == '__main__':
    ss = Solution()
    s = "abaacc"
    print(ss.longestPalindrome(s))