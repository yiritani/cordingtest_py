from typing import List
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return len(list(Counter(arr).values())) == len(list(set(list(Counter(arr).values()))))


arr = [-3,0]
s = Solution()
print(s.uniqueOccurrences(arr))