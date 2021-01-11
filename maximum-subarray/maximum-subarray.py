from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum, total = -2147483647, -2147483647

        for num in nums:
            # tmp = sum + num
            # if num < tmp:
            #     sum = tmp
            # else:
            #     sum = num

            sum = max(num, sum + num)

            # if total < sum:
            #     total = sum

            total = max(total, sum)

        return total

if __name__ == '__main__':
    s = Solution()
    nums = [0]
    print(s.maxSubArray(nums))


