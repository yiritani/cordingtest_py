from typing import List
from itertools import combinations
from collections import defaultdict

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        listRange = [i for i in range(0,len(rating))]
        result = defaultdict(int)
        for i in combinations(listRange, 3):
            result[rating[i[0]] + rating[i[1]] + rating[i[2]]] += 1
            print(rating[i[0]], rating[i[1]], rating[i[2]], rating[i[0]] + rating[i[1]] + rating[i[2]])

        print(result)


if __name__ == '__main__':
    s = Solution()
    s.numTeams([2,5,3,4,1])