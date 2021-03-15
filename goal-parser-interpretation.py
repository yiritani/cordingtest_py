class Solution:
    def interpret(self, command: str) -> str:
        listed_command = [i for i in command]
        result = ''
        for i, k in enumerate(listed_command):
            if k == ')':
                continue
            if k == '(':
                if listed_command[i+1] == ')':
                    result += 'o'
            else:
                result += k

        return result

if __name__ == '__main__':
    s = Solution()
    command = "(al)G(al)()()G"
    print(s.interpret(command))