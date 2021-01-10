class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        cnt, i = 0, 0

        while s:
            if len(s) == i:
                break
            if len(s) - 1  == i:
                cnt += romans[s[i]]
                break
            if romans[s[i]] < romans[s[i+1]]:
                cnt += romans[s[i + 1]] - romans[s[i]]
                i += 2

            else:
                cnt += romans[s[i]]
                i += 1

        return cnt


if __name__ == '__main__':
    print(Solution.romanToInt("", "III"))
