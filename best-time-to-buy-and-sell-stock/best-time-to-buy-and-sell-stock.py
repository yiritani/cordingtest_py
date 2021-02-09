from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_gains = 0
        min_value = prices[0] if prices else 0

        for i in range(1, len(prices)):
            max_gains = max(max_gains, prices[i] - min_value)
            min_value = min(min_value, prices[i])

        return max_gains


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([3,2,6,5,0,3]))