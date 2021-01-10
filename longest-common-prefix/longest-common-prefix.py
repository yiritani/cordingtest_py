from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        min_str_length = 200
        list_length = len(strs)

        for i in strs:
            if min_str_length > len(i):
                min_str_length = len(i)

        char_cnt = 0
        result = ""

        while char_cnt < min_str_length:
            list_cnt = 1
            is_all_same = False
            while list_cnt < list_length:
                if strs[0][char_cnt] == strs[list_cnt][char_cnt]:
                    is_all_same = True
                else:
                    is_all_same = False
                    break
                list_cnt += 1
            if not is_all_same:
                break
            if is_all_same:
                result += strs[0][char_cnt]

            char_cnt += 1

        return result

    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix2("", strs=strs))
