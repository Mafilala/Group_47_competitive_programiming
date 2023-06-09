class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        cp = [-s for s in stones]
        heapq.heapify(cp)
        while len(cp) > 1:
            s1 = -heapq.heappop(cp)
            s2 = -heapq.heappop(cp)
            if s1 - s2:
                heapq.heappush(cp, -(s1 - s2))
        return -cp[0] if cp else 0

