
class Solution():
    def min_move(self,nums):
        return sum(nums) - min(nums) * len(nums)

if __name__ == '__main__':
    s = Solution()
    print(s.min_move([1,2222222222]))
