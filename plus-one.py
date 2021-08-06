from typing import List
from collections import deque

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length_digits = len(digits)
        num = ""
        for s in digits:
            num += str(s)

        result = int(num) + 1

        result_list = deque()
        for i in range(len(str(result))):
            result_list.append(int(str(result)[i]))

        if length_digits > len(result_list):
            for _ in range(length_digits - 1):
                result_list.appendleft(0)

        return list(result_list)

if __name__ == '__main__':
    s = Solution()
    digits = [0,9,9]
    print(s.plusOne(digits))