class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = ''
        for i in address:
            if i == '.':
                result += '['+i+']'
            else:
                result += i

        return result


if __name__ == '__main__':
    address = "255.100.50.0"
    s =Solution()
    print(s.defangIPaddr(address))