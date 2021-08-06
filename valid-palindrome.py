class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ","", -1)

        normal, reverse = "", ""
        for moji in s:
            if moji.isalnum():
                normal += moji
        s = normal

        str_length = len(normal) - 1
        str_half_length = len(normal) // 2

        normal = normal[:str_half_length]

        while 0 < str_half_length:
            reverse += s[str_length]

            str_length -= 1
            str_half_length -= 1

        if normal == reverse:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    c = "0P"
    print(s.isPalindrome(c))