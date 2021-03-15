
class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = [start]
        for i in range(1, n):
            result.append(result[i-1]+2)

        xor = 0
        for i in result:
            xor = xor ^ i

        return xor






if __name__ == '__main__':
    n = 10
    start = 5
    s = Solution()
    s.xorOperation(n, start)
