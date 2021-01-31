from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        total_length = len(matrix[0]) * len(matrix)

        result = []
        right_index, left_index, ceeling_index, bottom_index = len(matrix[0])-1,0,0,len(matrix)-1

        for i in matrix[0]:
            result.append(i)
        ceeling_index += 1

        if len(result) == total_length:
            return result

        reversed_bottom = matrix[len(matrix)-1][::-1]

        for i in range(1, len(matrix)-1):
            result.append(matrix[i][right_index])
        right_index -= 1

        for i in reversed_bottom:
            result.append(i)

        def up_stair(bottom: int) -> int:
            tmp = bottom
            while bottom > ceeling_index:
                bottom -= 1
                result.append(matrix[bottom][left_index])
            return tmp - 1

        def right_step(left: int, right: int, ceeling: int) -> int:
            tmpl, tmpr = left, right
            while left < right:
                left += 1
                result.append(matrix[ceeling][left])
            return tmpl + 1

        def left_step(left: int, right: int, bottom: int) -> int:
            tmpl, tmpr = left, right
            while left_index < right:
                right -= 1
                result.append(matrix[bottom][right])
            return tmpr - 1

        def down_stair(ceeling: int) -> int:
            tmpc = ceeling
            while ceeling < bottom_index:
                ceeling += 1
                result.append(matrix[ceeling][right_index])
            return tmpc + 1

        while len(result) < total_length:
            bottom_index = up_stair(bottom_index)
            if len(result) == total_length:
                break
            left_index = right_step(left_index, right_index, ceeling_index)
            if len(result) == total_length:
                break
            ceeling_index = down_stair(ceeling_index)
            if len(result) == total_length:
                break
            right_index = left_step(left_index,right_index, bottom_index)

        return result


if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13,14,15,16]]
    matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
    # matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9],[10,11,12]]
    # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    # matrix = [[1]]
    print(s.spiralOrder(matrix))
