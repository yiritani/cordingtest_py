from typing import List
import collections

class Solution:
    def maxArea(self, height: List[int]) -> int:
        resultBefore = 0
        resultAfter = 0
        tmp = 0
        i = 0

        while i <= len(height):
            j = i + 1
            while j < len(height):
                if height[i] < height[j]:
                    tmp = height[i] * (j - i)
                elif height[i] > height[j]:
                    tmp = height[j] * (j - i)
                else:
                    tmp = height[i] * (j - i)

                if tmp > resultAfter:
                    resultAfter = tmp

                j += 1
            i += 1

        return resultAfter


if __name__ == '__main__':
    height = [1,0,0,0,1]
    i = Solution.maxArea("", height)
    print(i)
