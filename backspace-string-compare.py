from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        split_s, split_t = [i for i in S], [i for i in T]

        def prev_delete(index, source):
            if source[index] == '' and index > 0:
                prev_delete(index-1, source)
            if index != -1:
                source[index] = ''

        def back_space(source) -> List[str]:
            for i, k in enumerate(source):
                if k == '#':
                    source[i] = ''
                    prev_delete(i-1, source)
            return source

        # print(''.join(back_space(split_s)))
        # print(''.join(back_space(split_t)))
        if ''.join(back_space(split_s)) == ''.join(back_space(split_t)):
            return True
        else:
            return False


S = "hd#dp#czsp#####"
T = "hd#dp#czsp#######"
S = "y#fo##f"
T = "y#f#o##f"
s = Solution()
print(s.backspaceCompare(S,T))
