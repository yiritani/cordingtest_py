from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        for i in accounts:
            result.append(sum(i))
        return max(result)


if __name__ == '__main__':
    s = Solution()
    accounts = [[1,5],[7,3],[3,5]]
    print(s.maximumWealth(accounts))
