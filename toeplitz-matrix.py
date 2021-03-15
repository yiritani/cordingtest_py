from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        seikai = True
        for i, v in enumerate(matrix):
            for ii, vv in enumerate(v):
                for j in range(len(matrix)):
                    if len(matrix[0]) <= ii+j or len(matrix) <= i+j:
                        break
                    if matrix[i][ii] != matrix[i+j][ii+j]:
                        return False
                    # print(matrix[i][ii], matrix[i+j][ii+j])
                    # print(i,ii,j,matrix[i][ii])
            else:
                continue

        return seikai

s = Solution()
matrix = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
# matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
print(s.isToeplitzMatrix(matrix))
