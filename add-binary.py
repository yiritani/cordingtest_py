class Solution:
    def addBinary(self, a: str, b: str) -> str:
        intsum = int(a,2) + int(b,2)
        binsum = bin(intsum)
        return binsum[2:]


if __name__ == '__main__':
    s = Solution()
    a = "11"
    b = "1"
    print(s.addBinary(a,b))


    # https://leetcode.com/problems/add-binary/