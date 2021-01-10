class Solution:
    def myPow(self, x: float, n: int) -> float:
        return pow(x,n)



if __name__ == '__main__':
    x = 2.10000
    n = 3
    a = Solution.myPow("",x,n)
    print(a)