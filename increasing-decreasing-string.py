from collections import Counter, defaultdict

class Solution:
    def sortString(self, s: str) -> str:
        sNumDict = defaultdict(str)
        print(sNumDict)

        # for i in s:
        #     if sNumDict.get(ord(i)):
        #         sNumDict[ord(i)] += 1
        #     else:
        #         sNumDict[ord(i)] = 0
        # print(sNumDict)





s = Solution()
s.sortString("aaaabbbbcccc")