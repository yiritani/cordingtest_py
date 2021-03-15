class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        result = []
        tmp = ''
        is_twice = False
        for i in s:
            if i in tmp:
                result.append(''.join(tmp))
                tmp = ''
                is_twice = True
            if i not in tmp:
                tmp += i
        else:
            result.append(''.join(tmp))
            if is_twice is False:
                return False

        # print(result)
        if len(list(set(result))) == 1:
            return True

        return False



if __name__ == '__main__':
    s = Solution()
    print(s.repeatedSubstringPattern("aba"))
