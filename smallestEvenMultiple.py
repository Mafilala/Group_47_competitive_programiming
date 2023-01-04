class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n / 2 == int(n / 2):
            return n
        if 2 > n:
            return 2
        return 2 * n
