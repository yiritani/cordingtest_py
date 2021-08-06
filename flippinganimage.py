from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for iindex, i in enumerate(image):
            for jindex, j in enumerate(i[::-1]):
                image[iindex][jindex] = -(j - 1)
        return image
