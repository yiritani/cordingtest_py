from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for i in range(1, right):
            print(right,i,right%i)




s = Solution()
left = 1
right = 22
s.selfDividingNumbers(left, right)
