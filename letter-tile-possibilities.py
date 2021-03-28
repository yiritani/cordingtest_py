from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = []
        ext_duplicate = list(set(tiles))

        for i in tiles:
            if i not in result:
                result.append(i)

        for perm in permutations(tiles):
            for i in range(len(tiles)):
                for j in range(0, len(tiles)+1):
                    tage = ''.join(perm[i:j])
                    if tage not in result and tage != '':
                        result.append(tage)


        print(result)

        return len(result)


s = Solution()
tiles = "ADIUSIQ"
print(s.numTilePossibilities(tiles))
