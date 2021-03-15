from typing import List
from collections import defaultdict

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        result = []
        data = defaultdict(list)
        for i, k in enumerate(groupSizes):
            data[k].append(i)
        # print(data.items())

        for i in data.items():
            start, end = 0, i[0]
            for j in range(len(i[1]) // i[0]):
                result.append(i[1][start:end])
                start += i[0]
                end += i[0]

        return result



s = Solution()
print(s.groupThePeople([3,3,3,3,3,1,3]))
