from typing import List
from itertools import combinations


class Solution:
    def threeSum(self, nums: List[int], target) -> List[List[int]]:
        result = []

        for i in combinations(nums, 4):
            tmp_list = list(i)

            print(tmp_list)
            if sum(i) == target:
                tmp_list.sort()
                for j in result:
                    if j == tmp_list:
                        break
                else:
                    result.append(tmp_list)

        return result


s = Solution()

nums = [-490,-481,-471,-467,-453,-450,-446,-440,-437,-424,-423,-391,-384,-373,-358,-332,-318,-314,-311,-309,-299,-279,-270,-257,-243,-208,-205,-171,-153,-147,-142,-138,-129,-99,-20,-19,17,30,44,82,86,93,122,125,138,139,158,169,175,181,199,200,203,203,205,225,248,272,277,306,334,335,337,338,342,344,359,396,403,405,412,434,437,439,440,441,443,446,446,457,465,468,473,496]
target = 1896
print(s.threeSum(nums, target))

# https://leetcode.com/problems/3sum/