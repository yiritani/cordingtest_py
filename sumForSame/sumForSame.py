from typing import List, Tuple, Optional


class Solution(object):

    def get_param(self, numbers: List[int], target: int) -> Optional[Tuple[int, int]]:
        cache = set()
        for num in numbers:
            val = target - num
            if val in cache:
                return val, num
            cache.add(num)

    def get_param_half(self, numbers: List[int]) -> Optional[Tuple[int, int]]:
        sum_numbers = sum(numbers)

        half_sum, remainder = divmod(sum_numbers, 2)
        if remainder != 0:
            return

        cache = set()
        for num in numbers:
            val = half_sum - num
            if val in cache:
                return val, num
            cache.add(num)


if __name__ == '__main__':
    s = Solution()
    print(s.get_param([11, 2, 5, 9, 10, 3], 12))
    print(s.get_param_half([11, 2, 5, 9, 10, 3]))
