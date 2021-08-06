from collections import Counter
import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if len(Counter(sentence)) == len([i for i in string.ascii_lowercase]):
            return True
        else:
            return False
        # ss = []
        # for i in sentence:
        #     ss.append(ord(i))
        #
        # sss = list(set(ss))
        # sss.sort(reverse=True)
        #
        # if len(sss) == 26:
        #     for i in range(1, len(sss)):
        #         if (sss[i-1] - sss[i]) != 1:
        #             return False
        #     else:
        #         return True
        # else:
        #     return False


s = Solution()
sentence = "thequickbrownfoxjumpsoverthelazydog"
print(s.checkIfPangram(sentence))