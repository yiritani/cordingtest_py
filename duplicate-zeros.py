from typing import List
from collections import deque

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        print(deque(arr))
        for i in arr:
            arr.insert(9)

if __name__ == '__main__':
    s = Solution()
    arr = [1,0,2,3,0,4,5,0]
    s.duplicateZeros(arr)
    print(arr)