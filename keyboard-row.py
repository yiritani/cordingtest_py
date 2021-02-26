from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        upstr, middlestr, bottomstr = "qwertyuiop", "asdfghjkl", "zxcvbnm"
        result = []
        tmpNum = [[] for _ in range(len(words))]

        for index, i in enumerate(words):
            for j in i:
                if j.lower() in upstr:
                    tmpNum[index].append(0)
                elif j.lower() in middlestr:
                    tmpNum[index].append(1)
                elif j.lower() in bottomstr:
                    tmpNum[index].append(2)

        for i, k in enumerate(tmpNum):
            if len(set(k)) == 1:
                result.append(words[i])

        return result

s = Solution()
words = ["adsdf","sfd"]
print(s.findWords(words))