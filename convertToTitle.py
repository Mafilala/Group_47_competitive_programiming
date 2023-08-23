class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def recurse(c):
            if c < 26:
                return chr(ord('A') + c)

            return recurse(c // 26 - 1) + chr(ord('A') + (c) % 26)
        return recurse(columnNumber - 1)
