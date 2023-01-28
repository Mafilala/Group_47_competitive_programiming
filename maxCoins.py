class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles.sort()
        if n == 3:
            return piles[1]
        st = n // 3
        ans = sum(piles[st : -1 : 2])
        return ans
