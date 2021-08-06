class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        result = ''
        cnt = 0
        for i in s:
            if i == ' ':
                cnt += 1
            if cnt == k:
                break
            result += i
        return result


