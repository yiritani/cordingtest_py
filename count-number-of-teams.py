from typing import List
from itertools import permutations

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        rating.sort()
        for ran in range(len(rating)):
            for i in permutations(rating[0:ran+1]):
                print(sum(i))



if __name__ == '__main__':
    s = Solution()
    s.numTeams([2,5,3,4,1])