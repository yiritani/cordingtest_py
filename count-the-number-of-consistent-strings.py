from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for i in words:
            moji = i.split()
            print(moji)
            for j in moji:
                if j in allowed:
                    print(i)



s = Solution()
allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]
s.countConsistentStrings(allowed, words)