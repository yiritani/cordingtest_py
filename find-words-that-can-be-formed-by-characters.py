from collections import Counter
from typing import List
from itertools import permutations

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result_sum = 0

        for i in words:
            flag = True
            words_cnt = Counter(i)
            chars_cnt = Counter(chars)
            for j in i:
                if not chars_cnt[j] >= words_cnt[j]:
                    flag = False
            if flag is True:
                result_sum += len(i)

        print(result_sum)

if __name__ == '__main__':
    s = Solution()
    s.countCharacters(["hello","world","leetcode"], "welldonehoneyr")