class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        endF = False
        for i in s:
            if i == '(' and endF is True:
                cnt += 1
            elif i == '(' and endF is False:
                endF = True
            elif i == ')' and endF is True:
                endF = False

        print(cnt)

s = Solution()
s.maxDepth("1+(2*3)/(2-1)")