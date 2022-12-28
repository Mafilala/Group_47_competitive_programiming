class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        w_map = {}
        for idx, l in  enumerate(order):
            w_map[l] = idx
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j + 1 > len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if w_map[words[i][j]] > w_map[words[i + 1][j]]:
                        return False
                    break
        return True
