class Solution:
    def maximumTime(self, time: str) -> str:
        index = []
        result = ''
        index += ([i for i,k in enumerate(time) if k == '?'])

        for i in range(5):
            if i in index:
                if i == 0:
                    if time[1] == '?':
                        result += '2'
                    elif int(time[1]) > 3:
                        result += '1'
                    else:
                        result += '2'
                elif i == 1:
                    if time[0] == '0':
                        result += '9'
                    elif time[0] == '1':
                        result += '9'
                    else:
                        result += '3'
                elif i == 3:
                    result += '5'
                elif i == 4:
                    result += '9'
            else:
                result += time[i]

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.maximumTime("??:3?"))



