from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        end = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[end] = s[end], s[i]
            end -= 1


sol = Solution()
s = ["H","a","n","n","a"]
sol.reverseString(s)
print(s)
