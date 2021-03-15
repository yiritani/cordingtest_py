class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        str_day = str(day)
        str_month = str(month)
        str_year = str(year)
        A,B,C=0,0,0

        A = int(str_year[2:])
        if A % 2 != 0:
            A += 11

        B = A / 2
        if B % 2 != 0:
            C = B + 11
        else:
            C = B

        domesDay = C % 7

        print(domesDay)





day = 9
month = 3
year = 2021
s = Solution()
s.dayOfTheWeek(day, month, year)