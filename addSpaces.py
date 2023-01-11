class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        prev = 0
        ans = ""
        for idx in spaces:
            ans += s[prev : idx] + " "
            prev = idx
        ans += s[prev : ]
        return ans
