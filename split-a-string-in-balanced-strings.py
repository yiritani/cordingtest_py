class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = []
        last_index = 0
        cnt = 0

        for i, k in enumerate(s):

            for j in range(i, len(s)):
                if s[i] == s[j]:
                    cnt += 1

                elif s[i] != s[j]:
                    cnt -= 1

                if cnt == 0:
                    print(s[i], s[j], cnt)
                    break



sl = Solution()
s = "RLRRRLLRLL"
sl.balancedStringSplit(s)
