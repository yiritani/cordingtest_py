from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        result = 0
        allowed_set = set([i for i in allowed])
        sets = [set(i) for i in words]

        for i in sets:
            if allowed_set >= i:
                result += 1

        return result


allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]
s = Solution()
print(s.countConsistentStrings(allowed, words))
