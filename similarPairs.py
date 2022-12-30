class Solution:
    def similarPairs(self, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            w1 = words[i]
            for w2 in words[i + 1: ]:
                if set(w1) == set(w2):
                    ans += 1
        return ans
