class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def valid(k):
            hrs = 0
            for p in piles:
                if p < k:
                    hrs += 1
                else:
                    hrs += math.ceil(p / k)
            return hrs <= h

        l = 1
        r = max(piles)
        while l < r:
            mid = (l + r) // 2
            if valid(mid):
                r = mid
            else:
                l = mid + 1
        return r
