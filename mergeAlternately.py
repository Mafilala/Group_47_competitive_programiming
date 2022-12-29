class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        l = min(l1, l2)
        i = 0
        ans = ""
        while i < l:
            ans += word1[i]
            ans += word2[i]
            i += 1
        if l2 > l1:
            ans += word2[i :]
        if l2 < l1:
            ans += word1[i:]
        return ans
