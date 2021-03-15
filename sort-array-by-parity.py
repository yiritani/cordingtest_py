from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd, even = [], []
        for i in A:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        return even + odd


def create_data():
    aiueo = [i for i in range(10)]
    ueoai = [i for i in range(80)]
    if aiueo == ueoai:
        return True



s = Solution()
n = [3,1,2,4]
print(s.sortArrayByParity(n))