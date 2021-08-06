class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split = s.split(" ")
        cnt = 1
        while split:
            if len(split[len(split)-cnt]) == 0:
                if cnt == len(split):
                    return 0
                cnt += 1
                continue
            return len(split[len(split)-cnt])

if __name__ == '__main__':
    print(Solution.lengthOfLastWord("","  "))