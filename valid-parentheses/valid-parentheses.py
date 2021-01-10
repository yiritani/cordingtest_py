class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {'(':')', '{':'}', '[':']'}

        for i in range(len(s)):
            if s[i] in d:
                st.append(s[i])

            elif len(st) > 0 and s[i] == d[st[len(st)-1]]:
                st.pop()

            else:
                return False

        return (not len(st) > 0)

if __name__ == '__main__':
    print(Solution.isValid("", "()"))
