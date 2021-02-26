from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cache, ans = {}, []

        for s in strs:
            key = tuple(sorted(s))
            if key in cache:
                cache[key].append(s)
            else:
                cache[key] = [s]

        for key in cache:
            ans.append(cache[key])

        return ans


s = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(strs))