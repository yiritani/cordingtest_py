from typing import List

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        cnt = len(arr)-1
        tmp = arr[cnt] - arr[cnt-1]
        while cnt > 0:
            minus = arr[cnt] - arr[cnt-1]

            if tmp != minus:
                return False
            tmp = minus
            cnt -= 1

        return True


if __name__ == '__main__':
    arr = [3, 5, 1]
    # arr = [0, 0, 0, 0]
    # arr = [1,2,0]
    # arr = [1, 2, 4]
    s = Solution()
    print(s.canMakeArithmeticProgression(arr))