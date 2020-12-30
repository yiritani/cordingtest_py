from typing import List
import math

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        docking = nums1 + nums2
        docking.sort()

        if len(docking) % 2 != 0:
            median = docking[math.floor((len(docking) - 1) / 2)]
            return float(median)

        if len(docking) % 2 == 0:
            first = math.floor((len(docking)) / 2)
            second = math.floor((len(docking)) / 2 - 1)
            median = (docking[first] + docking[second]) / 2
            return float(median)


if __name__ == '__main__':
    nums1 = [1,2]
    nums2 = [3,4]
    findMedianSortedArrays("",nums1, nums2)

