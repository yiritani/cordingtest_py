from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = [0]
        for i in range(1, n):
            if i % 2 != 0:
                result.append(i+1)
            else:
                result.append(-i)
        if len(result) % 2 == 0:
            result[0] = -result[len(result)-1]
        return result



s = Solution()
n = 4
print(s.sumZero(n))