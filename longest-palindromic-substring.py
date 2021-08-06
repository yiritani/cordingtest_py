
class Solution:
    def longestPalindrome(self, s: str) -> str:
        order, reverse = [], []
        cnt = 0
        result = ""

        for i in s:
            order.append(i), reverse.append(i)
            while cnt < len(s):
                reverse_cnt = len(reverse)-1
                if order[cnt] == reverse[reverse_cnt]:
                    cnt += 1
                    order.append(s[cnt])
                    reverse.append(s[cnt])

                else:
                    cnt += 1






if __name__ == '__main__':
    l = "babad"
    Solution.longestPalindrome("", l)