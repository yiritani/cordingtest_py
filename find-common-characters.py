from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        result = []
        source = sorted(A[0])
        separated_source = [[] for _ in range(len(A)-1)]
        for i in range(0, len(A)-1):
            for j in sorted(A[i+1]):
                separated_source[i].append(j)

        print(separated_source)

        for i in source:
            all_in = 1
            for j in separated_source:
                if i in j:
                    all_in += 1
            if all_in == len(A):
                result.append(i)
                for s in range(0, len(separated_source)):
                    separated_source[s].pop(s)

        return result


s = Solution()
Input = ["cool","lock","cook"]
print(s.commonChars(Input))