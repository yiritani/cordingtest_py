class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            idx = haystack.find(needle)
            return idx
        else:
            return -1


if __name__ == '__main__':
    s = Solution()
    haystack = ""
    needle = ""
    print(s.strStr(haystack, needle))
