class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        n = len(max(s, key=len))
        ans = ["" for _ in range(n)]
        for word in s:
            for i in range(n):
                ans[i] += word[i] if i < len(word) else " "
        ans = list(map(str.rstrip, ans))
        return ans
